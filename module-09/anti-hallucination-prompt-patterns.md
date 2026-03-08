# Anti-Hallucination Prompt Patterns

## Module 09: Code and Examples

A comprehensive collection of 25 prompt patterns specifically designed to reduce hallucinations in AI outputs. Each pattern includes the template, usage context, effectiveness rating, and practical examples.

---

## How to Use This Guide

Each pattern follows this format:
- **Pattern Name** and description
- **Template**: The prompt text you can copy and adapt
- **When to Use**: The scenarios where this pattern is most effective
- **Effectiveness**: Rated from 1-5 stars based on practical experience
- **Example**: A concrete application of the pattern

---

## Category 1: Grounding Patterns

### Pattern 1: Source-Only Response

**Description**: Restricts the model to information in the provided source material.

**Template**:
```
Based ONLY on the following source material, answer the question below.

RULES:
- Use ONLY information from the provided text
- If the answer is not in the text, say "Not found in provided materials"
- Do not supplement with outside knowledge
- Quote relevant passages using quotation marks

SOURCE MATERIAL:
"""
{your_source_text}
"""

QUESTION: {your_question}
```

**When to Use**: Summarization, document Q&A, report generation from source materials.

**Effectiveness**: 5/5 stars — The most effective single technique when source material is available.

**Example**:
```
Based ONLY on the following source material, answer the question below.

RULES:
- Use ONLY information from the provided text
- If the answer is not in the text, say "Not found in provided materials"
- Do not supplement with outside knowledge

SOURCE MATERIAL:
"""
TechCorp Q3 2023 Results: Revenue reached $45.2M, up 23% YoY.
Operating expenses were $38.1M. Net income was $4.8M. Customer
count grew to 1,247 from 1,089 in Q3 2022.
"""

QUESTION: What was TechCorp's revenue growth rate?
```

---

### Pattern 2: Temporal Anchoring

**Description**: Makes the model aware of its knowledge limitations and time-sensitive gaps.

**Template**:
```
IMPORTANT CONTEXT:
- Today's date is {current_date}
- Your training data may not include events after {approximate_cutoff}
- If your answer involves information that may have changed
  since your training, explicitly state: "[POTENTIALLY OUTDATED]"
- For time-sensitive questions, recommend the user verify
  with current sources

QUESTION: {your_question}
```

**When to Use**: Any question about current events, recent data, or rapidly changing fields.

**Effectiveness**: 3/5 stars — Does not prevent hallucination but increases appropriate uncertainty markers.

---

### Pattern 3: Data-Grounded Analysis

**Description**: Anchors the analysis to specific provided data points.

**Template**:
```
Analyze the following data. Your analysis must:
1. Reference ONLY the numbers provided below
2. Show calculations for any derived metrics
3. Not introduce external benchmarks or comparisons
4. Flag any data gaps that limit the analysis

DATA:
{your_data}

ANALYSIS REQUESTED: {what_you_want_analyzed}

If you need additional data to complete the analysis,
list what is missing rather than estimating.
```

**When to Use**: Financial analysis, data reporting, statistical summaries.

**Effectiveness**: 4/5 stars — Very effective for numerical content.

---

## Category 2: Uncertainty and Honesty Patterns

### Pattern 4: Permission to Say "I Don't Know"

**Description**: Explicitly gives the model permission to express uncertainty.

**Template**:
```
Answer the following question honestly. It is completely
acceptable and preferred to say:
- "I don't know"
- "I'm not certain about this specific detail"
- "This may have changed since my training data"
- "I cannot verify this claim"

An honest expression of uncertainty is ALWAYS better than
a confident guess. You will not be penalized for admitting
the limits of your knowledge.

QUESTION: {your_question}
```

**When to Use**: Any factual query, especially about niche or recent topics.

**Effectiveness**: 4/5 stars — Significantly reduces fabrication by removing the incentive to guess.

---

### Pattern 5: Confidence Scoring

**Description**: Forces the model to self-assess the reliability of each claim.

