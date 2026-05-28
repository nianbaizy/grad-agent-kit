# Academic Deck Builder - Output Format

> Expected output structure for academic-deck-builder skill.

---

## Primary Deliverables

### 1. presentation-outline.md

**Purpose**: High-level presentation structure

**Structure**:
```markdown
# Presentation Outline

## Title
[Working title for the talk]

## Duration
[Total time] minutes ([Talk time] + [Q&A time])

## Audience
[Description of audience]

## Key Messages
1. [Message 1]
2. [Message 2]
3. [Message 3]

## Narrative Arc
```
Opening → Problem → Solution → Evidence → Impact → Close
```

## Section Breakdown

### 1. Opening (0:00 - 0:30)
**Purpose**: Hook audience
**Content**: [What to cover]
**Time**: 30 seconds

### 2. Motivation (0:30 - 2:30)
**Purpose**: Why this matters
**Content**: [What to cover]
**Time**: 2 minutes

### 3. Method (2:30 - 7:00)
**Purpose**: How it works
**Content**: [What to cover]
**Time**: 4.5 minutes

### 4. Results (7:00 - 12:00)
**Purpose**: What we found
**Content**: [What to cover]
**Time**: 5 minutes

### 5. Conclusion (12:00 - 14:00)
**Purpose**: Key takeaways
**Content**: [What to cover]
**Time**: 2 minutes

### 6. Q&A (14:00 - 15:00)
**Purpose**: Answer questions
**Time**: 5 minutes

## Visual Strategy
- Slides: [Number] slides
- Pace: [Slides per minute]
- Style: [Minimal / Balanced / Detailed]
```

---

### 2. slide-content.md

**Purpose**: Detailed content for each slide

**Structure**:
```markdown
# Slide Content

## Slide 1: Title Slide
**Layout**: Title + Subtitle + Author
**Content**:
- Title: [Paper title]
- Subtitle: [Conference name]
- Author: [Your name]
- Affiliation: [Your institution]
- Date: [Date]

**Speaker Notes**:
[What to say - 15 seconds]

---

## Slide 2: Motivation
**Layout**: Problem statement
**Content**:
- Headline: [One sentence]
- Bullet points:
  - [Point 1]
  - [Point 2]
  - [Point 3]
- Figure: [Optional visualization]

**Speaker Notes**:
[What to say - 1 minute]

---

## Slide 3: Method Overview
**Layout**: Architecture diagram
**Content**:
- Headline: [Method name]
- Figure: [Architecture diagram]
- Key components labeled

**Speaker Notes**:
[What to say - 1.5 minutes]

---

[Continue for all slides...]

## Slide N: Thank You
**Layout**: Contact info
**Content**:
- "Questions?"
- Email: [Your email]
- GitHub: [Your GitHub]
- Paper: [Link]

**Speaker Notes**:
[What to say - 15 seconds]
```

---

### 3. speaker-notes.md

**Purpose**: Detailed talking points

**Structure**:
```markdown
# Speaker Notes

## Opening (Slide 1)
**Time**: 0:00 - 0:30 (30 seconds)
**Goal**: Hook the audience
**Key Points**:
- [Point 1]
- [Point 2]
**Transition**: "Let me tell you why this matters..."

## Motivation (Slides 2-3)
**Time**: 0:30 - 2:30 (2 minutes)
**Goal**: Establish the problem
**Key Points**:
- [Point 1]
- [Point 2]
- [Point 3]
**Transition**: "So how do we solve this?"

## Method (Slides 4-7)
**Time**: 2:30 - 7:00 (4.5 minutes)
**Goal**: Explain the approach
**Key Points**:
- [Overview]
- [Component 1]
- [Component 2]
- [Innovation]
**Transition**: "Let's see if this works..."

## Results (Slides 8-12)
**Time**: 7:00 - 12:00 (5 minutes)
**Goal**: Show evidence
**Key Points**:
- [Main result]
- [Comparison]
- [Ablation]
- [Analysis]
**Transition**: "In conclusion..."

## Conclusion (Slides 13-14)
**Time**: 12:00 - 14:00 (2 minutes)
**Goal**: Summarize and impact
**Key Points**:
- [Summary]
- [Contributions]
- [Future work]
**Transition**: "Thank you. Questions?"

## Q&A Preparation (Slide 15)
**Time**: 14:00 - 15:00 (5 minutes)
**Anticipated Questions**:
1. [Question 1]
   - Answer: [Response]
2. [Question 2]
   - Answer: [Response]
```

---

### 4. visual-suggestions.md

**Purpose**: Design and visualization recommendations

**Structure**:
```markdown
# Visual Suggestions

## Overall Style
- **Color scheme**: [Minimal / Academic / Brand]
- **Font**: [Serif / Sans-serif / Monospace]
- **Layout**: [Clean / Detailed / Graphical]

## Slide Templates

### Title Slide
```
┌─────────────────────────────┐
│                             │
│     [Paper Title]           │
│                             │
│     [Your Name]             │
│     [Affiliation]           │
│                             │
│     [Conference]            │
│     [Date]                  │
│                             │
└─────────────────────────────┘
```

### Content Slide
```
┌─────────────────────────────┐
│ [Headline]                  │
├─────────────────────────────┤
│                             │
│  [Content area]             │
│                             │
│  [Figure if needed]         │
│                             │
└─────────────────────────────┘
```

## Figure Suggestions

### Figure 1: [Architecture Diagram]
**Type**: Block diagram
**Purpose**: Show method overview
**Components**:
- [Component 1]
- [Component 2]
- [Component 3]
**Style**: Clean, labeled, color-coded

### Figure 2: [Results Chart]
**Type**: Bar chart / Line chart
**Purpose**: Compare with baselines
**Data**: [What to plot]
**Style**: Clear labels, legend, annotations

### Figure 3: [Attention Visualization]
**Type**: Heatmap
**Purpose**: Show attention patterns
**Data**: [What to visualize]
**Style**: Color gradient, clear labels

## Animation Suggestions

### Slide Transitions
- [Fade / Slide / None]
- Duration: [0.5s / 1s]

### Element Animations
- [Appear / Fly in / Grow]
- Timing: [Sequential / Simultaneous]

## Typography

### Headings
- Font size: [Large]
- Font weight: [Bold]
- Color: [Dark]

### Body Text
- Font size: [Medium]
- Line height: [1.5]
- Color: [Dark gray]

### Code/Technical
- Font: [Monospace]
- Background: [Light gray]
- Syntax highlighting: [Yes]

## Color Palette

### Primary
- [Color 1]: [Hex code]
- [Color 2]: [Hex code]

### Accent
- [Color 3]: [Hex code]

### Neutral
- [Background]: [Hex code]
- [Text]: [Hex code]
```

---

## Secondary Deliverables

### 5. qa-preparation.md

**Purpose**: Q&A preparation

### 6. timing-guide.md

**Purpose**: Time management

---

## File Organization

```
output/
├── presentation-outline.md    # High-level structure
├── slide-content.md           # Detailed slide content
├── speaker-notes.md           # Talking points
├── visual-suggestions.md      # Design recommendations
├── qa-preparation.md          # Q&A prep
└── timing-guide.md            # Time management
```

---

## Quality Indicators

### Good Output
✅ Clear narrative arc
✅ One message per slide
✅ Appropriate pacing
✅ Helpful speaker notes
✅ Effective visuals

### Bad Output
❌ Text-heavy slides
❌ Unclear structure
❌ Poor timing
❌ No speaker notes
❌ Weak visuals

---

*Academic Deck Builder Output Format - Part of GradAgentKit*