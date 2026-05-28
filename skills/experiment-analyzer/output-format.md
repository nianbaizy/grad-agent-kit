# Experiment Analyzer - Output Format

> Expected output structure for experiment-analyzer skill.

---

## Primary Deliverables

### 1. analysis-report.md

**Purpose**: Comprehensive experiment analysis report

**Structure**:
```markdown
# Experiment Analysis Report

## Executive Summary
- Key findings (3-5 bullet points)
- Overall performance improvement
- Statistical significance status

## 1. Data Overview
### 1.1 Dataset Description
- Datasets used
- Data characteristics
- Preprocessing applied

### 1.2 Experimental Setup
- Model configurations
- Hyperparameters
- Training settings

## 2. Baseline Comparison
### 2.1 Performance Metrics
- [Table: Comparison with baselines]
- [Key observations]

### 2.2 Improvement Analysis
- Percentage improvements
- Statistical significance tests
- Effect size calculations

### 2.3 Per-Dataset Analysis
- Dataset-specific results
- Performance variations
- Outlier investigation

## 3. Ablation Study
### 3.1 Component Analysis
- [Table: Component-wise results]
- Contribution percentages
- Critical components identified

### 3.2 Interaction Effects
- Component synergies
- Redundancies discovered
- Optimal configurations

### 3.3 Parameter Sensitivity
- Hyperparameter impact
- Robustness analysis
- Recommended ranges

## 4. Training Dynamics
### 4.1 Loss Curves
- Training loss progression
- Validation loss progression
- Convergence analysis

### 4.2 Learning Rate Analysis
- Schedule effectiveness
- Optimal learning rate
- Stability observations

### 4.3 Early Stopping
- Stopping criteria analysis
- Overfitting detection
- Optimal epoch determination

## 5. Statistical Analysis
### 5.1 Significance Tests
- t-test results
- p-values reported
- Confidence intervals

### 5.2 Effect Size
- Cohen's d calculations
- Practical significance
- Magnitude interpretation

### 5.3 Variance Analysis
- Standard deviations
- Reproducibility assessment
- Consistency metrics

## 6. Interpretation
### 6.1 Success Factors
- Why method works
- Key design elements
- Performance drivers

### 6.2 Limitations
- Where method fails
- Edge cases identified
- Constraints discovered

### 6.3 Practical Implications
- Real-world applicability
- Deployment considerations
- Resource requirements

## 7. Recommendations
### 7.1 Immediate Improvements
- Quick fixes identified
- Low-hanging fruit
- Parameter adjustments

### 7.2 Future Experiments
- Suggested ablations
- Additional baselines
- Extended evaluations

### 7.3 Method Enhancements
- Architecture modifications
- Training strategies
- Optimization techniques

## 8. Visualization Suggestions
### 8.1 Recommended Charts
- Performance comparison plots
- Ablation study visualizations
- Training dynamics graphs

### 8.2 Table Formats
- LaTeX table templates
- Markdown alternatives
- Presentation-ready formats

## 9. Conclusion
- Summary of findings
- Key contributions validated
- Next steps outlined

## Appendix
### A. Raw Data
- Complete results tables
- Additional metrics
- Supplementary data

### B. Statistical Details
- Test assumptions verified
- Calculation methods
- Software versions used

### C. Configuration Details
- Full hyperparameters
- Environment setup
- Reproducibility information
```

**Requirements**:
- Use clear section headers
- Include data tables
- Provide statistical evidence
- Mark uncertainties
- Suggest visualizations

---

### 2. results-summary.md

**Purpose**: Concise summary of key findings

**Structure**:
```markdown
# Results Summary

## Key Metrics
| Metric | Baseline | Our Method | Improvement | p-value |
|--------|----------|------------|-------------|---------|
| MSE | 0.385 | 0.376 | -2.3% | 0.003 |
| MAE | 0.412 | 0.403 | -2.2% | 0.005 |
| Time | 15ms | 16ms | +6.7% | 0.12 |

## Top Findings
1. **Performance Gain**: 2.3% MSE improvement over SOTA baseline
2. **Statistical Significance**: p < 0.01 across all metrics
3. **Efficiency Trade-off**: Minimal inference time increase (+1ms)
4. **Robustness**: Consistent improvement across 5 datasets

## Ablation Results
| Component | Contribution | Critical? |
|-----------|--------------|-----------|
| Attention | 1.8% | Yes |
| Dynamic Allocation | 0.5% | Moderate |
| Both Combined | 2.3% | Synergistic |

## Statistical Confidence
- **Sample Size**: 5 independent runs
- **Confidence Level**: 95%
- **Effect Size**: Cohen's d = 0.85 (large)

## Quick Takeaways
- Method is statistically superior to baselines
- Attention mechanism is critical component
- Results are reproducible and robust
- Ready for paper submission
```

