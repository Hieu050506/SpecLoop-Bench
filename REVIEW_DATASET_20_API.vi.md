# Đánh giá SpecLoop-Bench: 20 API

Ngày kiểm tra: 01/11/2026. Phạm vi: `D:\SpecLoop-Bench`, đối chiếu thêm các tệp quản lý và công cụ trên repo nhóm tại commit `f5534cf24739b055b4b1218784d250f681bec12f`.

**Cập nhật khi chuẩn bị commit cùng ngày:** đã đồng bộ README và Compose theo bản 20 API trên repo nhóm, cập nhật manifest và stats từ dữ liệu cục bộ. Lỗi manifest 9/20 và thiếu bốn dịch vụ mới trong Compose nêu bên dưới đã được xử lý; Conduit vẫn chưa có dịch vụ chạy sẵn. Những số liệu về bản cục bộ 9 API trong báo cáo là ảnh chụp trạng thái trước cập nhật. Các hạn chế của bộ chấm, tài liệu gốc, behavior-GT và ablation vẫn còn.

Sau cập nhật, `tools/validate_dataset.py` báo **ĐẠT cho 20/20 API**; còn các cảnh báo về tài liệu gốc và kết nối API công khai. Giao diện xem dataset đã được bổ sung ở `tools/view_dataset.py` và `tools/dataset_viewer.html`, có hướng dẫn chạy trong README. Các nhãn request/response trên trang là thông tin khai báo trong đặc tả, chưa phải dữ liệu trao đổi với API thật.

Chưa có tiêu chí nghiệm thu riêng do nhóm cung cấp. Căn cứ đánh giá là README, checklist trước khi nộp/commit và mục tiêu RQ1–RQ3 trong dự án. `HUONG_DAN_XAY_DUNG_DATASET.vi.md` là hướng dẫn bổ sung, không được coi là quy định nghiệm thu đã được nhóm phê duyệt. Không có căn cứ kết luận bắt buộc bao nhiêu API mới là đủ.

**Kết luận:** dữ liệu có cấu trúc tốt và dùng được để chạy thử; chưa đủ cơ sở coi là benchmark hoàn chỉnh để kết luận RQ1–RQ3 trên cả 20 API. Cần phân biệt bản cục bộ chưa đồng bộ tệp quản lý với những hạn chế chất lượng vốn có trong dataset và bộ chấm.

## Kết quả kiểm tra thực tế

| Kiểm tra | Kết quả |
|---|---|
| API thực tế, không tính `_template` | 20 API, 877 operation, 61.793 doc facts |
| Ground truth theo tài liệu | 20/20 đúng nhãn 3.0.3 và qua validator OpenAPI |
| Facts lưu sẵn so với trích xuất lại | 20/20 khớp toàn bộ bản ghi, bao gồm giá trị |
| Tài liệu rendered so với render lại trong bộ nhớ | 20/20 khớp |
| Metadata chứa TODO | 0/20 |
| Tài liệu gốc độc lập được lưu trong dataset | 2/20: Bookstore-Lab và RealWorld Conduit |
| Behavior-GT | 1/20: Bookstore-Lab; 306 behavior facts khớp khi trích xuất lại |
| Nhãn sai lệch/đối chứng | Bookstore có 13 sai lệch và 10 đối chứng |
| Test hành vi Bookstore chạy lại | 20 passed, 1 cảnh báo deprecation của thư viện |
| Manifest cục bộ | 9 API; 63 tệp được liệt kê đều tồn tại và khớp SHA-256 |
| Validator toàn bộ ở trạng thái hiện tại | Thoát mã 1, báo 11 lỗi API chưa có trong manifest |
| Kiểm tra trực tiếp từng API, kể cả 11 API bị validator bỏ qua | Không phát hiện lỗi cấu trúc qua `check_api`; còn cảnh báo thiếu tài liệu gốc/kết nối |
| Ablation | 7 API, tổng 316 khóa ghi là bị ẩn; Typesense có 2 khóa renderer không sử dụng |

Facts khớp công cụ sinh ra chúng chứng minh tính nhất quán, chưa chứng minh công cụ bao phủ đủ ngữ nghĩa hoặc nhãn đúng với server thật. 61.793 facts cũng không phải 61.793 mẫu API độc lập.

## Các vấn đề cần xử lý

### 1. Bản máy đang trộn dữ liệu mới với tệp quản lý cũ

`manifest.json`, `stats.csv`, README cục bộ vẫn là bản 9 API. Compose cục bộ chỉ có Bookstore và Petstore, trong khi metadata hiện khai báo 7 API chạy Docker. Thiếu cấu hình dịch vụ của httpbin, Qdrant, Typesense, Spring PetClinic và Conduit.

