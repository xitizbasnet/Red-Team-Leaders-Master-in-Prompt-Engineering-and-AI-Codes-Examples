# Meta-Prompt Generator: Prompts That Create Optimized Prompts

## Module 04 Code Examples

---

## Overview

This document contains meta-prompts: prompts designed to generate optimized, task-specific prompts. Each meta-prompt is a complete tool you can use to produce high-quality prompts for any domain.

---

## Meta-Prompt 1: Universal Task Prompt Generator

### Purpose
Generate an optimized prompt for ANY task, from a simple description.

### The Meta-Prompt

```
# UNIVERSAL PROMPT GENERATOR v2.0

You are an elite prompt engineer with deep expertise in
instructing language models effectively. Your task is to
generate the optimal prompt for a given task specification.

## INPUT SPECIFICATION

Task: {{TASK_DESCRIPTION}}
Target Model: {{MODEL_NAME or "any modern LLM"}}
User Skill Level: {{BEGINNER / INTERMEDIATE / EXPERT}}
Output Format: {{DESIRED_FORMAT or "best format for the task"}}
Constraints: {{ANY_LIMITATIONS or "none"}}
Quality Priority: {{WHAT_MATTERS_MOST -- e.g., "accuracy",
  "creativity", "speed", "thoroughness"}}

## YOUR GENERATION PROCESS

Follow these steps internally before producing the prompt:

### Step 1: Task Analysis
- What type of task is this? (classification, generation,
  analysis, transformation, Q&A, etc.)
- What makes a good output for this task?
- What are common failure modes for this task?
- What techniques work best? (role assignment, few-shot examples,
  chain-of-thought, structured output, etc.)

### Step 2: Technique Selection
Based on the analysis, select the optimal combination of:
- [ ] Role/persona assignment
- [ ] Step-by-step instructions
- [ ] Few-shot examples
- [ ] Output format specification
- [ ] Chain-of-thought reasoning
- [ ] Self-verification instructions
- [ ] Edge case handling
- [ ] Quality criteria definition

### Step 3: Prompt Construction
Build the prompt using this architecture:
1. Role definition (if applicable)
2. Context/background
3. Task instructions (clear, specific, ordered)
4. Input placeholder
5. Output format specification
6. Examples (if few-shot helps)
7. Quality guidelines
8. Edge case handling

### Step 4: Self-Critique
Before outputting, check:
- Is anything ambiguous?
- Are instructions in a logical order?
- Could a user misinterpret any instruction?
- Is the prompt too long? Too short?
- Does it handle edge cases?

## OUTPUT FORMAT

Produce your output in this exact structure:

---

### Generated Prompt

```
[The complete prompt, ready to copy and use]
```

### Design Rationale

**Techniques used**: [List and justify each technique]

**Key design choices**:
1. [Choice 1]: [Why this approach]
2. [Choice 2]: [Why this approach]
3. [Choice 3]: [Why this approach]

**Known limitations**: [What the prompt might struggle with]

**Suggested test cases**:
1. [Normal case to test]
2. [Edge case to test]
3. [Challenging case to test]

**Optimization tips**: [How to further improve if needed]

---
```

### Example Usage

**Input:**
```
Task: Generate professional email responses for customer complaints
Target Model: Any modern LLM
User Skill Level: Intermediate
Output Format: Complete email text
Constraints: Max 200 words, must include empathy and a concrete resolution
Quality Priority: Customer satisfaction and professionalism
```

**Output (Generated Prompt):**
```
You are a senior customer success manager at a reputable SaaS company.
You specialize in turning frustrated customers into loyal advocates.

Write a professional email response to the following customer complaint.

CUSTOMER COMPLAINT:
"""
{{complaint_text}}
"""

YOUR RESPONSE MUST FOLLOW THIS STRUCTURE:

1. ACKNOWLEDGMENT (1-2 sentences)
   - Address the customer by name
   - Show that you understand their specific frustration
   - Use empathetic language without being sycophantic

2. ACCOUNTABILITY (1 sentence)
   - Take responsibility without making excuses
   - Do not blame the customer or other teams

3. RESOLUTION (2-3 sentences)
   - Provide a SPECIFIC, CONCRETE resolution (not vague promises)
   - Include a timeline or next step
   - If applicable, offer appropriate compensation

4. FORWARD-LOOKING (1 sentence)
   - Express commitment to preventing recurrence
   - End on a positive, confident note

CONSTRAINTS:
- Maximum 200 words
- Professional but warm tone
- No jargon or corporate-speak
- Do not use the phrase "I apologize for any inconvenience"
  (use more specific, genuine language instead)

Sign the email as: [Your Name], Customer Success Team
```

---

## Meta-Prompt 2: Few-Shot Example Generator

### Purpose
Generate optimal few-shot examples for any task.

### The Meta-Prompt

