# Task Decomposition Framework

## Module 03 — Code and Examples

---

A step-by-step framework for decomposing any complex task into manageable subtasks optimized for AI execution. Includes decision trees, templates, and worked examples.

---

## The DECOMPOSE Framework

```
D — Define the overall objective
E — Enumerate all components of the final output
C — Classify dependencies between components
O — Order subtasks (parallel or sequential)
M — Map inputs and outputs for each subtask
P — Prompt each subtask individually
O — Orchestrate the execution
S — Synthesize subtask outputs
E — Evaluate against the original objective
```

---

## Step 1: Define the Overall Objective

### What to Do
Write a single, clear sentence describing what you need to produce.

### Template
```
I need to produce a [deliverable type] that [purpose/goal]
for [audience]. It should include [key components] and be
[quality attributes].
```

### Examples

**Vague (needs work):**
```
I need a business report.
```

**Clear (ready to decompose):**
```
I need to produce a 10-page competitive analysis report that
evaluates our three main competitors' market positioning, product
offerings, pricing strategies, and growth trajectories for the
executive leadership team. It should include data-backed insights
and strategic recommendations, and be ready for board presentation.
```

### Checklist
- [ ] The objective states what the final deliverable IS
- [ ] The purpose/goal is explicit
- [ ] The audience is identified
- [ ] Key components are listed
- [ ] Quality attributes are defined
- [ ] Success criteria are implied or stated

---

## Step 2: Enumerate All Components

### What to Do
List every distinct piece that the final deliverable must contain. Think of this as a table of contents, outline, or parts list.

### Template
```
Final Deliverable: [name]

Components:
1. [Component name] — [brief description]
2. [Component name] — [brief description]
3. [Component name] — [brief description]
...

Optional Components:
A. [Component name] — [brief description]
B. [Component name] — [brief description]
```

### Worked Example: Competitive Analysis Report

```
Final Deliverable: Competitive Analysis Report

Components:
1. Executive Summary — 1-page overview of key findings and recommendations
2. Market Overview — Current market size, growth rate, trends
3. Competitor Profile: Company A — Products, pricing, market share, strategy
4. Competitor Profile: Company B — Products, pricing, market share, strategy
5. Competitor Profile: Company C — Products, pricing, market share, strategy
6. Comparative Matrix — Side-by-side comparison table across all criteria
7. SWOT Analysis — Our strengths, weaknesses, opportunities, threats
8. Strategic Recommendations — 3-5 actionable recommendations with rationale
9. Appendix — Data sources, methodology notes

Optional Components:
A. Market share visualization
B. Pricing trend analysis
C. Customer sentiment comparison
```

### Tips
- Be exhaustive — it is easier to remove components than to discover missing ones later
- Ask: "If I delivered everything on this list, would the deliverable be complete?"
- Check against the objective: does every component contribute to the goal?

---

## Step 3: Classify Dependencies

### What to Do
Determine which components depend on other components. Draw a dependency map.

### Dependency Types

| Type | Symbol | Meaning |
|------|--------|---------|
| Independent | `[ ]` | Can be created without any other component |
| Depends on | `->` | Requires another component's output as input |
| Informs | `~>` | Benefits from but does not strictly require another component |
| Mutual | `<->` | Two components that reference each other |

### Template
```
Dependency Map:

[Component 1] — Independent
[Component 2] — Independent
[Component 3] — Independent
[Component 4] -> Depends on [1, 2, 3]
[Component 5] -> Depends on [4]
[Component 6] ~> Informed by [1]
[Component 7] -> Depends on [ALL]
```

### Worked Example

```
Dependency Map:

[1] Executive Summary       -> Depends on [2,3,4,5,6,7,8] (write LAST)
[2] Market Overview         — Independent
[3] Competitor A Profile    — Independent
[4] Competitor B Profile    — Independent
[5] Competitor C Profile    — Independent
[6] Comparative Matrix      -> Depends on [3,4,5]
[7] SWOT Analysis           -> Depends on [2,6]
[8] Strategic Recommendations -> Depends on [7]
[9] Appendix                — Independent (can be built alongside)
```

### Visual Dependency Diagram
```
        [2] Market Overview (independent)
        |
        |   [3] Comp A ─┐
        |   [4] Comp B ──┼── [6] Comparative Matrix
        |   [5] Comp C ─┘        |
        |                         |
        └────────────────┐        |
                         v        v
                    [7] SWOT Analysis
                         |
                         v
                [8] Strategic Recommendations
                         |
                         v
                [1] Executive Summary

[9] Appendix (parallel throughout)
```

---

## Step 4: Order Subtasks

### What to Do
Using the dependency map, determine the execution order. Maximize parallel execution where possible.

