# Bias Detection Checklist

## Module 09: Code and Examples

A comprehensive checklist for identifying and mitigating biases in AI outputs. Use this as a practical tool during content review.

---

## How to Use This Checklist

1. Generate your AI output
2. Run through the relevant sections of this checklist
3. For each item, mark: PASS / FLAG / FAIL
4. For any FLAGS or FAILS, apply the corresponding mitigation
5. Regenerate or edit as needed
6. Document your findings for future reference

---

## Section 1: Language and Framing Bias

### Check the Language Used

| # | Check Item | Status | Notes |
|---|-----------|--------|-------|
| 1.1 | Is the language gender-neutral where gender is irrelevant? | | |
| 1.2 | Are descriptors balanced? (e.g., not using "aggressive" for men and "assertive" for women in the same context) | | |
| 1.3 | Are cultural terms used respectfully and accurately? | | |
| 1.4 | Is person-first language used where appropriate? (e.g., "person with a disability" vs. "disabled person") | | |
| 1.5 | Are loaded or politically charged terms avoided where neutrality is needed? | | |
| 1.6 | Is the vocabulary level consistent and appropriate for the audience? | | |
| 1.7 | Are euphemisms or hedging used unevenly across topics? | | |

### Mitigation Prompt
```markdown
Review the following text for language bias. Identify
any words or phrases that:
1. Assume a particular gender when none is specified
2. Use different descriptors for similar behaviors
   based on implied demographics
3. Use loaded or non-neutral language where objectivity
   is needed
4. Could be perceived as disrespectful by any group

For each issue, suggest a neutral alternative.

TEXT:
"""
{your_text}
"""
```

---

## Section 2: Representation Bias

### Check Who Is Represented

| # | Check Item | Status | Notes |
|---|-----------|--------|-------|
| 2.1 | Are multiple cultural perspectives included? | | |
| 2.2 | If people are mentioned/described, is there demographic diversity? | | |
| 2.3 | Are examples drawn from diverse contexts? (not just Western/American) | | |
| 2.4 | Are experts/authorities cited from diverse backgrounds? | | |
| 2.5 | Are non-Western contributions acknowledged where relevant? | | |
| 2.6 | Is there geographic diversity in examples and data? | | |
| 2.7 | Are different age groups and abilities represented? | | |

### Check What Is Represented

| # | Check Item | Status | Notes |
|---|-----------|--------|-------|
| 2.8 | Are both success stories and challenges/failures included? | | |
| 2.9 | Are alternative viewpoints presented, not just mainstream? | | |
| 2.10 | Are traditional/indigenous knowledge systems acknowledged where relevant? | | |
| 2.11 | Is the topic presented with appropriate complexity (not oversimplified)? | | |
| 2.12 | Are historical narratives inclusive of multiple perspectives? | | |

### Mitigation Prompt
```markdown
Review the following text for representation bias.

1. What demographic groups are represented? What groups
   are missing?
2. What geographic regions are referenced? What regions
   are absent?
3. What perspectives are presented? What perspectives
   are missing?
4. Are successes and failures both represented, or just one?

For each gap identified, suggest additions that would
make the content more representative.

TEXT:
"""
{your_text}
"""
```

---

## Section 3: Default Assumption Bias

### Check for Hidden Defaults

| # | Check Item | Status | Notes |
|---|-----------|--------|-------|
| 3.1 | Does the output assume a particular cultural context as "normal"? | | |
| 3.2 | When gender is unspecified, does the output default to one gender? | | |
| 3.3 | Does the output assume a particular socioeconomic background? | | |
| 3.4 | Does the output assume English-speaking or Western context? | | |
| 3.5 | Does the output assume a particular education level? | | |
| 3.6 | Does the output assume urban/suburban context vs. rural? | | |
| 3.7 | Does the output assume a particular family structure? | | |
| 3.8 | Does the output assume a particular religious or secular context? | | |
| 3.9 | Does the output assume a particular level of technology access? | | |
| 3.10 | Does the output assume able-bodied or neurotypical users? | | |

### Detection Technique: The Assumption Audit
```markdown
Read the following text and list every implicit assumption
it makes about the reader or subject. Assumptions can be
about:
- Culture and nationality
- Gender and family structure
- Socioeconomic status
- Education level
- Technology access
- Physical and cognitive ability
- Religious or philosophical background
- Geographic location (urban/rural)
- Language and communication norms

For each assumption, explain:
1. Where in the text it appears
2. Why it is an assumption (not a stated fact)
3. Who would be excluded by this assumption
4. How to make the text more inclusive

TEXT:
"""
{your_text}
"""
```

---

## Section 4: Confirmation and Framing Bias

### Check for One-Sided Framing

