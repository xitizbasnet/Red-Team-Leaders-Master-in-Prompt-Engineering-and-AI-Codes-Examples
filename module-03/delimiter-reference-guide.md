# Delimiter Reference Guide

## Module 03 — Code and Examples

---

A complete reference for all delimiter types used in prompt engineering, with syntax, use cases, best practices, and examples for each.

---

## Quick Reference Table

| Delimiter | Syntax | Best For | Supported By |
|-----------|--------|----------|-------------|
| Triple Quotes | `"""..."""` | Text passages | All models |
| Triple Backticks | ` ``` ``` ` | Code blocks | All models |
| XML Tags | `<tag>...</tag>` | Structured sections | All (Claude excels) |
| Single Backticks | `` `...` `` | Inline code/terms | All models |
| Square Brackets | `[...]` | Placeholders | All models |
| Curly Braces | `{...}` | Template variables | All models |
| Angle Brackets | `<...>` | Placeholders | All models |
| Dashes/Separators | `---` | Section breaks | All models |
| Hash Headers | `# ## ###` | Section hierarchy | All models |
| Pipe Tables | `\|...\|` | Tabular data | All models |
| Parentheses | `(...)` | Inline notes | All models |
| Blockquotes | `> ...` | Quoted content | All models |
| Bold/Italic | `**...**` / `*...*` | Emphasis | All models |
| Numbered Lists | `1. 2. 3.` | Ordered items | All models |
| Bullet Lists | `- ...` | Unordered items | All models |

---

## 1. Triple Quotes (""")

### Syntax
```
"""
Content goes here.
Multiple lines are supported.
"""
```

### Best For
- Enclosing text passages for analysis
- Wrapping articles, emails, or documents
- Separating user-provided text from instructions

### Example
```
Summarize the following article in 3 sentences:

"""
The European Central Bank announced its decision to hold
interest rates steady at 4.5%, defying market expectations
of a cut. ECB President Christine Lagarde cited persistent
core inflation of 3.2% as the primary factor. Markets
reacted with a 0.8% drop in the Euro Stoxx 50 index.
"""
```

### Best Practices
- Use triple quotes for ANY text that the model should treat as input data
- They prevent the model from confusing quoted content with instructions
- Consistent opening and closing quotes (both triple)

### Common Mistakes
- Using single quotes (less clear boundary)
- Forgetting to close the quotes
- Placing instructions inside the quotes

---

## 2. Triple Backticks (```)

### Syntax
````
```language
code goes here
```
````

### Best For
- Code blocks (any programming language)
- Configuration files
- Command-line examples
- Any content that should be treated as literal/technical

### Example
````
Review the following Python function for performance issues:

```python
def find_duplicates(items):
    duplicates = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] == items[j] and items[i] not in duplicates:
                duplicates.append(items[i])
    return duplicates
```

Suggest an optimized version.
````

### Best Practices
- Always include the language identifier after opening backticks
- Use for any content that is technical or should be treated literally
- Use for expected output examples when the output is code

### Common Mistakes
- Omitting the language identifier
- Using backticks for non-code text (use triple quotes instead)
- Nesting backticks without escaping (use four backticks for the outer level)

---

## 3. XML Tags

### Syntax
```
<tag_name>
Content goes here.
</tag_name>
```

### Best For
- Multiple distinct sections in a prompt
- Structured data with clear semantic meaning
- Prompts with many different types of content
- Claude/Anthropic models (they are trained to handle XML well)

### Example
```
<instructions>
Analyze the following customer review and extract
structured feedback.
</instructions>

<review>
I bought the ProMax 3000 vacuum cleaner last month.
The suction power is incredible — much better than my
previous Dyson. However, the dust bin is too small and
needs emptying every 10 minutes. The cord is also too
short for my living room. Would recommend for small
apartments only.
</review>

<output_schema>
{
  "product": "string",
  "overall_sentiment": "positive|negative|mixed",
  "pros": ["string"],
  "cons": ["string"],
  "recommendation": "string",
  "rating_estimate": "1-5"
}
</output_schema>
```

### Best Practices
- Use descriptive tag names that indicate the content type
- Maintain consistent naming conventions (snake_case or camelCase)
- Nest tags for hierarchical structures
- Close all tags properly
- Claude models respond particularly well to XML-tagged prompts

### Advanced: Nested XML
```
<task>
  <context>
    You are reviewing code for a banking application.
  </context>
  <requirements>
    <security>Check for SQL injection and XSS vulnerabilities.</security>
    <performance>Identify any N+1 query issues.</performance>
    <style>Verify adherence to the team's style guide.</style>
  </requirements>
  <code language="python">
    [code here]
  </code>
</task>
```

### Common Mistakes
- Unclosed tags
- Inconsistent tag naming
- Overly generic tag names (`<data>` is less clear than `<customer_review>`)
- Using XML for simple prompts where it adds unnecessary complexity

---

## 4. Single Backticks

### Syntax
```
Use `inline code` within regular text.
```

### Best For
- Highlighting technical terms within prose
- Referencing function names, variable names, or commands
- Indicating that a word should be treated literally

