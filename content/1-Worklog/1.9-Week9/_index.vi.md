---
title: "Tuần 09 – Serverless & Kiến trúc theo sự kiện"
date: 2026-06-15
draft: false
weight: 9
chapter: false
---

## Mục tiêu

* Khám phá dịch vụ serverless để chạy ứng dụng.
* Xây dựng luồng theo sự kiện với Lambda, API Gateway và EventBridge.
* Đánh giá lưu trữ quản lý như DynamoDB và S3 cho serverless.
* Tự động triển khai và kiểm thử tài nguyên serverless.

## Công việc (gợi ý theo ngày)

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Thiết kế API serverless bằng API Gateway và Lambda | Xác định endpoint, method, phân quyền |
| 2 | Triển khai lưu trữ với DynamoDB hoặc S3 | Áp dụng best practice về partition key, performance |
| 3 | Cấu hình EventBridge hoặc SNS cho event bất đồng bộ | Xây trigger hướng sự kiện |
| 4 | Deploy stack serverless bằng IaC và test end-to-end | Kiểm tra cold start, retry, error handling |
| 5 | Bật giám sát cho Lambda | Metrics, logs, và tracing X-Ray |
| 6 | Ghi chép kiến trúc serverless và hành vi retry | Lưu notes triển khai và giới hạn |

## Thành tựu

* Xây dựng ứng dụng nhẹ theo hướng event-driven bằng dịch vụ serverless.
* Kết nối API Gateway, Lambda và nguồn sự kiện cho workflow bất đồng bộ.
* Triển khai persistence quản lý bằng DynamoDB hoặc S3.
* Ghi lại triển khai và vận hành serverless.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/