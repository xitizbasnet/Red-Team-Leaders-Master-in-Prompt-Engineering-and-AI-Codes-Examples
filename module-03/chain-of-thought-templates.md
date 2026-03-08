# Chain-of-Thought Prompt Templates

## Module 03 — Code and Examples

---

This reference provides 10 ready-to-use Chain-of-Thought (CoT) prompt templates for different reasoning tasks. Each template includes the structure, a worked example, and usage notes.

---

## Template 1: Mathematical Word Problems

### Template

```
Solve the following math problem step by step.

Problem: {problem_text}

Solution:
Step 1: Identify what we know (given information).
Step 2: Identify what we need to find.
Step 3: Set up the equation or calculation.
Step 4: Solve step by step, showing all arithmetic.
Step 5: Verify the answer by checking it against the original problem.

Final Answer: [answer with units]
```

### Worked Example

```
Solve the following math problem step by step.

Problem: A bakery makes 240 cookies per day. They sell 75% of
them at $2.50 each and donate the rest. How much revenue does
the bakery earn from cookie sales in a 5-day work week?

Solution:
Step 1: Identify what we know.
- Production: 240 cookies/day
- Sold: 75% of production
- Price: $2.50 per cookie
- Work week: 5 days

Step 2: Identify what we need to find.
- Total weekly revenue from cookie sales.

Step 3: Set up the calculation.
Revenue = cookies_per_day x sell_rate x price x days

Step 4: Solve.
Cookies sold per day = 240 x 0.75 = 180 cookies
Daily revenue = 180 x $2.50 = $450
Weekly revenue = $450 x 5 = $2,250

Step 5: Verify.
180 cookies/day x 5 days = 900 cookies/week
900 x $2.50 = $2,250 ✓
Also: 240 x 5 = 1,200 total cookies; 75% = 900 sold ✓

Final Answer: $2,250 per week
```

### Usage Notes
- Works well for arithmetic, algebra, and percentage problems
- The verification step catches many computational errors
- Adapt the number of steps based on problem complexity

---

## Template 2: Logical Reasoning and Deduction

### Template

```
Analyze the following logical problem step by step.

Problem: {logical_problem}

Analysis:
Step 1: List all premises (facts given).
Step 2: Identify what we need to determine.
Step 3: Apply logical rules to each premise.
Step 4: Draw intermediate conclusions.
Step 5: Combine intermediate conclusions to reach the final answer.
Step 6: Check for logical validity — does the conclusion follow
        necessarily from the premises?

Conclusion: [answer]
Confidence: [certain / probable / uncertain]
```

### Worked Example

```
Problem: In a company, all managers attend the leadership retreat.
Some employees who attend the leadership retreat are promoted within
a year. Alex is a manager. Can we conclude that Alex will be
promoted within a year?

Analysis:
Step 1: List all premises.
- P1: All managers attend the leadership retreat.
- P2: Some employees who attend the leadership retreat are
  promoted within a year.
- P3: Alex is a manager.

Step 2: What we need to determine.
- Will Alex be promoted within a year?

Step 3: Apply logical rules.
- From P1 and P3: Alex attends the leadership retreat (certain).
- From P2: SOME retreat attendees are promoted (not all).

Step 4: Intermediate conclusions.
- Alex definitely attends the retreat.
- The retreat attendees who get promoted are a subset — we do not
  know if Alex is in that subset.

Step 5: Final conclusion.
- We CANNOT conclude that Alex will be promoted. We can only
  conclude that Alex attends the retreat and is in the pool of
  people who MIGHT be promoted.

Step 6: Validity check.
- The logic is valid. "Some" does not imply "all," so attending
  the retreat is necessary but not sufficient for promotion.

Conclusion: No, we cannot conclude Alex will be promoted.
Confidence: Certain (the logical structure is clear).
```

---

## Template 3: Comparative Decision-Making

### Template