| # | Check Item | Status | Notes |
|---|-----------|--------|-------|
| 4.1 | Does the output present the topic from only one perspective? | | |
| 4.2 | Are counterarguments given equal treatment? | | |
| 4.3 | Is the framing of the question influencing the answer unfairly? | | |
| 4.4 | Are "both sides" presented even when one side is not scientifically supported? (false balance) | | |
| 4.5 | Are nuances and complexities acknowledged? | | |
| 4.6 | Does the output simply agree with the user's stated position? (sycophancy) | | |
| 4.7 | Are qualifiers used appropriately? ("some researchers suggest" vs. "research proves") | | |

### Detection Technique: The Flip Test
```markdown
Step 1: Read the original output and identify the main
position or framing.

Step 2: Rewrite the original prompt to argue the opposite
position.

Step 3: Compare the two outputs:
- Does the AI argue each position with equal vigor?
- Are the same sources and evidence types used?
- Is the language equally confident/cautious?
- Are the same types of qualifiers used?

If the outputs are dramatically different in quality,
depth, or conviction, framing bias is present.
```

### Mitigation Prompt
```markdown
Rewrite the following text to present a more balanced view:

1. Identify the primary perspective currently presented
2. Identify 2-3 credible alternative perspectives
3. Give each perspective proportional treatment based on
   evidence strength (not equal treatment if evidence is unequal)
4. Clearly distinguish between well-supported views and
   minority opinions
5. Let the reader form their own conclusion

TEXT:
"""
{your_text}
"""
```

---

## Section 5: Omission Bias

### Check for What Is Missing

| # | Check Item | Status | Notes |
|---|-----------|--------|-------|
| 5.1 | Are important caveats or limitations mentioned? | | |
| 5.2 | Are risks and downsides addressed (not just benefits)? | | |
| 5.3 | Are relevant historical context and origins included? | | |
| 5.4 | Are affected parties beyond the primary audience considered? | | |
| 5.5 | Are ethical implications discussed where relevant? | | |
| 5.6 | Is the time period or context clearly stated? | | |
| 5.7 | Are competing theories or approaches mentioned? | | |
| 5.8 | Are sources of uncertainty acknowledged? | | |

### Detection Technique: The Completeness Audit
```markdown
Review the following text and identify what is NOT said
that should be:

1. MISSING PERSPECTIVES: What viewpoints are absent?
2. MISSING CONTEXT: What background information would
   change the reader's understanding?
3. MISSING CAVEATS: What limitations or qualifications
   should be added?
4. MISSING RISKS: What downsides or risks are not mentioned?
5. MISSING STAKEHOLDERS: Whose concerns are not represented?
6. MISSING HISTORY: What relevant historical context is absent?
7. MISSING DATA: What data would the reader need to form
   their own opinion?

For each omission, rate its importance:
- CRITICAL: The text is misleading without this
- IMPORTANT: The text is incomplete without this
- NICE TO HAVE: Would improve but is not essential

TEXT:
"""
{your_text}
"""
```

---

## Section 6: Stereotyping Bias

### Check for Stereotypes

| # | Check Item | Status | Notes |
|---|-----------|--------|-------|
| 6.1 | Are professional roles described without gender stereotyping? | | |
| 6.2 | Are cultural groups described without reductive stereotypes? | | |
| 6.3 | Are age groups described without ageist assumptions? | | |
| 6.4 | Are nationalities described without national stereotypes? | | |
| 6.5 | Are socioeconomic groups described without class-based assumptions? | | |
| 6.6 | Are descriptions of people based on individual characteristics, not group membership? | | |
| 6.7 | Are historical groups described with appropriate complexity? | | |

### Detection Technique: The Specificity Test
```markdown
For every description of a person or group in the text,
check whether the description:

1. Could apply to anyone in that role/position (generic)
   or is it specific to a particular demographic?
2. Focuses on individual qualities or group stereotypes?
3. Would be different if the person's gender, ethnicity,
   or background were changed?
4. Reinforces a common stereotype, even subtly?
5. Uses loaded adjectives that imply judgment?

If any description fails these tests, rewrite it to be
based on individual, observable characteristics rather
than assumed group traits.

TEXT:
"""
{your_text}
"""
```

---

## Section 7: Data and Statistical Bias

### Check Data-Related Claims

| # | Check Item | Status | Notes |
|---|-----------|--------|-------|
| 7.1 | Are statistics attributed to specific, verifiable sources? | | |
| 7.2 | Are sample populations described? (Who was studied?) | | |
| 7.3 | Are limitations of cited studies acknowledged? | | |
| 7.4 | Are correlations distinguished from causation? | | |
| 7.5 | Are absolute numbers used alongside percentages for context? | | |
| 7.6 | Are data ranges or confidence intervals provided where appropriate? | | |
| 7.7 | Is the time period of data clearly stated? | | |
| 7.8 | Are outliers or edge cases acknowledged? | | |
| 7.9 | Could the selected data points create a misleading impression? | | |

