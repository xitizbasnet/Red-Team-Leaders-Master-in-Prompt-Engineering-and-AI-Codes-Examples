# AI Limitations Quick Reference

## Module 09: Code and Examples

A quick reference of known AI limitations and practical workarounds for each. Keep this guide handy during any AI-assisted work.

---

## How to Use This Reference

Each limitation entry includes:
- **The Limitation**: What the AI struggles with
- **Why It Happens**: The technical reason
- **Risk Level**: How likely this is to cause problems
- **Detection**: How to spot when this limitation is affecting your output
- **Workaround**: Practical strategies to address it

---

## Category 1: Knowledge Limitations

### 1.1 Knowledge Cutoff

| Aspect | Detail |
|--------|--------|
| **Limitation** | The model has no knowledge of events after its training data cutoff date |
| **Why** | LLMs are trained on a fixed dataset; they cannot access new information |
| **Risk Level** | HIGH for current events; LOW for historical/timeless topics |
| **Detection** | Ask about recent events; model will either refuse, hallucinate, or provide outdated info |
| **Workaround** | Provide current information in the prompt. Use RAG systems. Include "as of [date]" in queries. Use tools/plugins that can search the web. |

**Workaround prompt:**
```
My question involves information that may have changed recently.
Here is the current information as of {today's_date}:
{current_information}

Based on this current data, {your_question}
```

---

### 1.2 Niche/Obscure Topic Knowledge

| Aspect | Detail |
|--------|--------|
| **Limitation** | Unreliable on niche, specialized, or obscure topics |
| **Why** | Less training data means less reliable pattern matching |
| **Risk Level** | HIGH — and the model often does not signal its uncertainty |
| **Detection** | Ask increasingly specific questions; note where answers become vague or suspiciously detailed |
| **Workaround** | Provide domain-specific context. Use specialist sources. Lower expectations for accuracy. Always verify. |

**Workaround prompt:**
```
I'm asking about a specialized topic. If you have limited
knowledge about any aspect of this question, please say so
rather than guessing. A partial answer with honest gaps is
much more useful than a complete answer with hidden
inaccuracies.

{your_niche_question}
```

---

### 1.3 Specific Statistics and Numbers

| Aspect | Detail |
|--------|--------|
| **Limitation** | Frequently fabricates precise numbers, percentages, and statistics |
| **Why** | The model generates statistically plausible numbers, not retrieved facts |
| **Risk Level** | VERY HIGH — fabricated numbers look exactly like real ones |
| **Detection** | Ask for the source of any specific number. Check if the number is consistent across rephrased queries. |
| **Workaround** | Provide the actual data. Use "approximate" ranges. Never trust AI-generated statistics without verification. |

**Workaround prompt:**
```
If your answer involves specific numbers, statistics,
or percentages, please:
1. Only include numbers you are highly confident about
2. Use ranges instead of precise figures when uncertain
   (e.g., "40-50%" instead of "47.3%")
3. For any number, indicate if it is [APPROXIMATE] or [EXACT]
4. Name the source for any specific statistic
```

---

### 1.4 Citations and References

| Aspect | Detail |
|--------|--------|
| **Limitation** | Frequently fabricates academic papers, books, URLs, and other citations |
| **Why** | The model generates citation-shaped text that follows patterns of real citations |
| **Risk Level** | EXTREME — fabricated citations can cause professional embarrassment, legal issues, and erosion of trust |
| **Detection** | Verify EVERY citation independently. Check author + title + venue + year. |
| **Workaround** | Never use AI-generated citations without verification. Provide real references for the model to cite. Use "[source needed]" pattern. |

**Workaround prompt:**
```
CITATION RULES:
- Do NOT generate any citations or references
- If you would normally cite a source, instead write:
  "[CITATION NEEDED: topic/claim]"
- I will look up and add real citations myself
- It is MUCH better to mark where citations are needed
  than to provide potentially fabricated ones
```

---

### 1.5 Individual People (Non-Famous)

| Aspect | Detail |
|--------|--------|
| **Limitation** | Unreliable information about people who are not globally famous |
| **Why** | Limited training data on most individuals; model may merge details from different people |
| **Risk Level** | HIGH — can produce plausible but wrong biographical details |
| **Detection** | Cross-reference any biographical details with independent sources |
| **Workaround** | Provide known facts about the person. Do not rely on AI for biographical details of non-public figures. |

