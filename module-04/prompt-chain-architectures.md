# Prompt Chain Architectures: 5 Complete Systems

## Module 04 Code Examples

---

## Overview

This document presents five complete prompt chain architectures with ASCII diagrams, full prompts for each step, data flow specifications, and error handling. Each architecture solves a different real-world problem.

---

## Architecture 1: Content Creation Pipeline

### Purpose
Transform a topic into a polished, SEO-optimized blog post through a multi-stage pipeline.

### Architecture Diagram

```
+------------------+
| INPUT: Topic +   |
| Keywords + Tone  |
+--------+---------+
         |
+--------v---------+
| STEP 1: RESEARCH |
| & OUTLINE        |
| (Analytical)     |
+--------+---------+
         |
+--------v---------+
| STEP 2: DRAFT    |
| GENERATION       |
| (Creative)       |
+--------+---------+
         |
+--------v---------+     +--YES---> Step 2 (regenerate
| STEP 3: QUALITY  |     |          flagged sections)
| REVIEW           +--+--+
| (Critical)       |  |
+--------+---------+  +--NO (passed)
         |                    |
+--------v--------------------v
| STEP 4: SEO OPTIMIZATION    |
| (Technical)                  |
+--------+--------------------+
         |
+--------v---------+
| STEP 5: FINAL    |
| POLISH & FORMAT  |
| (Editorial)      |
+--------+---------+
         |
+--------v---------+
| OUTPUT: Complete  |
| Blog Post         |
+------------------+
```

### Step-by-Step Prompts

**Step 1: Research and Outline**

```
You are a content strategist. Create a detailed outline for
a blog post.

TOPIC: {{topic}}
TARGET KEYWORDS: {{keywords}}
TONE: {{tone}}
TARGET AUDIENCE: {{audience}}
TARGET LENGTH: {{word_count}} words

Produce:

1. TITLE OPTIONS (3 compelling titles)
   - Title A: [informational style]
   - Title B: [curiosity-driven style]
   - Title C: [benefit-focused style]

2. OUTLINE
   - Introduction hook (2-3 approaches)
   - Main sections (4-6 sections with sub-points)
   - Key data points or statistics to include
   - Conclusion approach

3. KEYWORD INTEGRATION PLAN
   - Primary keyword placement: [where in the post]
   - Secondary keywords: [where to naturally include]

4. UNIQUE ANGLE
   - What makes this post different from existing content?
   - What unique insight or perspective will you offer?

OUTPUT FORMAT: Structured outline in markdown
```

**Step 2: Draft Generation**

```
You are an expert content writer. Write the full blog post
based on this outline.

SELECTED TITLE: {{chosen_title}}
OUTLINE: {{step1_output}}
TONE: {{tone}}
TARGET LENGTH: {{word_count}} words

WRITING GUIDELINES:
- Open with a compelling hook (question, statistic, or story)
- Use short paragraphs (3-4 sentences max)
- Include subheadings every 200-300 words
- Write in active voice
- Use transition words between sections
- Include at least one list or table for scannability
- End with a clear call-to-action

Write the complete post now. Mark any claims that need
fact-checking with [VERIFY: claim].
```

**Step 3: Quality Review**

```
You are a senior editor. Review this blog post critically.

POST:
"""
{{step2_output}}
"""

EVALUATE ON THESE CRITERIA:

1. ACCURACY: Flag any claims marked [VERIFY] or any
   potentially incorrect statements. For each:
   Status: ACCURATE / NEEDS VERIFICATION / INCORRECT
   Suggestion: [how to fix or verify]

2. FLOW: Does the post read smoothly from start to finish?
   Issues: [list any choppy transitions or logical gaps]

3. ENGAGEMENT: Rate the hook, body, and conclusion:
   Hook: [compelling / adequate / weak]
   Body: [engaging / adequate / dry]
   Conclusion: [strong / adequate / weak]

4. COMPLETENESS: Does it cover the topic adequately?
   Missing aspects: [list anything important that is missing]

5. TONE CONSISTENCY: Does it maintain the target tone throughout?
   Issues: [any sections that deviate from target tone]

VERDICT: PASS / NEEDS REVISION

If NEEDS REVISION, provide specific revision instructions
for each issue found.
```

