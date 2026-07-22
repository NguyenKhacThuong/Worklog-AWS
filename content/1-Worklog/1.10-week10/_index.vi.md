---
title: "Dịch vụ dữ liệu và Phân tích"
date: 2026-04-20
draft: false
weight: 10
chapter: false
pre: " <b> Tuần 10: </b> "

---

## Mục tiêu

* Khám phá các dịch vụ dữ liệu của AWS cho lưu trữ, phân tích và truy vấn.
* Triển khai vòng đời dữ liệu, lưu trữ lưu trữ và mô hình truy cập phù hợp.
* Xây dựng một quy trình phân tích nhỏ bằng Athena hoặc Glue.
* Tối ưu chi phí cho workload dữ liệu.

## Công việc đề xuất

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Định nghĩa mô hình lưu trữ dữ liệu với S3 và lifecycle policy | Phân tầng raw, processed và archive |
| 2 | Cấu hình data catalog và lớp truy vấn bằng Athena hoặc Glue | Kiểm tra schema và partitioning |
| 3 | Tạo query và báo cáo từ dữ liệu mẫu | Đo tốc độ truy vấn và chi phí |
| 4 | Khám phá ingestion serverless bằng Kinesis hoặc S3 event | Tự động hóa các bước của pipeline dữ liệu |
| 5 | Tối ưu storage class và retention để tiết kiệm chi phí | Sử dụng Intelligent-Tiering, Glacier và lifecycle rules |
| 6 | Ghi chép kiến trúc analytics và kết quả đạt được | Lưu lại những điểm thành công và cần cải thiện |

## Thành tựu chính

* Thiết kế mô hình lưu trữ dữ liệu và quản lý vòng đời cho phân tích.
* Xây dựng khả năng truy vấn và báo cáo bằng các dịch vụ dữ liệu được quản lý.
* Cải thiện hiệu quả chi phí thông qua tối ưu storage class và retention.
* Ghi chép toàn bộ luồng dữ liệu end-to-end và các bài học kinh nghiệm.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/