---

## Category 2: Reasoning Limitations

### 2.1 Mathematical Computation

| Aspect | Detail |
|--------|--------|
| **Limitation** | Unreliable at arithmetic, especially multi-step or multi-digit calculations |
| **Why** | Processes math as language patterns, not computation |
| **Risk Level** | HIGH for any calculation beyond simple single-digit arithmetic |
| **Detection** | Verify any calculation independently with a calculator |
| **Workaround** | Use code execution for math. Have the model write code to calculate rather than computing directly. Use chain-of-thought and verify each step. |

**Workaround prompt:**
```
For any mathematical calculation in this task:
1. Write out the formula first
2. Show each step of the calculation
3. Double-check by working backward from your answer
4. If the task involves more than simple arithmetic,
   write Python code to perform the calculation instead

ALTERNATIVE: Write a Python function that computes the
answer rather than computing it yourself.
```

---

### 2.2 Counting and Character-Level Tasks

| Aspect | Detail |
|--------|--------|
| **Limitation** | Cannot reliably count letters, words, syllables, or characters |
| **Why** | Tokenization means the model does not see individual characters |
| **Risk Level** | HIGH for any counting task |
| **Detection** | Count manually; AI counts are frequently wrong |
| **Workaround** | Use code for counting tasks. Do not trust the model's count. |

**Workaround prompt:**
```
Write a Python script that counts {what_to_count}
in the following text, rather than counting manually:
"{text}"
```

---

### 2.3 Multi-Step Reasoning

| Aspect | Detail |
|--------|--------|
| **Limitation** | Accuracy degrades with each reasoning step; errors compound |
| **Why** | Each step introduces potential error that propagates forward |
| **Risk Level** | MEDIUM for 2-3 steps; HIGH for 4+ steps |
| **Detection** | Verify each intermediate step independently |
| **Workaround** | Break into separate prompts, one step at a time. Use chain-of-thought. Verify intermediate results before proceeding. |

**Workaround prompt:**
```
I need you to solve a multi-step problem. Process it
ONE STEP AT A TIME:

Step 1: {first_step}
Provide ONLY the result of step 1. I will verify before
we proceed to step 2.
```

---

### 2.4 Spatial and Physical Reasoning

| Aspect | Detail |
|--------|--------|
| **Limitation** | Cannot reliably reason about physical space, 3D objects, or spatial relationships |
| **Why** | No spatial processing capability; no embodied experience |
| **Risk Level** | HIGH for any spatial reasoning task |
| **Detection** | Test with simple spatial problems you can verify |
| **Workaround** | Convert spatial problems to coordinate systems. Use explicit state tracking. Consider multimodal models for visual tasks. |

**Workaround prompt:**
```
Represent this spatial problem using a coordinate system:
- Define origin point (0,0)
- Track positions using (x,y) coordinates
- Show the coordinate state after each movement
- Calculate final position mathematically

Problem: {spatial_problem}
```

---

### 2.5 Logical Reasoning with Novel Structures

| Aspect | Detail |
|--------|--------|
| **Limitation** | Struggles with logic problems that do not match common patterns in training data |
| **Why** | Pattern matching works for familiar structures but fails for novel ones |
| **Risk Level** | MEDIUM — performs well on common logic, poorly on unusual logic |
| **Detection** | Test with non-standard logical problems |
| **Workaround** | Provide the logical framework explicitly. Break into simple steps. Use formal logic notation when possible. |

---

## Category 3: Output Quality Limitations

### 3.1 Sycophancy (People-Pleasing)

| Aspect | Detail |
|--------|--------|
| **Limitation** | Tends to agree with the user, even when the user is wrong |
| **Why** | RLHF training rewards helpful, agreeable responses |
| **Risk Level** | HIGH — can reinforce false beliefs and lead to confirmation bias |
| **Detection** | Present a false premise; see if the model corrects you or agrees |
| **Workaround** | Explicitly ask the model to disagree if warranted. Use the "devil's advocate" pattern. |