### Template
```
Execution Plan:

Phase 1 (Parallel — no dependencies):
  - [Component A]
  - [Component B]
  - [Component C]

Phase 2 (Requires Phase 1):
  - [Component D] (uses A, B, C)

Phase 3 (Requires Phase 2):
  - [Component E] (uses D)

Phase 4 (Requires all above):
  - [Component F] (synthesizes everything)
```

### Worked Example

```
Execution Plan:

Phase 1 — Research (Parallel):
  - [2] Market Overview
  - [3] Competitor A Profile
  - [4] Competitor B Profile
  - [5] Competitor C Profile
  - [9] Appendix (start building)

Phase 2 — Analysis (Requires Phase 1):
  - [6] Comparative Matrix (uses 3, 4, 5)

Phase 3 — Strategic Assessment (Requires Phases 1-2):
  - [7] SWOT Analysis (uses 2, 6)

Phase 4 — Recommendations (Requires Phase 3):
  - [8] Strategic Recommendations (uses 7)

Phase 5 — Synthesis (Requires all):
  - [1] Executive Summary (uses 2-8)
  - [9] Appendix (finalize)
```

### Decision: Parallel vs. Sequential

```
Can this subtask be completed without the output of any other subtask?
  YES -> Parallel (run simultaneously)
  NO  -> Sequential (run after dependencies complete)

Does this subtask BENEFIT from (but not REQUIRE) another subtask?
  BENEFIT -> Sequential but low priority for ordering
  REQUIRE -> Sequential and must wait
```

---

## Step 5: Map Inputs and Outputs

### What to Do
For each subtask, define exactly what it needs as input and what it produces as output.

### Template
```
Subtask: [Name]
  Input:  [What it needs]
  Output: [What it produces]
  Format: [Expected output format]
  Length:  [Expected output length]
  Quality Criteria: [How to evaluate the output]
```

### Worked Example

```
Subtask: Competitor A Profile
  Input:  Company name, product category, publicly available information
  Output: Structured profile covering products, pricing, market share, strategy
  Format: Markdown with headers, tables, and bullet points
  Length:  400-600 words
  Quality Criteria:
    - All sections covered (products, pricing, market share, strategy)
    - Specific numbers and facts (not vague generalizations)
    - Balanced tone (not opinionated)
    - Sourced claims where possible

Subtask: Comparative Matrix
  Input:  Profiles of Competitors A, B, C (from Phase 1)
  Output: Side-by-side comparison table
  Format: Markdown table with all competitors as columns
  Length:  1 table with 8-12 rows
  Quality Criteria:
    - Consistent criteria across all competitors
    - Apples-to-apples comparison (same metrics)
    - Visual indicators of advantage (highest/lowest highlighted)
    - No missing cells

Subtask: Executive Summary
  Input:  All other sections (2-8)
  Output: 1-page overview of key findings and top 3 recommendations
  Format: 3-4 paragraphs, no bullet points
  Length:  250-350 words
  Quality Criteria:
    - Can stand alone (reader gets the gist without reading the full report)
    - Includes the single most important finding prominently
    - Ends with a clear recommendation
    - No new information (only synthesizes what is in the report)
```

---

## Step 6: Write Individual Prompts

### What to Do
Write a focused prompt for each subtask. Each prompt should be self-contained and include all necessary context.

### Subtask Prompt Template
```
## Context
[Background information the model needs to know]

## Task
[Specific task for this subtask]

## Input
[Any data or previous outputs needed]

## Requirements
[Specific requirements for this subtask's output]

## Output Format
[Exact format specification]

## Constraints
[Length limits, style requirements, what to avoid]
```

### Worked Example: Prompt for Competitor Profile

```
You are a market research analyst preparing a competitive
analysis report.

## Task
Create a detailed profile of [Competitor Name] for inclusion
in a competitive analysis report.

## Context
Industry: [Industry]
Our company: [Brief description]
Purpose: This profile will be compared side-by-side with
two other competitors.

## Requirements
Cover these areas:
1. **Company Overview:** Founded, HQ, size, funding/revenue
2. **Product Offerings:** Main products/services, key features
3. **Pricing Strategy:** Pricing model, price points, tiers
4. **Market Position:** Estimated market share, target segments
5. **Growth Trajectory:** Recent growth, expansion plans
6. **Strengths:** Top 3 competitive advantages
7. **Weaknesses:** Top 3 vulnerabilities

## Output Format
Use Markdown with H3 headers (###) for each section.
Use tables for pricing and product comparison data.
Use bullet points for strengths and weaknesses.

## Constraints
- 400-600 words
- Factual and balanced tone (not promotional or dismissive)
- Quantify wherever possible (revenue numbers, growth rates)
- Clearly label any estimates as such
- Do not include speculative future predictions
```

---

