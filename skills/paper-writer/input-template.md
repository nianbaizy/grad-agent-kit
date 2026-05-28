# Paper Writer - Input Template

> Use this template when calling the paper-writer skill.

---

## Task

**What type of paper do you want to write?**

- [ ] Full paper draft
- [ ] Abstract only
- [ ] Introduction only
- [ ] Method section only
- [ ] Experiments section only

---

## Research Topic

**What is your research about?**

[Describe your research topic in detail]

**Example**:
```
Low-bit quantization for time-series Transformer models, focusing on dynamic 
bit-width allocation based on temporal attention weights.
```

---

## Method Description

**How does your method work?**

[Explain your approach technically]

**Example**:
```
Our method uses attention weights to determine the importance of each time step,
then allocates higher bit-widths (8-bit) to important steps and lower bit-widths 
(2-bit) to less important steps. This is done dynamically during inference.
```

---

## Experiment Results

**What are your key findings?**

[Provide quantitative results]

**Example**:
```
- ETTh1: 2.3% MSE improvement over PatchTST baseline
- ETTh2: 1.8% MSE improvement
- Model size: 30% reduction (from 12MB to 8.4MB)
- Inference speed: 15% faster on GPU
- Ablation: Attention-based allocation outperforms random by 1.5%
```

---

## Target Venue

**Where do you plan to submit?**

- [ ] NeurIPS 2026
- [ ] ICML 2026
- [ ] ICLR 2026
- [ ] AAAI 2026
- [ ] Other: _____________

**Venue Requirements**:
- Page limit: _____ pages
- Format: _____ (LaTeX / Word)
- Review type: _____ (double-blind / single-blind)

---

## Baseline Comparisons

**What methods do you compare against?**

[List baseline methods]

**Example**:
```
1. PatchTST (2023) - Current SOTA for time-series
2. iTransformer (2024) - Attention-based approach
3. TimesNet (2023) - Multi-scale method
4. Static quantization (2-bit) - Compression baseline
5. Static quantization (4-bit) - Compression baseline
```

---

## Key Contributions

**What are your main contributions?**

[List 3-5 contributions]

**Example**:
```
1. First dynamic quantization method for time-series Transformers
2. Attention-based bit-width allocation mechanism
3. Theoretical analysis of compression-accuracy trade-off
4. Extensive experiments on 5 benchmark datasets
5. 30% model size reduction with minimal accuracy loss
```

---

## Optional Information

### Figures and Tables
**What figures/tables do you want to include?**

- [ ] Method overview diagram
- [ ] Attention visualization
- [ ] Performance comparison table
- [ ] Ablation study table
- [ ] Efficiency analysis chart

### Word Limit
**Maximum word count**: _____ words

### Language
- [ ] English
- [ ] Chinese

### LaTeX Format
- [ ] Generate LaTeX code
- [ ] Generate Markdown only

### Additional Notes
**Any other requirements?**

[Add any other relevant information]

---

## Example Complete Input

```markdown
## Task
Full paper draft

## Research Topic
Low-bit quantization for time-series Transformer models

## Method Description
Dynamic bit-width allocation using attention weights to identify important 
time steps and assign higher precision to them.

## Experiment Results
- ETTh1: 2.3% MSE improvement
- ETTh2: 1.8% MSE improvement  
- Model size: 30% reduction
- Inference: 15% faster

## Target Venue
NeurIPS 2026 (8 pages, double-blind)

## Baseline Comparisons
1. PatchTST
2. iTransformer
3. TimesNet
4. Static 2-bit quantization
5. Static 4-bit quantization

## Key Contributions
1. First dynamic quantization for time-series
2. Attention-based bit allocation
3. Theoretical analysis
4. Extensive experiments
5. Significant compression with minimal loss
```

---

*Paper Writer Input Template - Part of GradAgentKit*