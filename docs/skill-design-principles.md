# Skill Design Principles

> How to design high-quality agent skills for GradAgentKit.

---

## Overview

Every skill in GradAgentKit follows 7 core principles to ensure quality, reusability, and reliability.

---

## 1. Role Clarity

**Principle**: Each skill must have a clear agent identity and expertise.

**Requirements**:
- Define what type of agent this is
- Specify the agent's expertise area
- Clarify the agent's limitations
- Set expectations for interaction style

**Example**:
```markdown
## Role

You are a senior research writing assistant specializing in SCI paper drafts.
Your expertise covers:
- Academic writing conventions
- Paper structure and flow
- Technical terminology
- Citation practices

You are NOT:
- A general chatbot
- A fact-checker (users must verify claims)
- A plagiarism detector
```

**Why**: Clear roles help the agent understand its boundaries and produce more focused outputs.

---

## 2. Input Discipline

**Principle**: Each skill must have structured input templates.

**Requirements**:
- Define required inputs
- Define optional inputs
- Provide input format examples
- Specify what to do if input is missing

**Example**:
```markdown
## Inputs

### Required
1. **Research Topic** - The main research question
2. **Method Description** - How the method works
3. **Experiment Results** - Key findings

### Optional
1. **Target Venue** - Journal or conference name
2. **Reference Style** - Citation format
3. **Word Limit** - Maximum word count

### If Missing
- If topic is unclear: Ask for clarification
- If method is missing: Request method description
- If results are missing: Cannot proceed
```

**Why**: Structured inputs ensure the agent has enough information to produce quality outputs.

---

## 3. Workflow Decomposition

**Principle**: Each skill must break down the task into clear, executable steps.

**Requirements**:
- Number each step
- Specify what happens in each step
- Define dependencies between steps
- Include decision points

**Example**:
```markdown
## Workflow

### Step 1: Analyze Input
- Read all provided files
- Identify key information
- Flag missing data

### Step 2: Generate Outline
- Create section structure
- Assign content to sections
- Define flow and transitions

### Step 3: Write Draft
- Write each section
- Ensure consistency
- Add citations placeholders

### Step 4: Review & Refine
- Check quality checklist
- Fix issues found
- Generate final output
```

**Why**: Clear workflows make the skill predictable and reproducible.

---

## 4. Output Contract

**Principle**: Each skill must define a fixed output format.

**Requirements**:
- Specify output structure
- Define section names
- Set formatting rules
- Provide output examples

**Example**:
```markdown
## Output Format

### Paper Draft
1. **Title** - Concise and descriptive
2. **Abstract** - 150-250 words
3. **Introduction** - Problem, motivation, contributions
4. **Related Work** - Key references and positioning
5. **Method** - Technical details
6. **Experiments** - Setup, results, analysis
7. **Discussion** - Limitations and future work
8. **Conclusion** - Summary and impact

### Formatting
- Use academic language
- Include section headers
- Add placeholder citations [1], [2], etc.
- Mark areas needing user input with [TODO]
```

**Why**: Fixed output formats make skills reliable and easy to integrate into workflows.

---

## 5. Quality Gates

**Principle**: Each skill must include quality checklists.

**Requirements**:
- Define what "good" looks like
- Create specific, measurable criteria
- Include both positive and negative checks
- Make checklists actionable

**Example**:
```markdown
## Quality Checklist

### Content Quality
- [ ] Addresses the research question directly
- [ ] Uses specific, not vague language
- [ ] Includes concrete examples
- [ ] Avoids unsupported claims

### Structure Quality
- [ ] Follows logical flow
- [ ] Each section has clear purpose
- [ ] Transitions are smooth
- [ ] Conclusion ties back to introduction

### Technical Quality
- [ ] Method is clearly explained
- [ ] Experiments are reproducible
- [ ] Results are accurately reported
- [ ] Limitations are acknowledged

### Language Quality
- [ ] Grammar is correct
- [ ] Terminology is consistent
- [ ] Sentences are concise
- [ ] No plagiarism
```

**Why**: Quality gates ensure outputs meet professional standards.

---

## 6. No Hallucination

**Principle**: Skills must not generate fake or unverifiable content.

**Requirements**:
- Never fabricate citations
- Never invent experimental results
- Never create fake data
- Always mark uncertain content

**Example**:
```markdown
## Constraints

### Forbidden
- ❌ Fabricating paper citations
- ❌ Inventing experimental results
- ❌ Creating fake datasets
- ❌ Making unsupported claims

### Required
- ✅ Mark placeholders with [CITATION NEEDED]
- ✅ Use [TODO] for user-required input
- ✅ Clearly state assumptions
- ✅ Acknowledge limitations
```

**Why**: Hallucination destroys trust and can cause serious problems in academic work.

---

## 7. Artifact-Oriented Delivery

**Principle**: Skills should deliver files, not just text.

**Requirements**:
- Generate actual files
- Use proper file formats
- Include file organization
- Provide file descriptions

**Example**:
```markdown
## Deliverables

### Primary Output
- `paper-draft.md` - Complete paper draft
- `references.bib` - Bibliography file
- `figures/` - Figure placeholders

### Secondary Output
- `analysis-report.md` - Writing analysis
- `checklist-results.md` - Quality check results
- `next-steps.md` - Recommended actions

### File Organization
```
output/
├── paper-draft.md
├── references.bib
├── figures/
│   ├── figure1-placeholder.md
│   └── figure2-placeholder.md
├── analysis-report.md
└── next-steps.md
```
```

**Why**: Artifacts are tangible, versionable, and easier to review than plain text.

---

## Applying These Principles

### When Creating a New Skill

1. Start with Role Clarity - Who is this agent?
2. Define Inputs - What does it need?
3. Design Workflow - How does it work?
4. Specify Output - What does it produce?
5. Add Quality Gates - How to verify quality?
6. Set Constraints - What not to do?
7. Plan Deliverables - What files to generate?

### When Reviewing an Existing Skill

Check each principle:
- [ ] Is the role clear?
- [ ] Are inputs structured?
- [ ] Is the workflow explicit?
- [ ] Is the output format fixed?
- [ ] Are quality gates defined?
- [ ] Is hallucination prevented?
- [ ] Are artifacts delivered?

---

## Common Mistakes

### ❌ Vague Prompts
```
"Write a good paper about AI"
```

### ✅ Structured Skill
```
Role: Senior research writing assistant
Input: Topic, method, results, target venue
Workflow: Analyze → Outline → Draft → Review
Output: Complete paper with sections
Quality: Checklist with 20+ criteria
```

### ❌ Just Chat
```
User: Help me write a paper
Agent: Sure, what's your topic?
User: AI
Agent: Here's a paper about AI...
```

### ✅ Workflow Execution
```
1. Read input template
2. Validate required fields
3. Execute workflow steps
4. Generate output files
5. Run quality checks
6. Deliver artifacts
```

---

## Summary

Following these 7 principles ensures:

1. **Quality** - Outputs meet professional standards
2. **Consistency** - Same inputs produce similar outputs
3. **Reusability** - Skills work across projects
4. **Reliability** - Predictable behavior
5. **Trust** - No hallucination or fabrication
6. **Efficiency** - Clear workflows save time
7. **Extensibility** - Easy to add new skills

---

*Design principles for building production-ready agent skills.*