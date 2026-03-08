# Prompt Anatomy Cheatsheet — Module 02

## Visual Reference Guide for Prompt Components

---

## 1. The Four Foundational Components

```
┌─────────────────────────────────────────────────────────────────┐
│                      EFFECTIVE PROMPT                            │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ 1. INSTRUCTION                                            │  │
│  │    What do you want the AI to DO?                        │  │
│  │    • Start with an action verb                           │  │
│  │    • Be specific about the task                          │  │
│  │    • One primary task per prompt                         │  │
│  │                                                           │  │
│  │    Examples: Analyze, Write, Compare, Extract, Generate   │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ 2. CONTEXT                                                │  │
│  │    What background does the AI need?                     │  │
│  │    • Who you are (your role)                             │  │
│  │    • Who the audience is                                 │  │
│  │    • What the situation is                               │  │
│  │    • Why this is needed                                  │  │
│  │                                                           │  │
│  │    Tip: Include only RELEVANT context                    │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ 3. INPUT DATA                                             │  │
│  │    What material should the AI work with?                │  │
│  │    • Text to analyze or transform                        │  │
│  │    • Data to process                                     │  │
│  │    • Examples to follow (few-shot)                       │  │
│  │    • Code to review or extend                            │  │
│  │                                                           │  │
│  │    Tip: Use clear delimiters (""", ```, <tags>)          │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │ 4. OUTPUT FORMAT                                          │  │
│  │    How should the result look?                           │  │
│  │    • Structure (paragraphs, bullets, table, JSON)        │  │
│  │    • Length (word count, sentences, pages)                │  │
│  │    • Tone (formal, casual, technical)                    │  │
│  │    • What to include AND what to exclude                 │  │
│  │                                                           │  │
│  │    Tip: Specify format EVERY time                        │  │
│  └───────────────────────────────────────────────────────────┘  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. The CRISP Framework

```
C ─── CONTEXT ───────── What is the background and situation?
│     • Industry/domain
│     • Current situation
│     • Target audience
│     • Stakes/importance
│
R ─── ROLE ──────────── Who should the AI be?
│     • Professional identity
│     • Expertise level
│     • Perspective to adopt
│     • Experience background
│
I ─── INSTRUCTIONS ──── What specific task to perform?
│     • Action verb (Analyze, Write, Compare...)
│     • Step-by-step if multi-part
│     • What NOT to do
│     • Priority order
│
S ─── SPECIFICS ─────── What details and constraints apply?
│     • Requirements (must-have elements)
│     • Constraints (boundaries and limits)
│     • Edge cases (how to handle exceptions)
│     • Quality criteria (what "good" looks like)
│
P ─── PARAMETERS ────── How should the output look?
      • Format (JSON, markdown, table, prose)
      • Length (word count, items, pages)
      • Tone (formal, casual, technical)
      • Style (academic, journalistic, conversational)
```

---

## 3. CRISP Quick-Fill Template

Copy and fill in this template for any prompt:

```
**CONTEXT:**
I am a [YOUR ROLE] at [ORGANIZATION TYPE].
I am working on [PROJECT/TASK].
The situation is [DESCRIBE SITUATION].
The audience is [DESCRIBE AUDIENCE].

**ROLE:**
You are a [PROFESSIONAL IDENTITY] with [EXPERIENCE LEVEL]
specializing in [AREA OF EXPERTISE].

**INSTRUCTIONS:**
[ACTION VERB] the following:
1. [STEP 1]
2. [STEP 2]
3. [STEP 3]

Do NOT:
- [EXCLUSION 1]
- [EXCLUSION 2]

**SPECIFICS:**
Requirements:
- [REQUIREMENT 1]
- [REQUIREMENT 2]
- [REQUIREMENT 3]

Constraints:
- [CONSTRAINT 1]
- [CONSTRAINT 2]

**PARAMETERS:**
Format: [STRUCTURE TYPE]
Length: [WORD/ITEM COUNT]
Tone: [TONE DESCRIPTION]
Include: [MUST-HAVE ELEMENTS]
Exclude: [MUST-NOT-HAVE ELEMENTS]
```

---

## 4. Instruction Verbs — Quick Reference

