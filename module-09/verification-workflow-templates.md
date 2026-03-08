# Verification Workflow Templates

## Module 09: Code and Examples

Complete verification workflow templates for different content types. Each template is ready to use and adapt for your specific context.

---

## Template 1: General Factual Content Verification

### Use Case
Blog posts, articles, informational content, general reports.

### Workflow

```
┌─────────────────────────────────┐
│ STAGE 1: AI GENERATION          │
│                                 │
│ Generate content with these     │
│ instructions appended:          │
│ "Mark uncertain claims with     │
│  [VERIFY]. Include confidence   │
│  scores for key facts."         │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│ STAGE 2: AUTOMATED PRE-CHECK   │
│                                 │
│ Run self-verification prompt    │
│ (see below)                     │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│ STAGE 3: CLAIM EXTRACTION       │
│                                 │
│ Extract all verifiable claims   │
│ into a checklist                │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│ STAGE 4: HUMAN VERIFICATION     │
│                                 │
│ Verify top-priority claims      │
│ against authoritative sources   │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│ STAGE 5: CORRECTION             │
│                                 │
│ Fix errors, flag unverifiable   │
│ claims, add caveats             │
└─────────────┬───────────────────┘
              │
              ▼
┌─────────────────────────────────┐
│ STAGE 6: FINAL REVIEW           │
│                                 │
│ Read through complete output    │
│ for coherence after corrections │
└─────────────────────────────────┘
```

### Self-Verification Prompt (Stage 2)

```markdown
You are a fact-checker. Review the following AI-generated text
and identify potential issues.

TEXT:
"""
{generated_text}
"""

REVIEW CHECKLIST:
1. List every specific factual claim (dates, numbers, names, events)
2. For each, rate confidence: HIGH / MEDIUM / LOW
3. Identify any claims that are:
   - Potentially outdated
   - Suspiciously specific (exact percentages, precise dates)
   - Lacking attributed sources
   - Potentially confused with similar facts
4. Check for internal contradictions
5. Check for logical consistency

OUTPUT FORMAT:
| # | Claim | Confidence | Issue | Recommendation |
|---|-------|------------|-------|----------------|
```

### Claim Extraction Prompt (Stage 3)

```markdown
Extract all verifiable claims from the following text.
A "verifiable claim" is any statement that can be checked
against an external source.

TEXT:
"""
{generated_text}
"""

For each claim, provide:
1. The exact claim (quoted from text)
2. Type: Date / Number / Name / Event / Relationship / Attribution
3. Priority: HIGH (critical to the content's message) /
   MEDIUM (supporting detail) / LOW (minor detail)

List in order of priority (HIGH first).
```

### Verification Log Template

```markdown
# Verification Log

Date: {date}
Content: {content title or description}
Reviewer: {name}

| # | Claim | Priority | Verified? | Source Used | Action |
|---|-------|----------|-----------|-------------|--------|
| 1 | {claim} | HIGH | Yes/No/Partial | {source} | {keep/fix/remove} |
| 2 | {claim} | HIGH | Yes/No/Partial | {source} | {keep/fix/remove} |
| 3 | {claim} | MEDIUM | Yes/No/Partial | {source} | {keep/fix/remove} |

Total claims: {number}
Verified correct: {number} ({percentage})
Corrected: {number}
Removed: {number}
Unverifiable: {number}

Overall assessment: {PASS / PASS WITH CAVEATS / FAIL}
Time spent: {minutes}
```

---

## Template 2: Technical Documentation Verification

### Use Case
API documentation, code tutorials, technical guides, software documentation.

### Workflow

```
┌──────────────────────────────────┐
│ STAGE 1: GENERATE DOCUMENTATION  │
│                                  │
│ With grounding in actual code,   │
│ API specs, or system config      │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 2: CODE VERIFICATION       │
│                                  │
│ Test every code example          │
│ Verify API endpoints exist       │
│ Check parameter names/types      │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 3: VERSION VERIFICATION    │
│                                  │
│ Confirm all features exist in    │
│ the specified version            │
│ Check for deprecated items       │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 4: ACCURACY REVIEW         │
│                                  │
│ Developer/engineer reviews       │
│ technical accuracy               │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 5: USABILITY REVIEW        │
│                                  │
│ Someone unfamiliar with the      │
│ system follows the documentation │
└──────────────────────────────────┘
```

### Technical Verification Prompt

```markdown
You are a senior developer reviewing technical documentation.
Check the following documentation for technical accuracy.

DOCUMENTATION:
"""
{generated_documentation}
"""

SPECIFIED TECHNOLOGY AND VERSION:
- Language/Framework: {name} {version}
- Dependencies: {list}
- Environment: {environment}

VERIFICATION CHECKLIST:
1. CODE EXAMPLES
   □ Syntactically correct?
   □ Will they actually run?
   □ Do they use the correct API for the specified version?
   □ Are there any missing imports or dependencies?
   □ Are error handling patterns correct?

2. API/FUNCTION REFERENCES
   □ Do the named functions/methods exist?
   □ Are parameters correctly named and typed?
   □ Are return values correctly described?
   □ Are any deprecated features referenced?

3. CONFIGURATION
   □ Are configuration keys and values correct?
   □ Are file paths and environment variables correct?
   □ Are default values accurately stated?

4. CONCEPTS
   □ Are technical concepts explained correctly?
   □ Are architecture descriptions accurate?
   □ Are best practices current?

OUTPUT:
For each issue found:
- Location: {line or section}
- Issue type: {syntax/api/concept/deprecated/missing}
- Current text: "{quote}"
- Correction: "{corrected text}"
- Severity: {Critical/Major/Minor}
```

