# Weak vs. Strong Prompts — Module 02

## 20 Before/After Prompt Comparisons

---

## How to Use This Guide

Each example shows a WEAK prompt (common mistakes) alongside a STRONG prompt (professional approach). Study the differences, identify the patterns, and apply the improvements to your own prompts.

**Legend:**
- WEAK = Common approach most people use
- STRONG = Professional prompt engineering approach
- ANALYSIS = What specifically changed and why it matters

---

## 1. Blog Post Writing

### WEAK
```
Write a blog post about artificial intelligence.
```

### STRONG
```
Role: You are a technology journalist who writes for a business
audience at publications like Harvard Business Review and MIT
Technology Review.

Task: Write a 1200-word blog post titled "5 Ways Small Businesses
Are Using AI to Cut Costs Without Cutting Staff."

Target audience: Small business owners (10-50 employees) who are
curious about AI but have no technical background.

Structure:
- Hook: Start with a specific, surprising statistic
- Introduction: Why AI is now accessible to small businesses (100 words)
- 5 sections: Each with a use case, a real-world example, estimated
  cost savings, and one actionable first step
- Conclusion: Summary + CTA to evaluate their own AI readiness

Tone: Practical, encouraging, not hype-driven. Use data over adjectives.
Avoid: "revolutionary," "game-changing," jargon without explanation.
Include: At least 3 specific dollar figures or percentages.
```

### ANALYSIS
| Element | Weak | Strong |
|---------|------|--------|
| Role | None | Technology journalist |
| Audience | None | Small business owners, non-technical |
| Topic scope | "AI" (entire field) | 5 specific cost-cutting use cases |
| Format | None | Detailed structure with sections |
| Length | None | 1200 words |
| Tone | None | Practical, encouraging, data-driven |
| Exclusions | None | Specific banned words |

---

## 2. Email Drafting

### WEAK
```
Write an email to a client.
```

### STRONG
```
Write a professional email from me (Project Manager) to our client
(Sarah Chen, VP of Operations at Meridian Corp) informing her that
the software deployment, originally scheduled for March 1, has been
delayed to March 15 due to a critical security vulnerability found
during QA testing.

Key points:
1. Acknowledge the delay and apologize for the inconvenience
2. Explain the reason transparently (security issue, not negligence)
3. Emphasize that the delay ensures a more secure product
4. Provide the revised timeline with specific milestones
5. Offer a call this week to discuss impact on her team's planning

Tone: Transparent, professional, confident (not groveling).
Length: Under 200 words.
Include: Subject line.
Do not: Blame any team member or use overly technical terms.
```

### ANALYSIS
The weak prompt provides zero context. The AI does not know the sender, recipient, purpose, content, tone, or length. The strong prompt gives the AI everything it needs to produce a ready-to-send email.

---

## 3. Code Generation

### WEAK
```
Write a login function.
```

### STRONG
```
Write a user login endpoint in Python using FastAPI with these
specifications:

Endpoint: POST /api/v1/auth/login
Input: JSON body with "email" (string) and "password" (string)
Process:
1. Validate email format (regex)
2. Query PostgreSQL database via SQLAlchemy for user by email
3. Verify password against bcrypt hash
4. Generate JWT access token (1h expiry) and refresh token (30d expiry)
5. Log the login attempt (success/failure) with timestamp and IP

Return:
- 200: { "access_token": str, "refresh_token": str, "token_type": "bearer" }
- 401: { "detail": "Invalid credentials" }
- 429: { "detail": "Too many attempts" } (after 5 failed attempts per 15 min)

Requirements:
- Type hints on all functions
- Async database operations
- Pydantic models for request/response validation
- Google-style docstrings
- Follow PEP 8

Include 5 unit tests using pytest covering: successful login,
wrong password, nonexistent user, invalid email format, and rate limiting.
```

### ANALYSIS
The weak prompt does not specify: language, framework, authentication method, security requirements, error handling, database, response format, or tests. The strong prompt eliminates ALL guesswork.

---

## 4. Data Analysis

### WEAK
```
Look at this data and tell me what you think.
```