```
Help me decide between the following options using structured reasoning.

Decision: {decision_question}
Options: {option_A} vs. {option_B} [vs. {option_C}]
Key Criteria: {criteria_list}

Analysis:

Step 1: Define evaluation criteria and assign weights (importance 1-5).
Step 2: Evaluate each option against each criterion (score 1-10).
Step 3: Calculate weighted scores.
Step 4: Consider qualitative factors not captured in scoring.
Step 5: Assess risks for each option.
Step 6: Make a recommendation with reasoning.

| Criterion | Weight | {Option A} Score | {Option B} Score |
|-----------|--------|-----------------|-----------------|
| ...       | ...    | ...             | ...             |

Recommendation: [option] because [reasoning]
```

### Worked Example

```
Decision: Should we use PostgreSQL or MongoDB for our new project?
Context: E-commerce application, 50K daily users, complex product catalog

Step 1: Criteria and weights.
| Criterion | Weight (1-5) |
|-----------|-------------|
| Data consistency | 5 |
| Query flexibility | 4 |
| Scalability | 4 |
| Developer familiarity (team knows SQL) | 3 |
| Schema evolution ease | 3 |

Step 2 & 3: Evaluation and weighted scores.
| Criterion | Weight | PostgreSQL | MongoDB |
|-----------|--------|-----------|---------|
| Data consistency | 5 | 9 (45) | 6 (30) |
| Query flexibility | 4 | 8 (32) | 7 (28) |
| Scalability | 4 | 7 (28) | 9 (36) |
| Developer familiarity | 3 | 9 (27) | 5 (15) |
| Schema evolution | 3 | 5 (15) | 9 (27) |
| **Total** | | **147** | **136** |

Step 4: Qualitative factors.
- E-commerce needs ACID transactions for payments (favors PostgreSQL)
- Product catalog has varied attributes (favors MongoDB)
- PostgreSQL's JSONB column type provides document flexibility

Step 5: Risk assessment.
- PostgreSQL risk: Schema migrations more complex as product catalog evolves
- MongoDB risk: Transaction management more complex for orders/payments

Step 6: Recommendation.
PostgreSQL, because data consistency for financial transactions
is critical, the team already knows SQL, and JSONB provides
adequate flexibility for the product catalog.
```

---

## Template 4: Root Cause Analysis

### Template

```
Analyze the following problem to identify the root cause.

Problem: {problem_description}
Symptoms: {observed_symptoms}

Root Cause Analysis:

Step 1: Clearly state the problem and its impact.
Step 2: List all observed symptoms.
Step 3: For each symptom, ask "Why does this happen?" (5 Whys technique).
Step 4: Identify common threads across symptom analyses.
Step 5: Determine the root cause (the deepest "why" that explains
        multiple symptoms).
Step 6: Validate: If we fix this root cause, would all symptoms
        be resolved?

Root Cause: [identified root cause]
Evidence: [what supports this conclusion]
Recommended Fix: [action to address root cause]
```

### Worked Example

```
Problem: Customer complaints increased 40% in the last month.
Symptoms: Longer response times, incorrect order fulfillments,
missed delivery windows.

Step 1: Problem statement.
Customer complaints rose from ~50/week to ~70/week.
Impact: NPS dropped 12 points; 5% increase in churn risk.

Step 2: Symptoms.
- Support response time: 4 hours -> 12 hours
- Order accuracy: 98% -> 91%
- On-time delivery: 95% -> 82%

Step 3: Five Whys.

Symptom: Longer response times
Why? -> Support team is overwhelmed with tickets
Why? -> More tickets being generated due to order errors
Why? -> Order fulfillment system has more errors
Why? -> New warehouse management system was deployed 5 weeks ago
Why? -> Inadequate testing before go-live

Symptom: Incorrect orders
Why? -> Wrong items being picked
Why? -> New WMS displays item locations differently
Why? -> Staff not fully trained on new interface
Why? -> Training was 2 hours; should have been 2 days
Why? -> Go-live timeline was rushed

Step 4: Common threads.
Both lead back to the new warehouse management system deployment.

Step 5: Root cause.
The WMS was deployed with insufficient testing and inadequate
staff training, causing fulfillment errors that cascaded into
delivery delays and support overload.

Step 6: Validation.
If staff were properly trained and the system bugs fixed,
order accuracy would improve, reducing support tickets and
restoring delivery timelines. Yes, this explains all symptoms.

Root Cause: Rushed WMS deployment with inadequate testing and training
Evidence: Timeline correlation (problems started 5 weeks ago = deployment date)
Recommended Fix:
1. Immediate: Additional staff training on new WMS (this week)
2. Short-term: Patch critical WMS bugs (2 weeks)
3. Long-term: Establish proper UAT process for future system changes
```

