"""Kiểm thử hành vi Bookstore-Lab: mọi probe trong discrepancies phải tái hiện đúng, các ràng buộc
'controls' phải khớp tài liệu. Chạy: pytest -q sut/test_behavior.py"""
from pathlib import Path

import pytest
import yaml
from fastapi.testclient import TestClient

import app as bookstore

HERE = Path(__file__).resolve().parent
SRC = yaml.safe_load((HERE.parent / "ground_truth" / "discrepancies.src.yaml").read_text(encoding="utf-8"))


@pytest.fixture()
def client():
    bookstore.DB = bookstore._seed()
    with TestClient(bookstore.app, raise_server_exceptions=False) as c:
        yield c


def _fill(body):
    if isinstance(body, dict):
        return {k: ("x" * 201 if v == "<201 ký tự>" else v) for k, v in body.items()}
    return body


@pytest.mark.parametrize("d", SRC["discrepancies"], ids=[d["id"] for d in SRC["discrepancies"]])
def test_discrepancy_probe(client, d):
    p = d["probe"]
    r = client.request(p["method"], "/v1" + p["path"], params=p.get("query"), json=_fill(p.get("body")))
    assert r.status_code == p["expect_status"], r.text
    if "expect_message" in p:
        assert r.json()["error"] == p["expect_message"]
    for k, v in (p.get("expect_body") or {}).items():
        assert r.json()[k] == v


def test_limit_boundaries(client):
    assert client.get("/v1/books", params={"limit": 100}).status_code == 200
    assert client.get("/v1/books", params={"limit": 1}).status_code == 200
    assert client.get("/v1/books", params={"limit": 0}).status_code == 400


def test_controls_match_docs(client):
    assert client.get("/v1/books", params={"page": 0}).status_code == 400
    assert client.get("/v1/books", params={"sort": "price"}).status_code == 400
    assert client.get("/v1/books", params={"order": "up"}).status_code == 400
    assert client.get("/v1/authors", params={"q": "a"}).status_code == 400
    assert client.get("/v1/authors", params={"q": "an"}).status_code == 200
    base = {"title": "T", "price": 1, "genre": "fiction", "author_id": 1}
    assert client.post("/v1/books", json={**base, "isbn": "123"}).status_code == 400
    assert client.post("/v1/orders", json={"book_id": 1, "quantity": 11}).status_code == 400
    assert client.post("/v1/orders", json={"book_id": 1, "quantity": 0}).status_code == 400
    assert client.post("/v1/orders", json={"book_id": 1, "quantity": 10}).status_code == 201
    assert client.post("/v1/orders", json={"book_id": 1, "quantity": 1, "coupon_code": "S",
                                           "voucher_type": "bogus"}).status_code == 400
    assert client.get("/v1/authors/999").status_code == 404
    assert client.get("/v1/orders/999").status_code == 404


def test_price_strictly_negative_rejected(client):
    r = client.post("/v1/books", json={"title": "N", "isbn": "9780000000009", "price": -0.01,
                                       "genre": "fiction", "author_id": 1})
    assert r.status_code == 400 and r.json()["error"] == "price must be greater than or equal to 0"


def test_order_lifecycle(client):
    o = client.post("/v1/orders", json={"book_id": 2, "quantity": 2, "coupon_code": "SALE",
                                        "voucher_type": "percent"}).json()
    assert o["status"] == "pending" and o["coupon_code"] == "SALE"
    assert client.get(f"/v1/orders/{o['id']}").json()["id"] == o["id"]
    assert client.delete(f"/v1/orders/{o['id']}").status_code == 204
    assert client.get(f"/v1/orders/{o['id']}").status_code == 404


def test_explicit_null_rejected(client):
    base = {"title": "T", "isbn": "9780000000011", "price": 1, "genre": "fiction", "author_id": 1}
    assert client.post("/v1/books", json={**base, "published_at": None}).status_code == 400
    assert client.post("/v1/orders", json={"book_id": 1, "quantity": 1, "coupon_code": None}).status_code == 400


def test_no_spec_exposed(client):
    assert client.get("/openapi.json").status_code == 404
    assert client.get("/docs").status_code == 404


def test_admin_reset(client):
    client.post("/v1/books", json={"title": "Z", "isbn": "9780000000010", "price": 1, "genre": "fiction", "author_id": 1})
    assert client.post("/__admin/reset").status_code == 403
    assert client.post("/__admin/reset", headers={"X-Admin-Token": "reset-me"}).status_code == 200
    assert client.get("/v1/books").json()["total"] == 40
