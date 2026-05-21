---
title: "Tuần 03 – Lưu trữ & Cơ sở dữ liệu"
date: 2026-05-04
draft: false
weight: 3
chapter: false
---

## Mục tiêu

* Thực hành host static website với Amazon S3.
* Triển khai Amazon RDS (MySQL) và kết nối từ EC2.
* Tìm hiểu DynamoDB và thực hiện CRUD cơ bản.
* Hiểu sự khác biệt SQL vs NoSQL trong môi trường cloud.

### Công việc

| Ngày | Công việc | Bắt đầu | Kết thúc | Tài liệu |
|------|-----------|---------|---------|---------|
| 1 | Workshop S3: upload file, bật static website hosting | 2026-05-04 | 2026-05-04 | https://000057.awsstudygroup.com |
| 2 | Cấu hình S3 bucket policy, kiểm tra public access | 2026-05-05 | 2026-05-05 | https://000069.awsstudygroup.com |
| 3 | Tạo RDS MySQL instance trong private subnet | 2026-05-06 | 2026-05-06 | https://000005.awsstudygroup.com |
| 4 | Kết nối RDS từ EC2, tạo bảng và insert dữ liệu mẫu | 2026-05-07 | 2026-05-07 | https://000005.awsstudygroup.com |
| 5 | Workshop DynamoDB: tạo table, thao tác CRUD | 2026-05-08 | 2026-05-08 | https://000060.awsstudygroup.com |
| 6 | So sánh RDS vs DynamoDB, cập nhật worklog | 2026-05-09 | 2026-05-09 | Tài liệu nội bộ |

### Thành tựu

* Host thành công static website trên S3 với custom bucket policy.
* Triển khai RDS MySQL trong private subnet, kết nối từ EC2 qua Security Group.
* Thực hành CRUD trên DynamoDB bằng AWS Console và AWS CLI.
* Viết so sánh RDS vs DynamoDB, trình bày với mentor.

### Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/1-explore/