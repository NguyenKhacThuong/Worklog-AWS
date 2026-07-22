---
title: "Tuần 07 – Nâng cao bảo mật"
date: 2026-04-20
draft: false
weight: 7
chapter: false
---

## Mục tiêu

* Tăng cường bảo mật cho môi trường AWS bằng nguyên tắc least-privilege.
* Kiểm tra IAM role, policy và quyền truy cập của các dịch vụ.
* Bật các dịch vụ bảo mật như GuardDuty, AWS Config và Security Hub.
* Cải thiện cách tách biệt tài nguyên và áp dụng mã hóa.

## Công việc đề xuất

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Kiểm tra IAM user, group, role và policy | Loại bỏ các quyền không còn cần thiết |
| 2 | Thiết lập quyền tối thiểu cho các dịch vụ ứng dụng | Dùng managed policy và role assumption |
| 3 | Bật GuardDuty và xem xét các findings | Điều tra các hoạt động đáng ngờ |
| 4 | Kích hoạt AWS Config rules và Security Hub | Tuân thủ các best practice bảo mật |
| 5 | Mã hóa dữ liệu khi lưu trữ và truyền tải | Sử dụng KMS, TLS và S3 encryption |
| 6 | Ghi chép các kiểm soát bảo mật và cách khắc phục | Lưu lại ghi chú rà soát bảo mật |

## Thành tựu chính

* Nâng cao kiểm soát nhận dạng và truy cập trong tài khoản AWS.
* Kích hoạt giám sát và kiểm tra tuân thủ tự động.
* Củng cố bảo vệ dữ liệu bằng các thực hành mã hóa phù hợp.
* Ghi lại quy trình tăng cường bảo mật và các bước tiếp theo.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/