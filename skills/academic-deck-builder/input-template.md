# Academic Deck Builder - Input Template

> Use this template when calling the academic-deck-builder skill.

---

## Task

**What type of presentation?**

- [ ] Conference talk (15-20 min)
- [ ] Seminar talk (30-45 min)
- [ ] Thesis defense (45-60 min)
- [ ] Group meeting (15-30 min)
- [ ] Workshop presentation (20-30 min)

---

## Presentation Topic

**What are you presenting?**

[Describe your topic clearly]

**Example**:
```
Dynamic quantization for time-series Transformer models
using attention-based bit-width allocation.
```

---

## Audience

**Who will be there?**

### Expertise Level
- [ ] Experts in your field
- [ ] General ML researchers
- [ ] Mixed audience
- [ ] Students

### Audience Size
- [ ] Small (< 20 people)
- [ ] Medium (20-50 people)
- [ ] Large (50+ people)

### Expectations
- [ ] Technical depth
- [ ] High-level overview
- [ ] Practical applications
- [ ] Theoretical insights

---

## Duration

**How long is the talk?**

- [ ] 10 minutes + 5 Q&A
- [ ] 15 minutes + 5 Q&A
- [ ] 20 minutes + 10 Q&A
- [ ] 30 minutes + 15 Q&A
- [ ] 45 minutes + 15 Q&A
- [ ] Other: _____________

---

## Source Material

**What material do you have?**

- [ ] Full paper (paper-draft.md)
- [ ] Abstract only
- [ ] Slides from previous talk
- [ ] Project documentation
- [ ] Experiment results

**File paths**:
```
[List file paths]
```

---

## Presentation Style

**How should it feel?**

- [ ] Formal academic
- [ ] Informal/Conversational
- [ ] Interactive/Discussion
- [ ] Storytelling
- [ ] Data-heavy

---

## Key Messages

**What should audience remember?**

1. [Message 1]
2. [Message 2]
3. [Message 3]

**Example**:
```
1. Dynamic quantization adapts to temporal patterns
2. Our method achieves 30% compression with <3% accuracy loss
3. Attention weights guide bit allocation effectively
```

---

## Visual Preferences

**How visual should it be?**

- [ ] Minimal text, lots of figures
- [ ] Balanced text and visuals
- [ ] Detailed with equations
- [ ] Graph-heavy

---

## Q&A Concerns

**What questions do you expect?**

1. [Anticipated question 1]
2. [Anticipated question 2]
3. [Anticipated question 3]

**Example**:
```
1. How does this compare to static quantization?
2. What's the computational overhead?
3. Does this work for other modalities?
```

---

## Special Requirements

**Any special needs?**

- [ ] Demo required
- [ ] Live coding
- [ ] Poll/Interaction
- [ ] Specific tools (Slidev/HTML/PowerPoint)
- [ ] Accessibility requirements

---

## Additional Notes

**Anything else?**

[Add context]

---

## Example Complete Input

```markdown
## Task
Conference talk (15 min + 5 Q&A)

## Presentation Topic
Dynamic quantization for time-series Transformers

## Audience
- ML researchers at NeurIPS
- Expertise: High
- Size: Medium (50-100)

## Duration
15 minutes + 5 minutes Q&A

## Source Material
- paper-draft.md (full paper)
- results/ (experiment data)

## Presentation Style
Formal academic, data-heavy

## Key Messages
1. Dynamic beats static quantization
2. Attention guides allocation
3. 30% compression, <3% loss

## Visual Preferences
Balanced text and visuals, clear figures

## Q&A Concerns
1. Comparison with other compression methods
2. Scalability to larger models
3. Deployment considerations

## Special Requirements
- Include architecture diagram
- Show attention visualization
```

---

*Academic Deck Builder Input Template - Part of GradAgentKit*