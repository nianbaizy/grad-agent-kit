# Reviewer Simulator - Output Format

> Expected output structure for reviewer-simulator skill.

---

## Primary Deliverables

### 1. review-report.md

**Purpose**: Complete peer review report

**Structure**:
```markdown
# Paper Review Report

## Paper Information
- Title: [Paper title]
- Authors: [Author names or Anonymous]
- Target Venue: [Conference/Journal]
- Review Date: [Date]

## Summary
[2-3 paragraph summary of the paper]

## Overall Assessment
- Score: [1-10]
- Confidence: [1-5]
- Recommendation: [Accept / Weak Accept / Borderline / Weak Reject / Strong Reject]

## Strengths
1. [Strength 1 with specific evidence]
2. [Strength 2 with specific evidence]
3. [Strength 3 with specific evidence]

## Major Concerns
### Concern 1: [Title]
**Description**: [Detailed explanation]
**Evidence**: [Page/line references]
**Impact**: [How this affects the paper]
**Suggestion**: [How to address]

### Concern 2: [Title]
**Description**: [Detailed explanation]
**Evidence**: [Page/line references]
**Impact**: [How this affects the paper]
**Suggestion**: [How to address]

## Minor Concerns
1. [Minor issue 1]
2. [Minor issue 2]
3. [Minor issue 3]

## Questions for Authors
1. [Question 1]
2. [Question 2]
3. [Question 3]

## Detailed Review

### Abstract
[Assessment of abstract]

### Introduction
[Assessment of introduction]

### Related Work
[Assessment of related work]

### Method
[Assessment of method]

### Experiments
[Assessment of experiments]

### Discussion
[Assessment of discussion]

### Conclusion
[Assessment of conclusion]

## Rejection Risk Assessment
- Risk Level: [High / Medium / Low]
- Key Factors: [List main risk factors]
- Mitigation: [How to reduce risk]

## Revision Priority
1. [Highest priority fix]
2. [Second priority]
3. [Third priority]

## Additional Notes
[Other observations]
```

---

### 2. strengths.md

**Purpose**: Detailed list of paper strengths

**Structure**:
```markdown
# Paper Strengths

## Strength 1: [Title]
**Category**: [Novelty / Methodology / Experiments / Writing / Impact]
**Evidence**: [Specific examples from paper]
**Significance**: [Why this is important]
**Page Reference**: [Where this appears]

## Strength 2: [Title]
**Category**: [Novelty / Methodology / Experiments / Writing / Impact]
**Evidence**: [Specific examples from paper]
**Significance**: [Why this is important]
**Page Reference**: [Where this appears]

## Strength 3: [Title]
**Category**: [Novelty / Methodology / Experiments / Writing / Impact]
**Evidence**: [Specific examples from paper]
**Significance**: [Why this is important]
**Page Reference**: [Where this appears]

## Summary
[Overall assessment of strengths]
```

---

### 3. concerns.md

**Purpose**: Detailed list of concerns

**Structure**:
```markdown
# Paper Concerns

## Major Concerns

### Concern 1: [Title]
**Severity**: Major
**Category**: [Novelty / Methodology / Experiments / Writing / Claims]
**Description**: [Detailed explanation]
**Evidence**: [Page/line references]
**Impact**: [How this affects validity]
**Suggestion**: [Specific fix]
**Difficulty**: [Easy / Medium / Hard]

### Concern 2: [Title]
**Severity**: Major
**Category**: [Novelty / Methodology / Experiments / Writing / Claims]
**Description**: [Detailed explanation]
**Evidence**: [Page/line references]
**Impact**: [How this affects validity]
**Suggestion**: [Specific fix]
**Difficulty**: [Easy / Medium / Hard]

## Minor Concerns

### Minor 1: [Title]
**Severity**: Minor
**Description**: [Brief explanation]
**Suggestion**: [Quick fix]

### Minor 2: [Title]
**Severity**: Minor
**Description**: [Brief explanation]
**Suggestion**: [Quick fix]

## Summary
[Overall assessment of concerns]
```

---

### 4. questions.md

**Purpose**: Questions for authors

**Structure**:
```markdown
# Questions for Authors

## Clarification Questions
1. [Question about method details]
2. [Question about experimental setup]
3. [Question about results interpretation]

## Technical Questions
1. [Question about assumptions]
2. [Question about theoretical claims]
3. [Question about limitations]

## Presentation Questions
1. [Question about unclear writing]
2. [Question about missing information]
3. [Question about figures/tables]

## Impact Questions
1. [Question about practical applications]
2. [Question about scalability]
3. [Question about future work]

## Priority
- Must answer: [Question numbers]
- Should answer: [Question numbers]
- Nice to have: [Question numbers]
```

---

### 5. suggestions.md

**Purpose**: Revision suggestions

**Structure**:
```markdown
# Revision Suggestions

## Priority 1 (Must Fix)
### Suggestion 1: [Title]
**Problem**: [What's wrong]
**Solution**: [How to fix]
**Effort**: [Hours/Days]
**Impact**: [High/Medium/Low]

### Suggestion 2: [Title]
**Problem**: [What's wrong]
**Solution**: [How to fix]
**Effort**: [Hours/Days]
**Impact**: [High/Medium/Low]

## Priority 2 (Should Fix)
### Suggestion 3: [Title]
**Problem**: [What's wrong]
**Solution**: [How to fix]
**Effort**: [Hours/Days]
**Impact**: [High/Medium/Low]

## Priority 3 (Nice to Have)
### Suggestion 4: [Title]
**Problem**: [What's wrong]
**Solution**: [How to fix]
**Effort**: [Hours/Days]
**Impact**: [High/Medium/Low]

## Timeline
- Week 1: [Priority 1 items]
- Week 2: [Priority 2 items]
- Week 3: [Priority 3 items]
```

---

## Secondary Deliverables

### 6. score-justification.md

**Purpose**: Detailed score rationale

### 7. rejection-risk.md

**Purpose**: Risk assessment and mitigation

---

## File Organization

```
output/
├── review-report.md        # Complete review
├── strengths.md            # Paper strengths
├── concerns.md             # Major and minor concerns
├── questions.md            # Questions for authors
├── suggestions.md          # Revision suggestions
├── score-justification.md  # Score rationale
└── rejection-risk.md       # Risk assessment
```

---

## Quality Indicators

### Good Review
✅ Specific, evidence-based feedback
✅ Constructive suggestions
✅ Fair and balanced
✅ Actionable recommendations
✅ Professional tone

### Bad Review
❌ Vague criticism
❌ Personal attacks
❌ Unfair bias
❌ No suggestions
❌ Hostile tone

---

*Reviewer Simulator Output Format - Part of GradAgentKit*