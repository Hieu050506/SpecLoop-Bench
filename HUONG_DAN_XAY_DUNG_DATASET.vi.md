# Hướng dẫn xây dựng dataset REST API theo cấu trúc SpecLoop-Bench

Hướng dẫn từ chọn nguồn và cào dữ liệu đến gắn nhãn, kiểm chứng, chia tập và phát hành. Ví dụ xuyên suốt dùng API giả định `library-demo`. URL trong ví dụ phải thay bằng nguồn thực tế; các lệnh là hướng dẫn, không phải các tác vụ đã được chạy.

## 1. Xác định dataset dùng để đo điều gì

Với bài toán của SpecLoop-Bench, một mẫu cấp API gồm:

```text
Tài liệu đầu vào + đáp án theo tài liệu + thông tin môi trường
               + đáp án hành vi và nhãn sai lệch nếu đánh giá runtime
```

Chốt trước các câu hỏi:

| Mục tiêu | Dữ liệu bắt buộc |
|---|---|
| Đánh giá sinh OpenAPI từ tài liệu | Tài liệu đầu vào và doc-GT có căn cứ |
| Đánh giá phát hiện sai lệch | Thêm API có thể kiểm thử, nhãn sai lệch và bằng chứng tái hiện |
| Đánh giá cải thiện sau phản hồi | Thêm behavior-GT đã xác minh và quy ước so sánh trước/sau |

Không phải API nào cũng phải đủ cả ba mục tiêu. Một API offline vẫn là mẫu hợp lệ cho đánh giá tài liệu nếu được đánh dấu đúng phạm vi.

Đơn vị thu thập ban đầu là API và phiên bản của nó. Đơn vị gắn nhãn là operation, field hoặc ràng buộc. Các facts sinh ra từ cùng schema không phải các mẫu độc lập.

**Đầu ra:** bản mô tả mục tiêu, đơn vị dữ liệu, phạm vi metric và tiêu chí nhận/loại API.

## 2. Lập danh sách nguồn trước khi cào

Tạo `candidates.csv`, ví dụ các cột:

```csv
id,docs_url,spec_url,api_version,source_revision,environment,auth,status,reason
```

Với mỗi ứng viên, tìm ba nguồn riêng: tài liệu người dùng, đặc tả OpenAPI/Swagger, và máy chủ hoặc mã triển khai. Tìm trong website chính thức và repository của dự án. Ghi URL tệp gốc và commit/tag cụ thể khi có; liên kết nhánh `main` đơn thuần không xác định một phiên bản cố định.

Ưu tiên ứng viên có tài liệu rõ, spec đáng tin, nguồn được phép sử dụng và môi trường thử được trong phạm vi đề tài. Tạo tập đa dạng về lĩnh vực, quy mô, kiểu tham số, body, auth và ràng buộc. Ghi cả lý do loại ứng viên để giải thích cách chọn mẫu.

Nếu chỉ có Swagger UI sinh từ spec, vẫn có thể nhận nhưng ghi là tài liệu sinh tự động. Không coi đó là tài liệu viết tay độc lập.

**Đầu ra:** danh sách ứng viên và danh sách được chọn, mỗi ứng viên có phiên bản/nguồn rõ.

## 3. Chuẩn bị khu vực dữ liệu thô

Tách bản tải về và bản sẽ làm sạch:

```text
staging/library-demo/
  raw_docs/                    # HTML/MD/PDF gốc
  openapi_original.yaml       # tải nguyên bản, chưa chuẩn hóa
  crawl_manifest.jsonl        # nguồn và kết quả tải
  docs_clean.md               # bản tài liệu đã làm sạch
```

`staging/` là khu vực chuẩn bị đề xuất; không phải thư mục mà công cụ hiện tại tự tạo. Một lần thu thập nên có mã snapshot riêng hoặc thư mục theo phiên bản để không ghi đè bản cũ.

Mỗi bản tải cần lưu URL yêu cầu, URL sau redirect, thời điểm UTC, HTTP status, content type, đường dẫn cục bộ, SHA-256, API version và commit/tag nếu có. URL chứa khóa truy cập phải được làm sạch trước khi ghi log.

