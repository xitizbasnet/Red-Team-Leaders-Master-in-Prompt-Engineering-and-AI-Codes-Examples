# Context Engineering Guide

## Module 09: Code and Examples

A practical guide to building optimal contexts with ready-to-use templates for different task types.

---

## Part 1: The Universal Context Structure

Every well-engineered prompt follows this structure. Customize the sections based on your task, but maintain the order.

### The Master Template

```markdown
# [1] ROLE
You are a {role_description} with expertise in {domain}.
Your communication style is {style_description}.

# [2] OBJECTIVE
Your task is to {specific_task}. The goal is {desired_outcome}.

# [3] BACKGROUND CONTEXT
Key information:
- {context_point_1}
- {context_point_2}
- {context_point_3}

# [4] DETAILED INSTRUCTIONS
Follow these steps:
1. {step_1}
2. {step_2}
3. {step_3}

# [5] CONSTRAINTS AND RULES
- DO: {what_to_do}
- DO NOT: {what_not_to_do}
- IMPORTANT: {critical_constraint}

# [6] INPUT / SOURCE MATERIAL
"""
{the_actual_content_to_work_with}
"""

# [7] OUTPUT FORMAT
Structure your response as:
{format_specification}

# [8] EXAMPLES (Optional)
Here is an example of the expected output:
"""
{example_output}
"""

# [9] QUALITY CHECK REMINDER
Before submitting your response:
- {quality_check_1}
- {quality_check_2}
- {quality_check_3}
```

---

## Part 2: Section-by-Section Guidance

### Section 1: Role Definition

**Purpose**: Sets the expertise level and perspective.

**Good examples:**
```
"You are a senior data scientist with 10 years of experience
in financial modeling."

"You are a patient educator who explains medical concepts
in clear, simple language for people without medical training."

"You are a technical writer who creates concise, accurate
API documentation following the Google developer documentation
style guide."
```

**Bad examples:**
```
"You are helpful." (too vague)
"You are the best AI ever." (meaningless flattery)
"You are a genius polymath." (too broad, no focus)
```

**Role selection guide:**
| Task Type | Effective Role |
|-----------|---------------|
| Factual writing | "[Domain] expert and technical writer" |
| Analysis | "Senior [domain] analyst with [X] years of experience" |
| Creative writing | "[Genre] author who writes in the style of [description]" |
| Code generation | "Senior [language] developer specializing in [area]" |
| Education | "[Subject] teacher for [audience level] students" |
| Editing | "Professional editor specializing in [type] content" |

---

### Section 2: Objective Definition

**Purpose**: Provides a clear, unambiguous goal.

**The SMART Objective Pattern:**
```
"Your task is to [SPECIFIC action] for [WHO] that
[MEASURABLE outcome] by [ACHIEVABLE scope],
focused on [RELEVANT domain], within [TIME-BOUND/
length constraints]."
```

**Good examples:**
```
"Your task is to write a 500-word executive summary of
the attached quarterly report for the board of directors,
highlighting the three most significant financial trends."

"Your task is to review this Python function and identify
all potential security vulnerabilities, explaining each
vulnerability and providing a corrected version."

"Your task is to create a comparison table of the five
cloud storage providers listed below, evaluating them
on price, storage capacity, security features, and
compliance certifications."
```

---

### Section 3: Background Context

**Purpose**: Provides information the model needs but does not have.

**What to include:**
```markdown
# Good: Specific, relevant context
- Company: SaaS B2B platform, Series C, 580 employees
- Industry: Cybersecurity
- Situation: Preparing for IPO in 18-24 months
- Audience: Board of directors (non-technical)
- Previous decisions: Decided to pursue IPO over acquisition

# Bad: Vague or irrelevant context
- Company: A tech company
- Industry: Technology
- Situation: Doing business stuff
```

**The Context Relevance Test:**
For each piece of context, ask: "If I removed this, would the output quality decrease?"
- If yes: keep it
- If no: remove it
- If maybe: include it briefly

---

### Section 4: Detailed Instructions

**Purpose**: Precise steps the model should follow.

