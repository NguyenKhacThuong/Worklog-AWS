---
title: "Đề xuất dự án"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---


## 1. Tổng quan dự án

AI Content Generator Platform là một nền tảng SaaS thế hệ mới, giúp các doanh nghiệp vừa và nhỏ (SMB) tự động hóa quy trình tạo nội dung marketing bằng công nghệ Generative AI. Nền tảng kết hợp AWS Cloud và Gemini API (Google AI) để cung cấp một giải pháp tạo nội dung có khả năng mở rộng, bảo mật và linh hoạt.

|  |  |
|---|---|
| Mô hình kinh doanh | SaaS — đăng ký theo tháng/năm |
| Đối tượng khách hàng | Doanh nghiệp vừa và nhỏ (SMB), agency marketing |
| Công nghệ AI | Gemini API (Google AI) qua AWS Lambda |
| Khu vực AWS | ap-southeast-1 (Singapore) |
| Availability Zones | ap-southeast-1a và ap-southeast-1b |
| Khả năng mở rộng | Auto Scaling Group (10–10,000+ người dùng) |
| Tính sẵn sàng | Triển khai Multi-AZ, RDS Multi-AZ failover (99.9% uptime) |

## 2. Mục tiêu

### 2.1 Mục tiêu dự án

| STT | Mục tiêu | Kết quả mong đợi |
|---|---|---|
| 1 | Xây dựng MVP hoàn chỉnh trong 4 tuần (Tuần 9–12) | Go-live trước cuối Tuần 12 |
| 2 | Đạt tính sẵn sàng cao cho hệ thống production | Uptime ≥ 99.9% |
| 3 | Tự động hóa toàn bộ quy trình tạo nội dung AI từ đầu đến cuối | < 60 giây cho mỗi nội dung |
| 4 | Xây dựng kiến trúc đúng chuẩn AWS Well-Architected Framework | Đáp ứng đầy đủ 6 trụ cột |
| 5 | Bảo mật toàn diện theo nguyên tắc Least Privilege | Không sử dụng quyền wildcard * |

### 2.2 Giá trị mang lại

- Tiết kiệm thời gian: rút ngắn quy trình tạo nội dung từ 3–5 ngày xuống còn dưới 30 phút.
- Tiết kiệm chi phí: giảm 60–80% so với thuê copywriter hoặc agency (từ $500–$3,000/tháng xuống còn $50–$150/tháng).
- Nhất quán thương hiệu: Brand Persona đảm bảo đúng giọng văn dù tạo 10 hay 1,000 nội dung.
- Dễ mở rộng: mở rộng sang nhiều sản phẩm, thị trường và ngôn ngữ mà không cần tăng nhân sự tuyến tính.

## 3. Vấn đề cần giải quyết

### 3.1 Bối cảnh thị trường

Thị trường marketing số tại Đông Nam Á đã tăng trưởng nhanh kể từ đại dịch COVID-19. Các SMB luôn chịu áp lực phải tạo nội dung đa kênh liên tục, trong khi nguồn lực sáng tạo còn hạn chế và chi phí thuê copywriter/agency ngày càng tăng.

### 3.2 Các vấn đề cốt lõi

Vấn đề 1 — Chi phí nhân công cao: một SMB trung bình chi khoảng $500–$3,000/tháng cho nội dung marketing, trong khi lực lượng sáng tạo chất lượng cao thì khan hiếm và đắt đỏ.

Vấn đề 2 — Thiếu nhất quán về thương hiệu: khi nhiều người hoặc agency tạo nội dung cùng lúc, giọng văn và hình ảnh thương hiệu dễ bị phân kỳ, làm suy giảm niềm tin của khách hàng cuối.

Vấn đề 3 — Tốc độ sản xuất nội dung chậm: quy trình truyền thống brief → viết → review → chỉnh sửa → xuất bản mất khoảng 3–7 ngày làm việc, không đủ tốc độ cho marketing theo thời gian thực.

Vấn đề 4 — Khó mở rộng: khi doanh nghiệp mở rộng sang nhiều sản phẩm hoặc thị trường mới, nhu cầu nội dung tăng mạnh nhưng nhân sự không thể tăng theo tỷ lệ tuyến tính.

### 3.3 Cơ hội

