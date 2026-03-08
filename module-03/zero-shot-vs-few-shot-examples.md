# Zero-Shot vs. Few-Shot Prompts: 15 Side-by-Side Comparisons

## Module 03 — Code and Examples

---

This reference provides 15 practical comparisons showing the same task implemented as both a zero-shot and a few-shot prompt. Use these to understand when each approach is appropriate and how to implement both.

---

## Comparison 1: Sentiment Classification

### Zero-Shot
```
Classify the sentiment of the following text as "positive,"
"negative," or "neutral":

"The hotel was clean and the staff was friendly, but the
breakfast options were very limited."
```

### Few-Shot
```
Classify the sentiment of each review:

Review: "Absolutely amazing experience, will definitely return!"
Sentiment: Positive

Review: "The worst service I've ever encountered. Never again."
Sentiment: Negative

Review: "The room was adequate for the price. Nothing remarkable."
Sentiment: Neutral

Review: "The hotel was clean and the staff was friendly, but the
breakfast options were very limited."
Sentiment:
```

**When to use which:**
- Zero-shot: Quick analysis of clearly positive/negative texts
- Few-shot: When dealing with mixed-sentiment texts or nuanced classification

---

## Comparison 2: Named Entity Recognition

### Zero-Shot
```
Extract all person names, organizations, and locations from
the following text. Return as JSON with keys "persons",
"organizations", "locations":

"Dr. Elena Vasquez from MIT presented her findings at the
Geneva International Conference, alongside researchers from
IBM and Stanford University."
```

### Few-Shot
```
Extract entities from text and return as JSON.

Text: "Tim Cook announced Apple's new partnership with Toyota in Tokyo."
Entities: {"persons": ["Tim Cook"], "organizations": ["Apple", "Toyota"], "locations": ["Tokyo"]}

Text: "Professor Williams from Oxford published a paper with
Dr. Singh's team at Cambridge."
Entities: {"persons": ["Professor Williams", "Dr. Singh"], "organizations": ["Oxford", "Cambridge"], "locations": []}

Text: "Dr. Elena Vasquez from MIT presented her findings at the
Geneva International Conference, alongside researchers from
IBM and Stanford University."
Entities:
```

**When to use which:**
- Zero-shot: Standard entity types in clear context
- Few-shot: When you need specific formatting or handling of ambiguous entities (is "Cambridge" a location or organization?)

---

## Comparison 3: Language Translation with Tone

### Zero-Shot
```
Translate the following English text to Spanish.
Use a formal, professional register suitable for
business correspondence:

"We would like to schedule a meeting to discuss the
upcoming project timeline."
```

### Few-Shot
```
Translate English to formal business Spanish:

English: "Thank you for your prompt response."
Spanish: "Le agradezco su pronta respuesta."

English: "Please find attached the quarterly report."
Spanish: "Adjunto encontrará el informe trimestral."

English: "We would like to schedule a meeting to discuss
the upcoming project timeline."
Spanish:
```

**When to use which:**
- Zero-shot: Common language pairs with standard register
- Few-shot: When specific register, regional dialect, or terminology conventions matter

---

## Comparison 4: Text Summarization

### Zero-Shot
```
Summarize the following article in exactly 3 bullet points,
each no longer than 20 words:

[Article text about renewable energy trends...]
```

### Few-Shot
```
Summarize articles in exactly 3 bullet points (max 20 words each):

Article: [Short article about electric vehicles...]
Summary:
- EV sales grew 45% globally in 2024, led by China and Europe
- Battery costs dropped below $100/kWh for the first time
- Charging infrastructure expanded 60% in major metropolitan areas

Article: [Short article about remote work...]
Summary:
- 58% of companies now offer permanent hybrid work options
- Productivity metrics show no decline from remote arrangements
- Commercial real estate values continue declining in major cities

Article: [Your target article about renewable energy trends...]
Summary:
```

**When to use which:**
- Zero-shot: When length and format instructions are clear enough
- Few-shot: When you need very precise bullet point style and length

---

## Comparison 5: Code Generation

### Zero-Shot
```
Write a Python function called `validate_email` that takes
a string parameter and returns True if it is a valid email
address format, False otherwise. Use regex. Include docstring.
```

