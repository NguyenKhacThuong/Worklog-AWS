---
title: "Tuần 02 – Nền tảng Mạng và Tính toán"
date: 2026-04-20
draft: false
weight: 2
chapter: false
---

## Mục tiêu

* Hiểu và thực hành cấu hình Amazon VPC bằng cách sử dụng subnet, route table và Internet Gateway.
* Triển khai và quản lý các EC2 instance một cách an toàn và hiệu quả.
* Thiết lập giám sát cơ bản với CloudWatch.
* Thực hành gắn IAM role vào EC2 và xác minh quyền truy cập.

## Công việc đề xuất

| Ngày | Công việc | Bắt đầu | Kết thúc | Tài liệu |
|------|-----------|---------|---------|---------|
| 1 | Hoàn thành workshop VPC và tạo public/private subnet | 2026-04-27 | 2026-04-27 | https://000003.awsstudygroup.com |
| 2 | Khởi chạy EC2 instance và cấu hình security group | 2026-04-28 | 2026-04-28 | https://000004.awsstudygroup.com |
| 3 | Gắn IAM role cho EC2 và kiểm tra quyền truy cập | 2026-04-29 | 2026-04-29 | https://000048.awsstudygroup.com |
| 4 | Cấu hình CloudWatch metrics và tạo alarm CPU | 2026-04-30 | 2026-04-30 | https://000008.awsstudygroup.com |
| 5 | Kết nối vào EC2 qua SSH và cài đặt một ứng dụng web đơn giản | 2026-05-01 | 2026-05-01 | https://000004.awsstudygroup.com |
| 6 | Viết báo cáo tuần và cập nhật worklog trên Hugo site | 2026-05-02 | 2026-05-02 | Tài liệu nội bộ |

## Thành tựu chính

* Tạo thành công VPC với public/private subnet, route table và Internet Gateway.
* Khởi chạy EC2 instance và truy cập qua SSH.
* Gắn IAM role cho EC2 và xác minh quyền đọc S3 từ instance.
* Tạo CloudWatch alarm để cảnh báo khi CPU vượt 80%.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/1-explore/