**Step 4: SEO Optimization**

```
You are an SEO specialist. Optimize this blog post for search
engines while maintaining readability.

POST: {{step3_approved_output}}
TARGET KEYWORDS: {{keywords}}

OPTIMIZE:

1. TITLE TAG: Rewrite the title for SEO (under 60 characters,
   include primary keyword)

2. META DESCRIPTION: Write a compelling meta description
   (under 160 characters, include primary keyword, include
   a call-to-action)

3. HEADING OPTIMIZATION: Review all H2 and H3 tags.
   Suggest improvements for keyword inclusion.

4. KEYWORD DENSITY: Check primary keyword appears 3-5 times
   naturally. If not, suggest where to add it.

5. INTERNAL LINKING: Suggest 2-3 places where internal links
   could be added (use placeholder: [INTERNAL LINK: topic])

6. IMAGE ALT TEXT: Suggest 3 image placements with SEO-
   optimized alt text.

7. READABILITY SCORE: Estimate the Flesch-Kincaid grade level.
   If above 8th grade, suggest simplifications.

Output the optimized post with all changes applied.
```

**Step 5: Final Polish**

```
You are a copy editor performing a final review. Polish this
post for publication.

POST: {{step4_output}}

FINAL CHECKS:
1. Fix any grammar, spelling, or punctuation errors
2. Ensure consistent formatting (heading levels, list styles)
3. Verify all [VERIFY] tags have been resolved (remove tags)
4. Ensure [INTERNAL LINK] placeholders are clearly marked
5. Add a table of contents if the post exceeds 1500 words
6. Format the final output in clean markdown

Output the publication-ready blog post.
```

### Data Flow Specification

```
Step 1 Input:  {topic, keywords, tone, audience, word_count}
Step 1 Output: {title_options[], outline, keyword_plan, unique_angle}

Step 2 Input:  {chosen_title, outline, tone, word_count}
Step 2 Output: {full_draft_text}

Step 3 Input:  {full_draft_text}
Step 3 Output: {verdict, issues[], revised_text OR revision_instructions}

Step 4 Input:  {approved_text, keywords}
Step 4 Output: {seo_optimized_text, meta_title, meta_description}

Step 5 Input:  {seo_optimized_text}
Step 5 Output: {final_publication_ready_text}
```

---

## Architecture 2: Multi-Language Customer Email Handler

### Purpose
Process incoming customer emails in any language, analyze intent, generate contextual responses, and translate back.

### Architecture Diagram

```
+-------------------+
| INPUT: Customer   |
| Email (any lang)  |
+--------+----------+
         |
+--------v----------+
| STEP 1: DETECT    |
| LANGUAGE &        |
| TRANSLATE         |
+--------+----------+
         |
+--------v----------+     +--------v----------+
| STEP 2: ANALYZE   |     | (parallel)        |
| INTENT &          |     | STEP 2B: SENTIMENT|
| EXTRACT ENTITIES  |     | ANALYSIS          |
+--------+----------+     +--------+----------+
         |                          |
         +------------+-------------+
                      |
         +------------v-------------+
         | STEP 3: ROUTE TO         |
         | APPROPRIATE HANDLER      |
         +--+------+------+------+--+
            |      |      |      |
         +--v--+ +-v--+ +-v--+ +-v--+
         |BILL | |TECH| |ACCT| |GEN |
         |ING  | |    | |    | |    |
         +--+--+ +--+-+ +--+-+ +--+-+
            |       |      |      |
            +---+---+---+--+------+
                |
         +------v-----------+
         | STEP 4: GENERATE |
         | RESPONSE         |
         +------+-----------+
                |
         +------v-----------+
         | STEP 5: TRANSLATE |
         | BACK TO ORIGINAL |
         | LANGUAGE          |
         +------+-----------+
                |
         +------v-----------+
         | STEP 6: QUALITY  |
         | CHECK & SEND     |
         +------------------+
```

### Step-by-Step Prompts