### STRONG
```
Analyze the following monthly revenue data for our e-commerce
platform (January-December 2024).

Data:
Jan: $142K | Feb: $138K | Mar: $155K | Apr: $147K | May: $162K | Jun: $158K
Jul: $171K | Aug: $165K | Sep: $189K | Oct: $201K | Nov: $278K | Dec: $312K

Perform the following analysis:
1. Calculate MoM growth rate for each month
2. Identify the months with the strongest and weakest performance
3. Calculate Q1, Q2, Q3, Q4 totals and QoQ growth
4. Determine if there is a seasonal pattern
5. Project January 2025 revenue based on the observed trend
6. Flag any data points that seem anomalous

Present as:
- Summary table (Month | Revenue | MoM Growth %)
- Quarterly summary table
- 3-sentence narrative of the key story this data tells
- One recommended action for Q1 2025

Audience: CFO in a quarterly review meeting.
```

### ANALYSIS
The weak prompt does not specify what analysis to perform, what format to use, or what conclusions to draw. The strong prompt defines exactly what calculations, format, and conclusions are needed.

---

## 5. Summarization

### WEAK
```
Summarize this article.
```

### STRONG
```
Summarize the following article for a weekly technology newsletter
targeting CTOs at mid-size companies (500-5000 employees).

Article:
"""
[article text here]
"""

Format:
- HEADLINE: One-sentence summary of the main takeaway (under 15 words)
- KEY POINTS: 3 bullet points (max 25 words each)
- BUSINESS IMPACT: One sentence on what this means for technology leaders
- ACTION ITEM: One specific step a CTO should consider based on this

Total length: Under 150 words.
Tone: Informed, direct, no fluff.
Do NOT: Editorialize or add opinions not present in the source article.
```

### ANALYSIS
Same task, dramatically different results. The strong version defines audience, format, length, tone, and constraints.

---

## 6. Product Description

### WEAK
```
Write a description for our new headphones.
```

### STRONG
```
Write a product description for the SoundWave Pro X1 wireless headphones.

Product specs:
- Active noise cancellation (40dB reduction)
- 60-hour battery life
- Bluetooth 5.3 with multipoint connection (2 devices)
- 40mm custom titanium drivers
- Weight: 250g
- Price: $249

Target customer: Work-from-home professionals aged 28-45 who
take frequent video calls and listen to music during deep work.

Format: 80-word paragraph + 4 bullet points highlighting key features +
one-line tagline

Tone: Premium but approachable. Think Apple product page, not
audiophile review.

Focus on BENEFITS (what the user experiences), not just features
(what the product has).

Do NOT: Use "immersive," "world-class," or "next-generation."
Do NOT: Mention competitor products.
```

### ANALYSIS
| Missing in Weak | Present in Strong |
|----------------|-------------------|
| Product name and specs | Full specifications |
| Target customer | Detailed customer profile |
| Format and length | Specific structure |
| Tone guidance | Brand voice reference |
| Benefit vs. feature focus | Explicitly requested |
| Exclusions | Banned words and topics |

---

## 7. Resume Review

### WEAK
```
Review my resume.
```

### STRONG
```
Review the following resume for a Senior Product Manager position
at a Series B B2B SaaS startup.

Resume:
"""
[resume text]
"""

Job description highlights:
- 5+ years PM experience
- B2B SaaS background
- Data-driven decision making
- Cross-functional leadership
- Experience with 0-to-1 product development

Evaluate:
1. Content alignment: How well does the resume match the job requirements?
   Score each requirement (Strong Match / Partial Match / Gap)
2. Impact language: Are achievements quantified with metrics?
   Flag any bullet that lacks measurable impact
3. Structure: Is the format ATS-friendly and scannable?
4. Missing elements: What key information is absent?
5. Red flags: Anything that might concern a hiring manager?

Then provide:
- Top 3 strengths of this resume
- Top 3 specific improvements (rewrite the actual bullet points)
- An overall readiness score (1-10) for this specific role
```

### ANALYSIS
The weak prompt produces a generic review. The strong prompt targets a specific role, provides the job description, and requests structured, actionable feedback.

---

## 8. Meeting Summary

### WEAK
```
Summarize this meeting.
```

