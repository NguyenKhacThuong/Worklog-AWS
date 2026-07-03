---
title: "Proposal"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# AI Content Generator Platform
## A Serverless AWS + Gemini API Solution for Automated Marketing Content Generation

### 1. Executive Summary
The **AI Content Generator Platform** is a next-generation SaaS platform that helps small and medium businesses (SMBs) automate their marketing content creation process using Generative AI. The platform combines **AWS Cloud** with the **Gemini API (Google AI)** to deliver a diverse, scalable, and highly secure content-generation solution.

| Criteria | Value |
|---|---|
| Business model | SaaS – Monthly/Annual subscription |
| Target customers | SMBs, Marketing agencies |
| AI technology | Gemini API (Google AI) via AWS Lambda |
| Infrastructure | AWS ap-southeast-1 / ap-southeast-2 |
| Scalability | Auto Scaling – from 10 to 10,000+ users |
| Availability | Multi-AZ, RDS Failover – 99.9% uptime |

### 2. Problem Statement
### Market Context
The Digital Marketing market in Southeast Asia has grown strongly since the COVID-19 pandemic. SMBs face constant pressure to produce multi-channel content, while creative resources remain limited and Copywriter/Agency costs keep rising.

### Core Problems
- **High labor cost** – An average SMB spends $500–$3,000/month on marketing content, and high-quality creative talent is scarce and expensive.
- **Inconsistent branding** – When multiple people or agencies produce content, tone of voice and brand imagery easily diverge, eroding end-customer trust.
- **Slow content production** – The traditional brief → write → review → edit → publish cycle takes **3–7 business days**, too slow for real-time marketing.
- **Difficult to scale** – As a business expands into new products or markets, content demand multiplies but headcount cannot scale linearly.

### The Opportunity
The rise of LLMs and API-based integration makes it possible to build a **content automation platform** that understands brand context, adapts to different audiences, and exports multiple formats — all through one simple, no-code interface.

### The Solution
The system runs on AWS with a multi-tier architecture that clearly separates the Edge, API, Compute, Queue, AI Worker, and Data layers. All compute resources sit inside a **VPC (10.0.0.0/16)** spanning **2 Availability Zones**. A React SPA is served through CloudFront and protected by WAF; API Gateway authenticates requests via Cognito; an Auto Scaling EC2 fleet behind an ALB handles business logic; AI generation jobs are processed asynchronously through SQS and Lambda, which call the Gemini API; results are stored in RDS PostgreSQL and S3.

### Benefits and Return on Investment
- **Time savings:** content creation time shrinks from 3–5 days to **under 30 minutes**.
- **Cost savings:** 60–80% cheaper than hiring a Copywriter/Agency (from $500–3,000/month down to $50–150/month).
- **Brand consistency:** a Brand Persona keeps tone of voice consistent whether generating 10 or 1,000 posts.
- **Easy scaling:** expand across products, markets, and languages without linear headcount growth.

### 3. Solution Architecture
The platform is built on a serverless, multi-tier AWS architecture. Data flows from the React SPA through CloudFront and WAF, is authenticated at API Gateway/Cognito, processed by an Auto Scaling EC2 fleet behind an ALB, and queued via SQS for asynchronous AI processing by Lambda workers calling the Gemini API. Results are persisted in RDS PostgreSQL and S3, with CloudWatch and X-Ray providing full observability.

### AWS Services Used
| Layer | Service | Role |
|---|---|---|
| Networking | Internet Gateway | Connects the VPC to the Internet; inbound/outbound traffic via Public Subnets (ALB, NAT Gateway) |
| Networking | NAT Gateway | Deployed in Public Subnets (2 AZs); lets Lambda/EC2 in Private Subnets reach the Internet (Gemini API) without a public IP |
| Networking | VPC Endpoint (S3) | Private connectivity to S3 without traversing the public Internet, improving security and cutting NAT data-transfer cost |
| Edge & Security | Amazon CloudFront | Global CDN serving the React SPA, caches static content |
| Edge & Security | AWS WAF | Protects against SQL Injection, XSS, bots, and Layer-7 DDoS |
| API | Amazon API Gateway | Accepts requests, applies rate limiting, authenticates via Cognito Authorizer |
| API | Amazon Cognito | User authentication and authorization (User Pool) |
| Compute | Application Load Balancer | Distributes traffic to EC2, automatic health checks, spans 2 AZs |
| Compute | Amazon EC2 (Express API) | Business logic: auth, Brand Persona, prompt building, RDS queries (Private Subnet, no public IP, traffic only via ALB) |
| Compute | Auto Scaling Group | Scales EC2 count with real load, spans 2 Availability Zones for high availability |
| Queue & AI Worker | Amazon SQS (Main Queue) | Receives AI jobs from EC2 for async processing; DLQ enabled via SQS Redrive Policy — failed messages move to the Dead Letter Queue after the Maximum Receive Count |
| Queue & AI Worker | AWS Lambda (Node.js) | Worker running in a VPC Private Subnet, pulls jobs from SQS, reaches the Internet via NAT Gateway to call the Gemini API |
| AI | Gemini API (Google AI) | LLM that generates marketing content |
| Data | Amazon RDS PostgreSQL (Multi-AZ) | Stores users, Brand Personas, campaign history, job status |
| Data | Amazon S3 | Stores exported files (PDF, DOCX, HTML), logos, and brand assets |
| Observability | CloudWatch | Logs, metrics, and alarms across the system |
| Observability | AWS X-Ray | Distributed tracing for end-to-end request tracking |
| Security | AWS Secrets Manager | Stores and issues the Gemini API key to Lambda and other sensitive credentials |
| Security | AWS KMS | Encrypts data at rest (RDS, S3) |
| Security | AWS IAM | Least-privilege access for every service; separate IAM roles for EC2 and Lambda |