**Step 1: Language Detection and Translation**

```
Analyze the following email:

EMAIL:
"""
{{customer_email}}
"""

1. DETECT the language of this email.
2. If NOT English, TRANSLATE it to English preserving:
   - Formal/informal tone
   - Emotional intensity
   - Any names, order numbers, or reference codes (do not translate these)
3. Note any cultural context that may affect how we respond.

OUTPUT:
{
  "detected_language": "language_code",
  "language_name": "English name of language",
  "original_text": "original email",
  "english_text": "translated text (or original if already English)",
  "tone": "formal/informal/angry/neutral/friendly",
  "cultural_notes": "any relevant cultural context"
}
```

**Step 2A: Intent Analysis and Entity Extraction**

```
Analyze this customer email and extract structured information.

EMAIL (English):
"""
{{english_text}}
"""

EXTRACT:
{
  "primary_intent": "one of: complaint, question, request, feedback,
                     cancellation, return, purchase, other",
  "secondary_intents": ["any additional intents"],
  "entities": {
    "order_id": "if mentioned",
    "product_name": "if mentioned",
    "date_referenced": "if mentioned",
    "amount_mentioned": "if mentioned",
    "person_name": "if mentioned"
  },
  "urgency": "low/medium/high/critical",
  "category": "billing/technical/account/general",
  "key_issue_summary": "one sentence summary of the core issue"
}
```

**Step 2B: Sentiment Analysis (parallel with 2A)**

```
Analyze the emotional tone of this customer email.

EMAIL:
"""
{{english_text}}
"""

{
  "overall_sentiment": "very_negative/negative/neutral/positive/very_positive",
  "frustration_level": 1-10,
  "satisfaction_risk": "low/medium/high (risk of losing this customer)",
  "emotional_cues": ["list specific phrases indicating emotion"],
  "empathy_approach": "recommended empathy strategy for the response"
}
```

**Steps 3-6 follow the same pattern, each with focused, specific prompts.**

---

## Architecture 3: Code Review Pipeline

### Architecture Diagram

```
+------------------+
| INPUT: Code Diff |
| (Pull Request)   |
+--------+---------+
         |
+--------v---------+      +--------v---------+
| STEP 1: PARSE &  |      | (parallel)       |
| CATEGORIZE       |      | STEP 1B: CHECK   |
| CHANGES          |      | STYLE/LINTING    |
+--------+---------+      +--------+---------+
         |                          |
+--------v---------+                |
| STEP 2: LOGIC    |                |
| & CORRECTNESS    |                |
| REVIEW           |                |
+--------+---------+                |
         |                          |
+--------v---------+                |
| STEP 3: SECURITY |                |
| REVIEW           |                |
+--------+---------+                |
         |                          |
+--------v---------+                |
| STEP 4: PERF     |                |
| REVIEW           |                |
+--------+---------+                |
         |                          |
         +-----------+--------------+
                     |
         +-----------v-----------+
         | STEP 5: SYNTHESIZE   |
         | REVIEW COMMENTS      |
         +-----------+-----------+
                     |
         +-----------v-----------+
         | STEP 6: GENERATE     |
         | PR REVIEW            |
         +----------------------+
```

### Key Prompts

**Step 2: Logic and Correctness Review**

```
You are a senior software engineer reviewing code for
logical correctness.

CODE CHANGES:
"""
{{parsed_diff}}
"""

CONTEXT: {{file_context}}

Review for:

1. LOGIC ERRORS
   - Off-by-one errors
   - Null/undefined handling
   - Edge cases not handled
   - Race conditions
   - Incorrect conditional logic

2. CORRECTNESS
   - Does the code do what the PR description says?
   - Are there unintended side effects?
   - Are return values correct in all paths?

3. ERROR HANDLING
   - Are exceptions caught appropriately?
   - Are error messages helpful?
   - Is there proper cleanup in error paths?

For each issue found:
{
  "file": "filename",
  "line": line_number,
  "severity": "critical/major/minor/suggestion",
  "category": "logic/correctness/error_handling",
  "description": "what the issue is",
  "suggestion": "how to fix it",
  "code_example": "suggested code if applicable"
}
```

