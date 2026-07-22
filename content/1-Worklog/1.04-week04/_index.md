---
title: "Week 04 – Scaling and Content Delivery"
date: 2026-04-20
draft: false
weight: 4
chapter: false
---

## Objectives

* Configure an EC2 Auto Scaling Group with an Application Load Balancer.
* Set up CloudFront for the S3 static website to improve delivery performance.
* Practice basic DNS management with Route 53.
* Understand the three-tier high-availability architecture on AWS.

## Suggested tasks

| Day | Task | Start | End | Reference |
|-----|------|-------|-----|-----------|
| 1 | Create a launch template and an Auto Scaling Group | 2026-05-11 | 2026-05-11 | https://000006.awsstudygroup.com |
| 2 | Attach an Application Load Balancer to the Auto Scaling Group | 2026-05-12 | 2026-05-12 | https://000006.awsstudygroup.com |
| 3 | Test scale-out behavior by increasing CPU load and observing instance launch | 2026-05-13 | 2026-05-13 | https://000006.awsstudygroup.com |
| 4 | Create a CloudFront distribution pointing to the S3 bucket | 2026-05-14 | 2026-05-14 | https://000094.awsstudygroup.com |
| 5 | Configure a Route 53 hosted zone and create an A record | 2026-05-15 | 2026-05-15 | https://000010.awsstudygroup.com |
| 6 | Draw the architecture diagram and update the worklog | 2026-05-16 | 2026-05-16 | Internal docs |

## Key achievements

* Configured the Auto Scaling Group to add instances automatically when CPU usage exceeds 70%.
* Attached an ALB to distribute traffic evenly across instances.
* Set up CloudFront and verified cache hits through the X-Cache response header.
* Created a Route 53 record pointing the domain to the CloudFront distribution.
* Presented a three-tier high-availability architecture diagram to the mentor.

## Notes

Reference: https://cloudjourney.awsstudygroup.com/1-explore/
