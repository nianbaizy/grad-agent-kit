# Academic Presentation Example

> Demonstrates academic-deck-builder skill for conference talks.

---

## Scenario

You're preparing a **15-minute conference presentation** for NeurIPS 2026 about dynamic quantization for time-series models.

### Presentation Details

- **Title**: Dynamic Quantization for Time-Series Transformers
- **Venue**: NeurIPS 2026 (Oral Presentation)
- **Duration**: 15 minutes + 5 minutes Q&A
- **Audience**: ML researchers, some time-series specialists

---

## Source Material

### Paper Draft
Your paper covers:
1. Problem: Model compression for time-series forecasting
2. Method: Attention-based dynamic bit-width allocation
3. Results: 2.3% improvement, 30% compression
4. Contribution: First dynamic quantization for time-series

### Key Findings
- Dynamic beats static quantization
- Attention weights guide bit allocation
- 30% model size reduction
- 15% inference speedup

---

## Files

### Input Files
- `source-material.md` - Paper content and results

### Expected Output Files
- `deck-outline.md` - Presentation structure
- `slide-structure.md` - Slide-by-slide content
- `expected-output.md` - Complete example output

---

## How to Use

```markdown
Use the academic-deck-builder skill to create my presentation.

## Topic
Dynamic quantization for time-series Transformer models

## Audience
ML researchers at NeurIPS (expert level)

## Duration
15 minutes + 5 minutes Q&A

## Source Material
source-material.md

## Key Messages
1. Dynamic quantization adapts to temporal patterns
2. Our method achieves 30% compression with <3% accuracy loss
3. Attention weights effectively guide bit allocation

## Style
Formal academic, data-heavy, clear visualizations
```

---

## Expected Output

### Presentation Structure

```
0:00 - 0:30  Title & Hook
0:30 - 2:30  Motivation & Problem
2:30 - 7:00  Method (with architecture diagram)
7:00 - 12:00 Results (with charts)
12:00 - 14:00 Conclusion & Impact
14:00 - 15:00 Q&A
```

### Key Slides

1. **Title Slide** - Paper title, authors, venue
2. **Motivation** - Why compression matters
3. **Problem** - Limitations of static quantization
4. **Method Overview** - Architecture diagram
5. **Attention Mechanism** - How it works
6. **Results Table** - Comparison with baselines
7. **Efficiency Chart** - Size vs. accuracy trade-off
8. **Ablation Study** - Component analysis
9. **Conclusion** - Key contributions
10. **Thank You** - Contact info

---

## Learning Objectives

After using this example, you should understand:

1. How to structure a 15-minute conference talk
2. How to create compelling narrative arc
3. How to design effective visualizations
4. How to manage time and pacing
5. How to prepare for Q&A

---

## Presentation Tips

### Opening (30 seconds)
- Start with a hook: "What if your model could think in 2-bit?"
- State the problem clearly
- Preview the solution

### Method (4.5 minutes)
- Use architecture diagram
- Explain step by step
- Highlight innovation

### Results (5 minutes)
- Show main comparison table first
- Use charts for visual impact
- Discuss ablation study

### Conclusion (2 minutes)
- Summarize 3 key contributions
- State impact
- Future work

---

*Example: Academic Presentation - Part of GradAgentKit*