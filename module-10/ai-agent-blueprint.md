# AI Agent Blueprint

## Code and Examples — Module 10

A comprehensive blueprint for designing and building AI agents, including architecture patterns, component specifications, and implementation guidance.

---

## Table of Contents

1. [Agent Design Philosophy](#1-agent-design-philosophy)
2. [Architecture Patterns](#2-architecture-patterns)
3. [Core Components](#3-core-components)
4. [Tool System Design](#4-tool-system-design)
5. [Memory Architecture](#5-memory-architecture)
6. [Safety and Guardrails](#6-safety-and-guardrails)
7. [Implementation Template](#7-implementation-template)
8. [Multi-Agent Systems](#8-multi-agent-systems)
9. [Evaluation Framework](#9-evaluation-framework)
10. [Production Deployment Checklist](#10-production-deployment-checklist)

---

## 1. Agent Design Philosophy

### Core Principles

```
1. PURPOSE-DRIVEN: Every agent must have a clearly defined purpose and scope.
   An agent that tries to do everything does nothing well.

2. MINIMAL AUTHORITY: Grant the least privileges necessary. An agent should
   only have access to the tools and data it needs for its specific task.

3. FAIL GRACEFULLY: Agents will encounter errors, unexpected inputs, and edge
   cases. Design for failure from the start.

4. HUMAN IN THE LOOP: For any consequential action, provide mechanisms for
   human review and override.

5. OBSERVABLE: Every thought, action, and decision should be logged and
   traceable. You cannot fix what you cannot see.

6. ITERATIVE DESIGN: Start simple, measure, and add complexity only when
   needed. A simple agent that works reliably beats a complex one that fails.
```

### Agent Design Checklist

Before building any agent, answer these questions:

```
[ ] What specific problem does this agent solve?
[ ] Who are the users and what are their expectations?
[ ] What are the inputs and expected outputs?
[ ] What tools does the agent need access to?
[ ] What data does the agent need?
[ ] What are the boundaries (what should the agent NOT do)?
[ ] What happens when the agent fails?
[ ] How will you measure success?
[ ] What are the safety requirements?
[ ] Is human oversight needed? At what points?
```

---

## 2. Architecture Patterns

### Pattern A: Simple ReAct Loop

Best for: General-purpose tasks, exploratory work, single-turn complex queries.

```
                    ┌─────────────────┐
                    │   USER INPUT    │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
              ┌────►│    REASON       │
              │     │  (Think about   │
              │     │   next step)    │
              │     └────────┬────────┘
              │              │
              │     ┌────────▼────────┐
              │     │     ACT         │
              │     │  (Execute tool  │
              │     │   or respond)   │
              │     └────────┬────────┘
              │              │
              │     ┌────────▼────────┐
              │     │   OBSERVE       │
              │     │  (Process tool  │
              │     │   result)       │
              │     └────────┬────────┘
              │              │
              │     ┌────────▼────────┐
              │     │  GOAL MET?      │
              │     └───┬────────┬────┘
              │     No  │        │ Yes
              └─────────┘        │
                        ┌────────▼────────┐
                        │  FINAL RESPONSE │
                        └─────────────────┘
```

### Pattern B: Plan-and-Execute

Best for: Complex multi-step tasks, tasks with clear subtask decomposition.

```
                    ┌─────────────────┐
                    │   USER INPUT    │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │    PLANNER      │
                    │  Decompose into │
                    │   subtasks      │
                    └────────┬────────┘
                             │
              ┌──────────────▼──────────────┐
              │         TASK QUEUE          │
              │  [Task 1] [Task 2] [Task 3] │
              └──────────────┬──────────────┘
                             │
                    ┌────────▼────────┐
              ┌────►│   EXECUTOR      │
              │     │  Execute next   │
              │     │  task in queue   │
              │     └────────┬────────┘
              │              │
              │     ┌────────▼────────┐
              │     │   RE-PLANNER    │
              │     │  Review result, │
              │     │  adjust plan    │
              │     └───┬────────┬────┘
              │   More  │        │ Done
              │   tasks │        │
              └─────────┘        │
                        ┌────────▼────────┐
                        │   SYNTHESIZER   │
                        │  Combine all    │
                        │  results        │
                        └────────┬────────┘
                                 │
                        ┌────────▼────────┐
                        │  FINAL RESPONSE │
                        └─────────────────┘
```

### Pattern C: Reflexion (Self-Improving)

Best for: Quality-critical tasks, creative work, tasks with clear success criteria.

```
                    ┌─────────────────┐
                    │   USER INPUT    │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │    ATTEMPT      │
                    │  Generate       │
                    │  initial output │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │    EVALUATE     │
                    │  Score against  │
                    │  criteria       │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  QUALITY OK?    │
                    └───┬────────┬────┘
                    No  │        │ Yes
                        │        │
               ┌────────▼───┐    │
               │  REFLECT   │    │
               │ What went  │    │
               │ wrong and  │    │
               │ how to fix │    │
               └────────┬───┘    │
                        │        │
               ┌────────▼───┐    │
               │  RETRY     │    │
               │ Improved   │    │
               │ attempt    │────┘
               └────────────┘
                        │
               ┌────────▼────────┐
               │  FINAL RESPONSE │
               └─────────────────┘
```

### Pattern D: Supervisor Multi-Agent

Best for: Large, complex tasks that benefit from specialization.

```
                    ┌─────────────────┐
                    │   USER INPUT    │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │   SUPERVISOR    │
                    │  Analyze task,  │
                    │  delegate work  │
                    └────────┬────────┘
                             │
              ┌──────────────┼──────────────┐
              │              │              │
     ┌────────▼───┐  ┌──────▼─────┐  ┌────▼────────┐
     │  AGENT A   │  │  AGENT B   │  │  AGENT C    │
     │ (Research) │  │ (Analysis) │  │ (Writing)   │
     └────────┬───┘  └──────┬─────┘  └────┬────────┘
              │              │              │
              └──────────────┼──────────────┘
                             │
                    ┌────────▼────────┐
                    │   SUPERVISOR    │
                    │  Review, merge, │
                    │  quality check  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  FINAL RESPONSE │
                    └─────────────────┘
```

---

## 3. Core Components

### 3.1 System Prompt Template

```python
AGENT_SYSTEM_PROMPT = """
You are {agent_name}, an AI agent designed to {primary_purpose}.

## Your Capabilities
You have access to the following tools:
{tool_descriptions}

## Your Process
1. Analyze the user's request carefully
2. Break complex tasks into smaller steps
3. Use tools when you need external information or actions
4. Verify your results before presenting them
5. Ask for clarification if the request is ambiguous

## Your Boundaries
- You MUST NOT {restriction_1}
- You MUST NOT {restriction_2}
- You MUST NOT {restriction_3}
- If asked to do something outside your scope, politely explain
  your limitations

## Your Communication Style
- Be {tone_adjective_1}, {tone_adjective_2}, and {tone_adjective_3}
- {additional_communication_guidelines}

## Error Handling
- If a tool fails, try an alternative approach
- If you cannot complete a task, explain what you accomplished
  and what remains
- Never guess or fabricate information

## Current Context
Date: {current_date}
User: {user_context}
Session: {session_context}
"""
```

### 3.2 Agent State Management

```python
from dataclasses import dataclass, field
from typing import List, Dict, Optional
from enum import Enum
import time


class AgentStatus(Enum):
    IDLE = "idle"
    THINKING = "thinking"
    ACTING = "acting"
    WAITING = "waiting_for_input"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass
class AgentState:
    """Tracks the complete state of an agent execution."""

    # Identity
    agent_id: str
    agent_name: str

    # Current status
    status: AgentStatus = AgentStatus.IDLE
    current_step: int = 0
    max_steps: int = 20

    # Task tracking
    original_task: str = ""
    current_subtask: str = ""
    plan: List[str] = field(default_factory=list)

    # Message history
    messages: List[Dict] = field(default_factory=list)

    # Tool usage tracking
    tool_calls: List[Dict] = field(default_factory=list)
    total_tool_calls: int = 0

    # Token and cost tracking
    total_input_tokens: int = 0
    total_output_tokens: int = 0
    estimated_cost: float = 0.0

    # Timing
    start_time: Optional[float] = None
    end_time: Optional[float] = None

    # Results
    final_result: Optional[str] = None
    error: Optional[str] = None

    # Memory references
    memories_retrieved: List[Dict] = field(default_factory=list)
    memories_stored: List[Dict] = field(default_factory=list)

    def elapsed_time(self) -> float:
        if self.start_time is None:
            return 0.0
        end = self.end_time or time.time()
        return end - self.start_time

    def is_within_limits(self) -> bool:
        return (self.current_step < self.max_steps and
                self.estimated_cost < 1.0)  # $1 cost cap example
```

---

## 4. Tool System Design

### 4.1 Tool Definition Schema

```python
TOOL_SCHEMA = {
    "name": "string — unique tool identifier",
    "description": "string — when and why to use this tool",
    "parameters": {
        "type": "object",
        "properties": {
            "param_name": {
                "type": "string | number | boolean | array | object",
                "description": "what this parameter does",
                "required": True,  # or False
                "default": "optional default value",
                "enum": ["optional", "list", "of", "valid", "values"]
            }
        }
    },
    "returns": "description of what the tool returns",
    "errors": ["list of possible error conditions"],
    "rate_limit": "e.g., 10 calls per minute",
    "cost": "e.g., $0.01 per call",
    "safety_level": "safe | review_required | dangerous"
}
```

### 4.2 Example Tool Definitions

```python
tools = [
    {
        "name": "search_knowledge_base",
        "description": (
            "Search the internal knowledge base for information. Use this "
            "when you need to find specific information from our documents, "
            "policies, or previous conversations. Returns the most relevant "
            "passages with source references."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Natural language search query"
                },
                "filters": {
                    "type": "object",
                    "description": "Optional filters",
                    "properties": {
                        "document_type": {
                            "type": "string",
                            "enum": ["policy", "procedure", "faq", "all"]
                        },
                        "date_range": {
                            "type": "string",
                            "description": "e.g., 'last_30_days', 'last_year'"
                        }
                    }
                },
                "top_k": {
                    "type": "integer",
                    "description": "Number of results to return (1-10)",
                    "default": 5
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "send_email",
        "description": (
            "Send an email to a specified recipient. IMPORTANT: Only use "
            "this tool after confirming with the user that the email "
            "content and recipient are correct. This action cannot be undone."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "to": {
                    "type": "string",
                    "description": "Recipient email address"
                },
                "subject": {
                    "type": "string",
                    "description": "Email subject line"
                },
                "body": {
                    "type": "string",
                    "description": "Email body (supports markdown)"
                },
                "cc": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "CC recipients (optional)"
                }
            },
            "required": ["to", "subject", "body"]
        }
    },
    {
        "name": "create_calendar_event",
        "description": (
            "Create a calendar event. Use this when the user wants to "
            "schedule a meeting or appointment. Confirm details with "
            "the user before creating."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "title": {
                    "type": "string",
                    "description": "Event title"
                },
                "start_time": {
                    "type": "string",
                    "description": "Start time in ISO 8601 format"
                },
                "end_time": {
                    "type": "string",
                    "description": "End time in ISO 8601 format"
                },
                "attendees": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Email addresses of attendees"
                },
                "description": {
                    "type": "string",
                    "description": "Event description (optional)"
                }
            },
            "required": ["title", "start_time", "end_time"]
        }
    },
    {
        "name": "execute_sql_query",
        "description": (
            "Execute a read-only SQL query against the analytics database. "
            "Only SELECT queries are allowed. Use this for data retrieval "
            "and analysis. Never execute INSERT, UPDATE, DELETE, or DDL."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "SQL SELECT query"
                },
                "limit": {
                    "type": "integer",
                    "description": "Maximum rows to return",
                    "default": 100
                }
            },
            "required": ["query"]
        }
    }
]
```

### 4.3 Tool Safety Classification

```
SAFE TOOLS (no confirmation needed):
├── search_knowledge_base
├── get_weather
├── calculate
├── get_current_time
└── read_file

REVIEW-REQUIRED TOOLS (confirm with user before executing):
├── send_email
├── create_calendar_event
├── update_record
├── create_ticket
└── post_to_slack

DANGEROUS TOOLS (require explicit authorization + logging):
├── delete_record
├── modify_permissions
├── execute_code
├── external_api_call
└── transfer_funds
```

---

## 5. Memory Architecture

### 5.1 Memory System Design

```
┌─────────────────────────────────────────────┐
│              MEMORY SYSTEM                   │
│                                              │
│  ┌──────────────────────────────────────┐   │
│  │       SHORT-TERM MEMORY              │   │
│  │  (Current conversation context)      │   │
│  │  • Last N messages                   │   │
│  │  • Current task state                │   │
│  │  • Active tool results               │   │
│  │  Storage: In-context (message list)  │   │
│  │  Capacity: Context window limit      │   │
│  └──────────────────────────────────────┘   │
│                                              │
│  ┌──────────────────────────────────────┐   │
│  │       WORKING MEMORY                 │   │
│  │  (Scratchpad for current task)       │   │
│  │  • Notes and intermediate results    │   │
│  │  • Current plan and progress         │   │
│  │  • Hypotheses being tested           │   │
│  │  Storage: Structured state object    │   │
│  │  Capacity: Per-task, cleared after   │   │
│  └──────────────────────────────────────┘   │
│                                              │
│  ┌──────────────────────────────────────┐   │
│  │       LONG-TERM MEMORY               │   │
│  │  (Persistent knowledge)              │   │
│  │  • User preferences and context      │   │
│  │  • Learned facts and relationships   │   │
│  │  • Domain knowledge additions        │   │
│  │  Storage: Vector database            │   │
│  │  Capacity: Unlimited, relevance-     │   │
│  │            ranked retrieval           │   │
│  └──────────────────────────────────────┘   │
│                                              │
│  ┌──────────────────────────────────────┐   │
│  │       EPISODIC MEMORY                │   │
│  │  (Past experiences)                  │   │
│  │  • Successful task completions       │   │
│  │  • Failed attempts and lessons       │   │
│  │  • User feedback on past outputs     │   │
│  │  Storage: Structured database        │   │
│  │  Capacity: Pruned by relevance       │   │
│  │            and recency               │   │
│  └──────────────────────────────────────┘   │
│                                              │
└─────────────────────────────────────────────┘
```

### 5.2 Memory Operations

```python
class MemoryManager:
    """Manages all memory types for an agent."""

    def store(self, content: str, memory_type: str,
              metadata: dict) -> str:
        """Store a memory and return its ID."""
        pass

    def recall(self, query: str, memory_type: str = "all",
               top_k: int = 5) -> List[dict]:
        """Retrieve relevant memories."""
        pass

    def summarize_and_compress(self, memories: List[dict]) -> str:
        """Compress old memories into summaries."""
        pass

    def forget(self, memory_id: str) -> bool:
        """Remove a specific memory (e.g., for privacy)."""
        pass

    def build_context(self, current_query: str) -> str:
        """Build the optimal context for the current query."""
        # 1. Get relevant long-term memories
        # 2. Get relevant episodic memories
        # 3. Combine with short-term context
        # 4. Prioritize by relevance and recency
        # 5. Fit within token budget
        pass
```

---

## 6. Safety and Guardrails

### 6.1 Input Validation

```python
class InputValidator:
    """Validates all inputs to the agent."""

    BLOCKED_PATTERNS = [
        r"ignore previous instructions",
        r"forget your rules",
        r"pretend you are",
        r"you are now",
        r"system prompt",
        r"reveal your instructions",
    ]

    MAX_INPUT_LENGTH = 10000  # characters

    def validate(self, user_input: str) -> tuple:
        """
        Returns (is_valid: bool, reason: str)
        """
        # Check length
        if len(user_input) > self.MAX_INPUT_LENGTH:
            return False, "Input exceeds maximum length"

        # Check for prompt injection patterns
        for pattern in self.BLOCKED_PATTERNS:
            if re.search(pattern, user_input, re.IGNORECASE):
                return False, "Input contains blocked pattern"

        # Check for sensitive data (basic patterns)
        if self._contains_sensitive_data(user_input):
            return True, "WARNING: Input may contain sensitive data"

        return True, "Valid"
```

### 6.2 Output Guardrails

```python
class OutputGuardrails:
    """Validates all outputs from the agent."""

    def check_output(self, output: str, context: dict) -> dict:
        return {
            "safe": self._is_safe(output),
            "on_topic": self._is_on_topic(output, context),
            "no_pii": self._no_pii_leaked(output),
            "no_harmful": self._no_harmful_content(output),
            "confidence": self._assess_confidence(output),
            "needs_review": self._needs_human_review(output, context)
        }
```

### 6.3 Action Limits

```python
AGENT_LIMITS = {
    "max_iterations": 25,
    "max_tool_calls": 50,
    "max_cost_usd": 2.00,
    "max_runtime_seconds": 300,
    "max_tokens_per_turn": 4096,
    "max_retries_per_tool": 3,
    "require_confirmation_for": ["send_email", "create_event",
                                  "update_record", "delete_record"],
    "forbidden_actions": ["delete_database", "modify_permissions",
                          "access_admin_panel"],
}
```

---

## 7. Implementation Template

### 7.1 Complete Agent Implementation

```python
"""
Complete AI Agent Implementation Template
Customize this template for your specific use case.
"""

import anthropic
import json
import time
import logging
from datetime import datetime
from typing import List, Dict, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("agent")


class Agent:
    def __init__(self, name: str, purpose: str, tools: list,
                 model: str = "claude-sonnet-4-20250514"):
        self.name = name
        self.purpose = purpose
        self.tools = tools
        self.model = model
        self.client = anthropic.Anthropic()
        self.max_iterations = 20
        self.cost_cap = 2.0

        # State tracking
        self.iteration_count = 0
        self.total_cost = 0.0
        self.tool_call_log = []

        # Build system prompt
        self.system_prompt = self._build_system_prompt()

    def _build_system_prompt(self) -> str:
        return f"""You are {self.name}, an AI agent.

Purpose: {self.purpose}

Process:
1. Analyze the task carefully
2. Plan your approach before acting
3. Use tools when you need external data or actions
4. Verify results before delivering them
5. If uncertain, explain what you know and what you do not

Rules:
- Stay focused on your purpose
- Never fabricate information
- When using tools, explain why
- If you cannot complete a task, say so clearly
- Always be truthful about your limitations

Current date: {datetime.now().strftime('%Y-%m-%d')}
"""

    def run(self, user_message: str) -> str:
        """Execute the agent on a user message."""
        logger.info(f"Agent '{self.name}' starting task: "
                    f"{user_message[:100]}...")

        messages = [{"role": "user", "content": user_message}]
        self.iteration_count = 0

        while self.iteration_count < self.max_iterations:
            self.iteration_count += 1
            logger.info(f"Iteration {self.iteration_count}")

            # Check cost cap
            if self.total_cost >= self.cost_cap:
                logger.warning("Cost cap reached")
                return ("I have reached my processing budget for this task. "
                        "Here is what I have so far based on my work.")

            # Call the model
            try:
                response = self.client.messages.create(
                    model=self.model,
                    max_tokens=4096,
                    system=self.system_prompt,
                    tools=self.tools,
                    messages=messages
                )
            except Exception as e:
                logger.error(f"API error: {e}")
                return f"I encountered an error: {str(e)}"

            # Track costs (approximate)
            self._track_cost(response.usage)

            # Process response
            if response.stop_reason == "tool_use":
                # Handle tool calls
                messages.append({
                    "role": "assistant",
                    "content": response.content
                })

                tool_results = self._process_tool_calls(response.content)
                messages.append({
                    "role": "user",
                    "content": tool_results
                })

            elif response.stop_reason == "end_turn":
                # Agent has completed
                final_text = ""
                for block in response.content:
                    if hasattr(block, "text"):
                        final_text += block.text

                logger.info(f"Task completed in {self.iteration_count} "
                           f"iterations, cost: ${self.total_cost:.4f}")
                return final_text

        return "I reached the maximum number of steps for this task."

    def _process_tool_calls(self, content) -> list:
        """Process and execute tool calls from the model response."""
        results = []

        for block in content:
            if block.type == "tool_use":
                logger.info(f"Tool call: {block.name}({block.input})")

                # Log the tool call
                self.tool_call_log.append({
                    "tool": block.name,
                    "input": block.input,
                    "timestamp": datetime.now().isoformat()
                })

                # Execute the tool
                try:
                    result = self._execute_tool(block.name, block.input)
                    results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": str(result)
                    })
                except Exception as e:
                    logger.error(f"Tool error: {block.name}: {e}")
                    results.append({
                        "type": "tool_result",
                        "tool_use_id": block.id,
                        "content": f"Error: {str(e)}",
                        "is_error": True
                    })

        return results

    def _execute_tool(self, tool_name: str, tool_input: dict):
        """Execute a specific tool. Override this method."""
        raise NotImplementedError(
            f"Tool '{tool_name}' not implemented. "
            f"Override _execute_tool in your agent subclass."
        )

    def _track_cost(self, usage):
        """Track approximate API costs."""
        input_cost = usage.input_tokens * 0.000003  # Approximate
        output_cost = usage.output_tokens * 0.000015  # Approximate
        self.total_cost += input_cost + output_cost

    def get_execution_summary(self) -> dict:
        """Return a summary of the agent's execution."""
        return {
            "agent": self.name,
            "iterations": self.iteration_count,
            "tool_calls": len(self.tool_call_log),
            "total_cost": f"${self.total_cost:.4f}",
            "tool_call_details": self.tool_call_log
        }
```

---

## 8. Multi-Agent Systems

### 8.1 Multi-Agent Orchestrator

```python
class MultiAgentOrchestrator:
    """Coordinates multiple specialized agents."""

    def __init__(self):
        self.agents = {}
        self.workflow_log = []

    def register_agent(self, agent_id: str, agent: Agent,
                       capabilities: list):
        self.agents[agent_id] = {
            "agent": agent,
            "capabilities": capabilities,
            "status": "available"
        }

    def execute_workflow(self, workflow: list) -> dict:
        """
        Execute a multi-agent workflow.

        workflow = [
            {
                "step": "research",
                "agent": "researcher",
                "task": "Research topic X",
                "depends_on": []
            },
            {
                "step": "analyze",
                "agent": "analyst",
                "task": "Analyze the research findings",
                "depends_on": ["research"]
            },
            {
                "step": "write",
                "agent": "writer",
                "task": "Write a report based on the analysis",
                "depends_on": ["analyze"]
            }
        ]
        """
        results = {}

        for step in workflow:
            # Check dependencies
            dep_results = {}
            for dep in step.get("depends_on", []):
                if dep not in results:
                    raise ValueError(
                        f"Dependency '{dep}' not yet completed "
                        f"for step '{step['step']}'"
                    )
                dep_results[dep] = results[dep]

            # Build task with dependency context
            task = step["task"]
            if dep_results:
                context = "\n\n".join(
                    f"Results from {k}:\n{v}"
                    for k, v in dep_results.items()
                )
                task = f"{task}\n\nContext from previous steps:\n{context}"

            # Execute
            agent_info = self.agents[step["agent"]]
            agent_info["status"] = "busy"

            result = agent_info["agent"].run(task)
            results[step["step"]] = result

            agent_info["status"] = "available"

            self.workflow_log.append({
                "step": step["step"],
                "agent": step["agent"],
                "task": step["task"],
                "result_length": len(result),
                "timestamp": datetime.now().isoformat()
            })

        return results
```

---

## 9. Evaluation Framework

### 9.1 Agent Performance Metrics

```python
class AgentEvaluator:
    """Evaluate agent performance across multiple dimensions."""

    def evaluate(self, test_cases: list) -> dict:
        """
        Run evaluation on a set of test cases.

        test_case = {
            "input": "user message",
            "expected_behavior": "what the agent should do",
            "success_criteria": ["criterion 1", "criterion 2"],
            "max_iterations": 10,
            "max_cost": 0.50
        }
        """
        results = {
            "total_cases": len(test_cases),
            "passed": 0,
            "failed": 0,
            "errors": 0,
            "avg_iterations": 0,
            "avg_cost": 0,
            "avg_latency": 0,
            "details": []
        }

        for case in test_cases:
            case_result = self._run_case(case)
            results["details"].append(case_result)

            if case_result["passed"]:
                results["passed"] += 1
            elif case_result["error"]:
                results["errors"] += 1
            else:
                results["failed"] += 1

        # Calculate averages
        n = len(test_cases)
        results["avg_iterations"] = (
            sum(d["iterations"] for d in results["details"]) / n
        )
        results["avg_cost"] = (
            sum(d["cost"] for d in results["details"]) / n
        )
        results["avg_latency"] = (
            sum(d["latency"] for d in results["details"]) / n
        )
        results["pass_rate"] = results["passed"] / n

        return results
```

### 9.2 Key Metrics

| Metric | Description | Target |
|---|---|---|
| Task completion rate | % of tasks successfully completed | > 90% |
| Accuracy | Correctness of final output | > 95% |
| Efficiency | Average iterations per task | < 10 |
| Cost per task | Average $ cost per task completion | < $0.50 |
| Latency | Average time to completion | < 60 seconds |
| Safety rate | % of outputs passing safety checks | 100% |
| Recovery rate | % of errors the agent recovers from | > 80% |
| Tool accuracy | % of tool calls that are appropriate | > 95% |

---

## 10. Production Deployment Checklist

```
PRE-DEPLOYMENT
[ ] All tools tested individually and in combination
[ ] System prompt reviewed and approved
[ ] Safety guardrails implemented and tested
[ ] Cost limits configured and tested
[ ] Logging and monitoring in place
[ ] Error handling covers all known failure modes
[ ] Load testing completed
[ ] Security review passed
[ ] Human escalation paths defined
[ ] Rollback procedure documented

DEPLOYMENT
[ ] Canary deployment to small user group
[ ] Monitor error rates, latency, and costs
[ ] Verify logging captures all actions
[ ] Test human escalation paths
[ ] Validate output quality with sample checks

POST-DEPLOYMENT
[ ] Daily monitoring of key metrics
[ ] Weekly review of edge cases and failures
[ ] Monthly evaluation against test suite
[ ] Quarterly security review
[ ] Continuous prompt and tool optimization
[ ] User feedback collection and analysis
```

---

*This blueprint is part of the Master in Prompt Engineering and AI — Module 10.*
