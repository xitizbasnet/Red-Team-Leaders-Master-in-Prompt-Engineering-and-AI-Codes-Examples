# Architecture Design Prompt Templates

## Module 08: AI for Software Development and Security

> Architecture design prompt templates with example outputs and evaluation criteria.

---

## Table of Contents

1. [System Design Prompts](#1-system-design-prompts)
2. [Architecture Pattern Selection](#2-architecture-pattern-selection)
3. [Database Architecture](#3-database-architecture)
4. [API Design](#4-api-design)
5. [Scalability Analysis](#5-scalability-analysis)
6. [Architecture Decision Records](#6-architecture-decision-records)
7. [Architecture Review](#7-architecture-review)
8. [Migration and Evolution](#8-migration-and-evolution)

---

## 1. System Design Prompts

### Template 1.1: Complete System Design

```
Design a complete system architecture for [SYSTEM NAME]:

### Business Context
- What the system does: [one paragraph description]
- Primary users: [user types and their needs]
- Revenue model: [how the business makes money]
- Competitive advantage: [what must be excellent]

### Functional Requirements
1. [FR-001] [Requirement description]
2. [FR-002] [Requirement description]
3. [FR-003] [Requirement description]
[... list all critical requirements]

### Non-Functional Requirements
- **Availability**: [target uptime, e.g., 99.9%]
- **Latency**: [p50, p95, p99 targets per operation]
- **Throughput**: [requests/sec, messages/sec, data volume]
- **Data durability**: [acceptable data loss window]
- **Consistency**: [strong, eventual, causal]
- **Security**: [compliance, data classification]
- **Cost**: [budget constraints]

### Scale Parameters
- Users: [current and projected]
- Data: [current volume and growth rate]
- Traffic: [daily patterns, peak multiplier]
- Geographic distribution: [regions]

### Constraints
- Team: [size, expertise, hiring plans]
- Timeline: [milestones and deadlines]
- Budget: [infrastructure budget]
- Existing systems: [integration requirements]
- Technology preferences/mandates: [any imposed choices]

### Expected Deliverables
1. High-level architecture diagram (textual description)
2. Component inventory with responsibilities
3. Data flow for top 3 user journeys
4. Technology selection with justification
5. Data storage strategy
6. Communication patterns (sync/async)
7. Deployment architecture
8. Key trade-offs and risks
9. Phased implementation roadmap
```

### Template 1.2: URL Shortening Service

```
Design a URL shortening service (like bit.ly):

Scale:
- 100 million URLs created per month
- 10:1 read-to-write ratio (1 billion redirects per month)
- URLs expire after 5 years by default (configurable)
- Global users, sub-100ms redirect latency

Features:
- Shorten URL with optional custom alias
- Redirect with analytics tracking (country, device, referrer)
- Link analytics dashboard (click count, geographic distribution, time series)
- API access with rate limiting
- Link expiration and deletion
- QR code generation

Constraints:
- Team of 5 engineers
- AWS infrastructure
- $10K/month infrastructure budget

Provide:
1. Architecture with all components
2. Short URL generation algorithm (base62 vs hash vs counter)
3. Database choice and schema
4. Caching strategy for hot URLs
5. Analytics pipeline design
6. Global latency optimization (CDN, edge)
7. Cost estimate
```

### Template 1.3: Real-Time Chat System

```
Design a real-time messaging system:

Scale:
- 50 million registered users
- 5 million daily active users
- 100K concurrent WebSocket connections at peak
- Average message size: 500 bytes
- Messages delivered in <200ms

Features:
- One-on-one messaging
- Group chats (up to 500 members)
- Read receipts and typing indicators
- Message search (last 2 years)
- File sharing (images, documents up to 100MB)
- Push notifications (mobile)
- End-to-end encryption (optional per chat)
- Message reactions and threads

Provide:
1. Architecture overview
2. WebSocket connection management at scale
3. Message delivery and ordering guarantees
4. Message storage strategy (hot/warm/cold)
5. Group chat fan-out strategy
6. Search indexing approach
7. File storage and delivery
8. Push notification pipeline
9. End-to-end encryption design
10. Offline message delivery
```

### Template 1.4: E-Commerce Platform

```
Design a scalable e-commerce platform:

Scale:
- 10 million products
- 1 million daily active buyers
- 5,000 orders per hour (normal), 50,000 per hour (flash sales)
- Average cart: 3 items
- Payment processing: multi-currency, multi-provider

Features:
- Product catalog with search and filtering
- Shopping cart with reservation
- Checkout and payment processing
- Order management and fulfillment
- Inventory management (multi-warehouse)
- Seller dashboard (marketplace model)
- Recommendation engine
- Flash sale support (high concurrency)
- Customer reviews and ratings

Critical requirements:
- Cart and checkout must handle flash sale spikes
- Inventory must be accurate (no overselling)
- Payment processing must be reliable (exactly-once semantics)
- Product search must be fast (<200ms)

Provide the architecture addressing each challenge specifically.
```

---

## 2. Architecture Pattern Selection

### Template 2.1: Monolith vs Microservices Decision

```
Help me decide between monolith and microservices for:

Application: [description]
Current state: [new project / existing monolith / existing microservices]
Team: [size, experience, organizational structure]
Scale: [current and projected 2 years out]
Deployment frequency: [how often do we deploy?]
Domain complexity: [number of distinct business domains]

Evaluate along these axes:
1. Development velocity (time to implement a typical feature)
2. Operational complexity (deployment, monitoring, debugging)
3. Scalability (can we scale independently?)
4. Team autonomy (can teams work independently?)
5. Data consistency (how do we maintain consistency?)
6. Testing complexity (integration test overhead)
7. Cost (infrastructure + engineering time)
8. Failure isolation (blast radius of a bug)
9. Technology flexibility (can different parts use different tech?)
10. Time to market for MVP

Also consider hybrid approaches:
- Modular monolith (monolith with clear module boundaries)
- Macro-services (fewer, larger services)
- Strangler fig pattern (gradual migration)

Provide a recommendation with a confidence level and conditions under which you would recommend differently.
```

### Template 2.2: Event-Driven vs Request-Response

```
Should we use event-driven architecture for [SYSTEM COMPONENT]?

Current communication: [synchronous REST/gRPC between services]
Problem: [what is driving the consideration — coupling, performance, etc.]

Evaluate:
1. What operations are naturally synchronous? (user waits for response)
2. What operations are naturally asynchronous? (fire-and-forget, fan-out)
3. What data consistency model does each operation need?
4. What failure modes exist and how should they be handled?
5. How complex is the event ordering requirement?

For an event-driven approach, design:
- Event schema and naming conventions
- Broker selection (Kafka vs RabbitMQ vs SNS/SQS)
- Event flow diagrams for top 3 workflows
- Saga patterns for distributed transactions
- Dead letter queue and retry strategy
- Event versioning and schema evolution
- Monitoring and observability for events

For staying with request-response, design:
- Circuit breaker configuration
- Retry policies
- Timeout cascades
- Service mesh consideration

Provide a recommendation for each operation type.
```

### Template 2.3: Serverless vs Containers Decision

```
Compare serverless vs containers for:

Workload: [description]
Traffic pattern: [steady / bursty / unpredictable / scheduled]
Execution duration: [milliseconds / seconds / minutes]
Resource requirements: [CPU / memory / GPU / storage]
Cold start tolerance: [acceptable latency for first request]
State requirements: [stateless / needs local state / session affinity]

Compare:
1. AWS Lambda + API Gateway vs ECS Fargate vs EKS
2. Cost at current scale and projected 10x scale
3. Operational complexity
4. Developer experience
5. Vendor lock-in
6. Performance characteristics
7. Debugging and observability
8. Security model
9. Scaling behavior (speed, limits, granularity)

For each option, provide:
- Architecture diagram
- Estimated monthly cost
- Deployment strategy
- Monitoring setup
- When it becomes the wrong choice (scale thresholds)
```

---

## 3. Database Architecture

### Template 3.1: Database Selection

```
Help me choose the right database for:

Data characteristics:
- Data model: [relational / document / key-value / graph / time-series]
- Schema flexibility: [strict schema / semi-structured / schema-less]
- Data volume: [current size and growth rate]
- Record size: [average and maximum]
- Relationships: [simple FK / complex joins / graph traversals]

Access patterns:
- Read/write ratio: [e.g., 80/20]
- Query types: [simple lookups / complex joins / aggregations / full-text search]
- Transaction requirements: [ACID needed? Isolation level?]
- Consistency model: [strong / eventual / configurable]
- Latency requirements: [p99 targets for reads and writes]

Operational requirements:
- Availability: [uptime target]
- Backup and recovery: [RPO / RTO]
- Scaling: [vertical / horizontal / auto]
- Team expertise: [what databases does the team know?]
- Budget: [managed service acceptable? Open source preferred?]

Compare these options:
1. [Option A — e.g., PostgreSQL]
2. [Option B — e.g., MongoDB]
3. [Option C — e.g., DynamoDB]

For each option, provide:
- Fit score (1-10) for each requirement
- Architecture diagram showing how it would be deployed
- Estimated cost (managed service)
- Migration effort from current system
- Risks and limitations
```

### Template 3.2: Data Partitioning Strategy

```
Design a data partitioning strategy for:

Table: [table name]
Current size: [rows and storage size]
Growth rate: [rows per day/month]
Projected size in 2 years: [rows and storage]

Access patterns:
1. [Most common query and frequency]
2. [Second most common query]
3. [Analytical/reporting query]

Current pain points:
- [e.g., queries slowing down as table grows]
- [e.g., maintenance operations (VACUUM, INDEX REBUILD) taking too long]

Evaluate these strategies:
1. Range partitioning (by date)
2. Hash partitioning (by tenant/user ID)
3. List partitioning (by status/region)
4. Composite partitioning (hash + range)

For the recommended strategy:
- Partition key selection and justification
- Number of partitions and naming convention
- Query routing (how queries hit the right partition)
- Partition maintenance (creating new partitions, archiving old)
- Impact on existing queries and indexes
- Migration plan from non-partitioned to partitioned table
- Performance benchmarks to expect
```

### Template 3.3: Caching Architecture

```
Design a caching architecture for:

Application: [description]
Current database load: [queries/sec, p99 latency]
Target: [reduce database load by X%, reduce latency to Y ms]

Data types to cache:
1. [Data type 1 — e.g., user profiles] — size: [avg], update frequency: [how often]
2. [Data type 2 — e.g., product catalog] — size: [avg], update frequency: [how often]
3. [Data type 3 — e.g., session data] — size: [avg], update frequency: [how often]

Design:
1. Cache topology (embedded, sidecar, remote)
2. Cache strategy per data type (cache-aside, read-through, write-through, write-behind)
3. TTL configuration per data type
4. Invalidation strategy (event-based, TTL, hybrid)
5. Cache stampede prevention
6. Cache warming strategy
7. Serialization format
8. Memory sizing
9. Monitoring and alerting (hit rate, eviction rate, memory)
10. Failure mode (what happens if cache is down?)

Technology options:
- Redis (standalone vs cluster vs ElastiCache)
- Memcached
- Application-level cache (in-process)
- CDN caching for API responses
```

---

## 4. API Design

### Template 4.1: REST API Design

```
Design a REST API for [APPLICATION]:

Resources:
[list all resources with relationships]

Design decisions needed:
1. URL structure and naming conventions
2. HTTP method mapping
3. Request/response payload format
4. Pagination strategy (offset vs cursor)
5. Filtering and sorting convention
6. Partial responses (field selection)
7. Bulk operations
8. Error response format
9. Versioning strategy (URL, header, query param)
10. Rate limiting tiers
11. Authentication mechanism (JWT, API key, OAuth2)
12. HATEOAS (yes/no and why)

For each endpoint, provide:
- Method + Path
- Description
- Request (headers, params, body with types)
- Response (status codes, body with types)
- Authorization requirements
- Rate limit tier
- Caching headers
- Example request/response
```

### Template 4.2: GraphQL vs REST Decision

```
Should we use GraphQL or REST for [APPLICATION]?

Use case:
- Client types: [web, mobile, third-party, internal]
- Data relationships: [shallow/flat vs deeply nested]
- Query patterns: [fixed queries vs ad-hoc]
- Real-time needs: [subscriptions needed?]
- Team experience: [REST expertise, GraphQL expertise]

Evaluate:
1. Over-fetching / under-fetching impact
2. Mobile app performance (bandwidth concerns)
3. API evolution and backwards compatibility
4. Caching complexity
5. Error handling
6. Tooling and ecosystem
7. Learning curve for the team
8. Performance (N+1 queries, query complexity)
9. Documentation and discoverability
10. Third-party API consumer experience

If REST: Provide the API design
If GraphQL: Provide the schema and resolver design
If both (BFF pattern): Explain the architecture

Include concrete examples showing how the same data access works in each.
```

### Template 4.3: API Gateway Design

```
Design an API Gateway architecture for:

Backend services:
1. [Service 1] — [description, port, protocol]
2. [Service 2] — [description, port, protocol]
3. [Service 3] — [description, port, protocol]

Requirements:
- Route requests to appropriate backend services
- Authentication and authorization
- Rate limiting (per user, per endpoint)
- Request/response transformation
- API versioning
- Circuit breaking
- Load balancing
- SSL termination
- Request logging and tracing
- CORS handling
- WebSocket support

Options to evaluate:
1. AWS API Gateway
2. Kong Gateway
3. Custom Nginx + Lua
4. Envoy-based (Istio)
5. Cloud-native (AWS ALB + Lambda authorizer)

For the recommended approach:
- Configuration/deployment
- Routing rules
- Authentication flow
- Rate limiting configuration
- Monitoring and alerting
- Cost estimate
```

---

## 5. Scalability Analysis

### Template 5.1: Capacity Planning

```
Perform capacity planning for:

System: [description]
Current metrics:
- Users: [DAU, MAU]
- Requests: [per second, peak]
- Data: [storage used, growth rate]
- Compute: [CPU utilization, memory usage]

Growth projection:
- 6 months: [multiplier]
- 12 months: [multiplier]
- 24 months: [multiplier]

For each time horizon, calculate:
1. Required compute capacity (CPU cores, memory)
2. Required storage (database, object storage, cache)
3. Required bandwidth (ingress, egress)
4. Required database IOPS
5. Required cache memory
6. Cost projection

Identify bottlenecks:
- What breaks first?
- At what scale does each component need to be redesigned?
- What are the scaling options for each bottleneck?

Provide a scaling roadmap:
- Now: [what to do immediately]
- 3 months: [near-term scaling]
- 6 months: [medium-term architecture changes]
- 12+ months: [long-term platform evolution]
```

### Template 5.2: Load Testing Design

```
Design a load testing strategy for:

Application: [description]
SLAs:
- p99 latency: [target]
- Error rate: [target]
- Availability: [target]

Critical user journeys:
1. [Journey 1 — e.g., "user registration and first login"]
2. [Journey 2 — e.g., "search and purchase flow"]
3. [Journey 3 — e.g., "dashboard loading"]

Design:
1. Load test types (smoke, load, stress, spike, soak)
2. User simulation profiles (think times, flow distribution)
3. Data preparation (test accounts, test products)
4. Infrastructure (where to run load tests, tool selection)
5. Metrics to collect
6. Pass/fail criteria per SLA
7. Scaling decision triggers
8. Reporting template

Tool recommendation: [k6 / Locust / Gatling / Artillery]
Provide example test scripts for each critical journey.
```

---

## 6. Architecture Decision Records

### Template 6.1: ADR Template

```
Write an ADR for:

Decision: [what needs to be decided]
Context: [why this decision needs to be made now]

# ADR-[NUMBER]: [TITLE]

## Status
[Proposed | Accepted | Deprecated | Superseded by ADR-XXX]

## Date
[YYYY-MM-DD]

## Context
[Describe the forces at play — technical, business, organizational.
What is the problem we are trying to solve? Why now?]

## Decision Drivers
- [Driver 1 — e.g., "Team expertise in Python"]
- [Driver 2 — e.g., "Need to handle 10K concurrent connections"]
- [Driver 3 — e.g., "Must integrate with existing PostgreSQL infrastructure"]

## Options Considered

### Option 1: [Name]
- Description: [brief description]
- Pros:
  - [pro 1]
  - [pro 2]
- Cons:
  - [con 1]
  - [con 2]
- Cost: [development hours + infrastructure]
- Risk: [technical and organizational risks]

### Option 2: [Name]
[same format]

### Option 3: [Name]
[same format]

## Decision
[State the decision and the primary justification. Be specific and unambiguous.]

## Consequences

### Positive
- [positive consequence 1]
- [positive consequence 2]

### Negative
- [negative consequence 1 — and how we will mitigate it]

### Risks
- [risk 1 — likelihood, impact, mitigation]

## Follow-up Actions
- [ ] [Action 1 with owner and deadline]
- [ ] [Action 2 with owner and deadline]

## References
- [link to related documentation]
- [link to discussion/RFC]
```

### Template 6.2: Common ADR Topics

```
Generate ADRs for these common decisions (use Template 6.1 for each):

1. Primary programming language selection
2. Database technology choice
3. API protocol (REST vs GraphQL vs gRPC)
4. Authentication mechanism (JWT vs session vs OAuth2)
5. Message broker selection (Kafka vs RabbitMQ vs SQS)
6. Deployment platform (Kubernetes vs ECS vs serverless)
7. Monolith vs microservices architecture
8. Frontend framework selection
9. CI/CD platform selection
10. Observability stack selection

For each, provide context relevant to [YOUR APPLICATION TYPE] with
team of [SIZE] engineers and [SCALE REQUIREMENTS].
```

---

## 7. Architecture Review

### Template 7.1: Architecture Health Check

```
Perform an architecture health check:

Architecture description:
[Describe components, technologies, communication patterns, deployment]

Evaluate on 8 dimensions (rate each Red / Amber / Green):

1. **Modularity**: Are concerns properly separated?
   - Are module boundaries well-defined?
   - Is coupling between modules minimized?
   - Can modules be independently developed and tested?

2. **Scalability**: Can it handle growth?
   - What are the scaling limits of each component?
   - Can components scale independently?
   - Are there stateful components that limit horizontal scaling?

3. **Reliability**: Is it resilient to failures?
   - What are the single points of failure?
   - Are there circuit breakers and fallbacks?
   - What is the blast radius of each component failure?

4. **Security**: Is it secure by design?
   - Are trust boundaries clearly defined?
   - Is data encrypted in transit and at rest?
   - Are there proper authentication and authorization boundaries?

5. **Operability**: Is it easy to operate?
   - Is deployment automated and repeatable?
   - Are there adequate monitoring and alerting?
   - Can issues be diagnosed quickly?

6. **Evolvability**: Is it easy to change?
   - Can new features be added without widespread changes?
   - Can components be replaced without system-wide impact?
   - Are APIs versioned for backwards compatibility?

7. **Performance**: Does it meet performance requirements?
   - Are there known performance bottlenecks?
   - Is caching used appropriately?
   - Are database queries optimized?

8. **Cost Efficiency**: Is it cost-effective?
   - Are resources right-sized?
   - Are there idle resources that could be optimized?
   - What is the cost per transaction/user?

For each dimension:
- Current rating
- Evidence for the rating
- Top 3 improvement recommendations
- Estimated effort for each improvement
```

### Template 7.2: Architecture Fitness Functions

```
Define architecture fitness functions for:

Architecture: [description]
Key quality attributes: [list the most important -ilities]

For each quality attribute, define automated fitness functions:

1. **Performance fitness**
   - Metric: p99 API latency < 500ms
   - How to measure: Continuous synthetic monitoring
   - Threshold: Warning at 400ms, Critical at 500ms
   - Automated test: Load test in CI running daily

2. **Reliability fitness**
   - Metric: Error rate < 0.1%
   - How to measure: Prometheus error counter / total requests
   - Threshold: Warning at 0.05%, Critical at 0.1%
   - Automated test: Error budget tracking

3. **Modularity fitness**
   - Metric: No circular dependencies between modules
   - How to measure: Static analysis tool (deptry, madge)
   - Threshold: Zero circular dependencies
   - Automated test: CI check on every PR

4. **Security fitness**
   - Metric: Zero critical/high vulnerabilities in dependencies
   - How to measure: Dependabot / Snyk continuous scanning
   - Threshold: Critical = block deploy, High = fix within 7 days
   - Automated test: CI security scan

5. **Coupling fitness**
   - Metric: Service communication complexity score
   - How to measure: Count inter-service API calls per user journey
   - Threshold: No journey touches > 5 services
   - Automated test: Architecture test in CI

Generate the monitoring, alerting, and CI configuration for each.
```

---

## 8. Migration and Evolution

### Template 8.1: Monolith to Microservices Migration

```
Plan a migration from monolith to microservices:

Current monolith:
- Language: [language]
- Framework: [framework]
- Database: [single database with N tables]
- Size: [lines of code, number of modules/features]
- Team: [number of developers]
- Deploy frequency: [how often]

Pain points:
1. [e.g., "Deploys take 2 hours and require full team coordination"]
2. [e.g., "A bug in the payment module can bring down the entire application"]
3. [e.g., "Different modules have different scaling requirements"]

Goals:
- [e.g., "Independent deployment per team"]
- [e.g., "Isolate payment processing for PCI compliance"]
- [e.g., "Scale search independently from order processing"]

Plan:
1. **Service identification**: Which modules become services?
   - Domain analysis (bounded contexts)
   - Dependency analysis (coupling between modules)
   - Data ownership analysis (which service owns which data)

2. **Extraction order**: Which service to extract first?
   - Risk assessment per extraction
   - Value assessment per extraction
   - Dependency ordering (extract leaf nodes first)

3. **Strangler fig pattern**: How to gradually migrate
   - API gateway routing rules
   - Database splitting strategy
   - Data synchronization during migration
   - Feature flags for routing traffic

4. **Infrastructure needs**: What infrastructure to add
   - Service mesh / API gateway
   - Message broker for async communication
   - Service discovery
   - Distributed tracing
   - Centralized logging

5. **Timeline**: Realistic migration schedule
   - Phase 1: [3 months] — Extract first service
   - Phase 2: [6 months] — Extract 2-3 more services
   - Phase 3: [12 months] — Complete migration
   - Each phase with rollback plan

6. **Risk mitigation**: How to reduce risk
   - Feature flag strategy
   - Canary deployments
   - Rollback procedures
   - Data consistency verification
```

### Template 8.2: Technology Migration

```
Plan a migration from [OLD TECHNOLOGY] to [NEW TECHNOLOGY]:

Current state:
- [OLD TECHNOLOGY] version [X]
- [How it is used in the system]
- [Pain points driving migration]

Target state:
- [NEW TECHNOLOGY] version [Y]
- [Expected benefits]

Constraints:
- Zero downtime during migration
- Rollback capability at every stage
- No data loss
- Team needs training on [NEW TECHNOLOGY]

Plan:
1. **Assessment phase** (2 weeks)
   - Feature parity analysis
   - Performance benchmarking
   - Risk identification

2. **Preparation phase** (4 weeks)
   - Team training
   - Proof of concept
   - Migration tooling development
   - Runbook creation

3. **Migration phase** (timeline depends on scope)
   - Dual-write/dual-read strategy
   - Data migration and verification
   - Traffic shifting (1% -> 10% -> 50% -> 100%)
   - Monitoring and validation at each stage

4. **Cleanup phase** (2 weeks)
   - Remove old technology
   - Clean up migration tooling
   - Update documentation
   - Post-migration review

Include:
- Decision points at each phase
- Rollback procedure for each stage
- Success criteria for moving to next stage
- Communication plan for stakeholders
```

---

## Usage Guide

### How to Get the Best Results

1. **Fill in all placeholders**: The more specific your context, the more useful the architecture advice.

2. **Include numbers**: Scale parameters, team size, timeline, and budget make architecture decisions concrete rather than theoretical.

3. **State constraints clearly**: Constraints are as important as requirements. They narrow the solution space to practical options.

4. **Iterate**: Use the initial output as a starting point, then drill down on specific components with follow-up prompts.

5. **Challenge the output**: Ask "What could go wrong with this architecture?" and "What would you change if we needed 100x scale?"

6. **Compare with experience**: AI provides patterns and options, but your organizational context and experience should guide the final decision.

### Combining Templates

- **New project**: Template 1.1 (System Design) + 2.1 (Monolith vs Micro) + 3.1 (Database) + 4.1 (API) + 6.1 (ADRs)
- **Scaling existing system**: Template 5.1 (Capacity) + 7.1 (Health Check) + 3.3 (Caching) + 8.1 (Migration if needed)
- **Technology evaluation**: Template 2.3 (Serverless vs Containers) + 3.1 (Database Selection) + 6.1 (ADR for each decision)
