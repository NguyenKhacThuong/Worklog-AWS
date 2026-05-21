---
title: "Tuần 02 – Nền tảng Mạng & Tính toán"
date: 2026-04-27
draft: false
weight: 2
chapter: false
---

## Mục tiêu

* Hiểu và thực hành cấu hình Amazon VPC (subnet, route table, IGW).
* Triển khai và quản lý EC2 instance.
* Thiết lập giám sát hệ thống với CloudWatch.
* Thực hành IAM Roles gắn vào EC2.

### Công việc

| Ngày | Công việc | Bắt đầu | Kết thúc | Tài liệu |
|------|-----------|---------|---------|---------|
| 1 | Workshop VPC: tạo VPC, public/private subnet | 2026-04-27 | 2026-04-27 | https://000003.awsstudygroup.com |
| 2 | Tạo EC2 instance, cấu hình Security Group | 2026-04-28 | 2026-04-28 | https://000004.awsstudygroup.com |
| 3 | Gắn IAM Role cho EC2, kiểm tra quyền truy cập | 2026-04-29 | 2026-04-29 | https://000048.awsstudygroup.com |
| 4 | Thiết lập CloudWatch metrics, tạo alarm CPU | 2026-04-30 | 2026-04-30 | https://000008.awsstudygroup.com |
| 5 | SSH vào EC2, cài ứng dụng web đơn giản | 2026-05-01 | 2026-05-01 | https://000004.awsstudygroup.com |
| 6 | Viết báo cáo tuần, cập nhật worklog lên Hugo site | 2026-05-02 | 2026-05-02 | Tài liệu nội bộ |

### Thành tựu

* Tạo thành công VPC với public/private subnet, route table và Internet Gateway.
* Triển khai EC2 instance và truy cập qua SSH.
* Gắn IAM Role cho EC2 và kiểm tra quyền S3 read từ instance.
* Tạo CloudWatch alarm cảnh báo khi CPU vượt 80%.

### Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/1-explore/