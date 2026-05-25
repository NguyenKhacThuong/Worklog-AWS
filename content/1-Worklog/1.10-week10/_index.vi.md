---
title: "Tuần 10 – Dịch vụ dữ liệu & Phân tích"
date: 2026-04-20
draft: false
weight: 10
chapter: false
---

## Mục tiêu

* Khám phá dịch vụ dữ liệu AWS cho lưu trữ, phân tích và truy vấn.
* Triển khai vòng đời dữ liệu, lưu trữ lưu trữ và mô hình truy cập.
* Xây dựng pipeline phân tích nhỏ bằng Athena hoặc Glue.
* Xem xét tối ưu chi phí cho workload dữ liệu.

## Công việc (gợi ý theo ngày)

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Định nghĩa mô hình lưu trữ dữ liệu với S3 và lifecycle | Phân tầng raw, processed và archive |
| 2 | Cấu hình data catalog và lớp truy vấn với Athena hoặc Glue | Kiểm tra schema và partitioning |
| 3 | Tạo query/báo cáo từ dữ liệu mẫu | Đo tốc độ truy vấn và chi phí |
| 4 | Khám phá ingestion serverless bằng Kinesis hoặc S3 event | Tự động hoá bước pipeline dữ liệu |
| 5 | Tối ưu class lưu trữ và retention để tiết kiệm | Dùng Intelligent-Tiering, Glacier, lifecycle |
| 6 | Ghi chép kiến trúc analytics và kết quả | Lưu lại điều đã thành công và cải thiện |

## Thành tựu

* Thiết kế lưu trữ dữ liệu và quản lý vòng đời cho phân tích.
* Xây dựng khả năng truy vấn/báo cáo bằng dịch vụ dữ liệu quản lý.
* Cải thiện hiệu quả chi phí bằng tối ưu lưu trữ và retention.
* Ghi chép luồng dữ liệu end-to-end và bài học.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/