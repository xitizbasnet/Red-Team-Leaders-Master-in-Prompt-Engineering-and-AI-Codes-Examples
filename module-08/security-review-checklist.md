# AI-Powered Security Review Checklist

## Module 08: AI for Software Development and Security

> Comprehensive security review checklist with AI prompts for each OWASP category and additional security domains.

---

## How to Use This Checklist

1. Go through each section relevant to your application
2. For each item, use the provided AI prompt to analyze your code
3. Mark items as: PASS, FAIL, N/A, or NEEDS REVIEW
4. Prioritize findings by severity
5. Create remediation tasks for all FAIL items

---

## OWASP A01: Broken Access Control

### Checklist

| # | Check | Status | Severity |
|---|-------|--------|----------|
| A01-01 | All API endpoints have authorization checks | | Critical |
| A01-02 | IDOR protection on all resource-accessing endpoints | | Critical |
| A01-03 | Function-level access control (admin endpoints protected) | | Critical |
| A01-04 | CORS is configured to allow only trusted origins | | High |
| A01-05 | Directory listing is disabled on web servers | | Medium |
| A01-06 | File access endpoints validate user ownership | | High |
| A01-07 | JWT tokens contain minimal claims (no sensitive data) | | Medium |
| A01-08 | Rate limiting on authentication endpoints | | High |
| A01-09 | Session invalidation on logout and password change | | High |
| A01-10 | Path traversal protection on file operations | | Critical |
| A01-11 | HTTP method restrictions (no unintended PUT/DELETE) | | Medium |
| A01-12 | API keys are scoped to minimum required permissions | | High |

### AI Prompt for A01

```
Review this code for Broken Access Control vulnerabilities:

```[language]
[paste your endpoint handlers, middleware, and authorization logic]
```

For each endpoint, verify:
1. Is there an authentication check? (401 for unauthenticated)
2. Is there an authorization check? (403 for unauthorized)
3. Can user A access user B's resources by changing the ID in the URL? (IDOR)
4. Can a regular user access admin-only functions?
5. Can a user modify their own role/permissions?
6. Are deleted/deactivated resources still accessible?

For each finding, provide:
- Endpoint and HTTP method
- Vulnerability type
- Severity (Critical/High/Medium/Low)
- Proof of concept request
- Remediation code
```

---

## OWASP A02: Cryptographic Failures

### Checklist

| # | Check | Status | Severity |
|---|-------|--------|----------|
| A02-01 | Passwords hashed with bcrypt/argon2/scrypt (cost >= 10) | | Critical |
| A02-02 | No MD5 or SHA-1 for password hashing | | Critical |
| A02-03 | All sensitive data encrypted at rest | | High |
| A02-04 | TLS 1.2+ for all data in transit | | Critical |
| A02-05 | No hardcoded encryption keys or secrets | | Critical |
| A02-06 | Cryptographically secure random number generation | | High |
| A02-07 | Proper IV/nonce usage (never reused) | | High |
| A02-08 | Key rotation mechanism in place | | Medium |
| A02-09 | Sensitive data not in URLs or query parameters | | High |
| A02-10 | Sensitive data not logged | | High |
| A02-11 | Database connection strings use TLS | | High |
| A02-12 | Deprecated algorithms not used (DES, 3DES, RC4) | | Critical |

### AI Prompt for A02

```
Audit this codebase for cryptographic failures:

```[language]
[paste code dealing with: passwords, encryption, tokens, secrets, hashing]
```

Also review these configuration files:
```
[paste: .env, database config, TLS config, etc.]
```

Check:
1. How are passwords stored? (algorithm, salt, cost factor)
2. How are secrets managed? (environment variables, vault, hardcoded)
3. What encryption is used for sensitive data at rest?
4. Is TLS enforced for all external communications?
5. How are random values generated for security purposes? (tokens, keys, IVs)
6. Are there any deprecated cryptographic algorithms?
7. Is there sensitive data in log files?

For each finding, classify severity and provide the secure alternative.
```