**Security Groups:** Traffic is controlled through a chained model, **ALB SG → EC2 SG → RDS SG**: the ALB SG only accepts HTTPS traffic from the Internet (via CloudFront/WAF); the EC2 SG only accepts traffic from the ALB SG; the RDS SG only accepts PostgreSQL connections from the EC2 SG. Lambda sits in its own Security Group, allowed only to make outbound calls via the NAT Gateway and to the RDS SG, following the Least Privilege principle.

### 4. Technical Implementation
**Main Processing Flow**
1. User → React SPA → CloudFront
2. CloudFront → WAF (checks SQL Injection, XSS, bots)
3. WAF → API Gateway (Cognito authentication, rate limiting)
4. API Gateway → ALB → EC2 (Auto Scaling Group)
5. EC2: authenticates the user, builds the prompt from the Brief + Brand Persona, queries RDS, and pushes a job to the SQS Main Queue
6. Lambda Worker: receives the message from SQS, fetches the Gemini API key from Secrets Manager, reaches the Internet via the NAT Gateway, and calls the Gemini API
7. Gemini API generates the content
8. Lambda: saves the result file to S3 via VPC Endpoint and updates job status in RDS. If processing fails after the Maximum Receive Count is reached, the message is automatically moved to the Dead Letter Queue via the SQS Redrive Policy
9. EC2 returns the result to the UI → the user edits and exports the file

**AWS Well-Architected Framework Alignment**
| Pillar | Applied Solution |
|---|---|
| Operational Excellence | CloudWatch Alarms, X-Ray Tracing, automated CI/CD |
| Security | WAF, IAM Least Privilege, Secrets Manager, KMS, Private Subnets |
| Reliability | ALB + Auto Scaling Group (2 AZ), RDS Multi-AZ Failover, SQS Redrive Policy (DLQ), CloudWatch Alarms |
| Performance Efficiency | CloudFront CDN, Serverless Lambda, RDS query optimization |
| Cost Optimization | Lambda pay-per-use, S3 Lifecycle Policy, demand-based Auto Scaling |
| Sustainability | Resources provisioned only as needed; Dev environment shut down off-hours |

### 5. Timeline & Milestones
| Week | Focus | Key Work | Milestone |
|---|---|---|---|
| 9 | Complete AWS infrastructure | VPC + Subnets + IAM; RDS Multi-AZ + Secrets Manager; ALB + EC2 ASG; CloudFront + WAF + API Gateway + CI/CD | Ping test: CloudFront → API GW → ALB → EC2 → RDS succeeds |
| 10 | Backend logic + base UI | Auth API (JWT + Cognito); Brand Persona CRUD; Prompt engine from Brief + Persona; React Dashboard (UI v1.0) | Login, create Persona, submit Brief, receive prompt automatically |
| 11 | End-to-end AI Worker flow | SQS pipeline; Lambda → Gemini API → S3 + RDS; PDF/DOCX/HTML export; load testing & tuning | Brief → AI-generated content → PDF export in under 60 seconds |
| 12 | Hardening & Production | Security audit (WAF, IAM, pentest); UAT + feedback collection; bug fixes + docs/runbook; Go-Live + onboarding | Production live, 24/7 monitoring, first customer onboarded |