### Creation Verbs
```
Write    → Produce new text from scratch
Generate → Create content based on parameters
Draft    → Produce an initial version for review
Compose  → Create structured content (letters, music, poetry)
Create   → Build something new (plans, frameworks, systems)
Design   → Conceptualize a structure or solution
```

### Analysis Verbs
```
Analyze  → Examine in detail to understand components
Evaluate → Assess quality, effectiveness, or value
Compare  → Identify similarities and differences
Assess   → Judge the significance or value of
Critique → Provide detailed critical evaluation
Audit    → Systematically examine for accuracy or compliance
```

### Transformation Verbs
```
Summarize  → Condense to key points
Paraphrase → Restate in different words
Translate  → Convert between languages
Convert    → Change from one format to another
Simplify   → Reduce complexity while preserving meaning
Expand     → Add detail and depth to existing content
```

### Extraction Verbs
```
Extract   → Pull specific information from text
Identify  → Find and name specific elements
List      → Enumerate items or findings
Highlight → Draw attention to specific elements
Classify  → Assign items to categories
Filter    → Select items matching criteria
```

### Reasoning Verbs
```
Explain    → Clarify how or why something works
Recommend  → Suggest a course of action with reasoning
Predict    → Estimate future outcomes based on data
Justify    → Provide reasoning for a position
Prioritize → Rank items by importance or urgency
Diagnose   → Identify the cause of a problem
```

---

## 5. Context Types — When to Include Each

```
┌─────────────────────────────────────────────────────┐
│  ALWAYS INCLUDE (Essential Context)                  │
├─────────────────────────────────────────────────────┤
│  • Your role / the relevant perspective              │
│  • Target audience                                   │
│  • Purpose of the output                             │
│  • Domain / industry                                 │
└─────────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────┐
│  INCLUDE WHEN RELEVANT (Situational Context)         │
├─────────────────────────────────────────────────────┤
│  • Current status or situation                       │
│  • Budget / timeline / resource constraints          │
│  • Previous attempts or approaches                   │
│  • Stakeholder concerns or preferences               │
│  • Specific examples or data                         │
└─────────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────┐
│  INCLUDE WHEN NECESSARY (Background Context)         │
├─────────────────────────────────────────────────────┤
│  • Historical background (how things got here)       │
│  • Technical environment details                     │
│  • Organizational structure / culture                │
│  • Regulatory / compliance requirements              │
└─────────────────────────────────────────────────────┘
              │
              ▼
┌─────────────────────────────────────────────────────┐
│  AVOID INCLUDING                                     │
├─────────────────────────────────────────────────────┤
│  ✗ Irrelevant personal details                      │
│  ✗ Redundant information (same thing 3 ways)        │
│  ✗ Entire company history (unless relevant)         │
│  ✗ Obvious facts the AI already knows               │
│  ✗ Confidential information not needed for the task │
└─────────────────────────────────────────────────────┘
```

---

## 6. Output Format Decision Tree

```
What will the output be used for?
│
├── Read by humans directly?
│   ├── Short communication → Plain text (email, message)
│   ├── Long-form content → Markdown (headers, formatting)
│   ├── Presentation → Bullet points or outline
│   └── Comparison → Table (markdown or HTML)
│
├── Processed by software?
│   ├── API / database → JSON
│   ├── Spreadsheet → CSV
│   ├── Legacy system → XML
│   └── Configuration → YAML or JSON
│
├── Executed as code?
│   ├── Single function → Code block with language tag
│   ├── Full module → Multiple code blocks, labeled
│   └── With tests → Code + test code blocks
│
└── Mixed use?
    └── Combine formats (e.g., markdown report with JSON data blocks)
```

---

## 7. The Goldilocks Zones

### Prompt Length
```
Too Short               Just Right                Too Long
◄──────────────────────────────────────────────────────────►
"Write code"      "Write a Python function     [500+ word prompt
                   that validates emails        for a simple task]
                   with regex, type hints,
                   error handling, and
                   3 unit tests"
```

