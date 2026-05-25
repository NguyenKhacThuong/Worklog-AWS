---
title: "Week 04 – Scaling & Content Delivery"
date: 2026-04-20
draft: false
weight: 4
chapter: false
---

## Objectives

* Configure EC2 Auto Scaling Group with an Application Load Balancer.
* Set up CloudFront CDN for the S3 static website.
* Practice Route 53 for basic DNS management.
* Understand the 3-tier High Availability architecture on AWS.

### Tasks

| Day | Task | Start | End | Reference |
|-----|------|-------|-----|-----------|
| 1 | Create Launch Template and Auto Scaling Group | 2026-05-11 | 2026-05-11 | https://000006.awsstudygroup.com |
| 2 | Attach Application Load Balancer to Auto Scaling Group | 2026-05-12 | 2026-05-12 | https://000006.awsstudygroup.com |
| 3 | Test scale-out: stress CPU, observe new instances launching | 2026-05-13 | 2026-05-13 | https://000006.awsstudygroup.com |
| 4 | Create CloudFront distribution pointing to S3 | 2026-05-14 | 2026-05-14 | https://000094.awsstudygroup.com |
| 5 | Configure Route 53 hosted zone, create A record | 2026-05-15 | 2026-05-15 | https://000010.awsstudygroup.com |
| 6 | Draw architecture diagram, update worklog | 2026-05-16 | 2026-05-16 | Internal docs |

### Achievements

* Configured Auto Scaling Group to automatically add instances when CPU > 70%.
* Attached ALB to distribute traffic evenly across instances.
* Set up CloudFront and verified cache hits via the X-Cache response header.
* Created a Route 53 record pointing the domain to the CloudFront distribution.
* Drew and presented a 3-tier High Availability architecture diagram to the mentor.

### Notes

Reference: https://cloudjourney.awsstudygroup.com/1-explore/
