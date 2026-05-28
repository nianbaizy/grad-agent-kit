# Reviewer Simulator - Input Template

> Use this template when calling the reviewer-simulator skill.

---

## Task

**What type of review do you need?**

- [ ] Full paper review
- [ ] Abstract review only
- [ ] Method review only
- [ ] Experiments review only
- [ ] Writing quality review

---

## Paper Files

**What files should be reviewed?**

- [ ] `paper-draft.md` - Complete paper
- [ ] `sections/abstract.md` - Abstract only
- [ ] `sections/introduction.md` - Introduction only
- [ ] `sections/method.md` - Method only
- [ ] `sections/experiments.md` - Experiments only
- [ ] `supplementary/` - Supplementary materials

**File paths**:
```
[List file paths here]
```

---

## Target Venue

**Where is this paper targeted?**

- [ ] NeurIPS 2026
- [ ] ICML 2026
- [ ] ICLR 2026
- [ ] AAAI 2026
- [ ] CVPR 2026
- [ ] Other: _____________

**Venue Details**:
- Acceptance rate: _____%
- Page limit: _____ pages
- Review format: _____ (single-blind / double-blind)

---

## Review Focus

**What aspects should be emphasized?**

### Novelty
- [ ] Originality of contribution
- [ ] Differentiation from prior work
- [ ] Significance of advance

### Methodology
- [ ] Technical soundness
- [ ] Theoretical foundation
- [ ] Assumptions validity

### Experiments
- [ ] Experimental setup
- [ ] Baseline comparisons
- [ ] Result significance
- [ ] Ablation study

### Writing
- [ ] Clarity
- [ ] Organization
- [ ] Grammar
- [ ] Figures/tables

### Impact
- [ ] Practical applications
- [ ] Theoretical contributions
- [ ] Future research directions

---

## Review Style

**How strict should the review be?**

- [ ] Strict (top-tier venue standards)
- [ ] Balanced (fair but rigorous)
- [ ] Lenient (constructive feedback)

---

## Specific Concerns

**Are there specific areas of concern?**

1. [Concern 1]
2. [Concern 2]
3. [Concern 3]

---

## Additional Context

**Any other information for the reviewer?**

[Add context about the research, prior reviews, author concerns, etc.]

---

## Example Complete Input

```markdown
## Task
Full paper review

## Paper Files
- paper-draft.md (complete paper)
- supplementary/code.zip (implementation)

## Target Venue
NeurIPS 2026 (8 pages, double-blind, ~25% acceptance rate)

## Review Focus
- Novelty: High priority
- Methodology: High priority
- Experiments: High priority
- Writing: Medium priority

## Review Style
Strict (top-tier venue standards)

## Specific Concerns
1. Is the method sufficiently novel?
2. Are experiments comprehensive enough?
3. Is the theoretical analysis sound?

## Additional Context
This is a first submission. Previous work was rejected from ICML
due to insufficient experiments. Authors have addressed this concern.
```

---

*Reviewer Simulator Input Template - Part of GradAgentKit*