**Template**:
```
Answer the following question. For each factual claim in
your response, append a confidence score:

[HIGH] = I am very confident this is correct
[MEDIUM] = I believe this is correct but cannot be certain
[LOW] = This is my best guess and should be verified
[UNSURE] = I am not confident in this claim at all

Prioritize accuracy over comprehensiveness. A shorter
response with all [HIGH] confidence claims is preferred
over a longer response with [LOW] confidence claims.

QUESTION: {your_question}
```

**When to Use**: Research queries, factual summaries, any task where accuracy is critical.

**Effectiveness**: 3/5 stars — Useful but the model's self-assessment is not perfectly calibrated.

---

### Pattern 6: Fact vs. Inference Separator

**Description**: Forces the model to clearly distinguish facts from inferences.

**Template**:
```
Respond to the following query. Structure your response
into three clearly labeled sections:

VERIFIED FACTS: [Statements you are highly confident are
factually correct]

REASONABLE INFERENCES: [Conclusions you are drawing from
those facts — label the reasoning]

SPECULATION: [Ideas that are plausible but that you cannot
verify — clearly mark as speculative]

QUESTION: {your_question}
```

**When to Use**: Analysis tasks, research assistance, advisory outputs.

**Effectiveness**: 4/5 stars — Effective at preventing speculation from being presented as fact.

---

### Pattern 7: Boundary Acknowledgment

**Description**: Has the model explicitly identify the limits of its knowledge.

**Template**:
```
Before answering, briefly identify:
1. What you know with high confidence about this topic
2. What you know with moderate confidence
3. What falls outside your reliable knowledge
4. What may have changed since your training data

Then provide your answer, staying within your high and
moderate confidence zones. Explicitly note where you are
approaching the boundaries of your reliable knowledge.

QUESTION: {your_question}
```

**When to Use**: Complex queries spanning multiple knowledge areas.

**Effectiveness**: 3/5 stars — Helpful for framing but does not prevent all hallucination.

---

## Category 3: Verification and Self-Check Patterns

### Pattern 8: Chain-of-Verification (CoVe)

**Description**: Has the model verify its own claims through self-questioning.

**Template**:
```
Step 1: Answer the following question.
Step 2: List every factual claim in your answer (numbered list).
Step 3: For each claim, ask yourself: "Am I certain this is
correct? What is my basis for this claim?"
Step 4: For any claim where you are less than 90% confident,
mark it with [UNVERIFIED] and explain why.
Step 5: Provide a REVISED answer that either removes or
flags all unverified claims.

QUESTION: {your_question}

Provide Steps 1 through 5 in order.
```

**When to Use**: High-stakes factual queries where accuracy is critical.

**Effectiveness**: 4/5 stars — One of the most effective self-correction techniques.

---

### Pattern 9: Dual-Response Comparison

**Description**: Generates two independent responses and compares them.

**Template**:
```
Generate two independent responses to this question:

RESPONSE A: Your first answer.
RESPONSE B: A second answer that takes a different approach
or emphasis.

COMPARISON:
- Where do both responses agree? (Higher confidence)
- Where do they disagree? (Lower confidence — flag for verification)
- Which claims appear in only one response? (May be hallucinated)

FINAL ANSWER: A synthesized response that includes only
the claims that both responses support, with disagreements
flagged.

QUESTION: {your_question}
```

**When to Use**: Research queries, factual analysis where cross-verification is important.

**Effectiveness**: 3/5 stars — Limited by the fact that both responses come from the same model.

---

### Pattern 10: Falsification Challenge

**Description**: Has the model attempt to disprove its own claims.

**Template**:
```
Answer the following question.

Then, for each major claim in your answer, try to think
of evidence or arguments that would CONTRADICT it.

If you can easily think of contradicting evidence for a
claim, either:
a) Revise the claim to be more nuanced
b) Remove the claim if it is not well-supported
c) Present both sides if the topic is genuinely debated

QUESTION: {your_question}
```

**When to Use**: Opinion-adjacent topics, analysis, recommendations.

**Effectiveness**: 3/5 stars — Good for nuance but may not catch specific factual hallucinations.

---

### Pattern 11: Multi-Pass Review

**Description**: Forces multiple review passes of the initial response.