### Code Example Test Template

```markdown
# Code Example Verification

## Example {number}: {title}

### Code
```{language}
{code_from_documentation}
```

### Test Method
- [ ] Pasted into IDE/editor
- [ ] Dependencies installed ({list})
- [ ] Executed successfully
- [ ] Output matches documentation

### Result
- [ ] PASS - works as documented
- [ ] PARTIAL - works with modifications: {modifications}
- [ ] FAIL - does not work: {error_message}

### Corrections needed
{corrections or "None"}
```

---

## Template 3: Medical/Health Content Verification

### Use Case
Health articles, patient education materials, clinical summaries.

### Workflow

```
┌──────────────────────────────────┐
│ STAGE 1: GENERATE WITH GROUNDING │
│                                  │
│ Provide clinical guidelines as   │
│ source material. Include:        │
│ "For educational purposes only.  │
│  Not medical advice."            │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 2: SAFETY SCREEN           │
│                                  │
│ Check for potentially dangerous  │
│ misinformation:                  │
│ - Wrong dosages                  │
│ - Incorrect contraindications    │
│ - Missing safety warnings        │
│ - Inappropriate self-treatment   │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 3: CLINICAL ACCURACY       │
│                                  │
│ Medical professional reviews:    │
│ - Diagnosis accuracy             │
│ - Treatment correctness          │
│ - Guideline compliance           │
│ - Current standard of care       │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 4: COMMUNICATION REVIEW    │
│                                  │
│ Health literacy check:           │
│ - Appropriate language level     │
│ - No misleading implications     │
│ - Proper disclaimers included    │
│ - Cultural sensitivity           │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 5: COMPLIANCE CHECK        │
│                                  │
│ Legal/regulatory compliance:     │
│ - Appropriate disclaimers        │
│ - No unauthorized health claims  │
│ - Privacy considerations         │
└──────────────────────────────────┘
```

### Medical Safety Screen Prompt

```markdown
You are a medical safety reviewer. Examine the following
health-related content for potentially dangerous information.

FLAG AS CRITICAL if the content:
- Contains specific medication dosages (verify against guidelines)
- Recommends stopping prescribed medications
- Suggests diagnoses without recommending professional consultation
- Contains incorrect contraindications or drug interactions
- Minimizes serious symptoms that should receive medical attention
- Provides treatment recommendations without appropriate caveats

FLAG AS IMPORTANT if the content:
- Makes claims about treatment effectiveness without evidence level
- Uses absolute language ("always," "never," "cures")
- Omits important side effects or risks
- Could lead to delays in seeking appropriate care

CONTENT:
"""
{generated_health_content}
"""

SAFETY REPORT:
| Issue | Location | Severity | Current Text | Recommendation |
|-------|----------|----------|-------------|----------------|
```

---

## Template 4: Legal Content Verification

### Use Case
Legal summaries, regulatory explanations, compliance content.

### Workflow

```
┌──────────────────────────────────┐
│ STAGE 1: GENERATE WITH SOURCES   │
│                                  │
│ Provide actual statutes, codes,  │
│ or regulations as source text.   │
│ Include jurisdiction and date.   │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 2: CITATION VERIFICATION   │
│                                  │
│ Verify every legal citation:     │
│ - Case names and numbers         │
│ - Statute sections               │
│ - Regulatory references          │
│ - Court and jurisdiction         │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 3: LEGAL ACCURACY          │
│                                  │
│ Licensed attorney reviews:       │
│ - Correct statement of law       │
│ - Appropriate jurisdiction       │
│ - Current legal status           │
│ - No misleading simplifications  │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 4: DISCLAIMER CHECK        │
│                                  │
│ Verify appropriate disclaimers:  │
│ - Not legal advice               │
│ - Consult an attorney            │
│ - Jurisdiction-specific caveats  │
│ - Date-specific caveats          │
└──────────────────────────────────┘
```

### Legal Citation Verification Prompt

```markdown
Review the following legal content and verify all citations.

CONTENT:
"""
{generated_legal_content}
"""

For EACH legal citation or reference, verify:

| # | Citation | Type | Exists? | Accurate? | Current? | Notes |
|---|----------|------|---------|-----------|----------|-------|
| 1 | {citation} | Case/Statute/Reg | Y/N/Uncertain | Y/N/Uncertain | Y/N/Uncertain | {notes} |

CRITICAL FLAGS:
- Any citation that does not appear to exist → [FABRICATED]
- Any citation where the stated holding is wrong → [MISREPRESENTED]
- Any statute that has been amended or repealed → [OUTDATED]
- Any case that has been overruled → [OVERRULED]

DISCLAIMER CHECK:
□ "This is not legal advice" disclaimer present?
□ "Consult an attorney" recommendation present?
□ Jurisdiction clearly specified?
□ Date of information clearly stated?
```

