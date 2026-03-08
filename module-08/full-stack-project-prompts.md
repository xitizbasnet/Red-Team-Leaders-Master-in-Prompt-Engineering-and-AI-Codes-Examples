# Full-Stack Project Prompts: Build TaskFlow from Scratch

## Module 08: AI for Software Development and Security

> Complete set of prompts to build a full-stack task management application from requirements to deployment, using AI at every stage.

---

## Project Overview

**Application**: TaskFlow -- A team task management application
**Tech Stack**: Python (FastAPI) + React (TypeScript) + PostgreSQL + Redis + Docker
**Architecture**: Monolithic API + SPA frontend

This document provides the exact prompts to use at each stage. Execute them in order, feeding the output of each phase as context into the next.

---

## Phase 1: Requirements and Planning

### Prompt 1.1: User Stories

```
I am building a team task management application called "TaskFlow."
It allows teams to organize work into projects and tasks.

Generate comprehensive user stories organized by epic:

Epics:
1. User Management — Registration, login, profile management
2. Project Management — Create, manage, and collaborate on projects
3. Task Management — Create, assign, track, and complete tasks
4. Comments and Activity — Communicate on tasks, view activity history
5. Dashboard and Reporting — Overview of work, status, and metrics

Roles: Admin (system-wide), Project Admin, Project Manager, Team Member, Guest (read-only)

For each user story provide:
- Story ID (e.g., US-001)
- As a [role], I want to [action], so that [benefit]
- Acceptance criteria (3-5 checkable items)
- Priority: P0 (must have for MVP), P1 (should have), P2 (nice to have)

Generate at least 30 user stories. Mark which ones are in the MVP scope.
```

### Prompt 1.2: Technical Requirements

```
Based on these user stories for TaskFlow (a team task management app):

[PASTE USER STORIES FROM PROMPT 1.1]

Generate detailed technical requirements:

1. **API Endpoints** — Complete list with method, path, description, auth requirement
2. **Data Model** — All entities with attributes, types, and relationships
3. **Authentication/Authorization** — JWT-based auth with role-based access control
4. **Non-Functional Requirements**:
   - Performance: API response times < 200ms for reads, < 500ms for writes
   - Security: OWASP Top 10 compliance
   - Scale: Support 1000 concurrent users
   - Data: PostgreSQL with proper indexing
5. **UI Pages** — List of pages with key components
6. **MVP Scope** — Clearly mark what is in MVP vs later phases

Format as a structured requirements document.
```

---

## Phase 2: Architecture and Design

### Prompt 2.1: System Architecture

```
Design the system architecture for TaskFlow based on these requirements:

[PASTE KEY REQUIREMENTS FROM PROMPT 1.2 — API endpoints, data model, NFRs]

Tech stack decisions (already made):
- Backend: Python 3.12 with FastAPI
- Database: PostgreSQL 16
- Cache: Redis 7
- Frontend: React 18 with TypeScript
- Deployment: Docker + Docker Compose

Please provide:

1. **Backend Project Structure**:
   ```
   backend/
   ├── src/
   │   ├── main.py
   │   ├── config.py
   │   ├── database.py
   │   ├── dependencies.py
   │   ├── auth/
   │   ├── users/
   │   ├── projects/
   │   ├── tasks/
   │   ├── comments/
   │   └── common/
   └── tests/
   ```
   Describe each file's responsibility.

2. **Frontend Project Structure**:
   ```
   frontend/
   ├── src/
   │   ├── api/
   │   ├── components/
   │   ├── hooks/
   │   ├── pages/
   │   ├── context/
   │   └── utils/
   ```
   Describe each directory's responsibility.

3. **Authentication Flow**: JWT access (30 min) + refresh (7 days) token flow
4. **API Response Format**: Standard envelope for all responses
5. **Error Handling Strategy**: Error codes, HTTP status mapping
6. **Caching Strategy**: What to cache in Redis, TTL, invalidation
7. **Database Connection**: Async SQLAlchemy with connection pooling

Include a data flow diagram for the key user journey: "User creates a task and assigns it to a team member."
```