Đây là hệ quả của thao tác trước đó chỉ bổ sung tệp chưa có, giữ nguyên tệp đã tồn tại. **Không phải repo nhóm quên cập nhật manifest:** bản trên GitHub đã ghi đúng 20 API, 877 operation, 61.793 facts; Compose trên đó có thêm 4 dịch vụ mới. Conduit vẫn chỉ là ghi chú chọn backend, chưa có cấu hình dịch vụ chạy sẵn ở cả hai bản.

Việc cần làm: đối chiếu và cập nhật các tệp đã tồn tại, đặc biệt README, manifest, stats và Compose; kiểm tra metadata/công cụ khác biệt trước khi chốt cùng một phiên bản dataset. Sau đó chạy lại validator. Không mặc định mọi khác biệt công cụ đều là thay đổi thuật toán: các khác biệt đã xem trong extractor và evaluator chủ yếu là cách ghi xuống dòng LF; validator hai bản giống nhau.

### 2. Bộ chấm có điểm mù ảnh hưởng kết luận nghiên cứu

Đã chạy các phép thử trên bản sao đặc tả trong bộ nhớ:

| Thay đổi | Kết quả hiện tại | Vấn đề |
|---|---|---|
| Bookstore: `tags.items.type` từ string sang integer | Micro F1 = 1,0000 | Sai kiểu phần tử mảng không bị phạt |
| Petstore: xóa security ở operation/root và securitySchemes | Micro F1 = 1,0000 | Bỏ xác thực vẫn đạt điểm tuyệt đối |
| Bookstore: xóa `info` | Micro F1 = 1,0000, nhưng validator xác nhận thiếu trường bắt buộc | Bộ chấm không buộc prediction hợp lệ trước khi chấm |
| Đổi `{book_id}` thành `{id}` cùng path parameter tương ứng | Micro F1 = 0,9860; parameter F1 = 0,9000 | Cách viết tương đương vẫn bị trừ điểm |

Trong ohsome, đặc tả có **64** điều kiện `x-dependencies` nhưng facts chỉ giữ **16**. `FactSink.add()` bỏ bản ghi có key đã tồn tại; các dependency trong cùng operation dùng chung key nên mất 48 điều kiện.

Vị trí chính: `tools/extract_facts.py` (`FactSink.add`, duyệt array và dependency), `tools/evaluate.py` (chấm trước khi kiểm tra tính hợp lệ), `tools/oas_utils.py` (chuẩn hóa path).

Việc cần làm: sửa định danh dependency, bổ sung coverage kiểu phần tử mảng và các thành phần trong phạm vi nghiên cứu, chuẩn hóa path parameter theo vị trí; báo cáo tỷ lệ OpenAPI hợp lệ riêng. Sau khi sửa extractor phải sinh lại facts và thống kê, chốt phiên bản metric để không trộn điểm trước/sau thay đổi.

### 3. Thiếu ground truth hành vi cho đánh giá diện rộng

19/20 API có `behavior_status: pending` và không có đường dẫn behavior-GT trong metadata. Chỉ Bookstore có đáp án hành vi cùng nhãn sai lệch/đối chứng. Khai báo `rq_scope: [RQ1, RQ2, RQ3]` là mục tiêu sử dụng, chưa chứng minh API đã sẵn sàng cho cả ba câu hỏi.

Vì vậy có thể dùng Bookstore để thử đánh giá RQ2/RQ3 trong phạm vi các ca đã gắn nhãn; chưa đủ để công bố kết quả định lượng đại diện cho cả 20 API. Cần thêm probe có kiểm soát, bằng chứng request/response, phạm vi coverage, nhãn sai lệch và đối chứng được duyệt cho các API được chọn đánh giá hành vi. Không cần bắt buộc mọi API đều có sai lệch; cần biết rõ phần nào đã được kiểm chứng.

Các cờ `connectivity_checked` là dữ liệu có sẵn. Lần đánh giá này không chạy Docker và không gọi API công khai, nên không xác nhận dịch vụ hiện còn truy cập được. Sáu API public cục bộ chưa được đánh dấu kiểm tra: FDIC, Genome Nexus, Jikan, LanguageTool, ohsome và OMDb. REST Countries đang cấu hình offline/none, chỉ RQ1.

### 4. Thiếu tài liệu gốc để chứng minh tính đại diện của RQ1

18/20 API chỉ lưu tài liệu render từ chính GT. Đây là đầu vào hợp lệ cho một thí nghiệm có công bố rõ cách tạo dữ liệu, nhưng thiên về dựng lại đặc tả từ biểu diễn văn bản có cấu trúc. Chưa đủ để kết luận tổng quát cho tài liệu REST API viết tay, phân tán hoặc không nhất quán.

Việc cần làm: chọn thêm API để lưu snapshot tài liệu độc lập cùng phiên bản, URL/ngày lấy và kiểm tra doc-GT với tài liệu đó. Báo cáo riêng original/rendered/ablated. Không coi việc thiếu `original.md` là lỗi cấu trúc bắt buộc cho mọi API vì README cho phép dùng bản render.

