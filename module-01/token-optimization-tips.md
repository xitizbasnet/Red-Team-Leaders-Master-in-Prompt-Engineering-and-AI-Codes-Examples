# Token Optimization Tips

## Module 01 - Foundations of Artificial Intelligence
### Practical Guide for Optimizing Token Usage and Reducing Costs

---

## Why Token Optimization Matters

Every interaction with an AI model costs tokens. Tokens translate directly to:

- **Money** -- You pay per token (input and output)
- **Speed** -- More tokens = slower responses
- **Quality** -- Better-structured prompts (even if shorter) often produce better results
- **Context space** -- Tokens wasted on verbosity leave less room for meaningful content

A well-optimized prompt can reduce costs by 30-80% while maintaining or even improving output quality.

---

## 1. Input Token Optimization

### 1.1 Write Concise Prompts

The single most impactful optimization. Say the same thing with fewer words.

**Before (42 tokens):**
```
I would really appreciate it if you could please help me by writing
a detailed and comprehensive summary of the following text that I am
about to provide to you below. Please make it thorough.
```

**After (7 tokens):**
```
Summarize this text thoroughly:
```

**Savings: 83%**

More examples:

| Verbose Prompt | Optimized Prompt | Savings |
|---|---|---|
| "Can you please help me by explaining what..." | "Explain:" | ~85% |
| "I would like you to write a Python function that takes a list..." | "Write a Python function: input=list,..." | ~50% |
| "Please take a look at the following code and tell me if there are any bugs or issues" | "Find bugs in this code:" | ~75% |
| "In your response, please make sure to include examples and be very detailed" | "Include examples. Be detailed." | ~60% |

### 1.2 Use Structured Data Formats

Replace prose with structured formats when conveying data.

**Before (45 tokens):**
```
The product is called SuperWidget Pro, it costs twenty-five dollars
and ninety-nine cents, it weighs three point five pounds, and it
comes in the colors red, blue, and green.
```

**After (25 tokens):**
```
Product: SuperWidget Pro
Price: $25.99
Weight: 3.5 lbs
Colors: red, blue, green
```

**Savings: 44%**

### 1.3 Eliminate Pleasantries and Filler

AI models do not need politeness. While being polite is a nice habit, every "please," "thank you," "I was wondering if," and "would you be so kind as to" costs tokens.

**Unnecessary fillers to remove:**
```
- "I was wondering if you could..."
- "Would it be possible for you to..."
- "Please be so kind as to..."
- "I hope this is not too much trouble, but..."
- "Thank you in advance for..."
- "If you don't mind, could you..."
- "I would greatly appreciate it if..."
```

**Keep it direct:**
```
- "List 5 benefits of..."
- "Compare X and Y"
- "Write code that..."
- "Explain why..."
```

### 1.4 Use Abbreviations and Shorthand (When Clear)

For technical or repeated content, abbreviations save tokens:

```
Before: "Artificial Intelligence and Machine Learning"
After:  "AI and ML"

Before: "Application Programming Interface"
After:  "API"

Before: "for example"
After:  "e.g.,"

Before: "that is to say"
After:  "i.e.,"
```

### 1.5 Reference Instead of Repeat

If you have already established context, reference it instead of restating it.

**Before:**
```
In the first paragraph I mentioned that the company was founded in
2020. Given that the company was founded in 2020, what was the
market like when the company was founded in 2020?
```

**After:**
```
What was the market like when the company was founded (2020)?
```

### 1.6 Remove Redundant Instructions

Many instructions are unnecessary because the model will do them by default.

**Often redundant:**
```
- "Write in English" (it will, unless you ask otherwise)
- "Be accurate" (it tries to be by default)
- "Read the text carefully" (it processes everything you send)
- "Think about this" (it processes the input regardless)
- "Use your knowledge" (it always does)
```

### 1.7 Optimize System Prompts

System prompts are sent with every message in a conversation. Optimize them aggressively.

**Before (88 tokens):**
```
You are a very helpful and knowledgeable customer service assistant
for our company called TechCorp. You should always be polite and
professional in your responses. You should try to answer questions
about our products and services. If you don't know the answer, you
should tell the customer that you will escalate their question.
You should always end your responses by asking if there is anything
else you can help with.
```

**After (38 tokens):**
```
You are TechCorp's customer service assistant.
- Answer product/service questions
- If unsure, escalate to human agent
- End with: "Anything else I can help with?"
```

**Savings: 57% -- and this saves on EVERY message in the conversation.**

---

## 2. Output Token Optimization

### 2.1 Request Concise Responses

Explicitly ask for brevity:

```
"Respond in 2-3 sentences."
"Answer in under 50 words."
"Be concise."
"Brief answer only."
```

### 2.2 Specify Output Format

Tell the model exactly what format you want:

```
"Respond with ONLY the answer, no explanation."
"Output as JSON: {name, price, category}"
"List only the top 3, no descriptions."
"Yes or No answer only."
```

### 2.3 Use max_tokens Parameter

Set the `max_tokens` parameter in API calls to cap response length:

