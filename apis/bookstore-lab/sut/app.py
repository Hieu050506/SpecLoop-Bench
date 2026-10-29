"""Bookstore-Lab – REST API thực nghiệm có kiểm soát cho SpecLoop-Bench.

Cài đặt này CỐ Ý khác tài liệu (docs/original.md) ở một số điểm (xem ground_truth/discrepancies.json)
để đo khả năng phát hiện sai lệch ràng buộc từ phản hồi kiểm thử. Không bật /docs, /openapi.json
để API không "lộ" đặc tả hành vi.

Chạy:  uvicorn app:app --port 8000      (hoặc docker compose up bookstore-lab)
"""
from __future__ import annotations

import math
import os
import re
from datetime import date

from fastapi import APIRouter, FastAPI, Header, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse, Response

app = FastAPI(title="Bookstore-Lab", openapi_url=None, docs_url=None, redoc_url=None)
v1 = APIRouter(prefix="/v1")
ADMIN_TOKEN = os.environ.get("BOOKSTORE_ADMIN_TOKEN", "reset-me")
AUTHOR_PAGE_SIZE = 10

GENRES = ["fiction", "science", "history", "children"]          # tài liệu chỉ nêu 3 giá trị đầu (D5)
ISBN_RE = re.compile(r"^[0-9]{13}$")


class ApiError(Exception):
    def __init__(self, status: int, message: str, field: str | None = None):
        self.status, self.message, self.field = status, message, field


@app.exception_handler(ApiError)
async def _api_error(_: Request, e: ApiError):
    return JSONResponse(status_code=e.status, content={"error": e.message, "field": e.field})


@app.exception_handler(RequestValidationError)
async def _validation_error(_: Request, e: RequestValidationError):
    return JSONResponse(status_code=400, content={"error": "invalid request", "field": None})


# ------------------------------------------------------------------ dữ liệu mẫu
def _seed():
    countries = ["UK", "US", "VN", "JP", "FR", "DE", "BR", "IN"]
    authors = [{"id": i, "name": n, "country": countries[(i - 1) % len(countries)]}
               for i, n in enumerate(["Ada Lane", "Bao Tran", "Carla Mendes", "Daichi Sato", "Elise Martin",
                                      "Felix Braun", "Gabriela Souza", "Hari Patel", "Iris Novak", "Jonas Berg",
                                      "Khanh Le", "Lucia Romano"], start=1)]
    books = []
    titles = ["Atlas of Clouds", "Binary Rivers", "City of Glass Ants", "Deep Field", "Echoes of Hue",
              "Fragments of Time", "Garden Physics", "Harbor Lights", "Inner Orbits", "Jade Archive",
              "Kites over Hanoi", "Lost Equations", "Maps of Silence", "Night Bakery", "Ocean Ledger",
              "Paper Engines", "Quiet Numbers", "Red Thread", "Salt and Signal", "Tidal Code",
              "Under the Banyan", "Violet Hours", "Winter Algebra", "Xenon Dreams", "Yellow Kite",
              "Zero Gravity Kitchen", "Amber Logic", "Blue Monsoon", "Copper Moons", "Dune Letters",
              "Ember Theory", "Forest Protocol", "Glass Harbor", "Hidden Primes", "Ivory Coast Notes",
              "Jungle Mathematics", "Kinetic Hearts", "Lantern Street", "Mosaic Mind", "Northbound"]
    for i, t in enumerate(titles, start=1):
        books.append({
            "id": i, "title": t,
            "isbn": None if i % 6 == 0 else f"978{i:010d}",            # bản ghi cũ thiếu ISBN (D8)
            "price": round(5 + (i * 3.7) % 40, 2),
            "genre": GENRES[i % 4] if i % 9 else "children",            # có sách thể loại 'children' (D5)
            "published_at": date(1990 + i % 30, 1 + i % 12, 1 + i % 28).isoformat(),
            "tags": ["bestseller"] if i % 5 == 0 else [],
            "author_id": 1 + i % 12,
        })
    return {"authors": authors, "books": books, "orders": [], "next_book": len(books) + 1, "next_order": 1}


DB = _seed()


# ------------------------------------------------------------------ tiện ích kiểm tra
def q_int(request: Request, name: str, default: int | None = None) -> int | None:
    raw = request.query_params.get(name)
    if raw is None:
        return default
    try:
        return int(raw)
    except ValueError:
        raise ApiError(400, f"{name} must be an integer", name)