---

## Template 5: Ethical Analysis

### Template

```
Analyze the following situation from an ethical perspective.

Situation: {ethical_dilemma}

Ethical Analysis:

Step 1: Identify the stakeholders (who is affected).
Step 2: Identify the ethical principles at stake.
Step 3: Analyze from a utilitarian perspective (greatest good
        for the greatest number).
Step 4: Analyze from a deontological perspective (duty and rights).
Step 5: Analyze from a virtue ethics perspective (what would a
        virtuous person do).
Step 6: Identify potential unintended consequences.
Step 7: Synthesize a recommendation balancing all perspectives.

Recommendation: [action]
Key Tradeoff: [what is sacrificed vs. gained]
```

### Worked Example

```
Situation: A company discovers that its AI hiring tool has a
bias against candidates from certain zip codes, which correlates
with racial demographics. The tool has been in use for 6 months
and has processed 5,000 applications.

Step 1: Stakeholders.
- Candidates who were unfairly rejected
- Candidates who benefited from the bias
- Current employees hired through the biased system
- The company's HR team
- Company leadership and shareholders
- The broader community

Step 2: Ethical principles at stake.
- Fairness and equal opportunity
- Transparency and honesty
- Responsibility and accountability
- Non-maleficence (do no harm)
- Justice

Step 3: Utilitarian analysis.
Continuing to use the biased tool harms a large number of
candidates. Removing it benefits the majority. Disclosing
the bias enables affected candidates to reapply.
Greatest good: Stop, disclose, remediate.

Step 4: Deontological analysis.
The company has a duty to treat all applicants fairly.
Using a biased tool violates the categorical imperative
(you would not want to be judged by a biased system).
Duty: Immediately stop using the tool and notify affected parties.

Step 5: Virtue ethics analysis.
A virtuous company would prioritize honesty and fairness.
They would take responsibility rather than cover up the problem.
Virtuous action: Full transparency and proactive remediation.

Step 6: Unintended consequences.
- Disclosure may lead to lawsuits
- Reassessing 5,000 applications is costly
- Public trust may be damaged (but worse if discovered later)
- Other companies using similar tools may face scrutiny

Step 7: Synthesis.
All three ethical frameworks align: stop the tool immediately,
disclose the bias to affected parties, offer re-evaluation
of rejected candidates, and implement bias testing for all
future AI tools.

Recommendation: Immediately deactivate the tool, conduct an
audit, notify affected candidates, and offer re-review.
Key Tradeoff: Short-term legal and reputational risk vs.
long-term trust, fairness, and regulatory compliance.
```

---

## Template 6: Scientific Hypothesis Evaluation

### Template

```
Evaluate the following scientific claim using critical reasoning.

Claim: {claim}
Evidence provided: {evidence}

Evaluation:

Step 1: State the claim precisely.
Step 2: Identify the type of evidence (anecdotal, correlational,
        experimental, meta-analysis).
Step 3: Evaluate the strength of the evidence.
Step 4: Identify potential confounding variables.
Step 5: Consider alternative explanations.
Step 6: Assess reproducibility and consensus.
Step 7: Rate the claim on a confidence scale.

Verdict: [Strongly Supported / Moderately Supported / Weakly
         Supported / Not Supported / Contradicted by Evidence]
Key Caveat: [most important limitation]
```