### Few-Shot
```
Write Python functions following this pattern:

Function: validate_phone
```python
def validate_phone(phone: str) -> bool:
    """Validate if the input string is a valid US phone number.

    Args:
        phone: String to validate.

    Returns:
        True if valid US phone format, False otherwise.
    """
    import re
    pattern = r'^\+?1?[-.\s]?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}$'
    return bool(re.match(pattern, phone))
```

Function: validate_url
```python
def validate_url(url: str) -> bool:
    """Validate if the input string is a valid URL.

    Args:
        url: String to validate.

    Returns:
        True if valid URL format, False otherwise.
    """
    import re
    pattern = r'^https?://(?:[\w-]+\.)+[\w-]+(?:/[\w-./?%&=]*)?$'
    return bool(re.match(pattern, url))
```

Now write: validate_email
```

**When to use which:**
- Zero-shot: Simple functions where the requirements are clear
- Few-shot: When you need consistent style, docstring format, or specific patterns

---

## Comparison 6: Product Description

### Zero-Shot
```
Write a 100-word product description for wireless noise-canceling
headphones priced at $199. Target audience: remote workers.
Focus on comfort and sound quality.
```

### Few-Shot
```
Write product descriptions following these examples:

Product: Ergonomic Standing Desk — $449 — Target: Office Workers
Description: "Transform your workspace with the ErgoRise Pro standing
desk. Seamlessly transition between sitting and standing with whisper-quiet
electric motors that adjust height from 28 to 48 inches. The bamboo
surface provides 60 inches of workspace — enough for dual monitors and
then some. Cable management channels keep your setup clean. Your back
will thank you after the first week."

Product: Mechanical Keyboard — $129 — Target: Developers
Description: "Code faster with the TypeForce K7 mechanical keyboard.
Cherry MX Brown switches deliver satisfying tactile feedback without
waking your deskmate. Programmable macro keys let you automate repetitive
sequences. The detachable USB-C cable and compact 75% layout keep your
desk uncluttered. Hot-swappable switches mean you can customize the feel
without soldering."

Product: Wireless Noise-Canceling Headphones — $199 — Target: Remote Workers
Description:
```

**When to use which:**
- Zero-shot: When brand voice and format are flexible
- Few-shot: When a specific writing style, structure, or voice must be matched

---

## Comparison 7: Data Format Conversion

### Zero-Shot
```
Convert the following CSV data to JSON format:

name,age,city,role
Alice,32,New York,Engineer
Bob,28,London,Designer
Carol,35,Tokyo,Manager
```

### Few-Shot
```
Convert CSV rows to JSON objects:

CSV: name,score,grade
     John,95,A
JSON: {"name": "John", "score": 95, "grade": "A"}

CSV: name,score,grade
     Maria,87,B+
JSON: {"name": "Maria", "score": 87, "grade": "B+"}

Now convert all rows:
CSV: name,age,city,role
     Alice,32,New York,Engineer
     Bob,28,London,Designer
     Carol,35,Tokyo,Manager
JSON:
```

**When to use which:**
- Zero-shot: Standard format conversions (CSV to JSON, XML to YAML)
- Few-shot: When specific type handling is needed (numbers vs. strings, null handling)

---

## Comparison 8: Intent Classification

### Zero-Shot
```
Classify the following user message into one of these intents:
BOOK_FLIGHT, CANCEL_BOOKING, CHECK_STATUS, CHANGE_SEAT, GENERAL_INQUIRY

User: "I need to switch from an aisle to a window seat on my
flight to Chicago next Thursday."
Intent:
```

### Few-Shot
```
Classify user intents:

User: "I want to fly from Boston to Miami on December 5th."
Intent: BOOK_FLIGHT

User: "Please cancel my reservation for flight AA1234."
Intent: CANCEL_BOOKING

User: "Has my flight been delayed?"
Intent: CHECK_STATUS

User: "Can I move to row 12 instead?"
Intent: CHANGE_SEAT

User: "What's your baggage policy for international flights?"
Intent: GENERAL_INQUIRY

User: "I need to switch from an aisle to a window seat on my
flight to Chicago next Thursday."
Intent:
```

**When to use which:**
- Zero-shot: When intent categories are self-explanatory
- Few-shot: When categories could overlap or when edge cases need clarification

---

## Comparison 9: Question Answering from Context