**Workaround prompt:**
```
I want an honest assessment, not agreement. If my premise
is wrong, tell me. If my approach has flaws, identify them.
I value correction over confirmation.

You will NOT be penalized for disagreeing with me. In fact,
I will consider the response more valuable if it identifies
problems I have not seen.

My claim/approach: {your_claim}
```

---

### 3.2 Verbosity and Filler

| Aspect | Detail |
|--------|--------|
| **Limitation** | Tends to produce verbose responses with filler content |
| **Why** | Trained on verbose human text; RLHF rewards "comprehensive" responses |
| **Risk Level** | LOW for accuracy, but reduces efficiency and can dilute key points |
| **Detection** | Review: what percentage of the response is essential information? |
| **Workaround** | Set explicit length limits. Ask for "concise" or "brief" responses. Use structured output formats. |

**Workaround prompt:**
```
Respond in exactly {N} sentences. Every sentence must
contain essential information. No filler, no padding,
no restating the question, no unnecessary caveats.
```

---

### 3.3 Inconsistency Across Runs

| Aspect | Detail |
|--------|--------|
| **Limitation** | Different responses to the same prompt across different sessions |
| **Why** | Temperature-based sampling introduces randomness; no persistent memory |
| **Risk Level** | MEDIUM — can produce contradictory information across sessions |
| **Detection** | Run the same prompt multiple times and compare |
| **Workaround** | Use temperature 0 for maximum consistency. Use few-shot examples. Pin important facts in the prompt. |

---

### 3.4 Difficulty with Negation

| Aspect | Detail |
|--------|--------|
| **Limitation** | Struggles to follow "do NOT" instructions reliably |
| **Why** | Attention mechanism may focus on the concept being negated, ironically increasing its probability |
| **Risk Level** | MEDIUM — the model may do exactly what you told it not to |
| **Detection** | Check output against negative constraints explicitly |
| **Workaround** | Use positive instructions instead of negative ones where possible. Repeat critical constraints at the end of the prompt. |

**Instead of:**
```
Do NOT mention competitor products.
Do NOT use technical jargon.
Do NOT include prices.
```

**Use:**
```
Mention ONLY our company's products.
Use plain language accessible to non-technical readers.
Focus on features and benefits without pricing information.
```

---

## Category 4: Structural Limitations

### 4.1 Context Window Limits

| Aspect | Detail |
|--------|--------|
| **Limitation** | Cannot process more text than the context window allows |
| **Why** | Fixed architectural constraint of the transformer model |
| **Risk Level** | MEDIUM — forces you to work within limits but is a hard constraint |
| **Detection** | You will receive an error or the model will truncate |
| **Workaround** | Chunk documents. Use summarization chains. Prioritize information. See Lesson 08 for detailed strategies. |

---

### 4.2 Lost in the Middle

| Aspect | Detail |
|--------|--------|
| **Limitation** | Information in the middle of long contexts is less likely to be used |
| **Why** | Attention mechanism has primacy and recency bias |
| **Risk Level** | HIGH for long contexts with important information in the middle |
| **Detection** | Place a specific fact in the middle and test retrieval |
| **Workaround** | Put critical info at the beginning and end. Repeat key instructions. Use clear headers for navigation. |

---

### 4.3 No Persistent Memory

| Aspect | Detail |
|--------|--------|
| **Limitation** | No memory between separate conversations |
| **Why** | Each conversation starts with a fresh context window |
| **Risk Level** | MEDIUM — you must re-establish context in each session |
| **Detection** | Reference previous conversations; model will not remember |
| **Workaround** | Maintain your own context files. Re-inject important context at the start of each session. Use conversation summaries. |

---

### 4.4 No Self-Awareness of Limitations

| Aspect | Detail |
|--------|--------|
| **Limitation** | The model does not reliably know what it does not know |
| **Why** | No architectural mechanism to distinguish knowledge from ignorance |
| **Risk Level** | VERY HIGH — the model will confidently provide information in areas where it has no reliable knowledge |
| **Detection** | The model's expressed confidence does not correlate well with actual accuracy |
| **Workaround** | Never rely on the model's self-reported confidence alone. Implement external verification. Use the uncertainty prompts from Lesson 03. |

---