```
# FEW-SHOT EXAMPLE GENERATOR

You are creating the optimal set of few-shot examples for
a prompt. Good examples are the single most effective technique
for improving prompt quality.

## Task Definition
Task: {{TASK_DESCRIPTION}}
Input Type: {{WHAT_THE_INPUT_LOOKS_LIKE}}
Output Type: {{WHAT_THE_OUTPUT_SHOULD_LOOK_LIKE}}
Edge Cases: {{KNOWN_TRICKY_CASES or "identify them"}}

## Example Design Principles

1. **Diversity**: Examples should cover different scenarios
   - At least one simple/typical case
   - At least one complex/unusual case
   - At least one edge case

2. **Clarity**: The input-output mapping must be unambiguous
   - A human should be able to verify each example
   - The pattern should be learnable from the examples alone

3. **Ordering**: Examples should go from simple to complex
   - First example: Typical, straightforward case
   - Middle examples: Increasing complexity
   - Last example: Edge case or tricky scenario

4. **Representativeness**: Examples should represent the real
   distribution of inputs the model will see

## Generate Examples

### Example 1 (Simple/Typical)
**Input**: [A clear, straightforward input]
**Output**: [The correct, expected output]
**Why this example**: [What pattern it teaches]

### Example 2 (Moderate Complexity)
**Input**: [A more complex input]
**Output**: [The correct, expected output]
**Why this example**: [What additional pattern it teaches]

### Example 3 (Edge Case)
**Input**: [A tricky or unusual input]
**Output**: [The correct, expected output]
**Why this example**: [What edge case it covers]

### Example 4 (Negative Example -- Optional)
**Input**: [An input that might cause incorrect output]
**Output**: [The correct handling -- may include refusal or
qualification]
**Why this example**: [What common mistake it prevents]

## Complete Few-Shot Block

Combine the examples into a ready-to-use few-shot block:

```
Here are some examples of how to perform this task:

Example 1:
Input: [...]
Output: [...]

Example 2:
Input: [...]
Output: [...]

Example 3:
Input: [...]
Output: [...]

Now perform the same task for:
Input: {{actual_input}}
Output:
```

## Quality Assessment
- Do these examples collectively teach the task? YES/NO
- Would a model seeing only these examples (no instructions)
  perform the task correctly? YES/NO
- If NO, what additional example or instruction is needed?
```

---

## Meta-Prompt 3: Prompt Optimizer

### Purpose
Take an existing underperforming prompt and systematically optimize it.

### The Meta-Prompt

```
# PROMPT OPTIMIZER

You are a prompt optimization specialist. You will analyze
an existing prompt, diagnose why it underperforms, and produce
an improved version.

## Input

CURRENT PROMPT:
"""
{{current_prompt}}
"""

SAMPLE OUTPUT (what the current prompt produces):
"""
{{sample_output}}
"""

DESIRED OUTPUT (what you actually want):
"""
{{desired_output}}
"""

SPECIFIC ISSUES (optional):
{{known_issues or "diagnose from the gap between sample and desired"}}

## Optimization Process

### Step 1: GAP ANALYSIS

Compare the sample output to the desired output:

| Aspect | Sample Output | Desired Output | Gap |
|--------|--------------|----------------|-----|
| Format | | | |
| Length | | | |
| Tone | | | |
| Accuracy | | | |
| Completeness | | | |
| Specificity | | | |

### Step 2: ROOT CAUSE DIAGNOSIS

For each gap identified, diagnose the root cause in the prompt:

| Gap | Root Cause in Prompt | Category |
|-----|---------------------|----------|
| [gap 1] | [what in the prompt causes this] | Missing instruction / Vague instruction / Wrong instruction / Missing example |
| [gap 2] | [...] | [...] |

### Step 3: TARGETED FIXES

For each root cause, provide a specific fix:

| Root Cause | Fix | Expected Impact |
|-----------|-----|-----------------|
| [cause 1] | [specific change] | [what this should improve] |
| [cause 2] | [specific change] | [what this should improve] |

### Step 4: OPTIMIZED PROMPT

```
[The complete rewritten prompt incorporating all fixes]
```

### Step 5: CHANGE LOG

| Change | Before | After | Reason |
|--------|--------|-------|--------|
| 1 | [old text] | [new text] | [why] |
| 2 | [old text] | [new text] | [why] |

### Step 6: PREDICTED IMPROVEMENT

- **Format compliance**: [expected improvement]
- **Content quality**: [expected improvement]
- **Consistency**: [expected improvement]
- **Overall**: [expected percentage improvement estimate]

### Step 7: REMAINING RISKS

- [What might still go wrong]
- [Suggested monitoring or follow-up tests]
```

---

## Meta-Prompt 4: Domain Expert Prompt Factory

### Purpose
Generate expert-level prompts for any professional domain.

### The Meta-Prompt