def q_enum(request: Request, name: str, allowed: list[str], default: str | None = None) -> str | None:
    raw = request.query_params.get(name)
    if raw is None:
        return default
    if raw not in allowed:
        raise ApiError(400, f"{name} must be one of: {', '.join(allowed)}", name)
    return raw


async def json_body(request: Request) -> dict:
    try:
        body = await request.json()
    except Exception:  # noqa: BLE001
        raise ApiError(400, "request body must be valid JSON", None)
    if not isinstance(body, dict):
        raise ApiError(400, "request body must be a JSON object", None)
    return body


def need(body: dict, name: str):
    if name not in body or body[name] is None:
        raise ApiError(400, f"{name} is required", name)
    return body[name]


def as_int(v, name):
    if isinstance(v, bool) or not isinstance(v, int):
        raise ApiError(400, f"{name} must be an integer", name)
    return v


def as_num(v, name):
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        raise ApiError(400, f"{name} must be a number", name)
    return v


def as_str(v, name):
    if not isinstance(v, str):
        raise ApiError(400, f"{name} must be a string", name)
    return v


def path_id(raw: str, name: str, invalid_status: int = 404, what: str = "resource") -> int:
    try:
        v = int(raw)
    except ValueError:
        v = -1
    if v < 1:
        if invalid_status == 400:
            raise ApiError(400, f"{name} must be a positive integer", name)
        raise ApiError(404, f"{what} not found", None)
    return v


# ------------------------------------------------------------------ Books
@v1.get("/books")
async def list_books(request: Request):
    limit = q_int(request, "limit", 20)
    if not 1 <= limit <= 100:                                         # tài liệu không nêu biên (D1)
        raise ApiError(400, "limit must be between 1 and 100", "limit")
    page = q_int(request, "page", 1)
    if page < 1:
        raise ApiError(400, "page must be greater than or equal to 1", "page")
    sort = q_enum(request, "sort", ["title", "published_at"], "title")  # tài liệu ghi 'Required' (D4)
    order = q_enum(request, "order", ["asc", "desc"], "asc")           # dùng được cả khi không có sort (D2)
    items = sorted(DB["books"], key=lambda b: (b.get(sort) is None, b.get(sort) or ""), reverse=(order == "desc"))
    start = (page - 1) * limit
    return {"items": items[start:start + limit], "total": len(items)}


@v1.get("/books/{book_id}")
async def get_book(book_id: str):
    bid = path_id(book_id, "book_id", invalid_status=400)              # 400/404 không có trong tài liệu (D7)
    for b in DB["books"]:
        if b["id"] == bid:
            return b
    raise ApiError(404, "book not found", None)


@v1.post("/books", status_code=201)
async def create_book(request: Request):
    body = await json_body(request)
    title = as_str(need(body, "title"), "title")
    if not 1 <= len(title) <= 200:                                    # tài liệu không nêu độ dài (D1)
        raise ApiError(400, "title must be between 1 and 200 characters", "title")
    isbn = as_str(need(body, "isbn"), "isbn")
    if not ISBN_RE.match(isbn):
        raise ApiError(400, "isbn must be a 13-digit string", "isbn")
    price = as_num(need(body, "price"), "price")
    if price < 0:                                                     # tài liệu: phải > 0; thực tế nhận 0 (D2)
        raise ApiError(400, "price must be greater than or equal to 0", "price")
    genre = as_str(need(body, "genre"), "genre")
    if genre not in GENRES:
        raise ApiError(400, f"genre must be one of: {', '.join(GENRES)}", "genre")
    author_id = as_int(need(body, "author_id"), "author_id")
    if not any(a["id"] == author_id for a in DB["authors"]):
        raise ApiError(400, "author_id does not refer to an existing author", "author_id")
    if "published_at" in body and body["published_at"] is None:
        raise ApiError(400, "published_at must be a string", "published_at")
    published_at = body.get("published_at")
    if published_at is not None:
        try:
            date.fromisoformat(as_str(published_at, "published_at"))
        except ValueError:
            raise ApiError(400, "published_at must be a date in YYYY-MM-DD format", "published_at")
    tags = body.get("tags", [])
    if tags is None or not isinstance(tags, list) or not all(isinstance(t, str) for t in tags):
        raise ApiError(400, "tags must be an array of strings", "tags")
    if len(tags) > 5:                                                 # tài liệu không nêu (D1)
        raise ApiError(400, "tags must contain at most 5 items", "tags")
    book = {"id": DB["next_book"], "title": title, "isbn": isbn, "price": price, "genre": genre,
            "tags": tags, "author_id": author_id}
    if published_at is not None:
        book["published_at"] = published_at
    DB["next_book"] += 1
    DB["books"].append(book)
    return book