### 6. Budget Estimation
### Build/Run Cost
| Service | Configuration | Monthly Cost |
|---|---|---|
| Amazon EC2 | t3.small × 2 (Auto Scaling Group, Multi-AZ) | ~$35–40 |
| Amazon RDS PostgreSQL | db.t3.micro, Multi-AZ | ~$50 |
| NAT Gateway | 2 AZ | ~$64 |
| CloudFront | 100 GB transfer | ~$8 |
| API Gateway | 1M requests | ~$3.50 |
| CloudWatch | Basic logs + metrics | ~$5 |
| AWS Lambda | ~100,000 invocations, 512MB | ~$1 |
| Amazon SQS | ~500,000 requests | ~$0.20 |
| Amazon S3 | 50 GB | ~$2 |
| AWS Secrets Manager | 1 secret (Gemini API Key) | ~$1 |
| AWS KMS | AWS Managed Key (RDS + S3 encryption) | $0 |
| Amazon Cognito | < 50,000 MAU (Free Tier) | $0 |
| **Total AWS/month** | | **~$170–175** |

Gemini API (Google AI) usage during Dev/Staging is estimated at ~1,000 requests/month, roughly $1–5/month.

**Cost optimization notes:** At the MVP stage, the Express API workload doesn't require the CPU/RAM of a **t3.medium**; **t3.small** is sufficient for initial SMB load, paired with an Auto Scaling Group to expand automatically when needed — optimizing cost without hurting performance or availability. Similarly, an **AWS Managed Key** fully satisfies at-rest encryption requirements for RDS and S3 at this stage (no custom key lifecycle control is needed), avoiding the $1/month/CMK fee and simplifying key management.

### Cost Optimization Strategy
- **Reserved Instances:** 1-year commitment on EC2 and RDS → 30–40% savings
- **Serverless Lambda:** the AI Worker only incurs cost per job, no idle charges
- **CloudFront caching:** reduces requests to EC2 and bandwidth usage
- **S3 Lifecycle Policy:** automatically moves files older than 90 days to S3 Glacier
- **Auto Scaling:** scales down to minimum instances outside peak hours
- **Spot Instances for Dev:** 60–70% savings versus On-Demand

### 7. Risk Assessment
#### Risk Matrix
| Risk | Likelihood | Impact |
|---|---|---|
| Gemini API downtime/throttling | Medium | High |
| Gemini API cost overrun | High | Medium |
| User data security breach | Low | Very High |
| Single EC2 instance failure | Low | High |
| Slow RDS failover | Low | Medium |
| Lambda timeout on slow Gemini response | Medium | Medium |
| AWS cost overrun | Medium | Low |
| Phase 3 (AI Integration) schedule slip | Medium | Low |

#### Mitigation Strategies
**Gemini API downtime/throttling**
- Lambda retries with Exponential Backoff (3 attempts, max 5 minutes)
- CloudWatch Alarm on abnormal job-failure spikes
- Fallback to OpenAI API or Amazon Bedrock (Phase 2+)

**Gemini API cost overrun**
- Cap AI calls by plan (Free: 10/month, Basic: 100, Pro: unlimited)
- Rate limiting at API Gateway (requests/minute per user)
- Google Cloud Budget Alert + AWS Cost Anomaly Detection

**User data security breach**
- EC2, Lambda, and RDS run in Private Subnets (no public IP)
- KMS encryption at rest (RDS + S3); all connections over TLS 1.2+
- Secrets Manager fully replaces environment variables for credentials
- WAF blocks SQL Injection, XSS, and bad bots; CloudTrail audits all API calls
- IAM permissions reviewed every 90 days

**Single EC2 instance failure**
- The Application Load Balancer automatically routes traffic to healthy instances
- The Auto Scaling Group automatically launches a replacement EC2 instance
- Service availability is maintained across two Availability Zones

**Lambda timeout on slow Gemini response**
- Lambda timeout set to 270 seconds (buffer below the 300-second max)
- Each job generates only one content type (no batching multiple types per call)
- Streaming responses from the Gemini API where possible
- Timeouts automatically retry with higher priority

**Phase 3 (AI Integration) schedule slip**
- 1-week buffer (Week 12) reserved for performance testing and bug fixing
- Lambda + Gemini API prototyped independently starting Week 2, in parallel with Phase 1
- Gemini API Sandbox (free tier) used during development

### 8. Expected Outcomes
#### Technical Improvements
End-to-end AI content generation replaces manual workflows, cutting content creation time to under 30 minutes with an automated, auditable pipeline built on AWS Well-Architected principles.

#### Long-term Value
A reusable, secure, and scalable SaaS foundation that supports SMB customers from 10 to 10,000+ users, laying the groundwork for future product lines and market expansion.

### References
- AWS Well-Architected (https://aws.amazon.com/architecture/well-architected/)
- Gemini API Docs (https://ai.google.dev/docs)
- Amazon SQS Best Practices (https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/best-practices.html)