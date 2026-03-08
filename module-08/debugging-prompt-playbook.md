# Debugging Prompt Playbook

## Module 08: AI for Software Development and Security

> A systematic debugging prompt playbook for common error types.

---

## Table of Contents

1. [Universal Debugging Framework](#1-universal-debugging-framework)
2. [Runtime Errors](#2-runtime-errors)
3. [Logic Errors](#3-logic-errors)
4. [Performance Issues](#4-performance-issues)
5. [Concurrency Bugs](#5-concurrency-bugs)
6. [Integration Errors](#6-integration-errors)
7. [Build and Dependency Errors](#7-build-and-dependency-errors)
8. [Database Errors](#8-database-errors)
9. [Frontend Errors](#9-frontend-errors)
10. [Infrastructure Errors](#10-infrastructure-errors)
11. [Quick Reference Card](#11-quick-reference-card)

---

## 1. Universal Debugging Framework

### The SIRFC Method

Use this framework for any bug, regardless of type:

```
S - Symptoms:    What is happening? What did you expect?
I - Isolation:   What is the minimal code/config that reproduces the bug?
R - Reproduce:   Can you reliably reproduce it? Under what conditions?
F - Facts:       What do you know for certain? (logs, error messages, stack traces)
C - Context:     Environment, versions, recent changes, deployment state
```

### The Master Debugging Prompt

```
## Bug Report

### Symptoms
- Expected behavior: [what should happen]
- Actual behavior: [what actually happens]
- Frequency: [always / intermittent / under specific conditions]
- First noticed: [when — after a deploy, config change, etc.?]

### Reproduction
- Steps to reproduce:
  1. [step 1]
  2. [step 2]
  3. [step 3]
- Minimal reproduction code:
```[language]
[minimal code that demonstrates the issue]
```

### Facts (Evidence)
- Error message / stack trace:
```
[full error output]
```
- Relevant logs:
```
[log entries around the time of the error]
```

### Context
- Language/Runtime: [e.g., Python 3.12.1]
- Framework: [e.g., FastAPI 0.109.0]
- OS: [e.g., Ubuntu 22.04 / macOS 14.2]
- Database: [e.g., PostgreSQL 16.1]
- Deployment: [e.g., Docker on ECS, Kubernetes]
- Recent changes: [what changed recently that might be related]

### What I Have Tried
1. [attempt 1 and its result]
2. [attempt 2 and its result]

### Questions
1. What is the root cause of this issue?
2. What is the recommended fix?
3. How can I prevent this from happening again?
4. What tests should I add to catch this in the future?
```

---

## 2. Runtime Errors

### 2.1 NullPointerException / TypeError / AttributeError

**When to use**: Variable is None/null/undefined when you expect a value.

```
I am getting a [NullPointerException / TypeError / AttributeError]:

Error:
```
[full error message with stack trace]
```

Code context:
```[language]
[the function/method where the error occurs, plus the calling code]
```

The variable `[name]` is None/null at line [X] when it should be [expected type].

Please:
1. Trace the data flow backward: Where should `[name]` have been assigned a value?
2. What code paths could lead to it being None/null? (conditional branches, early returns, exception handlers)
3. Is the root cause here, or upstream in a calling function?
4. Provide the fix — not just a null check, but fixing why it is null in the first place
5. If a null check IS appropriate, what should happen when it is null? (default value, raise specific error, skip operation)
```

### 2.2 IndexError / ArrayIndexOutOfBoundsException

```
I am getting an [IndexError / ArrayIndexOutOfBoundsException]:

Error:
```
[error message]
```

Code:
```[language]
[code with array/list access]
```

Data sample that triggers the error: [sample data]

Please:
1. Identify which array access is out of bounds
2. What is the array length vs the index being accessed?
3. Is this an off-by-one error, an empty collection issue, or wrong data?
4. Provide the fix with proper bounds checking
5. What assertion or validation should prevent this?
```

### 2.3 StackOverflow / RecursionError

```
I am getting a [StackOverflowError / RecursionError]:

Error:
```
[error showing the recursive call chain]
```

Code:
```[language]
[recursive function code]
```

Input that triggers it: [input data]

Please:
1. Identify the base case — is it missing, unreachable, or incorrect?
2. Does each recursive call make progress toward the base case?
3. Is there a cycle in the data causing infinite recursion?
4. Provide the fix (correct base case, or convert to iterative)
5. What is the maximum expected recursion depth for valid inputs?
```

### 2.4 OutOfMemory / MemoryError

```
My application is running out of memory:

Symptoms:
- Memory usage before issue: [X MB]
- Memory usage when it crashes: [Y MB]
- Time from start to crash: [duration]
- Trigger: [what action or workload causes it]

Code that might be causing the issue:
```[language]
[relevant code — data loading, collection building, caching]
```

Memory profiler output (if available):
```
[profiler output]
```

Please:
1. Identify objects that might be accumulating without release
2. Check for: unbounded caches, loading full datasets into memory, circular references preventing GC
3. Are there generators/iterators that should be used instead of lists?
4. Is there connection/resource pooling that is leaking?
5. Provide fixes with memory-efficient alternatives
6. What memory limits should be set for this workload?
```

### 2.5 Type Mismatch / ClassCastException

```
I am getting a type error:

Error:
```
[error message showing expected vs actual type]
```

Code:
```[language]
[code where the type mismatch occurs]
```

Please:
1. Where does the wrong type originate? (API response, database query, user input)
2. Is there implicit type coercion happening that should be explicit?
3. Is the type definition correct, or does it need updating?
4. Provide the fix with proper type conversion or type guard
5. Should I add runtime type validation? (Pydantic, Zod, etc.)
```

---

## 3. Logic Errors

### 3.1 Wrong Output (No Error Message)

```
My function returns incorrect results. No error is raised.

Function:
```[language]
[function code]
```

Test cases:
| Input | Expected Output | Actual Output | Pass/Fail |
|-------|----------------|---------------|-----------|
| [input1] | [expected1] | [actual1] | FAIL |
| [input2] | [expected2] | [actual2] | FAIL |
| [input3] | [expected3] | [actual3] | PASS |

Please:
1. Trace through the failing cases step by step
2. Identify where the logic diverges from expected behavior
3. Check for: off-by-one errors, wrong operators (< vs <=, && vs ||), wrong variable names
4. Provide the corrected logic
5. Add test cases that would have caught this during development
```

### 3.2 Conditional Logic Bugs

```
This conditional logic is not behaving as expected:

```[language]
[code with if/else, switch, or boolean logic]
```

Expected behavior:
- When [condition A], should [action A]
- When [condition B], should [action B]
- When [condition C], should [action C]

Actual behavior:
- When [condition A], it [wrong action]

Please:
1. Create a truth table for all possible condition combinations
2. Identify which cases are handled incorrectly
3. Check for: operator precedence issues, short-circuit evaluation, missing else branches
4. Is there a simpler way to express this logic?
5. Provide the corrected conditional logic
```

### 3.3 Off-by-One Errors

```
I suspect an off-by-one error in this code:

```[language]
[code with loops, array slicing, pagination, or range calculations]
```

Specifically, check:
1. Loop bounds — should it be `< length` or `<= length`?
2. Array slicing — is the end index inclusive or exclusive?
3. Pagination — is page 1 or page 0 the first page?
4. Range calculations — is the range inclusive on both ends?
5. String operations — is the last character included?

For each finding, show the incorrect value and the correct value.
```

### 3.4 Floating Point Precision

```
I am getting unexpected results with floating point arithmetic:

```[language]
[code with decimal/float calculations]
```

Example: [calculation] = [wrong result] (expected [correct result])

Please:
1. Explain why this precision issue occurs (IEEE 754)
2. Is this a comparison issue (0.1 + 0.2 != 0.3) or an accumulation issue?
3. What is the appropriate solution for this use case?
   - Decimal/BigDecimal types?
   - Epsilon comparison?
   - Integer arithmetic with scaling?
   - Rounding strategy?
4. Provide the fixed code
5. What is the maximum precision loss we should expect?
```

---

## 4. Performance Issues

### 4.1 Slow Database Query

```
This database query is taking [X seconds] when it should take [< Y ms]:

Query:
```sql
[the slow query]
```

EXPLAIN ANALYZE:
```
[explain analyze output]
```

Table definitions and indexes:
```sql
[CREATE TABLE and CREATE INDEX statements]
```

Table row counts: [table: count, ...]

Please:
1. Identify the performance bottleneck from the EXPLAIN output
2. Is the query doing a sequential scan where it should use an index?
3. Are there unnecessary JOINs or subqueries?
4. Rewrite the query for better performance
5. What indexes should be added? (include the CREATE INDEX statement)
6. Would a materialized view or denormalization help?
7. Estimate the improvement
```

### 4.2 Slow API Endpoint

```
This API endpoint takes [X seconds] to respond:

Endpoint code:
```[language]
[handler/controller code]
```

Service code:
```[language]
[service layer code called by the handler]
```

Profiling data (if available):
```
[profiling output showing where time is spent]
```

Please:
1. Identify the bottleneck (database, external API, computation, serialization)
2. Is there an N+1 query problem?
3. Are there synchronous operations that could be parallelized?
4. What caching could be applied? (at what layer, with what TTL)
5. Are there unnecessary data fetches? (fetching more than needed)
6. Provide the optimized code
7. What response time should we expect after optimization?
```

### 4.3 Memory Leak

```
My application's memory usage grows over time and never decreases:

Growth pattern:
- Start: [X MB]
- After 1 hour: [Y MB]
- After 24 hours: [Z MB]
- Triggers garbage collection but does not reclaim memory

Application type: [web server / background worker / etc.]

Suspect code areas:
```[language]
[code that might be leaking — caches, event listeners, closures, global state]
```

Please:
1. Identify potential memory leak sources in this code
2. Check for: unclosed connections, accumulating event listeners, growing caches without eviction, circular references
3. What profiling approach should I use to confirm?
   - [Language]-specific profiling tools
   - Heap snapshot comparison
4. Provide fixes for each identified leak
5. What monitoring should I add to detect memory leaks early?
```

### 4.4 CPU Spike

```
My application occasionally spikes to 100% CPU:

When it happens:
- [specific trigger or seemingly random]
- Duration: [how long the spike lasts]
- Frequency: [how often]

Suspect code:
```[language]
[potentially CPU-intensive code — loops, regex, serialization]
```

Thread/goroutine dump (if available):
```
[stack traces of threads during the spike]
```

Please:
1. Identify what could cause the CPU spike
2. Check for: infinite loops, catastrophic regex backtracking, excessive serialization, garbage collection pressure
3. How to reproduce and profile the spike
4. Provide the optimized code
5. What safeguards should prevent this? (timeouts, circuit breakers)
```

---

## 5. Concurrency Bugs

### 5.1 Race Condition

```
I have a race condition that causes incorrect results under concurrent access:

Code:
```[language]
[code with shared mutable state]
```

Symptoms:
- Under single-threaded access: works correctly
- Under concurrent access: [describe incorrect behavior]
- Frequency: [intermittent / every time under load]

Please:
1. Identify the critical section (shared state being read and modified non-atomically)
2. Explain the race condition step by step with a timeline of two threads
3. Provide multiple solutions:
   a. Mutex/lock-based solution
   b. Atomic operations (if applicable)
   c. Lock-free solution (if applicable)
   d. Database-level solution (if applicable)
4. Compare the tradeoffs of each solution
5. How to write a test that detects this race condition
```

### 5.2 Deadlock

```
My application occasionally freezes completely (deadlock):

Code with multiple locks:
```[language]
[code that acquires multiple locks or resources]
```

Thread dump during the freeze:
```
[thread dump showing waiting threads]
```

Please:
1. Identify the lock ordering that causes the deadlock
2. Draw the dependency graph (Thread A waits for Lock X held by Thread B, Thread B waits for Lock Y held by Thread A)
3. Provide the fix (consistent lock ordering, lock timeout, or restructuring)
4. How to detect deadlocks automatically (monitoring, lock timeouts)
5. Design guidelines to prevent future deadlocks
```

### 5.3 Async/Await Bugs

```
My async code is behaving unexpectedly:

Code:
```[language]
[async code with potential issues]
```

Symptoms: [describe unexpected behavior]

Please check for:
1. Missing await keywords (fire-and-forget when result is needed)
2. Unhandled promise rejections
3. Sequential awaits that should be parallel (Promise.all)
4. Stale closure capturing old state
5. Resource cleanup in error paths
6. Infinite loops from recursive async calls
7. Blocking the event loop with synchronous code in async context
8. Race conditions in shared async state
```

---

## 6. Integration Errors

### 6.1 API Integration Error

```
My application is getting errors when calling an external API:

Request:
```
[HTTP method] [URL]
Headers: [headers]
Body: [request body]
```

Response:
```
Status: [status code]
Headers: [response headers]
Body: [response body]
```

My client code:
```[language]
[API client code]
```

Expected behavior: [what should happen]
Actual behavior: [what actually happens]

Please:
1. Diagnose the error (authentication issue, malformed request, rate limiting, server error)
2. Is my request format correct according to the API documentation?
3. What am I missing? (headers, encoding, content type)
4. Provide the corrected client code
5. What error handling should I add for: timeout, rate limit, server error, invalid response?
```

### 6.2 Database Connection Issues

```
My application intermittently loses database connections:

Error:
```
[connection error message]
```

Database config:
```[language]
[connection pool configuration]
```

Application context:
- Request rate: [requests per second]
- Query patterns: [types of queries — short reads, long writes, etc.]
- Database: [PostgreSQL/MySQL/etc.] version [X]
- Connection pool size: [current setting]

Please:
1. Is the connection pool sized correctly for our workload?
2. Are connections being properly returned to the pool?
3. Are there long-running queries holding connections?
4. Is there a network issue (timeout, firewall, DNS)?
5. Provide the corrected connection configuration
6. What monitoring should I add?
```

---

## 7. Build and Dependency Errors

### 7.1 Dependency Conflict

```
I am getting a dependency conflict during build/install:

Error:
```
[full dependency resolution error]
```

My dependency file:
```
[package.json / requirements.txt / go.mod / etc.]
```

Please:
1. Which packages are conflicting and why?
2. What is the minimum set of version changes to resolve the conflict?
3. Are there alternative packages I should consider?
4. Is there a compatibility matrix I should be aware of?
5. Provide the updated dependency file
```

### 7.2 Import / Module Resolution Error

```
I am getting a module import error:

Error:
```
[ModuleNotFoundError / Cannot find module / import error]
```

My project structure:
```
[directory tree showing relevant files]
```

Import statement causing the error:
```[language]
[the import statement]
```

Configuration:
```
[tsconfig.json / pyproject.toml / package.json relevant sections]
```

Please:
1. Is the module installed? In the correct environment/node_modules?
2. Is the import path correct? (relative vs absolute, file extension)
3. Is the module configuration correct? (paths, baseUrl, module resolution)
4. Is there a circular import issue?
5. Provide the fix
```

---

## 8. Database Errors

### 8.1 Migration Failure

```
My database migration failed:

Migration script:
```sql
[migration SQL]
```

Error:
```
[migration error message]
```

Current schema state:
```sql
[relevant current schema]
```

Please:
1. Why did the migration fail?
2. Is the database in a partially migrated state? How to recover?
3. Provide the corrected migration
4. How to make it safe to re-run (idempotent)?
5. Should this migration be split into multiple steps?
```

### 8.2 Constraint Violation

```
I am getting a constraint violation:

Error:
```
[constraint violation error — unique, foreign key, check, not null]
```

Code attempting the operation:
```[language]
[code performing the database operation]
```

Relevant schema:
```sql
[table definition with constraints]
```

Please:
1. What constraint is being violated and why?
2. Is the constraint correct, or should it be changed?
3. Should the application validate before attempting the operation?
4. How to handle this error gracefully (user-friendly message)?
5. Is there a concurrency issue (two requests trying the same unique value)?
```

---

## 9. Frontend Errors

### 9.1 React Rendering Bug

```
My React component is not rendering correctly:

Component:
```tsx
[component code]
```

Props received: [props values]
Expected rendering: [what should appear]
Actual rendering: [what actually appears]

Please check for:
1. State not updating (mutation instead of new reference)
2. Missing key prop in lists
3. useEffect missing dependencies
4. Stale closure in event handlers
5. Conditional rendering logic errors
6. CSS/styling issues
7. Hydration mismatch (SSR)
```

### 9.2 State Management Bug

```
My application state is incorrect after a series of user interactions:

State management: [Redux / Zustand / Context / useState]

Initial state: [state at start]
User actions:
1. [action 1] -> expected state: [X], actual state: [Y]
2. [action 2] -> expected state: [X], actual state: [Y]

Relevant code:
```[language]
[state management code — reducers, actions, selectors]
```

Please:
1. Trace through each action and state transition
2. Identify where the state diverges from expected
3. Check for: direct state mutation, wrong action dispatched, selector returning stale data
4. Provide the fix
```

---

## 10. Infrastructure Errors

### 10.1 Docker Container Issues

```
My Docker container is failing:

Dockerfile:
```dockerfile
[Dockerfile content]
```

Error (build or run):
```
[error output]
```

Docker Compose (if applicable):
```yaml
[docker-compose.yml relevant sections]
```

Please:
1. Is this a build-time or runtime error?
2. Identify the specific layer/step that fails
3. Is it a missing dependency, permission issue, or configuration problem?
4. Provide the fixed Dockerfile/Compose
5. How to debug further (docker logs, exec into container)
```

### 10.2 Kubernetes Pod Issues

```
My Kubernetes pod is in [CrashLoopBackOff / Pending / ImagePullBackOff / OOMKilled]:

kubectl describe pod output:
```
[describe output]
```

kubectl logs output:
```
[pod logs]
```

Manifest:
```yaml
[pod/deployment YAML]
```

Please:
1. Interpret the pod status and events
2. Identify the root cause
3. Provide the specific fix
4. What resource adjustments are needed?
5. What monitoring should prevent this in the future?
```

---

## 11. Quick Reference Card

### Error Category Decision Tree

```
Error has a stack trace?
├── YES → Runtime Error (Section 2)
│   ├── Null/undefined → 2.1
│   ├── Index out of bounds → 2.2
│   ├── Stack overflow → 2.3
│   ├── Out of memory → 2.4
│   └── Type mismatch → 2.5
│
├── NO, but wrong output → Logic Error (Section 3)
│   ├── Wrong values → 3.1
│   ├── Wrong conditions → 3.2
│   ├── Off by one → 3.3
│   └── Precision issues → 3.4
│
├── NO, but slow → Performance Issue (Section 4)
│   ├── Slow query → 4.1
│   ├── Slow endpoint → 4.2
│   ├── Memory growing → 4.3
│   └── CPU spiking → 4.4
│
├── NO, but intermittent → Concurrency Bug (Section 5)
│   ├── Wrong results sometimes → 5.1 (Race condition)
│   ├── System freezes → 5.2 (Deadlock)
│   └── Async weird behavior → 5.3
│
└── Build/deploy failure → Sections 7-10
    ├── Dependency conflict → 7.1
    ├── Import error → 7.2
    ├── Docker failure → 10.1
    └── K8s pod issue → 10.2
```

### Debugging Checklist (Before Asking AI)

- [ ] **Reproduced** the bug locally
- [ ] **Collected** the full error message and stack trace
- [ ] **Identified** the minimal code that triggers the bug
- [ ] **Checked** recent changes (git log, deployment history)
- [ ] **Documented** what you have already tried
- [ ] **Noted** the environment (versions, OS, config)

### Effective Debugging Prompt Tips

1. **Be specific**: "My function returns 42 instead of 43" is better than "My function is broken"
2. **Include the full error**: Never truncate stack traces -- they contain crucial information
3. **Show minimal code**: Remove unrelated code, but keep enough context for the AI to understand
4. **State your hypothesis**: "I think it might be a race condition because..." helps AI confirm or redirect
5. **Share what you tried**: Prevents AI from suggesting things you already ruled out