Sự phổ biến của LLM và khả năng truy cập qua API mở ra cơ hội xây dựng một nền tảng tự động hóa nội dung, có khả năng hiểu ngữ cảnh thương hiệu, thích ứng với đối tượng mục tiêu và xuất ra nhiều định dạng — tất cả thông qua một giao diện đơn giản, không cần kỹ năng kỹ thuật.

## 4. Kiến trúc giải pháp

### 4.1 Tổng quan

Hệ thống được triển khai trên Amazon Web Services (AWS) theo kiến trúc đa tầng, phù hợp với AWS Well-Architected Framework. Toàn bộ hạ tầng chạy trong một Amazon VPC (10.0.0.0/16) tại khu vực ap-southeast-1 (Singapore), trải dài trên hai Availability Zones (ap-southeast-1a và ap-southeast-1b) nhằm đảm bảo tính sẵn sàng và chịu lỗi tốt.

Frontend React SPA được triển khai trên Amazon S3 Static Website và phân phối qua Amazon CloudFront. Mọi request API đi qua AWS WAF, Amazon API Gateway và Amazon Cognito Authorizer trước khi được chuyển tiếp qua VPC Link tới Application Load Balancer nội bộ. ALB thực hiện health check và phân phối request tới Amazon EC2 Auto Scaling Group chạy trên hai Availability Zones.

Sơ đồ kiến trúc:

![AI Content Generator Platform architecture](/images/5-Workshop/5.1-Workshop-overview/architecture.jpg)

### 4.2 Các thành phần kiến trúc

| Tầng | Thành phần | Vai trò |
|---|---|---|
| Edge & Bảo mật | Amazon CloudFront | Phân phối nội dung toàn cầu (CDN), cache nội dung tĩnh và điều hướng request tới Amazon S3 Static Website và Amazon API Gateway. |
|  | AWS WAF | Bảo vệ ứng dụng khỏi SQL Injection, XSS, DDoS Layer 7 và bot độc hại trước khi request tới API Gateway. |
| API | Amazon API Gateway | Thực hiện xác thực JWT qua Amazon Cognito User Pool Authorizer trước khi chuyển tiếp request đến Application Load Balancer. |
|  | Amazon Cognito | Quản lý User Pool, xác thực người dùng qua JWT và đóng vai trò Authorizer cho API Gateway. |
| Compute | Application Load Balancer | Được triển khai trên hai Availability Zones; nhận request từ API Gateway, thực hiện health check và phân phối tải tới Amazon EC2 Auto Scaling Group. |
|  | Amazon EC2 (Express API) | Xử lý nghiệp vụ cốt lõi: xác thực người dùng, xây dựng prompt từ Brand Persona, truy vấn Amazon RDS PostgreSQL và đưa AI job vào Amazon SQS. |
|  | Auto Scaling Group | Tự động mở rộng hoặc thu nhỏ số lượng EC2 theo tải thực tế. |
| Queue & AI Worker | Amazon SQS (Main Queue) | Nhận AI job từ EC2 để xử lý bất đồng bộ. |
|  | Amazon SQS (Dead Letter Queue) | Ghi nhận các message thất bại qua redrive policy. |
|  | AWS Lambda (Node.js) | Thực hiện worker logic, poll AI job từ SQS, gọi Gemini API và lưu kết quả vào Amazon S3 và Amazon RDS. |
| Networking | NAT Gateway | Cho phép EC2 và Lambda khởi tạo kết nối outbound ra internet mà không cần public IP. |
|  | Internet Gateway | Cung cấp điểm vào/ra của VPC tới internet cho các dịch vụ bên ngoài như Gemini API. |
|  | VPC Endpoint for S3 | Cho phép Lambda ghi output AI lên Amazon S3 qua mạng riêng của AWS. |
| AI | Gemini API (Google AI) | Mô hình LLM sinh nội dung marketing. |
| Data | Amazon RDS PostgreSQL (Multi-AZ) | Lưu trữ người dùng, dữ liệu Brand Persona, lịch sử chiến dịch và trạng thái job. |
|  | Amazon S3 (Static Website) | Lưu trữ React SPA và làm origin cho CloudFront. |
|  | Amazon S3 (Export Bucket) | Lưu các file PDF, DOCX, hình ảnh và tài sản AI sinh ra. |
| Observability | CloudWatch | Thu thập log, metric và alarm từ EC2, Lambda và API Gateway. |
| Security | AWS Secrets Manager | Lưu trữ Gemini API key và thông tin đăng nhập database. |
|  | AWS KMS | Quản lý key mã hóa cho Amazon RDS, Amazon S3 và AWS Secrets Manager. |
|  | AWS IAM | Thực thi nguyên tắc Least Privilege với IAM Role riêng cho EC2 và Lambda. |

