# Industry Prompt Libraries

## Code and Examples — Module 10

A comprehensive collection of prompt templates organized by industry. Each section contains tested, production-ready prompts that can be customized for specific use cases.

---

## Table of Contents

1. [Healthcare](#1-healthcare)
2. [Legal](#2-legal)
3. [Finance](#3-finance)
4. [Human Resources](#4-human-resources)
5. [Sales](#5-sales)
6. [Education](#6-education)
7. [Real Estate](#7-real-estate)
8. [Consulting](#8-consulting)
9. [Engineering](#9-engineering)
10. [Creative](#10-creative)

---

## 1. Healthcare

### 1.1 Clinical Documentation — SOAP Note

```
Role: Clinical documentation assistant
Task: Organize the following raw clinical notes into a SOAP note format.

Raw notes:
"""
[INSERT RAW CLINICAL NOTES]
"""

Rules:
- Maintain all medical terminology exactly as provided
- Do not add diagnoses or clinical interpretations not in the source
- Mark incomplete sections with [VERIFY WITH PROVIDER]
- Use standard medical abbreviations where appropriate
- Separate each SOAP section clearly

Output format:
S (Subjective): Patient-reported symptoms, history
O (Objective): Vital signs, exam findings, lab results
A (Assessment): Clinical impression, differential diagnoses
P (Plan): Treatment plan, follow-up, prescriptions
```

### 1.2 Patient Education Material

```
Convert the following medical information into patient-friendly language:

Medical information:
"""
[INSERT MEDICAL CONTENT]
"""

Requirements:
- Reading level: 6th grade (Flesch-Kincaid)
- Short sentences (under 15 words)
- Define every medical term in plain language
- Use "you" and "your" to speak directly to the patient
- Include a "Key Points" summary (3-5 bullets)
- Include a "When to Call Your Doctor" section
- Avoid negative or fear-inducing language where possible

Language: [ENGLISH / SPECIFY OTHER]

DISCLAIMER: This is supplementary patient education material and
does not replace medical advice from your healthcare provider.
```

### 1.3 Medical Literature Search Strategy

```
I need a literature search strategy for: [RESEARCH QUESTION]

Provide:
1. PICO framework breakdown
2. MeSH terms for each concept
3. Boolean search strings for PubMed
4. Suggested inclusion/exclusion criteria
5. Recommended secondary databases to search

Mark any uncertain MeSH terms with [VERIFY].
```

### 1.4 Medication Reconciliation

```
Review the following medication list for a [AGE]-year-old patient
with [CONDITIONS]:

Medications:
[LIST ALL MEDICATIONS WITH DOSES]

Identify:
1. Potential drug-drug interactions (severity: major/moderate/minor)
2. Therapeutic duplications
3. Potentially inappropriate medications (Beers criteria if age 65+)
4. Missing recommended therapies based on conditions listed
5. Dosing concerns

NOTE: Screening tool only. Verify with pharmacist or prescriber.
```

### 1.5 Telemedicine Visit Template

```
Create a structured telemedicine visit documentation template for
[SPECIALTY] including:

1. Technical readiness checklist
2. Verbal consent script for telehealth
3. History-taking prompts adapted for virtual setting
4. Virtual examination guidance
5. Documentation template with telehealth-specific fields
6. Appropriate billing codes
7. Follow-up and escalation criteria
```

---

## 2. Legal

### 2.1 Case Law Research

```
Research the following legal question:
"[LEGAL QUESTION]"

Jurisdiction: [SPECIFY]
Area of law: [SPECIFY]

Provide:
1. Governing legal principles
2. Seminal cases (with citations — mark uncertain ones with [VERIFY])
3. Recent developments
4. Relevant statutes
5. Circuit splits or conflicting authority

CRITICAL: I will verify every citation. Do not fabricate citations.
If uncertain, describe the case without a citation.
```

### 2.2 Contract Risk Analysis

```
Review this contract clause from [PARTY]'s perspective:

Contract type: [TYPE]
Clause:
"""
[INSERT CLAUSE]
"""

Analyze:
1. Plain-language summary
2. Obligations per party
3. Risks to my client (rated HIGH/MEDIUM/LOW)
4. Missing protections
5. Suggested revision language
6. Enforceability concerns
```

### 2.3 Legal Memo (IRAC)

```
Draft a legal memo in IRAC format:

Question: [LEGAL QUESTION]
Jurisdiction: [SPECIFY]
Facts: [BRIEF FACTS]

Structure: Issue → Rule (with citations) → Application → Conclusion

Include counterarguments. Flag uncertain citations with [VERIFY].
Length: approximately [WORD COUNT] words.
```

### 2.4 Compliance Gap Analysis

```
Assess compliance of [COMPANY TYPE] against [REGULATION]:

Current practices:
"""
[DESCRIBE PRACTICES]
"""

For each requirement: state the requirement, assess compliance status
(COMPLIANT / PARTIALLY / NON-COMPLIANT / UNABLE TO ASSESS), identify
gaps, recommend remediation, and prioritize by risk.
```

### 2.5 Discovery Document Review Protocol

```
Create a document review protocol for [CASE TYPE]:

Include:
1. Issue tags with definitions
2. Privilege categories
3. Relevance criteria per claim
4. Hot document indicators
5. Confidentiality tiers
6. Quality control sampling procedures
7. Escalation triggers
```

---

## 3. Finance

### 3.1 Financial Statement Analysis

```
Analyze the following financial data for [COMPANY]:

[INSERT FINANCIAL DATA — 3 YEARS]

Provide:
1. Profitability ratios and trends
2. Liquidity assessment
3. Leverage analysis
4. Efficiency metrics
5. Cash flow quality
6. Red flags or concerns
7. Peer comparison framework

Present key metrics in table format with trend indicators.
Not investment advice. Verify calculations independently.
```

### 3.2 Earnings Call Analysis

```
Analyze this earnings call transcript:
"""
[INSERT TRANSCRIPT]
"""

Assess:
1. Key metrics vs. expectations
2. Management tone (confident/cautious/defensive)
3. Forward guidance
4. Strategic shifts
5. Analyst concerns
6. Evasive responses
7. Red flags
8. Investment implications (1 paragraph)
```

### 3.3 DCF Valuation Framework

```
Structure a DCF valuation for [COMPANY]:
- Revenue: [CURRENT]
- EBITDA: [CURRENT]
- Industry: [INDUSTRY]

Provide:
1. Revenue projection methodology
2. Key assumptions (bull/base/bear)
3. WACC calculation framework
4. Terminal value approach
5. Sensitivity analysis variables
6. Sanity checks
```

### 3.4 Credit Risk Assessment

```
Assess credit risk for [ENTITY]:

Financial data:
"""
[INSERT DATA]
"""

Evaluate:
1. Leverage and coverage ratios
2. Liquidity and cash flow stability
3. Industry and competitive position
4. Management quality indicators
5. Suggested internal rating (map to S&P equivalent)
6. Top 5 monitoring triggers
```

### 3.5 Budget Variance Analysis

```
Analyze this budget vs. actual performance for [PERIOD]:

Data:
"""
[INSERT: Line item, Budget, Actual, Variance]
"""

Provide:
1. Executive summary of overall performance
2. Material variances (>5%) with root cause hypotheses
3. Favorable and unfavorable trends
4. Recommendations for next period
5. Risks and mitigation steps

Tone: Professional, balanced. Audience: [SPECIFY].
```

---

## 4. Human Resources

### 4.1 Job Description Writer

```
Create a job description for [TITLE] at [COMPANY TYPE]:

Details: [DEPARTMENT, LEVEL, LOCATION, REPORTS TO]

Include:
1. Clear, non-inflated title
2. Compelling company description (2-3 sentences)
3. Role summary
4. 8-10 responsibilities (action verbs, priority order)
5. Required qualifications (true requirements only)
6. Preferred qualifications
7. Benefits and culture highlights
8. Application instructions

Use gender-neutral, inclusive language. Avoid jargon.
Include a diversity encouragement statement.
```

### 4.2 Behavioral Interview Questions

```
Generate behavioral interview questions for [POSITION]:

Competencies to assess: [LIST 4-5 COMPETENCIES]

For each competency:
- 2 STAR-format questions
- 3 follow-up probes
- Strong response indicators
- Weak response indicators
- Scoring guide (1-5 scale with descriptions)

Ensure compliance with employment law (no protected characteristic questions).
```

### 4.3 Performance Review Feedback

```
Write performance review feedback for:

Situation: [DESCRIBE PERFORMANCE]
Competency: [AREA]
Level: [EXCEEDS / MEETS / BELOW EXPECTATIONS]
Examples: [2-3 SPECIFIC SITUATIONS]

Provide:
1. Summary statement
2. Specific behavioral examples
3. Impact on team/organization
4. Actionable recommendations
5. Development resources

Tone: [Direct / Encouraging / Developmental]
Focus on behavior, not personality. Avoid biased language.
```

### 4.4 90-Day Onboarding Plan

```
Create a 90-day onboarding plan for [POSITION] in [DEPARTMENT]:

Week 1: Orientation (day-by-day schedule, key meetings, setup)
Weeks 2-4: Learning (training, shadowing, initial assignments)
Weeks 5-8: Building (increasing responsibility, cross-functional exposure)
Weeks 9-12: Independence (full ownership, 90-day review)

Include: checklists, manager talking points, self-assessment templates.
```

### 4.5 Employee Engagement Survey

```
Design a [NUMBER]-question engagement survey covering:
1. Job satisfaction
2. Manager effectiveness
3. Growth opportunities
4. Work-life balance
5. Company culture
6. Overall engagement

Per dimension: 3-4 Likert scale + 1 open-ended question.
Include eNPS question and demographic fields.
Estimated completion: under [MINUTES] minutes.
```

---

## 5. Sales

### 5.1 Elevator Pitch

```
Create 3 elevator pitch versions for [PRODUCT/SERVICE]:

Target: [BUYER PERSONA]
Problem solved: [PROBLEM]
Key differentiators: [LIST 3]

Versions:
1. 30-second (networking)
2. 2-minute (discovery call)
3. 5-minute (presentation opening)

Focus on buyer's perspective. Avoid buzzwords.
End each with a low-pressure call to action.
```

### 5.2 Prospect Research Brief

```
Create a pre-call research brief for:

Company: [NAME]
Contact: [NAME, TITLE]
Our product: [WHAT WE SELL]

Include:
1. Company overview and strategic priorities
2. 3-5 likely pain points
3. Competitive landscape
4. 3 personalized conversation starters
5. Recommended call strategy
6. Next step to propose

NOTE: Verify company-specific information before outreach.
```

### 5.3 Objection Handling

```
Create objection handling scripts for [PRODUCT/SERVICE]:

For each common objection:
1. "Too expensive"
2. "Not the right time"
3. "Happy with current solution"
4. "Need to check with my boss"
5. "Looking at [COMPETITOR]"

Provide: Acknowledge → Explore (questions) → Respond (2-3 approaches)
→ Evidence → Redirect forward

Tone: Empathetic, never dismissive or combative.
```

### 5.4 Sales Email Sequence

```
Create a 5-email prospecting sequence:

Target: [TITLE, INDUSTRY, COMPANY SIZE]
Pain points: [LIST]

Email 1 (Day 1): Initial outreach — under 100 words
Email 2 (Day 3): Value-add insight — under 80 words
Email 3 (Day 7): Social proof — under 100 words
Email 4 (Day 14): Different angle — under 80 words
Email 5 (Day 21): Break-up — under 60 words

Include: 3 subject lines per email, personalization tokens [BRACKETS],
mobile-optimized format, CAN-SPAM compliance.
```

### 5.5 Competitive Battle Card

```
Create a battle card: Us ([PRODUCT]) vs. [COMPETITOR]:

1. Feature comparison matrix (15 features)
2. Our top 5 advantages with talking points
3. Their top 5 claims and how to counter each
4. Trap questions that favor us
5. "Do NOT say" list
6. Win/loss patterns

Keep factual and professional.
```

---

## 6. Education

### 6.1 Lesson Plan Generator

```
Create a detailed lesson plan for:

Subject: [SUBJECT]
Topic: [TOPIC]
Grade/Level: [LEVEL]
Duration: [MINUTES]
Learning objectives: [LIST 3-4]

Include:
1. Warm-up/hook activity (5 min)
2. Direct instruction (15 min)
3. Guided practice (15 min)
4. Independent practice (10 min)
5. Assessment check (5 min)
6. Closure and preview (5 min)

Include differentiation strategies for advanced, on-level,
and struggling learners. List materials needed.
```

### 6.2 Assessment Question Generator

```
Create a balanced assessment for [SUBJECT] — [TOPIC]:

Question types:
- 10 multiple choice (varied difficulty)
- 5 short answer
- 2 extended response
- 1 application/analysis question

Align each question to a specific learning objective.
Include answer key with scoring rubric for extended responses.
Bloom's taxonomy distribution: Remember (20%), Understand (25%),
Apply (25%), Analyze (20%), Evaluate/Create (10%).
```

### 6.3 Rubric Creator

```
Create a detailed rubric for [ASSIGNMENT TYPE]:

Criteria to assess: [LIST 4-6 CRITERIA]

For each criterion:
- Exemplary (4): Description
- Proficient (3): Description
- Developing (2): Description
- Beginning (1): Description

Include: point totals, grade conversion chart, student-friendly language.
```

### 6.4 Differentiated Instruction Planner

```
Adapt the following lesson for differentiated instruction:

Original lesson: [DESCRIBE]
Student population: [DESCRIBE DIVERSITY]

Provide modifications for:
1. Advanced learners (extension activities)
2. English Language Learners (scaffolding)
3. Students with learning disabilities (accommodations)
4. Visual, auditory, and kinesthetic learners

Maintain the same learning objectives across all modifications.
```

### 6.5 Parent Communication Templates

```
Write a [TYPE] communication to parents regarding [TOPIC]:

Types: progress report / behavior concern / positive update /
event invitation / policy change

Tone: Professional, warm, collaborative
Reading level: General public
Include: specific details, action items, contact information

Ensure cultural sensitivity and avoid assumptions about
family structure.
```

---

## 7. Real Estate

### 7.1 Property Listing Description

```
Write a compelling property listing for:

Property: [TYPE — house/condo/commercial]
Location: [ADDRESS/NEIGHBORHOOD]
Key features: [LIST 5-8 FEATURES]
Price: [PRICE]
Target buyer: [DESCRIBE IDEAL BUYER]

Write 3 versions:
1. MLS listing (factual, 200 words max)
2. Marketing description (emotional, 300 words)
3. Social media post (engaging, 100 words + hashtags)

Highlight lifestyle benefits, not just features.
Comply with Fair Housing Act (no discriminatory language).
```

### 7.2 Market Analysis Report

```
Create a comparative market analysis framework for [PROPERTY TYPE]
in [LOCATION]:

Include:
1. Active listings comparison (3-5 comps)
2. Recently sold comparison (3-5 comps)
3. Price per square foot analysis
4. Days on market trends
5. Pricing recommendation with justification
6. Market condition assessment (buyer's/seller's/balanced)

Format as a client-ready report.
```

### 7.3 Buyer Needs Assessment

```
Create a comprehensive buyer needs assessment questionnaire:

Sections:
1. Budget and financing (pre-approval, down payment, monthly target)
2. Location preferences (commute, schools, amenities)
3. Property requirements (size, bedrooms, features)
4. Lifestyle considerations (hobbies, entertaining, pets)
5. Timeline and urgency
6. Deal-breakers and must-haves (ranked priority)

Include follow-up questions to uncover unstated preferences.
```

### 7.4 Negotiation Strategy

```
Develop a negotiation strategy for [BUYER/SELLER]:

Situation: [DESCRIBE]
Asking price: [PRICE]
Market conditions: [DESCRIBE]
Competition: [DESCRIBE]
Client priorities: [LIST]

Provide:
1. Recommended initial offer/counter with justification
2. Concession strategy (what to give, what to get)
3. Contingency recommendations
4. Escalation points and walk-away triggers
5. Closing timeline strategy
```

### 7.5 Investment Property Analysis

```
Analyze this investment property opportunity:

Property: [DETAILS]
Purchase price: [PRICE]
Estimated rental income: [MONTHLY]
Estimated expenses: [LIST]

Calculate and analyze:
1. Cap rate
2. Cash-on-cash return
3. Gross rent multiplier
4. Monthly cash flow
5. 5-year projected returns
6. Risk factors
7. Comparison to alternative investments
```

---

## 8. Consulting

### 8.1 Client Proposal

```
Draft a consulting proposal for [CLIENT]:

Engagement: [TYPE — strategy, operations, technology, etc.]
Problem: [DESCRIBE CLIENT CHALLENGE]
Our approach: [METHODOLOGY]

Sections:
1. Executive summary
2. Understanding of the challenge
3. Proposed approach and methodology
4. Deliverables and timeline
5. Team and qualifications
6. Investment and payment terms
7. Next steps

Tone: Confident, client-focused, value-oriented.
Length: [PAGES].
```

### 8.2 SWOT Analysis

```
Conduct a SWOT analysis for [ORGANIZATION/PRODUCT]:

Context: [DESCRIBE SITUATION]
Industry: [INDUSTRY]

Provide:
1. Strengths (internal, positive) — 5-7 factors with evidence
2. Weaknesses (internal, negative) — 5-7 factors with evidence
3. Opportunities (external, positive) — 5-7 factors with evidence
4. Threats (external, negative) — 5-7 factors with evidence

For each factor: describe it, assess its significance (HIGH/MEDIUM/LOW),
and suggest a strategic response.

Include a SWOT matrix visualization and strategic priorities summary.
```

### 8.3 Stakeholder Analysis

```
Conduct a stakeholder analysis for [PROJECT/INITIATIVE]:

Known stakeholders: [LIST]

For each stakeholder:
1. Name/role
2. Interest in the project (what they care about)
3. Influence level (HIGH/MEDIUM/LOW)
4. Support level (CHAMPION/SUPPORTER/NEUTRAL/CRITIC/BLOCKER)
5. Key concerns
6. Engagement strategy
7. Communication approach and frequency

Create a stakeholder influence/interest matrix.
Recommend a stakeholder management plan.
```

### 8.4 Change Management Plan

```
Design a change management plan for [CHANGE INITIATIVE]:

Change description: [DESCRIBE]
Affected population: [WHO AND HOW MANY]
Timeline: [TIMELINE]

Using the ADKAR model, address:
1. Awareness: How to communicate the need for change
2. Desire: How to build motivation to support change
3. Knowledge: How to provide education and training
4. Ability: How to enable the change in practice
5. Reinforcement: How to sustain the change

Include: communication plan, training plan, resistance management,
success metrics, and risk mitigation.
```

### 8.5 Executive Presentation Outline

```
Create an executive presentation outline for [TOPIC]:

Audience: [C-SUITE / BOARD / INVESTORS]
Duration: [MINUTES]
Objective: [DECISION NEEDED / INFORMATION SHARING / APPROVAL]

Structure:
1. Opening hook (1 slide)
2. Executive summary (1 slide)
3. Situation analysis (2-3 slides)
4. Recommendation (2-3 slides)
5. Implementation plan (1-2 slides)
6. Financial impact (1 slide)
7. Risks and mitigation (1 slide)
8. Ask/decision needed (1 slide)

For each slide: headline, key message, supporting data points,
speaker notes.

Follow the Pyramid Principle: lead with the answer, then support.
```

---

## 9. Engineering

### 9.1 Technical Requirements Document

```
Create a technical requirements document for [SYSTEM/FEATURE]:

Context: [DESCRIBE PROJECT]
Stakeholders: [LIST]

Sections:
1. Purpose and scope
2. Functional requirements (numbered, testable)
3. Non-functional requirements (performance, security, scalability)
4. System interfaces and integrations
5. Data requirements
6. Constraints and assumptions
7. Acceptance criteria for each requirement
8. Priority (Must have / Should have / Could have / Won't have)

Use the MoSCoW prioritization framework.
Each requirement should be specific, measurable, and testable.
```

### 9.2 Code Review Checklist

```
Create a comprehensive code review checklist for [LANGUAGE/FRAMEWORK]:

Categories:
1. Functionality: Does the code do what it should?
2. Code quality: Is it readable, maintainable, DRY?
3. Performance: Are there efficiency concerns?
4. Security: Are there vulnerabilities?
5. Testing: Is it adequately tested?
6. Error handling: Are edge cases handled?
7. Documentation: Is it well-documented?
8. Architecture: Does it follow project patterns?

For each item: description, why it matters, what to look for,
common mistakes, and auto-detectable vs. manual review.
```

### 9.3 Architecture Decision Record

```
Document an architecture decision:

Title: [DECISION TITLE]
Status: [PROPOSED / ACCEPTED / DEPRECATED]
Context: [WHAT SITUATION REQUIRES THIS DECISION]

Evaluate options:

Option A: [NAME]
- Description
- Pros (3-5)
- Cons (3-5)
- Cost estimate
- Risk assessment

Option B: [NAME]
[Same structure]

Option C: [NAME]
[Same structure]

Decision: [WHICH OPTION AND WHY]
Consequences: [WHAT FOLLOWS FROM THIS DECISION]
Review date: [WHEN TO REVISIT]
```

### 9.4 Incident Post-Mortem

```
Create an incident post-mortem report:

Incident: [TITLE]
Severity: [SEV1-4]
Duration: [START TO RESOLUTION]
Impact: [WHO AND HOW AFFECTED]

Structure:
1. Executive summary
2. Timeline of events (minute-by-minute)
3. Root cause analysis (5 Whys)
4. Contributing factors
5. What went well in the response
6. What could be improved
7. Action items (owner, deadline, priority)
8. Lessons learned

Tone: Blameless. Focus on systems and processes, not individuals.
```

### 9.5 API Documentation Template

```
Document the following API endpoint:

Endpoint: [METHOD] [PATH]
Purpose: [DESCRIBE]

Generate:
1. Description and use cases
2. Authentication requirements
3. Request parameters (path, query, body) with types and validation
4. Request example (curl and code)
5. Response format with field descriptions
6. Response examples (success and error cases)
7. Error codes and troubleshooting
8. Rate limits
9. Versioning notes
10. Code examples in [LANGUAGES]
```

---

## 10. Creative

### 10.1 Brand Voice Guide

```
Create a brand voice guide for [BRAND]:

Brand personality: [DESCRIBE 3-5 TRAITS]
Target audience: [DESCRIBE]
Industry: [INDUSTRY]

Include:
1. Brand voice characteristics (3-5) with "We are / We are not" examples
2. Tone spectrum (formal ← → casual, serious ← → playful, etc.)
3. Vocabulary guidelines (preferred words, words to avoid)
4. Writing samples for different contexts:
   - Social media post
   - Email subject line
   - Product description
   - Customer service response
   - Error message
5. Do's and don'ts with examples
6. Tone adjustments by channel and situation
```

### 10.2 Content Calendar Planner

```
Create a monthly content calendar for [BRAND/TOPIC]:

Platforms: [LIST PLATFORMS]
Posting frequency: [PER PLATFORM]
Content pillars: [3-5 THEMES]

For each week:
- Content theme
- Platform-specific posts with:
  - Post type (image, video, carousel, text, story)
  - Caption/copy draft
  - Hashtag suggestions
  - Optimal posting time
  - Engagement prompt (question, CTA, poll)
- One cornerstone content piece (blog, video, podcast)

Include seasonal events, industry dates, and trending topics.
```

### 10.3 Creative Brief

```
Write a creative brief for [PROJECT TYPE]:

Client: [CLIENT]
Project: [DESCRIBE]
Objective: [WHAT SUCCESS LOOKS LIKE]

Include:
1. Background and context
2. Target audience (detailed persona)
3. Key message (single most important thing to communicate)
4. Supporting messages (3-4)
5. Tone and mood
6. Mandatory elements (logo, tagline, legal)
7. Deliverables and specifications
8. Timeline and milestones
9. Budget constraints
10. Inspiration and references
11. Success metrics
```

### 10.4 Storytelling Framework

```
Develop a story framework for [BRAND/PRODUCT]:

Story type: [ORIGIN / CUSTOMER SUCCESS / MISSION / PRODUCT]

Using the Hero's Journey adapted for brand storytelling:
1. The Ordinary World (customer's current state)
2. The Call to Adventure (the problem or opportunity)
3. Refusal of the Call (common objections or hesitations)
4. Meeting the Mentor (discovering the brand/product)
5. Crossing the Threshold (deciding to try)
6. Tests, Allies, Enemies (the experience)
7. The Reward (the transformation)
8. The Return (the new normal, now improved)

Provide 3 story examples using this framework for different channels:
1. 30-second video script
2. Long-form blog post outline
3. Social media carousel (6-8 slides)
```

### 10.5 Campaign Concept Generator

```
Generate 3 campaign concepts for [PRODUCT/SERVICE]:

Objective: [AWARENESS / ENGAGEMENT / CONVERSION]
Target: [AUDIENCE]
Budget: [RANGE]
Channels: [LIST]
Timeline: [DURATION]

For each concept:
1. Campaign name and tagline
2. Core creative idea (the big concept)
3. Key visual direction
4. Channel execution plan
5. Content pieces required
6. Estimated reach and engagement
7. Measurement plan (KPIs)

Differentiate the 3 concepts: one safe/proven, one creative/bold,
one innovative/experimental.
```

---

## Usage Guidelines

### How to Use These Prompt Libraries

1. **Select the appropriate prompt** for your task
2. **Customize all bracketed variables** with your specific information
3. **Adjust the detail level** by adding or removing requirements
4. **Test with your specific model** — different models may need adjustments
5. **Iterate based on output** — refine the prompt if results are not satisfactory
6. **Document your modifications** for future reference

### Customization Tips

- Add industry-specific terminology to improve relevance
- Adjust formality level based on your audience
- Include examples of desired output format when possible
- Specify the model you are using if it affects prompt design
- Add constraints specific to your organization's requirements

### Version Control

Track prompt modifications using this format:
```
v1.0 — [DATE] — Initial version
v1.1 — [DATE] — [Description of change]
v1.2 — [DATE] — [Description of change]
```

---

*This library is part of the Master in Prompt Engineering and AI — Module 10.*
