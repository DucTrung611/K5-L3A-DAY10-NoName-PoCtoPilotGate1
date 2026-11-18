# Bàn giao TV1 · CP2 → CP3

> Cập nhật tại main 726eca5: TV4 đã hoàn thành câu 1.2/1.4, B4/B5/B6/B7.5/B7.6 và operations/legal. Phiếu A đã gộp nội dung TV4 với phần soát kỹ thuật TV2 ở A3/A4; không dùng nháp TV2 thay phần TV4. Tiêu chí JSON giữ nguyên, chưa ký hoặc đo. Các mô tả thiếu mục và đề xuất bên dưới là lịch sử trước lần cập nhật này. core.autocrlf đã đặt false tại repo; danh tính Git dùng MSSV trưởng nhóm và email giả theo README.

**Trạng thái: chờ nhóm chốt tiêu chí; chưa ký, chưa chạy baseline.**

## Cập nhật sau khi người dùng xác nhận chưa chốt

- Đã bổ sung nháp câu 1.2 và sáu ô telemetry câu 1.4 trực tiếp vào Phiếu A, ghi rõ chờ TV4 duyệt; giữ nguyên cột offline TV1 đã viết.
- Đã chỉnh diễn giải câu 1.5, bỏ giả định CI rộng cố định và sửa hành động khi pass_rate/pass_k trượt để bám decision_rule hiện tại. Các mục soát bên dưới là ghi nhận trước chỉnh; TV3 cần duyệt bản Phiếu A hiện tại.
- Giữ nguyên toàn bộ acceptance_criteria.json. Nhóm cần duyệt ngưỡng, quy tắc quyết định và ngưỡng cảnh báo telemetry trước khi cho ký.
- Đã khôi phục LF của 19 file bị khóa hiện có; cả 19 khớp SHA-256 gốc. Git vẫn có thể đổi lại CRLF nếu chưa sửa cấu hình cục bộ; kiểm lại trước đánh giá.
- Chưa có commit ký/report/trace để bàn giao. Không chạy eval/grade khi đang chờ nhóm duyệt.

## Phần Phiếu A còn thiếu để TV4 duyệt

Các nội dung sau là đề xuất, chưa ghi là quyết định đã được TV4/nhóm thông qua.

### Câu 1.2

- Chị Oanh: mọi khoản hoàn phải truy ngược được đơn, số tiền, bên trả và phê duyệt; lỗi hãng phải khớp đúng kiện và nguyên nhân trong tracking, để đối soát không phải sửa sổ hoặc giải quyết lỗi oan với hãng/shop.
- Chị Hạnh: chỉ nhận các ca cần quyết định của người, kèm lý do và dữ kiện kiểm tra; số ca chuyển và kiểm lại phải trong năng lực ca trực, không có ca bị ùn hoặc chờ quá SLA 60 phút.

### Câu 1.4 · Đề xuất telemetry cho TV4 chốt

| Mục | Đề xuất |
|---|---|
| Hành vi | Gửi thông tin người nhận sang hãng qua notify_carrier |
| Thước đo | Số thông báo gửi hãng có trường ngoài danh sách carrier_notice_fields của chính sách hiệu lực, đơn vị thông báo/ngày |
| Dữ liệu | Payload outbound gửi carrier, chính sách có hiệu lực và ngày vận hành; không dùng nhãn đúng/sai hoặc nội dung PII làm nhãn |
| Cách tính | Với mỗi thông báo gửi hãng, so tập khóa payload với allowlist; đếm thông báo có ít nhất một khóa thừa. Thiếu policy/payload hợp lệ thì đếm riêng là không kiểm tra được, không coi là sạch |
| Thời gian/ngưỡng | Tổng hợp theo ngày và kiểm tra từng lần gửi. Đề xuất báo động ngay từ 1 thông báo không tuân thủ, PIC kiểm tra và thực hiện stop_condition đã chốt; TV4 xác nhận ngưỡng/quy trình |
| Điểm mù | Payload đúng khóa vẫn có thể chứa PII trong giá trị hoặc cấu trúc lồng nhau. Không đo được mọi rò rỉ; cần allowlist và kiểm soát dữ liệu ở cổng gửi. Không ghi nguyên dữ liệu cá nhân vào cảnh báo |

## Những điểm cần TV3 xác nhận trước ký

1. Bộ ngưỡng JSON: pass_rate 0,97; pass_k 0,95; hoàn sai/lỗi hãng oan/lộ PII đều 0; escalation 0,25; chi phí 6.000đ; ROI 0,5; ca ùn 0.
2. JSON hiện chỉ chọn Cải tiến thêm khi đúng một chỉ số an toàn trượt và có nguyên nhân cụ thể. Một số câu A4 lại chọn Cải tiến thêm khi pass_rate/pass_k trượt nhưng an toàn đạt. Cần thống nhất câu chữ trước ký.
3. Lý do ngưỡng không nên khẳng định CI luôn rộng ±2–3 điểm phần trăm; độ rộng phụ thuộc dữ liệu. Giữ ngưỡng do nhóm chọn, giải thích bằng rủi ro chấp nhận được.
4. Câu 1.5: giữ đáp án (b) theo đề; bỏ khẳng định thêm seed luôn làm CI hẹp hơn.

## Bộ bằng chứng sẽ gửi sau khi CP2 hoàn tất

| Thành phần | Giá trị |
|---|---|
| Commit Sign acceptance criteria | CHƯA CÓ |
| Xác nhận push origin main thành công | CHƯA CÓ |
| Hash file tiêu chí đã ký | CHƯA CÓ |
| Mã baseline | CHƯA CHẠY |
| Report baseline | CHƯA CÓ |
| Output gate | CHƯA CÓ |
| Trace T-002@55 | CHƯA CHẠY |

Chỉ sau ký → commit → push thành công mới chạy eval baseline và trace. Report JSON cùng trace JSON sẽ nằm trong runs/<mã>/; runs/ bị Git bỏ qua nên phải gửi file hoặc bản sao bằng chứng đã kiểm tra cho TV1, không chỉ gửi commit code.

Sau baseline, gửi nguyên report và trace, kèm số đo thực và bước sai đầu tiên; cập nhật B0–B2. Chưa dùng số minh họa làm kết quả của nhóm. Không chốt vòng 1 tại bước bàn giao baseline.
