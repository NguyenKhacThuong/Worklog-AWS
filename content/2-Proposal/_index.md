---
title: "Project Proposal"
date: 2024-01-01
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# PROJECT PROPOSAL

## 1. Project Overview

AI Content Generator Platform is a next-generation SaaS platform that helps small and medium businesses (SMBs) automate their marketing content creation process using Generative AI. The platform combines AWS Cloud and the Gemini API (Google AI) to deliver a scalable, secure, and versatile content generation solution.

|  |  |
|---|---|
| Business model | SaaS — monthly/annual subscription |
| Target customers | Small and medium businesses (SMBs), marketing agencies |
| AI technology | Gemini API (Google AI) via AWS Lambda |
| AWS Region | ap-southeast-1 (Singapore) |
| Availability Zones | ap-southeast-1a and ap-southeast-1b |
| Scalability | Auto Scaling Group (10–10,000+ users) |
| Availability | Multi-AZ deployment, RDS Multi-AZ failover (99.9% uptime) |

## 2. Objectives

### 2.1 Project objectives

| No. | Objective | Expected outcome |
|---|---|---|
| 1 | Build a complete MVP in 4 weeks (Week 9–12) | Go-live by the end of Week 12 |
| 2 | Achieve high availability for the production system | Uptime ≥ 99.9% |
| 3 | Automate the end-to-end AI content generation flow | < 60 seconds per content piece |
| 4 | Deliver an architecture aligned with the AWS Well-Architected Framework | All 6 pillars covered |
| 5 | Comprehensive security under the Least Privilege principle | No wildcard * permissions |

### 2.2 Value delivered

- Time savings: content creation time is reduced from 3–5 days to under 30 minutes.
- Cost savings: 60–80% lower than hiring a copywriter or agency (from $500–$3,000/month to $50–$150/month).
- Brand consistency: Brand Persona ensures the correct tone of voice whether generating 10 or 1,000 content pieces.
- Easy scaling: expand across products, markets, and languages without linear headcount growth.

## 3. Problem Statement

### 3.1 Market context

The digital marketing market in Southeast Asia has grown rapidly since the COVID-19 pandemic. SMBs face constant pressure to produce multi-channel content, while creative resources remain limited and copywriter/agency costs continue to rise.

### 3.2 Core problems

Problem 1 — High labor cost: an average SMB spends $500–$3,000/month on marketing content, while high-quality creative talent is scarce and expensive.

Problem 2 — Inconsistent branding: when multiple people or agencies produce content, tone of voice and brand imagery easily diverge, eroding end-customer trust.

Problem 3 — Slow content production: the traditional workflow of brief → write → review → revise → publish takes 3–7 business days, which cannot keep up with the pace of real-time marketing.

Problem 4 — Difficult to scale: as the business expands into new products or markets, content demand multiplies, but headcount cannot scale linearly to match.

### 3.3 Opportunity

The rise of LLMs and their API accessibility creates an opportunity to build a content automation platform capable of understanding brand context, adapting to target audiences, and exporting to multiple formats — all through a simple interface that requires no technical skills.

## 4. Solution Architecture

### 4.1 Overview

The system is deployed on Amazon Web Services (AWS) using a multi-tier architecture aligned with the AWS Well-Architected Framework. The entire infrastructure runs inside a single Amazon VPC (10.0.0.0/16) in the ap-southeast-1 (Singapore) region, spanning two Availability Zones (ap-southeast-1a and ap-southeast-1b) to ensure high availability and fault tolerance.

The React SPA frontend is hosted on Amazon S3 Static Website and distributed through Amazon CloudFront. Every API request passes through AWS WAF, Amazon API Gateway, and the Amazon Cognito Authorizer before being forwarded via a VPC Link to an internal Application Load Balancer. The Application Load Balancer performs health checks and distributes requests to the Amazon EC2 Auto Scaling Group deployed across two Availability Zones.

Architecture diagram:

![AI Content Generator Platform architecture](/images/5-Workshop/5.1-Workshop-overview/architecture.jpg)

### 4.2 Architecture components