### 5. Ablation đang ghi nhận hai khóa không được renderer xử lý

Typesense khai báo 26 khóa ẩn, nhưng chỉ 24 khóa được `Hider` sử dụng. Hai khóa còn lại:

```text
constraint|DELETE /collections/{}/documents|query:deleteDocumentsParameters:filter_by|filter_by|required
constraint|GET /collections/{}/documents/search|query:searchParameters:drop_tokens_mode|drop_tokens_mode|enum
```

Do đó không nên tính cả 26 khóa như 26 ràng buộc thực sự đã được loại khỏi đầu vào. Cần sửa sự tương thích giữa extractor và renderer hoặc loại các khóa không áp dụng được khỏi tập ablation, rồi kiểm tra lại thông tin còn xuất hiện ở mô tả, ví dụ và vị trí khác. Những bản ablation đã lưu khớp khi render lại chưa đủ chứng minh thông tin đã được ẩn hoàn toàn.

### 6. Validator và tài liệu tái lập cần hoàn thiện

Validator hiện chỉ so tập key của facts, không so toàn bộ giá trị; hash lệch chỉ tạo cảnh báo. Trong lần kiểm tra này đã bổ sung phép đối chiếu toàn bộ bản ghi và không thấy facts sai, nhưng công cụ mặc định chưa đủ bảo vệ các lần cập nhật tiếp theo.

Cần bổ sung kiểm tra đầy đủ giá trị facts/behavior facts, hiệu lực ablation và tính nhất quán manifest hai chiều; cân nhắc chế độ strict cho bản phát hành. Cần ghim phiên bản image/thư viện, quy trình khởi tạo và reset, phân tách API phát triển/đánh giá, và tài liệu giao thức benchmark. Không mặc định cần train split nếu không huấn luyện mô hình.

Nguồn được ghi trong metadata, nhưng mức chi tiết không đồng đều. Riêng httpbin: metadata nói chuyển từ Swagger 2.0, còn `source/openapi_original.yaml` đang là 3.0.3; nên bổ sung snapshot Swagger trước chuyển đổi để truy nguyên đầy đủ. Không suy từ việc YAML hợp lệ rằng mọi phép chuẩn hóa đã bảo toàn nghĩa.

Runner LLM, ngân sách, baseline, logging và chấm trước/sau thuộc hạ tầng thực nghiệm đi cùng dataset. Chưa kiểm tra backend/frontend của repo lớn trong lần này, nên không kết luận toàn dự án thiếu những thành phần đó. Khi đánh giá phải tách quyền đọc GT, spec nguồn và nhãn sai lệch khỏi hệ thống đang được chấm.

## Mức sẵn sàng và thứ tự ưu tiên

| Mục tiêu | Đánh giá hiện tại |
|---|---|
| Dữ liệu đầu vào để phát triển/chạy thử | Dùng được; nên thống nhất tệp quản lý trước |
| RQ1: chất lượng đặc tả sinh từ tài liệu | Có nền tảng; cần sửa bộ chấm và công bố rõ loại tài liệu/phạm vi |
| RQ2: độ chính xác phát hiện sai lệch từ test | Có thể thử trên Bookstore; thiếu nhãn hành vi cho diện rộng |
| RQ3: mức cải thiện sau feedback | Có thể thử trên Bookstore trong phạm vi đã gắn nhãn; chưa đủ bằng chứng cho cả bộ |
| Đạt nghiệm thu riêng của nhóm/trường | Chưa thể kết luận khi chưa có tiêu chí được cung cấp |

Ưu tiên: (1) thống nhất phiên bản local/repo nhóm; (2) sửa bộ chấm và ablation; (3) chọn tập API đánh giá, bổ sung tài liệu độc lập và nhãn hành vi; (4) chốt môi trường, giao thức và phát hành phiên bản có thể tái tạo. Chưa có lý do ưu tiên tăng số API trước các việc này.

## Cách kiểm tra đã dùng

```powershell
$env:PYTHONIOENCODING = 'utf-8'
$env:PYTHONDONTWRITEBYTECODE = '1'
.\.venv\Scripts\python.exe tools/validate_dataset.py
.\.venv\Scripts\python.exe -m pytest -q -p no:cacheprovider apis/bookstore-lab/sut/test_behavior.py
```

Ngoài hai lệnh trên, đã chạy các đoạn kiểm tra trong bộ nhớ: gọi `check_api` trực tiếp cho cả 20 API, so toàn bộ bản ghi từ `extract` với JSONL lưu sẵn, render lại tài liệu/ablation, kiểm tra hash của 63 tệp trong manifest và các phép thay đổi prediction nêu trên. Các đoạn kiểm tra bổ sung không được cài thành bộ test thường trực.

Không chạy `build_dataset.py`, không sửa GT/facts/metadata/tệp quản lý, không commit hay push. Tệp báo cáo này là đầu ra bổ sung của lần đánh giá.
