---
title: "Tuần 07 – Nâng cao bảo mật"
date: 2026-06-01
draft: false
weight: 7
chapter: false
---

## Mục tiêu

* Tăng cường bảo mật AWS bằng nguyên tắc least-privilege.
* Kiểm tra IAM role, policy và quyền truy cập dịch vụ.
* Bật dịch vụ bảo mật như GuardDuty, AWS Config, Security Hub.
* Cải thiện tách biệt tài nguyên và mã hoá.

## Công việc (gợi ý theo ngày)

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Kiểm tra IAM user, group, role và policy | Loại bỏ quyền không cần thiết |
| 2 | Thiết lập quyền ít nhất cho dịch vụ ứng dụng | Dùng managed policy và role assumption |
| 3 | Bật GuardDuty và xem các findings | Điều tra hoạt động đáng ngờ |
| 4 | Bật AWS Config rules và Security Hub | Tuân theo best practice bảo mật |
| 5 | Mã hoá dữ liệu khi lưu và truyền | KMS, TLS, S3 encryption |
| 6 | Ghi chép các kiểm soát và cách khắc phục | Lưu lại notes rà soát bảo mật |

## Thành tựu

* Nâng cao kiểm soát nhận dạng và truy cập trong tài khoản.
* Bật giám sát và kiểm tra tuân thủ tự động.
* Củng cố bảo vệ dữ liệu bằng các thực hành mã hoá.
* Ghi lại quy trình làm cứng bảo mật và bước tiếp theo.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/