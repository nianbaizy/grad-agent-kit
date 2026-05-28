# Usage Guide

> How to use GradAgentKit skills effectively.

---

## Overview

This guide provides detailed usage examples for each skill in GradAgentKit.

---

## 1. Paper Writer

### Use When

- Starting a new research paper
- Need to generate initial draft
- Want structured paper outline
- Preparing for submission

### Basic Usage

```markdown
# In your Claude Code session:

Use the paper-writer skill to generate a draft.

## Topic
Low-bit quantization for time-series Transformer models

## Method
Dynamic bit-width allocation based on temporal attention weights

## Results
- 2.3% MSE improvement on ETTh1 dataset
- 1.8% MSE improvement on ETTh2 dataset
- 30% reduction in model size

## Target Venue
NeurIPS 2026

## Language
English
```

### Advanced Usage

```markdown
Use the paper-writer skill with these specific requirements:

## Topic
Efficient attention mechanisms for long-sequence time-series forecasting

## Method
Sparse attention with learnable patterns

## Key Contributions
1. Novel sparse attention pattern
2. Theoretical complexity analysis
3. Extensive experiments on 5 datasets

## Results
- 15% faster inference
- Comparable accuracy to full attention
- Scalable to 10,000+ time steps

## Target Venue
ICML 2026

## Constraints
- Maximum 8 pages
- Include ablation study
- Compare with 5 baselines
```

### Expected Output

The skill will generate:
- `paper-draft.md` - Complete paper draft
- `references.bib` - Bibliography file
- `outline.md` - Paper structure
- `quality-report.md` - Quality check results

---

## 2. Experiment Analyzer

### Use When

- After running experiments
- Need to analyze results
- Want to identify patterns
- Preparing experiment section

### Basic Usage

```markdown
# In your Claude Code session:

Use the experiment-analyzer skill to analyze my results.

## Files to Read
- results.csv
- train.log
- config.yaml

## Baseline
PatchTST (original paper results)

## My Method
Improved PatchTST with dynamic patching

## Key Metrics
- MSE (Mean Squared Error)
- MAE (Mean Absolute Error)
- Inference time
```

### Advanced Usage

```markdown
Use the experiment-analyzer skill with detailed analysis:

## Files to Read
- results/etth1.csv
- results/etth2.csv
- results/ettm1.csv
- configs/base.yaml
- configs/ablation.yaml
- logs/training.log

## Baseline Comparisons
- PatchTST (2023)
- iTransformer (2024)
- TimesNet (2023)

## Analysis Focus
1. Performance across datasets
2. Ablation study results
3. Training convergence
4. Inference efficiency

## Specific Questions
- Why does method A outperform method B on ETTh1?
- Is the improvement statistically significant?
- What's the computational overhead?
```

### Expected Output

The skill will generate:
- `analysis-report.md` - Detailed analysis
- `results-summary.md` - Key findings
- `ablation-analysis.md` - Ablation study results
- `recommendations.md` - Suggested improvements

---

## 3. Reviewer Simulator

### Use When

- Before paper submission
- Want to identify weaknesses
- Need pre-submission review
- Preparing for rebuttal

### Basic Usage

```markdown
# In your Claude Code session:

Use the reviewer-simulator skill to review my paper.

## Paper File
paper-draft.md

## Target Venue
NeurIPS 2026

## Review Focus
- Novelty of contribution
- Experimental validation
- Writing quality
```

### Advanced Usage

```markdown
Use the reviewer-simulator skill for comprehensive review:

## Paper Files
- sections/abstract.md
- sections/introduction.md
- sections/method.md
- sections/experiments.md
- sections/conclusion.md

## Target Venue
ICML 2026

## Review Criteria
1. Soundness
2. Significance
3. Novelty
4. Clarity
5. Reproducibility

## Specific Concerns
- Is the method sufficiently novel?
- Are experiments comprehensive enough?
- Is the writing clear and concise?
- Are there any missing references?

## Review Style
Be strict but constructive. Focus on major concerns first.
```

### Expected Output

The skill will generate:
- `review-report.md` - Complete review
- `strengths.md` - Paper strengths
- `concerns.md` - Major and minor concerns
- `questions.md` - Questions for authors
- `suggestions.md` - Revision suggestions

---

## 4. Advisor Roaster

### Use When

- Preparing for advisor meeting
- Need to anticipate questions
- Want to strengthen arguments
- Pre-defense preparation

### Basic Usage

```markdown
# In your Claude Code session:

Use the advisor-roaster skill to prepare for my advisor meeting.

## Research Idea
Dynamic bit-width quantization for time-series models

## Method Design
Attention-based bit-width allocation

## Current Results
2.3% improvement on ETTh1

## Perceived Innovation
First to apply dynamic quantization to time-series

## Target
Submit to NeurIPS 2026
```

### Advanced Usage