```python
# Instead of letting the model write as much as it wants:
response = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=100,  # Hard cap at ~75 words
    messages=[{"role": "user", "content": "Explain gravity."}]
)
```

### 2.4 Request Bullet Points Over Prose

Bullet points are typically more token-efficient than paragraphs:

**Prose response (~120 tokens):**
```
Machine learning has several advantages. First, it can process
large amounts of data much faster than humans can. Second, it can
identify patterns that humans might miss. Third, it improves over
time as it is exposed to more data. Fourth, it can automate
repetitive tasks, freeing up humans for more creative work.
```

**Bullet point response (~60 tokens):**
```
ML advantages:
- Processes large data quickly
- Identifies hidden patterns
- Improves with more data
- Automates repetitive tasks
```

**Savings: 50%**

### 2.5 Suppress Unnecessary Preambles

Many models add preambles like "Great question! Let me explain..." or "Sure, I'd be happy to help with that."

Add to your prompt:
```
"Skip introductions. Start with the answer directly."
```

or in the system prompt:
```
"Never start with pleasantries. Answer directly."
```

---

## 3. Context Window Management

### 3.1 Sliding Window Strategy

For long conversations, keep only the most recent N messages:

```
Strategy:
  - Keep: System prompt (always)
  - Keep: Last 5-10 messages
  - Discard: Older messages

Implementation:
  messages = [system_prompt] + conversation_history[-10:]
```

### 3.2 Conversation Summarization

Periodically summarize the conversation and replace old messages:

```
Every 10 messages:
  1. Send old messages to a cheap model (GPT-4o mini)
  2. Ask: "Summarize this conversation in 3 sentences"
  3. Replace old messages with the summary
  4. Continue conversation with summary + recent messages

Result:
  - Before: 500 tokens of old messages
  - After: 50 tokens of summary
  - Savings: 90% on historical context
```

### 3.3 Selective Context Injection (RAG)

Do not send everything -- send only what is relevant:

```
Bad approach:
  Send entire 50-page manual + user question = 30,000+ tokens

Good approach:
  1. User asks a question
  2. Search the manual for relevant sections (semantic search)
  3. Send only the 2-3 most relevant paragraphs + question = 500 tokens

Savings: 98%+
```

### 3.4 Chunk Large Documents

When you must process large documents:

```
Strategy:
  1. Split document into chunks (500-1000 tokens each)
  2. Process each chunk with a cheap model
  3. Combine results with a more capable model

Example - Summarizing a 100-page report:
  Step 1: Split into 50 chunks of 2 pages each
  Step 2: Summarize each chunk with GPT-4o mini ($0.003 total)
  Step 3: Send 50 summaries to Claude Sonnet for final summary ($0.02)
  Total: ~$0.023

vs. sending entire document to Claude Sonnet: ~$0.50
Savings: 95%
```

---

## 4. Multi-Model Cost Optimization

### 4.1 Route by Complexity

Use different models for different task complexities:

```
Simple tasks (classification, extraction, formatting):
  -> GPT-4o mini or Claude Haiku
  Cost: $0.15-0.80 / 1M input tokens

Medium tasks (summarization, Q&A, basic analysis):
  -> GPT-4o or Claude Sonnet
  Cost: $2.50-3.00 / 1M input tokens

Complex tasks (deep analysis, creative writing, hard coding):
  -> Claude Opus or o3
  Cost: $15.00+ / 1M input tokens

Potential savings: 80%+ on high-volume applications
```

### 4.2 Use a Classifier to Route

```python
# Pseudo-code for intelligent model routing
def route_query(query):
    # Use a cheap model to classify complexity
    complexity = classify_with_mini_model(query)

    if complexity == "simple":
        return call_model("gpt-4o-mini", query)     # $0.15/1M
    elif complexity == "medium":
        return call_model("claude-sonnet", query)     # $3.00/1M
    else:
        return call_model("claude-opus", query)       # $15.00/1M
```

### 4.3 Cache Common Responses

```
Implementation:
  1. Hash the user's query (or compute semantic embedding)
  2. Check if a similar query has been answered before
  3. If yes, return cached response (cost: $0)
  4. If no, call the model and cache the result

Good candidates for caching:
  - FAQs and common questions
  - Standard responses (greetings, error messages)
  - Reference information that does not change

Typical cache hit rate: 20-50% for customer support
Savings: 20-50% of total API costs
```

---

## 5. Batch Processing

### 5.1 Use Batch APIs

Both OpenAI and Anthropic offer batch endpoints at 50% discount:

```
Standard API: $3.00 / 1M input tokens (Claude Sonnet)
Batch API:    $1.50 / 1M input tokens (50% off!)

Good for:
  - Processing large datasets
  - Non-time-sensitive tasks
  - Nightly batch jobs
  - Content generation at scale

Trade-off: Results are not immediate (typically within 24 hours)
```

### 5.2 Combine Multiple Questions

Instead of making separate API calls for related questions:

**Before (3 API calls):**
```
Call 1: "What is machine learning?"
Call 2: "What is deep learning?"
Call 3: "How do they differ?"
```

**After (1 API call):**
```
"Answer these three questions:
1. What is machine learning?
2. What is deep learning?
3. How do they differ?"
```