**The Numbered Steps Pattern:**
```markdown
Follow these steps in order:

1. Read the entire source document
2. Identify the three main themes
3. For each theme:
   a. State the theme in one sentence
   b. Provide 2-3 supporting evidence points from the text
   c. Note any counterarguments presented
4. Synthesize the themes into an overall assessment
5. Provide your confidence level for each claim
```

**Instruction clarity checklist:**
```
□ Is each instruction actionable? (not just descriptive)
□ Is the order clear?
□ Are there decision points? (if X, then do Y)
□ Is each instruction specific enough that two people
  would interpret it the same way?
```

---

### Section 5: Constraints and Rules

**Purpose**: Prevents common failure modes.

**The Three Categories of Constraints:**

```markdown
# WHAT TO DO (Positive constraints)
- Use formal academic language
- Include citations for every factual claim
- Provide confidence scores for each statement

# WHAT NOT TO DO (Negative constraints)
- Do not fabricate citations or references
- Do not include information not in the source material
- Do not make forward-looking projections

# HARD RULES (Non-negotiable constraints)
- NEVER provide specific medication dosages
- ALWAYS include the disclaimer at the end
- MAXIMUM response length: 500 words
```

**Common constraint patterns for anti-hallucination:**
```markdown
- If you are not sure about a fact, say so rather than guessing
- Use ranges instead of precise numbers when uncertain
- Mark speculative content clearly as speculation
- Do not introduce data not present in the provided materials
```

---

### Section 6: Input / Source Material

**Purpose**: The actual content the model should work with.

**Formatting source material:**
```markdown
# For single documents:
"""
[Document text here]
"""

# For multiple documents with attribution:
SOURCE 1 [Annual Report 2023]:
"""
[Document 1 text]
"""

SOURCE 2 [Market Analysis]:
"""
[Document 2 text]
"""

# For structured data:
DATA:
| Column A | Column B | Column C |
|----------|----------|----------|
| value    | value    | value    |

# For code:
```python
def example():
    return "example code"
```
```

---

### Section 7: Output Format

**Purpose**: Defines the structure of the expected response.

**Common format templates:**

```markdown
# For reports:
## Executive Summary
[2-3 sentences]
## Key Findings
[Numbered list, max 5 items]
## Detailed Analysis
[Organized by theme]
## Recommendations
[Prioritized list]
## Limitations
[What this analysis does not cover]

# For comparisons:
| Feature | Option A | Option B | Winner |
|---------|----------|----------|--------|
| [feature] | [detail] | [detail] | [A/B/Tie] |

# For Q&A:
ANSWER: [Direct answer in 1-2 sentences]
CONFIDENCE: [High/Medium/Low]
EXPLANATION: [Supporting detail]
CAVEATS: [Important limitations]
VERIFICATION: [How to verify this answer]

# For code:
## Solution
```{language}
[code]
```
## Explanation
[What the code does and why]
## Usage
[How to use it]
## Edge Cases
[What to watch for]
```

---

### Section 8: Examples

**Purpose**: Demonstrates what good output looks like.

**One-shot example pattern:**
```markdown
Here is an example of the expected output quality and format:

INPUT: "Summarize the key changes in GDPR Article 17."
OUTPUT: "Article 17 of the GDPR establishes the 'right to
erasure' (commonly called the 'right to be forgotten'),
requiring data controllers to delete personal data when:
(1) the data is no longer necessary for its original purpose,
(2) the data subject withdraws consent, or (3) the data
was unlawfully processed. [HIGH CONFIDENCE]

Key limitations: The right does not apply when processing
is necessary for freedom of expression, legal obligations,
public health, or legal claims. [HIGH CONFIDENCE]

Source: GDPR Article 17, Regulation (EU) 2016/679"

Now apply this same approach to:
[Your actual task]
```

---

### Section 9: Quality Check Reminder

**Purpose**: Reinforces critical requirements at the end where attention is highest.

