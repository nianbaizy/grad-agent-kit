# Experiment Analyzer - Input Template

> Use this template when calling the experiment-analyzer skill.

---

## Task

**What type of analysis do you need?**

- [ ] Full analysis report
- [ ] Baseline comparison only
- [ ] Ablation study analysis only
- [ ] Training dynamics analysis only
- [ ] Statistical significance test only

---

## Experiment Results

**Provide your experimental results data**

**Format Options**:
- CSV file
- JSON file
- Markdown table
- Paste directly below

**Example (CSV format)**:
```csv
Method,MSE,MAE,Inference_Time,Parameters
Baseline,0.385,0.412,15ms,12.5M
Our_Method,0.376,0.403,16ms,12.8M
Variant_A,0.381,0.408,14ms,12.6M
Variant_B,0.379,0.405,15ms,12.7M
```

**Example (Markdown table)**:
```
| Method | MSE | MAE | Inference_Time | Parameters |
|--------|-----|-----|----------------|------------|
| Baseline | 0.385 | 0.412 | 15ms | 12.5M |
| Our_Method | 0.376 | 0.403 | 16ms | 12.8M |
```

---

## Baseline Methods

**What methods do you compare against?**

[List baseline methods with brief descriptions]

**Example**:
```
1. PatchTST (2023) - Current SOTA for time-series forecasting
2. iTransformer (2024) - Attention-based approach
3. TimesNet (2023) - Multi-scale method
4. Static quantization (2-bit) - Compression baseline
```

---

## Experiment Configuration

**What settings were used?**

### Datasets
- [ ] ETTh1
- [ ] ETTh2
- [ ] ETTm1
- [ ] ETTm2
- [ ] Weather
- [ ] Electricity
- [ ] Traffic
- [ ] Other: _____________

### Evaluation Metrics
- [ ] MSE (Mean Squared Error)
- [ ] MAE (Mean Absolute Error)
- [ ] RMSE (Root Mean Squared Error)
- [ ] MAPE (Mean Absolute Percentage Error)
- [ ] Inference Time
- [ ] Model Size
- [ ] FLOPs
- [ ] Other: _____________

### Prediction Horizons
- [ ] Short-term: 96, 192
- [ ] Medium-term: 336, 512
- [ ] Long-term: 720, 960
- [ ] Custom: _____________

---

## Ablation Study Results

**Do you have ablation study results?**

**If yes, provide component-wise results**:

**Example**:
```
| Configuration | MSE | Improvement |
|---------------|-----|-------------|
| Full Model | 0.376 | 2.3% |
| w/o Attention | 0.389 | 0.5% |
| w/o Dynamic Allocation | 0.392 | 0.0% |
| w/o Both | 0.395 | -0.5% |
```

---

## Training Logs

**Do you have training logs?**

**If yes, provide key information**:
- Training loss curve data
- Validation loss curve data
- Learning rate schedule
- Number of epochs
- Early stopping criteria

**Example**:
```
Epoch 1: Train Loss = 0.45, Val Loss = 0.42
Epoch 10: Train Loss = 0.38, Val Loss = 0.37
Epoch 20: Train Loss = 0.35, Val Loss = 0.34
...
Final: Train Loss = 0.32, Val Loss = 0.33
```

---

## Statistical Analysis

**Do you have multiple runs?**

- [ ] Yes, I have multiple runs (recommended)
- [ ] No, single run only

**If multiple runs, provide**:
- Number of runs: _____
- Mean and standard deviation
- Confidence intervals

**Example**:
```
Our Method: 0.376 ± 0.003 (5 runs, 95% CI)
Baseline: 0.385 ± 0.004 (5 runs, 95% CI)
```

---

## Analysis Goals

**What do you want to understand?**

- [ ] Why our method outperforms baselines
- [ ] Which components contribute most to performance
- [ ] How training dynamics affect results
- [ ] Statistical significance of improvements
- [ ] Practical implications of results
- [ ] Limitations and failure cases
- [ ] Recommendations for improvement

---

## Target Venue

**Where will this analysis be used?**

- [ ] Research paper (SCI journal)
- [ ] Conference paper (NeurIPS, ICML, ICLR, etc.)
- [ ] Thesis or dissertation
- [ ] Technical report
- [ ] Presentation slides

**Venue-specific requirements**:
- Statistical rigor level: _____ (high/medium/low)
- Required significance level: _____ (p < 0.05, p < 0.01, etc.)
- Number of baselines required: _____

---

## Optional Information

### Visualization Preferences
- [ ] Generate comparison tables
- [ ] Suggest appropriate charts
- [ ] Recommend error bars
- [ ] Include confidence intervals

### Language
- [ ] English
- [ ] Chinese

### Output Format
- [ ] Markdown only
- [ ] LaTeX compatible
- [ ] Both

### Additional Context
**Any other relevant information?**

[Add any other context about your experiments]

---

## Example Complete Input

```markdown
## Task
Full analysis report

## Experiment Results
Method,MSE,MAE,Inference_Time
PatchTST,0.385,0.412,15ms
iTransformer,0.378,0.405,18ms
Our_Method,0.376,0.403,16ms

## Baseline Methods
1. PatchTST (2023) - Current SOTA
2. iTransformer (2024) - Attention-based

## Experiment Configuration
Datasets: ETTh1, ETTh2
Metrics: MSE, MAE, Inference Time
Prediction Horizons: 96, 192, 336, 512

## Ablation Study Results
Configuration,MSE,Improvement
Full_Model,0.376,2.3%
w/o_Attention,0.389,0.5%
w/o_Dynamic,0.392,0.0%

## Statistical Analysis
Multiple runs: Yes, 5 runs
Our Method: 0.376 ± 0.003
Baseline: 0.385 ± 0.004

## Analysis Goals
- Why our method outperforms baselines
- Which components contribute most
- Statistical significance

## Target Venue
Research paper (SCI journal)
Statistical rigor: High
Significance level: p < 0.05
```

---

*Experiment Analyzer Input Template - Part of GradAgentKit*
