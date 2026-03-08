# Tree of Thoughts: Implementation Templates

## Module 04 Code Examples

---

## Overview

This document provides five complete Tree of Thoughts (ToT) prompt templates, each designed for a different problem type. Each template includes the full prompt, expected flow, and usage notes.

---

## Template 1: Strategic Decision Making

### Problem Type
Choosing between multiple options with complex tradeoffs (e.g., business strategy, architecture decisions, career choices).

### Full Prompt Template

```
You are a strategic analyst using the Tree of Thoughts method
to evaluate a decision with multiple options.

DECISION: {{decision_description}}

OPTIONS: {{list_of_options}}

CONTEXT: {{relevant_context}}

---

PHASE 1: INITIAL BRANCHING (Breadth-First Exploration)

For EACH option, develop an initial analysis:

### Branch: {{Option A}}
**Strengths**: List 3-5 key advantages
**Weaknesses**: List 3-5 key disadvantages
**Key Assumption**: What must be true for this option to succeed?
**Initial Score**: Rate 1-10 on feasibility, impact, and risk
**Feasibility**: ___/10
**Impact**: ___/10
**Risk (10=lowest risk)**: ___/10
**Composite Score**: (Feasibility + Impact + Risk) / 3 = ___

### Branch: {{Option B}}
[Same structure]

### Branch: {{Option C}}
[Same structure]

---

PHASE 2: PRUNING

Based on the composite scores:
- **Advance** (top 2): [list the top 2 options]
- **Eliminate** (if clearly inferior): [list eliminated options and why]

---

PHASE 3: DEEP EXPLORATION (Depth-First on Top 2)

For each advancing branch, explore 3 levels deeper:

### Deep Dive: {{Top Option 1}}

**Level 1**: Implementation Plan
- What are the first 3 concrete steps?
- What resources are needed?
- Timeline estimate?

**Level 2**: Risk Mitigation
- What could go wrong?
- How would you detect early warning signs?
- What is the contingency plan?

**Level 3**: Long-Term Implications
- What does success look like in 1 year? 5 years?
- What second-order effects might emerge?
- How does this position you for future decisions?

### Deep Dive: {{Top Option 2}}
[Same structure]

---

PHASE 4: COMPARISON AND SELECTION

| Criterion | {{Option 1}} | {{Option 2}} |
|-----------|-------------|-------------|
| Short-term benefit | | |
| Long-term benefit | | |
| Risk level | | |
| Resource requirement | | |
| Reversibility | | |
| Alignment with goals | | |

**SYNTHESIS**: Consider whether elements from the runner-up
can strengthen the winner.

**FINAL RECOMMENDATION**: [Clear recommendation with justification]
**CONFIDENCE LEVEL**: [How confident are you in this recommendation?]
```

### Usage Example

```
DECISION: Should our 50-person SaaS startup expand into the
European market, the Asian market, or focus on deepening our
US market penetration?

OPTIONS: A) European expansion B) Asian expansion C) US deepening

CONTEXT: Current ARR $5M, 80% US customers, product is
an AI-powered HR platform, team of 50 (40 in US, 10 remote)
```

---

## Template 2: Creative Problem Solving

### Problem Type
Open-ended problems requiring creative or innovative solutions (e.g., product design, marketing campaigns, UX challenges).

### Full Prompt Template

```
You are a creative problem solver using the Tree of Thoughts
method. Generate diverse solutions through branching exploration.

PROBLEM: {{problem_description}}

CONSTRAINTS: {{any_limitations}}

TARGET AUDIENCE: {{who_this_is_for}}

---

PHASE 1: DIVERGENT BRANCHING (5 Ideas)

Generate 5 VERY DIFFERENT initial ideas. Each should use
a fundamentally different approach:

### Idea 1: The Conventional Approach
[What would the standard, safe solution look like?]
- Core concept: ___
- Key mechanism: ___
- Novelty score (1-10): ___

### Idea 2: The Opposite Approach
[What if you did the opposite of the conventional approach?]
- Core concept: ___
- Key mechanism: ___
- Novelty score (1-10): ___

### Idea 3: The Analogy Approach
[What solution works in a completely different domain that
you could adapt?]
- Borrowed from: ___ domain
- Core concept: ___
- Key mechanism: ___
- Novelty score (1-10): ___

### Idea 4: The Technology-First Approach
[What if you started with the most advanced technology available?]
- Technology leveraged: ___
- Core concept: ___
- Key mechanism: ___
- Novelty score (1-10): ___

### Idea 5: The Constraint-Removal Approach
[What would you do if you removed the biggest constraint?]
- Constraint removed: ___
- Core concept: ___
- Key mechanism: ___
- Novelty score (1-10): ___

---

PHASE 2: EVALUATE AND SELECT

For each idea, rate:
- **Feasibility** (1-10): Can this actually be implemented?
- **Impact** (1-10): How well does this solve the problem?
- **Novelty** (1-10): How differentiated is this from existing solutions?
- **Delight** (1-10): Would the target audience love this?

| Idea | Feasibility | Impact | Novelty | Delight | TOTAL |
|------|------------|--------|---------|---------|-------|
| 1    |            |        |         |         |       |
| 2    |            |        |         |         |       |
| 3    |            |        |         |         |       |
| 4    |            |        |         |         |       |
| 5    |            |        |         |         |       |

**Top 2 to explore further**: ___

---

PHASE 3: DEVELOP AND COMBINE

Take the top 2 ideas and develop each into a detailed concept:

### Concept A (from Idea ___):
- **Detailed description** (3-5 sentences):
- **User journey** (step by step):
- **Key differentiator**:
- **Biggest risk**:

### Concept B (from Idea ___):
- **Detailed description** (3-5 sentences):
- **User journey** (step by step):
- **Key differentiator**:
- **Biggest risk**:

### Hybrid Concept (best of both):
- Can elements from Concept A and B be combined?
- **Hybrid description**:
- **What from A**: ___
- **What from B**: ___
- **Why this combination works**: ___

---

PHASE 4: FINAL RECOMMENDATION

**Recommended Solution**: [The best concept -- A, B, or Hybrid]
**One-Sentence Pitch**: ___
**Next Steps**: [3 concrete actions to move forward]
```