### Prompt 2.2: Database Schema

```
Design the PostgreSQL database schema for TaskFlow.

Entities and their requirements:

1. **users**: Registration and authentication
   - id (UUID, PK), email (unique), password_hash, full_name
   - role (admin, user), avatar_url, is_active, last_login_at
   - created_at, updated_at

2. **projects**: Team workspaces
   - id (UUID, PK), name, description, slug (unique), status (active/archived)
   - owner_id (FK users), created_at, updated_at

3. **project_members**: Many-to-many with roles
   - id (UUID, PK), project_id (FK), user_id (FK), role (admin/manager/member/viewer)
   - joined_at

4. **tasks**: Work items
   - id (UUID, PK), project_id (FK), title, description (text)
   - status (todo/in_progress/in_review/done), priority (low/medium/high/critical)
   - assignee_id (FK users, nullable), creator_id (FK users)
   - due_date (nullable), estimated_hours (nullable), position (integer, for ordering)
   - created_at, updated_at

5. **comments**: Task discussions
   - id (UUID, PK), task_id (FK), user_id (FK), content (text)
   - created_at, updated_at

6. **activity_log**: Audit trail
   - id (UUID, PK), project_id (FK), task_id (FK nullable)
   - user_id (FK), action (enum), details (JSONB)
   - created_at

Generate:
1. Complete CREATE TABLE DDL with all constraints, indexes, and triggers
2. Unique constraint: (project_id, user_id) on project_members
3. Indexes for: tasks by project+status, tasks by assignee, activity by project
4. Auto-update trigger for updated_at columns
5. ENUM types for status, priority, and role fields
6. Alembic migration file (initial_schema)
7. SQLAlchemy 2.0 models (async, using mapped_column and Mapped types)
```

### Prompt 2.3: API Specification

```
Design the complete REST API specification for TaskFlow.

Use this response envelope:
{
  "data": { ... },
  "meta": { "timestamp": "...", "request_id": "..." }
}

Error envelope:
{
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "Human-readable message",
    "details": [{ "field": "email", "message": "Invalid email format" }]
  },
  "meta": { "timestamp": "...", "request_id": "..." }
}

Pagination:
{
  "data": [...],
  "pagination": { "total": 100, "page": 1, "page_size": 20, "pages": 5 },
  "meta": { ... }
}

Generate the complete API spec for these endpoint groups:

**Auth** (no auth required):
- POST /api/v1/auth/register
- POST /api/v1/auth/login
- POST /api/v1/auth/refresh
- POST /api/v1/auth/logout

**Users** (auth required):
- GET /api/v1/users/me
- PUT /api/v1/users/me
- GET /api/v1/users (admin only)

**Projects** (auth required):
- CRUD /api/v1/projects
- Member management: /api/v1/projects/{id}/members

**Tasks** (auth required, project member):
- CRUD /api/v1/projects/{project_id}/tasks
- Status update: PATCH /api/v1/tasks/{id}/status
- Assignment: PATCH /api/v1/tasks/{id}/assign

**Comments** (auth required, project member):
- CRUD /api/v1/tasks/{task_id}/comments

**Dashboard** (auth required):
- GET /api/v1/dashboard

For each endpoint provide:
- HTTP method and path
- Description
- Request body (if any) with field types and validation rules
- Response body with example
- Authorization rules
- Status codes
```

---

## Phase 3: Backend Implementation

### Prompt 3.1: Project Setup and Configuration

