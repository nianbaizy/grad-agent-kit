# Advisor Roaster - Input Template

> Use this template when calling the advisor-roaster skill.

---

## Research Idea

**What is your research about?**

[Describe your research idea clearly]

**Example**:
```
Dynamic bit-width quantization for time-series Transformer models,
using attention weights to allocate precision dynamically.
```

---

## Method Design

**How does your method work?**

[Explain your technical approach]

**Example**:
```
1. Compute attention weights in each layer
2. Use weights to determine time-step importance
3. Allocate 8-bit to important steps, 2-bit to others
4. Train end-to-end with straight-through estimator
```

---

## Current Results

**What do you have so far?**

[Provide quantitative results]

**Example**:
```
- ETTh1: 2.3% MSE improvement over PatchTST
- ETTh2: 1.8% improvement
- Model size: 30% reduction
- Only tested on 2 datasets so far
```

---

## Perceived Innovation

**What do you think is novel?**

[Explain your contribution claims]

**Example**:
```
1. First dynamic quantization for time-series models
2. Attention-based bit allocation (novel mechanism)
3. Theoretical analysis of compression-accuracy trade-off
```

---

## Target Venue

**Where do you plan to submit?**

- [ ] NeurIPS 2026
- [ ] ICML 2026
- [ ] ICLR 2026
- [ ] Other: _____________

---

## Known Weaknesses

**What do you already know is weak?**

[List known issues]

**Example**:
```
1. Only tested on forecasting, not classification
2. Limited theoretical analysis
3. No deployment experiments
4. Small number of baselines
```

---

## Specific Concerns

**What worries you most?**

[List your concerns]

**Example**:
```
1. Is the novelty sufficient?
2. Are experiments comprehensive enough?
3. Will reviewers question the theoretical contribution?
```

---

## Timeline

**When do you plan to finish?**

- [ ] 1 month
- [ ] 2 months
- [ ] 3 months
- [ ] Other: _____________

---

## Additional Context

**Any other information?**

[Add relevant context]

---

## Example Complete Input

```markdown
## Research Idea
Dynamic quantization for time-series Transformers

## Method Design
Attention-based bit allocation:
1. Compute attention weights
2. Quantize important steps to 8-bit
3. Quantize others to 2-bit
4. End-to-end training

## Current Results
- 2.3% MSE improvement on ETTh1
- 30% model size reduction
- Only 2 datasets tested

## Perceived Innovation
1. First dynamic quantization for time-series
2. Novel attention-based allocation
3. Theoretical analysis

## Target Venue
NeurIPS 2026

## Known Weaknesses
1. Limited datasets
2. Weak theory
3. No deployment tests

## Specific Concerns
1. Is novelty enough?
2. Are experiments sufficient?

## Timeline
2 months

## Additional Context
Previous rejection from ICML due to weak experiments.
```

---

*Advisor Roaster Input Template - Part of GradAgentKit*