# RAG vs. Fine-Tuning vs. Prompt Engineering: Decision Framework

## Module 05: Code and Examples

---

## Quick Decision Flowchart

```
START: What do you need to improve?
|
|-- "The model doesn't KNOW specific information"
|   |
|   |-- Does the info change frequently?
|   |   |-- YES --> RAG
|   |   |-- NO  --> RAG (or fine-tuning if very static)
|   |
|   |-- Do you need source citations?
|       |-- YES --> RAG (inherent source tracking)
|       |-- NO  --> RAG or Fine-Tuning
|
|-- "The model doesn't BEHAVE the way I want"
|   |
|   |-- Can better prompting fix it?
|   |   |-- YES --> Prompt Engineering
|   |   |-- Maybe --> Try prompting first, then fine-tune
|   |   |-- NO  --> Fine-Tuning
|   |
|   |-- Is it a format/style issue?
|   |   |-- YES --> Fine-Tuning (or structured output prompting)
|   |   |-- NO  --> Analyze further
|   |
|   |-- Is it a tone/persona issue?
|       |-- Mild --> Prompt Engineering
|       |-- Strong/consistent --> Fine-Tuning
|
|-- "Both: needs knowledge AND different behavior"
    |
    --> RAG + Fine-Tuning (Hybrid approach)
```

---

## Detailed Comparison Matrix

### When to Use Each Approach

| Scenario | Prompt Engineering | RAG | Fine-Tuning | Best Choice |
|----------|:--:|:--:|:--:|---|
| General Q&A | OK | -- | -- | **Prompting** |
| Domain-specific knowledge | Poor | Best | Poor | **RAG** |
| Consistent JSON output | Fair | Fair | Best | **Fine-Tuning** |
| Current events / live data | N/A | Best | N/A | **RAG** |
| Brand voice / persona | Fair | N/A | Best | **Fine-Tuning** |
| Source citations needed | N/A | Best | N/A | **RAG** |
| Reduce per-query cost | Worst | Middle | Best | **Fine-Tuning** |
| Quick deployment needed | Best | Middle | Worst | **Prompting** |
| Classification (50+ classes) | Poor | N/A | Best | **Fine-Tuning** |
| Proprietary document Q&A | N/A | Best | Poor | **RAG** |
| Multi-language support | Fair | Good | Fair | **RAG** |
| Edge case handling | Poor | Depends | Good | **Fine-Tuning** |

### Cost Analysis Template

```
SCENARIO: [Describe your use case]

Monthly query volume: ___________
Average prompt length (tokens): ___________
Average response length (tokens): ___________

OPTION A: PROMPT ENGINEERING ONLY
  Setup cost:           $0
  Tokens per query:     System prompt (___) + User (___) + Response (___)
  Cost per query:       $___
  Monthly cost:         $___
  Annual cost:          $___

OPTION B: RAG
  Setup cost:           $___  (vector DB + ingestion pipeline)
  Monthly infra:        $___  (vector DB hosting)
  Tokens per query:     System (___) + Context (___) + User (___) + Response (___)
  Cost per query:       $___
  Monthly cost:         $___
  Annual cost:          $___

OPTION C: FINE-TUNING
  Setup cost:           $___  (data prep + training)
  Tokens per query:     System (___) + User (___) + Response (___)
  Cost per query:       $___  (often lower due to shorter prompts)
  Monthly cost:         $___
  Annual cost:          $___

OPTION D: RAG + FINE-TUNING (HYBRID)
  Setup cost:           $___  (sum of both)
  Monthly infra:        $___
  Tokens per query:     System (___) + Context (___) + User (___) + Response (___)
  Cost per query:       $___
  Monthly cost:         $___
  Annual cost:          $___
```

---

## Decision Scorecard

Rate each factor on a scale of 0-3 for your specific use case:

| Factor | Weight | Prompting | RAG | Fine-Tuning | Your Scores |
|--------|--------|:---------:|:---:|:-----------:|-------------|
| Need for external knowledge | x3 | 0 | 3 | 0 | P:__ R:__ F:__ |
| Knowledge update frequency | x2 | 0 | 3 | 0 | P:__ R:__ F:__ |
| Output format consistency | x2 | 1 | 1 | 3 | P:__ R:__ F:__ |
| Speed to deploy | x2 | 3 | 2 | 1 | P:__ R:__ F:__ |
| Per-query cost sensitivity | x2 | 0 | 2 | 3 | P:__ R:__ F:__ |
| Source citation needed | x2 | 0 | 3 | 0 | P:__ R:__ F:__ |
| Team ML expertise | x1 | 3 | 2 | 1 | P:__ R:__ F:__ |
| Behavioral consistency | x2 | 1 | 1 | 3 | P:__ R:__ F:__ |
| Data privacy concerns | x1 | 3 | 2 | 2 | P:__ R:__ F:__ |
| Budget constraints | x1 | 3 | 2 | 1 | P:__ R:__ F:__ |

**Scoring**: Multiply each score by its weight, sum per column. Highest total wins.

```
Prompting total:    ___
RAG total:          ___
Fine-Tuning total:  ___

Recommended approach: _____________

Consider hybrid if top two scores are close: _______________
```

---

## Real-World Decision Examples

### Example 1: Internal HR Chatbot

```
Requirement: Answer employee questions about company policies
Knowledge: 500 pages of HR documents, updated quarterly
Users: 2,000 employees
Volume: ~500 queries/day

ANALYSIS:
  - External knowledge needed? YES (company policies)     --> RAG
  - Updates frequently?         QUARTERLY                  --> RAG handles well
  - Special behavior needed?    Standard helpful responses  --> Prompting sufficient
  - Source citations?           YES (policy references)     --> RAG

DECISION: RAG + Prompt Engineering
REASON: Primary need is knowledge access, not behavior change.
        RAG provides knowledge + citations. Good prompting provides tone.
```