### 4.3 Luồng xử lý chính

1. Người dùng truy cập ứng dụng qua Amazon CloudFront.
2. CloudFront phục vụ React SPA từ Amazon S3 Static Website.
3. CloudFront chuyển tiếp request API tới Amazon API Gateway.
4. Amazon API Gateway xác thực JWT thông qua Amazon Cognito Authorizer.
5. Amazon API Gateway chuyển tiếp request tới Application Load Balancer nội bộ.
6. Application Load Balancer phân phối request tới Amazon EC2 Auto Scaling Group.
7. Amazon EC2 xử lý xác thực nghiệp vụ, truy vấn Amazon RDS PostgreSQL, lấy thông tin bí mật từ AWS Secrets Manager và đưa AI job vào Amazon SQS.
8. AWS Lambda poll AI job từ Amazon SQS Main Queue và lấy Gemini API key từ AWS Secrets Manager.
9. AWS Lambda khởi tạo kết nối outbound qua NAT Gateway và gửi prompt tới Gemini API.
10. AWS Lambda lưu kết quả AI vào Amazon S3 export bucket qua VPC Endpoint cho S3.
11. AWS Lambda cập nhật trạng thái job trong Amazon RDS PostgreSQL.
12. Amazon EC2 lấy kết quả từ Amazon RDS và trả response qua Amazon API Gateway, CloudFront và React SPA.

### 4.4 AWS Well-Architected Framework

| Trụ cột | Tập trung |
|---|---|
| Operational Excellence | CloudWatch, CI/CD |
| Security | AWS WAF, IAM Least Privilege, Secrets Manager, KMS, private subnets |
| Reliability | Application Load Balancer, Auto Scaling Group, Multi-AZ RDS, NAT Gateway, SQS DLQ, VPC Endpoint for S3 |
| Performance Efficiency | CloudFront, Lambda, tối ưu RDS |
| Cost Optimization | Auto Scaling, Lambda pay-per-use, lifecycle policy cho S3 |
| Sustainability | Tự động scale theo nhu cầu, tắt môi trường Dev ngoài giờ làm việc |

## 5. Lộ trình triển khai

| Tuần | Mục tiêu | Công việc chính | Mốc đạt được |
|---|---|---|---|
| 9 | Hoàn thiện hạ tầng AWS | Vẽ sơ đồ kiến trúc + VPC + subnet + IAM; RDS Multi-AZ + Secrets Manager; ALB + EC2 ASG; CloudFront + WAF + API Gateway + CI/CD | Ping test: CloudFront → API Gateway → Application Load Balancer → EC2 → RDS |
| 10 | Backend cốt lõi + UI cơ bản | Auth API (JWT + Cognito); CRUD Brand Persona; prompt engine từ brief + persona; React dashboard (UI v1.0) | Đăng nhập, tạo persona, gửi brief, nhận prompt tự động |
| 11 | Luồng AI worker end-to-end | SQS pipeline; Lambda → Gemini API → S3 + RDS; export PDF/DOCX/HTML; load testing & tối ưu | Brief → AI sinh nội dung → export PDF dưới 60 giây |
| 12 | Hardening & production | Security audit (WAF, IAM, pentest); UAT + thu feedback; sửa bug + hoàn thiện docs/runbook; go-live + onboarding | Production live, monitoring 24/7, khách hàng đầu tiên onboard |

## 6. Ngân sách

### 6.1 Chi phí xây dựng