```
Generate the project setup files for the TaskFlow backend:

1. **pyproject.toml** using Poetry:
   Dependencies:
   - fastapi[standard], uvicorn[standard]
   - sqlalchemy[asyncio], asyncpg, alembic
   - pydantic[email], pydantic-settings
   - python-jose[cryptography], passlib[bcrypt]
   - redis (async support)
   - python-multipart, python-dateutil
   Dev dependencies:
   - pytest, pytest-asyncio, pytest-cov
   - httpx (for async test client)
   - factory-boy
   - ruff, mypy

2. **src/config.py** — Pydantic Settings:
   - DATABASE_URL (PostgreSQL async URL)
   - REDIS_URL
   - JWT_SECRET_KEY, JWT_ALGORITHM (RS256 or HS256)
   - JWT_ACCESS_TOKEN_EXPIRE_MINUTES (30)
   - JWT_REFRESH_TOKEN_EXPIRE_DAYS (7)
   - CORS_ORIGINS (list)
   - DEBUG (bool, default False)
   - APP_NAME, APP_VERSION

3. **src/database.py**:
   - Async engine creation
   - Async session factory
   - Base model class
   - get_session dependency

4. **src/main.py**:
   - FastAPI app creation with lifespan
   - CORS middleware
   - Request ID middleware
   - Global exception handlers (map domain errors to HTTP responses)
   - Include all routers
   - Health check endpoint: GET /api/v1/health

5. **src/common/exceptions.py**:
   - AppException base class
   - NotFoundError, ConflictError, ForbiddenError, ValidationError, AuthenticationError
   - Each with error code and HTTP status mapping

6. **src/common/schemas.py**:
   - ResponseEnvelope[T] generic model
   - PaginatedResponse[T] generic model
   - ErrorResponse model
   - PaginationParams (page, page_size with validation)

Generate all files with complete, runnable code.
```

### Prompt 3.2: Authentication Module

```
Implement the complete authentication module for TaskFlow.

Context: We are using FastAPI with async SQLAlchemy. Here are the relevant files:
[PASTE: config.py, database.py, common/exceptions.py, common/schemas.py from Prompt 3.1]

Generate:

1. **src/users/models.py**:
   - User SQLAlchemy model (all fields from the schema design)

2. **src/auth/utils.py**:
   - hash_password(password: str) -> str (bcrypt)
   - verify_password(plain: str, hashed: str) -> bool
   - create_access_token(user_id: str) -> str
   - create_refresh_token(user_id: str) -> str
   - decode_token(token: str) -> dict (with expiry validation)

3. **src/auth/schemas.py** (Pydantic v2):
   - RegisterRequest: email (EmailStr), password (min 8 chars), full_name (2-100)
   - LoginRequest: email, password
   - TokenResponse: access_token, refresh_token, token_type, expires_in
   - RefreshRequest: refresh_token
   - UserResponse: id, email, full_name, role, avatar_url, created_at (no password!)

4. **src/auth/service.py**:
   - register(db, request) -> TokenResponse
     - Check email uniqueness, hash password, create user, generate tokens
   - login(db, request) -> TokenResponse
     - Find user by email, verify password, update last_login, generate tokens
     - Same error message for wrong email or wrong password (prevent enumeration)
   - refresh(db, request) -> TokenResponse
     - Decode refresh token, verify user still active, generate new access token

5. **src/auth/router.py**:
   - POST /api/v1/auth/register — register
   - POST /api/v1/auth/login — login
   - POST /api/v1/auth/refresh — refresh
   - Include OpenAPI tags and descriptions

6. **src/dependencies.py**:
   - get_current_user(token, db) -> User dependency
     - Extract Bearer token from Authorization header
     - Decode JWT, find user by ID, verify active
     - Raise 401 if any step fails
   - require_admin(user) -> User dependency
     - Raise 403 if user.role != "admin"

Ensure passwords are NEVER included in any response.
```

### Prompt 3.3: Projects Module