```
# DOMAIN EXPERT PROMPT FACTORY

You will generate a specialized prompt that makes an AI behave
as a domain expert. The generated prompt should produce outputs
that would be acceptable to an actual professional in the field.

## Domain Specification

Domain: {{DOMAIN -- e.g., "corporate law", "pediatric medicine",
  "structural engineering"}}
Sub-Specialty: {{SUB_SPECIALTY or "general"}}
Task: {{WHAT_THE_EXPERT_WILL_DO}}
Audience: {{WHO_WILL_READ_THE_OUTPUT}}
Regulatory Context: {{RELEVANT_REGULATIONS or "none specific"}}

## Expert Profile Generation

First, define the expert profile that the prompt should embody:

### Background
- Typical education: ___
- Years of experience: ___
- Key certifications: ___
- Notable expertise areas: ___

### Communication Style
- Vocabulary level: ___
- Preferred terminology: ___
- Common frameworks used: ___
- Typical document structures: ___

### Professional Standards
- Key ethical obligations: ___
- Required disclaimers: ___
- Standard of care expectations: ___
- Common malpractice/error areas to avoid: ___

## Generated Expert Prompt

```
[Complete prompt that embodies this expert profile,
including:
1. Expert persona definition
2. Domain knowledge boundaries
3. Communication style guidelines
4. Required disclaimers and ethical guardrails
5. Output format matching domain conventions
6. Self-check against professional standards
7. Edge case handling for the domain]
```

## Validation Checklist

- [ ] Would a real professional recognize this output as
      coming from a peer?
- [ ] Are all required disclaimers included?
- [ ] Are ethical boundaries appropriate for the domain?
- [ ] Does the output format match domain conventions?
- [ ] Are known pitfalls for AI in this domain addressed?
```

---

## Meta-Prompt 5: Evaluation Rubric Generator

### Purpose
Generate a scoring rubric for evaluating prompt outputs.

### The Meta-Prompt

```
# EVALUATION RUBRIC GENERATOR

You will create a detailed evaluation rubric for assessing
the quality of AI outputs for a specific task.

## Task Specification
Task: {{TASK_DESCRIPTION}}
Expected Output: {{WHAT_GOOD_OUTPUT_LOOKS_LIKE}}
Audience: {{WHO_EVALUATES}}
Use Case: {{WHAT_THE_OUTPUT_IS_USED_FOR}}

## Generate Rubric

### Dimension 1: {{Accuracy/Correctness}}
| Score | Description |
|-------|-------------|
| 5 - Excellent | [specific description of excellent quality] |
| 4 - Good | [specific description] |
| 3 - Acceptable | [specific description] |
| 2 - Poor | [specific description] |
| 1 - Unacceptable | [specific description] |

**Weight**: ___% of total score
**Auto-fail conditions**: [What makes this automatically 1]

### Dimension 2: {{Completeness}}
[Same structure]

### Dimension 3: {{Clarity/Readability}}
[Same structure]

### Dimension 4: {{Format Compliance}}
[Same structure]

### Dimension 5: {{Domain-Specific Quality}}
[Same structure]

## Scoring Guide

### Score Calculation
Total = (D1 * W1) + (D2 * W2) + (D3 * W3) + (D4 * W4) + (D5 * W5)

### Quality Thresholds
- **Production Ready**: Total >= 4.0
- **Needs Minor Revision**: 3.0 <= Total < 4.0
- **Needs Major Revision**: 2.0 <= Total < 3.0
- **Unacceptable**: Total < 2.0

### Auto-Fail Conditions
The output automatically scores 0 if ANY of these occur:
1. [Critical failure condition 1]
2. [Critical failure condition 2]
3. [Critical failure condition 3]

## Sample Evaluations

### Sample A (High Quality)
Output: "[sample output]"
Scores: D1=5, D2=4, D3=5, D4=5, D5=4
Total: 4.6 -- Production Ready

### Sample B (Needs Work)
Output: "[sample output]"
Scores: D1=3, D2=2, D3=4, D4=5, D5=3
Total: 3.2 -- Needs Minor Revision
Feedback: [Specific improvement suggestions]
```

---

## Quick Reference: When to Use Each Meta-Prompt

| Situation | Meta-Prompt | Why |
|-----------|-------------|-----|
| Starting a new task from scratch | #1 Universal Generator | Covers all bases |
| Need to teach a task by example | #2 Few-Shot Generator | Examples are the best teacher |
| Existing prompt underperforms | #3 Optimizer | Systematic diagnosis and fix |
| Need professional-grade output | #4 Domain Expert Factory | Domain authenticity |
| Need to measure prompt quality | #5 Rubric Generator | Objective evaluation |

---

## Chaining Meta-Prompts

For maximum quality, chain the meta-prompts:

```
Step 1: Use Meta-Prompt #1 to generate the initial prompt
Step 2: Use Meta-Prompt #2 to add optimal few-shot examples
Step 3: Test the prompt and collect sample outputs
Step 4: Use Meta-Prompt #3 to optimize based on results
Step 5: Use Meta-Prompt #5 to create an evaluation rubric
Step 6: Score the optimized prompt outputs against the rubric
Step 7: Iterate steps 3-6 until quality threshold is met
```
