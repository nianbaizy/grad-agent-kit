# Slide Structure

> Detailed content for each slide.

---

## Slide 1: Title Slide

**Layout**: Centered title + author info

**Content**:
```
Dynamic Quantization for Time-Series Transformer Models
via Attention-Guided Bit Allocation

[Your Name]
[Your Affiliation]

NeurIPS 2026
```

**Speaker Notes**:
"Good morning. Today I'll present our work on dynamic quantization for time-series Transformers. This is joint work with [collaborators]."

**Time**: 30 seconds

---

## Slide 2: Motivation - Why Compression?

**Layout**: Problem statement + bullet points

**Content**:
```
Why Model Compression?

• Transformers are powerful but expensive
• Time-series forecasting requires real-time inference
• Edge deployment has strict resource constraints
• Static quantization treats all time steps equally

[Figure: Computational cost comparison]
```

**Speaker Notes**:
"Transformers have achieved state-of-the-art performance in time-series forecasting. However, they're computationally expensive, making deployment on edge devices challenging. Model compression is crucial, but existing methods treat all time steps equally."

**Time**: 1 minute

---

## Slide 3: Problem - Static vs Dynamic

**Layout**: Comparison diagram

**Content**:
```
Static vs Dynamic Quantization

Static:                    Dynamic:
┌─────────────────┐       ┌─────────────────┐
│ All 4-bit       │       │ 8-bit (important)│
│                 │       │ 2-bit (others)   │
└─────────────────┘       └─────────────────┘

Problem: Time steps have varying importance!
[Figure: Attention weights showing importance]
```

**Speaker Notes**:
"The key insight is that not all time steps are equally important. Attention weights naturally capture this importance. Why should we allocate the same precision to all steps?"

**Time**: 1 minute

---

## Slide 4: Method Overview

**Layout**: Architecture diagram

**Content**:
```
DynamicQuant: Attention-Guided Bit Allocation

[Architecture Diagram]
Input → Transformer → Attention Weights → Bit Allocation → Quantized Output

Key Innovation:
• Extract attention weights
• Compute importance scores
• Allocate 8-bit or 2-bit dynamically
```

**Speaker Notes**:
"Our method, DynamicQuant, uses attention weights to guide bit allocation. We extract attention weights from each layer, compute importance scores, and allocate higher precision to important time steps."

**Time**: 1.5 minutes

---

## Slide 5: Attention Mechanism

**Layout**: Attention visualization

**Content**:
```
Attention Captures Temporal Importance

[Heatmap: Attention weights across time steps]

• Darker = higher attention = more important
• Important steps get 8-bit precision
• Less important steps get 2-bit precision
```

**Speaker Notes**:
"Here you can see attention weights from a trained model. Darker regions indicate higher attention. Our method uses these weights to determine which time steps need higher precision."

**Time**: 1 minute

---

## Slide 6: Bit Allocation Strategy

**Layout**: Decision flowchart

**Content**:
```
Bit Allocation Decision

Importance Score > 0.7?
        ↓ Yes              ↓ No
    8-bit precision    2-bit precision

Training: Straight-Through Estimator
• Forward: quantize
• Backward: pass gradient through
```

**Speaker Notes**:
"We use a simple threshold-based allocation. If importance score exceeds 0.7, we use 8-bit; otherwise, 2-bit. For training, we use straight-through estimators to handle the non-differentiable quantization."

**Time**: 1 minute

---

## Slide 7: Key Innovation

**Layout**: Contribution highlights

**Content**:
```
Our Contributions

1. First dynamic quantization for time-series
   → No existing work in this direction

2. Attention-based bit allocation
   → Leverages natural importance signals

3. Theoretical analysis
   → Compression-accuracy trade-off bounds

4. Extensive experiments
   → 5 datasets, 5 baselines
```

**Speaker Notes**:
"Our contributions are threefold. First, we're the first to apply dynamic quantization to time-series models. Second, we propose a novel attention-based allocation mechanism. Third, we provide theoretical analysis and extensive experiments."

**Time**: 1 minute

---

## Slide 8: Experimental Setup

**Layout**: Table + dataset info

**Content**:
```
Experimental Setup

Datasets:
• ETTh1: 17K samples, hourly
• ETTh2: 17K samples, hourly  
• ETTm1: 70K samples, 15-min

Baselines:
• PatchTST (2023) - Current SOTA
• iTransformer (2024)
• TimesNet (2023)
• Static 2-bit, 4-bit

Metrics: MSE, MAE
```

**Speaker Notes**:
"We evaluate on three widely-used benchmarks. We compare against five baselines, including the current state-of-the-art PatchTST. We report MSE and MAE metrics."

