# Paper Writer - Output Format

> Expected output structure for paper-writer skill.

---

## Primary Deliverables

### 1. paper-draft.md

**Purpose**: Complete research paper draft

**Structure**:
```markdown
# [Paper Title]

## Abstract
[150-250 words]

## 1. Introduction
### 1.1 Problem Statement
### 1.2 Motivation
### 1.3 Contributions

## 2. Related Work
### 2.1 [Topic Area 1]
### 2.2 [Topic Area 2]
### 2.3 [Topic Area 3]

## 3. Method
### 3.1 Overview
### 3.2 [Component 1]
### 3.3 [Component 2]
### 3.4 [Component 3]

## 4. Experiments
### 4.1 Setup
### 4.2 Datasets
### 4.3 Baselines
### 4.4 Main Results
### 4.5 Ablation Study
### 4.6 Analysis

## 5. Discussion
### 5.1 Limitations
### 5.2 Future Work
### 5.3 Broader Impact

## 6. Conclusion

## References
[1] [CITATION NEEDED]
[2] [CITATION NEEDED]
...
```

**Requirements**:
- Follow academic writing conventions
- Use placeholder citations [1], [2], etc.
- Mark TODOs for user input
- Include section numbers
- Use consistent terminology

---

### 2. references.bib

**Purpose**: Bibliography file with placeholder entries

**Structure**:
```bibtex
@article{placeholder1,
  title={[TODO: Add title]},
  author={[TODO: Add authors]},
  journal={[TODO: Add journal]},
  year={[TODO: Add year]},
  note={[CITATION NEEDED]}
}

@inproceedings{placeholder2,
  title={[TODO: Add title]},
  author={[TODO: Add authors]},
  booktitle={[TODO: Add conference]},
  year={[TODO: Add year]},
  note={[CITATION NEEDED]}
}
```

**Requirements**:
- Use proper BibTeX format
- Include all referenced papers
- Mark placeholders clearly
- Use consistent entry types

---

### 3. outline.md

**Purpose**: Paper structure outline

**Structure**:
```markdown
# Paper Outline

## Title
[Working title]

## Abstract (150-250 words)
- Problem: [1-2 sentences]
- Method: [1-2 sentences]
- Results: [1-2 sentences]
- Contributions: [1-2 sentences]

## 1. Introduction (1-1.5 pages)
### 1.1 Problem Statement
- [Point 1]
- [Point 2]

### 1.2 Motivation
- [Point 1]
- [Point 2]

### 1.3 Contributions
1. [Contribution 1]
2. [Contribution 2]
3. [Contribution 3]

## 2. Related Work (1-1.5 pages)
### 2.1 [Topic 1]
- [Key papers]
- [Gaps]

### 2.2 [Topic 2]
- [Key papers]
- [Gaps]

## 3. Method (2-3 pages)
### 3.1 Overview
- [High-level description]

### 3.2 [Component 1]
- [Details]

### 3.3 [Component 2]
- [Details]

## 4. Experiments (2-3 pages)
### 4.1 Setup
- [Datasets]
- [Metrics]
- [Implementation details]

### 4.2 Main Results
- [Table: Comparison with baselines]
- [Analysis]

### 4.3 Ablation Study
- [Component analysis]
- [Parameter sensitivity]

## 5. Discussion (0.5-1 page)
### 5.1 Limitations
- [Limitation 1]
- [Limitation 2]

### 5.2 Future Work
- [Direction 1]
- [Direction 2]

## 6. Conclusion (0.5 page)
- [Summary]
- [Impact]
```

---

## Secondary Deliverables

### 4. quality-report.md

**Purpose**: Quality check results

**Structure**:
```markdown
# Quality Report

## Summary
- Overall score: [X/10]
- Sections complete: [X/6]
- Issues found: [X]

## Section Analysis
### Abstract
- [Status]
- [Issues]

### Introduction
- [Status]
- [Issues]

[Continue for all sections]

## Recommendations
1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

## Checklist Results
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]
```

---

### 5. next-steps.md

**Purpose**: Recommended improvements

**Structure**:
```markdown
# Next Steps

## Immediate Actions
1. [Action 1]
2. [Action 2]
3. [Action 3]

## Improvements Needed
### Content
- [Improvement 1]
- [Improvement 2]

### Structure
- [Improvement 1]
- [Improvement 2]

### Language
- [Improvement 1]
- [Improvement 2]

## Missing Elements
- [ ] [Element 1]
- [ ] [Element 2]
- [ ] [Element 3]

## Timeline
- [ ] Week 1: [Task]
- [ ] Week 2: [Task]
- [ ] Week 3: [Task]
```

---

## File Organization

```
output/
├── paper-draft.md          # Complete paper draft
├── references.bib          # Bibliography file
├── outline.md              # Paper structure
├── quality-report.md       # Quality check results
└── next-steps.md           # Recommended actions
```

---

## Formatting Rules

### General
- Use Markdown format
- Include section headers (##, ###)
- Use consistent formatting
- Add placeholder citations [1], [2], etc.

### Academic Writing
- Use formal tone
- Be precise and concise
- Avoid colloquial language
- Use technical terminology correctly

### Citations
- Use numbered citations: [1], [2], [3]
- Include all referenced works
- Use proper citation format
- Mark missing citations: [CITATION NEEDED]

### TODOs
- Mark user-required input: [TODO: Add specific results]
- Mark areas needing revision: [TODO: Revise this section]
- Mark missing information: [TODO: Add implementation details]

---

## Quality Indicators

### Good Output
✅ Complete paper structure
✅ Clear problem statement
✅ Detailed method description
✅ Comprehensive experiments
✅ Honest limitations discussion
✅ Proper citation placeholders

### Bad Output
❌ Missing sections
❌ Vague descriptions
❌ Incomplete experiments
❌ Unsupported claims
❌ Fabricated citations
❌ Poor organization

---

*Paper Writer Output Format - Part of GradAgentKit*