---

## Template 7: Financial Analysis

### Template

```
Analyze the following financial situation step by step.

Data: {financial_data}
Question: {financial_question}

Analysis:

Step 1: Identify the relevant financial metrics.
Step 2: Calculate key ratios or figures.
Step 3: Compare against benchmarks (industry averages, historical
        performance, targets).
Step 4: Identify trends (improving, stable, declining).
Step 5: Assess the overall financial health/situation.
Step 6: Provide actionable recommendations.

Summary: [key finding]
Recommendation: [action with reasoning]
Risk Level: [low/medium/high]
```

### Worked Example

```
Data:
- Revenue 2023: $10M | Revenue 2024: $12.5M
- COGS 2023: $6M | COGS 2024: $8M
- Operating Expenses 2023: $2.5M | Operating Expenses 2024: $3.5M
- Cash on hand: $1.2M | Monthly burn rate: $200K

Question: Is this company in a healthy financial position?

Step 1: Relevant metrics.
Revenue growth, gross margin, operating margin, runway.

Step 2: Calculate.
Revenue growth: ($12.5M - $10M) / $10M = 25%
Gross margin 2023: ($10M - $6M) / $10M = 40%
Gross margin 2024: ($12.5M - $8M) / $12.5M = 36%
Operating income 2024: $12.5M - $8M - $3.5M = $1M
Operating margin 2024: $1M / $12.5M = 8%
Runway: $1.2M / $200K = 6 months

Step 3: Benchmark comparison.
- 25% revenue growth: Strong (industry average: 15-20%)
- 36% gross margin: Below average (industry: 40-60% for SaaS)
- 8% operating margin: Below average (industry: 15-25%)
- 6 months runway: Concerning (12+ months is healthy)

Step 4: Trends.
- Revenue: Strong growth (+25%) — positive
- Gross margin: Declining (40% -> 36%) — concerning
- COGS growing faster than revenue (33% vs 25%) — red flag
- Operating expenses growing faster than revenue (40% vs 25%) — red flag

Step 5: Overall assessment.
Mixed. Top-line growth is strong but profitability is eroding.
Cost structure is scaling poorly. Limited cash runway creates
urgency.

Step 6: Recommendations.
1. Investigate COGS increase — why are costs growing faster
   than revenue?
2. Audit operating expenses — $1M increase needs justification
3. Urgently address runway — either raise capital or cut expenses
4. Focus on gross margin recovery before accelerating growth

Summary: Strong revenue growth masks deteriorating profitability
and dangerously low cash runway.
Recommendation: Pause growth investments and focus on unit economics.
Seek funding or cut costs within 60 days to extend runway.
Risk Level: High
```

---

## Template 8: Code Debugging

### Template

```
Debug the following code step by step.

Code:
```{language}
{code}
```

Error/Issue: {error_description}

Debugging Process:

Step 1: Understand what the code is supposed to do.
Step 2: Trace the execution with a sample input.
Step 3: Identify where the actual behavior diverges from expected.
Step 4: Diagnose the root cause of the bug.
Step 5: Propose a fix.
Step 6: Verify the fix handles edge cases.

Bug: [description]
Root Cause: [why it happens]
Fix:
```{language}
[corrected code]
```
Edge Cases to Test: [list]
```

---

## Template 9: Strategic Planning

### Template

```
Develop a strategic plan for the following objective.

Objective: {strategic_objective}
Context: {current_situation}
Constraints: {constraints}
Timeline: {timeline}

Strategic Analysis:

Step 1: Assess the current state (where are we now).
Step 2: Define the target state (where do we want to be).
Step 3: Identify the gap between current and target state.
Step 4: Generate strategic options to close the gap.
Step 5: Evaluate each option (feasibility, impact, risk, cost).
Step 6: Select the optimal strategy.
Step 7: Define milestones and success metrics.
Step 8: Identify risks and mitigation strategies.

Strategy: [selected approach]
Key Milestones:
- Month 1-3: [milestone]
- Month 4-6: [milestone]
- Month 7-12: [milestone]
Success Metrics: [how we measure progress]
Top 3 Risks: [risk + mitigation]
```