**Time**: 1 minute

---

## Slide 9: Main Results

**Layout**: Comparison table

**Content**:
```
Main Results (ETTh1, MSE)

| Method    | 96   | 192  | 336  | 720  | Size |
|-----------|------|------|------|------|------|
| PatchTST  | 0.370| 0.413| 0.422| 0.436| 12MB |
| Static 2b | 0.412| 0.458| 0.472| 0.490| 3MB  |
| Static 4b | 0.389| 0.435| 0.448| 0.465| 6MB  |
| DynamicQuant| 0.361| 0.405| 0.415| 0.430| 8.4MB|

✓ 2.3% improvement over PatchTST
✓ 30% smaller model
```

**Speaker Notes**:
"Here are our main results on ETTh1. Our method achieves 2.3% MSE improvement over PatchTST while reducing model size by 30%. The improvement is consistent across all prediction horizons."

**Time**: 1.5 minutes

---

## Slide 10: Efficiency Analysis

**Layout**: Scatter plot

**Content**:
```
Efficiency Trade-off

[Scatter plot: Model Size vs MSE]
• X-axis: Model Size (MB)
• Y-axis: MSE
• Points: Different methods
• Highlight: Our method on Pareto frontier

Key: Better accuracy AND smaller size!
```

**Speaker Notes**:
"This scatter plot shows the trade-off between model size and accuracy. Our method achieves better accuracy with smaller model size - we're on the Pareto frontier, meaning no other method dominates us in both dimensions."

**Time**: 1 minute

---

## Slide 11: Ablation Study

**Layout**: Component breakdown

**Content**:
```
Ablation Study

| Component          | Contribution |
|--------------------|--------------|
| Attention Guidance | 1.9%         |
| Dynamic Allocation | 0.5%         |
| Straight-Through   | 0.3%         |
| **Total**          | **2.7%**     |

Key Finding: Attention guidance is crucial!
```

**Speaker Notes**:
"Our ablation study shows that attention guidance contributes 1.9% of the total 2.7% improvement. This confirms that attention weights are effective importance indicators."

**Time**: 1.5 minutes

---

## Slide 12: Failure Cases & Limitations

**Layout**: Honest assessment

**Content**:
```
Limitations

1. Threshold sensitivity
   → Performance depends on threshold choice

2. Noisy data
   → Attention weights become unreliable

3. Short sequences
   → Need ≥ 96 time steps

4. Hardware support
   → 2-bit needs specialized hardware
```

**Speaker Notes**:
"We're honest about limitations. Our method is sensitive to threshold choice, struggles with very noisy data, and requires specialized hardware for 2-bit quantization. We're working on addressing these."

**Time**: 1 minute

---

## Slide 13: Conclusion

**Layout**: Summary points

**Content**:
```
Conclusion

✓ First dynamic quantization for time-series
✓ Attention-based bit allocation
✓ 30% compression, <3% accuracy loss
✓ 15% inference speedup

Impact: Enables edge deployment of Transformers
```

**Speaker Notes**:
"In conclusion, we propose the first dynamic quantization method for time-series Transformers. Our attention-based allocation achieves 30% compression with less than 3% accuracy loss, enabling deployment on edge devices."

**Time**: 1 minute

---

## Slide 14: Future Work

**Layout**: Research directions

**Content**:
```
Future Work

1. Apply to other modalities
   → Text, Vision, Multimodal

2. Learnable threshold
   → Adapt to data automatically

3. Hardware-aware optimization
   → Co-design with accelerators

4. Real-world deployment
   → Edge devices, IoT
```

**Speaker Notes**:
"We see several exciting directions. First, applying dynamic quantization to other modalities. Second, learning the threshold automatically. Third, co-designing with hardware accelerators for optimal performance."

**Time**: 1 minute

---

## Slide 15: Thank You

**Layout**: Contact info + Q&A

**Content**:
```
Thank You!

Questions?

[Your Name]
[Email]
[GitHub]
[Paper Link]

Code: github.com/your-repo/DynamicQuant
```

**Speaker Notes**:
"Thank you for your attention. I'm happy to take questions. Code is available at [GitHub link]."

**Time**: Q&A (5 minutes)

---

## Design Notes

### Color Scheme
- Primary: #2196F3 (Blue)
- Accent: #FF9800 (Orange)
- Success: #4CAF50 (Green)
- Background: #FFFFFF

### Typography
- Title: 36pt, Bold
- Headings: 28pt, Bold
- Body: 24pt, Regular
- Code: 20pt, Monospace

### Animations
- Fade in for bullet points
- Highlight for key results
- Zoom for architecture diagram

---

*Slide Structure - Academic Presentation Example*