## Category 5: Bias Limitations

### 5.1 Training Data Bias

| Aspect | Detail |
|--------|--------|
| **Limitation** | Outputs reflect biases in training data (demographic, cultural, temporal) |
| **Why** | The model learned from internet text, which is not demographically representative |
| **Risk Level** | HIGH — bias is systematic and pervasive |
| **Detection** | Use the bias detection checklist from this module |
| **Workaround** | Use debiasing prompts. Request diverse perspectives. Review outputs for bias explicitly. See Lesson 09. |

---

### 5.2 English/Western Centrism

| Aspect | Detail |
|--------|--------|
| **Limitation** | Defaults to English-language, Western cultural perspective |
| **Why** | Training data is predominantly English-language, Western-origin content |
| **Risk Level** | HIGH for non-Western contexts or multilingual work |
| **Detection** | Ask about non-Western topics; note depth and accuracy vs. Western equivalents |
| **Workaround** | Explicitly specify the cultural context. Ask for non-Western perspectives. Verify with local sources. |

---

## Quick Decision Matrix

**"Should I trust this AI output?"**

| Factor | Trust More | Trust Less |
|--------|-----------|------------|
| Topic familiarity | Well-known, widely documented | Niche, obscure, specialized |
| Data type | Concepts, explanations | Specific numbers, dates, citations |
| Time sensitivity | Historical, timeless | Current, recent, rapidly changing |
| Output type | Structure, language, format | Facts, data, evidence |
| Task complexity | Simple, single-step | Complex, multi-step reasoning |
| Grounding | Source material provided | No source material |
| Domain | General knowledge | Medical, legal, financial |
| Audience | Internal draft | Published, official, consequential |

---

## Quick Fix Reference

| Problem | Quick Fix |
|---------|-----------|
| Model fabricates statistics | Add: "Use ranges, not precise numbers. Mark all statistics with [VERIFY]." |
| Model invents citations | Add: "Do not generate citations. Write [CITATION NEEDED] instead." |
| Model is too confident | Add: "Rate each claim HIGH/MEDIUM/LOW confidence. I value honest uncertainty." |
| Model agrees with everything | Add: "Challenge my assumptions. Tell me what could be wrong with my approach." |
| Model adds info to summary | Add: "Use ONLY information from the provided text. Nothing else." |
| Model gives wrong math | Add: "Write Python code to calculate instead of computing directly." |
| Model output too long | Add: "Answer in exactly N sentences. No filler." |
| Model misses middle context | Move critical info to beginning. Repeat key instruction at end. |
| Model biased output | Add: "Present at least three different perspectives on this topic." |
| Model outdated info | Provide current data in the prompt with date stamp. |

---

## When NOT to Use AI

These tasks should not rely on AI output, even with workarounds:

1. **Safety-critical decisions** without expert human review
2. **Legal filings** without attorney verification
3. **Medical diagnosis or treatment** without clinical review
4. **Financial advice** for individual investment decisions
5. **Any task where the cost of error exceeds the cost of manual work**
6. **Precise arithmetic** (use a calculator or code)
7. **Real-time data** (use APIs and databases)
8. **Character-level text manipulation** (use code)
9. **Claims about specific living people** (verify all claims)
10. **Content that will be used as sole basis for decisions affecting people's lives**

---

## Model-Specific Notes

### GPT-4 / GPT-4o
- Strong general reasoning; weaker on math
- Good instruction following
- Moderate context window (128K)
- Tends toward verbosity

### Claude (3.5 Sonnet / 3 Opus)
- Strong instruction following; good at nuance
- Large context window (200K)
- Generally more cautious about uncertain claims
- Better at following complex constraints

### Gemini 1.5 Pro
- Very large context window (1M+)
- Strong multimodal capabilities
- Good for processing long documents
- May have different bias patterns than GPT/Claude

### Open Source Models (Llama, Mistral)
- Smaller context windows generally
- Less instruction tuning (may be less constraint-following)
- Can be fine-tuned for specific use cases
- Running locally eliminates data privacy concerns

**Note**: These characterizations are generalizations based on experience up to early 2025. Model capabilities change with each update.

---

*Part of Module 09: Managing Hallucinations and AI Limitations*