### Zero-Shot
```
Based on the following passage, answer the question.
If the answer is not found in the passage, say "Not mentioned."

Passage: "The company reported revenue of $4.2 billion for
fiscal year 2024, a 12% increase from the prior year. Operating
margins improved to 18.5%, driven by cost optimization
initiatives. The company plans to invest $500 million in R&D
during fiscal year 2025."

Question: What was the operating margin?
Answer:
```

### Few-Shot
```
Answer questions based on the passage. If the information is
not in the passage, respond with "Not mentioned in the text."

Passage: "Apple sold 230 million iPhones in 2023."
Question: "How many iPads were sold?"
Answer: Not mentioned in the text.

Passage: "The temperature in Phoenix reached 115°F on July 4th."
Question: "What was the temperature in Phoenix on July 4th?"
Answer: 115°F

Passage: "The company reported revenue of $4.2 billion for
fiscal year 2024, a 12% increase from the prior year. Operating
margins improved to 18.5%, driven by cost optimization
initiatives."
Question: "What was the operating margin?"
Answer:
```

**When to use which:**
- Zero-shot: Simple, direct factual extraction
- Few-shot: When you need the model to handle "not found" cases correctly or maintain a specific answer format

---

## Comparison 10: Email Classification

### Zero-Shot
```
Classify this email as one of: URGENT, NORMAL, LOW_PRIORITY, SPAM

Subject: "Re: Server outage affecting production environment"
Body: "Team, our production servers went down at 3:47 AM.
Customer-facing services are impacted. All hands on deck.
Please join the war room immediately."

Classification:
```

### Few-Shot
```
Classify emails by priority:

Subject: "FREE IPHONE! Click here to claim your prize now!!!"
Body: "Congratulations! You have been selected..."
Classification: SPAM

Subject: "Office supply order for next week"
Body: "Hi, we need to reorder paper and toner cartridges..."
Classification: LOW_PRIORITY

Subject: "Meeting notes from today's standup"
Body: "Here are the action items from today's meeting..."
Classification: NORMAL

Subject: "CRITICAL: Customer data breach detected"
Body: "Our security team has identified unauthorized access..."
Classification: URGENT

Subject: "Re: Server outage affecting production environment"
Body: "Team, our production servers went down at 3:47 AM.
Customer-facing services are impacted. All hands on deck."
Classification:
```

**When to use which:**
- Zero-shot: When priority levels are obvious from content
- Few-shot: When you need consistent classification boundaries (what makes something URGENT vs. NORMAL)

---

## Comparison 11: Text Rewriting (Tone Change)

### Zero-Shot
```
Rewrite the following message in a polite, diplomatic tone
suitable for a business email:

"Your report is late again. This is the third time. Fix it."
```

### Few-Shot
```
Rewrite aggressive messages in a polite, diplomatic business tone:

Aggressive: "This is wrong. Redo it."
Diplomatic: "I noticed a few areas in the document that may
need revision. Could we schedule a brief call to go over
them together?"

Aggressive: "Why hasn't this been done yet?"
Diplomatic: "I wanted to check in on the status of this task.
Is there anything I can help with to move it forward?"

Aggressive: "Your report is late again. This is the third time. Fix it."
Diplomatic:
```

**When to use which:**
- Zero-shot: Simple tone shifts with clear direction
- Few-shot: When the specific level of diplomacy needs to be calibrated through examples

---

## Comparison 12: Keyword Extraction

### Zero-Shot
```
Extract the 5 most important keywords from the following text.
Return as a comma-separated list:

"Machine learning algorithms have been increasingly applied to
medical imaging analysis, particularly in detecting early-stage
breast cancer through mammography screening. Recent studies show
that deep learning models can match radiologist performance in
identifying malignant tumors."
```

### Few-Shot
```
Extract the 5 most important keywords as a comma-separated list:

Text: "Cloud computing has transformed how businesses manage their
IT infrastructure, enabling scalable solutions through services
like AWS, Azure, and Google Cloud Platform."
Keywords: cloud computing, IT infrastructure, scalable solutions, AWS, businesses

Text: "The Paris Agreement established a framework for global climate
action, setting targets to limit temperature rise to 1.5 degrees
Celsius above pre-industrial levels."
Keywords: Paris Agreement, climate action, temperature rise, 1.5 degrees, pre-industrial levels

Text: "Machine learning algorithms have been increasingly applied to
medical imaging analysis, particularly in detecting early-stage
breast cancer through mammography screening."
Keywords:
```

