---
title: "Lưu trữ và Cơ sở dữ liệu"
date: 2026-04-20
draft: false
weight: 3
chapter: false
pre: " <b> Tuần 03: </b> "

---

## Mục tiêu

* Host một website tĩnh bằng Amazon S3.
* Triển khai Amazon RDS MySQL và kết nối tới nó từ EC2.
* Làm quen với DynamoDB và thực hiện các thao tác CRUD cơ bản.
* So sánh mô hình SQL và NoSQL trong môi trường cloud.

## Công việc đề xuất

| Ngày | Công việc | Bắt đầu | Kết thúc | Tài liệu |
|------|-----------|---------|---------|---------|
| 1 | Hoàn thành workshop S3 và bật static website hosting | 2026-05-04 | 2026-05-04 | https://000057.awsstudygroup.com |
| 2 | Cấu hình bucket policy cho S3 và kiểm tra public access | 2026-05-05 | 2026-05-05 | https://000069.awsstudygroup.com |
| 3 | Tạo RDS MySQL instance trong private subnet | 2026-05-06 | 2026-05-06 | https://000005.awsstudygroup.com |
| 4 | Kết nối tới RDS từ EC2, tạo bảng và chèn dữ liệu mẫu | 2026-05-07 | 2026-05-07 | https://000005.awsstudygroup.com |
| 5 | Hoàn thành workshop DynamoDB và thực hiện các thao tác CRUD | 2026-05-08 | 2026-05-08 | https://000060.awsstudygroup.com |
| 6 | So sánh RDS và DynamoDB và cập nhật worklog | 2026-05-09 | 2026-05-09 | Tài liệu nội bộ |

## Thành tựu chính

* Host thành công website tĩnh trên S3 với bucket policy tùy chỉnh.
* Triển khai RDS MySQL trong private subnet và kết nối từ EC2 qua security group.
* Thực hành CRUD trên DynamoDB bằng AWS Console và AWS CLI.
* Chuẩn bị một bản so sánh RDS và DynamoDB và chia sẻ với mentor.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/1-explore/