### Example
```
Explain the difference between `let`, `const`, and `var`
in JavaScript. For each, provide:
- Scope behavior
- Reassignment rules
- Hoisting behavior
Include code examples demonstrating each.
```

### Best Practices
- Use for any technical term that should be treated literally
- Helps the model understand what is a keyword vs. natural language
- Use consistently throughout the prompt

---

## 5. Square Brackets

### Syntax
```
[placeholder_description]
```

### Best For
- Indicating where the user should fill in information
- Template placeholders
- Optional elements

### Example
```
Write a cover letter for the following:

Position: [Job Title]
Company: [Company Name]
Your Key Skills: [Skill 1], [Skill 2], [Skill 3]
Years of Experience: [Number]
Notable Achievement: [Brief description of achievement]
```

### Best Practices
- Use descriptive placeholder names
- Add type hints when helpful: `[number: 1-10]`, `[date: YYYY-MM-DD]`
- Distinguish required `[required_field]` from optional `[optional_field?]`

### Common Mistakes
- Using brackets in running text where they could be mistaken for placeholders
- Inconsistent placeholder naming

---

## 6. Curly Braces

### Syntax
```
{variable_name}
```

### Best For
- Template variables in programmatic contexts
- LangChain, Semantic Kernel, and similar frameworks
- Distinguishing variables from static text

### Example
```
You are a {role} at {company}.
Explain {topic} to a {audience} audience
in {language}.
Keep your response under {word_limit} words.
```

### Best Practices
- Standard in most LLM frameworks and libraries
- Use snake_case for variable names
- Distinguish from JSON/dictionary content by context
- Document all variables and their expected types

### Integration with Python
```python
template = """You are a {role}. Explain {topic} in {word_count} words."""
prompt = template.format(
    role="senior data scientist",
    topic="neural networks",
    word_count=200
)
```

---

## 7. Dashes and Horizontal Rules (---)

### Syntax
```
Section 1 content

---

Section 2 content
```

### Best For
- Visual separation between major sections
- Separating instructions from input
- Breaking up long prompts for readability

### Example
```
Instructions:
You are an editor. Review the following essay for grammar,
clarity, and structure. Provide specific feedback.

---

Essay to review:
The impact of social media on mental health has been widely
debated in recent years...

---

Output format:
1. Overall Assessment (1-2 sentences)
2. Grammar Issues (bulleted list)
3. Clarity Issues (bulleted list)
4. Structural Suggestions (numbered list)
```

### Best Practices
- Use three dashes minimum (`---`)
- Place on their own line with blank lines above and below
- Use consistently throughout the prompt
- Do not overuse — 2-4 separators per prompt is typical

---

## 8. Markdown Headers (# ## ###)

### Syntax
```
# Main Title (H1)
## Section (H2)
### Subsection (H3)
#### Sub-subsection (H4)
```

### Best For
- Organizing multi-section prompts
- Creating clear hierarchy in complex prompts
- System prompts with multiple components

### Example
```
# System Configuration

## Role
You are a senior marketing strategist.

## Task
Create a marketing plan for the following product.

## Product Details
- Name: CloudSync Pro
- Category: SaaS / Productivity
- Price: $29/month
- Target: Small business owners

## Deliverables
### Required
1. Target audience profile
2. Positioning statement
3. Three key messages

### Optional
4. Content calendar (1 month)
5. Budget allocation suggestion

## Constraints
- Focus on digital channels only
- Budget assumption: $10K/month
- Timeline: Launch in 6 weeks
```

### Best Practices
- Use H1 (`#`) only once per prompt (main title or system context)
- Use H2 (`##`) for major sections
- Use H3 (`###`) for subsections within those sections
- Maintain consistent hierarchy (do not skip levels)

---

## 9. Pipe Tables

### Syntax
```
| Column 1 | Column 2 | Column 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
```

### Best For
- Presenting structured data for analysis
- Specifying output format
- Comparison matrices
- Criteria definitions

### Example
```
Analyze the following sales data and identify the top performer:

| Salesperson | Q1 Sales | Q2 Sales | Q3 Sales | Q4 Sales |
|------------|----------|----------|----------|----------|
| Alice      | $45,000  | $52,000  | $48,000  | $61,000  |
| Bob        | $38,000  | $41,000  | $55,000  | $58,000  |
| Carol      | $51,000  | $49,000  | $53,000  | $50,000  |
| David      | $42,000  | $58,000  | $61,000  | $64,000  |

Return your analysis as:

| Metric | Alice | Bob | Carol | David |
|--------|-------|-----|-------|-------|
| Total  |       |     |       |       |
| Growth |       |     |       |       |
| Rank   |       |     |       |       |
```

### Best Practices
- Always include the header separator row (`|---|---|`)
- Align columns for readability (optional but helpful)
- Use for any data that has a clear tabular structure
- Specify whether you want the output in table format

---

## 10. Blockquotes

### Syntax
```
> This is a blockquote.
> It can span multiple lines.
```

### Best For
- Highlighting important notes or warnings
- Quoting source material
- Emphasizing key requirements