**When to use which:**
- Zero-shot: When "important" is straightforward
- Few-shot: When you need a specific keyword style (single words vs. phrases, technical vs. general)

---

## Comparison 13: Pros and Cons Analysis

### Zero-Shot
```
List 3 pros and 3 cons of working remotely from home.
Be specific and balanced.
```

### Few-Shot
```
Analyze pros and cons. Be specific, balanced, and provide
brief reasoning for each point.

Topic: Electric Vehicles
Pros:
1. Lower operating costs — Electricity is cheaper than gasoline, saving ~$1,000/year
2. Reduced emissions — Zero direct tailpipe emissions improve air quality
3. Lower maintenance — Fewer moving parts mean fewer repairs (no oil changes, fewer brake replacements)
Cons:
1. Higher upfront cost — Average EV costs $10,000-15,000 more than equivalent gas car
2. Range anxiety — Most EVs limited to 200-300 miles per charge
3. Charging infrastructure — Rural areas still lack adequate fast-charging stations

Topic: Working Remotely from Home
Pros:
1.
```

**When to use which:**
- Zero-shot: When you just need a quick list
- Few-shot: When you need a specific format, depth of reasoning, and balance

---

## Comparison 14: Analogies and Explanations

### Zero-Shot
```
Explain how a blockchain works using an analogy that a
12-year-old would understand. Keep it under 100 words.
```

### Few-Shot
```
Explain technical concepts using analogies for 12-year-olds (under 100 words):

Concept: API
Explanation: "Imagine you're at a restaurant. You (the customer)
don't go into the kitchen yourself. Instead, the waiter takes your
order to the kitchen and brings back your food. An API is like that
waiter — it takes your request to a computer system and brings back
the answer, without you needing to know how the kitchen works."

Concept: Cloud Computing
Explanation: "Think of it like Netflix. You don't own the movies —
they're stored somewhere else, and you stream them whenever you
want. Cloud computing works the same way with computer programs
and files. Instead of storing everything on your computer, you
access it over the internet from powerful computers somewhere else."

Concept: Blockchain
Explanation:
```

**When to use which:**
- Zero-shot: When the audience and style are clearly specified
- Few-shot: When you need a consistent analogy style and complexity level

---

## Comparison 15: Meeting Notes to Action Items

### Zero-Shot
```
Extract action items from the following meeting notes.
For each action item, include: the task, the owner,
and the deadline.

Meeting Notes:
"Sarah mentioned we need to finalize the Q1 budget by Friday.
Tom volunteered to update the project timeline and will have
it done by next Wednesday. Lisa will coordinate with the
vendor about the new pricing — she said she'd reach out by
end of day tomorrow. We also discussed the new hire — HR
(Jake) will post the job listing this week."
```

### Few-Shot
```
Extract action items from meeting notes.

Meeting Notes: "Mark will prepare the client presentation by Monday.
Anna needs to review the contract before Thursday."
Action Items:
| # | Task | Owner | Deadline |
|---|------|-------|----------|
| 1 | Prepare client presentation | Mark | Monday |
| 2 | Review contract | Anna | Thursday |

Meeting Notes: "Sarah mentioned we need to finalize the Q1 budget
by Friday. Tom volunteered to update the project timeline and will
have it done by next Wednesday. Lisa will coordinate with the vendor
about the new pricing — she said she'd reach out by end of day
tomorrow. We also discussed the new hire — HR (Jake) will post the
job listing this week."
Action Items:
```

**When to use which:**
- Zero-shot: When the instructions for format are detailed enough
- Few-shot: When you need a consistent table format and extraction style

---

## Quick Decision Guide

| Factor | Favor Zero-Shot | Favor Few-Shot |
|--------|----------------|----------------|
| Task complexity | Simple, well-defined | Complex, nuanced |
| Format requirements | Flexible | Strict |
| Token budget | Tight | Generous |
| Output consistency needed | Low | High |
| Domain specificity | General | Specialized |
| Edge case handling | Not critical | Important |
| Speed priority | High | Lower |
| Customization needed | Minimal | Significant |

---

*This reference is part of Module 03: Basic and Intermediate Prompt Techniques.*