---

### 3. ablation-analysis.md

**Purpose**: Detailed component-wise analysis

**Structure**:
```markdown
# Ablation Study Analysis

## Overview
- Total components analyzed: N
- Critical components identified: M
- Synergistic effects discovered: K

## Component Analysis

### Component 1: [Name]
- **Contribution**: X% improvement
- **Criticality**: High/Medium/Low
- **Interactions**: Works well with [Component X]
- **Recommendation**: Keep/Modify/Remove

### Component 2: [Name]
- **Contribution**: Y% improvement
- **Criticality**: High/Medium/Low
- **Interactions**: Conflicts with [Component Z]
- **Recommendation**: Keep/Modify/Remove

## Interaction Matrix
| | Comp A | Comp B | Comp C |
|---|---|---|---|
| Comp A | - | Synergy | Neutral |
| Comp B | Synergy | - | Conflict |
| Comp C | Neutral | Conflict | - |

## Optimal Configuration
```
Best: [Comp A + Comp B]
Avoid: [Comp B + Comp C]
```

## Recommendations
1. Keep Components A and B (synergistic)
2. Consider removing Component C (conflicts with B)
3. Test alternative implementations of Component C
```

---

## Secondary Deliverables

### 4. recommendations.md

**Purpose**: Actionable improvement suggestions

**Structure**:
```markdown
# Recommendations

## Immediate Actions
1. **Hyperparameter Tuning**
   - Try learning rate: [range]
   - Adjust batch size: [suggestion]
   - Modify regularization: [technique]

2. **Architecture Changes**
   - Add [component] to improve [metric]
   - Remove [component] to reduce [issue]
   - Modify [component] for better [performance]

3. **Training Strategies**
   - Implement [technique] for [benefit]
   - Use [scheduler] for [improvement]
   - Apply [augmentation] for [robustness]

## Future Experiments
### Short-term (1-2 weeks)
- [ ] Experiment with [alternative]
- [ ] Test on [additional dataset]
- [ ] Validate with [different metric]

### Medium-term (1 month)
- [ ] Implement [enhancement]
- [ ] Compare with [new baseline]
- [ ] Analyze [specific aspect]

### Long-term (3 months)
- [ ] Explore [research direction]
- [ ] Develop [new component]
- [ ] Publish [findings]

## Risk Assessment
- **High Risk**: [Experiment] - [Why risky]
- **Medium Risk**: [Experiment] - [Why risky]
- **Low Risk**: [Experiment] - [Why safe]
```

---

### 5. visualization-suggestions.md

**Purpose**: Recommended charts and plots

**Structure**:
```markdown
# Visualization Suggestions

## Performance Comparison

### Bar Chart: MSE Comparison
```python
import matplotlib.pyplot as plt
import numpy as np

methods = ['PatchTST', 'iTransformer', 'Our Method']
mse_values = [0.385, 0.378, 0.376]
errors = [0.004, 0.003, 0.003]

plt.figure(figsize=(8, 6))
plt.bar(methods, mse_values, yerr=errors, capsize=5)
plt.ylabel('MSE (lower is better)')
plt.title('Performance Comparison')
plt.savefig('mse_comparison.png', dpi=300)
```

### Line Plot: Training Curves
```python
epochs = range(1, 51)
train_loss = [...]  # Your data
val_loss = [...]    # Your data

plt.figure(figsize=(10, 6))
plt.plot(epochs, train_loss, label='Training Loss')
plt.plot(epochs, val_loss, label='Validation Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training Dynamics')
plt.legend()
plt.savefig('training_curves.png', dpi=300)
```

## Ablation Study

### Stacked Bar: Component Contributions
```python
components = ['Full Model', 'w/o Attention', 'w/o Dynamic', 'w/o Both']
mse_values = [0.376, 0.389, 0.392, 0.395]

