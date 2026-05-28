# Quantization Paper Example

> Demonstrates paper-writer, reviewer-simulator, and advisor-roaster skills.

---

## Scenario

You're writing a paper on **dynamic quantization for time-series Transformer models**.

### Research Topic
Low-bit quantization for time-series forecasting, using attention weights to dynamically allocate bit-widths.

### Method
- Compute attention weights in each Transformer layer
- Use weights to determine time-step importance
- Allocate 8-bit precision to important time steps
- Allocate 2-bit precision to less important steps
- Train end-to-end with straight-through estimator

### Results
- ETTh1 dataset: 2.3% MSE improvement over PatchTST baseline
- ETTh2 dataset: 1.8% MSE improvement
- Model size: 30% reduction (12MB → 8.4MB)
- Inference speed: 15% faster on GPU

### Target Venue
NeurIPS 2026 (8 pages, double-blind review)

---

## Files

### Input Files
- `method-description.md` - Detailed method description
- `experiment-results.md` - Experimental data and results

### Expected Output Files
- `expected-paper-draft.md` - Example paper draft
- `expected-review.md` - Example review report
- `expected-advisor-questions.md` - Example advisor questions

---

## How to Use

### 1. Paper Writer

```markdown
Use the paper-writer skill to generate a draft.

## Topic
Dynamic quantization for time-series Transformer models

## Method
Attention-based bit-width allocation...

## Results
2.3% MSE improvement on ETTh1...

## Target Venue
NeurIPS 2026
```

### 2. Reviewer Simulator

```markdown
Use the reviewer-simulator skill to review the draft.

## Paper File
paper-draft.md

## Target Venue
NeurIPS 2026

## Review Focus
- Novelty of dynamic quantization
- Experimental validation
- Writing quality
```

### 3. Advisor Roaster

```markdown
Use the advisor-roaster skill to prepare for advisor meeting.

## Research Idea
Dynamic quantization using attention weights

## Method Design
8-bit for important steps, 2-bit for others

## Current Results
2.3% improvement on ETTh1

## Perceived Innovation
First dynamic quantization for time-series
```

---

## Expected Outputs

### Paper Draft
- Complete 8-page paper
- Abstract, Introduction, Method, Experiments, Conclusion
- Placeholder citations

### Review Report
- Score: 7/10 (Weak Accept)
- 3 major concerns
- 5 minor concerns
- Revision suggestions

### Advisor Questions
- 10 anticipated questions
- Defense strategies
- Improvement priorities

---

## Learning Objectives

After using this example, you should understand:

1. How to use paper-writer for initial draft generation
2. How to use reviewer-simulator for pre-submission review
3. How to use advisor-roaster for defense preparation
4. How to integrate feedback and improve paper

---

*Example: Quantization Paper - Part of GradAgentKit*