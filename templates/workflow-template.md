# Workflow Template

> Template for creating new GradAgentKit skills.

---

## Step 1: Define the Skill

### 1.1 Skill Name
Choose a descriptive, kebab-case name:
- ✅ `paper-writer`
- ✅ `experiment-analyzer`
- ❌ `writing-helper`
- ❌ `analysis-tool`

### 1.2 Skill Purpose
Write a clear one-sentence description:
```
[Skill name] helps users [accomplish what] by [how].
```

Example:
```
paper-writer helps users generate research paper drafts by following academic writing conventions.
```

### 1.3 Target Users
Who will use this skill?
- Graduate students
- Research developers
- AI-assisted programmers
- Academic writers

---

## Step 2: Define the Role

### 2.1 Agent Identity
```
You are a [specific type] agent specializing in [domain].
```

### 2.2 Expertise Areas
List 3-5 areas of expertise:
- [Expertise 1]
- [Expertise 2]
- [Expertise 3]

### 2.3 Limitations
List what the agent cannot do:
- Cannot [limitation 1]
- Cannot [limitation 2]
- Cannot [limitation 3]

---

## Step 3: Define Inputs

### 3.1 Required Inputs
What information must be provided?
1. **[Input 1]** - [Description]
2. **[Input 2]** - [Description]
3. **[Input 3]** - [Description]

### 3.2 Optional Inputs
What information can be provided?
1. **[Optional 1]** - [Description]
2. **[Optional 2]** - [Description]

### 3.3 Input Validation
How to handle missing or invalid inputs:
- If [Input 1] missing: [Action]
- If [Input 2] invalid: [Action]

---

## Step 4: Design the Workflow

### 4.1 Workflow Steps
Break down the task into clear steps:

```
Step 1: [Step Name]
- [Action 1]
- [Action 2]

Step 2: [Step Name]
- [Action 1]
- [Action 2]

Step 3: [Step Name]
- [Action 1]
- [Action 2]

Step 4: Quality Check
- Run checklist
- Verify output
```

### 4.2 Decision Points
Where should the agent make decisions?
- If [condition]: [action]
- If [condition]: [action]

### 4.3 Dependencies
What depends on what?
- Step 2 depends on Step 1
- Step 3 depends on Step 2

---

## Step 5: Define Outputs

### 5.1 Primary Outputs
What files should be generated?
1. `[filename1.md]` - [Description]
2. `[filename2.md]` - [Description]

### 5.2 Secondary Outputs
What additional files?
1. `[filename3.md]` - [Description]
2. `[filename4.md]` - [Description]

### 5.3 Output Format
How should outputs be structured?
```
output/
├── [filename1.md]
├── [filename2.md]
├── [filename3.md]
└── [filename4.md]
```

---

## Step 6: Define Constraints

### 6.1 Forbidden Actions
What must the agent NOT do?
- ❌ [Forbidden 1]
- ❌ [Forbidden 2]
- ❌ [Forbidden 3]

### 6.2 Required Actions
What must the agent ALWAYS do?
- ✅ [Required 1]
- ✅ [Required 2]
- ✅ [Required 3]

---

## Step 7: Create Quality Checklist

### 7.1 Content Quality
- [ ] [Check 1]
- [ ] [Check 2]
- [ ] [Check 3]

### 7.2 Structure Quality
- [ ] [Check 4]
- [ ] [Check 5]
- [ ] [Check 6]

### 7.3 Language Quality
- [ ] [Check 7]
- [ ] [Check 8]
- [ ] [Check 9]

---

## Step 8: Create Examples

### 8.1 Example 1
**Input**:
```
[Input content]
```

**Output**:
```
[Output content]
```

### 8.2 Example 2
**Input**:
```
[Input content]
```

**Output**:
```
[Output content]
```

---

## Step 9: Documentation

### 9.1 SKILL.md
- Role definition
- When to use
- Inputs
- Workflow
- Output
- Constraints
- Quality gates
- Examples

### 9.2 input-template.md
- Task description
- Background
- Files to read
- Required output
- Constraints
- Additional notes

### 9.3 output-format.md
- Primary deliverables
- Secondary deliverables
- File organization
- Formatting rules
- Quality indicators

### 9.4 checklist.md
- Pre-execution checks
- Execution checks
- Output checks
- Content quality
- Technical quality
- Documentation quality

---

## Step 10: Testing

### 10.1 Test Cases
Create test cases for:
- Normal operation
- Edge cases
- Error conditions

### 10.2 Validation
Run validation:
```bash
python scripts/validate-skills.py
```

### 10.3 Review
Have others review:
- Skill clarity
- Workflow logic
- Output quality

---

## Checklist

Before releasing a new skill:

- [ ] Skill name is descriptive
- [ ] Role is clearly defined
- [ ] Inputs are structured
- [ ] Workflow is explicit
- [ ] Output format is fixed
- [ ] Quality gates are defined
- [ ] Constraints are clear
- [ ] Examples are provided
- [ ] Documentation is complete
- [ ] Validation passes

---

*Workflow template for creating new GradAgentKit skills*