### STRONG
```
Summarize the following meeting transcript into an actionable
meeting summary.

Transcript:
"""
[meeting transcript]
"""

Output format:

## Meeting Summary
- Date: [extract from transcript]
- Attendees: [list names mentioned]
- Duration: [if mentioned]

## Decisions Made
[Numbered list — only firm decisions, not discussions]

## Action Items
| # | Action | Owner | Deadline | Priority |
|---|--------|-------|----------|----------|

## Key Discussion Points
[3-5 bullet points of important topics discussed but not yet decided]

## Open Questions
[Items that need follow-up or further discussion]

Rules:
- Only list something as a "Decision" if it was clearly agreed upon
- Only list action items that have a clear owner (ask if unclear)
- Distinguish between decisions, discussions, and suggestions
- Keep the entire summary under 400 words
```

### ANALYSIS
The strong version produces a structured, actionable document with clear categories (decisions vs. discussions vs. action items), accountability (owners, deadlines), and constraints (word limit).

---

## 9. Competitive Analysis

### WEAK
```
Compare our product to competitors.
```

### STRONG
```
Create a competitive analysis comparing our project management tool
(TaskFlow) against Asana, Monday.com, and ClickUp.

Our positioning: Best for engineering teams (10-50 people) who need
deep GitHub/GitLab integration and sprint planning.

Analysis dimensions:
| Dimension | What to evaluate |
|-----------|-----------------|
| Pricing | Free tier, per-user cost, enterprise pricing |
| Engineering features | Git integration, sprint planning, CI/CD hooks |
| Ease of use | Learning curve, onboarding time, UI complexity |
| Integrations | Number and quality of relevant integrations |
| Scalability | Performance at 50, 200, 1000 users |
| Support | Response time, channels, documentation quality |

Output:
1. Comparison table (dimensions as rows, products as columns)
2. TaskFlow's competitive advantages (top 3)
3. TaskFlow's competitive gaps (top 3)
4. Recommended positioning statement (2 sentences)
5. One feature we should build to improve competitive position

Do NOT: Unfairly disparage competitors. Present factual differences.
```

### ANALYSIS
The weak prompt does not name competitors, does not specify comparison dimensions, and does not define the output format. The strong prompt provides everything needed for a useful competitive analysis.

---

## 10. Customer Survey Questions

### WEAK
```
Write some survey questions for our customers.
```

### STRONG
```
Create a 10-question customer satisfaction survey for users of our
cloud storage platform (similar to Dropbox) who have been customers
for 6+ months.

Goals:
1. Measure overall satisfaction (NPS)
2. Identify top pain points
3. Understand feature usage patterns
4. Gauge likelihood of renewal/expansion
5. Collect testimonial-worthy feedback

Question mix:
- 2 quantitative rating questions (1-10 scale)
- 3 multiple choice questions
- 3 Likert scale questions (Strongly Disagree to Strongly Agree)
- 2 open-ended questions

Requirements:
- Questions must be unbiased (no leading questions)
- Each question should take under 15 seconds to answer
- Include the NPS question: "How likely are you to recommend..."
- Group questions logically (satisfaction, features, future)
- Include one question that identifies potential case study candidates

Provide each question with:
- The question text
- Response format (scale, MC options, or open)
- What insight this question provides
- Which business goal (1-5) it addresses
```

### ANALYSIS
The strong prompt specifies the survey goals, question types, methodological requirements (unbiased), and connects each question to a business objective.

---

## 11. Job Description

### WEAK
```
Write a job description for a developer.
```

### STRONG
```
Write a job description for a Senior Frontend Engineer at our
company (FinTech startup, 45 employees, Series A, remote-first).

Role details:
- Reports to: VP of Engineering
- Team: 4 frontend engineers, 6 backend engineers
- Product: Consumer-facing banking dashboard
- Tech stack: React 18, TypeScript, Next.js, Tailwind CSS, GraphQL
- Salary range: $150K-$180K + equity (0.05-0.1%)

Required experience:
- 5+ years frontend development
- 3+ years with React/TypeScript
- Experience with financial/regulated applications (preferred)
- Proven ability to mentor junior developers

Format:
1. About Us (3 sentences — mission, stage, culture)
2. About the Role (what they will own and build)
3. What You Will Do (5-7 bullet points of responsibilities)
4. What You Bring (5-7 requirements, clearly split into Required/Nice-to-Have)
5. What We Offer (5 benefits/perks)
6. How to Apply

Tone: Authentic, not corporate. Show personality.
Do NOT: Use "rockstar," "ninja," "guru," or any gendered language.
Do NOT: List unrealistic requirements (10 years of React experience).
Include: The salary range (transparency matters).
```

