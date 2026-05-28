# Deck Outline

> High-level presentation structure for NeurIPS talk.

---

## Presentation Overview

- **Title**: Dynamic Quantization for Time-Series Transformers
- **Duration**: 15 minutes + 5 minutes Q&A
- **Slides**: 15 slides
- **Pace**: ~1 slide per minute

---

## Narrative Arc

```
Opening (Hook)
    ↓
Problem (Why it matters)
    ↓
Solution (Our method)
    ↓
Evidence (Results)
    ↓
Impact (Why it matters)
    ↓
Close (Call to action)
```

---

## Section Breakdown

### 1. Opening (0:00 - 0:30)
**Purpose**: Hook the audience
**Slides**: 1 (Title)
**Key Message**: "What if your model could think in 2-bit?"

### 2. Motivation (0:30 - 2:30)
**Purpose**: Establish the problem
**Slides**: 2-3
**Key Message**: Static quantization is suboptimal for time-series

### 3. Method (2:30 - 7:00)
**Purpose**: Explain our approach
**Slides**: 4-7
**Key Message**: Attention weights guide dynamic bit allocation

### 4. Results (7:00 - 12:00)
**Purpose**: Show evidence
**Slides**: 8-12
**Key Message**: We achieve better accuracy with less computation

### 5. Conclusion (12:00 - 14:00)
**Purpose**: Summarize and impact
**Slides**: 13-14
**Key Message**: 30% compression, <3% loss, practical impact

### 6. Q&A (14:00 - 15:00)
**Purpose**: Answer questions
**Slides**: 15
**Key Message**: "Thank you. Questions?"

---

## Slide List

### Slide 1: Title
- Paper title
- Authors
- NeurIPS 2026
- **Time**: 30 seconds

### Slide 2: Motivation - Why Compression?
- Edge deployment challenges
- Computational cost of Transformers
- Need for efficient models
- **Time**: 1 minute

### Slide 3: Problem - Static vs Dynamic
- Static quantization limitations
- Varying importance of time steps
- Opportunity for dynamic allocation
- **Time**: 1 minute

### Slide 4: Method Overview
- Architecture diagram
- Key components
- High-level flow
- **Time**: 1.5 minutes

### Slide 5: Attention Mechanism
- How attention weights work
- Importance extraction
- Visualization
- **Time**: 1 minute

### Slide 6: Bit Allocation
- Threshold-based allocation
- 8-bit vs 2-bit
- Training procedure
- **Time**: 1 minute

### Slide 7: Key Innovation
- What's new
- Why it works
- Theoretical motivation
- **Time**: 1 minute

### Slide 8: Experimental Setup
- Datasets (ETTh1, ETTh2, ETTm1)
- Baselines
- Metrics
- **Time**: 1 minute

### Slide 9: Main Results
- Comparison table
- Key improvements
- Statistical significance
- **Time**: 1.5 minutes

### Slide 10: Efficiency Analysis
- Model size comparison
- Inference speed
- Trade-off visualization
- **Time**: 1 minute

### Slide 11: Ablation Study
- Component analysis
- Contribution breakdown
- Key findings
- **Time**: 1.5 minutes

### Slide 12: Failure Cases
- When method struggles
- Limitations
- Mitigation strategies
- **Time**: 1 minute

### Slide 13: Conclusion
- Summary of contributions
- Key takeaways
- Impact statement
- **Time**: 1 minute

### Slide 14: Future Work
- Extensions
- Open questions
- Call to action
- **Time**: 1 minute

### Slide 15: Thank You
- Questions?
- Contact info
- Paper/code links
- **Time**: Q&A

---

## Timing Summary

| Section | Duration | Slides |
|---------|----------|--------|
| Opening | 0:30 | 1 |
| Motivation | 2:00 | 2-3 |
| Method | 4:30 | 4-7 |
| Results | 5:00 | 8-12 |
| Conclusion | 2:00 | 13-14 |
| Q&A | 5:00 | 15 |
| **Total** | **19:30** | **15** |

**Note**: 15 minutes + 5 minutes Q&A = 20 minutes total

---

## Visual Strategy

### Figures Needed
1. **Architecture diagram** - Method overview
2. **Attention heatmap** - Importance visualization
3. **Bar chart** - MSE comparison
4. **Scatter plot** - Size vs. accuracy trade-off
5. **Ablation table** - Component contributions

### Design Principles
- One message per slide
- Minimal text, maximum visuals
- Consistent color scheme
- Clear labels and annotations

---

*Deck Outline - Academic Presentation Example*