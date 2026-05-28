# Installation Guide

> How to install and use GradAgentKit with Claude Code, Codex, and Cursor.

---

## Quick Install

### Option 1: Clone Repository

```bash
# Clone the repository
git clone https://github.com/your-username/grad-agent-kit.git

# Navigate to the directory
cd grad-agent-kit

# Copy skills to your project
cp -r skills/* /path/to/your-project/.claude/skills/
```

### Option 2: Download Skills Only

```bash
# Create skills directory
mkdir -p /path/to/your-project/.claude/skills/

# Download individual skills
curl -L https://github.com/your-username/grad-agent-kit/raw/main/skills/paper-writer.zip -o paper-writer.zip
unzip paper-writer.zip -d /path/to/your-project/.claude/skills/
```

---

## Platform-Specific Installation

### Claude Code

Claude Code automatically discovers skills in `.claude/skills/` directory.

```bash
# 1. Navigate to your project
cd /path/to/your-project

# 2. Create skills directory (if not exists)
mkdir -p .claude/skills

# 3. Copy skills
cp -r /path/to/grad-agent-kit/skills/* .claude/skills/

# 4. Verify installation
ls .claude/skills/
# Should show: paper-writer/ experiment-analyzer/ reviewer-simulator/ advisor-roaster/ academic-deck-builder/
```

**Usage in Claude Code**:
```
# Claude Code will automatically detect available skills
# Use them in your prompts:

Use the paper-writer skill to generate a draft for my quantization paper.
```

---

### Codex

Codex uses a similar skills directory structure.

```bash
# 1. Navigate to your project
cd /path/to/your-project

# 2. Create skills directory
mkdir -p .codex/skills

# 3. Copy skills
cp -r /path/to/grad-agent-kit/skills/* .codex/skills/

# 4. Verify installation
ls .codex/skills/
```

**Usage in Codex**:
```
# Codex will discover skills in .codex/skills/
# Reference them in your prompts:

Using the experiment-analyzer skill, analyze my training results.
```

---

### Cursor

Cursor can use skills from `.cursor/skills/` or integrate with `.cursorrules`.

```bash
# 1. Navigate to your project
cd /path/to/your-project

# 2. Create skills directory
mkdir -p .cursor/skills

# 3. Copy skills
cp -r /path/to/grad-agent-kit/skills/* .cursor/skills/

# 4. Verify installation
ls .cursor/skills/
```

**Alternative: Add to .cursorrules**:

```bash
# Add skill references to .cursorrules
cat >> .cursorrules << 'EOF'

## Available Skills

- paper-writer: Generate paper drafts
- experiment-analyzer: Analyze experiment results
- reviewer-simulator: Simulate peer review
- advisor-roaster: Simulate advisor questioning
- academic-deck-builder: Build presentations

Use these skills when appropriate tasks arise.
EOF
```

---

### Obsidian

For Obsidian users, skills can be stored in your vault.

```bash
# 1. Navigate to your Obsidian vault
cd /path/to/your-vault

# 2. Create skills directory
mkdir -p .claude/skills

# 3. Copy skills
cp -r /path/to/grad-agent-kit/skills/* .claude/skills/

# 4. Use in Obsidian with Claude Code plugin
```

---

## Verification

After installation, verify that skills are correctly installed:

```bash
# Check directory structure
ls -la .claude/skills/

# Expected output:
# paper-writer/
# experiment-analyzer/
# reviewer-simulator/
# advisor-roaster/
# academic-deck-builder/

# Check skill files
ls .claude/skills/paper-writer/

# Expected output:
# SKILL.md
# input-template.md
# output-format.md
# checklist.md
# examples/
```

---

## Updating Skills

### Pull Latest Changes

```bash
# Navigate to grad-agent-kit directory
cd /path/to/grad-agent-kit

# Pull latest changes
git pull origin main

# Copy updated skills
cp -r skills/* /path/to/your-project/.claude/skills/
```

### Manual Update

```bash
# Download latest version
curl -L https://github.com/your-username/grad-agent-kit/archive/main.zip -o grad-agent-kit.zip

# Extract
unzip grad-agent-kit.zip

# Copy skills
cp -r grad-agent-kit-main/skills/* /path/to/your-project/.claude/skills/

# Clean up
rm grad-agent-kit.zip
rm -rf grad-agent-kit-main
```

---

## Customization

### Adding Custom Skills

```bash
# Create new skill directory
mkdir -p .claude/skills/my-custom-skill

# Create skill files
cat > .claude/skills/my-custom-skill/SKILL.md << 'EOF'
# My Custom Skill

## Role
You are a specialized agent for...

## When to Use
Use this skill when...

## Inputs
1. Input 1
2. Input 2

## Workflow
1. Step 1
2. Step 2

## Output
Expected output format...

## Constraints
- Don't do X
- Always do Y
EOF
```

### Modifying Existing Skills

```bash
# Edit skill file
nano .claude/skills/paper-writer/SKILL.md

# Add custom constraints
# Add custom workflow steps
# Modify output format
```

---

## Troubleshooting

### Skills Not Detected

**Problem**: Claude Code doesn't recognize skills.

**Solution**:
```bash
# 1. Check directory location
ls -la .claude/skills/

# 2. Verify file structure
ls .claude/skills/paper-writer/

# 3. Restart Claude Code
# Skills are loaded on startup
```

### Permission Issues

**Problem**: Cannot copy skills.

**Solution**:
```bash
# Check permissions
ls -la .claude/

# Fix permissions if needed
chmod -R 755 .claude/skills/
```

### Skill Not Working

**Problem**: Skill produces unexpected output.

**Solution**:
```bash
# 1. Check SKILL.md for role definition
cat .claude/skills/paper-writer/SKILL.md

# 2. Verify input template
cat .claude/skills/paper-writer/input-template.md

# 3. Review quality checklist
cat .claude/skills/paper-writer/checklist.md

# 4. Provide complete input
# Fill all required fields in input template
```

---

## Advanced Setup

### Multiple Projects

```bash
# Install skills globally
mkdir -p ~/.claude/skills
cp -r /path/to/grad-agent-kit/skills/* ~/.claude/skills/

# Or per-project
cd /path/to/project-a
mkdir -p .claude/skills
cp -r /path/to/grad-agent-kit/skills/* .claude/skills/

cd /path/to/project-b
mkdir -p .claude/skills
cp -r /path/to/grad-agent-kit/skills/* .claude/skills/
```

### Team Setup

```bash
# Add skills to version control
cd /path/to/your-project
git add .claude/skills/
git commit -m "Add GradAgentKit skills"

# Team members can now use them
git pull
# Skills are automatically available
```

---

## Next Steps

After installation:

1. **Read the Usage Guide** - See [usage.md](usage.md)
2. **Try Examples** - See [examples/](../examples/)
3. **Create Custom Skills** - See [skill-design-principles.md](skill-design-principles.md)
4. **Join Community** - See [CONTRIBUTING.md](../CONTRIBUTING.md)

---

*Installation guide for GradAgentKit.*