## Step 7: Orchestrate Execution

### What to Do
Execute the prompts according to the phase plan, feeding outputs forward as needed.

### Execution Tracker Template

```
## Execution Tracker

| Phase | Subtask | Status | Output Quality | Notes |
|-------|---------|--------|----------------|-------|
| 1 | Market Overview | Complete | 4/5 | Needs more recent data |
| 1 | Competitor A | Complete | 5/5 | Good |
| 1 | Competitor B | Complete | 4/5 | Missing pricing detail |
| 1 | Competitor C | In Progress | — | — |
| 2 | Comparative Matrix | Blocked | — | Waiting for Comp C |
| 3 | SWOT | Not Started | — | — |
| 4 | Recommendations | Not Started | — | — |
| 5 | Executive Summary | Not Started | — | — |
```

### Handling Quality Issues
When a subtask output does not meet quality criteria:

1. **Minor issues:** Note them and proceed; fix during synthesis.
2. **Major issues:** Re-run the subtask with refined instructions.
3. **Blocking issues:** Fix before proceeding to dependent phases.

---

## Step 8: Synthesize Outputs

### What to Do
Combine all subtask outputs into the final deliverable.

### Synthesis Prompt Template

```
You are an editor assembling a [deliverable type] from
sections written by different analysts.

Here are the sections:

<section_1>
[Output of subtask 1]
</section_1>

<section_2>
[Output of subtask 2]
</section_2>

[... additional sections ...]

## Your Task
Combine these sections into a single, cohesive [deliverable type].

## Requirements
1. Ensure consistent terminology throughout
   (e.g., if one section calls it "revenue" and another "sales,"
   standardize to one term)
2. Add smooth transitions between sections
3. Remove any redundant information
4. Ensure the document flows logically
5. Verify no contradictory statements exist
6. Add an introduction if not present
7. Add a conclusion that ties everything together

## Constraints
- Do not add new information not present in the sections
- Maintain the factual content of each section
- Keep the total length under [limit]
- Use [style/tone] throughout
```

### Synthesis Checklist
- [ ] All components are present
- [ ] Terminology is consistent
- [ ] Transitions are smooth
- [ ] No contradictions between sections
- [ ] No redundant information
- [ ] Introduction and conclusion present
- [ ] Formatting is consistent
- [ ] Meets length requirements

---

## Step 9: Evaluate the Final Result

### What to Do
Check the final deliverable against the original objective.

### Evaluation Template

```
## Evaluation Checklist

### Completeness
- [ ] All required components are present
- [ ] All optional components included (if specified)
- [ ] No sections are stub or placeholder

### Quality
- [ ] Factually accurate
- [ ] Well-reasoned analysis
- [ ] Actionable recommendations
- [ ] Appropriate depth for the audience

### Consistency
- [ ] Consistent tone throughout
- [ ] Consistent terminology
- [ ] No contradictions between sections
- [ ] Formatting is uniform

### Alignment with Objective
- [ ] Meets the stated purpose
- [ ] Appropriate for the target audience
- [ ] Includes all required deliverable elements

### Final Rating
Overall Quality: [1-5]
Ready for delivery: [Yes / Needs revision]
Revision notes: [specific items to fix]
```

---

## Quick Decomposition Templates for Common Tasks

### Template A: Report Writing
```
Phase 1 (Parallel): Research each section topic independently
Phase 2 (Sequential): Write each section
Phase 3 (Sequential): Synthesize into cohesive document
Phase 4 (Sequential): Write executive summary (last)
Phase 5 (Sequential): Edit and polish
```

### Template B: Code Development
```
Phase 1 (Sequential): Design architecture / API contracts
Phase 2 (Parallel): Implement independent modules
Phase 3 (Sequential): Integrate modules
Phase 4 (Parallel): Write tests for each module
Phase 5 (Sequential): Integration testing and review
```

### Template C: Strategic Analysis
```
Phase 1 (Parallel): Gather data from multiple perspectives
Phase 2 (Sequential): Analyze data and identify patterns
Phase 3 (Sequential): Develop options and evaluate tradeoffs
Phase 4 (Sequential): Form recommendation
Phase 5 (Sequential): Write up with supporting evidence
```

### Template D: Content Campaign
```
Phase 1 (Sequential): Define messaging and value propositions
Phase 2 (Parallel): Create assets for each channel
Phase 3 (Sequential): Review for cross-channel consistency
Phase 4 (Sequential): Finalize and prepare for deployment
```

### Template E: Educational Course
```
Phase 1 (Sequential): Define learning objectives
Phase 2 (Parallel): Create content for each lesson
Phase 3 (Parallel): Create exercises and assessments
Phase 4 (Sequential): Order and connect lessons
Phase 5 (Sequential): Create introduction and overview
Phase 6 (Sequential): Review for pedagogical coherence
```

