# Temperature and Parameter Quick Reference Guide — Module 02

## Complete Reference for AI Generation Parameters

---

## 1. Temperature At a Glance

```
TEMPERATURE SCALE
═══════════════════════════════════════════════════════════════

0.0          0.3          0.5          0.7          1.0          1.5          2.0
 │            │            │            │            │            │            │
 ▼            ▼            ▼            ▼            ▼            ▼            ▼
Deterministic  Focused     Balanced    Creative    Natural     Wild        Chaotic
Predictable   Consistent  Moderate    Varied      Full        Surprising  Incoherent
Repetitive    Reliable    Flexible    Engaging    Range       Unexpected  Unreliable

◄─── MORE PREDICTABLE ────────────────────────────── MORE CREATIVE ───►
◄─── MORE ACCURATE ───────────────────────────────── MORE DIVERSE ────►
◄─── LESS INTERESTING ────────────────────────────── LESS RELIABLE ───►
```

---

## 2. Temperature by Use Case

### The Definitive Guide

| Use Case | Temperature | Why |
|----------|:-----------:|-----|
| **Factual Q&A** | 0 | Only correct answers matter |
| **Data extraction** | 0 | Consistency is critical |
| **Classification** | 0 | Same input should yield same output |
| **JSON/structured output** | 0 — 0.2 | Format reliability is essential |
| **Code generation** | 0 — 0.3 | Code must be syntactically correct |
| **Code completion** | 0.2 | Predictable, conventional patterns |
| **Summarization** | 0.2 — 0.4 | Faithful to source, slight variation |
| **Translation** | 0.2 — 0.4 | Accuracy with natural phrasing |
| **Technical writing** | 0.3 — 0.5 | Clear and precise but not robotic |
| **Business email** | 0.3 — 0.5 | Professional with natural variation |
| **Report writing** | 0.4 — 0.6 | Thorough with readable prose |
| **Conversational chat** | 0.5 — 0.7 | Natural-sounding responses |
| **Explanations** | 0.5 — 0.7 | Clear with engaging delivery |
| **Blog writing** | 0.6 — 0.8 | Engaging, readable, varied |
| **Marketing copy** | 0.7 — 0.9 | Compelling, creative, attention-grabbing |
| **Brainstorming** | 0.8 — 1.2 | Diverse ideas, unusual connections |
| **Creative fiction** | 0.7 — 1.0 | Vivid, surprising, original |
| **Poetry** | 0.8 — 1.2 | Lyrical, metaphorical, unexpected |
| **Humor writing** | 0.8 — 1.0 | Surprising word choices, wit |
| **Name/title generation** | 0.9 — 1.3 | Maximum variety needed |
| **Random generation** | 1.0 — 1.5 | High variability desired |

---

## 3. All Parameters — Quick Reference

### Temperature

```
Parameter:   temperature
Range:       0.0 — 2.0 (OpenAI, Gemini) | 0.0 — 1.0 (Anthropic)
Default:     1.0
Effect:      Controls randomness of token selection
Low value:   Predictable, focused, repetitive
High value:  Creative, varied, potentially incoherent
```

### Top_p (Nucleus Sampling)

```
Parameter:   top_p
Range:       0.0 — 1.0
Default:     1.0
Effect:      Limits token selection to a probability threshold
Low value:   Only highest-probability tokens considered
High value:  More tokens eligible for selection

Common Settings:
  0.1  → Very restrictive (only top tokens)
  0.5  → Moderately restrictive
  0.9  → Slight safety net against unlikely tokens
  0.95 → Minimal filtering (recommended default)
  1.0  → No filtering (default)
```

### Top_k

```
Parameter:   top_k
Range:       1 — vocabulary size
Default:     Varies by provider
Effect:      Limits selection to top K tokens by probability
Low value:   Only top few tokens (more deterministic)
High value:  More tokens eligible

Common Settings:
  1   → Greedy (always pick the top token)
  10  → Very focused
  40  → Moderate variety (Gemini default)
  100 → Wide variety
  0   → No limit (disabled)

Availability: Anthropic (yes), Gemini (yes), OpenAI (no)
```

### Frequency Penalty

```
Parameter:   frequency_penalty
Range:       -2.0 — 2.0 (OpenAI) | Not available (Anthropic, Gemini)
Default:     0
Effect:      Penalizes tokens proportional to how often they appeared
Low/zero:    No penalty for repetition
High value:  Strong discouragement of repeated words/phrases
Negative:    Encourages repetition (rarely useful)

Common Settings:
  0.0 → No penalty (default — good for code, technical writing)
  0.3 → Light penalty (reduces obvious repetition)
  0.5 → Moderate penalty (good for general writing)
  0.8 → Strong penalty (very diverse vocabulary)
  1.0+ → Very strong (may produce awkward phrasing)
```

### Presence Penalty