---

## Template 3: Technical Debugging

### Problem Type
Diagnosing complex technical issues with multiple possible causes.

### Full Prompt Template

```
You are a senior software engineer using the Tree of Thoughts
method to diagnose a complex technical issue.

BUG DESCRIPTION: {{bug_description}}
SYMPTOMS: {{what_is_observed}}
ENVIRONMENT: {{system_details}}
RECENT CHANGES: {{what_changed_recently}}

---

PHASE 1: HYPOTHESIS GENERATION

Generate 4 independent hypotheses for the root cause:

### Hypothesis A: {{Category 1 -- e.g., Data Issue}}
- **Theory**: [What might have gone wrong]
- **Expected Evidence**: [If this hypothesis is correct, we would see...]
- **Quick Test**: [Simplest way to confirm or deny this hypothesis]
- **Prior Probability**: ___% (how likely based on symptoms)

### Hypothesis B: {{Category 2 -- e.g., Configuration Issue}}
[Same structure]

### Hypothesis C: {{Category 3 -- e.g., Concurrency Issue}}
[Same structure]

### Hypothesis D: {{Category 4 -- e.g., External Dependency Issue}}
[Same structure]

---

PHASE 2: EVIDENCE COLLECTION

For each hypothesis, trace the evidence:

### Testing Hypothesis A:
- **Test 1**: [What to check] -> **Expected if A is correct**: [result]
- **Test 2**: [What to check] -> **Expected if A is correct**: [result]
- **Verdict**: CONFIRMED / DENIED / INCONCLUSIVE

### Testing Hypothesis B:
[Same structure]

### Testing Hypothesis C:
[Same structure]

### Testing Hypothesis D:
[Same structure]

---

PHASE 3: NARROWING

Based on evidence:
- **Most likely cause**: [Hypothesis ___] because [reasoning]
- **Runner-up**: [Hypothesis ___] because [reasoning]
- **Eliminated**: [Hypothesis ___] because [evidence against it]

Develop the most likely cause further:
- **Exact mechanism**: Step by step, how does this cause the bug?
- **Root cause vs. symptom**: Is this the root cause or just a symptom?
- **If it is a symptom, what is the deeper root cause?**: ___

---

PHASE 4: SOLUTION

**Root Cause**: [clear statement]

**Fix**:
1. [Immediate fix to stop the bleeding]
2. [Proper fix to address root cause]
3. [Preventive measure to avoid recurrence]

**Verification**:
- How to verify the fix works: ___
- How to confirm no regressions: ___
- Monitoring to add: ___
```

---

## Template 4: Ethical Dilemma Analysis

### Problem Type
Complex ethical decisions where multiple valid perspectives exist and there is no clear "right answer."

### Full Prompt Template