```
Implement the Projects module for TaskFlow.

Context from previous implementation:
[PASTE: User model, auth dependencies, common schemas/exceptions]

Generate:

1. **src/projects/models.py**:
   - Project model
   - ProjectMember model (association table with role)

2. **src/projects/schemas.py**:
   - CreateProjectRequest: name (3-100), description (optional, max 2000)
   - UpdateProjectRequest: name (optional), description (optional), status (optional)
   - ProjectResponse: id, name, description, slug, status, owner, member_count, task_count, created_at
   - ProjectDetailResponse: includes members list
   - AddMemberRequest: user_id, role
   - ProjectMemberResponse: user_id, email, full_name, role, joined_at

3. **src/projects/repository.py**:
   - create(db, project_data, owner_id) -> Project
   - get_by_id(db, project_id) -> Project | None
   - list_for_user(db, user_id, pagination) -> tuple[list[Project], int]
   - update(db, project_id, update_data) -> Project
   - delete(db, project_id) -> None (soft delete by setting status=archived)
   - add_member(db, project_id, user_id, role) -> ProjectMember
   - remove_member(db, project_id, user_id) -> None
   - get_member_role(db, project_id, user_id) -> str | None
   - is_member(db, project_id, user_id) -> bool

4. **src/projects/service.py**:
   - create_project(db, request, current_user) -> ProjectResponse
     - Create project, add creator as admin member
     - Generate slug from name
   - get_project(db, project_id, current_user) -> ProjectDetailResponse
     - Must be a member to view (raise 403 otherwise)
   - list_projects(db, current_user, pagination) -> PaginatedResponse
     - Only return projects user is a member of
   - update_project(db, project_id, request, current_user) -> ProjectResponse
     - Only project admin can update
   - delete_project(db, project_id, current_user) -> None
     - Only project admin can delete
   - add_member(db, project_id, request, current_user) -> ProjectMemberResponse
     - Only admin/manager can add members
   - remove_member(db, project_id, user_id, current_user) -> None
     - Only admin can remove members
     - Cannot remove the last admin

5. **src/projects/router.py**:
   - All CRUD endpoints + member management
   - Use proper HTTP status codes
   - Include authorization checks via service layer

Include a `get_project_member_or_403` dependency for endpoints
that require project membership.
```

### Prompt 3.4: Tasks Module

```
Implement the Tasks module for TaskFlow.

Context from previous implementation:
[PASTE: Project model, ProjectMember model, dependencies, common schemas]

Generate:

1. **src/tasks/models.py**:
   - Task model with all fields from schema design
   - TaskStatus enum (todo, in_progress, in_review, done)
   - TaskPriority enum (low, medium, high, critical)

2. **src/tasks/schemas.py**:
   - CreateTaskRequest: title (3-200), description (optional), priority (default: medium),
     assignee_id (optional UUID), due_date (optional, must be future), estimated_hours (optional, positive)
   - UpdateTaskRequest: all fields optional
   - TaskResponse: all fields + assignee name, creator name
   - TaskListResponse: with pagination
   - TaskFilterParams: status (optional, list), priority (optional, list),
     assignee_id (optional), search (optional text search on title/description),
     due_before (optional date), due_after (optional date),
     sort_by (created_at/due_date/priority, default: created_at), sort_order (asc/desc)
   - UpdateStatusRequest: status (TaskStatus)
   - AssignTaskRequest: assignee_id (UUID, nullable to unassign)

3. **src/tasks/repository.py**:
   - create(db, task_data) -> Task
   - get_by_id(db, task_id) -> Task | None
   - list_for_project(db, project_id, filters, pagination) -> tuple[list[Task], int]
     - Apply all filter params dynamically
     - Support text search on title and description
   - update(db, task_id, update_data) -> Task
   - delete(db, task_id) -> None

4. **src/tasks/service.py**:
   - create_task(db, project_id, request, current_user)
     - Verify user is project member
     - If assignee provided, verify assignee is project member
     - Log activity: "task_created"
   - get_task(db, task_id, current_user)
     - Verify user is member of task's project
   - list_tasks(db, project_id, filters, pagination, current_user)
     - Verify project membership
   - update_task(db, task_id, request, current_user)
     - Log activity: "task_updated" with changed fields
   - update_status(db, task_id, request, current_user)
     - Log activity: "status_changed" with old and new status
   - assign_task(db, task_id, request, current_user)
     - Verify assignee is project member
     - Log activity: "task_assigned"
   - delete_task(db, task_id, current_user)
     - Only creator or project admin can delete

5. **src/tasks/router.py**:
   - POST /api/v1/projects/{project_id}/tasks
   - GET /api/v1/projects/{project_id}/tasks (with query filters)
   - GET /api/v1/tasks/{task_id}
   - PUT /api/v1/tasks/{task_id}
   - DELETE /api/v1/tasks/{task_id}
   - PATCH /api/v1/tasks/{task_id}/status
   - PATCH /api/v1/tasks/{task_id}/assign
```