### Example
```
Write a response to the following customer email.

> Dear Support Team,
> I purchased a laptop from your store on January 15th
> and it stopped working after just two weeks. I am very
> disappointed with the quality and would like a full refund.
> Order number: #ORD-2025-0789
> Thank you,
> Maria

Respond with empathy, acknowledge the issue, and explain
the return process.
```

---

## 11. Numbered and Bullet Lists

### Syntax
```
Numbered:
1. First item
2. Second item
3. Third item

Bulleted:
- Item one
- Item two
- Item three
```

### Best For
- Step-by-step instructions
- Requirements lists
- Output structure specifications
- Priority orderings

### Example
```
Analyze the following code and provide feedback.

Your feedback must cover these areas in this order:
1. Security vulnerabilities (critical)
2. Performance issues (high priority)
3. Code readability (medium priority)
4. Style consistency (low priority)

For each issue found, include:
- The specific line or section
- What the problem is
- Why it matters
- How to fix it
```

---

## 12. Bold and Italic Emphasis

### Syntax
```
**Bold text** for strong emphasis
*Italic text* for light emphasis
***Bold italic*** for maximum emphasis
```

### Best For
- Highlighting key terms in instructions
- Emphasizing critical requirements
- Drawing attention to important constraints

### Example
```
Write a product description for a smartwatch.

**Critical requirements:**
- Must mention **battery life** in the first sentence
- Must include *at least 3* specific features
- Must **NOT** include pricing information
- Target audience: *health-conscious professionals aged 30-45*

The tone should be **informative** but not overly technical.
```

---

## Delimiter Combination Patterns

### Pattern 1: The Full-Structure Prompt
```
# Role and Context

You are a [role].

## Task

[Clear task description]

## Input

"""
[User-provided text content]
"""

## Constraints

- [Constraint 1]
- [Constraint 2]
- **Critical:** [Most important constraint]

## Output Format

| Field | Type | Required |
|-------|------|----------|
| ...   | ...  | ...      |

---

Provide your response below:
```

### Pattern 2: The XML-Structured Prompt
```
<system>
You are an expert in {domain}.
</system>

<task>
{task_description}
</task>

<input>
{user_input}
</input>

<constraints>
- {constraint_1}
- {constraint_2}
</constraints>

<output_format>
{format_specification}
</output_format>
```

### Pattern 3: The Code-Analysis Prompt
````
## Instructions
Review the following {language} code for {review_focus}.

## Code
```{language}
{code_block}
```

## Expected Behavior
"""
{expected_behavior_description}
"""

## Actual Behavior
"""
{actual_behavior_description}
"""

## Output Format
For each issue:
1. **Line:** [line number]
2. **Issue:** [description]
3. **Fix:**
```{language}
[corrected code]
```
````

### Pattern 4: The Data-Processing Prompt
```
<instructions>
Process the following data according to the rules below.
</instructions>

<rules>
1. [Rule 1]
2. [Rule 2]
3. [Rule 3]
</rules>

<data>
| Column A | Column B | Column C |
|----------|----------|----------|
| ...      | ...      | ...      |
</data>

<output>
Return the processed data as valid JSON:
{
  "results": [
    {"field1": "value", "field2": "value"}
  ],
  "summary": "string"
}
</output>
```

---

## Decision Guide: Which Delimiter to Use

```
Is the content code?
  YES -> Use triple backticks (```)
  NO  -> Continue

Is the content a text passage for analysis?
  YES -> Use triple quotes (""")
  NO  -> Continue

Do you have multiple distinct sections?
  YES -> Are you using Claude/API?
    YES -> Use XML tags (<tag>)
    NO  -> Use Markdown headers (## ##)
  NO  -> Continue

Is it a template variable?
  YES -> Use curly braces ({var})
  NO  -> Continue

Is it a placeholder for the user to fill in?
  YES -> Use square brackets ([placeholder])
  NO  -> Continue

Is it a key term or technical name?
  YES -> Use single backticks (`term`)
  NO  -> Continue

Do you need to emphasize something critical?
  YES -> Use bold (**text**)
  NO  -> Use plain text
```

---

## Common Anti-Patterns to Avoid

### Anti-Pattern 1: No Delimiters
```
BAD:
Summarize this the global economy showed signs of recovery in Q3

GOOD:
Summarize the following text:
"""
The global economy showed signs of recovery in Q3...
"""
```

### Anti-Pattern 2: Inconsistent Delimiters
```
BAD:
Instructions are in """triple quotes"""
Input is in <xml tags>
Output format uses ```backticks```
(Confusing mix)

GOOD:
Pick one system and be consistent, or use each delimiter
for its intended purpose.
```

### Anti-Pattern 3: Over-Delimiting
```
BAD:
"""
<instructions>
### Task:
**Summarize** the `text` below:
</instructions>
"""
(Too many layers of delimiting)

GOOD:
<instructions>
Summarize the following text in 3 sentences.
</instructions>

<text>
[content here]
</text>
```

---

*This reference is part of Module 03: Basic and Intermediate Prompt Techniques.*