**Template**:
```
Process this request in four passes:

PASS 1 (DRAFT): Write your initial response.
PASS 2 (ACCURACY CHECK): Review every factual claim.
Mark any uncertain claims with [CHECK].
PASS 3 (LOGIC CHECK): Verify that all reasoning is sound
and conclusions follow from evidence.
PASS 4 (FINAL): Present the cleaned-up, verified response
with all uncertain claims either verified, removed, or
clearly flagged.

Show me only the PASS 4 result, but mention how many
claims you flagged in PASS 2 and how many you resolved.

QUESTION: {your_question}
```

**When to Use**: Any task where the final output will be used without further review.

**Effectiveness**: 4/5 stars — Multiple review passes catch more errors than single generation.

---

## Category 4: Constraint Patterns

### Pattern 12: Vocabulary Restriction

**Description**: Limits the model to specific approved terminology.

**Template**:
```
Answer using ONLY the following approved terminology:
{list_of_approved_terms}

If you need to express a concept not covered by this
vocabulary, use the phrase "TERM NOT IN APPROVED LIST:
[your term]" and explain why it is necessary.

Do not use synonyms or alternative phrasings for the
approved terms.

QUESTION: {your_question}
```

**When to Use**: Regulated industries, technical documentation, compliance content.

**Effectiveness**: 4/5 stars — Very effective for domain-specific content.

---

### Pattern 13: Format Constraint

**Description**: Restricts output to a specific format that limits fabrication opportunity.

**Template**:
```
Answer this question using ONLY the following format.
Each field is required. If you cannot fill a field
accurately, write "UNKNOWN" rather than guessing.

ANSWER FORMAT:
- Main claim: [one sentence]
- Supporting evidence: [cite specific source or say "General knowledge"]
- Confidence level: [High/Medium/Low]
- Key caveat: [most important limitation of this answer]
- Verification suggestion: [how the reader could verify this]
```

**When to Use**: Structured reporting, Q&A systems, knowledge base entries.

**Effectiveness**: 4/5 stars — The structure forces accountability for each component.

---

### Pattern 14: Conservative Response Mode

**Description**: Instructs the model to prioritize accuracy over completeness.

**Template**:
```
Adopt CONSERVATIVE RESPONSE MODE:
- State ONLY what you are highly confident about
- Leave out anything that might be inaccurate, even if
  it makes the response less complete
- Use ranges instead of precise numbers when uncertain
  (e.g., "approximately 40-50%" instead of "47.3%")
- Use hedging language for anything that is not well-established
- Err on the side of saying less rather than saying something wrong

A shorter, fully accurate response is MUCH better than
a longer response with potential inaccuracies.

QUESTION: {your_question}
```

**When to Use**: Any high-stakes factual query.

**Effectiveness**: 4/5 stars — Trades completeness for accuracy, which is often the right tradeoff.

---

### Pattern 15: Extraction-Only Mode

**Description**: Restricts the model to extracting information from provided text.

**Template**:
```
You are in EXTRACTION-ONLY MODE. Your only job is to extract
information from the provided text.

YOU MAY:
- Quote directly from the text
- Paraphrase content from the text
- Organize information from the text

YOU MAY NOT:
- Add information not in the text
- Make inferences beyond what is explicitly stated
- Fill gaps with outside knowledge
- Speculate about what the text might mean

If the requested information is not in the text, respond
with "Not present in the provided text."

TEXT:
"""
{your_text}
"""

EXTRACTION REQUEST: {what_to_extract}
```

**When to Use**: Document summarization, data extraction, content analysis.

**Effectiveness**: 5/5 stars — Highly effective because it eliminates the generation mode entirely.

---

## Category 5: Citation and Attribution Patterns

### Pattern 16: No Fabrication Citation Rule

**Description**: Explicitly prohibits fabricated citations.

**Template**:
```
For any claims in your response that would benefit from
a citation:

1. If you can provide a REAL, specific citation you are
   confident exists, provide it
2. If you cannot provide a specific citation, write:
   "[Source needed — verify independently]"
3. NEVER fabricate a citation. A missing citation is
   infinitely better than a fake one

Apply this rule to ALL of the following:
- Academic papers
- Books
- URLs/websites
- Statistics and data
- Named studies or reports
- Quotes attributed to specific people

QUESTION: {your_question}
```

