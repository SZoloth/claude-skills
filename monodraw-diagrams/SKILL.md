---
name: monodraw-diagrams
description: Create clean, technical ASCII-art diagrams in Monodraw-inspired style for system architectures, workflow processes, system maps, and service blueprints. Use when the user asks to visually explain something, create a diagram, visualize a system, or illustrate technical concepts. Produces monospaced, line-drawn diagrams with boxes, arrows, and dotted shading for clear technical documentation.
---

# Monodraw Diagrams

## Overview

This skill enables creation of clean, technical ASCII-art style diagrams using monospaced characters. The aesthetic is inspired by Monodraw with a focus on clarity, simplicity, and professional technical documentation. All diagrams use plain text characters to create boxes, arrows, connectors, and shading that render beautifully in monospaced fonts.

## When to Use This Skill

Use this skill when users ask to:
- "Visually explain [system/concept]"
- "Create a diagram of [architecture/process]"
- "Visualize [system/workflow]"
- "Show me how [X] works"
- "Diagram [data structure/flow]"
- "Map out [system/service]"

The skill supports four primary diagram types: system architectures, workflow processes, system maps (Donella Meadows style), and service blueprints.

## Core Diagram Types

### 1. System Architecture Diagrams

Use for: visualizing software systems, microservices, APIs, databases, and technical infrastructure.

**Key elements:**
- Rectangular boxes for services/components
- Arrows showing data flow and dependencies
- Cylindrical shapes for databases (using curved characters)
- Dotted/stippled areas for grouping related components
- Dashed boxes for logical boundaries (e.g., "Backend", "Frontend")

**Example request:** "Show me how a microservices architecture communicates"

Refer to `references/patterns.md` for system architecture templates and `references/box-drawing.md` for character options.

### 2. Workflow Process Diagrams

Use for: illustrating step-by-step processes, algorithms, decision flows, and sequential operations.

**Key elements:**
- Rectangular boxes for process steps
- Diamond shapes for decisions
- Arrows indicating flow direction
- Start/end terminals (rounded rectangles)
- Swim lanes for different actors/systems (horizontal divisions)
- Parallel process indicators

**Example request:** "Diagram the user onboarding workflow"

Refer to `references/patterns.md` for workflow templates including decision trees and swim lane patterns.

### 3. System Maps (Donella Meadows Style)

Use for: showing causal relationships, feedback loops, stocks and flows, and systems thinking diagrams.

**Key elements:**
- Boxes or circles for variables/components
- Arrows with +/- polarity labels (causal links)
- Reinforcing loops marked with `R` or `R1, R2...`
- Balancing loops marked with `B` or `B1, B2...`
- Stock and flow notation (rectangles for stocks, valves for flows)
- Delay indicators `||` on arrows
- Cloud symbols for sources/sinks

**Example request:** "Create a system map showing the feedback loops in our growth model"

Refer to `references/patterns.md` for system map notation and `references/examples.md` for complete examples.

### 4. Service Blueprints

Use for: mapping customer journeys with frontstage/backstage service components, touchpoints, and support processes.

**Key elements:**
- Horizontal swim lanes (Customer Actions, Frontstage, Backstage, Support Processes)
- Time axis flowing left to right
- Boxes for actions/touchpoints
- Line of interaction (separating customer from service)
- Line of visibility (separating frontstage from backstage)
- Internal interaction line (separating backstage from support)
- Arrows showing dependencies

**Example request:** "Visualize the service blueprint for our checkout process"

Refer to `references/patterns.md` for service blueprint templates with proper lane structure.

## Design Principles

Follow these principles to maintain the clean Monodraw aesthetic:

### 1. Character Set

Use only standard ASCII characters for maximum compatibility:
- Box drawing: `─ │ ┌ ┐ └ ┘ ├ ┤ ┬ ┴ ┼ ═ ║ ╔ ╗ ╚ ╝`
- Arrows: `→ ← ↑ ↓ ↔ ↕` or simple `->` `<-` `<->` `-->`
- Shading: `░ ▒ ▓` or ASCII patterns like `:::` `...` `%%%`
- Connectors: `+` for junctions, `*` for bullet points

See `references/box-drawing.md` for complete character reference.

### 2. Visual Style

- **Clean and minimal**: Avoid unnecessary decoration
- **Aligned grid**: Keep boxes and elements aligned on an invisible grid
- **Consistent spacing**: Use uniform padding inside boxes and between elements
- **Monospaced font**: All diagrams assume monospaced rendering
- **High contrast**: Black on white, clear readability
- **Strategic emphasis**: Use dotted/stippled shading sparingly to highlight important areas

### 3. Layout Guidelines

- **Left-to-right flow**: Primary flow should generally move left to right (or top to bottom)
- **Logical grouping**: Use dashed or dotted containers to group related components
- **Clear labels**: Every box, arrow, and zone should be clearly labeled
- **Adequate spacing**: Leave breathing room between components
- **Legend when needed**: Include a legend/key for complex diagrams with multiple symbol types

### 4. Text Formatting

- **Concise labels**: Keep text short and descriptive
- **Centered in boxes**: Center text within rectangular boxes
- **Sentence case**: Use sentence case for labels and descriptions
- **Annotations**: Add explanatory notes outside the main diagram flow

## Output Format

When creating a diagram:

1. **Start with a brief explanation** of what the diagram shows
2. **Present the diagram** in a markdown code block with no language specified (renders in monospaced font)
3. **Add a legend/key** if the diagram uses special symbols
4. **Follow up with any clarifications** or notes about specific elements

**Example output structure:**

```
This diagram shows the authentication flow between the client, API gateway, and auth service.

[ASCII diagram here]

Legend:
- Solid arrows (→): synchronous requests
- Dashed arrows (⇢): asynchronous events
- [dotted areas]: external systems
```

## Resources

### references/

This skill includes reference documentation for detailed guidance:

- **`box-drawing.md`**: Complete character reference for boxes, arrows, connectors, and shading
- **`patterns.md`**: Template patterns for each diagram type with reusable structures
- **`examples.md`**: Full example diagrams for each of the four core types

Load these references as needed when creating diagrams. They provide comprehensive details without cluttering this main skill file.

## Tips for Effective Diagrams

- **Start simple**: Begin with the core flow or structure, then add details
- **Iterate**: Show the basic diagram first, then refine based on feedback
- **Ask clarifying questions**: If the system is complex, ask about key components before diagramming
- **Use appropriate diagram type**: Match the diagram type to the user's need (architecture vs. workflow vs. system map vs. service blueprint)
- **Test readability**: Ensure the diagram is clear even without color or styling
- **Leverage references**: For complex diagrams, review examples in `references/examples.md` first