---

## OWASP A03: Injection

### Checklist

| # | Check | Status | Severity |
|---|-------|--------|----------|
| A03-01 | All SQL queries use parameterized statements | | Critical |
| A03-02 | No string concatenation in database queries | | Critical |
| A03-03 | ORM used with proper parameterization | | High |
| A03-04 | No OS command execution with user input | | Critical |
| A03-05 | Template rendering does not accept raw user input | | Critical |
| A03-06 | LDAP queries are parameterized | | High |
| A03-07 | XML parsing disables external entities (XXE) | | High |
| A03-08 | User input in log messages is sanitized | | Medium |
| A03-09 | Email headers are not injectable | | Medium |
| A03-10 | NoSQL queries are parameterized | | High |
| A03-11 | GraphQL queries have depth/complexity limits | | Medium |
| A03-12 | XSS: All user output is properly encoded | | High |

### AI Prompt for A03

```
Scan this code for ALL injection vulnerability types:

```[language]
[paste: database queries, command execution, template rendering,
 email sending, logging, XML/JSON parsing]
```

Check for each injection type:
1. SQL Injection — Any string concatenation in SQL?
2. NoSQL Injection — Unparameterized MongoDB/DynamoDB queries?
3. Command Injection — os.system/subprocess with user input?
4. Template Injection (SSTI) — User input in template rendering?
5. XSS — User input rendered without encoding?
6. LDAP Injection — Unescaped input in LDAP queries?
7. XXE — XML parser with external entities enabled?
8. Log Injection — Unescaped user input in log messages?
9. Header Injection (CRLF) — User input in HTTP headers?
10. Expression Language Injection — User input in expression evaluation?

For each finding:
- Show the vulnerable code
- Provide an exploitation example
- Show the secure code
- Explain the defense mechanism
```

---

## OWASP A04: Insecure Design

### Checklist

| # | Check | Status | Severity |
|---|-------|--------|----------|
| A04-01 | Threat model exists for the application | | High |
| A04-02 | Security requirements defined before development | | High |
| A04-03 | Business logic abuse cases identified | | High |
| A04-04 | Rate limiting designed into critical flows | | High |
| A04-05 | Defense in depth (multiple security layers) | | Medium |
| A04-06 | Trust boundaries clearly defined | | Medium |
| A04-07 | Secure defaults for all configurations | | High |
| A04-08 | Fail-safe design (deny by default) | | High |
| A04-09 | Separation of duties in critical operations | | Medium |
| A04-10 | Resource consumption limits in place | | Medium |

### AI Prompt for A04

```
Analyze this system design for security design flaws:

Architecture:
[describe your architecture — components, data flows, trust boundaries]

Business flows:
1. [critical flow 1 — e.g., payment processing]
2. [critical flow 2 — e.g., user registration]
3. [critical flow 3 — e.g., data export]

Check for:
1. Missing authentication on sensitive operations
2. Business logic that can be bypassed
3. Race conditions in financial or state-changing operations
4. Missing rate limiting that enables abuse
5. Lack of defense in depth
6. Overly permissive default configurations
7. Missing input validation at trust boundary crossings
8. Insufficient separation of duties
9. Missing audit trail for critical operations
10. Resource exhaustion attack vectors

For each finding, provide design-level recommendations.
```

---

## OWASP A05: Security Misconfiguration

### Checklist

| # | Check | Status | Severity |
|---|-------|--------|----------|
| A05-01 | Debug mode disabled in production | | Critical |
| A05-02 | Default credentials changed or removed | | Critical |
| A05-03 | Error messages do not expose stack traces | | High |
| A05-04 | Security headers configured (CSP, HSTS, X-Frame-Options) | | High |
| A05-05 | Unnecessary features/services disabled | | Medium |
| A05-06 | Directory listing disabled | | Medium |
| A05-07 | Cloud storage (S3) not publicly accessible | | Critical |
| A05-08 | Database not directly accessible from internet | | Critical |
| A05-09 | CORS policy is restrictive (not wildcard) | | High |
| A05-10 | TLS configured with strong cipher suites | | High |
| A05-11 | HTTP methods restricted to those needed | | Medium |
| A05-12 | Admin interfaces not exposed to the internet | | Critical |