---

## Decision Trees

### Should I Decompose This Task?

```
Is the task achievable with a single, focused prompt?
|
+-- YES: Does the output need to be > 1000 words?
|   |
|   +-- YES -> Decompose (long outputs lose quality)
|   +-- NO  -> Single prompt is fine
|
+-- NO: Does it require multiple types of work?
    |
    +-- YES -> Decompose by function
    |          (research, analysis, writing, formatting)
    |
    +-- NO: Does it have sequential dependencies?
        |
        +-- YES -> Decompose sequentially
        +-- NO  -> Decompose into parallel components
```

### How Many Subtasks?

```
Task complexity:
|
+-- Simple (1-2 requirements) -> 1-2 subtasks
+-- Moderate (3-5 requirements) -> 3-5 subtasks
+-- Complex (6-10 requirements) -> 5-8 subtasks
+-- Very Complex (10+ requirements) -> 8-15 subtasks
                                       (use hierarchical decomposition)
```

### When to Stop Decomposing?

```
For each subtask, ask:
|
+-- Can it be described in 1-2 sentences? -> STOP
+-- Does it have a single, clear output? -> STOP
+-- Can the model handle it in one prompt? -> STOP
+-- Is it still complex or multi-part? -> KEEP DECOMPOSING
```

---

## Worked Example: Complete Decomposition

### Task: "Create a product launch plan for a new mobile app"

**Step 1: Define**
```
Produce a comprehensive product launch plan for a new fitness
mobile app (FitTrack AI) that includes market positioning,
go-to-market strategy, marketing tactics, timeline, and budget
for the product marketing team. The plan should cover the period
from 8 weeks pre-launch through 4 weeks post-launch.
```

**Step 2: Enumerate**
```
1. Executive Summary
2. Product Positioning Statement
3. Target Audience Profiles (3 personas)
4. Competitive Landscape Summary
5. Key Messages and Value Propositions
6. Go-to-Market Strategy
7. Marketing Channels and Tactics
8. Launch Timeline (12-week calendar)
9. Budget Allocation
10. KPIs and Success Metrics
11. Risk Assessment and Contingency Plans
```

**Step 3: Classify Dependencies**
```
[1]  Executive Summary      -> ALL (write last)
[2]  Positioning            — Independent
[3]  Target Audience        — Independent
[4]  Competitive Landscape  — Independent
[5]  Key Messages           -> [2, 3]
[6]  GTM Strategy           -> [2, 3, 4, 5]
[7]  Marketing Tactics      -> [3, 5, 6]
[8]  Launch Timeline        -> [6, 7]
[9]  Budget                 -> [7, 8]
[10] KPIs                   -> [6]
[11] Risk Assessment        -> [6, 7, 8]
```

**Step 4: Order**
```
Phase 1 (Parallel): [2] [3] [4]
Phase 2 (Sequential): [5] (needs 2, 3)
Phase 3 (Sequential): [6] (needs 2, 3, 4, 5)
Phase 4 (Parallel): [7] [10] (both need 6)
Phase 5 (Parallel): [8] [11] (need 6, 7)
Phase 6 (Sequential): [9] (needs 7, 8)
Phase 7 (Sequential): [1] (needs everything)
```

**Step 5: Map I/O**
```
[2] Positioning: Input=product features -> Output=positioning statement
[3] Audience: Input=product description -> Output=3 persona profiles
[4] Competition: Input=app category -> Output=landscape summary
[5] Messages: Input=positioning+personas -> Output=3-5 key messages
[6] GTM: Input=positioning+personas+competition+messages -> Output=strategy doc
[7] Tactics: Input=personas+messages+strategy -> Output=channel plan
[8] Timeline: Input=strategy+tactics -> Output=12-week calendar
[9] Budget: Input=tactics+timeline -> Output=budget table
[10] KPIs: Input=strategy -> Output=metrics dashboard design
[11] Risks: Input=strategy+tactics+timeline -> Output=risk register
[1] Summary: Input=ALL -> Output=1-page executive summary
```

**Steps 6-9:** Execute each subtask with its own focused prompt, assemble, and evaluate.

---

## Troubleshooting Common Decomposition Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Subtask outputs contradict each other | No shared context | Include consistent background info in each subtask prompt |
| Synthesis produces disjointed output | Styles too different | Add style guide to each subtask prompt |
| Some subtasks produce thin output | Too narrowly scoped | Combine related subtasks |
| Dependencies create bottlenecks | Too many sequential dependencies | Re-evaluate if some can be parallelized |
| Final result misses the objective | Lost sight of goal during decomposition | Re-check components against objective before execution |

---

*This reference is part of Module 03: Basic and Intermediate Prompt Techniques.*