### ANALYSIS
The strong prompt provides company context, role specifics, tech stack, requirements, format structure, tone guidance, and inclusive language requirements.

---

## 12. Presentation Outline

### WEAK
```
Help me with a presentation.
```

### STRONG
```
Create a 12-slide presentation outline for a board meeting where I
(CEO) am requesting approval for a $2M investment in AI capabilities.

Context:
- Company: B2B SaaS, $15M ARR, 150 employees
- Problem: Customer churn is 4.5% monthly (industry avg is 2.5%)
- Proposal: Build AI-powered churn prediction and intervention system
- Expected ROI: Reduce churn to 2.5% within 12 months = $3.2M saved annually
- Board concern: We missed revenue targets last quarter

For each slide provide:
- Slide number and title
- 3-4 bullet points of content
- One key data point or visual suggestion
- Speaker notes (2-3 sentences of what to say)

Narrative arc: Problem → Impact → Opportunity → Solution → Investment → Returns
Lead with the business problem, not the technology solution.
Close with a clear ask and timeline for the decision.
```

### ANALYSIS
The strong prompt defines the audience (board), purpose (approval), narrative arc, and provides all the context needed to create a compelling presentation.

---

## 13. Error Message Writing

### WEAK
```
Write some error messages.
```

### STRONG
```
Write user-facing error messages for our web application's checkout
flow. The audience is non-technical consumers shopping online.

For each error, provide:
- Error code (for developer reference)
- User-facing title (clear, non-technical)
- User-facing description (explains what happened and what to do)
- Tone: Helpful, not blaming the user

Errors to write messages for:
1. Payment declined by card issuer
2. Card expired
3. Insufficient funds
4. Invalid CVV code
5. Network timeout during payment processing
6. Item went out of stock during checkout
7. Shipping address not deliverable
8. Promo code expired
9. Cart session timed out
10. Maximum quantity exceeded for an item

Requirements:
- Title: Under 8 words
- Description: Under 30 words
- Always include a next action ("Try again," "Use a different card," etc.)
- Never expose technical details (API errors, status codes)
- Never blame the user ("You entered wrong information")
- Use positive framing where possible
```

### ANALYSIS
The strong prompt specifies the context (checkout flow), audience (consumers), tone (helpful), format (title + description), constraints (word limits), and covers specific error scenarios.

---

## 14. Social Media Strategy

### WEAK
```
Give me ideas for social media.
```

### STRONG
```
Create a 4-week social media content calendar for our B2B SaaS
project management tool, targeting engineering team leads at
companies with 50-500 employees.

Platforms: LinkedIn (primary), Twitter/X (secondary)
Posting frequency: LinkedIn 3x/week, Twitter 5x/week
Brand voice: Smart, helpful, slightly irreverent. Think: a senior
engineer who is great at explaining things and has a dry sense of humor.

Content pillars (rotate evenly):
1. Product tips and shortcuts (show, don't tell)
2. Engineering leadership insights
3. Team productivity research/data
4. Customer success stories (anonymized)
5. Industry commentary and trends

For each post provide:
- Week and day
- Platform
- Content pillar
- Post text (full copy, ready to publish)
- Suggested visual type (screenshot, infographic, meme, quote card)
- Hashtags (3-5 per post)
- Goal (engagement, traffic, awareness)

Include one "hero" piece per week (longer, high-effort content).
```

### ANALYSIS
The weak prompt produces generic ideas. The strong prompt produces a ready-to-execute calendar with copy, platform strategy, content pillars, and brand voice.

---

## 15. Technical Explanation

### WEAK
```
Explain Docker.
```

