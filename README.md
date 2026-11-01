# SpecLoop-Bench v0.1 – Bộ dữ liệu thực nghiệm

Bộ dữ liệu phục vụ đề tài NCKH *“Xây dựng hệ thống web sinh đặc tả OpenAPI từ tài liệu REST API bằng mô hình
ngôn ngữ lớn và tinh chỉnh ràng buộc dựa trên phản hồi kiểm thử API”*.

Mỗi API trong bộ dữ liệu gồm ba thứ:

1. **Tài liệu đầu vào** cho hệ thống (LLM đọc tài liệu → sinh OpenAPI).
2. **Ground truth (GT)** để chấm điểm: đặc tả OpenAPI 3.0.3 chuẩn và danh sách *atomic facts* sinh tự động.
3. **Thông tin môi trường chạy** để kiểm thử thật và thu phản hồi (URL, xác thực, phạm vi được phép).

Bộ dữ liệu trả lời được ba câu hỏi nghiên cứu: **RQ1** chất lượng OAS sinh từ tài liệu, **RQ2** độ chính xác khi
phát hiện sai lệch ràng buộc từ phản hồi kiểm thử, **RQ3** mức cải thiện sau khi tinh chỉnh.

## 1. Tổng quan

| API | Nhóm | Môi trường | Kiểm thử | Op | Tham số | Ràng buộc* | Facts | Tài liệu gốc | Lược RB | GT hành vi |
|---|---|---|---|---:|---:|---:|---:|---|---:|---|
| `bookstore-lab` | A | Docker cục bộ | đầy đủ | 8 | 10 | 98 | 285 | có | 10 | chính xác |
| `fdic` | B | Công khai | chỉ đọc | 6 | 73 | 104 | 3977 | – | – | chờ xác minh |
| `genome-nexus` | B | Công khai | chỉ đọc | 23 | 34 | 572 | 3984 | – | – | chờ xác minh |
| `httpbin` | A | Docker cục bộ | đầy đủ | 78 | 63 | 59 | 373 | – | 1 | chờ xác minh |
| `jikan` | B | Công khai | chỉ đọc | 100 | 221 | 673 | 5112 | – | – | chờ xác minh |
| `language-tool` | B | Công khai | chỉ đọc | 2 | 0 | 6 | 39 | – | – | chờ xác minh |
| `nws-weather` | B | Công khai | chỉ đọc | 69 | 185 | 1752 | 5412 | – | – | chờ xác minh |
| `ohsome` | B | Công khai | chỉ đọc | 122 | 1488 | 2262 | 11642 | – | – | chờ xác minh |
| `omdb` | B | Công khai | chỉ đọc | 1 | 9 | 9 | 112 | – | – | chờ xác minh |
| `opendota` | B | Công khai | chỉ đọc | 55 | 235 | 142 | 2018 | – | – | chờ xác minh |
| `petstore3` | A | Docker cục bộ | đầy đủ | 19 | 17 | 98 | 521 | – | 4 | chờ xác minh |
| `pokeapi` | B | Công khai | chỉ đọc | 102 | 200 | 2291 | 5643 | – | – | chờ xác minh |
| `postcodes-io` | B | Công khai | chỉ đọc | 11 | 14 | 1067 | 2274 | – | – | chờ xác minh |
| `qdrant` | A | Docker cục bộ | đầy đủ | 69 | 160 | 3011 | 7874 | – | 195 | chờ xác minh |
| `realworld-conduit` | A | Docker cục bộ | đầy đủ | 19 | 19 | 309 | 924 | có | 8 | chờ xác minh |
| `rest-countries` | B | Ngoại tuyến | không | 21 | 42 | 19 | 166 | – | – | chờ xác minh |
| `spaceflight-news` | B | Công khai | chỉ đọc | 7 | 73 | 169 | 535 | – | – | chờ xác minh |
| `spring-petclinic` | A | Docker cục bộ | đầy đủ | 37 | 31 | 2137 | 4355 | – | 72 | chờ xác minh |
| `typesense` | A | Docker cục bộ | đầy đủ | 79 | 72 | 594 | 4566 | – | 26 | chờ xác minh |
| `wikimedia-rest` | B | Công khai | chỉ đọc | 49 | 90 | 322 | 1981 | – | – | chờ xác minh |
| **Tổng (20 API)** | | | | **877** | **3036** | **15694** | **61793** | | **316** | |

