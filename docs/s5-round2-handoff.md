# S5 · Bàn giao kết quả R3 vòng 2 cho C7

- Commit đã đo **`67509f410a1a4554793ae8ace6cf9faa96e44213`** (main merge PR #5); guards khớp commit code **`730d909`**.
- Code hash `3a909280bbcbce014fae5f658b5f072b44060bc13c004275e1cf51bdd43dfb8b`; tiêu chí còn nguyên, checkpoint `6640aec4` còn nguyên; chưa thay config so vòng 1.

| Lần đo theo thứ tự | Run ID | Kết quả |
|---|---|---|
| S5/after | `R-S5-after-20261118-173332-3a9092` | 90/90 đạt; hoàn sai/thiếu/lỗi hãng oan/PII đều 0 |
| base/after | `R-base-after-20261118-173333-3a9092` | 110/110 đạt; không regression |
| grade S5 | `R-S5-grade-20261118-173333-3a9092` | criteria/visible/regression/monitor đạt; tổng FAIL do integrity thiếu 28 file thẻ khác |

- [S5 eval report](evidence/R-S5-after-20261118-173332-3a9092/report.json)
- [Base eval report](evidence/R-base-after-20261118-173333-3a9092/report.json)
- [Grade JSON](evidence/R-S5-grade-20261118-173333-3a9092/grade-report.json) · [Grade Markdown](evidence/R-S5-grade-20261118-173333-3a9092/grade-report.md) · [manifest/commit đo](evidence/R-S5-grade-20261118-173333-3a9092/measurement.json)
- [S5-21 after](evidence/R-S5-grade-20261118-173333-3a9092/S5-21@11-after.txt): refunded **12.000đ**, fault đúng MKD/O-2521-P1, lời báo khách khớp khoản mới.
- [S5-02 after](evidence/R-S5-grade-20261118-173333-3a9092/S5-02@11-after.txt) và [S5-20 after](evidence/R-S5-grade-20261118-173333-3a9092/S5-20@11-after.txt): denied, ghi mới **0đ**, lời trả phân biệt khoản đã trả trước với lượt này. Không hoàn trùng.
- [Public tests](evidence/R-S5-grade-20261118-173333-3a9092/public-tests.txt): **13/13 OK**.

## Số liệu cho TV1 điền C7

Nhánh [1] fault tree: trước sửa R3 deny toàn bộ khi proposal + paid > entitlement; sau sửa `_refund_gate` tính phần còn lại, clamp khoản mới và chỉ deny khi đã trả đủ; `_blocked_refund_reply` làm rõ khoản trả trước/lượt mới. Tầng chặn/điều chỉnh thao tác ghi và phản hồi.

Prepared (giữ snapshot): 85/90 đạt, pass_rate/pass_k 0,9444, hoàn thiếu 60.000đ/5 seed. After: 90/90 đạt, pass_rate/pass_k 1,0, CI95 [1,1], hoàn thiếu **0**. Hai mốc cùng scope 60%. Không suy rộng CI trên mẫu mock thành bảo đảm production.

Chi phí S5/ticket **3.897đ**, ROI **1,57**; base **4.202đ**, ROI **1,38**; không vượt trần, không ca ùn. Monitor after S5 **4.214,25**, base **4.586,4**. Monitor không thay metric under_refund.

Biện pháp ngăn lỗi tái hiện trong mô phỏng tuần tự với ledger/chính sách đúng; còn rủi ro ghi đồng thời hoặc ledger sai, nên không tuyên bố ngăn mọi hoàn trùng ngoài thực tế. TV1 có thể dẫn run `R-S5-after-20261118-173332-3a9092` và grade `R-S5-grade-20261118-173333-3a9092` trong C7. TV2 đã cập nhật C0/C8/C9; giữ nguyên C7 để TV1 hoàn thiện.

## Giới hạn kết luận grade

`integrity=false` do thiếu 28 file S1/S2/S3/S4/S6/S7/S8; không sửa manifest để né. Bốn file S5 và các file khóa hiện có khớp hash. Chưa có hidden tests. `continue_allowed=true` chỉ phản ánh trần/ngưỡng số hiện đạt, không bù điều kiện integrity. Quyết định v2 thuộc TV3/cả nhóm; chưa gom submission cuối trong bước này.