| Dịch vụ | Cấu hình | Chi phí/tháng |
|---|---|---|
| Amazon EC2 | t3.medium × 2 (On-Demand, Auto Scaling min=2, 1/AZ) | ~$60 |
| Amazon RDS PostgreSQL | db.t3.micro, Multi-AZ | ~$50 |
| NAT Gateway | Production: 2 NAT Gateways · Development: 1 NAT Gateway | ~$64 |
| CloudFront | 100 GB transfer | ~$8 |
| API Gateway | 1M requests | ~$3–4/tháng |
| CloudWatch | Logs + metrics cơ bản | ~$5 |
| AWS Lambda | ~100,000 invocations, 512MB | ~$1 |
| Amazon SQS | ~500,000 requests | ~$0.20 |
| Amazon S3 | 50 GB | ~$2 |
| AWS Secrets Manager | 2 secrets (Gemini API key, database credentials) | ~$2/tháng |
| AWS KMS | 1 customer-managed KMS key (dùng cho RDS, S3, Secrets Manager) | ~$1 |
| Amazon Cognito | < 50,000 MAU (Free Tier) | $0 |
| Tổng AWS/tháng |  | ~$196 |

Gemini API (Google AI) ở giai đoạn Dev/Staging ước tính khoảng 1,000 request/tháng, khoảng $1–5/tháng.

### 6.2 Chiến lược tối ưu chi phí

- Reserved Instances: cam kết 1 năm cho EC2 và RDS → tiết kiệm 30–40%.
- Lambda serverless: AI worker chỉ tính phí khi có job, không phát sinh chi phí idle.
- CloudFront caching: giảm số request tới EC2 và giảm băng thông.
- S3 Lifecycle Policy: tự động chuyển file cũ hơn 90 ngày sang S3 Glacier.
- Auto Scaling: thu nhỏ về minimum instances ngoài giờ cao điểm.
- Spot Instances cho Dev: tiết kiệm 60–70% so với On-Demand.

## 7. Rủi ro

### 7.1 Ma trận rủi ro

| Rủi ro | Khả năng | Tác động |
|---|---|---|
| Gemini API downtime/throttling | Trung bình | Cao |
| Chi phí Gemini API vượt ngân sách | Cao | Trung bình |
| Lộ lọt dữ liệu người dùng | Thấp | Rất cao |
| Một EC2 instance bị lỗi (không phải toàn hệ thống — được xử lý bằng ASG đa AZ tự động thay thế) | Trung bình | Thấp |
| RDS failover chậm | Thấp | Trung bình |
| Lambda timeout khi Gemini phản hồi chậm | Trung bình | Trung bình |
| Chi phí AWS vượt ước tính | Trung bình | Thấp |
| Trễ tiến độ Phase 3 (AI Integration) | Trung bình | Thấp |

### 7.2 Biện pháp giảm thiểu

- AWS WAF bảo vệ hệ thống khỏi SQL Injection, XSS và bot.
- Amazon API Gateway sử dụng Cognito Authorizer để xác thực JWT.
- Application Load Balancer nhận request từ API Gateway và phân phối tải tới Amazon EC2 Auto Scaling Group trên hai Availability Zones.
- Amazon EC2, AWS Lambda và Amazon RDS đều chạy trong private subnet.
- AWS Secrets Manager lưu trữ thông tin đăng nhập database và Gemini API key.
- AWS KMS mã hóa Amazon RDS, Amazon S3 và AWS Secrets Manager.
- NAT Gateway và Internet Gateway giới hạn outbound internet chỉ ở những dịch vụ EC2/Lambda cần.
- Amazon VPC Endpoint for S3 cho phép AWS Lambda ghi dữ liệu lên Amazon S3 qua mạng riêng.
- IAM Roles thực thi nguyên tắc Least Privilege.
- Tất cả kết nối sử dụng TLS 1.2 hoặc cao hơn.

## Additional Links

- [AWS-Logo_White-Color](/)
- [1. Worklog](/1-worklog/)
- [2. Project Proposal](/2-proposal/)
- [3. Blog Posts](/3-blogsposted/)
- [4. Events Participated](/4-eventparticipated/)
- [5. Workshop](/5-workshop/)
- [6. Self-Assessment](/6-self-evaluation/)
- [7. Sharing and Feedback](/7-feedback/)
- [AWS Study Group - Blog](https://awsstudygroup.com/)
- [AWS Study Group - FB Group](https://www.facebook.com/groups/awsstudygroupfcj)
- [Clear History](#)
- [First Cloud AI Journey](https://www.facebook.com/groups/660548818043427)