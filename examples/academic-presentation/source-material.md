# Source Material

> Paper content for presentation preparation.

---

## Paper Title

Dynamic Quantization for Time-Series Transformer Models via Attention-Guided Bit Allocation

---

## Abstract

Model compression is crucial for deploying Transformer models in resource-constrained environments. While static quantization applies uniform bit-width across all time steps, time-series data exhibits varying importance across temporal positions. We propose **DynamicQuant**, a novel method that uses attention weights to dynamically allocate bit-widths (8-bit for important steps, 2-bit for others). Extensive experiments on three benchmark datasets show that DynamicQuant achieves **2.3% MSE improvement** over PatchTST baseline while reducing model size by **30%** and inference time by **15%**.

---

## 1. Introduction

### Problem
- Time-series Transformer models are computationally expensive
- Static quantization treats all time steps equally
- Important temporal patterns get insufficient precision

### Motivation
- Attention weights naturally capture time-step importance
- Dynamic allocation can improve both efficiency and accuracy
- No existing work on dynamic quantization for time-series

### Contributions
1. First dynamic quantization method for time-series Transformers
2. Attention-based bit-width allocation mechanism
3. Theoretical analysis of compression-accuracy trade-off
4. Extensive experiments on 5 benchmark datasets

---

## 2. Method

### Overview
DynamicQuant uses attention weights from Transformer layers to determine the importance of each time step, then allocates higher precision (8-bit) to important steps and lower precision (2-bit) to less important ones.

### Key Components
1. **Attention Weight Extraction**: Compute attention weights in each layer
2. **Importance Aggregation**: Average across heads, normalize to [0,1]
3. **Bit Allocation**: Threshold-based allocation (threshold = 0.7)
4. **Dynamic Quantization**: Apply bit-width per time step
5. **Training**: Straight-through estimator for gradient flow

### Innovation
- First to use attention weights for bit allocation in time-series
- Novel threshold-based allocation strategy
- End-to-end training with compression regularization

---

## 3. Experiments

### Datasets
- ETTh1: 17,420 samples, 7 features
- ETTh2: 17,420 samples, 7 features
- ETTm1: 69,680 samples, 7 features

### Baselines
1. PatchTST (2023) - Current SOTA
2. iTransformer (2024)
3. TimesNet (2023)
4. Static 2-bit quantization
5. Static 4-bit quantization

### Main Results

**ETTh1 Dataset (MSE, lower is better)**:

| Method | 96 | 192 | 336 | 720 | Size |
|--------|-----|-----|-----|-----|------|
| PatchTST | 0.370 | 0.413 | 0.422 | 0.436 | 12MB |
| Static 2-bit | 0.412 | 0.458 | 0.472 | 0.490 | 3MB |
| Static 4-bit | 0.389 | 0.435 | 0.448 | 0.465 | 6MB |
| **DynamicQuant** | **0.361** | **0.405** | **0.415** | **0.430** | **8.4MB** |

**Key Findings**:
- 2.3% improvement over PatchTST (horizon=96)
- 30% model size reduction
- 15% inference speedup
- Statistically significant (p < 0.01)

### Ablation Study

| Component | Contribution |
|-----------|--------------|
| Attention Guidance | 1.9% |
| Dynamic Allocation | 0.5% |
| Straight-Through | 0.3% |

**Finding**: Attention guidance is the key component.

---

## 4. Analysis

### Why Dynamic Works
- Attention weights capture temporal importance
- Important time steps need higher precision
- Less important steps can tolerate lower precision

### Threshold Sensitivity
- Threshold = 0.7 gives best trade-off
- Too low: insufficient compression
- Too high: accuracy degradation

### Failure Cases
- Highly noisy data
- Very short sequences (< 96)
- Sudden distribution shifts

---

## 5. Conclusion

### Summary
- DynamicQuant achieves better accuracy with less computation
- Attention weights effectively guide bit allocation
- Significant compression (30%) with minimal accuracy loss (<3%)

### Impact
- Enables deployment on edge devices
- Reduces inference cost
- Maintains forecasting quality

### Future Work
- Apply to other modalities (text, vision)
- Learnable threshold
- Hardware-aware optimization

---

## Figures to Include

### Figure 1: Architecture Diagram
- Show attention weight extraction
- Show bit allocation mechanism
- Show dynamic quantization process

### Figure 2: Results Comparison
- Bar chart: MSE comparison across methods
- Highlight our method improvement

### Figure 3: Efficiency Analysis
- Scatter plot: Model size vs. accuracy
- Show Pareto frontier

### Figure 4: Attention Visualization
- Heatmap of attention weights
- Show correlation with bit allocation

---

## Key Messages for Presentation

1. **Dynamic beats static**: Our method outperforms uniform quantization
2. **Attention guides allocation**: Attention weights are effective importance indicators
3. **Significant compression**: 30% size reduction with <3% accuracy loss

---

*Source Material - Academic Presentation Example*