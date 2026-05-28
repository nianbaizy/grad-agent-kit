# Experiment Analyzer - Quality Checklist

> Use this checklist to verify experiment analysis quality.

---

## Pre-Execution Checks

### Input Validation
- [ ] Results data is provided (CSV, JSON, or table)
- [ ] Baseline results are available for comparison
- [ ] Experiment configuration is documented
- [ ] Key metrics are clearly defined
- [ ] Data format is consistent and parseable

### Data Quality
- [ ] No missing values in critical columns
- [ ] Outliers identified and investigated
- [ ] Data units are consistent
- [ ] Results are from valid experiments
- [ ] Multiple runs available (if applicable)

### Skill Selection
- [ ] Correct skill for analysis task
- [ ] Skill version is current
- [ ] All dependencies available
- [ ] Input template completed

---

## Execution Checks

### Workflow Adherence
- [ ] All workflow steps completed
- [ ] Steps executed in correct order
- [ ] No steps skipped
- [ ] Decision points handled correctly
- [ ] Data validation performed

### Quality Gates
- [ ] All quality gates passed
- [ ] No critical issues found
- [ ] Minor issues documented
- [ ] Recommendations provided
- [ ] Statistical methods appropriate

---

## Output Checks

### Completeness
- [ ] All required files generated
- [ ] All sections present
- [ ] No placeholder content left
- [ ] All TODOs resolved or marked
- [ ] Analysis covers all provided data

### Accuracy
- [ ] Facts are correct
- [ ] No fabricated information
- [ ] Statistical calculations verified
- [ ] Data is accurately represented
- [ ] Improvements calculated correctly

### Structure
- [ ] Follows analysis report format
- [ ] Logical flow between sections
- [ ] Clear section headings
- [ ] Proper numbering
- [ ] Tables well-formatted

---

## Content Quality

### Executive Summary
- [ ] Key findings highlighted
- [ ] Overall improvement stated
- [ ] Statistical significance mentioned
- [ ] Clear and concise
- [ ] Captures main contributions

### Data Overview
- [ ] Datasets described
- [ ] Experimental setup documented
- [ ] Configurations specified
- [ ] Preprocessing steps noted
- [ ] Reproducibility information included

### Baseline Comparison
- [ ] All baselines listed
- [ ] Fair comparison ensured
- [ ] Improvements calculated
- [ ] Statistical tests performed
- [ ] Results presented clearly

### Ablation Study
- [ ] All components analyzed
- [ ] Contributions quantified
- [ ] Interactions identified
- [ ] Critical components highlighted
- [ ] Recommendations provided

### Training Dynamics
- [ ] Loss curves analyzed
- [ ] Convergence discussed
- [ ] Overfitting detected (if any)
- [ ] Learning rate effects noted
- [ ] Training stability assessed

### Statistical Analysis
- [ ] Significance tests performed
- [ ] p-values reported
- [ ] Confidence intervals provided
- [ ] Effect sizes calculated
- [ ] Sample sizes mentioned

### Interpretation
- [ ] Results explained clearly
- [ ] Success factors identified
- [ ] Limitations acknowledged
- [ ] Alternative explanations considered
- [ ] Causal claims supported

### Recommendations
- [ ] Actionable suggestions provided
- [ ] Immediate improvements identified
- [ ] Future experiments suggested
- [ ] Risk assessment included
- [ ] Prioritization clear

---

## Technical Quality

### Statistical Rigor
- [ ] Appropriate tests used (t-test, ANOVA, etc.)
- [ ] Assumptions verified
- [ ] Multiple comparison correction (if needed)
- [ ] Effect size reported
- [ ] Practical significance discussed

### Data Analysis
- [ ] Trends identified
- [ ] Correlations analyzed
- [ ] Anomalies investigated
- [ ] Patterns explained
- [ ] Variability accounted for

### Methodology
- [ ] Analysis methods appropriate
- [ ] Techniques are valid
- [ ] Assumptions are reasonable
- [ ] Limitations of methods noted
- [ ] Alternative methods considered

---

## Reporting Quality

### Tables
- [ ] Clear headers
- [ ] Consistent formatting
- [ ] Appropriate decimal places
- [ ] Best results highlighted
- [ ] Units specified

### Figures
- [ ] Appropriate chart types
- [ ] Clear labels and legends
- [ ] Error bars included
- [ ] High resolution
- [ ] Accessible colors

### Text
- [ ] Clear and concise
- [ ] Academic tone
- [ ] No jargon without explanation
- [ ] Consistent terminology
- [ ] Proper grammar

### Citations
- [ ] Baseline methods cited
- [ ] Statistical methods referenced
- [ ] Tools and software noted
- [ ] Datasets attributed
- [ ] No fabricated references

---

## Statistical Quality

### Significance Testing
- [ ] Appropriate test selected
- [ ] Assumptions met
- [ ] p-values reported correctly
- [ ] One-tailed vs two-tailed justified
- [ ] Multiple comparisons handled

### Effect Size
- [ ] Cohen's d calculated
- [ ] Magnitude interpreted
- [ ] Practical significance discussed
- [ ] Confidence intervals provided
- [ ] Effect size context given

### Confidence Intervals
- [ ] 95% CI calculated
- [ ] CI width reasonable
- [ ] CI interpretation clear
- [ ] Sample size adequate
- [ ] Precision assessed

---

## Ablation Quality

### Component Analysis
- [ ] All components tested
- [ ] Individual contributions measured
- [ ] Interactions identified
- [ ] Critical components flagged
- [ ] Redundancies detected

### Configuration Testing
- [ ] Optimal configuration identified
- [ ] Parameter sensitivity analyzed
- [ ] Robustness assessed
- [ ] Edge cases tested
- [ ] Recommendations provided

---

## Interpretation Quality

### Success Factors
- [ ] Why method works explained
- [ ] Key design elements identified
- [ ] Performance drivers analyzed
- [ ] Theoretical justification provided
- [ ] Empirical evidence cited

### Limitations
- [ ] Failure cases identified
- [ ] Constraints documented
- [ ] Scope boundaries defined
- [ ] Generalizability assessed
- [ ] Honest assessment provided

### Practical Implications
- [ ] Real-world applicability discussed
- [ ] Deployment considerations noted
- [ ] Resource requirements specified
- [ ] Cost-benefit analysis included
- [ ] Scalability addressed

---

## Final Checks

### Overall Quality
- [ ] Meets analysis objectives
- [ ] Addresses all research questions
- [ ] Supports paper claims
- [ ] Ready for human review
- [ ] Publication-ready quality

### Deliverables
- [ ] analysis-report.md complete
- [ ] results-summary.md generated
- [ ] ablation-analysis.md provided
- [ ] recommendations.md included
- [ ] visualization-suggestions.md ready

---

## Issue Tracking

### Critical Issues
- [ ] Issue 1: [Description]
- [ ] Issue 2: [Description]
- [ ] Issue 3: [Description]

### Minor Issues
- [ ] Issue 1: [Description]
- [ ] Issue 2: [Description]
- [ ] Issue 3: [Description]

### Recommendations
- [ ] Recommendation 1: [Description]
- [ ] Recommendation 2: [Description]
- [ ] Recommendation 3: [Description]

---

## Sign-off

- [ ] Quality reviewer: [Name]
- [ ] Date: [Date]
- [ ] Status: [Pass / Fail / Conditional]
- [ ] Ready for paper integration: [Yes / No / Needs revision]

---

*Experiment Analyzer Quality Checklist - Part of GradAgentKit*