### STRONG
```
Explain Docker to a backend developer who has 3 years of experience
with Python/Django but has never used containerization.

Structure:
1. THE PROBLEM (2-3 sentences): What problem does Docker solve?
   Use their Django experience as the frame — "You know when your
   app works on your machine but not on the server? Here's why..."
2. THE CORE CONCEPT (3-4 sentences): Explain containers using an
   analogy they would relate to
3. KEY TERMS: Define these in one sentence each: image, container,
   Dockerfile, Docker Compose, registry
4. FIRST STEPS: A step-by-step guide to Dockerize a Django app
   (actual commands, not pseudo-code)
5. COMMON GOTCHAS: 3 mistakes new Docker users make with Django
6. WHEN TO USE IT: Specific scenarios where Docker helps vs. overkill

Length: 800-1000 words
Tone: Peer-to-peer (senior dev to mid dev), not teacher-to-student
Do NOT: Assume knowledge of Kubernetes, cloud services, or CI/CD
```

### ANALYSIS
The strong prompt specifies the learner's exact background, uses their experience as a reference frame, provides a clear structure, and sets the appropriate peer-to-peer tone.

---

## 16. Feedback Writing

### WEAK
```
Write feedback for my employee.
```

### STRONG
```
Help me write performance feedback for a mid-level software engineer
on my team for their semi-annual review.

Employee context:
- Name: Alex (they/them)
- Role: Software Engineer II, 2 years at company
- Strengths: Excellent code quality, thorough code reviews, reliable delivery
- Growth areas: Rarely speaks up in meetings, avoids taking ownership
  of ambiguous projects, documentation is sparse
- Recent achievement: Led the migration of our auth system to OAuth 2.0
  (completed 1 week ahead of schedule)
- Recent concern: Declined to take the lead on a cross-team project,
  citing "not enough experience" despite being qualified

Write the feedback covering:
1. Summary of overall performance (2-3 sentences, positive framing)
2. Key strengths with specific examples (3 items)
3. Areas for growth with specific, actionable suggestions (2-3 items)
4. Goals for next review period (2-3 SMART goals)

Tone: Supportive, specific, growth-oriented. Use the SBI framework
(Situation-Behavior-Impact) for examples.
Length: 400-500 words
Do NOT: Use vague language like "needs improvement" without specifics
Do NOT: Compare to other team members
```

### ANALYSIS
The strong prompt provides employee context, specific examples, the desired feedback framework (SBI), and constraints against common feedback-writing mistakes.

---

## 17. Crisis Communication

### WEAK
```
Write a message about our data breach.
```

### STRONG
```
Write a customer notification email about a security incident at
our company (CloudStore, a cloud storage provider with 50,000 users).

Incident details:
- What happened: Unauthorized access to a database containing user
  email addresses and hashed (bcrypt) passwords
- When: Discovered January 15, occurred between Jan 10-14
- Impact: 12,000 users' email addresses exposed. Passwords were
  hashed and salted — no evidence of decryption. No financial data,
  files, or payment information was affected.
- Actions taken: Vulnerability patched within 2 hours of discovery,
  forced password reset for affected users, engaged third-party
  security firm for forensic investigation
- Ongoing: Investigation continues, additional security measures
  being implemented

Write the email covering:
1. Subject line (clear, not alarming)
2. What happened (factual, transparent, no downplaying)
3. What information was affected (and explicitly what was NOT affected)
4. What we have done
5. What users should do (specific steps)
6. What we are doing next
7. How to contact us with questions

Tone: Transparent, accountable, calm. No corporate-speak.
Length: 300-400 words.
Do NOT: Minimize the incident, blame third parties, or use legal hedging.
Do NOT: Start with "We take your security seriously" (overused cliche).
```

### ANALYSIS
The strong prompt provides complete incident details, required sections for legal and ethical compliance, tone guidance, and explicitly bans the most common crisis communication cliches.

---

## 18. API Request Example

### WEAK
```
Show me how to use the Stripe API.
```

### STRONG
```
Write a complete, working example of creating a Stripe checkout
session for a subscription product using the Stripe API.

Technical context:
- Language: Python 3.11
- Framework: FastAPI
- Stripe product: Monthly SaaS subscription at $49/month
- Success URL: https://app.example.com/success?session_id={CHECKOUT_SESSION_ID}
- Cancel URL: https://app.example.com/pricing

Include:
1. Required pip packages (requirements.txt format)
2. Environment variable setup (using python-dotenv)
3. FastAPI endpoint: POST /create-checkout-session
4. Webhook handler: POST /webhook for checkout.session.completed
5. Error handling for: invalid API key, network errors, Stripe errors
6. Stripe signature verification for the webhook
7. Brief inline comments explaining each step

Do NOT: Include actual API keys (use environment variable placeholders)
Do NOT: Skip error handling for brevity
Format: Complete, copy-pasteable code in a single code block
```