---

## Template 5: Financial Content Verification

### Use Case
Financial reports, market analysis, investment information.

### Workflow

```
┌──────────────────────────────────┐
│ STAGE 1: GENERATE WITH DATA      │
│                                  │
│ Provide actual financial data    │
│ from verified sources.           │
│ Specify "no external data"       │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 2: MATHEMATICAL VERIFY     │
│                                  │
│ Recalculate all derived metrics  │
│ (growth rates, ratios, margins)  │
│ using the raw data provided      │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 3: DATA SOURCE CHECK       │
│                                  │
│ Verify any market data, indices, │
│ or benchmarks cited against      │
│ authoritative financial sources  │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 4: COMPLIANCE REVIEW       │
│                                  │
│ Check for:                       │
│ - Forward-looking statements     │
│ - Required disclaimers           │
│ - Appropriate qualifiers         │
│ - No unauthorized recommendations│
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 5: EXPERT SIGN-OFF         │
│                                  │
│ Financial professional reviews   │
│ methodology and conclusions      │
└──────────────────────────────────┘
```

### Financial Calculation Verification Prompt

```markdown
Verify all calculations in the following financial content.

CONTENT:
"""
{generated_financial_content}
"""

RAW DATA PROVIDED:
{the_original_data}

For EACH calculated figure in the content:

| # | Stated Value | Calculation | Recalculated Value | Match? | Difference |
|---|-------------|-------------|-------------------|--------|------------|
| 1 | {stated} | {formula} | {recalculated} | Y/N | {diff} |

Also flag:
- Numbers stated as fact but not derivable from provided data
- Industry benchmarks or comparisons not in the original data
- Projections or forecasts presented as fact
- Misleading representations of data

CRITICAL: Any number that does not match the recalculated
value or is not traceable to the provided data should be
flagged as [UNVERIFIED].
```

---

## Template 6: Academic/Research Content Verification

### Use Case
Literature reviews, research summaries, academic writing.

### Workflow

```
┌──────────────────────────────────┐
│ STAGE 1: GENERATE WITH SOURCES   │
│                                  │
│ Provide actual papers/sources.   │
│ Instruct: "Cite only these."    │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 2: CITATION VERIFICATION   │
│                                  │
│ Every citation must be verified: │
│ - Author names correct           │
│ - Title exact                    │
│ - Year correct                   │
│ - Journal/publisher correct      │
│ - DOI/URL valid                  │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 3: CLAIM-SOURCE ALIGNMENT  │
│                                  │
│ Does each cited source actually  │
│ support the claim made?          │
│ Check actual paper, not just     │
│ the abstract.                    │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 4: METHODOLOGY CHECK       │
│                                  │
│ Are research methods accurately  │
│ described? Are limitations noted?│
│ Is the evidence strength         │
│ appropriately characterized?     │
└──────────────┬───────────────────┘
               │
               ▼
┌──────────────────────────────────┐
│ STAGE 5: PEER REVIEW             │
│                                  │
│ Domain expert reviews for:       │
│ - Accuracy of interpretations    │
│ - Missing important literature   │
│ - Appropriate conclusions        │
└──────────────────────────────────┘
```

### Academic Citation Verification Prompt

```markdown
Verify every citation in the following text. For each one:

1. Search for the exact paper title
2. Verify the author names
3. Verify the publication venue and year
4. Determine if the paper actually supports the claim made

TEXT:
"""
{generated_academic_text}
"""

CITATION VERIFICATION TABLE:
| # | Cited As | Real? | Authors Match? | Year Match? | Supports Claim? | Notes |
|---|----------|-------|---------------|-------------|-----------------|-------|
| 1 | {citation} | Y/N/Uncertain | Y/N | Y/N | Y/N/Partially | {notes} |

FLAG KEY:
[FABRICATED] - Citation does not appear to exist
[CHIMERIC] - Combines real elements (e.g., real author, fake title)
[MISATTRIBUTED] - Paper exists but does not support the claim made
[OUTDATED] - Cited paper has been superseded by newer research
[ACCURATE] - Citation fully verified
```

---

## Workflow Selection Guide

| Content Type | Template | Minimum Review Level | Estimated Time |
|-------------|----------|---------------------|----------------|
| Blog post / Article | Template 1 | Stages 1-4 | 30-60 min |
| Technical docs | Template 2 | Stages 1-5 | 60-120 min |
| Health content | Template 3 | ALL stages | 120+ min |
| Legal content | Template 4 | ALL stages | 120+ min |
| Financial content | Template 5 | ALL stages | 90-120 min |
| Academic content | Template 6 | ALL stages | 120+ min |
| Internal notes | Template 1 (stages 1-3 only) | Stages 1-3 | 15-30 min |

---

*Part of Module 09: Managing Hallucinations and AI Limitations*