**Step 3: Security Review**

```
You are a security engineer reviewing code for vulnerabilities.

CODE CHANGES:
"""
{{parsed_diff}}
"""

CHECK FOR:

1. INJECTION VULNERABILITIES
   - SQL injection
   - Command injection
   - XSS (cross-site scripting)
   - Template injection

2. AUTHENTICATION/AUTHORIZATION
   - Missing auth checks
   - Privilege escalation
   - Insecure token handling

3. DATA EXPOSURE
   - Sensitive data in logs
   - PII handling issues
   - Hardcoded secrets or credentials

4. DEPENDENCY SECURITY
   - Known vulnerable dependencies
   - Untrusted input to system calls

For each vulnerability found:
{
  "file": "filename",
  "line": line_number,
  "severity": "critical/high/medium/low",
  "vulnerability_type": "category",
  "description": "detailed description",
  "cwe_id": "CWE-XXX if applicable",
  "remediation": "how to fix",
  "code_example": "secure alternative code"
}
```

---

## Architecture 4: Meeting Minutes to Action Items Pipeline

### Architecture Diagram

```
+--------------------+
| INPUT: Meeting     |
| Transcript/Notes   |
+--------+-----------+
         |
+--------v-----------+
| STEP 1: STRUCTURE  |
| Identify speakers, |
| topics, timeline   |
+--------+-----------+
         |
+--------v-----------+     +----------v----------+
| STEP 2: EXTRACT    |     | (parallel)          |
| DECISIONS &        |     | STEP 2B: EXTRACT    |
| KEY POINTS         |     | ACTION ITEMS        |
+--------+-----------+     +----------+----------+
         |                             |
         +------------+----------------+
                      |
         +------------v-----------+
         | STEP 3: ASSIGN &       |
         | PRIORITIZE ACTIONS     |
         +------------+-----------+
                      |
         +------------v-----------+
         | STEP 4: GENERATE       |
         | MEETING SUMMARY        |
         +------------+-----------+
                      |
         +------------v-----------+
         | STEP 5: FORMAT FOR     |
         | DISTRIBUTION           |
         | (Email + Ticket system)|
         +------------------------+
```

### Key Prompts

**Step 2B: Extract Action Items**

```
You are a project manager extracting action items from meeting notes.

MEETING NOTES:
"""
{{structured_notes}}
"""

For EACH action item, extract:

{
  "action_items": [
    {
      "id": "AI-001",
      "description": "Clear, specific description of what needs to be done",
      "owner": "Person's name (or 'Unassigned' if not clear)",
      "deadline": "Date mentioned or 'TBD'",
      "priority": "high/medium/low",
      "context": "Brief context from the discussion",
      "dependencies": ["list any prerequisites"],
      "deliverable": "What the output of this action should be",
      "mentioned_by": "Who raised this action",
      "verbatim_quote": "The exact words from the meeting that
                         generated this action item"
    }
  ]
}

RULES:
- Only extract EXPLICIT action items (someone agreed to do something)
- Do NOT infer action items that were not clearly stated
- If ownership is unclear, mark as "Unassigned" and flag
- If deadline is unclear, mark as "TBD" and flag
- Include enough context that someone who was not in the meeting
  understands the action item
```

---

## Architecture 5: Automated Report Generator

### Purpose
Transform raw data into an executive-ready report with analysis, visualizations, and recommendations.

### Architecture Diagram