\* Ràng buộc không tính từ khóa `type`. Số liệu chi tiết: `stats.csv`, `manifest.json`.

- **Nhóm A** (7 API) – chạy cục bộ bằng Docker, được phép gọi mọi phương thức. `bookstore-lab` do nhóm tự xây dựng, có
  **13 sai lệch tài liệu – cài đặt được cài cắm có chủ đích** (mã D0–D9) và **10 ràng buộc đối chứng**, kèm GT hành vi
  chính xác. Các API còn lại là phần mềm mở có đặc tả chính thức, thuộc các lĩnh vực khác nhau: Petstore (mẫu chuẩn),
  RealWorld Conduit (blog), Spring PetClinic (nghiệp vụ CRUD), httpbin (dịch vụ thử HTTP), Typesense (máy tìm kiếm),
  Qdrant (cơ sở dữ liệu vector).
- **Nhóm B** (13 API) – API công khai, chỉ gọi phương thức đọc với tốc độ thấp (≤ 1 req/s). Sáu API đầu lấy đặc tả từ
  kho NLP2REST (ISSTA 2023); bảy API thêm đợt 11/2026 lấy đặc tả do chính nhà cung cấp công bố (thời tiết NWS, PokéAPI,
  OpenDota, Spaceflight News, Jikan, Postcodes.io, Wikimedia REST) – đa dạng về cỡ (7–102 operation) và kiểu ràng buộc
  (pattern, enum, min/max, phân trang).
- `rest-countries`: nhà cung cấp đã gỡ các phiên bản v2/v3 nên chỉ dùng cho RQ1 (đánh giá trích xuất).
- Mỗi API ghi rõ giấy phép, URL đặc tả gốc, ngày lấy và các bước chuẩn hóa trong `meta.yaml`; bản gốc chưa chuẩn hóa
  nằm trong `source/`.

## 2. Cấu trúc thư mục

```
SpecLoop-Bench/
├── README.md               # tài liệu này
├── manifest.json           # danh sách API, thống kê, mã băm SHA-256 của mọi tệp
├── stats.csv               # bảng thống kê
├── docker-compose.sut.yml  # chạy các API nhóm A
├── apis/
│   ├── _template/          # mẫu để thêm API thủ công
│   └── <id>/
│       ├── meta.yaml                   # nguồn, giấy phép, môi trường, phạm vi kiểm thử
│       ├── source/                     # đặc tả gốc như khi tải về (chưa chuẩn hóa)
│       ├── docs/
│       │   ├── original.md             # tài liệu gốc viết cho con người (nếu có)
│       │   ├── rendered.md             # tài liệu dạng trang Swagger UI, sinh từ GT
│       │   └── ablated.md              # bản đã lược ~40% ràng buộc đầu vào (nhóm A)
│       ├── ground_truth/
│       │   ├── openapi.yaml            # GT theo tài liệu (OpenAPI 3.0.3)
│       │   ├── facts.jsonl             # atomic facts sinh từ openapi.yaml
│       │   ├── ablation.json           # ràng buộc nào bị ẩn trong ablated.md
│       │   ├── behavior_openapi.yaml   # GT theo hành vi thật (bookstore-lab)
│       │   ├── behavior_facts.jsonl
│       │   └── discrepancies.json      # danh sách sai lệch cài cắm + probe tái hiện
│       └── sut/                        # (bookstore-lab) mã nguồn API, Dockerfile, test hành vi
└── tools/                  # công cụ dựng, kiểm tra, chấm điểm, thêm API
```

## 3. Atomic facts

Mỗi đặc tả được phân rã thành 7 nhóm fact: `endpoint`, `parameter`, `request_body`, `request_field`, `response`,
`response_field`, `constraint`. Ví dụ một dòng trong `facts.jsonl`:

```json
{"id": "9db865092a62", "category": "constraint", "op": "POST /v1/orders", "location": "body:quantity",
 "name": "quantity", "keyword": "minimum", "value": 1,
 "key": "constraint|POST /v1/orders|body:quantity|quantity|minimum"}
```

Quy ước so khớp: đường dẫn ghép base path của `servers` và bỏ tên biến (`{id}` ≡ `{bookId}`); enum so như tập hợp;
fact `constraint` chỉ đúng khi trùng cả vị trí lẫn giá trị.

## 4. Cài đặt và lệnh thường dùng