**Standard quality check:**
```markdown
Before submitting, verify:
□ All claims are based on the provided source material
□ No fabricated citations or statistics
□ Response follows the specified format
□ Confidence levels are included for factual claims
□ Uncertain claims are marked as such
□ Response length is within the specified limit
```

---

## Part 3: Complete Templates by Task Type

### Template A: Document Analysis

```markdown
# ROLE
You are a senior analyst specializing in {domain}.

# OBJECTIVE
Analyze the provided document and produce a {output_type}
for {audience}.

# BACKGROUND
- Document type: {type}
- Purpose of analysis: {purpose}
- Key questions to address:
  1. {question_1}
  2. {question_2}
  3. {question_3}

# INSTRUCTIONS
1. Read the document completely
2. Identify key themes and findings
3. Extract specific data points relevant to the questions
4. Organize findings by question
5. Note any gaps or limitations in the document

# CONSTRAINTS
- Base analysis ONLY on the provided document
- Quote specific passages for key claims
- If the document does not address a question, state
  "Not addressed in this document"
- Do not introduce outside knowledge or benchmarks

# DOCUMENT
"""
{document_text}
"""

# OUTPUT FORMAT
## Summary (3-5 sentences)
## Question 1: {question_1}
[Answer with citations from document]
## Question 2: {question_2}
[Answer with citations from document]
## Question 3: {question_3}
[Answer with citations from document]
## Key Data Points
| Metric | Value | Location in Document |
|--------|-------|---------------------|
## Gaps and Limitations
[What the document does not cover]

# QUALITY CHECK
□ Every claim traces to the document
□ Questions are directly addressed
□ Data points are exact (not paraphrased numbers)
□ Gaps are acknowledged, not filled
```

---

### Template B: Content Creation

```markdown
# ROLE
You are a {content_type} writer for {audience_description}.
Your writing style is {style_description}.

# OBJECTIVE
Create {content_type} about {topic} that {goal}.
Target length: {word_count} words.

# AUDIENCE
- Who: {audience}
- Knowledge level: {beginner/intermediate/expert}
- What they care about: {interests}
- What action you want them to take: {CTA}

# KEY MESSAGES
1. {message_1}
2. {message_2}
3. {message_3}

# TONE AND STYLE
- Tone: {professional/casual/academic/conversational}
- Vocabulary: {simple/technical/mixed}
- Sentence structure: {short_and_punchy/detailed_and_nuanced}
- Reference style: [Provide writing sample if available]

# CONSTRAINTS
- Do not include unverified statistics (use "approximately"
  or "research suggests" for general claims)
- Avoid {specific_things_to_avoid}
- Include {required_elements}
- Maximum {number} paragraphs

# FACTUAL GROUNDING
For any factual claims, use ONLY these verified facts:
{list_of_verified_facts}

# OUTPUT FORMAT
{Headline}
{Subheading}
{Body with specified structure}
{Call to action}

# QUALITY CHECK
□ Tone matches the specified style
□ Key messages are all addressed
□ No unverified factual claims
□ Word count is within range
□ Audience-appropriate language
```

---

### Template C: Code Generation

```markdown
# ROLE
You are a senior {language} developer specializing in
{area}. You write clean, well-documented, production-ready code.

# OBJECTIVE
Write {what_to_build} that {what_it_does}.

# TECHNICAL CONTEXT
- Language: {language} {version}
- Framework: {framework} {version}
- Dependencies: {list}
- Target environment: {environment}
- Style guide: {guide}

# REQUIREMENTS
Functional requirements:
1. {requirement_1}
2. {requirement_2}
3. {requirement_3}

Non-functional requirements:
- Performance: {expectations}
- Security: {requirements}
- Error handling: {approach}

# CONSTRAINTS
- Use ONLY standard library and listed dependencies
- Do not use deprecated functions or features
- Handle all edge cases (list known edge cases: {list})
- Include type hints/annotations
- Maximum function length: {number} lines

# EXISTING CODE CONTEXT
The new code must integrate with:
```{language}
{existing_code_or_interfaces}
```

# OUTPUT FORMAT
```{language}
# Module docstring explaining purpose

# Imports

