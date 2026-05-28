# Contributing to GradAgentKit

Thank you for your interest in contributing to GradAgentKit! This guide will help you get started.

---

## How to Contribute

### 1. Adding a New Skill

The most valuable contribution is adding new skills for research tasks.

#### Step-by-Step Guide

1. **Choose a skill name**
   - Use kebab-case: `my-new-skill`
   - Be descriptive: `paper-polisher`, not `writing-helper`

2. **Create skill directory**
   ```bash
   mkdir -p skills/my-new-skill/examples
   ```

3. **Create required files**
   - `SKILL.md` - Skill definition
   - `input-template.md` - Input format
   - `output-format.md` - Output format
   - `checklist.md` - Quality checklist

4. **Follow the template**
   - Use `templates/skill-template/` as reference
   - Include all sections from the template
   - Add specific content for your skill

5. **Add examples**
   - Create `examples/` directory
   - Include at least one example
   - Show input → output transformation

6. **Test your skill**
   ```bash
   python scripts/validate-skills.py
   ```

7. **Submit pull request**
   - Fork the repository
   - Create feature branch
   - Submit PR with description

---

### 2. Improving Existing Skills

#### What to Improve

- **Quality gates** - Add more checks
- **Examples** - Add more use cases
- **Documentation** - Clarify instructions
- **Edge cases** - Handle special scenarios

#### How to Submit

1. Open an issue describing the improvement
2. Fork and create branch
3. Make changes
4. Submit PR linking to issue

---

### 3. Adding Examples

Examples help users understand how to use skills.

#### Example Structure

```
examples/my-example/
├── README.md           # What this example demonstrates
├── input-files.md      # Example input
├── expected-output.md  # Expected result
└── usage-instructions.md # How to use
```

#### Example Guidelines

- Use realistic scenarios
- Include complete inputs
- Show expected outputs
- Explain the use case

---

### 4. Improving Documentation

#### Documentation Tasks

- Fix typos and grammar
- Add usage examples
- Clarify confusing sections
- Translate to other languages
- Add diagrams and figures

---

### 5. Reporting Issues

#### Bug Reports

Include:
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details

#### Feature Requests

Include:
- Use case description
- Proposed solution
- Alternatives considered

---

## Skill Design Guidelines

### 1. Role Clarity

```markdown
## Role
You are a [specific type] agent specializing in [domain].

### Expertise
- [Area 1]
- [Area 2]

### Limitations
- You do NOT [limitation]
```

### 2. Input Discipline

```markdown
## Inputs
### Required
1. **[Input]** - [Description]

### Optional
1. **[Optional]** - [Description]
```

### 3. Workflow Decomposition

```markdown
## Workflow
### Step 1: [Name]
- [Action]
- [Action]
```

### 4. Output Contract

```markdown
## Output
### Primary Output
- `[file.md]` - [Description]
```

### 5. Quality Gates

```markdown
## Quality Checklist
- [ ] [Check 1]
- [ ] [Check 2]
```

---

## Code Style

### Markdown

- Use ATX headers (`#`, `##`, `###`)
- Use `-` for bullet points
- Use `1.` for numbered lists
- Use code blocks for examples
- Keep lines under 100 characters

### File Naming

- Use kebab-case: `my-file.md`
- Be descriptive: `input-template.md`
- Use `.md` extension for all docs

---

## Pull Request Process

### Before Submitting

1. **Test locally**
   ```bash
   python scripts/validate-skills.py
   ```

2. **Check formatting**
   - Consistent style
   - No typos
   - Clear structure

3. **Update documentation**
   - Add to CHANGELOG.md
   - Update README if needed

### PR Template

```markdown
## Description
[What this PR does]

## Changes
- [Change 1]
- [Change 2]

## Testing
- [How you tested]

## Related Issues
- Closes #[issue]
```

---

## Community Guidelines

### Be Respectful

- Welcome newcomers
- Be constructive
- Focus on the work, not the person

### Be Helpful

- Answer questions
- Review PRs
- Share knowledge

### Be Patient

- Reviews take time
- Iteration is normal
- Quality over speed

---

## Recognition

Contributors will be:
- Listed in README.md
- Mentioned in CHANGELOG.md
- Credited in skill documentation

---

## Questions?

- Open an issue for questions
- Join discussions
- Read existing issues first

---

Thank you for contributing to GradAgentKit! 🎓

---

*Contributing Guide - GradAgentKit*