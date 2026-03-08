# Code Generation Prompt Templates

## Module 08: AI for Software Development and Security

> 50+ code generation prompts organized by language and task type.

---

## Table of Contents

1. [Python Prompts (1-12)](#python-prompts)
2. [JavaScript/TypeScript Prompts (13-22)](#javascripttypescript-prompts)
3. [Go Prompts (23-30)](#go-prompts)
4. [Rust Prompts (31-36)](#rust-prompts)
5. [Java/C# Prompts (37-42)](#javac-prompts)
6. [SQL Prompts (43-48)](#sql-prompts)
7. [Multi-Language Patterns (49-55)](#multi-language-patterns)

---

## Python Prompts

### Prompt 1: FastAPI CRUD Endpoint

```
Write a complete FastAPI CRUD module for a [RESOURCE_NAME] resource.

Resource fields: [list fields with types]
Database: PostgreSQL with SQLAlchemy 2.0 async
Auth: JWT Bearer token (assume get_current_user dependency exists)

Generate:
1. models.py — SQLAlchemy model with mapped_column style
2. schemas.py — Pydantic v2 models (Create, Update, Response, ListResponse with pagination)
3. repository.py — Async database operations (create, get_by_id, list_with_filters, update, delete)
4. service.py — Business logic with authorization checks
5. router.py — FastAPI router with all CRUD endpoints

Follow these conventions:
- UUID primary keys
- Soft delete (is_deleted flag)
- created_at/updated_at timestamps
- Proper error handling (404, 403, 409, 422)
- Pagination: cursor-based with page_size parameter
- Include OpenAPI examples in schemas
```

### Prompt 2: Python Data Pipeline

```
Write a Python data processing pipeline that:
- Reads data from [SOURCE: CSV file / API / database]
- Validates each record against a schema: [describe schema]
- Transforms the data: [describe transformations]
- Loads results into [DESTINATION: database / file / API]

Requirements:
- Use dataclasses for data models
- Use generators for memory-efficient processing
- Include progress reporting (tqdm or custom)
- Handle errors per-record (log and continue, do not stop pipeline)
- Support resumption (checkpoint file)
- Include retry logic for network operations
- Configurable batch size for database inserts
- Type hints throughout
- Logging with structured output (JSON)
- No Pandas — use stdlib and minimal dependencies
```

### Prompt 3: Python Decorator Library

```
Write a Python utility module with these decorators:

1. @retry(max_attempts=3, backoff_factor=2, exceptions=(ConnectionError,))
   - Retries function on specified exceptions
   - Exponential backoff with jitter
   - Works with both sync and async functions
   - Logs each retry attempt

2. @cache(ttl=300, maxsize=1000)
   - In-memory cache with TTL
   - Thread-safe
   - LRU eviction when maxsize reached
   - Works with hashable arguments

3. @rate_limit(calls=10, period=60)
   - Token bucket rate limiter
   - Thread-safe
   - Raises RateLimitExceeded after limit

4. @timeout(seconds=30)
   - Raises TimeoutError if function takes too long
   - Works with both sync and async functions
   - Properly cleans up on timeout

5. @validate_args(**validators)
   - Validates function arguments before execution
   - Validators are callables returning bool
   - Raises ValueError with descriptive message

Each decorator must:
- Preserve function signature (functools.wraps)
- Include type hints using ParamSpec and TypeVar
- Work as both @decorator and @decorator() (with and without arguments)
- Include docstring with usage examples
```

### Prompt 4: Python CLI Application

```
Write a Python CLI application using Click:

Command: `taskctl` — a task management CLI

Subcommands:
- `taskctl add "Task title" --priority high --due 2025-03-01 --tags bug,frontend`
- `taskctl list [--status todo|done|all] [--priority low|medium|high] [--tag TAG]`
- `taskctl done TASK_ID`
- `taskctl edit TASK_ID [--title "New title"] [--priority medium]`
- `taskctl delete TASK_ID [--force]`
- `taskctl stats` — Show task statistics

Storage: SQLite database in ~/.taskctl/tasks.db
Output: Rich library for tables and formatting
Config: ~/.taskctl/config.yaml for defaults

Include:
- Auto-completion for shell (Click's built-in)
- Color-coded priority and status
- Confirmation prompt for delete (unless --force)
- Export command (JSON, CSV)
- Import command (from JSON)
```

### Prompt 5: Python Background Worker

```
Write a Python background task worker using asyncio:

Worker processes jobs from a Redis queue:
- Queue name: "tasks:{task_type}"
- Job format: JSON with {id, type, payload, created_at, attempts}
- Supports multiple task types with registered handlers
- Configurable concurrency (max concurrent tasks)
- Automatic retry with exponential backoff (max 3 attempts)
- Dead letter queue for failed tasks
- Graceful shutdown on SIGTERM/SIGINT
- Health check endpoint (HTTP on configurable port)
- Structured logging with job context
- Metrics: jobs processed, failed, processing time

Include:
- Worker class
- TaskHandler base class/protocol
- Example handlers for: send_email, resize_image, generate_report
- Configuration via environment variables
- Docker-ready (proper signal handling)
```

### Prompt 6: Python WebSocket Server

```
Write a FastAPI WebSocket server for real-time notifications:

Features:
- Authenticated WebSocket connections (JWT token in query param)
- Room-based messaging (subscribe to project channels)
- Event types: task_created, task_updated, task_assigned, comment_added
- Connection management (track active connections per user)
- Heartbeat/ping-pong for connection health
- Reconnection support (send missed events since last_event_id)
- Rate limiting on outgoing messages

Include:
- ConnectionManager class
- Event schemas (Pydantic models)
- WebSocket endpoint
- Utility function to broadcast events from API endpoints
- Tests for WebSocket connections
```

### Prompt 7: Python Configuration Management

```
Write a configuration management module:

- Load from: environment variables, .env file, YAML config file, CLI arguments
- Priority: CLI > environment > .env > YAML > defaults
- Validation: Pydantic settings with validators
- Secrets: Support for AWS Secrets Manager / HashiCorp Vault (pluggable)
- Type coercion: Strings to int, bool, list, dict automatically
- Nested configuration support
- Environment-specific configs (development, staging, production)
- Hot reload: Watch config file for changes
- Include: database, redis, jwt, cors, logging, email settings

Generate the config module and example configuration files.
```

### Prompt 8: Python Testing Utilities

```
Write a testing utilities module for a FastAPI application:

1. Database test fixtures:
   - Async test database setup/teardown
   - Transaction rollback after each test
   - Database seeding with test data

2. Factory classes (factory-boy):
   - UserFactory (with hashed password)
   - ProjectFactory (with owner)
   - TaskFactory (with project and assignee)

3. Authentication helpers:
   - create_test_token(user) — Generate JWT for test user
   - authenticated_client(user) — Return httpx client with auth headers

4. API test helpers:
   - assert_api_error(response, status_code, error_code)
   - assert_paginated_response(response, expected_count)
   - assert_created(response, expected_fields)

5. Mock helpers:
   - MockRedis — In-memory Redis mock
   - MockEmailService — Captures sent emails
   - MockFileStorage — In-memory file storage

Use pytest fixtures and conftest.py patterns.
```

### Prompt 9: Python Data Validation Library

```
Write a data validation library for API input:

- Validate email addresses (RFC 5322 compliant)
- Validate phone numbers (E.164 format)
- Validate URLs (with scheme whitelist)
- Validate credit card numbers (Luhn algorithm, card type detection)
- Validate dates (format, range, business day checks)
- Validate passwords (configurable rules: length, complexity, common password list)
- Validate UUIDs (version 4)
- Validate slugs (URL-safe strings)
- Validate file uploads (MIME type, size, dimensions for images)

Each validator should:
- Return a ValidationResult with is_valid, errors, sanitized_value
- Be usable standalone and as Pydantic validators
- Include comprehensive unit tests
- Handle edge cases (unicode, special characters, None)
```

### Prompt 10: Python ORM Query Builder

```
Write a dynamic query builder for SQLAlchemy async:

Features:
- Fluent API: query.filter(status="active").sort("-created_at").paginate(page=2, size=20)
- Support operators: eq, ne, gt, gte, lt, lte, in, not_in, like, ilike, between, is_null
- Date range helpers: created_today(), created_this_week(), created_between(start, end)
- Relation loading: .include("author", "comments.user")
- Aggregation: .count(), .sum("amount"), .avg("rating")
- Search: .search(["title", "description"], query="keyword")
- Pagination: Cursor-based and offset-based
- Sorting: Multiple columns, ascending/descending

Generate:
- QueryBuilder[T] generic class
- FilterSpec data class
- PaginatedResponse[T] data class
- Usage examples with a real SQLAlchemy model
```

### Prompt 11: Python Event System

```
Write an in-process event system (event bus):

Features:
- Type-safe event definitions using dataclasses
- Subscribe to events by type
- Async and sync handlers
- Handler priority ordering
- Event middleware (logging, error handling)
- Wildcard subscriptions (subscribe to all events)
- One-time handlers (auto-unsubscribe after first call)
- Error isolation (one handler failure does not stop others)

Example usage:
@dataclass
class UserCreated(Event):
    user_id: str
    email: str

@event_bus.on(UserCreated, priority=10)
async def send_welcome_email(event: UserCreated):
    await email_service.send_welcome(event.email)

await event_bus.emit(UserCreated(user_id="123", email="user@example.com"))
```

### Prompt 12: Python File Processing

```
Write a file processing module:

Functions:
1. parse_csv(file, schema) — Parse CSV with schema validation
2. parse_excel(file, sheet_name, schema) — Parse Excel file
3. generate_pdf(template, data) — Generate PDF from HTML template
4. resize_image(file, width, height, quality) — Resize and optimize image
5. extract_text(file) — Extract text from PDF
6. generate_csv(data, columns) — Generate CSV from data
7. validate_file(file, allowed_types, max_size) — Validate uploaded file

Requirements:
- Streaming processing for large files
- Memory-efficient (do not load entire file into memory)
- Error handling with descriptive messages
- Progress callback for long operations
- Support for S3 sources/destinations
- Type hints and docstrings
```

---

## JavaScript/TypeScript Prompts

### Prompt 13: React Custom Hooks Library

```
Write a TypeScript React custom hooks library:

1. useDebounce<T>(value: T, delay: number): T
2. useThrottle<T>(value: T, delay: number): T
3. useLocalStorage<T>(key: string, initialValue: T): [T, (value: T) => void]
4. useMediaQuery(query: string): boolean
5. usePrevious<T>(value: T): T | undefined
6. useClickOutside(ref: RefObject, handler: () => void): void
7. useIntersectionObserver(ref: RefObject, options?): IntersectionObserverEntry | null
8. useFetch<T>(url: string, options?): { data: T | null, loading: boolean, error: Error | null }
9. useForm<T>(initialValues: T, validate: (values: T) => Errors<T>): FormMethods<T>
10. useKeyPress(targetKey: string, handler: () => void): void

Each hook must:
- Include full TypeScript generics where appropriate
- Include JSDoc with usage examples
- Handle cleanup (event listeners, timers, subscriptions)
- Be tested with React Testing Library
```

### Prompt 14: Express.js Middleware Collection

```
Write a TypeScript Express middleware collection:

1. requestLogger — Structured JSON logging with request ID, duration, status
2. errorHandler — Centralized error handling with error classification
3. rateLimiter — Redis-backed rate limiting with sliding window
4. authenticate — JWT authentication with role extraction
5. authorize(...roles) — Role-based authorization middleware factory
6. validateBody(schema) — Zod schema validation for request body
7. cors — Configurable CORS with credential support
8. requestId — Generate and attach unique request ID
9. compression — Response compression with threshold
10. cacheControl(maxAge) — Cache headers middleware

Each middleware must:
- Export as a factory function with configuration options
- Include TypeScript types for options
- Include error handling
- Include JSDoc documentation
- Be chainable with other middleware
```

### Prompt 15: Next.js API Routes

```
Write Next.js 14 API routes (App Router) for a blog platform:

Routes:
1. app/api/posts/route.ts — GET (list with pagination), POST (create)
2. app/api/posts/[id]/route.ts — GET, PUT, DELETE
3. app/api/posts/[id]/comments/route.ts — GET (list), POST (create)
4. app/api/auth/[...nextauth]/route.ts — NextAuth.js configuration
5. app/api/upload/route.ts — Image upload with validation

Include:
- Zod validation for all inputs
- NextAuth session verification
- Error responses in consistent format
- Response types (TypeScript interfaces)
- Rate limiting using upstash/ratelimit
- Edge runtime where appropriate
```

### Prompt 16: TypeScript Utility Types and Functions

```
Write a TypeScript utility module with advanced type utilities:

Types:
1. DeepPartial<T> — Make all nested properties optional
2. DeepRequired<T> — Make all nested properties required
3. DeepReadonly<T> — Make all nested properties readonly
4. Prettify<T> — Flatten intersection types for readability
5. StrictOmit<T, K> — Omit that errors if K is not a key of T
6. NonEmptyArray<T> — Array that must have at least one element
7. Branded<T, Brand> — Branded/opaque types (e.g., UserId = Branded<string, 'UserId'>)
8. Result<T, E> — Rust-like Result type with Ok/Err
9. AsyncResult<T, E> — Promise<Result<T, E>> with utility methods
10. EventMap<T> — Type-safe event emitter map

Functions:
1. pipe(...fns) — Type-safe pipe function
2. match(value, patterns) — Pattern matching
3. exhaustiveCheck(value: never) — Ensure exhaustive switch/if
4. retry(fn, options) — Retry async function with backoff
5. chunk(array, size) — Split array into chunks of given size
```

### Prompt 17: React State Management

```
Write a lightweight React state management solution in TypeScript:

Features:
- createStore<T>(initialState, actions) — Create a type-safe store
- useStore(store, selector?) — Hook to consume store with optional selector
- Middleware support (logging, persistence, devtools)
- Computed values (derived state)
- Async actions support
- Undo/redo support
- Store persistence to localStorage
- DevTools integration (if window.__REDUX_DEVTOOLS_EXTENSION__ exists)

API Example:
const counterStore = createStore({
  state: { count: 0, name: "counter" },
  actions: {
    increment: (state) => ({ ...state, count: state.count + 1 }),
    decrement: (state) => ({ ...state, count: state.count - 1 }),
    setCount: (state, count: number) => ({ ...state, count }),
    asyncIncrement: async (state) => {
      await delay(1000);
      return { ...state, count: state.count + 1 };
    }
  },
  computed: {
    isPositive: (state) => state.count > 0,
    doubled: (state) => state.count * 2,
  }
});

// In component:
const count = useStore(counterStore, s => s.count);
const { increment, setCount } = counterStore.actions;
```

### Prompt 18: Node.js File Processing

```
Write a TypeScript Node.js file processing library:

1. CSV Parser: Stream-based CSV parsing with schema validation
2. JSON Lines: Read and write JSONL files efficiently
3. File Watcher: Watch directory for changes with debounce
4. Archive: Create and extract tar.gz archives
5. Temp Files: Create temporary files/directories with automatic cleanup
6. File Hash: Calculate MD5/SHA-256 of files (streaming)
7. Directory Walker: Recursively walk directories with glob filtering
8. File Lock: Advisory file locking for concurrent access

Each utility must:
- Use Node.js streams for memory efficiency
- Handle errors gracefully
- Support cancellation via AbortController
- Include TypeScript types
- Include progress events for long operations
```

### Prompt 19: React Form Library

```
Write a lightweight React form library in TypeScript:

Features:
- useForm<T>(config) hook
- Field-level validation (sync and async)
- Form-level validation
- Touched/dirty state tracking
- Submit handling with loading state
- Array fields (add/remove/reorder)
- Nested object fields
- Custom field components via render props
- Error display helpers
- Form reset and pre-fill
- Integration with Zod schemas

Do not use any form library as a dependency.
Under 500 lines of code total.
```

### Prompt 20: TypeScript API Client Generator

```
Write a TypeScript API client generator:

Input: An API specification object like:
const api = defineApi({
  baseUrl: '/api/v1',
  endpoints: {
    getUsers: { method: 'GET', path: '/users', response: User[] },
    getUser: { method: 'GET', path: '/users/:id', response: User },
    createUser: { method: 'POST', path: '/users', body: CreateUserInput, response: User },
    updateUser: { method: 'PUT', path: '/users/:id', body: UpdateUserInput, response: User },
    deleteUser: { method: 'DELETE', path: '/users/:id', response: void },
  }
});

Output: A fully typed API client:
const client = createClient(api);
const users = await client.getUsers(); // Type: User[]
const user = await client.getUser({ id: '123' }); // Type: User
const newUser = await client.createUser({ body: { name: 'Alice' } }); // Type: User

Features:
- Full TypeScript inference (no codegen needed)
- Axios or fetch-based
- Interceptors for auth tokens
- Request/response transformation
- Error handling
- Request cancellation
- Retry logic
```

### Prompt 21: WebSocket Client with Reconnection

```
Write a TypeScript WebSocket client class:

Features:
- Automatic reconnection with exponential backoff
- Heartbeat/ping-pong to detect dead connections
- Event-based API: on('message', handler), on('connect', handler)
- Type-safe events with generics
- Message queuing during disconnection (send when reconnected)
- Authentication support (token in connection params)
- Room/channel subscription management
- Connection state tracking (connecting, connected, disconnecting, disconnected)
- Binary message support
- Maximum reconnection attempts with configurable limit

Works in both browser and Node.js environments.
```

### Prompt 22: React Data Table Component

```
Write a TypeScript React data table component:

Props:
- data: T[] — Array of row data
- columns: ColumnDef<T>[] — Column definitions
- loading: boolean
- pagination: { page, pageSize, total, onChange }
- sorting: { column, direction, onChange }
- selection: { selected, onChange } (optional)
- expandable: { render: (row) => ReactNode } (optional)

Features:
- Server-side sorting and pagination
- Column resizing
- Row selection (single and multi)
- Expandable rows
- Sticky header
- Loading skeleton
- Empty state
- Keyboard navigation (arrow keys, Enter to expand)
- Accessible (proper ARIA table roles)

Use TailwindCSS. No external table library.
Under 400 lines total.
```

---

## Go Prompts

### Prompt 23: Go HTTP Server

```
Write a Go HTTP server with:
- Standard library only (net/http)
- Go 1.22 routing with method patterns
- Middleware chain (logging, recovery, CORS, auth)
- JSON request/response helpers
- Error handling with proper HTTP status codes
- Graceful shutdown on SIGTERM
- Health check endpoint
- Request ID middleware
- Structured logging with slog

Include:
- server.go — Server setup and middleware
- handlers/ — Example CRUD handlers for a "users" resource
- middleware/ — Middleware implementations
- response/ — Response helpers
```

### Prompt 24: Go Repository Pattern

```
Write a Go repository implementation with:
- Generic Repository[T any] interface
- PostgreSQL implementation using pgx/v5
- Transaction support
- Dynamic query builder for filters
- Cursor-based pagination
- Soft delete support
- Audit logging (created_by, updated_by)

Include:
- repository.go — Interface definitions
- postgres.go — PostgreSQL implementation
- query_builder.go — Dynamic filter/sort builder
- Example: UserRepository implementation
- Tests using testcontainers-go with real PostgreSQL
```

### Prompt 25: Go Worker Pool

```
Write a generic Go worker pool:

type WorkerPool[T, R any] struct { ... }

Features:
- Configurable number of workers
- Submit jobs via channel
- Collect results via channel
- Context cancellation support
- Graceful shutdown (drain queue)
- Error handling per job
- Retry with backoff
- Job timeout
- Metrics (processed, failed, in-flight)
- Rate limiting (max jobs per second)

Usage:
pool := NewWorkerPool[Input, Output](WorkerPoolConfig{
    Workers:    10,
    BufferSize: 100,
    RetryMax:   3,
    JobTimeout: 30 * time.Second,
})
pool.Start(ctx, processFunc)
pool.Submit(input)
result := <-pool.Results()
```

### Prompt 26: Go CLI Tool

```
Write a Go CLI tool using cobra:

Command: `svcgen` — Service code generator
Subcommands:
- `svcgen init` — Initialize project structure
- `svcgen add resource <name>` — Add a new CRUD resource with handler, service, repository, model
- `svcgen add middleware <name>` — Add middleware skeleton
- `svcgen migrate create <name>` — Create migration file
- `svcgen migrate up` — Run pending migrations
- `svcgen docs` — Generate OpenAPI documentation from code annotations

Each command generates Go source files from templates.
Use Go's text/template for code generation.
Include proper error handling, progress output, and --dry-run flag.
```

### Prompt 27: Go Middleware Library

```
Write a Go HTTP middleware library:

1. Logger — Structured request/response logging with slog
2. Recoverer — Panic recovery with stack trace logging
3. RequestID — Generate and propagate request IDs
4. CORS — Configurable CORS headers
5. RateLimit — Token bucket rate limiter (in-memory and Redis)
6. Timeout — Request timeout with context
7. Auth — JWT validation with claims extraction
8. Compress — Response compression (gzip, deflate)
9. Cache — HTTP cache headers and in-memory cache
10. Metrics — Prometheus metrics (request count, duration, size)

Each middleware must:
- Follow the func(http.Handler) http.Handler pattern
- Be independently usable
- Be composable with other middleware
- Include configuration options
- Include tests
```

### Prompt 28: Go Error Handling

```
Write a comprehensive Go error handling package:

Features:
1. Custom error types with codes: AppError{Code, Message, Details, HTTPStatus, Cause}
2. Error wrapping with context: Wrap(err, "context message")
3. Error type checking: Is(err, ErrNotFound), As(err, &appErr)
4. Stack trace capture for debugging
5. Predefined errors: NotFound, Unauthorized, Forbidden, Validation, Internal, Conflict
6. Validation error builder: ValidationError().Field("email", "invalid format").Field("age", "must be positive")
7. HTTP response conversion: ToHTTPResponse(err) -> (statusCode, body)
8. Slog integration: LogError(logger, err) logs with proper level and attributes
9. Error catalog for documentation

Include tests and usage examples.
```

### Prompt 29: Go Database Migration Tool

```
Write a Go database migration library:

Features:
- SQL migration files (YYYYMMDDHHMMSS_name.up.sql / .down.sql)
- Migration status tracking table
- Up, Down, Redo, Reset, Status commands
- Transaction per migration
- Dry run mode
- Migration locking (prevent concurrent migrations)
- PostgreSQL support via pgx
- Migration file generator
- Embedding migrations with embed.FS
- Programmatic API and CLI interface

Include:
- migrator.go — Core migration logic
- migration.go — Migration file loading and parsing
- postgres.go — PostgreSQL-specific implementation
- cli.go — Command-line interface
- Example migration files
```

### Prompt 30: Go Configuration Library

```
Write a Go configuration library:

Features:
- Load from: environment variables, .env file, YAML/JSON config file, CLI flags
- Priority: CLI flags > env vars > .env > config file > defaults
- Struct tags: `env:"DB_HOST" yaml:"db.host" default:"localhost" required:"true"`
- Nested struct support
- Type conversion (string to int, bool, duration, []string)
- Validation (required fields, format, range)
- Secret masking in logging
- Hot reload with file watching
- Thread-safe access
- Generated documentation from struct tags

Usage:
type Config struct {
    Server struct {
        Port int    `env:"PORT" yaml:"server.port" default:"8080"`
        Host string `env:"HOST" yaml:"server.host" default:"0.0.0.0"`
    }
    Database struct {
        URL string `env:"DATABASE_URL" yaml:"database.url" required:"true" secret:"true"`
    }
}

var cfg Config
err := Load(&cfg)
```

---

## Rust Prompts

### Prompt 31: Rust CLI Application

```
Write a Rust CLI application using clap v4:

Command: `fwatch` — File watcher and processor
Usage: fwatch [OPTIONS] <DIRECTORY> <COMMAND>

Features:
- Watch a directory for file changes (create, modify, delete)
- Execute a command when changes are detected
- Debounce (configurable, default 300ms)
- Glob patterns for include/exclude
- Recursive watching
- Quiet mode (suppress output)
- Initial run (execute command once before watching)
- Signal handling (Ctrl+C graceful shutdown)

Options:
--debounce <MS>      Debounce interval (default: 300)
--include <GLOB>     Include pattern (can be repeated)
--exclude <GLOB>     Exclude pattern (can be repeated)
--initial            Run command once before watching
--quiet              Suppress file change output
--clear              Clear screen before each run

Use: clap (derive API), notify (file watching), anyhow (error handling)
```

### Prompt 32: Rust Error Handling Module

```
Write a Rust error handling module for a web application:

Using thiserror:
- AppError enum with variants: NotFound, Unauthorized, Forbidden,
  Validation(Vec<FieldError>), Conflict, Internal, BadRequest,
  ExternalService(String), Database, RateLimited
- Implement std::fmt::Display with user-friendly messages
- Implement From for common error types (sqlx::Error, reqwest::Error,
  serde_json::Error, std::io::Error)
- Implement axum::response::IntoResponse for HTTP error responses
- JSON error format: { "error": { "code": "NOT_FOUND", "message": "...", "details": [...] } }
- FieldError struct: { field: String, code: String, message: String }
- Error context extension trait: .context("additional info")
- Result type alias: type AppResult<T> = Result<T, AppError>

Include comprehensive tests.
```

### Prompt 33: Rust Async HTTP Client

```
Write a Rust async HTTP client wrapper:

Features:
- Built on reqwest
- Automatic retry with exponential backoff
- Circuit breaker pattern
- Request/response logging
- Timeout configuration
- Base URL and default headers
- JSON serialization/deserialization with serde
- Bearer token authentication (with auto-refresh callback)
- Rate limiting (client-side)
- Response caching (in-memory, TTL-based)

API:
let client = HttpClient::builder()
    .base_url("https://api.example.com")
    .timeout(Duration::from_secs(30))
    .retry(RetryConfig { max_retries: 3, backoff: Duration::from_secs(1) })
    .auth(BearerAuth::new(token))
    .build()?;

let users: Vec<User> = client.get("/users").query(&[("page", "1")]).send().await?.json()?;
```

### Prompt 34: Rust Data Structures

```
Write these data structures in Rust with comprehensive implementations:

1. LRUCache<K, V> — Least Recently Used cache
   - O(1) get and put
   - Configurable max size
   - TTL support per entry
   - Iterator support
   - Thread-safe version (with Arc<Mutex>)

2. BloomFilter<T> — Probabilistic set membership
   - Configurable false positive rate
   - Multiple hash functions
   - Serialization support
   - Merge two bloom filters

3. Trie<V> — Prefix tree
   - Insert, search, delete
   - Prefix search (find all keys with prefix)
   - Longest prefix match
   - Iterator over all entries

Each must include:
- Full trait implementations (Debug, Clone, Iterator, etc.)
- Comprehensive unit tests
- Benchmark tests (using criterion)
- Documentation with examples
```

### Prompt 35: Rust Web Server Module

```
Write a Rust web server module using axum:

Features:
- CRUD endpoints for a generic resource
- Request validation with validator crate
- JWT authentication middleware
- Role-based authorization
- Database layer with sqlx (PostgreSQL)
- Structured error handling (from Prompt 32)
- OpenAPI documentation with utoipa
- Request ID tracking
- Structured logging with tracing

Generate:
- main.rs — Server setup and routing
- models.rs — Database models
- handlers.rs — Request handlers
- middleware.rs — Auth and logging middleware
- db.rs — Database connection and queries
- config.rs — Configuration from environment
- error.rs — Error types and handling
```

### Prompt 36: Rust Testing Utilities

```
Write Rust testing utilities:

1. Test fixtures:
   - Database test helpers (create test database, run migrations, cleanup)
   - Test server (spawn axum server on random port, return client)
   - Factory traits for creating test entities

2. Assertion helpers:
   - assert_json_eq!(response, expected) — Compare JSON responses
   - assert_status!(response, StatusCode) — Check HTTP status
   - assert_error_code!(response, "NOT_FOUND") — Check error response

3. Mock server:
   - MockServer for external API testing
   - Configurable responses per endpoint
   - Request recording for assertions

4. Property-based testing:
   - Arbitrary implementations for domain types
   - Strategy generators for common patterns

Use: tokio::test, sqlx::test, proptest
```

---

## Java/C# Prompts

### Prompt 37: Spring Boot Service Layer

```
Write a Spring Boot 3.2 service layer with:

- Generic CrudService<T, ID> base class
- Specification-based dynamic filtering
- Pagination and sorting support
- Audit logging (who changed what, when)
- Event publishing (entity created/updated/deleted events)
- Caching with Spring Cache (Redis)
- Transaction management
- Validation with Jakarta Validation

Include:
- CrudService base class
- Example: ProductService extending CrudService
- ProductSpecification for dynamic filtering
- Product events (ProductCreated, ProductUpdated, ProductDeleted)
- Unit tests with Mockito
- Integration tests with @SpringBootTest

Use Java 21 features: records, pattern matching, sealed classes.
```

### Prompt 38: .NET Minimal API

```
Write a .NET 8 Minimal API for an inventory management system:

Endpoints:
- Products CRUD
- Categories CRUD
- Stock adjustments (add/remove stock with reason)
- Stock level reports

Features:
- Entity Framework Core with PostgreSQL
- FluentValidation for input validation
- MediatR for CQRS pattern
- Serilog for structured logging
- Swagger/OpenAPI documentation
- Health checks (database, Redis)
- Response caching
- Global exception handling

Use records for DTOs, nullable reference types, and
file-scoped namespaces throughout.
```

### Prompt 39: Java Repository with Specifications

```
Write a Spring Data JPA repository with dynamic query support:

- Base repository interface extending JpaRepository and JpaSpecificationExecutor
- Specification builder for type-safe dynamic queries
- Support filters: equals, contains, between, in, isNull, greaterThan, lessThan
- Combine filters with AND/OR
- Sortable by any field
- Paginated results

Usage:
var spec = SpecificationBuilder.<Product>builder()
    .where("name", contains, "laptop")
    .and("price", between, 500, 2000)
    .and("category.name", eq, "Electronics")
    .and("status", in, List.of("ACTIVE", "ON_SALE"))
    .build();

Page<Product> results = productRepo.findAll(spec, PageRequest.of(0, 20, Sort.by("price")));
```

### Prompt 40: C# Background Service

```
Write a .NET 8 Background Service for processing queued jobs:

Features:
- IHostedService implementation
- Read jobs from RabbitMQ queue
- Process different job types with registered handlers
- Retry failed jobs with exponential backoff
- Dead letter queue for permanently failed jobs
- Health check reporting
- Graceful shutdown
- Structured logging with Serilog
- Dependency injection for job handlers
- Concurrent processing (configurable worker count)

Include:
- JobProcessor background service
- IJobHandler<T> interface
- Example handlers: SendEmailJob, GenerateReportJob
- Job serialization/deserialization
- Error handling and retry logic
- Unit tests
```

### Prompt 41: Java Stream Processing

```
Write Java data processing utilities using Streams API (Java 21):

1. CollectionUtils:
   - groupAndAggregate(Collection<T>, Function<T,K> groupBy, Collector<T,?,R> aggregator)
   - partition(Collection<T>, int batchSize) -> List<List<T>>
   - zipWith(List<A>, List<B>, BiFunction<A,B,C>) -> List<C>
   - sliding(List<T>, int windowSize) -> Stream<List<T>>

2. MapUtils:
   - mergeMaps(Map<K,V>...) with conflict resolver
   - invertMap(Map<K,V>) -> Map<V,List<K>>
   - filterByKeys(Map<K,V>, Predicate<K>)
   - transformValues(Map<K,V>, Function<V,R>) -> Map<K,R>

3. StreamUtils:
   - distinctBy(Function<T,K> keyExtractor) -> Stream filter
   - takeWhileInclusive(Predicate<T>) -> Stream operator
   - parallelBatchProcess(Stream<T>, int batchSize, Function<List<T>, List<R>>)
   - toFrequencyMap(Stream<T>) -> Map<T, Long>

Include comprehensive JUnit 5 tests for each utility.
```

### Prompt 42: C# CQRS with MediatR

```
Write a complete CQRS implementation in .NET 8 with MediatR:

Commands:
1. CreateOrder -> OrderId
2. UpdateOrderStatus -> Unit
3. CancelOrder -> Unit

Queries:
1. GetOrderById -> OrderDto
2. GetOrdersByCustomer -> PagedResult<OrderDto>
3. GetOrderStatistics -> OrderStatsDto

Infrastructure:
1. ValidationBehavior<TRequest, TResponse> — FluentValidation pipeline
2. LoggingBehavior<TRequest, TResponse> — Request/response logging
3. CachingBehavior<TRequest, TResponse> — Response caching for queries
4. TransactionBehavior<TRequest, TResponse> — Transaction wrapping for commands

Include:
- Command/Query classes (records)
- Handler implementations
- Validators (FluentValidation)
- Domain events (OrderCreated, OrderStatusChanged, OrderCancelled)
- Unit tests for each handler
- Integration test for the full pipeline
```

---

## SQL Prompts

### Prompt 43: Database Schema Design

```
Write a PostgreSQL schema for a [DOMAIN] application:

[Describe the domain and entities]

Requirements:
- UUID primary keys using gen_random_uuid()
- Proper foreign keys with cascading behavior
- CHECK constraints for enums and business rules
- Indexes for all foreign keys and common query patterns
- Composite indexes for multi-column queries
- Partial indexes where appropriate
- created_at (DEFAULT now()), updated_at (trigger-based)
- Soft delete (deleted_at timestamp)
- Audit columns (created_by, updated_by)
- Table and column comments
- Use appropriate data types (not everything is VARCHAR)

Also include:
- A function and trigger for auto-updating updated_at
- ENUM types for status fields
- A materialized view for a common reporting query
```

### Prompt 44: Complex Analytical Query

```
Write a PostgreSQL query for [ANALYSIS DESCRIPTION]:

Tables: [describe tables and their columns]

The query should:
- [Requirement 1 — e.g., Calculate monthly trends]
- [Requirement 2 — e.g., Include year-over-year comparison]
- [Requirement 3 — e.g., Rank results by a metric]

Requirements:
- Use CTEs for readability
- Use window functions where appropriate
- Handle NULL values and empty results
- Optimize for tables with [X million] rows
- Include index recommendations as comments
- Use EXPLAIN ANALYZE comments for key decisions
```

### Prompt 45: Database Migration Script

```
Write a PostgreSQL migration script to [CHANGE DESCRIPTION]:

Current schema: [describe relevant current tables]

The migration must:
- Be safe to run on production (no long locks)
- Support concurrent access during migration
- Be idempotent (safe to run multiple times)
- Include both UP and DOWN scripts
- Handle data migration if needed
- Use CREATE INDEX CONCURRENTLY for new indexes
- Include progress comments for long operations

Test the migration against edge cases:
- Empty tables
- Tables with millions of rows
- NULL values in affected columns
- Concurrent transactions during migration
```

### Prompt 46: PostgreSQL Functions and Triggers

```
Write PostgreSQL functions and triggers for:

1. Auto-update `updated_at` on row modification
2. Audit logging — Record all changes to an audit_log table with:
   - Table name, operation (INSERT/UPDATE/DELETE), old_data, new_data (JSONB)
   - User ID from session variable (set_config/current_setting)
   - Timestamp
3. Soft delete cascade — When a parent is soft-deleted, soft-delete children
4. Search vector update — Automatically update tsvector column for full-text search
5. Validation trigger — Complex business rule validation before INSERT/UPDATE

Each function must include:
- SECURITY DEFINER or SECURITY INVOKER (with justification)
- Proper error handling (RAISE EXCEPTION)
- Performance considerations
- Tests (using pgTAP or plain SQL assertions)
```

### Prompt 47: Database Performance Optimization

```
Optimize this PostgreSQL query:

```sql
[slow query]
```

EXPLAIN ANALYZE output:
```
[paste explain analyze output]
```

Table definitions:
```sql
[relevant CREATE TABLE statements]
```

Current indexes:
```sql
[current index definitions]
```

Table statistics:
- [table_name]: [row count]

Please:
1. Identify the performance bottleneck
2. Rewrite the query for better performance
3. Suggest new indexes (with size estimate)
4. Consider partial indexes and covering indexes
5. Evaluate if a materialized view would help
6. Estimate the improvement
7. Consider the write performance impact of new indexes
```

### Prompt 48: Row-Level Security

```
Write PostgreSQL Row-Level Security (RLS) policies for a multi-tenant SaaS:

Tables: users, tenants, tenant_members, projects, tasks

Requirements:
- Users can only see data belonging to their tenant
- Tenant admins can see all tenant data
- Project managers can see project-level data
- Regular members see only assigned tasks
- Super admins (platform level) can see everything
- Tenant context set via SET app.current_tenant_id = 'uuid'

Generate:
1. RLS policies for each table
2. Helper functions for permission checking
3. Session variable management functions
4. Test scenarios verifying isolation
5. Performance considerations for RLS
```

---

## Multi-Language Patterns

### Prompt 49: Repository Pattern (Any Language)

```
Implement the Repository pattern in [LANGUAGE]:

Interface:
- FindById(id) -> Entity | null
- FindAll(filters, pagination, sorting) -> PagedResult<Entity>
- Create(input) -> Entity
- Update(id, input) -> Entity
- Delete(id) -> void
- Exists(id) -> bool
- Count(filters) -> int

Include:
- Generic interface/trait definition
- Concrete implementation for [DATABASE]
- Unit of Work / Transaction support
- Query specification pattern for complex filters
- Caching decorator (optional layer)
- Test implementation (in-memory)
```

### Prompt 50: Event-Driven Architecture (Any Language)

```
Implement an event-driven system in [LANGUAGE]:

Components:
1. Event base type/class/trait
2. Event bus (in-process pub/sub)
3. Event handler registration
4. Async event processing
5. Event store (append-only log)
6. Event replay capability
7. Dead letter handling for failed events

Event types to implement:
- OrderPlaced { orderId, customerId, items[], total }
- PaymentProcessed { orderId, paymentId, amount, status }
- InventoryReserved { orderId, items[] }
- OrderConfirmed { orderId, estimatedDelivery }
- OrderFailed { orderId, reason }

Show the saga pattern for order processing:
OrderPlaced -> PaymentProcessed -> InventoryReserved -> OrderConfirmed
With compensation events for failure at each step.
```

### Prompt 51: Authentication System (Any Language)

```
Implement a complete authentication system in [LANGUAGE]:

Features:
1. Registration with email verification
2. Login with JWT (access + refresh tokens)
3. Password reset via email
4. Multi-factor authentication (TOTP)
5. OAuth2 social login (Google, GitHub)
6. Session management
7. Account lockout after failed attempts
8. Password strength validation
9. Audit logging of all auth events
10. Rate limiting on auth endpoints

Security requirements:
- Passwords hashed with bcrypt/argon2 (cost factor 12+)
- JWT signed with RS256 (asymmetric)
- Refresh token rotation (one-time use)
- CSRF protection
- Secure cookie settings (HttpOnly, Secure, SameSite)
- Constant-time password comparison

Include database schema, API endpoints, and tests.
```

### Prompt 52: Background Job System (Any Language)

```
Implement a background job processing system in [LANGUAGE]:

Features:
- Job queuing with priority levels
- Delayed/scheduled jobs
- Job retry with configurable backoff
- Dead letter queue for failed jobs
- Job lifecycle hooks (before, after, on_error)
- Concurrency control (max workers)
- Job uniqueness (prevent duplicate processing)
- Progress tracking
- Job cancellation
- Batch job support
- Cron-style recurring jobs
- Web UI for job monitoring

Backend: Redis for job queue
Use existing job processing libraries where appropriate for the language.
```

### Prompt 53: REST API Client SDK (Any Language)

```
Write a REST API client SDK in [LANGUAGE] for the following API:

Base URL: https://api.example.com/v1

Endpoints:
- POST /auth/token — Get access token
- GET /users — List users (paginated)
- GET /users/{id} — Get user by ID
- POST /users — Create user
- PUT /users/{id} — Update user
- DELETE /users/{id} — Delete user
- GET /users/{id}/orders — Get user orders

Features:
- Automatic authentication (token refresh)
- Pagination helpers (iterate all pages)
- Rate limit handling (automatic retry with Retry-After)
- Error handling with typed exceptions
- Request/response logging
- Timeout configuration
- Custom HTTP headers
- Webhook signature verification

Include:
- Client class with all methods
- Type definitions for all request/response models
- Configuration builder
- Usage examples
- Unit tests with mocked HTTP
```

### Prompt 54: Caching Layer (Any Language)

```
Implement a multi-level caching layer in [LANGUAGE]:

Levels:
1. L1: In-memory cache (per-instance, fast, limited size)
2. L2: Distributed cache (Redis, shared across instances)
3. L3: Database (source of truth)

Features:
- Cache-aside pattern (read: check L1->L2->L3, populate on miss)
- Write-through pattern (write: update L3, invalidate L1 and L2)
- TTL support per key and per level
- Cache stampede prevention (single-flight / distributed locks)
- Cache warming on startup
- Cache statistics (hit rate, miss rate, eviction count)
- Tag-based invalidation (invalidate all keys with a tag)
- Serialization (JSON, MessagePack, or protocol-specific)
- Generic typed interface: Cache<T>.get(key) -> T?

Include:
- Cache interface/trait
- In-memory implementation (LRU)
- Redis implementation
- Multi-level composite cache
- Tests for each level and the composite
```

### Prompt 55: Health Check System (Any Language)

```
Implement a comprehensive health check system in [LANGUAGE]:

Health checks:
1. Database connectivity (PostgreSQL)
2. Redis connectivity
3. External API availability
4. Disk space
5. Memory usage
6. CPU usage
7. Message queue connectivity
8. DNS resolution
9. TLS certificate expiry
10. Custom business logic checks

Features:
- Health check endpoint: GET /health (summary) and GET /health/details
- Individual check timeout
- Parallel check execution
- Degraded state (some checks failing but service is operational)
- History tracking (last N check results)
- Configurable check intervals
- Kubernetes-compatible responses (liveness vs readiness)
- Prometheus metrics export

Response format:
{
  "status": "healthy|degraded|unhealthy",
  "timestamp": "ISO-8601",
  "checks": {
    "database": { "status": "healthy", "latency_ms": 5, "details": {} },
    "redis": { "status": "healthy", "latency_ms": 2, "details": {} },
    ...
  }
}
```

---

## Usage Tips

1. **Replace placeholders** like [LANGUAGE], [DATABASE], [RESOURCE_NAME] with your specific technology choices.

2. **Combine prompts**: Use these as building blocks. For example, combine Prompt 1 (FastAPI CRUD) + Prompt 8 (Testing) + Prompt 10 (Query Builder) for a complete module.

3. **Iterate**: These prompts produce good first drafts. Always review and refine the output to match your project's specific needs.

4. **Add context**: Include relevant code from your project (types, interfaces, existing patterns) when using these prompts for the best results.

5. **Version specificity**: Always specify the exact version of languages and frameworks you are using to avoid deprecated patterns.
