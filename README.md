# GradAgentKit

> Reusable AI agent skills for research writing, experiment analysis, academic presentation, reviewer simulation, and project delivery.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Skills-5-green)](skills/)
[![Version](https://img.shields.io/badge/Version-0.1.0-orange)](CHANGELOG.md)
[![Platform](https://img.shields.io/badge/Platform-Claude%20%7C%20Codex%20%7C%20Cursor-lightgrey)](#installation)

---

## What is GradAgentKit?

GradAgentKit is an open-source collection of **workflow-first AI agent skills** designed for graduate students, researchers, and developers who use AI-assisted tools for academic work.

Instead of writing prompts from scratch every time, GradAgentKit provides **production-ready skills** that follow structured workflows with clear inputs, outputs, and quality checks.

```
Traditional Prompt          GradAgentKit Skill
─────────────────          ──────────────────
"Help me write a paper"    → Structured workflow with templates
Output varies each time    → Consistent, inspectable output
No quality checks          → Built-in quality gates
Hard to reproduce          → Reusable across projects
```

---

## Who is it for?

- **Graduate students** writing papers, preparing defenses, or analyzing experiments
- **Researchers** who want consistent AI-assisted workflows
- **Developers** using Claude Code, Codex, or Cursor for academic tasks
- **Anyone** who needs structured, reusable AI agent skills

---

## Why GradAgentKit?

| Problem | GradAgentKit Solution |
|---------|----------------------|
| Every task needs a new prompt | Reusable skill templates |
| AI output quality is inconsistent | Built-in quality checklists |
| Research tasks are long and complex | Workflow-first decomposition |
| Hard to track and review AI work | Artifact-oriented delivery |
| Same tasks repeated across projects | Portable skill library |

---

## Core Principles

1. **Workflow-first, not Chat-first** — Each skill defines a clear execution workflow
2. **Executable, not just advisory** — Skills tell agents what files to read, modify, and output
3. **Inspectable, not just intuitive** — Every skill includes quality checklists
4. **Portable, not project-bound** — Copy skills to `.claude/skills`, `.codex/skills`, or any agent workspace
5. **Artifact-oriented** — Deliver files and structured outputs, not just text

---

## Available Skills

| Skill | Purpose | Best For | Path |
|-------|---------|----------|------|
| **paper-writer** | Generate research paper drafts | Starting a new paper from topic, method, and results | [skills/paper-writer](skills/paper-writer/) |
| **experiment-analyzer** | Analyze experiment results and logs | Post-experiment analysis, result interpretation | [skills/experiment-analyzer](skills/experiment-analyzer/) |
| **reviewer-simulator** | Simulate peer review for papers | Pre-submission review, identifying weaknesses | [skills/reviewer-simulator](skills/reviewer-simulator/) |
| **advisor-roaster** | Simulate strict advisor questioning | Defense preparation, anticipating tough questions | [skills/advisor-roaster](skills/advisor-roaster/) |
| **academic-deck-builder** | Build presentation structures | Conference talks, seminar presentations | [skills/academic-deck-builder](skills/academic-deck-builder/) |

Each skill includes 4 standard files:
- `SKILL.md` — Role, workflow, constraints, quality gates
- `input-template.md` — Structured input format
- `output-format.md` — Expected output structure
- `checklist.md` — Quality verification checklist

See [docs/skill-index.md](docs/skill-index.md) for the auto-generated skill index.

---

## Quick Start

### For Claude Code

```bash
# Clone the repository
git clone https://github.com/nianbaizy/grad-agent-kit.git

# Copy all skills to your project
cp -r grad-agent-kit/skills/* your-project/.claude/skills/

# Or copy a specific skill
cp -r grad-agent-kit/skills/paper-writer your-project/.claude/skills/
```

Then use in your Claude Code session:

```markdown
Use the paper-writer skill to generate a draft.

## Topic
Dynamic quantization for time-series Transformer models

## Method
Attention-based bit-width allocation

## Results
2.3% MSE improvement on ETTh1

## Target Venue
NeurIPS 2026
```

### For Codex

```bash
cp -r grad-agent-kit/skills/* your-project/.codex/skills/
```

### For Cursor

```bash
cp -r grad-agent-kit/skills/* your-project/.cursor/skills/
```

---

## Skill Structure

Every skill follows the same structure:

```
skills/
└── skill-name/
    ├── SKILL.md              # Skill definition (role, workflow, constraints)
    ├── input-template.md     # What to provide when using the skill
    ├── output-format.md      # What the skill produces
    ├── checklist.md          # Quality verification checklist
    └── examples/             # Usage examples (optional)
```

This structure ensures:
- **Consistency** — Every skill works the same way
- **Portability** — Copy to any agent platform
- **Quality** — Built-in verification
- **Extensibility** — Easy to add new skills

---

## Usage Examples

### Write a Paper Draft

```markdown
Use the paper-writer skill.

## Topic
Low-bit quantization for time-series Transformer models

## Method
Dynamic bit-width allocation using attention weights

## Results
- ETTh1: 2.3% MSE improvement
- Model size: 30% reduction

## Target Venue
NeurIPS 2026
```

### Analyze Experiment Results

```markdown
Use the experiment-analyzer skill.

## Files to Read
- results.csv
- train.log
- config.yaml

## Baseline
PatchTST

## Focus
- Performance comparison
- Ablation study analysis
- Statistical significance
```

### Simulate Peer Review

```markdown
Use the reviewer-simulator skill.

## Paper File
paper-draft.md

## Target Venue
ICML 2026

## Review Focus
- Novelty
- Experimental validation
- Writing quality
```

### Prepare for Advisor Meeting

```markdown
Use the advisor-roaster skill.

## Research Idea
Dynamic quantization for time-series models

## Current Results
2.3% improvement on ETTh1

## Perceived Innovation
First dynamic quantization for time-series
```

### Build Presentation

```markdown
Use the academic-deck-builder skill.

## Topic
Dynamic quantization for time-series Transformers

## Audience
ML researchers at NeurIPS

## Duration
15 minutes + 5 Q&A

## Source Material
paper-draft.md
```

---

## Repository Structure

```
grad-agent-kit/
├── README.md                              # This file
├── LICENSE                                # MIT License
├── CHANGELOG.md                           # Version history
├── CONTRIBUTING.md                        # How to contribute
├── docs/                                  # Documentation
│   ├── overview.md                        # Project overview
│   ├── skill-design-principles.md         # How to design skills
│   ├── workflow-first-agent.md            # Why workflow-first
│   ├── installation.md                    # Installation guide
│   ├── usage.md                           # Usage examples
│   ├── skill-index.md                     # Auto-generated skill index
│   └── roadmap.md                         # Future plans
├── skills/                                # Agent skills
│   ├── paper-writer/
│   ├── experiment-analyzer/
│   ├── reviewer-simulator/
│   ├── advisor-roaster/
│   └── academic-deck-builder/
├── examples/                              # Usage examples
│   ├── quantization-paper/
│   ├── time-series-experiment/
│   └── academic-presentation/
├── templates/                             # Skill templates
│   ├── skill-template/
│   └── workflow-template.md
└── scripts/                               # Utility scripts
    ├── validate-skills.py                 # Validate skill structure
    └── generate-skill-index.py            # Generate skill index
```

---

## Examples

The `examples/` directory contains complete workflow demonstrations:

| Example | Demonstrates | Skills Used |
|---------|-------------|-------------|
| [quantization-paper](examples/quantization-paper/) | Full paper writing workflow | paper-writer, reviewer-simulator, advisor-roaster |
| [time-series-experiment](examples/time-series-experiment/) | Experiment analysis workflow | experiment-analyzer |
| [academic-presentation](examples/academic-presentation/) | Presentation building workflow | academic-deck-builder |

Each example includes input files, expected outputs, and usage instructions.

---

## Validation

Run the validation script to check skill structure:

```bash
python scripts/validate-skills.py
```

Expected output:

```
[VALIDATE] Validating GradAgentKit skills...

[PASS] academic-deck-builder passed
[PASS] advisor-roaster passed
[PASS] experiment-analyzer passed
[PASS] paper-writer passed
[PASS] reviewer-simulator passed

[SUMMARY]
   [PASS] Passed: 5
   [FAIL] Failed: 0

[SUCCESS] All skills passed validation!
```

Generate the skill index:

```bash
python scripts/generate-skill-index.py
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [overview.md](docs/overview.md) | What is GradAgentKit and why it exists |
| [skill-design-principles.md](docs/skill-design-principles.md) | How to design high-quality skills |
| [workflow-first-agent.md](docs/workflow-first-agent.md) | Why workflow-first, not chat-first |
| [installation.md](docs/installation.md) | Installation guide for different platforms |
| [usage.md](docs/usage.md) | Detailed usage examples |
| [skill-index.md](docs/skill-index.md) | Auto-generated skill index |
| [roadmap.md](docs/roadmap.md) | Future development plans |

---

## Roadmap

### v0.1.0 (Current)
- ✅ 5 core research agent skills
- ✅ Example workflows
- ✅ Skill validation scripts
- ✅ Documentation

### v0.2.0 (Planned)
- [ ] paper-polisher skill
- [ ] rebuttal-writer skill
- [ ] github-readme-crafter skill
- [ ] experiment-archiver skill

### v1.0.0 (Future)
- [ ] CLI tool for skill management
- [ ] GitHub Action integration
- [ ] Obsidian plugin

See [docs/roadmap.md](docs/roadmap.md) for details.

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### How to Add a New Skill

1. Create a new folder in `skills/`
2. Add the 4 required files (see [templates/skill-template](templates/skill-template/))
3. Add an example in `examples/`
4. Run validation: `python scripts/validate-skills.py`
5. Submit a pull request

---

## Installation

See [docs/installation.md](docs/installation.md) for detailed installation instructions.

### Quick Install

```bash
git clone https://github.com/nianbaizy/grad-agent-kit.git
cp -r grad-agent-kit/skills/* your-project/.claude/skills/
```

---

## License

MIT License — see [LICENSE](LICENSE) for details.

---

## Acknowledgments

Built for graduate students and research developers who want to make AI agents work like a structured team, not just a chatbot.

---

*GradAgentKit — Making research workflows reusable.*