Ví dụ bản ghi:

```json
{"api_id":"library-demo","url":"https://docs.example.org/v1/books","retrieved_at":"2026-10-28T03:00:00Z","status":200,"local_file":"raw_docs/books.html","sha256":"<sha256-thuc-te>","api_version":"v1"}
```

**Đầu ra:** nơi lưu snapshot và quy ước ghi nguồn thống nhất.

## 4. Cào tài liệu và tải spec

Thu thập hai nhánh độc lập:

| Nhánh | Cần lấy | Mục đích |
|---|---|---|
| Tài liệu cho con người | Overview, auth, convention, từng endpoint, schema, lỗi, ví dụ và phân trang | Đầu vào của mô hình |
| Đặc tả | OpenAPI JSON/YAML và các tệp được `$ref` tham chiếu | Nguồn để xây đáp án |

Tải spec trực tiếp nếu đã có URL tệp; không cần cào HTML để dựng lại một spec đã được cung cấp. Với trang HTML tĩnh có thể dùng Scrapy. Với trang chỉ hiện đầy đủ sau JavaScript, có thể dùng Playwright để lấy DOM sau khi phần nội dung cần thiết đã xuất hiện; giữ cả bản gốc và bản render nếu cần đối chiếu.

Lập danh sách trang seed rõ ràng. Nếu theo link tự động, giới hạn domain và prefix phiên bản, bỏ fragment khi khử trùng URL nhưng không tùy tiện bỏ query có ý nghĩa. Không lẫn docs v1/v2 hoặc các ngôn ngữ khác nhau. Nếu spec chia nhiều file, lưu đủ cây tham chiếu và giữ đường dẫn tương đối; resolver hiện tại của SpecLoop-Bench chỉ hỗ trợ `$ref` nội bộ nên cần bước bundle có kiểm tra trước khi nhập.

Cấu hình bắt đầu có thể dùng trong Scrapy:

```python
custom_settings = {
    "ROBOTSTXT_OBEY": True,
    "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
    "DOWNLOAD_DELAY": 1.0,
    "AUTOTHROTTLE_ENABLED": True,
}
```

Điều chỉnh tốc độ theo phạm vi được phép của nguồn. Lưu danh sách URL thất bại; không nhận nhầm trang login, trang lỗi hoặc nội dung chỉ có menu là tài liệu hoàn chỉnh. Việc tải thành công một trang overview chưa chứng minh đã lấy đủ tài liệu API.