| Layer | Component | Responsibility |
|---|---|---|
| Edge & Security | Amazon CloudFront | Global content delivery (CDN), caches static content, and routes requests to two origins: Amazon S3 Static Website and Amazon API Gateway. |
|  | AWS WAF | Protects the application from SQL Injection, Cross-Site Scripting (XSS), Layer 7 DDoS, and malicious bots before requests reach API Gateway. |
| API | Amazon API Gateway | Performs JWT validation via the Amazon Cognito User Pool Authorizer before forwarding requests to the Application Load Balancer. |
|  | Amazon Cognito | Manages the User Pool, authenticates users via JWT tokens, and acts as the Authorizer for Amazon API Gateway. |
| Compute | Application Load Balancer | Deployed across two Availability Zones; receives requests from Amazon API Gateway, performs health checks, and distributes load to the Amazon EC2 Auto Scaling Group. |
|  | Amazon EC2 (Express API) | Handles core business logic: user authentication, building prompts from Brand Persona, querying Amazon RDS PostgreSQL, and enqueuing AI jobs to Amazon SQS. |
|  | Auto Scaling Group | Automatically scales the number of EC2 instances based on real load. |
| Queue & AI Worker | Amazon SQS (Main Queue) | Receives AI jobs from EC2 for asynchronous processing. |
|  | Amazon SQS (Dead Letter Queue) | Captures failed messages via a redrive policy. |
|  | AWS Lambda (Node.js) | Runs the worker logic, polls AI jobs from SQS, uses the Gemini API, and stores results in both Amazon S3 and Amazon RDS. |
| Networking | NAT Gateway | Allows EC2 and Lambda to initiate outbound internet connections without a public IP. |
|  | Internet Gateway | Provides the VPC entry/exit point to the internet for external services such as the Gemini API. |
|  | VPC Endpoint for S3 | Lets Lambda write AI output to Amazon S3 over the AWS private network. |
| AI | Gemini API (Google AI) | The LLM that generates marketing content. |
| Data | Amazon RDS PostgreSQL (Multi-AZ) | Stores users, Brand Persona data, campaign history, and job status. |
|  | Amazon S3 (Static Website) | Hosts the React SPA and serves as the origin for CloudFront. |
|  | Amazon S3 (Export Bucket) | Stores generated PDF, DOCX, image files, and other AI-generated assets. |
| Observability | CloudWatch | Collects logs, metrics, and alarms from EC2, Lambda, and API Gateway. |
| Security | AWS Secrets Manager | Stores the Gemini API key and database credentials. |
|  | AWS KMS | Manages encryption keys for Amazon RDS, Amazon S3, and AWS Secrets Manager. |
|  | AWS IAM | Enforces the Least Privilege principle with separate IAM Roles for EC2 and Lambda. |

### 4.3 Main processing flow

1. The user accesses the application through Amazon CloudFront.
2. CloudFront serves the React SPA from Amazon S3 Static Website.
3. CloudFront forwards API requests to Amazon API Gateway.
4. Amazon API Gateway authenticates the JWT via the Amazon Cognito Authorizer.
5. Amazon API Gateway forwards the request to the internal Application Load Balancer.
6. The Application Load Balancer distributes the request to the Amazon EC2 Auto Scaling Group.
7. Amazon EC2 handles business authentication, queries Amazon RDS PostgreSQL, retrieves database credentials from AWS Secrets Manager, and enqueues the AI job into Amazon SQS.
8. AWS Lambda polls the AI job from the Amazon SQS Main Queue and retrieves the Gemini API key from AWS Secrets Manager.
9. AWS Lambda initiates an outbound connection through the NAT Gateway and sends the prompt to the Gemini API.
10. AWS Lambda stores the AI output in the Amazon S3 export bucket via the Amazon VPC Endpoint for S3.
11. AWS Lambda updates the job status in Amazon RDS PostgreSQL.
12. Amazon EC2 retrieves the result from Amazon RDS and returns the response through Amazon API Gateway, CloudFront, and the React SPA.

### 4.4 AWS Well-Architected Framework

| Pillar | Focus |
|---|---|
| Operational Excellence | CloudWatch, CI/CD |
| Security | AWS WAF, IAM Least Privilege, Secrets Manager, KMS, private subnets |
| Reliability | Application Load Balancer, Auto Scaling Group, Multi-AZ RDS, NAT Gateway, SQS DLQ, VPC Endpoint for S3 |
| Performance Efficiency | CloudFront, Lambda, RDS optimization |
| Cost Optimization | Auto Scaling, Lambda pay-per-use, S3 lifecycle policies |
| Sustainability | Scale on demand, shut down Dev environments outside business hours |

## 5. Timeline