```
+--------------------+
| INPUT: Raw Data +  |
| Report Parameters  |
+--------+-----------+
         |
+--------v-----------+
| STEP 1: DATA       |
| PROFILING &        |
| VALIDATION         |
+--------+-----------+
         |
    +----+----+----+----+
    |         |         |
+---v---+ +--v----+ +--v----+
| STEP  | | STEP  | | STEP  |
| 2A:   | | 2B:   | | 2C:   |
| TREND | | COMP- | | ANOM- |
| ANAL. | | ARISON| | ALIES |
+---+---+ +---+---+ +---+---+
    |         |         |
    +----+----+----+----+
         |
+--------v-----------+
| STEP 3: INSIGHT    |
| SYNTHESIS          |
+--------+-----------+
         |
+--------v-----------+
| STEP 4: GENERATE   |
| RECOMMENDATIONS    |
+--------+-----------+
         |
+--------v-----------+
| STEP 5: COMPOSE    |
| EXECUTIVE REPORT   |
+--------+-----------+
         |
+--------v-----------+
| STEP 6: EXECUTIVE  |
| SUMMARY & FORMAT   |
+------------------+-+
         |
+--------v-----------+
| OUTPUT: Complete   |
| Executive Report   |
+--------------------+
```

### Key Prompts

**Step 3: Insight Synthesis**

```
You are a senior business analyst synthesizing findings from
multiple analyses into coherent insights.

TREND ANALYSIS:
{{step2a_output}}

COMPARATIVE ANALYSIS:
{{step2b_output}}

ANOMALY DETECTION:
{{step2c_output}}

REPORT PARAMETERS:
- Period: {{reporting_period}}
- Audience: {{audience}}
- Focus Areas: {{focus_areas}}

SYNTHESIZE:

1. KEY INSIGHTS (prioritized by business impact):

   Insight 1: [Title]
   - Finding: [What the data shows]
   - Significance: [Why it matters]
   - Confidence: [How reliable this finding is]
   - Supported by: [Which analyses support this]

   Insight 2: [Title]
   [Same structure]

   [Continue for top 5-7 insights]

2. NARRATIVE THREAD:
   What is the overall story the data tells?
   [2-3 paragraph narrative connecting the insights]

3. AREAS OF CONCERN:
   [Specific metrics or trends that warrant attention]

4. POSITIVE DEVELOPMENTS:
   [Specific metrics or trends that show improvement]

5. DATA GAPS:
   [What the data does NOT tell us that we should investigate]
```

**Step 4: Generate Recommendations**

```
You are a strategic advisor generating actionable recommendations
based on data insights.

INSIGHTS:
{{step3_output}}

CONTEXT:
- Organization type: {{org_type}}
- Current priorities: {{priorities}}
- Known constraints: {{constraints}}

GENERATE RECOMMENDATIONS:

For each recommendation:

### Recommendation [N]: [Title]

**What**: [Specific action to take]
**Why**: [Which insight(s) drive this recommendation]
**Expected Impact**: [Quantified if possible]
**Effort Required**: [Low / Medium / High]
**Timeline**: [Quick win / Medium-term / Long-term]
**Risk if NOT implemented**: [What happens if we do nothing]
**Dependencies**: [What needs to happen first]
**Success Metric**: [How to measure if this worked]

PRIORITIZATION MATRIX:

| Recommendation | Impact | Effort | Priority |
|---------------|--------|--------|----------|
| Rec 1 | H/M/L | H/M/L | 1-N |
| Rec 2 | H/M/L | H/M/L | 1-N |

TOP 3 ACTIONS (if leadership only has time for three things):
1. [Most critical recommendation]
2. [Second most critical]
3. [Third most critical]
```

---

## Cross-Architecture Patterns

### Error Handling Pattern (Used in All Architectures)

```
IF step output is malformed:
  RETRY with: "Your previous output was not in the expected
  format. Please reformat following this structure: {{format}}"
  MAX RETRIES: 2

IF step output fails quality check:
  ROUTE TO: Revision step with specific feedback
  MAX REVISIONS: 2

IF step times out:
  FALLBACK TO: Simplified version of the step
  NOTIFY: Include a note in final output that this section
  used simplified processing

IF entire chain fails:
  RETURN: Partial results with clear indication of which
  stages completed successfully and which did not
```

### Monitoring Pattern (Used in All Architectures)

```
For each step, log:
{
  "chain_id": "unique_run_identifier",
  "step": "step_number_and_name",
  "start_time": "timestamp",
  "end_time": "timestamp",
  "tokens_used": number,
  "input_size": number,
  "output_size": number,
  "quality_score": number_or_null,
  "retries": number,
  "status": "success/failure/partial"
}
```