### Mitigation Prompt
```markdown
Review the following text for data and statistical bias:

1. For each statistic cited:
   - Is the source named?
   - Is the sample population described?
   - Is the time period stated?
   - Are limitations acknowledged?

2. For each claim of correlation or causation:
   - Is the relationship correctly characterized?
   - Are alternative explanations mentioned?
   - Is the evidence strength noted?

3. For the overall data narrative:
   - Does the selected data tell a complete story?
   - Is contradictory data acknowledged?
   - Could a different selection of data points tell
     a different story?

TEXT:
"""
{your_text}
"""
```

---

## Section 8: Quick Bias Scan (5-Minute Version)

When you do not have time for the full checklist, run this quick scan:

```markdown
# 5-MINUTE BIAS SCAN

Read through the output and answer YES or NO:

□ Does the output assume a Western/American default? [Y/N]
□ Does the output assume a particular gender? [Y/N]
□ Is only one perspective presented? [Y/N]
□ Are stereotypes present (even subtle ones)? [Y/N]
□ Is something important obviously missing? [Y/N]
□ Would someone from a different cultural background
  find this incomplete or offensive? [Y/N]

If ANY answer is YES → Apply relevant mitigation from
the detailed sections above.

If ALL answers are NO → Proceed (but note that this
quick scan may miss subtle issues).
```

---

## Section 9: Domain-Specific Bias Checklists

### For Hiring/HR Content

```
□ Job descriptions use gender-neutral language
□ Requirements focus on skills, not backgrounds
□ No "culture fit" language that could exclude
□ Varied example candidates in scenarios
□ Accommodations and accessibility mentioned
□ No age-coded language ("digital native," "energetic")
□ No unnecessary physical requirements
```

### For Healthcare Content

```
□ Conditions described across demographic groups
□ Social determinants of health acknowledged
□ Cultural practices respected, not pathologized
□ Health disparities mentioned where relevant
□ Person-first language used
□ Access barriers acknowledged
□ Not assuming a particular healthcare system
```

### For Education Content

```
□ Diverse examples and case studies
□ Multiple learning styles acknowledged
□ No assumptions about home environment
□ Accessibility considerations included
□ Diverse contributors and experts cited
□ Cultural examples are varied and respectful
□ No assumptions about parental involvement
```

### For Technology Content

```
□ Not assuming high-speed internet access
□ Not assuming latest hardware
□ Accessibility features discussed
□ Privacy implications considered
□ Multiple platforms and devices represented
□ Global context considered (not just Silicon Valley)
□ Open source alternatives mentioned alongside paid
```

### For Financial Content

```
□ Multiple income levels considered
□ Global financial systems represented
□ Not assuming bank access or credit access
□ Cultural attitudes toward money respected
□ Informal economies acknowledged where relevant
□ Regulatory differences across jurisdictions noted
□ Not assuming a particular tax system
```

---

## Section 10: Bias Severity and Response Guide

| Severity | Description | Response |
|----------|-------------|----------|
| **Critical** | Could cause harm, discrimination, or exclusion | Must fix before using. Regenerate with strong debiasing instructions. |
| **Major** | Significantly one-sided or stereotyping | Should fix. Edit the output or regenerate with corrections. |
| **Moderate** | Missing perspectives or subtle defaults | Ideally fix. Add missing perspectives or context. |
| **Minor** | Slight imbalance that does not mislead | Note for improvement. Consider fixing in final version. |
| **Informational** | Not bias per se, but worth monitoring | Log for pattern tracking. May indicate systemic issues over many outputs. |

---

## Section 11: Tracking and Reporting

### Bias Tracking Log

```markdown
| Date | Output Type | Bias Found | Severity | Category | Mitigation Applied | Effective? |
|------|------------|------------|----------|----------|-------------------|------------|
| {date} | {type} | {description} | {C/Mj/Mo/Mi/I} | {section #} | {what you did} | {Y/N} |
```

### Monthly Bias Report Template

```markdown
# Monthly AI Bias Audit Report — {Month Year}

## Summary
- Total outputs reviewed: {number}
- Outputs with bias detected: {number} ({percentage})
- Critical biases found: {number}
- Most common bias type: {type}

## Breakdown by Category
| Category | Occurrences | % of Total | Trend |
|----------|------------|-----------|-------|
| Language/Framing | {n} | {%} | Up/Down/Stable |
| Representation | {n} | {%} | Up/Down/Stable |
| Default Assumptions | {n} | {%} | Up/Down/Stable |
| Confirmation/Framing | {n} | {%} | Up/Down/Stable |
| Omission | {n} | {%} | Up/Down/Stable |
| Stereotyping | {n} | {%} | Up/Down/Stable |
| Data/Statistical | {n} | {%} | Up/Down/Stable |

## Most Effective Mitigations
1. {mitigation and why it works}
2. {mitigation and why it works}

## Recommendations for Next Month
1. {recommendation}
2. {recommendation}
3. {recommendation}
```

---

*Part of Module 09: Managing Hallucinations and AI Limitations*