### Prompt 3.5: Comments, Activity, and Dashboard

```
Implement the remaining backend modules for TaskFlow:

Context:
[PASTE: relevant models, schemas, dependencies from previous prompts]

**Comments Module:**
1. Comment model, schemas, repository, service, router
2. POST /api/v1/tasks/{task_id}/comments — add comment (project member)
3. GET /api/v1/tasks/{task_id}/comments — list comments with pagination
4. PUT /api/v1/comments/{id} — edit comment (author only)
5. DELETE /api/v1/comments/{id} — delete comment (author or project admin)
6. Log activity on comment creation

**Activity Log:**
1. ActivityLog model (already defined in schema)
2. Activity logging utility function:
   log_activity(db, project_id, task_id, user_id, action, details)
3. GET /api/v1/projects/{project_id}/activity — list activity with pagination
4. Activity types: task_created, task_updated, task_assigned, status_changed,
   comment_added, member_added, member_removed

**Dashboard Endpoint:**
GET /api/v1/dashboard returns for the current user:
{
  "total_projects": number,
  "total_tasks": number,
  "tasks_by_status": { "todo": n, "in_progress": n, "in_review": n, "done": n },
  "tasks_by_priority": { "low": n, "medium": n, "high": n, "critical": n },
  "my_tasks": { "assigned_to_me": n, "created_by_me": n, "overdue": n },
  "recent_activity": [ last 20 activity entries across all user's projects ]
}
- Use aggregate queries (not Python-level counting)
- Only count tasks/projects the user has access to

Generate all code, complete and runnable.
```

---

## Phase 4: Frontend Implementation

### Prompt 4.1: Frontend Setup

```
Generate the complete frontend setup for TaskFlow:

Requirements:
- React 18 + TypeScript + Vite
- TailwindCSS for styling
- React Router v6 for routing
- Axios for API calls

Generate these files:

1. **package.json** with all dependencies
2. **vite.config.ts** with proxy to backend (localhost:8000)
3. **tailwind.config.js**
4. **tsconfig.json** (strict mode)
5. **src/main.tsx** — React entry point
6. **src/App.tsx** — Router setup
7. **src/api/client.ts** — Axios instance with:
   - Base URL from environment
   - Request interceptor to add JWT token from localStorage
   - Response interceptor to handle 401 (auto-refresh, then retry)
   - Response interceptor to unwrap { data: ... } envelope
8. **src/api/types.ts** — TypeScript interfaces for all API responses:
   - User, Project, Task, Comment, ActivityEntry, DashboardStats
   - PaginatedResponse<T>, ErrorResponse
9. **src/api/auth.ts** — login, register, refresh, logout functions
10. **src/api/projects.ts** — CRUD functions for projects
11. **src/api/tasks.ts** — CRUD functions for tasks + status/assign
12. **src/context/AuthContext.tsx** — Auth provider with:
    - user state, login, register, logout functions
    - Auto-load user from stored token on mount
    - Token refresh logic
13. **src/router.tsx** — Route definitions with protected route wrapper:
    - /login, /register — public
    - /dashboard, /projects, /projects/:id, /tasks/:id — protected
```

### Prompt 4.2: Layout and Auth Components