Savings: Eliminates overhead of 2 API calls + reduces duplicated context.

---

## 6. Language-Specific Optimization

### 6.1 Non-English Text Uses More Tokens

As discussed in Lesson 05, non-Latin scripts cost 1.5-3x more tokens:

```
"Hello, how are you?" = ~6 tokens (English)
"こんにちは、お元気ですか？" = ~11 tokens (Japanese)
"مرحبا، كيف حالك؟" = ~12 tokens (Arabic)
```

**Optimization strategies for non-English:**
```
1. Process in English when possible, translate at the end
2. Use models with larger vocabularies (GPT-4o's o200k_base
   is more efficient for non-English than cl100k_base)
3. Keep prompts/instructions in English even if content is
   in another language
4. Consider the token cost when choosing languages for
   multilingual applications
```

---

## 7. Quick Reference: Token Optimization Checklist

```
INPUT OPTIMIZATION:
  [ ] Remove pleasantries and filler words
  [ ] Use structured data instead of prose
  [ ] Write concise, direct prompts
  [ ] Optimize system prompts (sent with every message)
  [ ] Use abbreviations where clear
  [ ] Reference instead of repeat
  [ ] Send only relevant context (RAG)

OUTPUT OPTIMIZATION:
  [ ] Request concise responses
  [ ] Specify output format
  [ ] Set max_tokens parameter
  [ ] Request bullet points over prose
  [ ] Suppress unnecessary preambles

ARCHITECTURE OPTIMIZATION:
  [ ] Route queries to appropriately sized models
  [ ] Cache common responses
  [ ] Use batch APIs for non-urgent tasks
  [ ] Implement sliding window for conversations
  [ ] Summarize old conversation context
  [ ] Chunk large documents

MONITORING:
  [ ] Track token usage per endpoint/user
  [ ] Set up cost alerts
  [ ] Review and optimize top token-consuming prompts
  [ ] Compare model costs regularly (prices change)
```

---

## 8. Real-World Cost Savings Example

### Scenario: Customer Support Chatbot

**Before optimization:**
```
Model: GPT-4o for everything
System prompt: 150 tokens (verbose)
Average input per turn: 200 tokens
Average output per turn: 300 tokens
Turns per conversation: 5
Conversations per day: 10,000

Daily tokens:
  Input:  10,000 x 5 x (150 + 200) = 17,500,000
  Output: 10,000 x 5 x 300 = 15,000,000

Daily cost:
  Input:  17.5M x $2.50/1M = $43.75
  Output: 15.0M x $10.00/1M = $150.00
  Total:  $193.75/day = $5,813/month
```

**After optimization:**
```
Changes made:
  1. Route simple queries (60%) to GPT-4o mini
  2. Optimize system prompt: 150 -> 40 tokens (-73%)
  3. Request concise responses: avg 300 -> 150 tokens (-50%)
  4. Cache top 100 FAQs (covers 25% of queries)
  5. Summarize conversations after 3 turns

Results:
  - 25% of queries cached: $0
  - 45% of queries to GPT-4o mini (simple):
    Input:  4,500 x 5 x (40 + 200) = 5,400,000 x $0.15/1M = $0.81
    Output: 4,500 x 5 x 150 = 3,375,000 x $0.60/1M = $2.03
  - 30% of queries to GPT-4o (complex):
    Input:  3,000 x 5 x (40 + 200) = 3,600,000 x $2.50/1M = $9.00
    Output: 3,000 x 5 x 150 = 2,250,000 x $10.00/1M = $22.50

  Daily total: $34.34/day = $1,030/month

  SAVINGS: $4,783/month (82% reduction!)
```

---

## 9. Tools for Monitoring Token Usage

```
1. API DASHBOARDS
   - OpenAI: platform.openai.com/usage
   - Anthropic: console.anthropic.com (usage tab)
   - Google: Cloud Console billing

2. PROGRAMMATIC TRACKING
   - Log token usage from every API response
   - Build dashboards with Grafana, Datadog, etc.
   - Set up alerts for unusual spending

3. TOKEN COUNTING TOOLS
   - tiktoken (Python library for OpenAI models)
   - Anthropic's token counting endpoint
   - Online tokenizers for quick estimates

4. COST ESTIMATION BEFORE SENDING
   # Count tokens before making the API call
   estimated_tokens = count_tokens(prompt)
   estimated_cost = estimated_tokens * price_per_token
   if estimated_cost > budget_threshold:
       use_cheaper_model()
```

---

## Summary

The key principles of token optimization are:

1. **Be concise** -- Every unnecessary word costs money and time
2. **Be structured** -- Data formats are more efficient than prose
3. **Be strategic** -- Use the right model for the right task
4. **Be smart about context** -- Send only what is relevant
5. **Cache and batch** -- Avoid redundant API calls
6. **Monitor and iterate** -- Track usage and continuously optimize

By applying these techniques systematically, you can typically reduce AI API costs by 50-80% while maintaining or improving output quality.

---

*This guide is part of Module 01: Foundations of Artificial Intelligence in the Master in Prompt Engineering and AI course.*