plt.figure(figsize=(8, 6))
plt.bar(components, mse_values)
plt.ylabel('MSE')
plt.title('Ablation Study Results')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('ablation_results.png', dpi=300)
```

### Heatmap: Component Interactions
```python
import seaborn as sns

# Your interaction matrix data
interaction_matrix = [...]

plt.figure(figsize=(8, 6))
sns.heatmap(interaction_matrix, annot=True, cmap='coolwarm')
plt.title('Component Interaction Matrix')
plt.savefig('interaction_heatmap.png', dpi=300)
```

## Statistical Analysis

### Box Plot: Distribution of Results
```python
data = [run1_mse, run2_mse, run3_mse, run4_mse, run5_mse]

plt.figure(figsize=(8, 6))
plt.boxplot(data, labels=['Our Method'])
plt.ylabel('MSE')
plt.title('Result Distribution (5 runs)')
plt.savefig('result_distribution.png', dpi=300)
```

### Error Bar Plot: Confidence Intervals
```python
methods = ['Baseline', 'Our Method']
means = [0.385, 0.376]
ci_lower = [0.381, 0.373]
ci_upper = [0.389, 0.379]

plt.figure(figsize=(8, 6))
plt.errorbar(methods, means, 
             yerr=[means - ci_lower, ci_upper - means],
             fmt='o', capsize=5, capthick=2)
plt.ylabel('MSE')
plt.title('95% Confidence Intervals')
plt.savefig('confidence_intervals.png', dpi=300)
```

## LaTeX Templates

### Performance Table
```latex
\begin{table}[h]
\centering
\caption{Performance Comparison}
\label{tab:performance}
\begin{tabular}{lccc}
\hline
Method & MSE & MAE & Time (ms) \\
\hline
PatchTST & 0.385 & 0.412 & 15 \\
iTransformer & 0.378 & 0.405 & 18 \\
Our Method & \textbf{0.376} & \textbf{0.403} & 16 \\
\hline
\end{tabular}
\end{table}
```

### Ablation Table
```latex
\begin{table}[h]
\centering
\caption{Ablation Study Results}
\label{tab:ablation}
\begin{tabular}{lcc}
\hline
Configuration & MSE & Improvement \\
\hline
Full Model & 0.376 & 2.3\% \\
w/o Attention & 0.389 & 0.5\% \\
w/o Dynamic & 0.392 & 0.0\% \\
w/o Both & 0.395 & -0.5\% \\
\hline
\end{tabular}
\end{table}
```

---

## File Organization

```
output/
├── analysis-report.md          # Main analysis report
├── results-summary.md          # Key findings summary
├── ablation-analysis.md        # Component analysis
├── recommendations.md          # Improvement suggestions
├── visualization-suggestions.md # Chart recommendations
└── figures/                    # Generated visualizations
    ├── mse_comparison.png
    ├── training_curves.png
    ├── ablation_results.png
    └── ...
```

---

## Formatting Rules

### General
- Use Markdown format
- Include section headers (##, ###)
- Use consistent formatting
- Add data tables with clear headers
- Include statistical measures

### Data Presentation
- Use tables for numerical results
- Include error bars or confidence intervals
- Bold best results
- Use consistent decimal places

### Statistical Reporting
- Report p-values: p < 0.05, p < 0.01, p < 0.001
- Include effect sizes: Cohen's d
- Provide confidence intervals: 95% CI
- Mention sample sizes

### LaTeX Compatibility
- Use standard table environments
- Include \label and \caption
- Use \textbf for best results
- Escape special characters

---

## Quality Indicators

### Good Output
✅ Complete analysis structure
✅ Statistical significance reported
✅ Confidence intervals provided
✅ Ablation study included
✅ Clear recommendations
✅ Visualization suggestions

### Bad Output
❌ Missing statistical tests
❌ No confidence intervals
❌ Incomplete ablation analysis
❌ Unsupported conclusions
❌ No recommendations
❌ Poor data presentation

---

*Experiment Analyzer Output Format - Part of GradAgentKit*