### Context Amount
```
No Context              Right Amount              Context Overload
◄──────────────────────────────────────────────────────────►
"Fix this"         "Fix this login bug.       [Entire company
                    Stack: React + Node.       history, team bios,
                    Error: 401 on valid        5-year roadmap for
                    credentials. Started       a bug fix]
                    after the auth
                    middleware update."
```

### Specificity Level
```
Too Vague               Just Right                Over-Specified
◄──────────────────────────────────────────────────────────►
"Write an email"   "Write a 150-word           "Write exactly 147
                    professional email          words, 3 paragraphs
                    to a client about a         of 49 words each,
                    project delay. Tone:        starting each para
                    transparent, reassuring.    with a different
                    Include revised timeline    vowel, using only
                    and apology."               Anglo-Saxon words..."
```

---

## 8. Delimiter Reference

Use delimiters to clearly separate different parts of your prompt:

```
TRIPLE QUOTES — For text input
"""
Your input text goes here.
"""

TRIPLE BACKTICKS — For code input
```python
def example():
    return "code here"
```

XML TAGS — For structured sections (especially effective with Claude)
<context>
Background information here.
</context>

<input>
Data to process here.
</input>

MARKDOWN HEADERS — For prompt sections
## Task
What to do.

## Context
Background info.

## Format
How to structure the output.

DASHES/EQUALS — For simple separation
---
Section content here
---

NUMBERED SECTIONS — For sequential instructions
1. First, do this.
2. Then, do this.
3. Finally, do this.
```

---

## 9. Common Tone Specifications

| Tone Label | What It Means | Good For |
|------------|---------------|----------|
| **Formal** | Professional, structured, no contractions | Legal, academic, executive communication |
| **Professional** | Business-appropriate, clear, respectful | Emails, reports, documentation |
| **Conversational** | Natural, uses contractions, friendly | Blog posts, chat, social media |
| **Technical** | Precise, jargon-acceptable, detailed | Developer docs, specs, technical writing |
| **Casual** | Relaxed, informal, personality-forward | Social media, internal team comms |
| **Authoritative** | Confident, decisive, expert | Thought leadership, recommendations |
| **Empathetic** | Warm, understanding, supportive | Customer support, sensitive topics |
| **Persuasive** | Compelling, benefit-focused, engaging | Marketing, sales, proposals |
| **Neutral** | Balanced, objective, no opinion | News reporting, research summaries |
| **Enthusiastic** | Energetic, positive, excited | Product launches, community engagement |

---

## 10. Pre-Submit Checklist

Run through this before sending any important prompt:

```
BEFORE YOU HIT SEND
====================

□ INSTRUCTION is clear
  □ Starts with an action verb
  □ Single interpretation possible
  □ One primary task

□ CONTEXT is sufficient
  □ Audience defined
  □ Purpose stated
  □ Domain/industry specified
  □ No irrelevant information

□ INPUT is well-formatted
  □ Clearly delimited
  □ Labeled if multiple inputs
  □ Complete (nothing missing)

□ OUTPUT is specified
  □ Format defined
  □ Length defined
  □ Tone defined
  □ Inclusions stated
  □ Exclusions stated

□ SANITY CHECK
  □ No conflicting instructions
  □ No ambiguous pronouns
  □ Stranger could understand this
  □ Task is achievable in one prompt
  □ Ready to iterate if needed
```

---

## 11. Emergency Fixes for Common Problems

| Problem | Quick Fix |
|---------|-----------|
| Output is too long | Add: "Maximum [X] words. Be concise." |
| Output is too generic | Add: Role assignment + specific audience |
| Output has wrong tone | Add: "Tone: [specific description]. Write like [example publication]." |
| Output format is wrong | Add: Exact format template with example |
| Output includes unwanted content | Add: "Do NOT include [specific exclusions]." |
| Output is repetitive | Add: "Use varied vocabulary. Do not repeat phrases." |
| Output is too cautious/disclaimery | Add: "Respond directly without disclaimers or caveats." |
| Output misses the point | Add: More context about WHY you need this |
| Output has factual errors | Add: "Only state facts you are confident about. Flag uncertainty." |
| Output is not actionable | Add: "Every recommendation must include a specific next step." |

---

*Part of Module 02 — Introduction to Prompt Engineering*
