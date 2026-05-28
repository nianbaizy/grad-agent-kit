# GradAgentKit

> Reusable AI agent skills for research writing, experiment analysis, academic presentation, reviewer simulation, and project delivery.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Skills](https://img.shields.io/badge/Skills-5-blue)](skills/)
[![Version](https://img.shields.io/badge/Version-1.0.0-green)](CHANGELOG.md)

---

## What is GradAgentKit?

GradAgentKit helps graduate students and research developers transform repetitive research tasks into reusable, inspectable, and workflow-first AI agent skills.

Instead of writing prompts from scratch every time, you get **production-ready skills** that:

- ✅ Follow structured workflows (not just chat)
- ✅ Have clear input/output contracts
- ✅ Include quality checklists
- ✅ Work with Claude Code, Codex, and Cursor
- ✅ Can be copied directly to your `.claude/skills` folder

---

## Why GradAgentKit?

| Problem | Solution |
|---------|----------|
| Every task needs a new prompt | Reusable skill templates |
| AI output quality is inconsistent | Built-in quality gates |
| Research tasks are long and complex | Workflow-first decomposition |
| Hard to track and review AI work | Artifact-oriented delivery |
| Same tasks repeated across projects | Portable skill library |

---

## Skills

| Skill | Purpose | Use When |
|-------|---------|----------|
| [paper-writer](skills/paper-writer/) | Generate paper drafts | Starting a new paper |
| [experiment-analyzer](skills/experiment-analyzer/) | Analyze experiment results | After running experiments |
| [reviewer-simulator](skills/reviewer-simulator/) | Simulate peer review | Before submission |
| [advisor-roaster](skills/advisor-roaster/) | Simulate advisor questioning | Pre-defense preparation |
| [academic-deck-builder](skills/academic-deck-builder/) | Build presentation decks | Conference talks |

---

## Quick Start

### For Claude Code

```bash
# Clone the repository
git clone https://github.com/your-username/grad-agent-kit.git

# Copy skills to your project
cp -r grad-agent-kit/skills/* your-project/.claude/skills/

# Use a skill
# In Claude Code, the skill will be automatically discovered
```

### For Codex

```bash
# Copy skills to Codex skills directory
cp -r grad-agent-kit/skills/* ~/.codex/skills/
```

### For Cursor

```bash
# Copy skills to your project's .cursorrules or skills folder
cp -r grad-agent-kit/skills/* your-project/.cursor/skills/
```

---

## Usage Examples

### 1. Write a Paper Draft

```markdown
# In your Claude Code session:

Use the paper-writer skill to generate a draft for my quantization paper.

Topic: Low-bit quantization for time-series Transformer models
Method: Dynamic bit-width allocation based on temporal attention
Results: 2.3% improvement on ETTh1 dataset
Target: NeurIPS 2026
```

### 2. Analyze Experiment Results

```markdown
Use the experiment-analyzer skill to analyze my training results.

Files to read:
- results.csv
- train.log
- config.yaml

Baseline: PatchTST
My method: Improved by 1.5% MSE
```

### 3. Simulate Peer Review

```markdown
Use the reviewer-simulator skill to review my paper draft.

Target venue: ICML 2026
Focus: Check if experiments are sufficient
```

---

## Recommended Workflow

```
1. paper-writer      → Generate initial draft
2. experiment-analyzer → Analyze your results
3. reviewer-simulator  → Get pre-submission review
4. advisor-roaster    → Prepare for advisor questions
5. academic-deck-builder → Build presentation
```

---

## Project Structure

```
grad-agent-kit/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── CHANGELOG.md                       # Version history
├── CONTRIBUTING.md                    # How to contribute
├── docs/                              # Documentation
│   ├── overview.md                    # Project overview
│   ├── skill-design-principles.md     # Design principles
│   ├── workflow-first-agent.md        # Why workflow-first
│   ├── installation.md                # Installation guide
│   ├── usage.md                       # Usage examples
│   └── roadmap.md                     # Future plans
├── skills/                            # Agent skills
│   ├── paper-writer/
│   ├── experiment-analyzer/
│   ├── reviewer-simulator/
│   ├── advisor-roaster/
│   └── academic-deck-builder/
├── examples/                          # Usage examples
│   ├── quantization-paper/
│   ├── time-series-experiment/
│   └── academic-presentation/
├── templates/                         # Skill templates
│   ├── skill-template/
│   └── workflow-template.md
└── scripts/                           # Utility scripts
    ├── validate-skills.py
    └── generate-skill-index.py
```

---

## Skill Design Principles

Each skill in GradAgentKit follows these principles:

1. **Role Clarity** - Clear agent identity and expertise
2. **Input Discipline** - Structured input templates
3. **Workflow Decomposition** - Step-by-step execution
4. **Output Contract** - Fixed output format
5. **Quality Gates** - Built-in checklists
6. **No Hallucination** - Fact-based outputs only
7. **Artifact-Oriented** - Deliver files, not just text

---

## Roadmap

### v1.0 (Current)
- ✅ 5 core research skills
- ✅ Usage examples
- ✅ Validation scripts
- ✅ Documentation

### v1.1 (Planned)
- [ ] paper-polisher skill
- [ ] rebuttal-writer skill
- [ ] github-readme-crafter skill
- [ ] experiment-archiver skill

### v2.0 (Future)
- [ ] CLI tool (`gradagent`)
- [ ] GitHub Action integration
- [ ] Obsidian plugin
- [ ] Web gallery

---

## Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### Adding a New Skill

1. Create a new folder in `skills/`
2. Add the 4 required files:
   - `SKILL.md` - Skill definition
   - `input-template.md` - Input format
   - `output-format.md` - Output format
   - `checklist.md` - Quality checklist
3. Add an example in `examples/`
4. Run validation: `python scripts/validate-skills.py`

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

## Acknowledgments

Built for graduate students and research developers who want to make AI agents work like a team, not just a chatbot.

---

*GradAgentKit - Making research workflows reusable.*