Nguồn kỹ thuật: [Scrapy Tutorial](https://docs.scrapy.org/en/latest/intro/tutorial.html), [robots.txt settings](https://docs.scrapy.org/en/latest/topics/settings.html#robotstxt-obey), [AutoThrottle](https://docs.scrapy.org/en/latest/topics/autothrottle.html), [Playwright Python](https://playwright.dev/python/docs/intro).

**Đầu ra:** snapshot tài liệu thô, spec nguyên bản, crawl manifest và danh sách lỗi tải.

## 5. Làm sạch và kiểm tra độ đầy đủ của tài liệu

Loại bỏ menu lặp, footer, quảng cáo, widget và nội dung không liên quan. Giữ nguyên heading, HTTP method/path, bảng tham số, dấu so sánh, enum, required/optional, ví dụ JSON, mã trạng thái, đơn vị và các điều kiện phụ thuộc. Đừng chuyển bảng thành một chuỗi văn bản mất quan hệ cột.

Chuyển HTML hoặc PDF sang Markdown/text để xử lý, giữ URL và heading nguồn cho từng phần. Với PDF scan cần OCR và kiểm tra lại dấu, số và tên field. Không để LLM tự bổ sung ràng buộc trong lúc làm sạch. Nếu dùng LLM hỗ trợ, so lại với bản thô và lưu dấu vết thay đổi.

Tạo bảng kiểm kê operation và đánh dấu mỗi operation xuất hiện ở trang nào. So với mục lục và spec để phát hiện trang bị bỏ sót; không tự điền nội dung thiếu từ spec vào tài liệu gốc. Nếu chỉ lấy một phần API, công bố danh sách operation được giữ và dùng cùng phạm vi khi chấm.

**Đầu ra:** `docs_clean.md`, bản đồ heading/URL nguồn và danh sách phần còn thiếu.

## 6. Xây ground truth theo tài liệu

Spec chính thức là nguồn hỗ trợ, không tự động bảo đảm trùng với tài liệu đã cào. Kiểm tra từng operation, tham số, request, response và ràng buộc so với tài liệu của cùng phiên bản.

Ví dụ tài liệu ghi:

```text
GET /books
limit: integer, default 20
```

Doc-GT nên phản ánh thông tin đó. Không thêm `maximum: 100` chỉ vì server có giới hạn này; giới hạn hành vi thuộc nhánh kiểm chứng runtime. Một field có mặt trong ví dụ cũng chưa đủ chứng minh nó bắt buộc.

Với thông tin chưa xác định, ghi trạng thái chưa rõ trong bảng annotation hoặc loại khỏi phạm vi chấm có kiểm soát. Không chuyển sự thiếu bằng chứng thành nhãn chắc chắn sai/đúng. Nếu muốn công cụ chấm bỏ qua các mục chưa rõ, cần thêm cơ chế mask; `evaluate.py` hiện chưa có chức năng này.

Nếu không có spec chính thức, người gắn nhãn phải dựng doc-GT từ tài liệu và lưu căn cứ. Có thể dùng mô hình để tạo bản nháp, nhưng đáp án cuối phải được kiểm chứng độc lập với hệ thống đang đánh giá.

Chọn phiên bản OpenAPI đích. Để tương thích folder hiện tại dùng 3.0.3, không phải vì đây là phiên bản mới nhất. Không chỉ đổi trường version khi chuyển 3.1 về 3.0.3; cần kiểm tra nullable, union types, exclusive bounds và các keyword không chuyển được. Công cụ hiện tại có trường hợp mất nghĩa khi chuyển union types.

Nguồn chuẩn để đối chiếu cấu trúc: [OpenAPI 3.0.3](https://spec.openapis.org/oas/v3.0.3.html).

**Đầu ra:** `ground_truth/openapi.yaml`, ghi chú chuẩn hóa và bảng căn cứ annotation.

## 7. Nhập một API vào cấu trúc folder hiện có

Sau khi có spec gốc và tài liệu sạch, từ thư mục gốc chạy ví dụ PowerShell:

```powershell
.\.venv\Scripts\python.exe tools/add_api.py --id library-demo --name "Library Demo" --group A --spec staging/library-demo/openapi_original.yaml --base-url http://localhost:8100/v1 --env local-docker --scope full --doc-original staging/library-demo/docs_clean.md --source-url https://example.org/library-demo --docs-url https://docs.example.org/v1 --license MIT --ablated
```

Đây là ví dụ cho API tự triển khai với giấy phép MIT giả định. Thay toàn bộ nguồn, giấy phép, URL, group và scope bằng thông tin thực. API công khai dùng group B và phạm vi được phép; API chỉ đánh giá tài liệu có thể đặt offline/none. Chỉ thêm `--ablated` khi muốn làm thí nghiệm tài liệu bị lược thông tin.

Script sẽ lưu spec nguyên bản, tạo spec chuẩn hóa, docs, metadata, facts và cập nhật thống kê. Nó tạo nhiều TODO; phải mở `meta.yaml` và điền các mục đó. Nếu doc-GT cần điều chỉnh để khớp tài liệu, sửa bằng căn cứ từ bước 6 rồi build lại.

Vì đầu vào spec ở ví dụ là tệp local, cần cập nhật `source.spec_url` thành URL nguồn thật nếu có. Bổ sung tên người gắn nhãn, phiên bản, ngày lấy, nguồn giấy phép, probe, auth và phạm vi kiểm thử.

Để giữ snapshot cùng mẫu API, có thể sao chép raw docs và crawl manifest vào `apis/library-demo/source/`. Quy ước này là bổ sung đề xuất; `add_api.py` chưa tự sao chép cả thư mục raw. Dùng `docs/original.md` cho tài liệu sạch có nguồn từ bản gốc. Script nhận cả PDF nhưng validator hiện đọc tài liệu dạng UTF-8, nên nên giữ PDF ở source và dùng bản trích xuất Markdown cho docs.

**Đầu ra:** một thư mục API đúng cấu trúc và metadata đã hoàn thiện.

## 8. Dựng và kiểm tra môi trường chạy

Nếu đánh giá runtime, phải ghim backend/image/commit và cấu hình, khởi tạo dữ liệu mẫu, xác định health check, credentials qua biến môi trường và cách reset. Kiểm tra một request hợp lệ và một request lỗi đã biết trước.

Với API có trạng thái, xác định thứ tự tạo tác giả/sách/đơn hàng hoặc tài nguyên tương ứng. Một request bị từ chối vì ID không tồn tại không đủ chứng minh ràng buộc kiểu hay biên đang sai.

Một image tự viết có thể thêm vào Compose, nhưng không sử dụng tag thay đổi như `latest`/`unstable` để xác định một bản phát hành benchmark. Với API công khai, lưu thời điểm và phiên bản quan sát được; khả năng tái lập sẽ hạn chế hơn máy chủ được kiểm soát.

`check_connectivity.py` có thể hỗ trợ kiểm tra probe sau khi metadata đã đúng. HTTP 2xx chỉ chứng minh probe đó nhận được 2xx; cần kiểm tra nội dung để tránh nhận trang HTML hoặc response lỗi nghiệp vụ là thành công.

**Đầu ra:** môi trường tái tạo được và quy trình reset; nếu không có, đánh dấu chỉ đánh giá tài liệu.

## 9. Xác minh hành vi và tạo nhãn sai lệch

Lập ma trận kiểm chứng theo từng ràng buộc:

| Loại | Các ca cần kiểm tra |
|---|---|
| minimum/maximum | Dưới biên, tại biên, trong miền và trên biên |
| required | Bỏ field, có giá trị hợp lệ, null nếu cần phân biệt |
| enum | Giá trị được tài liệu cho phép và các giá trị ngoài tập được chọn kiểm chứng |
| độ dài/mảng | Ngay dưới, tại và ngay trên giới hạn |
| phụ thuộc A → B | Có/không A kết hợp có/không B |
| status/response | Thành công, đầu vào sai, tài nguyên không tồn tại và schema của từng phản hồi |

Giữ các input khác hợp lệ và reset khi cần. Fuzzing có thể tìm ứng viên sai lệch; dùng probe có kiểm soát để xác nhận. Không suy ra toàn bộ miền enum chỉ từ một vài giá trị bị từ chối; không coi timeout, 401/403 hoặc 429 là bằng chứng ràng buộc dữ liệu.

Lưu request/response đã loại bỏ thông tin bí mật, cấu hình và phiên bản máy chủ, thời điểm, trạng thái dữ liệu, kết quả lặp và ID test. Có thể dùng Schemathesis bổ sung để tìm lỗi và tạo báo cáo; công cụ này không tự tạo đáp án hành vi chắc chắn cho bạn. Xem [hướng dẫn CLI chính thức](https://schemathesis.readthedocs.io/en/stable/tutorials/cli/).

Ví dụ một bản ghi tương thích các trường bắt buộc của danh sách discrepancies hiện tại:

```json
{
  "id": "LIB-001",
  "code": "D1",
  "op": "GET /books",
  "location": "query:limit",
  "keyword": ["maximum"],
  "description": "Tài liệu thiếu giới hạn trên của limit.",
  "doc": "không nêu maximum",
  "behavior": "maximum: 100",
  "probe": {
    "method": "GET",
    "path": "/books",
    "query": {"limit": 101},
    "expect_status": 400
  }
}
```

Bản ghi trên là minh họa; chỉ gắn nhãn giới hạn 100 sau khi có các probe xác nhận hai phía biên. Lưu thêm đường dẫn bằng chứng và người kiểm chứng. Tạo các đối chứng mà tài liệu và hành vi khớp để đo cảnh báo sai. Không bắt buộc phải tìm thấy sai lệch ở mọi API; danh sách rỗng sau phạm vi xác minh rõ vẫn có giá trị.

Với API ngoài thực tế, giữ nguyên lỗi quan sát được rồi phân loại. Với API lab tự viết, có thể chủ động cài sai lệch như Bookstore để kiểm soát đáp án, nhưng phải đánh dấu synthetic và báo cáo riêng với sai lệch thật. Một lỗi server không mặc nhiên là lý do sửa spec để hợp thức hóa lỗi.

Tạo `behavior_openapi.yaml` cho phần đã xác minh. Đặt `behavior_status: partial` nếu mới kiểm tra một phần, lưu coverage và ngoại lệ. Chỉ sử dụng exact trong phạm vi định nghĩa và kiểm chứng rõ; một số test qua không chứng minh mọi hành vi đều đúng.

**Đầu ra:** behavior-GT trong phạm vi xác minh, discrepancies, controls, bằng chứng và test tái hiện.

## 10. Kiểm duyệt nhãn

Người thứ nhất gắn nhãn, người thứ hai đối chiếu tài liệu và chạy lại bằng chứng. Nếu chỉ có một người, dành một lượt kiểm tra độc lập theo checklist và ghi rõ hạn chế này. Lưu ai sửa gì, lý do, nguồn và quyết định khi bất đồng.

Kiểm tra annotation ở mức operation/field/ràng buộc, không chỉ kiểm tra file YAML có parse được. Đảm bảo doc-GT và behavior-GT không bị trộn. Những mục chưa chắc chắn phải được giữ trạng thái chưa rõ, không tự động tính là đối chứng âm.

Các tệp annotation/coverage/evidence là phần mở rộng đề xuất. Công cụ hiện tại không tự tạo hoặc tự kiểm duyệt chúng.

**Đầu ra:** tập nhãn được duyệt, danh sách chưa rõ và phạm vi được dùng để tính điểm.

## 11. Sinh facts, tài liệu và thống kê

Chạy sau khi đã chỉnh xong các tệp nguồn của mẫu:

```powershell
.\.venv\Scripts\python.exe tools/build_dataset.py --api library-demo
.\.venv\Scripts\python.exe tools/validate_dataset.py --api library-demo
```

`build_dataset.py` sinh facts theo doc-GT, behavior facts nếu có file chuẩn theo tên, rendered docs, ablated docs nếu bật, manifest và thống kê. Nó không cào dữ liệu, không xác minh nhãn, không gọi LLM và không tự tạo discrepancies cho API mới. Script `make_discrepancies.py` hiện tại viết riêng cho Bookstore, không phải công cụ chung cho mọi API.

Trước khi dùng facts để chấm chính thức, sửa các lỗi đã phát hiện trong review: dependency trùng key, coverage kiểu phần tử mảng/xác thực và validator chỉ so key. Sau đó kiểm tra bằng các spec sai có chủ đích để bảo đảm metric phát hiện đúng loại lỗi bạn muốn đo.

Ablation là tùy chọn phục vụ câu hỏi nghiên cứu, không phải tiêu chí bắt buộc để mọi dataset hoàn chỉnh. Khi tạo ablation, kiểm tra ràng buộc bị ẩn có còn xuất hiện ở example, response hoặc operation khác không. Chốt đơn vị ẩn và seed; không diễn giải mọi khôi phục là nhờ runtime nếu thông tin vẫn còn trong tài liệu.

**Đầu ra:** các tệp sinh ra nhất quán và có phạm vi metric đã công bố.

## 12. Chia tập, kiểm thử đánh giá và phát hành

Chia theo API/họ API/phiên bản liên quan trước khi dùng dữ liệu để chỉnh prompt, quy tắc hoặc mô hình. Không chia ngẫu nhiên facts của cùng API thành train/test vì dễ lặp schema và thông tin. Với ít API, có thể dùng nhóm phát triển và nhóm đánh giá giữ riêng; không bắt buộc tỷ lệ 80/10/10.

Chỉ tạo train split nếu thực sự huấn luyện; dataset benchmark không bắt buộc phải có tập train. Có thể lưu `splits.json` và `benchmark_protocol.md`; đây là phần bổ sung, các công cụ hiện tại chưa thực thi split tự động.

Chạy thử bộ chấm: spec GT với chính nó, một spec có lỗi đúng loại cần đo, một spec tương đương về cách đặt tên, một spec không hợp lệ và một spec thiếu dữ liệu. Self-score bằng 1 chưa đủ chứng minh metric đúng.

Chỉ cấp tài liệu và thông tin vận hành cần thiết cho hệ thống đang đánh giá. Giữ spec nguồn, GT, mã SUT, discrepancy labels, ablation keys và bằng chứng kiểm duyệt ngoài quyền truy cập của mô hình trong phiên benchmark. Dữ liệu GT có thể phát hành cho nghiên cứu, nhưng runner phải tách quyền đọc khi đánh giá.

Đóng gói phiên bản phát hành với manifest SHA-256, README/dataset card, nguồn và giấy phép, hướng dẫn dựng lại, môi trường ghim phiên bản, giới hạn đã biết và quy trình thực nghiệm. Thử tái tạo trên môi trường sạch hoặc bởi một người khác. Nếu phải bỏ raw docs khỏi gói công khai do phạm vi sử dụng, ghi rõ phần nào có thể tái phân phối và cách thu thập lại.

**Đầu ra:** bản phát hành có phiên bản, phạm vi đánh giá rõ và có thể tái tạo.

## Cấu trúc đích

```text
SpecLoop-Bench/
  README.md
  manifest.json
  stats.csv
  docker-compose.sut.yml
  splits.json                    # đề xuất bổ sung
  benchmark_protocol.md          # đề xuất bổ sung
  tools/
  apis/
    library-demo/
      meta.yaml
      source/
        openapi_original.yaml
        raw_docs/                # đề xuất bổ sung
        crawl_manifest.jsonl     # đề xuất bổ sung
      docs/
        original.md
        rendered.md
        ablated.md               # tùy chọn
      ground_truth/
        openapi.yaml
        facts.jsonl
        behavior_openapi.yaml    # nếu đánh giá hành vi
        behavior_facts.jsonl
        discrepancies.json
        ablation.json            # nếu làm ablation
        annotations.jsonl        # đề xuất bổ sung
        coverage.json            # đề xuất bổ sung
      evidence/                  # đề xuất bổ sung
        requests_responses.jsonl
      sut/                       # nếu tự triển khai
        Dockerfile
        app.py
        test_behavior.py
```

## Tiêu chí nghiệm thu

| Mức | Điều kiện |
|---|---|
| Hoàn chỉnh cho đánh giá tài liệu | Có nguồn/phiên bản, snapshot, tài liệu sạch, doc-GT có căn cứ, phạm vi coverage và metric rõ, kiểm tra nhất quán, chia tập và hướng dẫn tái tạo |
| Hoàn chỉnh thêm cho đánh giá hành vi | Có môi trường chạy phù hợp, coverage xác minh, behavior-GT, nhãn sai lệch/đối chứng và bằng chứng tái hiện |
| Hoàn chỉnh cho thực nghiệm vòng phản hồi | Có thêm runner, ngân sách cố định, logging, baseline và cách chấm trước/sau; đây là hạ tầng thực nghiệm đi cùng dataset |

Tệp đủ tên không có nghĩa nhãn đúng. Cào xong mới có dữ liệu thô; dataset có giá trị đánh giá khi mỗi mẫu được gắn nguồn, phiên bản, đáp án có căn cứ, phạm vi sử dụng và cách kiểm chứng rõ ràng.