### AI Prompt for A05

```
Review these configuration files for security misconfigurations:

Application config:
```
[paste application configuration: settings.py, application.yml, .env, etc.]
```

Web server config:
```
[paste nginx.conf, apache config, etc.]
```

Docker config:
```
[paste Dockerfile, docker-compose.yml]
```

Cloud config:
```
[paste Terraform, CloudFormation, or cloud console settings]
```

Check for:
1. Debug/development mode flags in production config
2. Default or weak credentials
3. Verbose error messages that leak information
4. Missing security headers
5. Overly permissive CORS
6. Unnecessary ports or services exposed
7. Cloud resources with public access
8. Missing encryption settings
9. Permissive firewall/security group rules
10. Missing TLS or weak TLS configuration

Provide the corrected configuration for each finding.
```

---

## OWASP A06: Vulnerable and Outdated Components

### Checklist

| # | Check | Status | Severity |
|---|-------|--------|----------|
| A06-01 | Dependency scanning in CI/CD pipeline | | High |
| A06-02 | No known critical CVEs in dependencies | | Critical |
| A06-03 | No known high CVEs older than 30 days unpatched | | High |
| A06-04 | Lock files committed (package-lock, poetry.lock, etc.) | | Medium |
| A06-05 | Automated dependency update mechanism (Dependabot) | | Medium |
| A06-06 | Base Docker images regularly updated | | High |
| A06-07 | OS packages updated in container images | | High |
| A06-08 | No end-of-life (EOL) frameworks or runtimes | | High |
| A06-09 | Unused dependencies removed | | Low |
| A06-10 | SBOM generated for the application | | Medium |

### AI Prompt for A06

```
Analyze these dependencies for security risks:

```
[paste your dependency files: package.json, requirements.txt,
 go.mod, Cargo.toml, pom.xml, etc.]
```

Dockerfile base images:
```
[paste FROM lines from your Dockerfiles]
```

Check:
1. Known CVEs in current dependency versions
2. Severely outdated packages (>2 major versions behind)
3. Abandoned/unmaintained packages
4. Packages with known supply chain issues
5. Typosquatting risks (similar names to popular packages)
6. Unnecessary dependencies that increase attack surface
7. Base image vulnerabilities
8. EOL runtimes or frameworks

For each risk, provide:
- Package name and version
- Risk description
- Recommended action (update to version X, replace with Y, remove)
- How to check if it is exploitable in our context
```

---

## OWASP A07: Authentication Failures

### Checklist

| # | Check | Status | Severity |
|---|-------|--------|----------|
| A07-01 | Password minimum length >= 8 characters | | High |
| A07-02 | Password complexity requirements enforced | | Medium |
| A07-03 | Common password list check | | High |
| A07-04 | Brute force protection (account lockout/delay) | | Critical |
| A07-05 | MFA available and recommended | | High |
| A07-06 | Session timeout (idle and absolute) | | High |
| A07-07 | Session invalidation on password change | | High |
| A07-08 | No account enumeration via error messages | | Medium |
| A07-09 | No account enumeration via timing differences | | Medium |
| A07-10 | Password reset tokens expire (< 1 hour) | | High |
| A07-11 | Password reset uses secure random tokens | | Critical |
| A07-12 | Credential recovery does not reveal if account exists | | Medium |

### AI Prompt for A07

```
Review the authentication implementation:

```[language]
[paste: login handler, registration handler, password reset handler,
 session management, token generation/validation, MFA implementation]