```
Generate the layout and authentication components for TaskFlow:

Context:
[PASTE: AuthContext, API types, router configuration from Prompt 4.1]

Generate:

1. **src/components/Layout/AppLayout.tsx**:
   - Left sidebar: Logo, navigation links (Dashboard, Projects), user info at bottom
   - Top bar: Page title, search input (placeholder for now), user avatar with dropdown
   - Main content area (children)
   - Responsive: sidebar collapses to hamburger menu on mobile (< 768px)
   - Use TailwindCSS, clean professional design
   - Dark sidebar (#1e293b), white content area

2. **src/components/Layout/Sidebar.tsx** — Navigation sidebar component
3. **src/components/Layout/TopBar.tsx** — Top navigation bar

4. **src/components/Auth/LoginForm.tsx**:
   - Email input, password input, submit button
   - Client-side validation (email format, password not empty)
   - Loading state on submit (button shows spinner)
   - Error message display (red text below form)
   - "Do not have an account? Register" link
   - Centered on page with card layout

5. **src/components/Auth/RegisterForm.tsx**:
   - Email, password, confirm password, full name inputs
   - Password strength indicator (weak/medium/strong based on rules)
   - Client-side validation
   - "Already have an account? Login" link

6. **src/pages/LoginPage.tsx** — Full page with LoginForm
7. **src/pages/RegisterPage.tsx** — Full page with RegisterForm

8. **src/components/Common/Button.tsx** — Reusable button:
   - Variants: primary (blue), secondary (gray), danger (red), ghost (transparent)
   - Sizes: sm, md, lg
   - Loading state (shows spinner, disabled)
   - Full TypeScript props

9. **src/components/Common/Modal.tsx** — Reusable modal:
   - Overlay background
   - Close on escape key and backdrop click
   - Title, body (children), footer (actions)
   - Transition animation

10. **src/components/Common/LoadingSpinner.tsx** — Simple spinner

All components must use TailwindCSS and be fully typed with TypeScript.
```

### Prompt 4.3: Core Feature Pages

```
Generate the core feature pages and components for TaskFlow:

Context:
[PASTE: API functions, types, AuthContext, AppLayout, Common components]

Generate:

1. **src/pages/DashboardPage.tsx**:
   - 4 stat cards in a row: Total Projects, Total Tasks, My Tasks, Overdue
   - Tasks by status breakdown (horizontal stacked bar using CSS)
   - Recent activity feed (list of activity entries with user, action, time)
   - Loading skeleton while data fetches

2. **src/pages/ProjectsPage.tsx**:
   - Header: "Projects" title + "New Project" button
   - Grid of project cards (2-3 columns)
   - Each card: project name, description (truncated), member count, task count
   - Empty state: illustration text + create button
   - Click card -> navigate to project detail

3. **src/components/Projects/CreateProjectModal.tsx**:
   - Modal with form: name, description
   - Submit creates project and navigates to it

4. **src/pages/ProjectDetailPage.tsx**:
   - Project header: name, description, settings button
   - Tab navigation: Tasks (default), Members, Activity
   - Tasks tab: TaskBoard component
   - Members tab: member list with roles, add/remove
   - Activity tab: activity log list

5. **src/components/Tasks/TaskBoard.tsx**:
   - Kanban board with 4 columns: Todo, In Progress, In Review, Done
   - Each column shows count of tasks
   - Task cards in each column
   - "Add Task" button at top of Todo column
   - Basic drag and drop (HTML5 DnD API) to move between columns

6. **src/components/Tasks/TaskCard.tsx**:
   - Title
   - Priority badge (color-coded: green/yellow/orange/red)
   - Assignee avatar (or "Unassigned" text)
   - Due date (red if overdue)
   - Click opens task detail modal or page

7. **src/components/Tasks/CreateTaskModal.tsx**:
   - Form: title, description (textarea), priority (dropdown), assignee (dropdown of members), due date
   - Submit creates task and refreshes board

8. **src/pages/TaskDetailPage.tsx** (or Modal):
   - Task title (editable), description (editable)
   - Status dropdown, priority dropdown, assignee dropdown
   - Due date picker
   - Comments section below:
     - List of comments with user name, time, content
     - Add comment form (textarea + submit button)
   - Activity sidebar or section

All pages should handle: loading, error, and empty states.
Include proper React hooks for data fetching (useEffect + useState pattern).
```