| Week | Focus | Key work | Milestone |
|---|---|---|---|
| 9 | Complete AWS infrastructure | Draw architecture diagram + VPC + subnets + IAM; RDS Multi-AZ + Secrets Manager; ALB + EC2 ASG; CloudFront + WAF + API Gateway + CI/CD | Ping test: CloudFront → API Gateway → Application Load Balancer → EC2 → RDS |
| 10 | Core backend + basic UI | Auth API (JWT + Cognito); Brand Persona CRUD; prompt engine from brief + persona; React dashboard (UI v1.0) | Log in, create a persona, submit a brief, receive an auto-generated prompt |
| 11 | End-to-end AI worker flow | SQS pipeline; Lambda → Gemini API → S3 + RDS; PDF/DOCX/HTML export; load testing & optimization | Brief → AI generates content → export to PDF in under 60 seconds |
| 12 | Hardening & production | Security audit (WAF, IAM, pentest); UAT + feedback collection; bug fixes + finalize docs/runbook; go-live + onboarding | Production live, 24/7 monitoring, first customer onboarded |

## 6. Budget

### 6.1 Build cost

| Service | Configuration | Monthly cost |
|---|---|---|
| Amazon EC2 | t3.medium × 2 (On-Demand, Auto Scaling min=2, 1/AZ) | ~$60 |
| Amazon RDS PostgreSQL | db.t3.micro, Multi-AZ | ~$50 |
| NAT Gateway | Production: 2 NAT Gateways · Development: 1 NAT Gateway | ~$64 |
| CloudFront | 100 GB transfer | ~$8 |
| API Gateway | 1M requests | ~$3–4/month |
| CloudWatch | Basic logs + metrics | ~$5 |
| AWS Lambda | ~100,000 invocations, 512MB | ~$1 |
| Amazon SQS | ~500,000 requests | ~$0.20 |
| Amazon S3 | 50 GB | ~$2 |
| AWS Secrets Manager | 2 secrets (Gemini API key, database credentials) | ~$2/month |
| AWS KMS | 1 customer-managed KMS key (used by RDS, S3, Secrets Manager) | ~$1 |
| Amazon Cognito | < 50,000 MAU (Free Tier) | $0 |
| Total AWS/month |  | ~$196 |

Gemini API (Google AI) usage during Dev/Staging is estimated at about 1,000 requests/month, around $1–5/month.

### 6.2 Cost optimization strategy

- Reserved Instances: 1-year commitment for EC2 and RDS → 30–40% savings.
- Lambda serverless: the AI worker is billed only per job, with no idle cost.
- CloudFront caching: reduces the number of requests reaching EC2 and lowers bandwidth usage.
- S3 Lifecycle Policy: automatically moves files older than 90 days to S3 Glacier.
- Auto Scaling: scales down to minimum instances outside peak hours.
- Spot Instances for Dev: 60–70% savings versus On-Demand.

## 7. Risks

### 7.1 Risk matrix

| Risk | Likelihood | Impact |
|---|---|---|
| Gemini API downtime/throttling | Medium | High |
| Gemini API cost exceeding budget | High | Medium |
| User data security breach | Low | Very high |
| A single EC2 instance failure (not the whole system — mitigated by the multi-AZ Auto Scaling Group’s automatic replacement) | Medium | Low |
| Slow RDS failover | Low | Medium |
| Lambda timeout when Gemini responds slowly | Medium | Medium |
| AWS cost exceeding estimates | Medium | Low |
| Phase 3 (AI Integration) schedule delay | Medium | Low |

### 7.2 Mitigation measures

- AWS WAF protects the system from SQL Injection, XSS, and bots.
- Amazon API Gateway uses the Cognito Authorizer to validate JWTs.
- The Application Load Balancer receives requests from Amazon API Gateway and distributes traffic to the Amazon EC2 Auto Scaling Group across two Availability Zones.
- Amazon EC2, AWS Lambda, and Amazon RDS all run in private subnets.
- AWS Secrets Manager stores database credentials and the Gemini API key.
- AWS KMS encrypts Amazon RDS, Amazon S3, and AWS Secrets Manager.
- The NAT Gateway and Internet Gateway restrict outbound internet access to only what EC2/Lambda need for external services.
- The Amazon VPC Endpoint for S3 lets AWS Lambda write data to Amazon S3 over the AWS private network.
- IAM Roles enforce the Least Privilege principle.
- All connections use TLS 1.2 or higher.

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