```
Parameter:   presence_penalty
Range:       -2.0 — 2.0 (OpenAI) | Not available (Anthropic, Gemini)
Default:     0
Effect:      Flat penalty for any token that has appeared at all
Low/zero:    No penalty for revisiting topics
High value:  Encourages exploring new topics/ideas
Negative:    Encourages staying on topic (rarely useful)

Common Settings:
  0.0 → No penalty (default — good for focused tasks)
  0.3 → Light nudge toward new topics
  0.6 → Moderate encouragement to diversify
  0.8 → Strong push for new topics (good for brainstorming)
  1.0+ → Very strong (may cause topic-jumping)
```

### Max Tokens

```
Parameter:   max_tokens (OpenAI, Anthropic) | max_output_tokens (Gemini)
Range:       1 — model maximum
Default:     Varies (often 4096)
Effect:      Hard limit on output length (cuts off mid-sentence if reached)

Token-to-Word Conversion (English):
  50 tokens   ≈ 38 words    (a short paragraph)
  100 tokens  ≈ 75 words    (a long paragraph)
  250 tokens  ≈ 188 words   (half a page)
  500 tokens  ≈ 375 words   (one page)
  1000 tokens ≈ 750 words   (two pages)
  2000 tokens ≈ 1500 words  (four pages)
  4000 tokens ≈ 3000 words  (eight pages)
```

### Stop Sequences

```
Parameter:   stop (OpenAI) | stop_sequences (Anthropic, Gemini)
Type:        Array of strings
Default:     None
Effect:      Model stops generating when any stop sequence is produced
Max:         Up to 4 (OpenAI) | varies by provider

Common Stop Sequences:
  "\n\n"       → Stop at double newline (end of paragraph)
  "###"        → Stop at section marker
  "\nHuman:"   → Stop before next conversation turn
  "\nQ:"       → Stop before generating next question
  "```"        → Stop at end of code block
  "</output>"  → Stop at closing XML tag
  "---"        → Stop at horizontal rule
```

---

## 4. Parameter Presets — Copy and Use

### Preset A: "Factual and Precise"
```json
{
  "temperature": 0,
  "top_p": 1.0,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "max_tokens": 500
}
```
**Use for:** Fact extraction, classification, data parsing, JSON output, Q&A

### Preset B: "Reliable Professional"
```json
{
  "temperature": 0.3,
  "top_p": 0.95,
  "frequency_penalty": 0.1,
  "presence_penalty": 0.1,
  "max_tokens": 1000
}
```
**Use for:** Business emails, technical docs, summaries, translations

### Preset C: "Balanced Quality"
```json
{
  "temperature": 0.5,
  "top_p": 0.95,
  "frequency_penalty": 0.3,
  "presence_penalty": 0.2,
  "max_tokens": 1500
}
```
**Use for:** Blog posts, reports, explanations, educational content

### Preset D: "Conversational"
```json
{
  "temperature": 0.7,
  "top_p": 0.95,
  "frequency_penalty": 0.4,
  "presence_penalty": 0.3,
  "max_tokens": 500
}
```
**Use for:** Chatbots, dialogue, conversational AI, customer support

### Preset E: "Creative Writer"
```json
{
  "temperature": 0.85,
  "top_p": 0.95,
  "frequency_penalty": 0.5,
  "presence_penalty": 0.5,
  "max_tokens": 2000
}
```
**Use for:** Creative writing, marketing copy, storytelling, speeches

### Preset F: "Maximum Creativity"
```json
{
  "temperature": 1.2,
  "top_p": 0.98,
  "frequency_penalty": 0.8,
  "presence_penalty": 0.8,
  "max_tokens": 2000
}
```
**Use for:** Brainstorming, poetry, experimental writing, name generation

### Preset G: "Structured Data Only"
```json
{
  "temperature": 0,
  "top_p": 1.0,
  "frequency_penalty": 0,
  "presence_penalty": 0,
  "max_tokens": 2000,
  "response_format": {"type": "json_object"}
}
```
**Use for:** JSON generation, API responses, structured data extraction (OpenAI only for response_format)

---

## 5. Platform-Specific Parameter Matrix

```
╔═══════════════════╦═══════════╦═══════════╦═══════════╗
║ Parameter         ║  OpenAI   ║ Anthropic ║  Gemini   ║
╠═══════════════════╬═══════════╬═══════════╬═══════════╣
║ temperature       ║  0 — 2.0  ║  0 — 1.0  ║  0 — 2.0  ║
║ top_p             ║  0 — 1.0  ║  0 — 1.0  ║  0 — 1.0  ║
║ top_k             ║    N/A    ║  Yes      ║  Yes      ║
║ frequency_penalty ║ -2 — 2.0  ║    N/A    ║    N/A    ║
║ presence_penalty  ║ -2 — 2.0  ║    N/A    ║    N/A    ║
║ max_tokens        ║  Yes      ║  Yes      ║  Yes      ║
║ stop sequences    ║  Up to 4  ║  Yes      ║  Yes      ║
║ JSON mode         ║  Yes      ║    N/A    ║  Yes      ║
║ seed (repro)      ║  Yes      ║    N/A    ║    N/A    ║
║ logprobs          ║  Yes      ║    N/A    ║    N/A    ║
╚═══════════════════╩═══════════╩═══════════╩═══════════╝
```

---

## 6. Decision Flowchart: Choosing Your Temperature

```
START: What type of task?
│
├─► Factual / Extractive / Structured
│   │
│   └─► Does the output need to be identical every time?
│       ├─► YES → Temperature: 0
│       └─► NO  → Temperature: 0.1 — 0.3
│
├─► Professional / Business
│   │
│   └─► How much creative variation is acceptable?
│       ├─► Very little → Temperature: 0.3 — 0.5
│       └─► Some        → Temperature: 0.5 — 0.7
│
├─► Conversational / Explanatory
│   │
│   └─► Temperature: 0.5 — 0.7
│
├─► Creative / Marketing
│   │
│   └─► Is coherence critical?
│       ├─► YES → Temperature: 0.7 — 0.9
│       └─► NO  → Temperature: 0.9 — 1.2
│
└─► Brainstorming / Experimental
    │
    └─► Temperature: 1.0 — 1.5