```
You are an ethics advisor using the Tree of Thoughts method
to analyze a complex ethical dilemma.

DILEMMA: {{dilemma_description}}

STAKEHOLDERS: {{who_is_affected}}

---

PHASE 1: FRAMEWORK BRANCHING

Analyze this dilemma through 4 different ethical frameworks:

### Branch A: Consequentialist Analysis (outcomes-focused)
- **Best case outcome**: If we choose [action], the best outcome is...
- **Worst case outcome**: The worst outcome is...
- **Most likely outcome**: Realistically...
- **Who benefits**: ___
- **Who is harmed**: ___
- **Net assessment**: Positive / Negative / Neutral

### Branch B: Deontological Analysis (duty/rules-focused)
- **Relevant duties/rules**: What obligations apply here?
- **Rights at stake**: Whose rights are involved?
- **Universal principle test**: If everyone took this action,
  would it be acceptable?
- **Assessment**: Permissible / Impermissible / Obligatory

### Branch C: Virtue Ethics Analysis (character-focused)
- **What would a person of good character do?**
- **Which virtues are relevant** (courage, honesty, compassion,
  justice, etc.)?
- **Which vices are tempting** (cowardice, dishonesty, cruelty, etc.)?
- **Assessment**: Virtuous / Neutral / Vicious

### Branch D: Care Ethics Analysis (relationship-focused)
- **How does this affect relationships?**
- **Who is most vulnerable?**
- **What does caring for all parties look like?**
- **Assessment**: Caring / Neglectful

---

PHASE 2: CROSS-FRAMEWORK COMPARISON

| Criterion | Consequentialist | Deontological | Virtue | Care |
|-----------|-----------------|---------------|--------|------|
| Recommended action | | | | |
| Primary concern | | | | |
| Key risk | | | | |

**Points of agreement**: [Where do multiple frameworks agree?]
**Points of disagreement**: [Where do they conflict?]

---

PHASE 3: SYNTHESIS

Considering all four frameworks:

**If frameworks agree**: The clear ethical path is [action] because
multiple ethical traditions converge on the same conclusion.

**If frameworks disagree**: The dilemma is genuine. Here is a
balanced recommendation:
- **Recommended action**: ___
- **Primary justification**: ___
- **Acknowledged tradeoff**: ___
- **Mitigation for those disadvantaged by this choice**: ___

---

PHASE 4: PRACTICAL GUIDANCE

1. **What to do**: [Clear, actionable recommendation]
2. **How to communicate**: [How to explain this decision to stakeholders]
3. **What to monitor**: [Ongoing concerns to watch for]
4. **When to revisit**: [Conditions that would trigger re-evaluation]
```

---

## Template 5: Research Question Exploration

### Problem Type
Exploring a complex research question where the best approach is unclear.

### Full Prompt Template

```
You are a research strategist using the Tree of Thoughts method
to explore a complex question from multiple angles before
determining the best answer.

RESEARCH QUESTION: {{question}}

---

PHASE 1: ANGLE GENERATION

Generate 4 different angles from which to approach this question:

### Angle 1: The Historical Perspective
- **Reframe**: How has this question been answered historically?
- **Key historical examples or precedents**: ___
- **What history suggests**: ___
- **Confidence in this angle**: ___/10

### Angle 2: The Data-Driven Perspective
- **Reframe**: What does the available data say?
- **Key statistics or studies**: ___
- **What the data suggests**: ___
- **Confidence in this angle**: ___/10

### Angle 3: The Theoretical Perspective
- **Reframe**: What do established theories predict?
- **Relevant theories or models**: ___
- **What theory suggests**: ___
- **Confidence in this angle**: ___/10

### Angle 4: The Contrarian Perspective
- **Reframe**: What if the common assumption is wrong?
- **Key challenge to conventional wisdom**: ___
- **Alternative interpretation**: ___
- **Confidence in this angle**: ___/10

---

PHASE 2: DEEP DIVE INTO TOP 2

Select the two most productive angles and explore each in depth:

### Deep Dive: {{Angle X}}

**Sub-Question 1**: ___
- Finding: ___
- Confidence: HIGH / MEDIUM / LOW

**Sub-Question 2**: ___
- Finding: ___
- Confidence: HIGH / MEDIUM / LOW

**Sub-Question 3**: ___
- Finding: ___
- Confidence: HIGH / MEDIUM / LOW

**Interim Conclusion from this angle**: ___

### Deep Dive: {{Angle Y}}
[Same structure]

---

PHASE 3: INTEGRATION

**Where the angles agree**: ___
**Where they disagree**: ___
**What additional information would resolve disagreements**: ___

---

PHASE 4: COMPREHENSIVE ANSWER

Drawing on all explored angles:

**Answer**: [Comprehensive answer to the research question]

**Confidence**: [Overall confidence level with justification]

**Key Caveats**: [What could change this answer]

**Suggested Further Research**: [What questions remain open]
```

---

## Quick Reference: Choosing the Right Template

| Problem Type | Template | Key Feature |
|-------------|----------|-------------|
| Choose between options | Template 1 (Strategic) | Comparative scoring |
| Need creative solutions | Template 2 (Creative) | Divergent then convergent |
| Diagnose what went wrong | Template 3 (Debugging) | Hypothesis testing |
| Navigate ethical complexity | Template 4 (Ethical) | Multi-framework analysis |
| Explore a research topic | Template 5 (Research) | Multi-angle investigation |

---

## Tips for Customization

1. **Adjust the number of branches** based on problem complexity (3-5 is typical)
2. **Adjust evaluation criteria** to match what matters most for your domain
3. **Add domain-specific frameworks** (e.g., PESTLE for business, OWASP for security)
4. **Combine templates** when a problem spans multiple types
5. **Use the output of one template** as the input for another (e.g., Template 5 output feeds into Template 1 for decision-making)