```

Configuration:
```
[paste: session config, JWT config, password policy config]
```

Check each item:
1. Password storage (algorithm, salt, cost factor)
2. Password policy enforcement (length, complexity, common passwords)
3. Brute force protection (lockout, rate limiting, CAPTCHA)
4. Session management (generation, storage, expiration, invalidation)
5. Token security (randomness, expiration, single-use)
6. MFA implementation (TOTP, backup codes)
7. Account enumeration (error messages, timing, registration)
8. Password reset flow (token generation, expiration, one-time use)
9. OAuth2/OIDC implementation (state parameter, PKCE, token validation)
10. "Remember me" implementation security

For each finding, provide the secure implementation.
```

---

## OWASP A08: Software and Data Integrity Failures

### Checklist

| # | Check | Status | Severity |
|---|-------|--------|----------|
| A08-01 | CI/CD pipeline uses verified actions/plugins | | High |
| A08-02 | Dependencies verified with checksums/signatures | | Medium |
| A08-03 | No auto-update of dependencies without review | | Medium |
| A08-04 | Deserialization of untrusted data is avoided or restricted | | Critical |
| A08-05 | Code signing for deployments | | Medium |
| A08-06 | Branch protection rules enforced | | High |
| A08-07 | CI/CD secrets properly scoped | | High |
| A08-08 | SBOM generated and maintained | | Low |
| A08-09 | Container images signed and verified | | Medium |
| A08-10 | Data integrity checks on critical data | | Medium |

---

## OWASP A09: Security Logging and Monitoring Failures

### Checklist

| # | Check | Status | Severity |
|---|-------|--------|----------|
| A09-01 | Authentication events logged (success and failure) | | High |
| A09-02 | Authorization failures logged (403 events) | | High |
| A09-03 | Input validation failures logged | | Medium |
| A09-04 | High-value transactions logged with audit trail | | High |
| A09-05 | No sensitive data in logs (passwords, tokens, PII) | | Critical |
| A09-06 | Logs are tamper-evident (centralized, append-only) | | Medium |
| A09-07 | Alerting on suspicious patterns (brute force, scanning) | | High |
| A09-08 | Log retention meets compliance requirements | | Medium |
| A09-09 | Centralized log management in place | | Medium |
| A09-10 | Incident response playbook exists and is tested | | High |
| A09-11 | Log injection is prevented | | Medium |
| A09-12 | Monitoring covers all critical paths | | High |

### AI Prompt for A09

```
Audit the logging and monitoring implementation:

Logging code:
```[language]
[paste logging configuration, logging calls in security-relevant code]
```

Monitoring/alerting config:
```
[paste Prometheus rules, CloudWatch alarms, PagerDuty config, etc.]
```

Verify:
1. Are ALL authentication events logged? (login success, failure, logout, password change)
2. Are authorization failures logged? (403 responses)
3. Are input validation failures logged? (rejected requests)
4. Is there an audit trail for critical business operations?
5. Is sensitive data excluded from logs? (search for: password, token, secret, credit_card)
6. Are logs protected from injection? (is user input sanitized before logging?)
7. Is there alerting for: brute force, account enumeration, privilege escalation attempts?
8. What is the log retention policy? Does it meet compliance requirements?
9. Are logs centralized and tamper-evident?
10. Is there a documented incident response procedure?

For each gap, provide the implementation (code + configuration).
```

---

## OWASP A10: Server-Side Request Forgery (SSRF)

### Checklist

| # | Check | Status | Severity |
|---|-------|--------|----------|
| A10-01 | URLs from user input are validated against allowlist | | Critical |
| A10-02 | Internal IP ranges blocked (10.x, 172.16.x, 192.168.x) | | Critical |
| A10-03 | Localhost/loopback (127.0.0.1, ::1) blocked | | Critical |
| A10-04 | Cloud metadata endpoints blocked (169.254.169.254) | | Critical |
| A10-05 | URL scheme restricted (http/https only) | | High |
| A10-06 | DNS rebinding protection in place | | High |
| A10-07 | Redirect following disabled or validated | | High |
| A10-08 | Response content filtered (not returned to user raw) | | Medium |
| A10-09 | Webhook URLs validated before calling | | High |
| A10-10 | Network-level egress filtering configured | | Medium |