# ------------------------------------------------------------------ Authors
@v1.get("/authors")
async def list_authors(request: Request):
    q = request.query_params.get("q")
    if q is not None and len(q) < 2:
        raise ApiError(400, "q must be at least 2 characters", "q")
    page = q_int(request, "page", 1)
    if page == 0:
        raise ApiError(400, "page must be greater than or equal to 1", "page")
    items = [a for a in DB["authors"] if not q or q.lower() in a["name"].lower()]
    offset = (page - 1) * AUTHOR_PAGE_SIZE
    if offset < 0:
        # LỖI CÀI CẮM (D0): trang âm làm chỉ số vượt phạm vi -> 500 Internal Server Error
        _ = items[offset * 1000]
    return {"items": items[offset:offset + AUTHOR_PAGE_SIZE], "total": len(items)}


@v1.get("/authors/{author_id}")
async def get_author(author_id: str):
    aid = path_id(author_id, "author_id", what="author")
    for a in DB["authors"]:
        if a["id"] == aid:
            return a
    raise ApiError(404, "author not found", None)


# ------------------------------------------------------------------ Orders
@v1.post("/orders", status_code=201)                                  # tài liệu ghi 200 (D7)
async def create_order(request: Request):
    body = await json_body(request)
    book_id = as_int(need(body, "book_id"), "book_id")
    book = next((b for b in DB["books"] if b["id"] == book_id), None)
    if book is None:
        raise ApiError(400, "book_id does not refer to an existing book", "book_id")
    quantity = as_int(need(body, "quantity"), "quantity")
    if not 1 <= quantity <= 10:
        raise ApiError(400, "quantity must be between 1 and 10", "quantity")
    for opt in ("coupon_code", "voucher_type"):
        if opt in body and body[opt] is None:
            raise ApiError(400, f"{opt} must be a string", opt)
    coupon = body.get("coupon_code")
    vtype = body.get("voucher_type")
    if coupon is not None:
        as_str(coupon, "coupon_code")
        if vtype is None:                                             # phụ thuộc không có trong tài liệu (D9)
            raise ApiError(400, "voucher_type is required when coupon_code is provided", "voucher_type")
    if vtype is not None and vtype not in ("percent", "fixed"):
        raise ApiError(400, "voucher_type must be one of: percent, fixed", "voucher_type")
    total = round(book["price"] * quantity, 2)
    if not math.isfinite(total):                                      # ràng buộc ngữ nghĩa, không biểu diễn được bằng OAS
        raise ApiError(400, "total_price is out of range", "quantity")
    if coupon is not None:
        total = round(total * 0.9, 2) if vtype == "percent" else max(0.0, round(total - 2, 2))
    order = {"id": DB["next_order"], "book_id": book_id, "quantity": quantity, "total_price": total,
             "status": "pending", "coupon_code": coupon}
    DB["next_order"] += 1
    DB["orders"].append(order)
    return order


@v1.get("/orders/{order_id}")
async def get_order(order_id: str):
    oid = path_id(order_id, "order_id", what="order")
    for o in DB["orders"]:
        if o["id"] == oid:
            return o
    raise ApiError(404, "order not found", None)


@v1.delete("/orders/{order_id}", status_code=204)
async def cancel_order(order_id: str):
    oid = path_id(order_id, "order_id", what="order")
    for o in DB["orders"]:
        if o["id"] == oid:
            DB["orders"].remove(o)                                    # hủy = xóa khỏi hệ thống
            return Response(status_code=204)
    raise ApiError(404, "order not found", None)


# ------------------------------------------------------------------ vận hành (không thuộc tài liệu)
@app.get("/health")
async def health():
    return {"status": "ok"}


@app.post("/__admin/reset")
async def reset(x_admin_token: str | None = Header(default=None)):
    if x_admin_token != ADMIN_TOKEN:
        raise HTTPException(status_code=403, detail="forbidden")
    global DB
    DB = _seed()
    return {"status": "reset"}


app.include_router(v1)