```markdown
Use the advisor-roaster skill for thorough preparation:

## Research Context
- Field: Efficient deep learning
- Problem: Model compression for time-series
- Gap: No dynamic quantization for temporal models

## Method Details
- Architecture: Transformer-based
- Innovation: Attention-guided bit allocation
- Training: Joint optimization of accuracy and efficiency

## Current Status
- Experiments: 3/5 datasets complete
- Ablation: Partial (2/4 components)
- Baselines: 3/5 compared

## Known Weaknesses
- Limited theoretical analysis
- Only tested on forecasting tasks
- No deployment experiments

## Target Questions
1. Why dynamic over static?
2. How to handle different time granularities?
3. What's the overhead of attention computation?
```

### Expected Output

The skill will generate:
- `anticipated-questions.md` - Likely questions
- `weaknesses.md` - Potential attack points
- `defense-strategies.md` - How to respond
- `improvement-priorities.md` - What to work on next

---

## 5. Academic Deck Builder

### Use When

- Preparing conference presentation
- Need to create slides
- Want structured talk
- Building presentation deck

### Basic Usage

```markdown
# In your Claude Code session:

Use the academic-deck-builder skill to create my presentation.

## Topic
Dynamic Quantization for Time-Series Models

## Audience
Machine learning researchers

## Duration
15 minutes + 5 minutes Q&A

## Material
paper-draft.md

## Style
Academic, clear, visual
```

### Advanced Usage

```markdown
Use the academic-deck-builder skill for conference talk:

## Presentation Details
- Title: Efficient Time-Series Forecasting with Dynamic Quantization
- Venue: NeurIPS 2026
- Session: Oral presentation
- Duration: 20 minutes

## Audience Profile
- Expertise: ML researchers, some time-series specialists
- Expectations: Novel method, solid experiments, clear insights

## Material Sources
- paper-draft.md
- figures/
- results/

## Key Messages
1. Dynamic quantization adapts to temporal patterns
2. Our method achieves better accuracy-efficiency trade-off
3. Extensive experiments validate effectiveness

## Visual Style
- Clean, minimal design
- Emphasis on results visualization
- Use animations sparingly
```

### Expected Output

The skill will generate:
- `deck-outline.md` - Presentation structure
- `slide-content.md` - Content for each slide
- `speaker-notes.md` - Talking points
- `visual-suggestions.md` - Design recommendations

---

## Combining Skills

### Full Research Workflow

```markdown
# Step 1: Generate paper draft
Use paper-writer skill with my research details...

# Step 2: Analyze experiments
Use experiment-analyzer skill with my results...

# Step 3: Get pre-submission review
Use reviewer-simulator skill on my draft...

# Step 4: Prepare for advisor
Use advisor-roaster skill for my meeting...

# Step 5: Build presentation
Use academic-deck-builder skill for conference...
```

### Iterative Refinement

```markdown
# Round 1: Initial draft
Use paper-writer skill...

# Round 2: Review and improve
Use reviewer-simulator skill...
# Address concerns in paper

# Round 3: Final review
Use reviewer-simulator skill again...
# Verify improvements
```

---

## Tips for Best Results

### 1. Be Specific

❌ Vague: "Write a paper about AI"
✅ Specific: "Write a paper about dynamic quantization for time-series Transformers targeting NeurIPS 2026"

### 2. Provide Context

❌ Minimal: "Analyze my results"
✅ Complete: "Analyze results.csv comparing with PatchTST baseline, focusing on MSE and inference time"

### 3. Set Constraints

❌ Open-ended: "Review my paper"
✅ Constrained: "Review for ICML 2026, focus on novelty and experiments, be strict"

### 4. Use Templates

Fill in the input template completely:
- All required fields
- Relevant optional fields
- Clear constraints
- Specific questions

### 5. Review Output

Always check:
- Quality checklist results
- Generated artifacts
- Recommendations
- Areas for improvement

---

## Common Patterns

### Pattern 1: Paper Writing Pipeline

```
paper-writer → experiment-analyzer → reviewer-simulator → revise → submit
```

### Pattern 2: Defense Preparation

```
advisor-roaster → revise → academic-deck-builder → practice → defend
```

### Pattern 3: Iterative Improvement

```
draft → review → revise → review → revise → finalize
```

---

## Troubleshooting

### Skill Produces Generic Output

**Problem**: Output is too generic, not specific to your research.

**Solution**: Provide more detailed input:
- Specific method details
- Concrete experimental results
- Clear constraints
- Target venue requirements

### Skill Misses Important Aspects

**Problem**: Skill doesn't cover important aspects of your work.

**Solution**: Add specific instructions:
- "Include ablation study"
- "Compare with method X"
- "Discuss limitations"

### Output Format Issues

**Problem**: Output doesn't match expected format.

**Solution**: Check output-format.md:
- Verify skill version
- Check for customization
- Report issues

---

*Usage guide for GradAgentKit skills.*