---

## Phase 5: Testing

### Prompt 5.1: Backend Test Suite

```
Generate a comprehensive backend test suite for TaskFlow:

Context:
[PASTE: all backend code — models, schemas, services, routers]

Generate:

1. **tests/conftest.py**:
   - Async test database (SQLite for speed)
   - AsyncClient fixture using httpx
   - User factory (create_user helper with hashed password)
   - Project factory (create_project helper)
   - Task factory (create_task helper)
   - Auth helper: get_auth_headers(user) returns {"Authorization": "Bearer <token>"}
   - Database cleanup between tests (rollback transaction)

2. **tests/test_auth.py** (12+ tests):
   - Register with valid data -> 201 + tokens
   - Register with duplicate email -> 409
   - Register with invalid email -> 422
   - Register with short password -> 422
   - Login with valid credentials -> 200 + tokens
   - Login with wrong password -> 401 (generic message)
   - Login with non-existent email -> 401 (same generic message!)
   - Access protected endpoint with valid token -> 200
   - Access protected endpoint without token -> 401
   - Access protected endpoint with expired token -> 401
   - Refresh token flow -> new access token
   - Response never contains password hash

3. **tests/test_projects.py** (12+ tests):
   - Create project -> 201
   - List projects (only user's projects) -> 200
   - Get project detail (as member) -> 200
   - Get project detail (non-member) -> 403
   - Update project (as admin) -> 200
   - Update project (as member, not admin) -> 403
   - Delete project (as admin) -> 204
   - Add member -> 201
   - Remove member -> 204
   - Cannot remove last admin -> 400
   - Project slug is unique -> 409
   - Pagination works correctly

4. **tests/test_tasks.py** (12+ tests):
   - Create task -> 201
   - List tasks with filters -> 200 (test each filter)
   - Update task status -> 200
   - Assign task to member -> 200
   - Assign task to non-member -> 400
   - Delete task (as creator) -> 204
   - Non-member cannot see project tasks -> 403
   - Overdue tasks appear in correct queries
   - Pagination and sorting work correctly
   - Activity log entries created on task changes

5. **tests/test_dashboard.py** (5 tests):
   - Returns correct counts
   - Only includes user's projects/tasks
   - Handles user with no projects
   - Recent activity is ordered correctly
   - Overdue count is accurate

Use pytest-asyncio with proper async fixtures.
Every test should verify both status code AND response body content.
```

---

## Phase 6: Docker and Deployment

### Prompt 6.1: Complete Docker Setup

```
Generate the complete Docker configuration for TaskFlow:

1. **backend/Dockerfile** (production):
   - Multi-stage: builder (install deps) + runtime (copy app)
   - Python 3.12 slim
   - Non-root user
   - Health check: curl localhost:8000/api/v1/health
   - Expose 8000

2. **frontend/Dockerfile** (production):
   - Multi-stage: deps, build (Vite), runtime (nginx)
   - Node 20 Alpine for build
   - Nginx Alpine for runtime
   - Custom nginx.conf with SPA routing, gzip, security headers
   - Health check
   - Expose 80

3. **docker-compose.yml** (development):
   - backend: build from ./backend, port 8000, volume mount for hot reload,
     depends on db and redis
   - frontend: build from ./frontend, port 3000, volume mount, Vite dev server
   - db: postgres:16-alpine, port 5432, named volume, health check
   - redis: redis:7-alpine, port 6379
   - init: one-off container that runs migrations and seeds test data
   - All services on one network

4. **docker-compose.prod.yml** (production):
   - backend: production Dockerfile
   - frontend: production Dockerfile with nginx
   - db: with backups directory volume
   - redis: with persistence
   - nginx: reverse proxy in front of backend and frontend

5. **backend/.dockerignore** and **frontend/.dockerignore**

6. **.env.example** with all required variables:
   - DATABASE_URL, REDIS_URL, JWT_SECRET_KEY
   - Frontend: VITE_API_URL

7. **Makefile** with commands:
   - make up — docker compose up -d
   - make down — docker compose down
   - make logs — docker compose logs -f
   - make migrate — run alembic upgrade head
   - make seed — seed test data
   - make test — run backend tests in container
   - make shell — open shell in backend container
   - make build — build production images
```

