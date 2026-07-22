---
title: "Serverless và Kiến trúc theo sự kiện"
date: 2026-04-20
draft: false
weight: 9
chapter: false
pre: " <b> Tuần 09: </b> "

---

## Mục tiêu

* Khám phá các dịch vụ serverless để triển khai ứng dụng.
* Xây dựng luồng theo sự kiện với Lambda, API Gateway và EventBridge.
* Đánh giá các dịch vụ lưu trữ quản lý như DynamoDB và S3 cho ứng dụng serverless.
* Tự động hóa việc triển khai và kiểm thử tài nguyên serverless.

## Công việc đề xuất

| Ngày | Công việc | Ghi chú |
|------|-----------|---------|
| 1 | Thiết kế API serverless bằng API Gateway và Lambda | Xác định endpoint, method và phân quyền |
| 2 | Triển khai lưu trữ với DynamoDB hoặc S3 | Áp dụng best practice về partition key và hiệu năng |
| 3 | Cấu hình EventBridge hoặc SNS cho các sự kiện bất đồng bộ | Xây dựng trigger hướng sự kiện |
| 4 | Triển khai stack serverless bằng IaC và kiểm thử end-to-end | Kiểm tra cold start, retry và error handling |
| 5 | Kích hoạt giám sát cho Lambda | Sử dụng metrics, logs và tracing X-Ray |
| 6 | Ghi chép kiến trúc serverless và hành vi retry | Lưu lại ghi chú triển khai và các giới hạn |

## Thành tựu chính

* Xây dựng ứng dụng nhẹ theo hướng event-driven bằng các dịch vụ serverless của AWS.
* Kết nối API Gateway, Lambda và các nguồn sự kiện cho workflow bất đồng bộ.
* Triển khai persistence quản lý bằng DynamoDB hoặc S3.
* Ghi lại quy trình triển khai và vận hành cho kiến trúc serverless.

## Ghi chú

Tham khảo: https://cloudjourney.awsstudygroup.com/