### AI Prompt for A10

```
Check this code for SSRF vulnerabilities:

```[language]
[paste: any code that makes HTTP requests based on user input,
 webhook handlers, URL fetching, file download from URL,
 image fetching, link preview generation]
```

Check:
1. Are user-provided URLs validated?
2. Is there an allowlist of permitted hosts/schemes?
3. Are internal IP ranges blocked?
4. Is the cloud metadata endpoint (169.254.169.254) blocked?
5. Can redirect following bypass URL validation?
6. Is DNS rebinding mitigated? (resolve DNS, then check IP before connecting)
7. Is the response filtered? (not returning raw internal responses)
8. Are webhook callback URLs validated?

For each vulnerability:
- Show the vulnerable code path
- Demonstrate exploitation
- Provide comprehensive SSRF prevention code
- Include both application-level and network-level mitigations
```

---

## Additional Security Domains

### API Security

| # | Check | Status | Severity |
|---|-------|--------|----------|
| API-01 | API authentication on all non-public endpoints | | Critical |
| API-02 | Rate limiting applied per-user and per-endpoint | | High |
| API-03 | Request body size limits configured | | Medium |
| API-04 | API versioning strategy in place | | Low |
| API-05 | Response does not include more data than needed | | Medium |
| API-06 | GraphQL query depth and complexity limits | | High |
| API-07 | Batch/bulk endpoints have item count limits | | Medium |
| API-08 | API documentation does not expose internal details | | Low |

### Data Protection

| # | Check | Status | Severity |
|---|-------|--------|----------|
| DP-01 | PII identified and classified | | High |
| DP-02 | Data minimization (collect only what is needed) | | Medium |
| DP-03 | Data retention policies defined and enforced | | Medium |
| DP-04 | Data deletion capability (right to erasure) | | High |
| DP-05 | Data export capability (right to portability) | | Medium |
| DP-06 | Data masking in non-production environments | | High |
| DP-07 | Backup encryption | | High |
| DP-08 | Cross-border data transfer compliance | | Medium |

### Container Security

| # | Check | Status | Severity |
|---|-------|--------|----------|
| CS-01 | Non-root user in container | | High |
| CS-02 | Minimal base image (distroless or Alpine) | | Medium |
| CS-03 | No secrets baked into image | | Critical |
| CS-04 | Image scanning in CI/CD | | High |
| CS-05 | Read-only root filesystem | | Medium |
| CS-06 | Capabilities dropped (no-new-privileges) | | Medium |
| CS-07 | Resource limits set (CPU, memory) | | Medium |
| CS-08 | Image pinned by digest (not just tag) | | Medium |

---

## Summary Report Template

After completing the checklist, generate a summary report:

```
# Security Review Report

Date: [date]
Application: [name]
Reviewer: [name]
Scope: [what was reviewed]

## Executive Summary
- Total items checked: [count]
- PASS: [count] ([percentage]%)
- FAIL: [count] ([percentage]%)
- N/A: [count]
- NEEDS REVIEW: [count]

## Critical Findings (Immediate Action Required)
1. [Finding 1 — description, location, remediation]
2. [Finding 2 — description, location, remediation]

## High-Severity Findings (Fix Within 7 Days)
1. [Finding 1]
2. [Finding 2]

## Medium-Severity Findings (Fix Within 30 Days)
1. [Finding 1]

## Low-Severity Findings (Fix in Next Release)
1. [Finding 1]

## Remediation Priority
| # | Finding | Severity | Effort | Priority |
|---|---------|----------|--------|----------|
| 1 | | | | |
| 2 | | | | |

## Recommendations
1. [Strategic recommendation 1]
2. [Strategic recommendation 2]
```