---

## Phase 7: Security Review

### Prompt 7.1: Security Audit

```
Perform a security review of the entire TaskFlow application:

Backend code:
[PASTE: all backend Python code]

Check for the OWASP Top 10:

1. **A01 Broken Access Control**: Can users access other users' projects/tasks by guessing IDs?
2. **A02 Cryptographic Failures**: Is password hashing strong? Are JWTs secure?
3. **A03 Injection**: Any SQL injection risks? XSS in stored comments?
4. **A04 Insecure Design**: Any business logic bypasses?
5. **A05 Security Misconfiguration**: Debug mode, CORS, error exposure?
6. **A06 Vulnerable Components**: Any known dependency vulnerabilities?
7. **A07 Authentication Failures**: Account enumeration? Brute force protection?
8. **A08 Integrity Failures**: JWT tampering? Unsigned tokens?
9. **A09 Logging Failures**: Are security events logged?
10. **A10 SSRF**: Any URL fetching from user input?

For each finding:
- Location (file:line)
- Severity (Critical/High/Medium/Low)
- Current code
- Fixed code
- Test to verify the fix

Generate a security hardening middleware file (rate limiting, security headers,
request validation) and show how to add it to main.py.
```

---

## Phase 8: Documentation

### Prompt 8.1: Project Documentation

```
Generate documentation for TaskFlow:

Based on the entire codebase we have built:
[SUMMARIZE: tech stack, architecture, API endpoints, features]

Generate:

1. **README.md** — Project overview, features, quick start (3 commands to run),
   tech stack, development setup, testing, deployment, contributing

2. **API_DOCS.md** — Complete API documentation with:
   - Authentication guide (register, login, use token)
   - Endpoint reference (organized by resource)
   - Request/response examples (curl)
   - Error codes reference
   - Pagination guide
   - Rate limiting details

3. **ARCHITECTURE.md** — Architecture overview:
   - System diagram (text description)
   - Backend module structure
   - Frontend component structure
   - Database schema overview
   - Authentication flow
   - Key design decisions

Make the README practical and focused on getting developers up and running quickly.
```

---

## Execution Checklist

Use this checklist to track your progress:

- [ ] Phase 1: Requirements (Prompts 1.1-1.2)
- [ ] Phase 2: Architecture (Prompts 2.1-2.3)
- [ ] Phase 3: Backend (Prompts 3.1-3.5)
  - [ ] Project setup and configuration
  - [ ] Authentication module
  - [ ] Projects module
  - [ ] Tasks module
  - [ ] Comments, activity, dashboard
- [ ] Phase 4: Frontend (Prompts 4.1-4.3)
  - [ ] Frontend setup
  - [ ] Layout and auth components
  - [ ] Core feature pages
- [ ] Phase 5: Testing (Prompt 5.1)
- [ ] Phase 6: Docker (Prompt 6.1)
- [ ] Phase 7: Security (Prompt 7.1)
- [ ] Phase 8: Documentation (Prompt 8.1)

### Tips for Success

1. **Review each output before moving on**: AI-generated code needs human review. Fix issues before building on top of them.

2. **Feed context forward**: Each prompt says "[PASTE: relevant output from previous prompt]". This is critical for consistency.

3. **Ask for fixes**: If AI generates code with issues, show it the error and ask for a fix rather than trying to fix it manually.

4. **Iterate on quality**: After generating the initial code, ask AI to review it for improvements, edge cases, and best practices.

5. **Test as you go**: Do not wait until Phase 5 to test. Run the tests after each module is implemented to catch issues early.