### Example 2: Code Review Bot

```
Requirement: Review pull requests following company coding standards
Knowledge: Coding guidelines (50 pages), evolving standards
Users: 80 developers
Volume: ~100 PRs/day

ANALYSIS:
  - External knowledge?    YES (coding standards)     --> RAG
  - Updates frequently?    Monthly                     --> RAG
  - Special behavior?      YES (specific review format) --> Fine-Tuning
  - Consistent format?     YES (severity, categories)   --> Fine-Tuning

DECISION: RAG + Fine-Tuning (Hybrid)
REASON: Need both knowledge (current standards) and behavior (review format).
```

### Example 3: Marketing Copy Generator

```
Requirement: Generate ad copy in brand voice for 50 clients
Knowledge: Brand guidelines per client
Users: 20 marketers
Volume: ~200 requests/day

ANALYSIS:
  - External knowledge?    Minimal (brand guidelines)  --> Prompting (few-shot)
  - Updates frequently?    Rarely per client            --> Either
  - Special behavior?      YES (brand voice per client) --> Prompting (per-client)
  - Consistent format?     Varies by client             --> Prompting

DECISION: Prompt Engineering (with brand-specific prompts per client)
REASON: Too many clients to fine-tune individually.
        Brand voice can be captured with good system prompts + examples.
        If one client dominates volume, consider fine-tuning for that one.
```

### Example 4: Medical Triage Assistant

```
Requirement: Help nurses triage patients based on symptoms
Knowledge: Medical protocols, drug interactions, clinical guidelines
Users: 500 nurses across 10 hospitals
Volume: ~2,000 queries/day

ANALYSIS:
  - External knowledge?    YES (critical, domain-specific)  --> RAG
  - Updates frequently?    Monthly (new protocols)           --> RAG
  - Special behavior?      YES (clinical reasoning format)   --> Fine-Tuning
  - Source citations?      YES (regulatory requirement)      --> RAG
  - Safety critical?       YES                               --> RAG + Fine-Tuning

DECISION: RAG + Fine-Tuning + Human-in-the-Loop
REASON: Safety-critical application requires:
  - RAG for current, citable medical knowledge
  - Fine-tuning for consistent clinical reasoning format
  - Human validation before any recommendation is actioned
```

---

## Progressive Enhancement Strategy

The recommended approach for most projects:

```
PHASE 1: START WITH PROMPTING (Week 1)
  Goal: Validate the use case
  Effort: 1-3 days
  Cost: $0 (just API costs)
  Deliverable: Working prototype with system prompt + few-shot examples

  Evaluate: Does it work 70%+ of the time?
  If YES and 70% is enough --> STOP (prompting is sufficient)
  If YES but need better --> Go to Phase 2
  If NO --> Go to Phase 2

PHASE 2: ADD RAG (Weeks 2-3)
  Goal: Solve knowledge gaps and add source attribution
  Effort: 1-2 weeks
  Cost: $200-$1000 (vector DB + pipeline setup)
  Deliverable: RAG pipeline with document retrieval

  Evaluate: Does it work 85%+ of the time?
  If YES and 85% is enough --> STOP
  If YES but need better --> Go to Phase 3
  If NO and it is a knowledge problem --> Improve RAG (chunking, retrieval)
  If NO and it is a behavior problem --> Go to Phase 3

PHASE 3: ADD FINE-TUNING (Weeks 4-6)
  Goal: Improve behavioral consistency, reduce costs, handle edge cases
  Effort: 2-4 weeks (primarily data preparation)
  Cost: $500-$5000 (data prep labor + training costs)
  Deliverable: Fine-tuned model with RAG pipeline

  Evaluate: Does it meet all requirements?
  If YES --> Production deployment
  If NO --> Iterate on data quality, consider model upgrade
```

---

## Anti-Patterns to Avoid

### 1. Fine-Tuning for Knowledge
```
BAD:  "Our model doesn't know our product prices, let's fine-tune!"
WHY:  Fine-tuning doesn't reliably teach facts; it teaches behavior.
      The model may hallucinate prices or generate outdated ones.
GOOD: Use RAG to retrieve current pricing from your database.
```

### 2. RAG for Style/Format
```
BAD:  "Our model's output format is inconsistent, let's add more RAG docs!"
WHY:  RAG provides information, not formatting instructions.
      More documents won't fix a formatting problem.
GOOD: Fine-tune for consistent format, or improve your prompt template.
```

### 3. Skipping Prompt Engineering
```
BAD:  "Our basic prompt doesn't work well, let's jump to fine-tuning!"
WHY:  Fine-tuning amplifies behavior. If your prompt is bad, your
      training data (based on what you think the model should do)
      may also be suboptimal.
GOOD: Master prompting first. The insights inform better training data.
```

### 4. Over-Engineering
```
BAD:  "Let's build RAG + fine-tuning + MCP + agents for our FAQ bot!"
WHY:  Most FAQ bots work great with just RAG + good prompting.
      Extra complexity means more failure points and maintenance.
GOOD: Start simple. Add complexity only when simple isn't enough.
```

---

## Summary: The One-Sentence Guide

- **Prompt Engineering**: When you need to *instruct* the model differently.
- **RAG**: When the model needs to *know* things it does not know.
- **Fine-Tuning**: When the model needs to *behave* differently than its default.
- **Hybrid**: When you need *both* new knowledge *and* new behavior.