---

## Template 10: Argument Evaluation

### Template

```
Evaluate the strength of the following argument.

Argument: {argument_text}

Critical Evaluation:

Step 1: Identify the main claim (conclusion).
Step 2: Identify the supporting premises.
Step 3: Evaluate each premise: Is it true? Is it relevant?
        Is it sufficient?
Step 4: Identify logical fallacies (if any).
Step 5: Identify unstated assumptions.
Step 6: Consider counterarguments.
Step 7: Assess the overall argument strength.

Main Claim: [what the argument concludes]
Premises: [numbered list]
Fallacies Found: [list or "None identified"]
Unstated Assumptions: [list]
Strongest Counterargument: [description]
Overall Strength: [Strong / Moderate / Weak / Fallacious]
Explanation: [why this rating]
```

### Worked Example

```
Argument: "Social media causes depression in teenagers.
Studies show that teens who use social media more than 3 hours
a day are twice as likely to report symptoms of depression.
Therefore, we should ban social media for everyone under 18."

Step 1: Main claim.
Social media should be banned for everyone under 18.

Step 2: Premises.
P1: Social media causes depression in teenagers.
P2: Teens using social media 3+ hours/day are 2x likely to
    report depression symptoms.
P3: (Implied) Banning is the appropriate response.

Step 3: Evaluate premises.
P1: Stated as fact but the evidence (P2) only shows correlation,
    not causation. Depressed teens might use social media more
    (reverse causation).
P2: May be true but "report symptoms" is self-reported data,
    which has limitations.
P3: Banning is an extreme measure. Not supported by the evidence
    strength.

Step 4: Logical fallacies.
- Correlation-causation fallacy (P2 supports correlation, P1
  claims causation)
- False dichotomy (either unrestricted access or complete ban)
- Hasty generalization (applies to all teens based on 3+ hour users)

Step 5: Unstated assumptions.
- That the correlation is not due to a third variable
- That banning is enforceable
- That banning would not have negative consequences
- That no level of social media use is acceptable

Step 6: Counterarguments.
- Social media provides important social connection for teens
- Moderate use might not be harmful
- Education about healthy use might be more effective than banning
- Banning may push usage underground, making it harder to monitor

Step 7: Overall assessment.

Main Claim: Ban social media for under-18s
Fallacies Found: Correlation-causation, false dichotomy, hasty generalization
Unstated Assumptions: Causal link, enforceability, no positive effects
Strongest Counterargument: The evidence shows correlation, not causation;
  education and moderation may be more effective than prohibition
Overall Strength: Weak
Explanation: The argument relies on a causal claim that the evidence
  does not support, proposes an extreme solution without considering
  alternatives, and ignores potential benefits of the technology.
```

---

## Usage Guide: Selecting the Right Template

| If your task involves... | Use Template # |
|--------------------------|----------------|
| Arithmetic or word problems | 1: Mathematical Word Problems |
| Logical deductions or syllogisms | 2: Logical Reasoning |
| Choosing between options | 3: Comparative Decision-Making |
| Diagnosing why something went wrong | 4: Root Cause Analysis |
| Ethical dilemmas or policy decisions | 5: Ethical Analysis |
| Evaluating scientific claims | 6: Scientific Hypothesis Evaluation |
| Financial data interpretation | 7: Financial Analysis |
| Finding bugs in code | 8: Code Debugging |
| Planning a project or initiative | 9: Strategic Planning |
| Assessing whether an argument is sound | 10: Argument Evaluation |

---

*This reference is part of Module 03: Basic and Intermediate Prompt Techniques.*