**When to Use**: Any task requiring citations or references.

**Effectiveness**: 4/5 stars — Significantly reduces citation fabrication, though some may still occur.

---

### Pattern 17: Quote Verification

**Description**: Forces accountability when quoting someone.

**Template**:
```
If you include any direct quotes in your response:

1. Provide the attributed speaker/author
2. Provide the source where the quote appeared
3. Rate your confidence that this is the EXACT wording:
   [Exact] [Approximate] [Paraphrased]
4. If you are not confident in the exact wording, use
   indirect speech instead of quotation marks

NEVER put words in quotation marks unless you are
confident those are the actual words used.

QUESTION: {your_question}
```

**When to Use**: Content that includes quotes, biographical writing, journalism.

**Effectiveness**: 4/5 stars — Very effective at reducing misattributed quotes.

---

## Category 6: Role and Persona Patterns

### Pattern 18: The Skeptical Expert

**Description**: Assigns a persona that naturally resists hallucination.

**Template**:
```
You are a senior fact-checker at a major news organization.
Your professional reputation depends on never publishing
unverified information. You would rather publish nothing
than publish something that might be wrong.

Apply this level of rigor to the following question.
For every claim, ask yourself: "Would I stake my
professional reputation on this being correct?"

If the answer is "no," either verify it, caveat it,
or remove it.

QUESTION: {your_question}
```

**When to Use**: Any factual content where accuracy is paramount.

**Effectiveness**: 3/5 stars — The persona influences but does not guarantee behavior.

---

### Pattern 19: The Peer Reviewer

**Description**: Frames the task as producing content for expert review.

**Template**:
```
Write your response as if it will be immediately reviewed
by three domain experts who will challenge every claim.
These reviewers are:
1. An expert in {specific_field}
2. A methodologist who checks reasoning and evidence quality
3. A fact-checker who verifies every specific claim

Your response should be able to withstand scrutiny from
all three reviewers. If you include a claim that would
not survive expert review, remove it or flag it.

QUESTION: {your_question}
```

**When to Use**: Technical writing, academic content, professional reports.

**Effectiveness**: 3/5 stars — Raises the quality bar but does not eliminate hallucination.

---

## Category 7: Structured Output Patterns

### Pattern 20: The Evidence Table

**Description**: Forces every claim into a structured evidence format.

**Template**:
```
Answer the following question using ONLY this table format.
Every claim must be entered as a row:

| Claim | Evidence | Source | Confidence | Verified? |
|-------|----------|--------|------------|-----------|
| [statement] | [supporting evidence] | [where you learned this] | [H/M/L] | [Y/N/Uncertain] |

After the table, provide a narrative summary using ONLY
the claims rated H or M confidence and Y or Uncertain
for verified.

Do NOT include any claim in the narrative that is rated
L confidence or N for verified.

QUESTION: {your_question}
```

**When to Use**: Research summaries, evidence reviews, decision support.

**Effectiveness**: 4/5 stars — The structure makes unsupported claims visible.

---

### Pattern 21: The Decision Matrix

**Description**: For analytical tasks, forces structured comparison.

**Template**:
```
Analyze the following using this exact matrix structure.
Fill each cell based ONLY on information you are confident
about. Use "Insufficient data" for any cell you cannot
fill reliably.

| Criterion | Option A | Option B | Option C | Confidence |
|-----------|----------|----------|----------|------------|
| {criterion_1} | | | | H/M/L |
| {criterion_2} | | | | H/M/L |
| {criterion_3} | | | | H/M/L |

"Insufficient data" is always better than a fabricated cell value.

QUESTION: {your_question}
```

**When to Use**: Comparison tasks, decision support, evaluations.

**Effectiveness**: 4/5 stars — Empty cells are more honest than fabricated ones.

---

## Category 8: Meta-Cognitive Patterns

### Pattern 22: Think Before You Speak

**Description**: Forces the model to plan before generating.