```bash
pip install -r tools/requirements.txt

python tools/build_dataset.py                 # dựng lại facts, tài liệu render, manifest, stats
python tools/validate_dataset.py              # kiểm tra toàn vẹn (phải ra "KẾT QUẢ: ĐẠT")

# Chấm một đặc tả do hệ thống sinh ra so với GT
python tools/evaluate.py --api bookstore-lab --pred ket_qua/bookstore_v0.yaml --no-type
python tools/evaluate.py --api bookstore-lab --gt-kind behavior --pred ket_qua/bookstore_v2.yaml --report bao_cao.json

# Kiểm tra API công khai còn truy cập được (chạy trên máy có Internet)
export OMDB_API_KEY=...                       # nếu dùng OMDb (PowerShell: $env:OMDB_API_KEY="...")
python tools/check_connectivity.py --update-meta
```

> **Windows:** các lệnh nhiều dòng dùng dấu `\` để xuống dòng là cú pháp bash. Trên PowerShell hãy thay `\` bằng
> dấu backtick, hoặc viết cả lệnh trên một dòng.

Chạy các API nhóm A bằng Docker (cổng ghi trong `docker-compose.sut.yml` và `meta.yaml` của từng API):

```bash
docker compose -f docker-compose.sut.yml up -d          # bookstore-lab 8000, petstore3 8080, spring-petclinic 9966,
                                                         # httpbin 8800, typesense 8108 (khóa: specloop), qdrant 6343
export TYPESENSE_API_KEY=specloop                        # PowerShell: $env:TYPESENSE_API_KEY="specloop"
python tools/check_connectivity.py --update-meta         # mỗi API trả 2xx -> connectivity_checked: true
```

### Xem danh sách API trên trình duyệt

Từ thư mục gốc của repo, chạy bằng PowerShell:

```powershell
# Chỉ cần tạo môi trường và cài thư viện ở lần đầu
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install fastapi uvicorn pyyaml

# Khởi động giao diện xem dataset
.\.venv\Scripts\python.exe tools/view_dataset.py
```

Mở **http://127.0.0.1:8765** để xem 20 API, tìm endpoint theo phương thức/đường dẫn,
đọc tham số, cấu trúc request, các phản hồi được khai báo, tài liệu và OpenAPI JSON.
Giao diện đọc các thư mục API thực tế; không cần khởi động các dịch vụ Docker để xem dữ liệu.
Có thể đổi cổng bằng `--port 8766`; nhấn `Ctrl+C` ở terminal để dừng.

Đây là trang xem tài liệu và đặc tả. Bấm vào endpoint chỉ mở nội dung được khai báo trong dataset,
chưa gửi request tới máy chủ API và chưa nhận phản hồi thật. Trang Swagger UI mở riêng cần Internet
để tải thư viện giao diện; chức năng gửi request đang tắt. Muốn kiểm thử API thật, cần khởi động dịch vụ
tương ứng và dùng công cụ gửi request.

Mã giao diện nằm ở `tools/view_dataset.py` và `tools/dataset_viewer.html`.

Chạy Bookstore-Lab và test hành vi:

```bash
cd apis/bookstore-lab/sut
pip install -r requirements.txt && uvicorn app:app --port 8000      # hoặc: docker compose -f ../../../docker-compose.sut.yml up -d bookstore-lab
pytest -q test_behavior.py                                          # 20 test phải đạt
curl "http://localhost:8000/v1/books?limit=101"                      # {"error":"limit must be between 1 and 100",...}
curl -X POST -H "X-Admin-Token: reset-me" http://localhost:8000/__admin/reset   # khôi phục dữ liệu mẫu
```

## 5. Thêm API mới

### 5.1. Tiêu chí chọn API

- Có đặc tả **OpenAPI 3.x** đáng tin cậy (do nhà cung cấp công bố hoặc được bảo trì) để làm GT.
- Có **tài liệu cho người đọc** (trang docs, README). Nếu chỉ có trang Swagger UI thì dùng bản `rendered.md`.
- Có **môi trường được phép kiểm thử**: tự chạy bằng Docker (ưu tiên) hoặc API công khai cho phép gọi tự động.
- Điều khoản sử dụng cho phép dùng cho nghiên cứu; ghi rõ giấy phép vào `meta.yaml`.
- Đa dạng: ưu tiên API có nhiều ràng buộc (enum, min/max, pattern, phụ thuộc tham số) và cỡ khác nhau.

Nguồn gợi ý: [APIs.guru openapi-directory](https://github.com/APIs-guru/openapi-directory) (hàng nghìn đặc tả),
EvoMaster Benchmark (EMB – API chạy cục bộ), kho NLP2REST, trang docs của các dịch vụ mở.

### 5.2. Cách nhanh – dùng `add_api.py`

```bash
python tools/add_api.py --id apis-guru --name "APIs.guru" --group B \
  --spec https://raw.githubusercontent.com/APIs-guru/openapi-directory/main/APIs/apis.guru/2.2.0/openapi.yaml \
  --base-url https://api.apis.guru/v2 --env public --scope read-only \
  --license "CC0-1.0" --source-url https://apis.guru --docs-url https://apis.guru/api-doc/