### ANALYSIS
The strong prompt specifies language, framework, specific Stripe product, URLs, all required components, error handling requirements, and security considerations.

---

## 19. Research Question

### WEAK
```
Tell me about climate change effects.
```

### STRONG
```
Provide a research-grade summary of the economic impact of climate
change on commercial agriculture in the US Midwest (corn belt states)
from 2020-2025.

Specifically address:
1. Yield impact: How have extreme weather events affected corn and
   soybean yields? Cite specific years and percentage impacts.
2. Cost impact: How have input costs (irrigation, insurance, adaptive
   practices) changed for Midwest farmers?
3. Market dynamics: How have climate-driven supply fluctuations
   affected commodity prices?
4. Adaptation measures: What are the top 3 adaptive strategies
   farmers are implementing and at what cost?
5. Insurance trends: How have crop insurance premiums and claims
   changed?

Quality standards:
- Cite specific studies, USDA reports, or recognized data sources
- Distinguish between established data and projections
- Note where data is uncertain or contested
- Provide specific numbers (dollar amounts, percentages, yield bushels)

Format: 1000-word research brief with numbered sections
Audience: Agricultural policy analyst
Acknowledge your knowledge cutoff when relevant.
```

### ANALYSIS
The strong prompt narrows the scope (US Midwest, specific crops, specific timeframe), defines specific questions, requires citations and data quality standards, and specifies the audience.

---

## 20. Process Documentation

### WEAK
```
Document our onboarding process.
```

### STRONG
```
Create a new employee onboarding checklist and guide for engineering
hires at our startup (45 people, remote-first, Python/React stack).

Onboarding timeline: First 30 days, broken into Week 1, Week 2,
Weeks 3-4.

For each week, provide:

## Week X

### Goals
What the new hire should achieve by end of week.

### Day-by-Day Schedule (for Week 1 only)
| Day | Morning | Afternoon |
|-----|---------|-----------|

### Checklist
- [ ] Task (Owner: [who is responsible])

### Meetings to Schedule
| Meeting | With | Purpose | Duration |

### Resources to Review
| Resource | Link Placeholder | Priority |

Cover these areas:
- IT setup (accounts, access, development environment)
- Team introductions (who they should meet and why)
- Codebase onboarding (where to start, first PR expectations)
- Culture and processes (how we work, communication norms)
- First meaningful contribution (target: ship something in Week 2)

Tone: Welcoming, organized, not overwhelming.
Include a "30-day success criteria" section at the end so the new
hire knows what "good" looks like.
```

### ANALYSIS
The strong prompt provides company context, a specific timeline structure, format for each section, all topic areas to cover, and success criteria.

---

## Summary: Patterns of Weak vs. Strong Prompts

| Pattern | Weak Prompt | Strong Prompt |
|---------|------------|---------------|
| **Scope** | Too broad | Precisely defined |
| **Audience** | Not specified | Clearly described |
| **Format** | Left to chance | Explicitly structured |
| **Length** | Uncontrolled | Bounded with word/item counts |
| **Tone** | Default AI voice | Specified with examples |
| **Context** | Missing | Sufficient and relevant |
| **Examples** | None | Included when needed |
| **Exclusions** | Not mentioned | Explicitly listed |
| **Action verb** | Vague ("help," "tell") | Specific ("analyze," "compare") |
| **Success criteria** | Undefined | Measurable and clear |

---

## The Transformation Formula

To transform any weak prompt into a strong one, add these layers:

```
1. WHO    → Define the role and audience
2. WHAT   → Specify the exact task with an action verb
3. WHY    → Provide the context and purpose
4. HOW    → Define the format, length, and structure
5. BOUNDS → Set inclusions, exclusions, and constraints
```

If your prompt is missing any of these five elements, it has room for improvement.

---

*Part of Module 02 — Introduction to Prompt Engineering*
