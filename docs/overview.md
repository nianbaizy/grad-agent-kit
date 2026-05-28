# GradAgentKit Overview

> What is GradAgentKit and why does it exist?

---

## What is GradAgentKit?

GradAgentKit is an open-source collection of reusable AI agent skills designed for graduate students, research developers, and AI-assisted programming users.

It provides **production-ready skills** that transform repetitive research tasks into structured, inspectable, and workflow-first AI agent workflows.

---

## The Problem

Current AI programming tools and large models have strong capabilities for research development, but most users still停留在"临时聊天式提问"阶段:

1. **Every task needs a new prompt** - No reusable task templates
2. **AI output quality is inconsistent** - No quality checklists or gates
3. **Research tasks are long and complex** - Papers, experiments, code, charts, presentations, and archives
4. **Tools lack standardization** - Claude Code, Codex, Cursor have execution capabilities but no structured skill organization
5. **Repetitive work** - Experiment log analysis, paper polishing, review simulation, PPT outline generation, README beautification

---

## The Solution

GradAgentKit transforms "research task experience" into "executable agent skill library", allowing users to call different research agents like calling tools.

### Core Principles

1. **Workflow-first, not Chat-first**
   - Each skill corresponds to a clear task workflow
   - Not scattered prompts

2. **Executable, not just advisory**
   - Each skill tells the agent what files to read, modify, and output
   - Not just suggestions

3. **Inspectable, not just intuitive**
   - Each skill includes quality checklists
   - Not just "looks good"

4. **Portable, not project-bound**
   - Users can copy directly to `.claude/skills`, `.codex/skills`, or their knowledge base
   - Not tied to specific projects

5. **Extensible, not one-time scripts**
   - Can be extended to CLI, web, mini-programs, Obsidian plugins, or GitHub Actions
   - Not disposable

---

## Target Users

### Primary Users

1. Graduate students
2. Research paper authors
3. AI-assisted programming users
4. Developers using Claude Code / Codex / Cursor
5. People who need academic presentations, experiment analysis, project archives

### Typical Scenarios

1. Write SCI paper draft
2. Polish paper paragraphs
3. Analyze experiment results
4. Check if experiment design is sufficient
5. Simulate reviewer questions
6. Generate rebuttal response ideas
7. Generate academic presentation outline
8. Generate HTML / Slidev presentations
9. Initialize GitHub project documentation
10. Archive experiment logs and results

---

## Skills Overview

| Skill | Purpose | Input | Output |
|-------|---------|-------|--------|
| paper-writer | Generate paper drafts | Topic, method, results | Full paper sections |
| experiment-analyzer | Analyze experiment results | CSV, logs, config | Analysis paragraphs |
| reviewer-simulator | Simulate peer review | Paper draft | Review report |
| advisor-roaster | Simulate advisor questioning | Research idea | Question list |
| academic-deck-builder | Build presentations | Material, audience | Slide structure |

---

## How It Works

### 1. Choose a Skill

Select the appropriate skill based on your task.

### 2. Prepare Input

Fill in the input template with your specific information.

### 3. Execute Workflow

The agent follows the skill's workflow step by step.

### 4. Review Output

Check the output against the quality checklist.

### 5. Iterate if Needed

Refine based on feedback and re-run if necessary.

---

## Integration

GradAgentKit works with:

- **Claude Code** - Copy to `.claude/skills/`
- **Codex** - Copy to `.codex/skills/`
- **Cursor** - Copy to `.cursor/skills/`
- **Obsidian** - Use as knowledge base templates
- **Any AI agent** - Follow the skill structure

---

## Benefits

### For Individual Users

- ✅ Save time on repetitive tasks
- ✅ Get consistent, high-quality outputs
- ✅ Learn structured research workflows
- ✅ Build personal skill library

### For Teams

- ✅ Standardize research processes
- ✅ Share best practices
- ✅ Onboard new members faster
- ✅ Maintain quality across projects

### For the Community

- ✅ Open-source and extensible
- ✅ Community-driven improvements
- ✅ Cross-platform compatibility
- ✅ Growing skill library

---

## Getting Started

See [installation.md](installation.md) for setup instructions.

See [usage.md](usage.md) for detailed usage examples.

---

*GradAgentKit - Making research workflows reusable.*