**Template**:
```
Before answering, complete this pre-flight check:

1. COMPREHENSION: Restate the question in your own words
   to confirm you understand it correctly.
2. KNOWLEDGE ASSESSMENT: Rate your knowledge of this topic
   (Expert / Knowledgeable / Basic / Limited).
3. RISK ASSESSMENT: What types of hallucinations are most
   likely for this type of question?
4. STRATEGY: How will you ensure accuracy? What will you
   be extra careful about?

Then provide your answer with these safeguards in mind.

QUESTION: {your_question}
```

**When to Use**: Complex queries requiring careful handling.

**Effectiveness**: 3/5 stars — The metacognitive step catches some issues.

---

### Pattern 23: The Assumption Explicator

**Description**: Forces the model to make implicit assumptions explicit.

**Template**:
```
Answer the following question. Before your answer, list
every assumption you are making. For each assumption,
note whether it is:
- Stated by the user (explicit)
- Reasonable to assume (implicit but justified)
- An assumption you are making due to incomplete information
  (flag for user confirmation)

After listing assumptions, provide your answer. The reader
should be able to evaluate whether your assumptions are
valid for their specific situation.

QUESTION: {your_question}
```

**When to Use**: Advisory tasks, analysis, recommendations.

**Effectiveness**: 4/5 stars — Making assumptions explicit prevents hidden biases and errors.

---

### Pattern 24: The Socratic Self-Interrogation

**Description**: Has the model question its own response.

**Template**:
```
Answer the following question. Then interrogate your own
response with these questions:

1. "What would someone who disagrees with this say?"
2. "What evidence would change my answer?"
3. "Am I stating this more confidently than warranted?"
4. "What am I assuming that might not be true?"
5. "Is there a simpler or more likely explanation?"

Revise your answer based on this self-interrogation.

QUESTION: {your_question}
```

**When to Use**: Analysis, recommendations, complex factual queries.

**Effectiveness**: 3/5 stars — Adds nuance and catches some overconfident claims.

---

### Pattern 25: The Comprehensive Safety Net

**Description**: Combines multiple anti-hallucination techniques into one pattern.

**Template**:
```
SAFETY NET MODE ACTIVATED. Apply ALL of the following rules:

1. SOURCE RULE: Base claims on provided sources when available.
   Mark external knowledge with [GENERAL KNOWLEDGE].
2. CONFIDENCE RULE: Append [HIGH], [MEDIUM], or [LOW]
   confidence to each factual claim.
3. CITATION RULE: Never fabricate citations. Use
   "[Source needed]" when you cannot provide one.
4. UNCERTAINTY RULE: Say "I'm not certain" when appropriate.
   It is always preferred over guessing.
5. PRECISION RULE: Use ranges for uncertain numbers.
   Use hedging for uncertain claims.
6. VERIFICATION RULE: After your response, list the top 3
   claims that the reader should verify independently.
7. COMPLETENESS RULE: Note what you have NOT covered that
   might be relevant.

QUESTION: {your_question}
```

**When to Use**: Any high-stakes task. This is the "maximum protection" pattern.

**Effectiveness**: 5/5 stars — Combining multiple techniques provides the strongest protection, though it produces more verbose output.

---

## Quick Reference: Pattern Selection Guide

| Situation | Recommended Patterns |
|-----------|---------------------|
| Document summarization | #1, #15, #6 |
| Factual Q&A | #4, #5, #8, #14 |
| Research with citations | #16, #17, #8, #20 |
| Data analysis | #3, #12, #21 |
| Technical writing | #19, #11, #12 |
| Advisory/recommendations | #6, #23, #24 |
| High-stakes content | #25, #8, #11, #16 |
| Creative but grounded | #6, #7, #14 |
| Quick, low-risk queries | #4, #5 |

---

## Effectiveness Summary

| Rating | Patterns |
|--------|----------|
| 5 stars | #1 (Source-Only), #15 (Extraction-Only), #25 (Comprehensive) |
| 4 stars | #3, #4, #6, #8, #11, #12, #13, #14, #16, #17, #20, #21, #23 |
| 3 stars | #2, #5, #7, #9, #10, #18, #19, #22, #24 |

---

*Part of Module 09: Managing Hallucinations and AI Limitations*