```

Tham số quan trọng:

| Tham số | Ý nghĩa |
|---|---|
| `--id` | tên thư mục, chữ thường + số + gạch nối |
| `--group` | `A` (tự triển khai, kiểm thử đầy đủ) hoặc `B` (công khai) |
| `--spec` | tệp hoặc URL tới OpenAPI 3.0/3.1 (YAML/JSON) |
| `--base-url` | URL dùng khi kiểm thử (ghi đè `servers`) |
| `--env` / `--scope` | `local-docker`/`public`/`offline` và `full`/`read-only`/`none` |
| `--auth`, `--auth-env` | kiểu xác thực và tên biến môi trường chứa khóa |
| `--doc-original` | tài liệu gốc (HTML/MD/PDF/TXT) – đường dẫn hoặc URL |
| `--ablated` | sinh thêm bản tài liệu lược ràng buộc (nên bật cho nhóm A) |

Script tự động: lưu đặc tả gốc vào `source/`, chuẩn hóa về OpenAPI 3.0.3 (hạ cấp 3.1, sửa mã phản hồi dạng số),
sinh `meta.yaml`, `facts.jsonl`, `rendered.md`, cập nhật `manifest.json` rồi chạy kiểm tra.
**Sau đó mở `meta.yaml` điền các mục còn ghi TODO** (mô tả, giấy phép, probe kết nối) và chạy lại
`python tools/build_dataset.py --api <id>`.

### 5.3. Cách thủ công

1. Sao chép `apis/_template/` thành `apis/<id>/`.
2. Đặt đặc tả gốc vào `source/`, bản đã chuẩn hóa 3.0.3 vào `ground_truth/openapi.yaml`.
3. Đặt tài liệu gốc (nếu có) vào `docs/original.md` (hoặc `.html`).
4. Điền `meta.yaml`, chạy `build_dataset.py` và `validate_dataset.py`.

### 5.4. Trường hợp đặc biệt

- **Swagger 2.0**: chuyển sang OpenAPI 3 trước bằng công cụ kèm theo (không cần Node.js):
  `python tools/swagger2_to_oas3.py swagger.json -o openapi.yaml` (body/formData → requestBody, definitions →
  components, host/basePath → servers), rồi chạy `add_api.py` với tệp đã chuyển. `httpbin` được thêm theo cách này.
- **Đặc tả gốc chưa hợp lệ OAS 3.0** (gặp ở nhiều đặc tả tự sinh): tên kiểu không chuẩn (`int`, `float`), số hoặc
  boolean viết dạng chuỗi (`minimum: '1'`, `default: 'false'`), regex dùng lớp Unicode `\p{L}`, thiếu khai báo tham số
  path, trường lạ trong `info.contact`, từ khóa JSON Schema 2020-12 (`patternProperties`, `if/then`…). Sửa tối thiểu
  để hợp lệ và **ghi từng thay đổi vào `source.normalization`** của `meta.yaml` (xem các API thêm đợt 11/2026).
- **Tài liệu gốc chỉ có trên web**: mở trang docs, lưu dạng “Webpage, HTML only” (Ctrl+S) hoặc sao chép nội dung
  sang `docs/original.md`, ghi URL và ngày lấy vào `meta.yaml`.
- **Xác minh GT hành vi**: khi đã kiểm chứng hành vi thật (bằng probe/thủ công), tạo `ground_truth/behavior_openapi.yaml`,
  đặt `ground_truth.behavior` và `behavior_status: partial|exact`, ghi người xác minh vào `verified_by`.

### 5.5. Checklist trước khi nộp/commit

- [ ] `python tools/validate_dataset.py` ra **ĐẠT**, không còn TODO trong `meta.yaml`.
- [ ] Đã ghi nguồn, giấy phép, ngày lấy dữ liệu, các bước chuẩn hóa.
- [ ] API công khai: đã chạy `check_connectivity.py`; đặt `rate_limit_rps` thấp; không dùng phương thức ghi.
- [ ] Không đưa khóa API/token vào bất kỳ tệp nào (chỉ dùng biến môi trường).

## 6. Kiểm chứng ban đầu

- `validate_dataset.py`: 20/20 API đạt; mọi GT hợp lệ OpenAPI 3.0.3. `check_connectivity.py` (01/11/2026): 10/10 API
  công khai có probe trả 200 (Jikan bị timeout từ mạng thử nghiệm – xem `meta.yaml`), 6/6 API Docker nhóm A trả 200.
- Bookstore-Lab: 20/20 test hành vi đạt; mọi probe trong `discrepancies.json` tái hiện đúng.
- **Mốc tham chiếu:** nếu hệ thống trích xuất *hoàn hảo* tài liệu Bookstore-Lab (lấy chính doc-GT làm đặc tả sinh ra)
  rồi chấm theo GT hành vi, F1 nhóm ràng buộc chỉ đạt **0,81** (micro F1 0,86, không tính `type`). Phần chênh này là
  thứ chỉ phản hồi kiểm thử mới bù được – đúng mục tiêu RQ2/RQ3.
- Chạy Schemathesis 45 giây lên Bookstore-Lab (`sut/sanity/`): với doc-GT phát hiện các nhóm sai lệch cài cắm
  (mã trạng thái chưa khai báo, phản hồi lệch schema, tham số bắt buộc giả, biên `limit`…); với behavior-GT chỉ còn
  lỗi D0 cài cắm, ràng buộc tham chiếu (`non_expressible`) và phụ thuộc `x-dependencies` mà Schemathesis không hiểu.

## 7. Hạn chế đã biết

Đánh giá chi tiết: [review bản 20 API](REVIEW_DATASET_20_API.vi.md),
[hướng dẫn xây dựng dataset](HUONG_DAN_XAY_DUNG_DATASET.vi.md).
[Review bản 9 API](REVIEW.vi.md) ghi lại trạng thái kiểm tra ngày 28/10/2026.

- Nhóm B mới có GT theo tài liệu; GT hành vi cần xác minh dần (trường `behavior_status`).
- `rendered.md` sinh từ chính GT nên “dễ” hơn tài liệu viết tay; báo cáo kết quả tách riêng theo loại tài liệu.
- API công khai có thể thay đổi theo thời gian: ghi ngày chạy và lưu vết request/response khi thực nghiệm.
- Ràng buộc tham chiếu (id phải tồn tại) không biểu diễn được bằng OpenAPI – liệt kê ở `non_expressible`.
- `ohsome` rất lớn (~73 nghìn từ tài liệu render) – bắt buộc phân đoạn, có thể dùng tập con operation.

## 8. Nguồn và giấy phép

- Swagger Petstore v3 – https://github.com/swagger-api/swagger-petstore (Apache-2.0).
- RealWorld – https://github.com/gothinkster/realworld (MIT), commit `ebbcdeb`.
- FDIC, Genome Nexus, LanguageTool, ohsome, OMDb, REST Countries – đặc tả lấy từ
  https://github.com/codingsoo/nlp2rest (commit `ae3783b7`), đã đổi `servers` sang URL công khai hiện hành.
  Kim et al., *Enhancing REST API Testing with NLP Techniques*, ISSTA 2023.
- Đợt mở rộng 11/2026 (đặc tả do nhà cung cấp công bố, URL và ngày lấy ghi trong `meta.yaml`):
  Spring PetClinic REST (Apache-2.0), httpbin (ISC), Typesense (GPL-3.0), Qdrant (Apache-2.0),
  NWS weather.gov (public domain), PokéAPI (BSD-3-Clause), OpenDota (MIT), Spaceflight News – The Space Devs
  (miễn phí, ghi nguồn), Jikan (MIT), Postcodes.io (MIT), Wikimedia REST (Apache-2.0; nội dung CC BY-SA).
- Bookstore-Lab, công cụ trong `tools/` – sản phẩm của đề tài.
