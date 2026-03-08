# DevOps and IaC Prompt Templates

## Module 08: AI for Software Development and Security

> DevOps and Infrastructure as Code prompt templates for Docker, Kubernetes, Terraform, and CI/CD.

---

## Table of Contents

1. [Docker Prompts](#1-docker-prompts)
2. [Kubernetes Prompts](#2-kubernetes-prompts)
3. [Terraform Prompts](#3-terraform-prompts)
4. [CI/CD Pipeline Prompts](#4-cicd-pipeline-prompts)
5. [Monitoring and Observability Prompts](#5-monitoring-and-observability-prompts)
6. [Cloud Architecture Prompts](#6-cloud-architecture-prompts)
7. [Scripting and Automation Prompts](#7-scripting-and-automation-prompts)

---

## 1. Docker Prompts

### 1.1 Production Dockerfile Generator

```
Write a production-ready Dockerfile for a [LANGUAGE/FRAMEWORK] application:

Application details:
- Language: [e.g., Python 3.12]
- Framework: [e.g., FastAPI]
- Package manager: [e.g., Poetry / pip / npm / pnpm]
- Application entry point: [e.g., uvicorn main:app]
- Port: [e.g., 8000]
- System dependencies: [e.g., PostgreSQL client, ImageMagick]
- Static files: [yes/no, build step needed?]

Requirements:
- Multi-stage build (builder + runtime)
- Pin base image with SHA digest
- Non-root user (UID 1000)
- Minimal image size (use slim/alpine/distroless)
- Production-only dependencies (no dev/test packages)
- Proper layer ordering for cache optimization
- HEALTHCHECK instruction
- Proper signal handling (PID 1 / tini)
- Labels: maintainer, version, description
- .dockerignore file
- No secrets or credentials in the image
- Environment variables for runtime configuration

Generate the Dockerfile and .dockerignore.
```

### 1.2 Docker Compose for Development

```
Write a Docker Compose file for local development:

Services needed:
1. [Application] — language: [X], port: [Y], hot reload: yes
2. [Database] — type: [PostgreSQL/MySQL/MongoDB], with persistent volume
3. [Cache] — type: [Redis/Memcached]
4. [Queue] — type: [RabbitMQ/Kafka] (if needed)
5. [Object Storage] — MinIO (S3-compatible)
6. [Email] — Mailpit (email testing)
7. [Admin UI] — pgAdmin/Mongo Express/RedisInsight

Requirements:
- Named volumes for data persistence
- Shared network between all services
- Health checks on all services
- Environment variables from .env file
- Dependency ordering (app waits for DB to be healthy)
- Resource limits
- Development optimizations:
  - Source code volume mount for hot reload
  - Debug ports exposed
  - Seed data initialization
  - Log output to stdout

Also generate:
- .env.example with all required variables
- Makefile with common commands (up, down, logs, shell, test, migrate)
```

### 1.3 Docker Security Audit

```
Review this Dockerfile for security issues:

```dockerfile
[paste Dockerfile]
```

Check for:
1. Running as root
2. Using unpinned or latest base images
3. Installing unnecessary packages
4. Copying secrets or credentials into the image
5. Missing HEALTHCHECK
6. Excessive capabilities
7. Not using multi-stage builds
8. Package manager caches not cleaned
9. Sensitive build arguments
10. Missing .dockerignore for sensitive files

Also check the docker-compose.yml:
```yaml
[paste docker-compose.yml]
```

Check for:
1. Exposed ports that should be internal only
2. Missing resource limits
3. Hardcoded secrets (should use docker secrets)
4. Privileged mode unnecessarily enabled
5. Host network mode security implications

Provide the hardened versions of both files.
```

### 1.4 Multi-Architecture Build

```
Write a Docker build configuration for multi-architecture support:

Application: [description]
Target architectures: amd64, arm64

Provide:
1. Dockerfile optimized for multi-arch (no architecture-specific commands)
2. GitHub Actions workflow for multi-arch build with buildx
3. Docker Compose override for development on ARM (Apple Silicon)
4. Performance considerations for each architecture
```

---

## 2. Kubernetes Prompts

### 2.1 Complete Application Deployment

```
Write Kubernetes manifests for deploying [APPLICATION]:

Application specs:
- Container image: [registry/image:tag]
- Port: [container port]
- Replicas: [count]
- Resource requirements: CPU [request/limit], Memory [request/limit]
- Health check endpoint: [path]
- Environment configuration: [list env vars]
- Secrets needed: [list secrets]
- Storage needs: [persistent volumes if any]

Generate these manifests:
1. **Namespace** — with labels and annotations
2. **Deployment** — with:
   - Rolling update strategy
   - Resource requests and limits
   - Liveness and readiness probes
   - Security context (non-root, read-only FS, drop capabilities)
   - Anti-affinity (spread across nodes)
   - Topology spread constraints
3. **Service** — ClusterIP with proper selectors
4. **Ingress** — with TLS (cert-manager annotation)
5. **ConfigMap** — for non-sensitive configuration
6. **Secret** — for sensitive configuration (template, not actual values)
7. **HPA** — Horizontal Pod Autoscaler (CPU 70%, min/max replicas)
8. **PDB** — Pod Disruption Budget (minAvailable)
9. **NetworkPolicy** — restrict ingress/egress
10. **ServiceAccount** — with RBAC (if needed)

Each manifest must include:
- Proper labels (app, version, environment, team)
- Annotations for monitoring and documentation
- Comments explaining non-obvious configurations
```

### 2.2 Helm Chart Generator

```
Create a Helm chart for a generic microservice:

Chart name: [name]
Values to make configurable:
- image.repository, image.tag, image.pullPolicy
- replicaCount
- resources.requests/limits (CPU, memory)
- service.type, service.port
- ingress.enabled, ingress.host, ingress.tls
- env (plain and secret)
- autoscaling.enabled, autoscaling.minReplicas, autoscaling.maxReplicas
- podDisruptionBudget.enabled, podDisruptionBudget.minAvailable
- nodeSelector, tolerations, affinity
- serviceAccount.create, serviceAccount.name
- monitoring.enabled (ServiceMonitor for Prometheus)

Generate:
1. Chart.yaml
2. values.yaml (with sensible defaults)
3. values-dev.yaml, values-staging.yaml, values-prod.yaml (environment overrides)
4. templates/deployment.yaml
5. templates/service.yaml
6. templates/ingress.yaml
7. templates/configmap.yaml
8. templates/secret.yaml
9. templates/hpa.yaml
10. templates/pdb.yaml
11. templates/servicemonitor.yaml
12. templates/_helpers.tpl
13. templates/NOTES.txt
14. templates/tests/test-connection.yaml
```

### 2.3 Kubernetes Troubleshooting

```
My Kubernetes [RESOURCE TYPE] is having issues:

Problem: [describe the problem — CrashLoopBackOff, Pending, ImagePullBackOff,
OOMKilled, Evicted, connection refused, etc.]

kubectl describe output:
```
[paste kubectl describe output]
```

kubectl logs output:
```
[paste kubectl logs output, including previous container logs if applicable]
```

kubectl get events:
```
[paste relevant events]
```

Manifest:
```yaml
[paste the relevant YAML manifest]
```

Please:
1. Diagnose the root cause from the evidence
2. Provide the specific fix (updated manifest or kubectl commands)
3. What additional commands should I run for more information?
4. What monitoring/alerting would catch this earlier?
5. Is there a design issue that should be addressed?
```

### 2.4 Kubernetes Network Policy

```
Design NetworkPolicies for a microservices application:

Services:
1. Frontend (nginx, port 80) — accessible from ingress controller only
2. API Gateway (port 8080) — accessible from frontend and external (via ingress)
3. User Service (port 8081) — accessible from API Gateway only
4. Order Service (port 8082) — accessible from API Gateway only
5. Payment Service (port 8083) — accessible from Order Service only
6. Database (PostgreSQL, port 5432) — accessible from User, Order, Payment services only
7. Redis (port 6379) — accessible from API Gateway and all services

Generate NetworkPolicy manifests that implement:
- Default deny all ingress and egress
- Specific allow rules for each service's required communication
- DNS egress allowed for all pods
- External API egress allowed for Payment Service only

Include comments explaining each policy.
```

### 2.5 Kubernetes Operators and CRDs

```
Design a Kubernetes Custom Resource Definition (CRD) and operator for:

Use case: [e.g., "Managing database backups", "Scheduling canary deployments",
"Managing feature flags"]

CRD specification:
- API group: [e.g., mycompany.io]
- Resource name: [e.g., DatabaseBackup]
- Spec fields: [list configurable fields]
- Status fields: [list status tracking fields]

Generate:
1. CRD YAML manifest
2. Example Custom Resource YAML
3. Operator logic description (reconciliation loop)
4. RBAC for the operator (ServiceAccount, ClusterRole, ClusterRoleBinding)
5. Operator deployment manifest
```

---

## 3. Terraform Prompts

### 3.1 AWS VPC Module

```
Write a Terraform module for an AWS VPC:

Requirements:
- Configurable CIDR block (default: 10.0.0.0/16)
- 3 AZs with public, private, and database subnets
- NAT Gateway (configurable: one per AZ or single)
- Internet Gateway
- Route tables for each subnet tier
- VPC Flow Logs (CloudWatch)
- VPC Endpoints (S3, DynamoDB gateway; ECR, SSM, CloudWatch interface)
- DNS resolution enabled
- Standard tagging

Provide:
1. main.tf
2. variables.tf (with descriptions, types, defaults, validation)
3. outputs.tf (VPC ID, subnet IDs by tier, NAT gateway IPs, route table IDs)
4. versions.tf (required providers)
5. locals.tf (computed values)
6. Example usage in a root module
```

### 3.2 AWS ECS Fargate Service

```
Write Terraform for an ECS Fargate service:

Application:
- Container image: [ECR repository URL]
- Port: [container port]
- CPU: [256/512/1024/2048/4096]
- Memory: [512/1024/2048/4096/8192]
- Desired count: [number]
- Health check path: [path]

Resources to create:
1. ECS Cluster (with Container Insights enabled)
2. Task Definition (with logging to CloudWatch)
3. ECS Service (with deployment circuit breaker)
4. Application Load Balancer (with HTTPS)
5. Target Group (with health checks)
6. Security Groups (ALB and ECS tasks)
7. IAM Roles (task role and execution role)
8. Auto Scaling (CPU and memory targets)
9. CloudWatch Log Group (with retention)
10. Service Discovery (optional, for inter-service communication)

Variables for:
- Environment (dev/staging/prod)
- Container configuration
- Scaling parameters
- Network configuration (VPC, subnets)
- Domain name and certificate ARN
```

### 3.3 AWS RDS with Terraform

```
Write Terraform for a production PostgreSQL RDS instance:

Requirements:
- PostgreSQL 16
- Multi-AZ for production, single-AZ for non-prod
- Encrypted storage (KMS)
- Automated backups (7-day retention for prod, 1-day for non-prod)
- Parameter group with performance tuning
- Subnet group (private subnets only)
- Security group (allow from application security group only)
- Enhanced monitoring
- Performance Insights enabled
- IAM authentication enabled
- CloudWatch alarms for CPU, memory, connections, storage

Provide:
1. main.tf (RDS instance, parameter group, subnet group, security group)
2. variables.tf (instance class, storage, passwords, environment toggles)
3. outputs.tf (endpoint, port, database name)
4. monitoring.tf (CloudWatch alarms)

Include environment-specific configurations:
- dev: db.t3.micro, 20GB, single-AZ, 1-day backup
- staging: db.t3.small, 50GB, single-AZ, 3-day backup
- prod: db.r6g.large, 100GB, multi-AZ, 7-day backup, read replica
```

### 3.4 Terraform State Management

```
Write Terraform configuration for remote state management:

Requirements:
- S3 backend for state storage
- DynamoDB for state locking
- State file encryption (KMS)
- Separate state per environment
- State bucket with versioning
- Access logging on state bucket
- Prevent accidental state deletion

Provide:
1. Bootstrap script (create S3 bucket and DynamoDB table before Terraform init)
2. Backend configuration for each environment
3. IAM policy for state access (least privilege)
4. State import procedure (for existing resources)
5. State migration procedure (moving between backends)
```

### 3.5 Terraform Module Testing

```
Write Terratest tests (in Go) for a Terraform module:

Module: [describe the module — e.g., VPC module, ECS module]

Tests:
1. Plan validation — Module plans without errors
2. Resource creation — Module creates expected resources
3. Output validation — Module outputs have expected values
4. Security validation — Resources have required security settings
5. Idempotency — Applying twice produces no changes
6. Destroy — All resources are properly cleaned up

Include:
- Test setup (random naming, test AWS account)
- Assertions for each resource
- Cleanup (defer destroy)
- CI integration (how to run in pipeline)
- Test timeout configuration
```

---

## 4. CI/CD Pipeline Prompts

### 4.1 GitHub Actions — Complete Pipeline

```
Write a GitHub Actions CI/CD pipeline for a [LANGUAGE/FRAMEWORK] application:

Stages:
1. **Lint** — [linting tools]
2. **Type Check** — [type checking tools]
3. **Unit Test** — [testing framework], with coverage report
4. **Integration Test** — [with service containers: DB, Redis, etc.]
5. **Security Scan** — dependency audit, SAST, container scan
6. **Build** — Docker image build and push to [registry]
7. **Deploy Staging** — [deployment method]
8. **Smoke Test** — [test against staging]
9. **Deploy Production** — [deployment method with approval]
10. **Post-Deploy** — [verification and notification]

Requirements:
- Reusable workflows for common steps
- Matrix strategy for testing multiple versions
- Caching for dependencies and Docker layers
- Concurrency groups (prevent parallel deploys)
- Environment protection rules (manual approval for prod)
- OIDC authentication to cloud provider
- Artifact sharing between jobs
- Slack notification on failure
- Automatic rollback on failed smoke test
- Branch protection integration

Generate:
1. .github/workflows/ci.yml (runs on PR)
2. .github/workflows/deploy.yml (runs on merge to main)
3. .github/workflows/security.yml (runs on schedule)
4. .github/workflows/reusable-build.yml (reusable workflow)
```

### 4.2 GitLab CI Pipeline

```
Write a GitLab CI pipeline (.gitlab-ci.yml) for the same application:

Include GitLab-specific features:
- Stages: lint, test, security, build, deploy-staging, deploy-production
- include: templates for SAST, dependency scanning
- rules: for conditional job execution
- needs: for DAG optimization
- cache: for dependency caching
- services: for test databases
- environments: with URLs and auto-stop
- review apps: for merge request environments
- manual gates: for production deployment
- artifacts: for test reports and coverage
- variables: with environment-specific values

Generate the complete .gitlab-ci.yml with all stages.
```

### 4.3 CI/CD Pipeline Optimization

```
Optimize this CI/CD pipeline:

Current pipeline:
```yaml
[paste current pipeline YAML]
```

Current execution time: [X minutes]
Target execution time: [Y minutes]

Problems:
- [e.g., "Tests take 15 minutes"]
- [e.g., "Docker build is slow even with cache"]
- [e.g., "Deployment takes 10 minutes"]

Optimize for:
1. **Speed** — Reduce total execution time
   - Parallelization opportunities
   - Caching improvements
   - Test splitting and parallel execution
   - Docker layer caching
   - Dependency caching

2. **Cost** — Reduce compute usage
   - Right-size runners
   - Eliminate redundant steps
   - Conditional job execution
   - Spot/preemptible instances

3. **Reliability** — Reduce flaky failures
   - Retry strategies for flaky tests
   - Timeout configuration
   - Error handling

4. **Security** — Harden the pipeline
   - Secret management
   - Minimal permissions
   - Supply chain security
   - Artifact signing
```

### 4.4 Release Management

```
Design a release management workflow:

Application: [monorepo / multi-repo]
Versioning: [SemVer / CalVer]
Release cadence: [weekly / bi-weekly / continuous]

Provide:
1. Branch strategy (trunk-based / GitFlow / feature branches)
2. Version bumping automation
3. Changelog generation
4. Release notes template
5. Tag and release creation
6. Artifact publishing
7. Deployment promotion (staging -> production)
8. Hotfix procedure
9. Rollback procedure
10. Communication (Slack/email notifications)

Generate:
- GitHub Actions workflow for release process
- Changelog generation script
- Version bump script
- Release checklist
```

---

## 5. Monitoring and Observability Prompts

### 5.1 Prometheus Alert Rules

```
Write Prometheus alert rules for a web application:

Application details:
- Type: [API / web app / worker]
- SLOs: p99 latency [X]ms, error rate < [Y]%, availability [Z]%
- Expected RPS: [requests per second]

Generate PrometheusRule resources for:
1. High error rate (5xx responses)
2. High latency (p99 exceeding SLO)
3. Pod crash loops
4. High CPU usage
5. High memory usage
6. Database connection pool exhaustion
7. Queue depth growing
8. Disk space low
9. Certificate expiry approaching
10. Deployment failure
11. SLO burn rate (multi-window, multi-burn-rate)
12. Horizontal pod autoscaler at max

For each alert:
- Expression with appropriate thresholds
- For duration (how long before alerting)
- Labels (severity, team, service)
- Annotations (summary, description, runbook_url, dashboard_url)
- Warning and critical thresholds
```

### 5.2 Grafana Dashboard

```
Design a Grafana dashboard for a microservice:

Service: [description]
Data source: Prometheus

Dashboard sections:
1. **Overview Row** — Key metrics at a glance
   - Request rate (RPS)
   - Error rate (%)
   - p50/p95/p99 latency
   - Active instances

2. **RED Metrics Row** — Rate, Errors, Duration
   - Request rate by endpoint
   - Error rate by endpoint and status code
   - Latency distribution by endpoint

3. **Resource Usage Row**
   - CPU usage by pod
   - Memory usage by pod
   - Network I/O

4. **Dependencies Row**
   - Database query rate and latency
   - Cache hit/miss ratio
   - External API call rate and latency

5. **Business Metrics Row**
   - [Business-specific metrics]

Provide the dashboard as JSON (Grafana dashboard model).
Include template variables for namespace and pod selection.
```

### 5.3 Structured Logging

```
Design a structured logging strategy:

Application: [language/framework]

Provide:
1. Log format specification (JSON with standard fields)
2. Required fields: timestamp, level, message, service, request_id, user_id
3. Log levels and when to use each (DEBUG, INFO, WARN, ERROR, FATAL)
4. Sensitive data filtering (PII, secrets)
5. Request context propagation
6. Log correlation with traces and metrics
7. Performance considerations (async logging, sampling)
8. Log rotation and retention configuration
9. Example logging implementation in [LANGUAGE]
10. Useful log queries for common debugging scenarios
```

---

## 6. Cloud Architecture Prompts

### 6.1 AWS Well-Architected Review

```
Perform an AWS Well-Architected review for:

Architecture:
[describe your AWS architecture — services, networking, data flow]

Review against the 6 pillars:

1. **Operational Excellence**
   - Infrastructure as Code coverage
   - Deployment automation
   - Monitoring and observability
   - Incident management

2. **Security**
   - IAM best practices
   - Network security
   - Data protection
   - Detection and response

3. **Reliability**
   - Fault isolation
   - Recovery procedures
   - Capacity planning
   - Change management

4. **Performance Efficiency**
   - Resource selection
   - Scaling strategy
   - Performance monitoring
   - Optimization opportunities

5. **Cost Optimization**
   - Right-sizing
   - Reserved/spot instance usage
   - Unused resource identification
   - Cost allocation and tracking

6. **Sustainability**
   - Resource efficiency
   - Managed services usage
   - Data lifecycle management

For each pillar:
- Current maturity (1-5)
- Top 3 recommendations
- Estimated effort and impact
```

### 6.2 Multi-Region Architecture

```
Design a multi-region architecture for:

Application: [description]
Primary region: [e.g., us-east-1]
Secondary region: [e.g., eu-west-1]
Active-Active or Active-Passive: [choice]

Requirements:
- RPO: [recovery point objective]
- RTO: [recovery time objective]
- Data sovereignty: [any data residency requirements]
- Latency: [latency requirements for each region]

Design:
1. Compute: How are applications deployed in each region?
2. Database: Replication strategy (read replicas, multi-master)
3. Storage: S3 cross-region replication
4. CDN: CloudFront with regional origins
5. DNS: Route 53 routing policy (latency, failover, geolocation)
6. Networking: Transit Gateway, VPC peering
7. Messaging: Cross-region event replication
8. Monitoring: Centralized vs per-region
9. Failover: Automated vs manual, procedure and testing
10. Cost: Estimated cost for each region

Provide Terraform for the multi-region infrastructure.
```

---

## 7. Scripting and Automation Prompts

### 7.1 Database Backup Script

```
Write a Bash script for PostgreSQL database backups:

Requirements:
- Take logical backup using pg_dump
- Compress with gzip
- Upload to S3 with server-side encryption
- Retain last 7 daily, 4 weekly, and 12 monthly backups
- Verify backup integrity (pg_restore --list)
- Send notification on success/failure (Slack webhook)
- Logging with timestamps
- Error handling (exit on failure, cleanup on error)
- Support for multiple databases
- Configurable via environment variables
- Run as a cron job or Kubernetes CronJob

Generate:
1. backup.sh script
2. restore.sh script (point-in-time restore)
3. Kubernetes CronJob manifest
4. Monitoring (alert if backup age > 25 hours)
```

### 7.2 Environment Setup Script

```
Write a setup script for a new developer joining the team:

Environment: macOS / Linux

The script should:
1. Check and install prerequisites (Homebrew, Docker, Git)
2. Install required languages (Python, Node.js, Go) using version managers
3. Install required tools (kubectl, terraform, awscli, helm)
4. Clone all required repositories
5. Set up local development environment (Docker Compose up)
6. Run database migrations
7. Seed test data
8. Verify everything works (run health checks)
9. Print a summary of what was set up and next steps

Requirements:
- Idempotent (safe to run multiple times)
- Cross-platform (macOS and Linux)
- Interactive (ask for confirmation before major steps)
- Colorized output for readability
- Detailed error messages
- Takes < 15 minutes on a fresh machine (with good internet)
```

### 7.3 Deployment Script

```
Write a deployment script for [APPLICATION]:

Deployment target: [ECS / Kubernetes / EC2 / Lambda]

Steps:
1. Validate prerequisites (AWS CLI configured, kubectl context correct)
2. Run pre-deployment checks (tests passing, no critical vulnerabilities)
3. Build and push Docker image (with git SHA tag)
4. Deploy to [target] with zero-downtime strategy
5. Wait for health checks to pass
6. Run smoke tests against the new deployment
7. If smoke tests fail: automatic rollback
8. If smoke tests pass: notify team (Slack)
9. Update deployment record (who, when, what version)

Requirements:
- Dry-run mode (--dry-run flag)
- Rollback command (deploy rollback --version <tag>)
- Environment parameter (--env staging|production)
- Verbose mode (--verbose)
- Confirmation prompt for production
- Timeout for health checks
- Colorized output
```

### 7.4 Infrastructure Audit Script

```
Write a script to audit AWS infrastructure:

Checks:
1. S3 buckets with public access
2. Security groups with 0.0.0.0/0 ingress
3. IAM users with console access and no MFA
4. IAM access keys older than 90 days
5. EC2 instances without tags (Owner, Environment)
6. RDS instances without encryption
7. RDS instances publicly accessible
8. EBS volumes not encrypted
9. CloudTrail not enabled in all regions
10. Root account with access keys

Output:
- Console output with color-coded severity
- JSON report for automated processing
- CSV report for sharing with management
- Slack notification if critical findings

Generate using AWS CLI and jq.
Include instructions to run as a scheduled Lambda.
```

---

## Usage Guide

### Getting the Best Results

1. **Be specific about your environment**: Include cloud provider, region, existing infrastructure, and team expertise.

2. **Include security requirements**: Every IaC prompt should explicitly mention security considerations.

3. **Specify environments**: Most infrastructure needs dev/staging/prod variations. Ask for all of them.

4. **Request cost estimates**: Always ask for infrastructure cost estimates to avoid surprises.

5. **Ask for testing**: Infrastructure code should be tested. Request Terratest, checkov, or kubeval validation.

6. **Include monitoring**: Every infrastructure component should have associated monitoring and alerting.

### Prompt Chaining for Infrastructure Projects

```
1. Start: Architecture Design prompt (architecture-design-prompts.md)
2. Then: VPC/Network Terraform (3.1)
3. Then: Database Terraform (3.3)
4. Then: Application Deployment — ECS (3.2) or K8s (2.1)
5. Then: CI/CD Pipeline (4.1 or 4.2)
6. Then: Monitoring (5.1 + 5.2)
7. Finally: Security Audit (Docker 1.3, Cloud 6.1)
```
