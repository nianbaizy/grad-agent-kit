# Advisor Roaster - Output Format

> Expected output structure for advisor-roaster skill.

---

## Primary Deliverables

### 1. anticipated-questions.md

**Purpose**: Questions your advisor will likely ask

**Structure**:
```markdown
# Anticipated Advisor Questions

## Motivation Questions
1. **Why is this important?**
   - Context: [Why advisor asks this]
   - Good answer: [How to respond]
   - Trap: [What not to say]

2. **Who cares about this problem?**
   - Context: [Why advisor asks this]
   - Good answer: [How to respond]
   - Trap: [What not to say]

## Novelty Questions
3. **What's new here?**
   - Context: [Why advisor asks this]
   - Good answer: [How to respond]
   - Trap: [What not to say]

4. **How is this different from [paper X]?**
   - Context: [Why advisor asks this]
   - Good answer: [How to respond]
   - Trap: [What not to say]

## Method Questions
5. **Why this approach?**
   - Context: [Why advisor asks this]
   - Good answer: [How to respond]
   - Trap: [What not to say]

## Results Questions
6. **Is this statistically significant?**
   - Context: [Why advisor asks this]
   - Good answer: [How to respond]
   - Trap: [What not to say]

## Priority
- Must prepare: [Question numbers]
- Should prepare: [Question numbers]
- Nice to have: [Question numbers]
```

---

### 2. weaknesses.md

**Purpose**: Points where your research is vulnerable

**Structure**:
```markdown
# Research Weaknesses

## Critical Weaknesses

### Weakness 1: [Title]
**Category**: [Novelty / Method / Results / Theory]
**Description**: [Detailed explanation]
**Evidence**: [Why this is weak]
**Attack Vector**: [How advisor might attack]
**Severity**: High / Medium / Low

### Weakness 2: [Title]
**Category**: [Novelty / Method / Results / Theory]
**Description**: [Detailed explanation]
**Evidence**: [Why this is weak]
**Attack Vector**: [How advisor might attack]
**Severity**: High / Medium / Low

## Minor Weaknesses

### Weakness 3: [Title]
**Category**: [Novelty / Method / Results / Theory]
**Description**: [Brief explanation]
**Severity**: Low

## Vulnerability Assessment
- Most dangerous: [Weakness number]
- Easiest to fix: [Weakness number]
- Hardest to defend: [Weakness number]
```

---

### 3. defense-strategies.md

**Purpose**: How to respond to tough questions

**Structure**:
```markdown
# Defense Strategies

## Strategy 1: [For specific question]
**Question**: [The tough question]
**Weak Response**: [What NOT to say]
**Strong Response**: [What TO say]
**Evidence**: [Supporting points]
**Backup Plan**: [If pressed further]

## Strategy 2: [For specific question]
**Question**: [The tough question]
**Weak Response**: [What NOT to say]
**Strong Response**: [What TO say]
**Evidence**: [Supporting points]
**Backup Plan**: [If pressed further]

## General Defense Principles
1. Be honest about limitations
2. Pivot to strengths
3. Provide evidence
4. Acknowledge weaknesses
5. Offer alternatives

## Phrases to Avoid
- "Nobody has done this before" (usually false)
- "This is clearly novel" (let others judge)
- "The results speak for themselves" (they don't)

## Phrases to Use
- "We acknowledge this limitation..."
- "Our contribution is specifically..."
- "The key insight is..."
```

---

### 4. improvement-priorities.md

**Purpose**: What to work on before advisor meeting

**Structure**:
```markdown
# Improvement Priorities

## Priority 1: [Most Critical]
**Issue**: [What's wrong]
**Solution**: [How to fix]
**Effort**: [Hours/Days]
**Impact**: High / Medium / Low
**Deadline**: [When to finish]

## Priority 2: [Important]
**Issue**: [What's wrong]
**Solution**: [How to fix]
**Effort**: [Hours/Days]
**Impact**: High / Medium / Low
**Deadline**: [When to finish]

## Priority 3: [Nice to Have]
**Issue**: [What's wrong]
**Solution**: [How to fix]
**Effort**: [Hours/Days]
**Impact**: High / Medium / Low
**Deadline**: [When to finish]

## Quick Wins (< 1 day)
1. [Quick improvement]
2. [Quick improvement]
3. [Quick improvement]

## Timeline
- This week: [Priority 1]
- Next week: [Priority 2]
- Before meeting: [Priority 3]
```

---

## Secondary Deliverables

### 5. advisor-personality.md

**Purpose**: Simulated advisor profile

**Structure**:
```markdown
# Simulated Advisor Profile

## Advisor Style
- Strictness: [1-10]
- Focus areas: [List]
- Question style: [Direct / Probing / Socratic]
- Expectations: [High / Medium / Low]

## Typical Questions
1. [Common question 1]
2. [Common question 2]
3. [Common question 3]

## Red Flags
- [What irritates this advisor]
- [What impresses this advisor]
- [What to avoid]

## Meeting Tips
- [How to prepare]
- [How to present]
- [How to respond]
```

---

### 6. meeting-preparation.md

**Purpose**: Checklist for advisor meeting

**Structure**:
```markdown
# Advisor Meeting Preparation

## Before Meeting
- [ ] Review anticipated questions
- [ ] Prepare defense strategies
- [ ] Fix priority improvements
- [ ] Prepare slides/figures
- [ ] Practice answers

## Materials to Bring
- [ ] Paper draft (if ready)
- [ ] Results summary
- [ ] Figures/tables
- [ ] Questions for advisor
- [ ] Notebook for notes

## During Meeting
- [ ] Listen carefully
- [ ] Take notes
- [ ] Ask for clarification
- [ ] Be honest about limitations
- [ ] Follow up on suggestions

## After Meeting
- [ ] Review notes
- [ ] Prioritize feedback
- [ ] Update timeline
- [ ] Schedule follow-up
```

---

## File Organization

```
output/
├── anticipated-questions.md   # Likely questions
├── weaknesses.md              # Vulnerability points
├── defense-strategies.md      # How to respond
├── improvement-priorities.md  # What to work on
├── advisor-personality.md     # Simulated advisor
└── meeting-preparation.md     # Prep checklist
```

---

## Quality Indicators

### Good Output
✅ Realistic tough questions
✅ Specific weaknesses identified
✅ Actionable defense strategies
✅ Clear improvement priorities
✅ Practical advice

### Bad Output
❌ Softball questions
❌ Vague weaknesses
❌ Generic defenses
❌ Unrealistic priorities
❌ Unhelpful advice

---

*Advisor Roaster Output Format - Part of GradAgentKit*