# Constants

# Functions/Classes with docstrings

# Example usage
```

## Explanation
[What the code does and design decisions]

## Testing
[How to test this code]

## Known Limitations
[What this code does not handle]

# QUALITY CHECK
□ Code is syntactically correct
□ All requirements are addressed
□ Edge cases are handled
□ Code is well-documented
□ No deprecated features used
□ Compatible with specified versions
```

---

### Template D: Research and Analysis

```markdown
# ROLE
You are a research analyst providing evidence-based analysis.

# OBJECTIVE
Analyze {topic} and provide {output_type} for {audience}.

# RESEARCH QUESTION
{specific_question}

# SOURCE MATERIALS
{Provide all source materials with clear labels}

# INSTRUCTIONS
1. Review all provided sources
2. Extract relevant findings from each source
3. Synthesize findings across sources
4. Identify areas of agreement and disagreement
5. Assess the strength of evidence
6. Draw conclusions supported by the evidence
7. Identify gaps in the available evidence

# CONSTRAINTS
- Use ONLY the provided source materials
- Distinguish between strong evidence, moderate evidence,
  and weak evidence
- Note when sources disagree and present both sides
- Do not fabricate citations or statistics
- Mark any inference or extrapolation clearly

# OUTPUT FORMAT
## Research Question
[Restate the question]

## Evidence Summary
| Source | Key Finding | Evidence Strength | Relevance |
|--------|------------|-------------------|-----------|
| {source} | {finding} | Strong/Moderate/Weak | H/M/L |

## Synthesis
[What the evidence collectively suggests]

## Areas of Disagreement
[Where sources conflict and why]

## Conclusions
[Evidence-supported conclusions only]

## Evidence Gaps
[What additional evidence would be needed]

## Confidence Assessment
[Overall confidence in the conclusions: High/Medium/Low]

# QUALITY CHECK
□ Every claim traces to a specific source
□ Evidence strength is accurately characterized
□ Disagreements are fairly presented
□ Conclusions do not exceed the evidence
□ Gaps are honestly acknowledged
```

---

## Part 4: Context Optimization Checklist

Before sending any prompt, run through this checklist:

```markdown
# Context Optimization Checklist

## Structure
□ Role is specific and relevant
□ Objective is clear and SMART
□ Instructions are numbered and actionable
□ Constraints are explicit and prioritized
□ Output format is defined
□ Critical instructions appear at beginning AND end

## Content
□ All necessary information is included
□ No irrelevant information is included
□ Source material is clearly delimited
□ Data is formatted for easy parsing (tables, lists)
□ Examples are provided for ambiguous tasks

## Anti-Hallucination
□ Source restriction instruction included (if applicable)
□ "Say I don't know" permission included
□ Citation rules specified
□ Uncertainty marking instructions included
□ Quality check reminder at the end

## Efficiency
□ No redundant information
□ Compressed where possible without losing meaning
□ Signal-to-noise ratio is high (>70% relevant content)
□ Within token budget
□ Most important info at beginning and end (not middle)
```

---

## Part 5: Context Size Planning

### Token Budget Calculator

```
Model context window:         _______ tokens
Reserved for response:       -_______ tokens
Reserved for system prompt:  -_______ tokens
                             ─────────────────
Available for user context:   _______ tokens

Allocate:
  Role + Objective:          _______ tokens (2-5%)
  Instructions + Constraints: _______ tokens (3-8%)
  Source material:           _______ tokens (50-80%)
  Examples:                  _______ tokens (5-15%)
  Format + Quality check:    _______ tokens (2-5%)
                             ─────────────────
  Total allocated:           _______ tokens
  Remaining buffer:          _______ tokens
```

### When Context Exceeds Budget

Priority order for cuts:
1. Remove irrelevant examples (keep 1-2 best)
2. Compress background context (summarize)
3. Reduce source material (extract relevant sections only)
4. Simplify instructions (combine similar constraints)
5. Never cut: Role, Objective, critical constraints, output format

---

*Part of Module 09: Managing Hallucinations and AI Limitations*
