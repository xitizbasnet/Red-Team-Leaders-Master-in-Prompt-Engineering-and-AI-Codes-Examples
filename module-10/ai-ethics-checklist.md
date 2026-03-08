# Comprehensive AI Ethics Checklist

## Code and Examples — Module 10

A practical, actionable ethics checklist for AI projects, from initial conception through deployment and ongoing monitoring.

---

## Table of Contents

1. [How to Use This Checklist](#1-how-to-use-this-checklist)
2. [Phase 1: Project Conception](#2-phase-1-project-conception)
3. [Phase 2: Data and Training](#3-phase-2-data-and-training)
4. [Phase 3: Design and Development](#4-phase-3-design-and-development)
5. [Phase 4: Testing and Evaluation](#5-phase-4-testing-and-evaluation)
6. [Phase 5: Deployment](#6-phase-5-deployment)
7. [Phase 6: Ongoing Monitoring](#7-phase-6-ongoing-monitoring)
8. [Domain-Specific Considerations](#8-domain-specific-considerations)
9. [Ethical Red Flags](#9-ethical-red-flags)
10. [Ethics Review Documentation Template](#10-ethics-review-documentation-template)

---

## 1. How to Use This Checklist

### Purpose
This checklist provides a structured approach to identifying, assessing, and mitigating ethical risks in AI projects. It is designed for prompt engineers, AI engineers, product managers, and anyone involved in building or deploying AI systems.

### When to Use
- At the start of every new AI project
- When modifying or expanding an existing AI system
- During periodic reviews of deployed AI systems
- When a concern or incident is raised about an AI system
- Before any significant deployment or release

### How to Complete
1. Work through each phase relevant to your project stage
2. For each item, mark: PASS / CONCERN / FAIL / N/A
3. Document justification for each assessment
4. Address all CONCERN and FAIL items before proceeding
5. Have the completed checklist reviewed by a second party
6. Archive the checklist as part of project documentation

### Severity Ratings
- **CRITICAL**: Must be addressed before any deployment; potential for serious harm
- **HIGH**: Should be addressed before deployment; significant risk
- **MEDIUM**: Should be addressed; moderate risk
- **LOW**: Should be addressed when feasible; minor risk

---

## 2. Phase 1: Project Conception

### 2.1 Purpose and Need Assessment

```
[ ] P1.1 [CRITICAL] The AI system has a clearly defined, legitimate purpose
    Justification: _________________________________________________

[ ] P1.2 [HIGH] The need for AI (vs. non-AI approach) is justified
    Justification: _________________________________________________

[ ] P1.3 [HIGH] The intended benefits outweigh the identified risks
    Justification: _________________________________________________

[ ] P1.4 [MEDIUM] Alternative non-AI approaches were considered and
    documented
    Justification: _________________________________________________

[ ] P1.5 [HIGH] The AI system does not automate decisions that should
    remain with humans
    Justification: _________________________________________________
```

### 2.2 Stakeholder Impact Assessment

```
[ ] P1.6 [CRITICAL] All affected populations have been identified
    Populations: ___________________________________________________

[ ] P1.7 [CRITICAL] Potential for harm to vulnerable populations has
    been assessed
    Assessment: ____________________________________________________

[ ] P1.8 [HIGH] Stakeholder voices (especially affected communities)
    have been consulted
    Method: ________________________________________________________

[ ] P1.9 [HIGH] Potential for discriminatory impact has been assessed
    across protected characteristics (race, gender, age, disability,
    religion, national origin, etc.)
    Assessment: ____________________________________________________

[ ] P1.10 [MEDIUM] A stakeholder communication plan exists for
    transparency about AI use
    Plan: __________________________________________________________
```

### 2.3 Legal and Regulatory Compliance

```
[ ] P1.11 [CRITICAL] Applicable laws and regulations have been identified
    Regulations: ___________________________________________________

[ ] P1.12 [CRITICAL] The project complies with all applicable data
    protection laws (GDPR, CCPA, HIPAA, etc.)
    Compliance assessment: _________________________________________

[ ] P1.13 [HIGH] Intellectual property rights have been assessed
    (training data rights, output ownership)
    Assessment: ____________________________________________________

[ ] P1.14 [HIGH] Industry-specific regulations have been identified
    and compliance planned
    Regulations: ___________________________________________________

[ ] P1.15 [MEDIUM] The project's risk classification under the EU AI
    Act (or equivalent regulation) has been determined
    Classification: ________________________________________________
```

---

## 3. Phase 2: Data and Training

### 3.1 Data Collection and Consent

```
[ ] P2.1 [CRITICAL] Data used has been collected with proper consent
    or legal basis
    Legal basis: ___________________________________________________

[ ] P2.2 [CRITICAL] Data subjects have been informed about AI use
    of their data (where applicable)
    Method: ________________________________________________________

[ ] P2.3 [HIGH] Data minimization principle applied — only necessary
    data is collected
    Justification: _________________________________________________

[ ] P2.4 [HIGH] Data retention policies are defined and comply with
    regulations
    Policy: ________________________________________________________

[ ] P2.5 [MEDIUM] Mechanisms exist for data subjects to exercise their
    rights (access, deletion, correction)
    Mechanism: _____________________________________________________
```

### 3.2 Data Quality and Bias

```
[ ] P2.6 [CRITICAL] Training data has been assessed for demographic
    representation
    Assessment: ____________________________________________________

[ ] P2.7 [CRITICAL] Known historical biases in the data have been
    identified and documented
    Biases identified: _____________________________________________

[ ] P2.8 [HIGH] Mitigation strategies for identified biases have been
    implemented
    Strategies: ____________________________________________________

[ ] P2.9 [HIGH] Data labeling processes include quality checks and
    calibration
    Process: _______________________________________________________

[ ] P2.10 [MEDIUM] Data provenance is documented (source, collection
    method, date, processing)
    Documentation location: ________________________________________
```

### 3.3 Privacy and Security

```
[ ] P2.11 [CRITICAL] Personally identifiable information (PII) is
    properly protected
    Protection measures: ___________________________________________

[ ] P2.12 [CRITICAL] Data encryption is implemented at rest and in transit
    Method: ________________________________________________________

[ ] P2.13 [HIGH] Access controls limit who can access training data
    Controls: ______________________________________________________

[ ] P2.14 [HIGH] De-identification or anonymization applied where
    appropriate
    Method: ________________________________________________________

[ ] P2.15 [HIGH] Data breach response plan exists
    Plan location: _________________________________________________
```

---

## 4. Phase 3: Design and Development

### 4.1 Fairness and Non-Discrimination

```
[ ] P3.1 [CRITICAL] The system has been designed to avoid discriminatory
    outcomes across protected groups
    Design measures: _______________________________________________

[ ] P3.2 [HIGH] Fairness metrics have been defined (demographic parity,
    equalized odds, etc.)
    Metrics chosen: ________________________________________________

[ ] P3.3 [HIGH] Proxy variables that could encode protected
    characteristics have been identified and addressed
    Variables assessed: ____________________________________________

[ ] P3.4 [MEDIUM] The system performs comparably across different
    demographic groups
    Testing results: _______________________________________________

[ ] P3.5 [MEDIUM] An appeals or override mechanism exists for
    individuals affected by AI decisions
    Mechanism: _____________________________________________________
```

### 4.2 Transparency and Explainability

```
[ ] P3.6 [CRITICAL] Users are informed when they are interacting
    with AI (not deceived into thinking it is human)
    Disclosure method: _____________________________________________

[ ] P3.7 [HIGH] The system can provide meaningful explanations for
    its outputs or decisions
    Explanation approach: __________________________________________

[ ] P3.8 [HIGH] The system's limitations are clearly documented
    and communicated
    Documentation: _________________________________________________

[ ] P3.9 [MEDIUM] Technical documentation is comprehensive enough
    for external audit
    Documentation location: ________________________________________

[ ] P3.10 [MEDIUM] AI-generated content is identifiable as such
    Labeling method: _______________________________________________
```

### 4.3 Human Oversight

```
[ ] P3.11 [CRITICAL] Human oversight mechanisms are built into the
    system for high-stakes decisions
    Oversight design: ______________________________________________

[ ] P3.12 [HIGH] Users can override or correct AI decisions
    Override mechanism: ____________________________________________

[ ] P3.13 [HIGH] The level of automation is appropriate for the
    decision's impact
    Impact assessment: _____________________________________________

[ ] P3.14 [MEDIUM] Escalation paths to human reviewers are defined
    Escalation process: ____________________________________________

[ ] P3.15 [MEDIUM] Human reviewers have the information needed to
    make informed decisions
    Information provided: __________________________________________
```

### 4.4 Safety and Robustness

```
[ ] P3.16 [CRITICAL] The system includes guardrails against harmful
    outputs
    Guardrails: ____________________________________________________

[ ] P3.17 [HIGH] Adversarial testing has been conducted to identify
    vulnerabilities
    Testing approach: ______________________________________________

[ ] P3.18 [HIGH] The system degrades gracefully under unexpected
    inputs
    Failure behavior: ______________________________________________

[ ] P3.19 [HIGH] Input validation prevents injection attacks and
    manipulation
    Validation: ____________________________________________________

[ ] P3.20 [MEDIUM] Rate limits and cost caps are implemented
    Limits: ________________________________________________________
```

---

## 5. Phase 4: Testing and Evaluation

### 5.1 Bias Testing

```
[ ] P4.1 [CRITICAL] The system has been tested for disparate impact
    across demographic groups
    Testing methodology: ___________________________________________
    Results: _______________________________________________________

[ ] P4.2 [HIGH] Testing includes edge cases and underrepresented
    populations
    Edge cases tested: _____________________________________________

[ ] P4.3 [HIGH] Bias testing covers all protected characteristics
    relevant to the application
    Characteristics tested: ________________________________________

[ ] P4.4 [MEDIUM] Testing data is separate from training data
    Confirmation: __________________________________________________

[ ] P4.5 [MEDIUM] Bias testing results have been reviewed by
    diverse evaluators
    Evaluators: ____________________________________________________
```

### 5.2 Safety Testing

```
[ ] P4.6 [CRITICAL] Red-teaming has been conducted to identify
    harmful outputs
    Approach: ______________________________________________________
    Findings: ______________________________________________________

[ ] P4.7 [HIGH] The system has been tested for misinformation
    generation
    Results: _______________________________________________________

[ ] P4.8 [HIGH] The system has been tested for inappropriate
    content generation
    Results: _______________________________________________________

[ ] P4.9 [HIGH] Prompt injection and jailbreak resistance has been
    tested
    Results: _______________________________________________________

[ ] P4.10 [MEDIUM] The system handles sensitive topics appropriately
    Topics tested: _________________________________________________
```

### 5.3 Performance Evaluation

```
[ ] P4.11 [HIGH] Performance metrics are defined and measured
    Metrics: _______________________________________________________

[ ] P4.12 [HIGH] Performance is evaluated across different user
    segments and use cases
    Segments: ______________________________________________________

[ ] P4.13 [MEDIUM] Error rates and failure modes are documented
    Error rates: ___________________________________________________

[ ] P4.14 [MEDIUM] System performance under load has been tested
    Results: _______________________________________________________

[ ] P4.15 [LOW] Comparison against baseline (non-AI) performance
    has been conducted
    Comparison: ____________________________________________________
```

---

## 6. Phase 5: Deployment

### 6.1 Deployment Readiness

```
[ ] P5.1 [CRITICAL] All CRITICAL and HIGH items from previous phases
    are resolved
    Confirmation: __________________________________________________

[ ] P5.2 [CRITICAL] Incident response plan is documented and tested
    Plan location: _________________________________________________

[ ] P5.3 [HIGH] Rollback capability is in place
    Rollback process: ______________________________________________

[ ] P5.4 [HIGH] Users have been trained on appropriate AI use
    Training provided: _____________________________________________

[ ] P5.5 [HIGH] Feedback mechanisms are available for users to report
    issues
    Feedback channel: ______________________________________________
```

### 6.2 Communication and Transparency

```
[ ] P5.6 [CRITICAL] All affected parties have been notified about
    AI deployment
    Notification method: ___________________________________________

[ ] P5.7 [HIGH] Terms of use clearly describe AI capabilities and
    limitations
    Terms location: ________________________________________________

[ ] P5.8 [HIGH] Privacy policy is updated to reflect AI data
    processing
    Policy updated: ________________________________________________

[ ] P5.9 [MEDIUM] External documentation (help docs, FAQs) addresses
    AI-specific questions
    Documentation: _________________________________________________

[ ] P5.10 [MEDIUM] Media or public communication plan exists (if
    applicable)
    Plan: __________________________________________________________
```

### 6.3 Gradual Rollout

```
[ ] P5.11 [HIGH] Deployment follows a gradual rollout strategy
    (canary, phased)
    Strategy: ______________________________________________________

[ ] P5.12 [HIGH] Success criteria for expanding deployment are
    defined
    Criteria: ______________________________________________________

[ ] P5.13 [MEDIUM] A/B testing or comparison methodology is in place
    Methodology: ___________________________________________________

[ ] P5.14 [MEDIUM] Rollout can be paused or reversed at any stage
    Process: _______________________________________________________
```

---

## 7. Phase 6: Ongoing Monitoring

### 7.1 Performance Monitoring

```
[ ] P6.1 [CRITICAL] Continuous monitoring for model performance
    degradation is in place
    Monitoring tools: ______________________________________________

[ ] P6.2 [HIGH] Bias metrics are monitored continuously post-deployment
    Frequency: _____________________________________________________

[ ] P6.3 [HIGH] User feedback is collected and analyzed regularly
    Collection method: _____________________________________________

[ ] P6.4 [MEDIUM] Regular bias audits are scheduled
    Audit schedule: ________________________________________________

[ ] P6.5 [MEDIUM] Performance benchmarks are re-evaluated periodically
    Re-evaluation schedule: ________________________________________
```

### 7.2 Incident Management

```
[ ] P6.6 [CRITICAL] An incident classification and response process
    exists
    Process: _______________________________________________________

[ ] P6.7 [HIGH] Incidents are documented with root cause analysis
    Documentation method: __________________________________________

[ ] P6.8 [HIGH] Serious incidents are reported to appropriate
    authorities (if required by regulation)
    Reporting process: _____________________________________________

[ ] P6.9 [MEDIUM] Lessons learned from incidents are incorporated
    into system improvements
    Improvement process: ___________________________________________

[ ] P6.10 [MEDIUM] Incident trends are tracked and analyzed
    Tracking method: _______________________________________________
```

### 7.3 Regular Review

```
[ ] P6.11 [HIGH] The system is reviewed against current ethical
    standards at least annually
    Review schedule: _______________________________________________

[ ] P6.12 [HIGH] Regulatory compliance is re-verified when
    regulations change
    Monitoring method: _____________________________________________

[ ] P6.13 [MEDIUM] The ethics checklist is re-applied at each
    major update
    Process: _______________________________________________________

[ ] P6.14 [MEDIUM] Stakeholder feedback is solicited periodically
    Feedback schedule: _____________________________________________

[ ] P6.15 [LOW] The system's continued necessity is evaluated
    Evaluation schedule: ___________________________________________
```

---

## 8. Domain-Specific Considerations

### Healthcare AI

```
[ ] HC.1 [CRITICAL] HIPAA compliance verified (if handling PHI)
[ ] HC.2 [CRITICAL] Clinical claims are clearly marked as
    AI-generated and requiring professional review
[ ] HC.3 [CRITICAL] No direct clinical decisions made by AI alone
[ ] HC.4 [HIGH] System tested for demographic bias in clinical
    recommendations
[ ] HC.5 [HIGH] FDA regulations assessed for software as medical
    device classification
```

### Legal AI

```
[ ] LG.1 [CRITICAL] Client confidentiality protections in place
[ ] LG.2 [CRITICAL] AI-generated citations verified before court
    submission
[ ] LG.3 [HIGH] Unauthorized practice of law boundaries respected
[ ] LG.4 [HIGH] Court-specific AI disclosure requirements met
[ ] LG.5 [HIGH] Professional responsibility rules followed
```

### Financial AI

```
[ ] FN.1 [CRITICAL] No investment advice given without proper licensing
[ ] FN.2 [CRITICAL] Regulatory compliance (SEC, FINRA, etc.) verified
[ ] FN.3 [HIGH] Market manipulation risks assessed
[ ] FN.4 [HIGH] Algorithmic bias in lending/insurance checked
[ ] FN.5 [HIGH] Data security meets financial industry standards
```

### HR / Employment AI

```
[ ] HR.1 [CRITICAL] Compliance with employment discrimination laws
[ ] HR.2 [CRITICAL] Algorithmic decision-making transparency (as
    required by law)
[ ] HR.3 [HIGH] Disparate impact testing across protected groups
[ ] HR.4 [HIGH] Candidates informed about AI use in hiring process
[ ] HR.5 [HIGH] EEOC and local employment law compliance
```

### Education AI

```
[ ] ED.1 [CRITICAL] Student data privacy protected (FERPA, COPPA)
[ ] ED.2 [HIGH] AI does not replace pedagogical judgment
[ ] ED.3 [HIGH] Accessibility for diverse learners ensured
[ ] ED.4 [HIGH] Academic integrity considerations addressed
[ ] ED.5 [MEDIUM] Age-appropriate content controls in place
```

---

## 9. Ethical Red Flags

### Immediate Stop Conditions

If any of the following are true, the project should be paused for ethical review:

```
RED FLAG 1: The system makes consequential decisions about people's
lives (employment, credit, healthcare, criminal justice) without
meaningful human oversight.
ACTION: Implement human-in-the-loop before proceeding.

RED FLAG 2: Testing reveals significant disparate impact across
demographic groups that cannot be mitigated.
ACTION: Redesign the system or reconsider the approach.

RED FLAG 3: The system processes sensitive personal data without
clear legal basis or consent.
ACTION: Halt data processing and consult legal counsel.

RED FLAG 4: The system is being used to deceive users about whether
they are interacting with AI.
ACTION: Implement immediate disclosure.

RED FLAG 5: The system generates content that could be used for
manipulation, fraud, or harm.
ACTION: Implement content guardrails and review safety measures.

RED FLAG 6: Users or affected populations have not been consulted
or informed about the AI system.
ACTION: Pause deployment and implement stakeholder engagement.

RED FLAG 7: The system is being deployed in a domain where errors
could cause physical harm.
ACTION: Implement rigorous safety testing and human oversight.

RED FLAG 8: There is no way to audit, explain, or override the
system's decisions.
ACTION: Implement transparency and override mechanisms.
```

---

## 10. Ethics Review Documentation Template

### Project Ethics Review Form

```
PROJECT INFORMATION
Project name: _____________________________________________________
Project lead: _____________________________________________________
Ethics reviewer: __________________________________________________
Review date: ______________________________________________________
Review type: [ ] Initial  [ ] Periodic  [ ] Incident-triggered

PROJECT DESCRIPTION
Brief description:
___________________________________________________________________
___________________________________________________________________

AI technology used:
___________________________________________________________________

Affected populations:
___________________________________________________________________

RISK CLASSIFICATION
Overall risk level: [ ] Unacceptable  [ ] High  [ ] Limited  [ ] Minimal
Justification:
___________________________________________________________________

CHECKLIST RESULTS SUMMARY
Phase 1 (Conception):     _____ / _____ items passed
Phase 2 (Data):           _____ / _____ items passed
Phase 3 (Development):    _____ / _____ items passed
Phase 4 (Testing):        _____ / _____ items passed
Phase 5 (Deployment):     _____ / _____ items passed
Phase 6 (Monitoring):     _____ / _____ items passed

CRITICAL items unresolved: _____
HIGH items unresolved: _____
MEDIUM items unresolved: _____
LOW items unresolved: _____

KEY FINDINGS
Strengths:
1. ________________________________________________________________
2. ________________________________________________________________
3. ________________________________________________________________

Concerns:
1. ________________________________________________________________
2. ________________________________________________________________
3. ________________________________________________________________

REQUIRED ACTIONS
Action 1: _________________________________________________________
Owner: ______________ Deadline: ______________ Priority: ____________

Action 2: _________________________________________________________
Owner: ______________ Deadline: ______________ Priority: ____________

Action 3: _________________________________________________________
Owner: ______________ Deadline: ______________ Priority: ____________

DECISION
[ ] APPROVED — Project may proceed
[ ] APPROVED WITH CONDITIONS — Must complete required actions by deadline
[ ] HOLD — Major concerns must be addressed before proceeding
[ ] REJECTED — Project should not proceed in its current form

Conditions (if applicable):
___________________________________________________________________
___________________________________________________________________

SIGNATURES
Project lead: _________________________  Date: ____________________
Ethics reviewer: ______________________  Date: ____________________
Approver: _____________________________  Date: ____________________

NEXT REVIEW DATE: __________________________________________________
```

---

## Quick Reference Card

### The 10 Essential Questions

For any AI project, always ask:

1. **Who could be harmed?** (Identify all affected populations)
2. **Is it fair?** (Test for bias across demographics)
3. **Is it transparent?** (Can users understand what is happening?)
4. **Is there oversight?** (Can a human intervene?)
5. **Is data protected?** (Privacy and security assured?)
6. **Is consent obtained?** (Legal basis for data use?)
7. **Is it necessary?** (AI is the right approach?)
8. **Is it tested?** (Rigorous evaluation completed?)
9. **Is it monitored?** (Ongoing checks in place?)
10. **Is it documented?** (Decisions and rationale recorded?)

If you cannot answer "yes" to all 10 questions, additional work is needed.

---

*This checklist is part of the Master in Prompt Engineering and AI — Module 10.*