```

---

## 7. Troubleshooting Parameter Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Output is boring and generic | Temperature too low | Increase to 0.5 — 0.7 |
| Output is incoherent or nonsensical | Temperature too high | Decrease to 0.7 or below |
| Same output every time | Temperature at 0 | Increase to 0.3+ if variation desired |
| Output repeats phrases constantly | Frequency penalty too low | Increase to 0.3 — 0.5 |
| Output uses bizarre vocabulary | Frequency penalty too high | Decrease to 0.3 or below |
| Output keeps circling the same topic | Presence penalty too low | Increase to 0.3 — 0.6 |
| Output jumps between topics randomly | Presence penalty too high | Decrease to 0.3 or below |
| Output cuts off mid-sentence | Max tokens too low | Increase max_tokens |
| Output rambles excessively | Max tokens too high + no stop | Lower max_tokens or add stop sequences |
| JSON output has errors | Temperature too high | Set temperature to 0 |
| Code has syntax errors | Temperature too high | Set temperature to 0 — 0.2 |
| Creative text feels forced | Too many penalties | Reduce frequency + presence penalties |

---

## 8. API Code Examples

### OpenAI (Python)

```python
from openai import OpenAI
client = OpenAI()

# Factual task
response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0,
    max_tokens=500,
    messages=[
        {"role": "system", "content": "You are a data extraction specialist."},
        {"role": "user", "content": "Extract all dates from this text: ..."}
    ]
)

# Creative task
response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0.85,
    top_p=0.95,
    frequency_penalty=0.5,
    presence_penalty=0.5,
    max_tokens=2000,
    messages=[
        {"role": "system", "content": "You are a creative writing assistant."},
        {"role": "user", "content": "Write a short story about ..."}
    ]
)

# Structured JSON output
response = client.chat.completions.create(
    model="gpt-4o",
    temperature=0,
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": "Return data as JSON."},
        {"role": "user", "content": "Extract person info: ..."}
    ]
)
```

### Anthropic (Python)

```python
import anthropic
client = anthropic.Anthropic()

# Factual task
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=500,
    temperature=0,
    system="You are a data extraction specialist.",
    messages=[
        {"role": "user", "content": "Extract all dates from this text: ..."}
    ]
)

# Creative task
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=2000,
    temperature=0.85,
    top_k=50,
    system="You are a creative writing assistant.",
    messages=[
        {"role": "user", "content": "Write a short story about ..."}
    ]
)
```

### Google Gemini (Python)

```python
import google.generativeai as genai

model = genai.GenerativeModel("gemini-2.0-flash")

# Factual task
response = model.generate_content(
    "Extract all dates from this text: ...",
    generation_config=genai.GenerationConfig(
        temperature=0,
        top_p=1.0,
        top_k=1,
        max_output_tokens=500,
    )
)

# Creative task
response = model.generate_content(
    "Write a short story about ...",
    generation_config=genai.GenerationConfig(
        temperature=0.85,
        top_p=0.95,
        top_k=40,
        max_output_tokens=2000,
    )
)
```

---

## 9. Quick Cheat Sheet (Print This Page)

```
TASK TYPE        │ TEMP │ TOP_P │ FREQ_PEN │ PRES_PEN │ MAX_TOK
─────────────────┼──────┼───────┼──────────┼──────────┼────────
Data extraction  │ 0    │ 1.0   │ 0        │ 0        │ 500
Code generation  │ 0.2  │ 0.95  │ 0        │ 0        │ 1000
Summarization    │ 0.3  │ 0.95  │ 0.1      │ 0.1      │ 500
Business writing │ 0.5  │ 0.95  │ 0.3      │ 0.2      │ 1500
Chatbot          │ 0.7  │ 0.95  │ 0.4      │ 0.3      │ 500
Creative writing │ 0.85 │ 0.95  │ 0.5      │ 0.5      │ 2000
Brainstorming    │ 1.1  │ 0.98  │ 0.8      │ 0.8      │ 2000
```

---

*Part of Module 02 — Introduction to Prompt Engineering*
