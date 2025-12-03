# Box Drawing Character Reference

This reference provides a comprehensive guide to characters used in Monodraw-style diagrams.

## Basic Box Drawing Characters

### Single Line Boxes

```
┌─────────┐
│         │
└─────────┘
```

Characters:
- `─` horizontal line
- `│` vertical line
- `┌` top-left corner
- `┐` top-right corner
- `└` bottom-left corner
- `┘` bottom-right corner

### Double Line Boxes

```
╔═════════╗
║         ║
╚═════════╝
```

Characters:
- `═` horizontal double line
- `║` vertical double line
- `╔` top-left corner
- `╗` top-right corner
- `╚` bottom-left corner
- `╝` bottom-right corner

### Mixed Line Boxes

```
╓─────────╖
║         ║
╙─────────╜
```

Characters for mixing:
- `╓` `╖` `╙` `╜` - double vertical, single horizontal
- `╒` `╕` `╘` `╛` - single vertical, double horizontal

### Dashed/Dotted Boxes

```
┌ ─ ─ ─ ─ ┐
│         │
└ ─ ─ ─ ─ ┘
```

For dashed boxes, use spaced characters or:
- `┄` `┅` - dashed horizontal lines (light and heavy)
- `┆` `┇` - dashed vertical lines (light and heavy)
- `┈` `┉` - dotted horizontal lines
- `┊` `┋` - dotted vertical lines

### Simple ASCII Boxes

When Unicode isn't available or for simplicity:

```
+----------+
|          |
+----------+
```

Characters:
- `+` corners
- `-` horizontal
- `|` vertical

## Connectors and Junctions

### Line Intersections

```
┼  single line cross
╬  double line cross
┿  vertical double, horizontal single cross
╂  horizontal double, vertical single cross
```

### T-Junctions

```
├  left T
┤  right T
┬  top T
┴  bottom T
```

Double line versions:
```
╠  ╣  ╦  ╩
```

### Complex Junctions

For more complex diagrams:
```
╞═  ═╡  ═╤═  ═╧═  (mixed thickness)
```

## Arrows

### Unicode Arrows

```
→  right arrow
←  left arrow
↑  up arrow
↓  down arrow
↔  left-right arrow
↕  up-down arrow
⇒  double right arrow
⇐  double left arrow
⇄  right over left
↺  circular arrow (clockwise)
↻  circular arrow (counterclockwise)
```

### ASCII Arrows

```
->   right
<-   left
<->  bidirectional
-->  long right
==>  thick right
~~>  wavy right (for indirect/causal)
```

### Curved Arrows

```
↱  down-right
↲  down-left
↰  up-right
↱  up-left
⤴  up-right curved
⤵  down-right curved
```

### Causal/Special Arrows

For system maps and causal diagrams:
```
--+-->  positive influence
------->
--(-)->  negative influence
--||-->  delayed causal link (|| represents delay)
```

## Shading and Fill Patterns

### Block Shading

```
░  light shade (25%)
▒  medium shade (50%)
▓  dark shade (75%)
█  solid block
```

### ASCII Pattern Alternatives

When Unicode shading isn't available:

```
:::::::  light stipple
.......  dots
///////  diagonal lines
#######  heavy fill
%%%%%%%  medium pattern
```

### Stippled Areas (Monodraw style)

For the classic Monodraw aesthetic, use sparse dot patterns:
```
··········
··········
··········
```

Or for more density:
```
:::::::::::
:::::::::::
```

## Special Shapes

### Database (Cylinder)

```
  ╭─────╮
  │ DB  │
  ╰─────╯
```

Characters:
- `╭` `╮` rounded top corners
- `╰` `╯` rounded bottom corners

### Diamond (Decision)

```
    ╱╲
   ╱  ╲
   ╲  ╱
    ╲╱
```

Or simplified:
```
   /\
  /  \
  \  /
   \/
```

### Rounded Rectangle (Terminal)

```
╭──────────╮
│  START   │
╰──────────╯
```

### Circle/Ellipse

```
   ╭───╮
  ╱     ╲
  ╲     ╱
   ╰───╯
```

### Cloud (for sources/sinks)

```
  .-~~~-.
 (       )
  `~---~'
```

Or simplified:
```
  ,---.
 (     )
  `---'
```

### Queue/Message Bus

```
║│││││││║
```

Or:
```
[====]
```

## Spacing and Alignment

### Padding Inside Boxes

Use at least 1 space on each side:
```
Good:
┌─────────┐
│  Text   │
└─────────┘

Bad (cramped):
┌───────┐
│Text   │
└───────┘
```

### Vertical Spacing

Leave blank lines between distinct components:
```
┌─────────┐
│  Box 1  │
└─────────┘
     │
     ↓
┌─────────┐
│  Box 2  │
└─────────┘
```

### Horizontal Alignment

Align boxes on a consistent grid:
```
┌─────┐         ┌─────┐
│  A  │  ----→  │  B  │
└─────┘         └─────┘
   │               │
   ↓               ↓
┌─────┐         ┌─────┐
│  C  │  ----→  │  D  │
└─────┘         └─────┘
```

## Multi-line Text in Boxes

Center each line:
```
┌─────────────┐
│   Service   │
│    Name     │
│             │
│  (details)  │
└─────────────┘
```

## Labels and Annotations

### On Arrows

```
     Label
─────────────→

Or inline:
──────[Label]─────→
```

### Beside Boxes

```
┌─────────┐
│  Box    │  ← This is an important note
└─────────┘
```

### Numbered Steps

```
    1
┌─────────┐
│  First  │
└─────────┘
    │
    2
    ↓
┌─────────┐
│  Second │
└─────────┘
```

## System Map Specific Characters

### Loop Markers

```
R1  (Reinforcing loop 1)
R2  (Reinforcing loop 2)
B1  (Balancing loop 1)
B2  (Balancing loop 2)
```

### Polarity Indicators

```
  (+)
────────→  positive relationship

  (-)
────────→  negative relationship
```

### Stock and Flow

```
┌─────────┐
│  Stock  │  (rectangle)
└─────────┘

──<╳>──  (flow valve - ╳ or >◁ or >|<)

~~~~~   (cloud/source)
```

### Delay Indicator

```
──||──→  (parallel bars indicate delay)
```

## Tips for Consistent Style

1. **Choose one box style** per diagram (single or double line, not mixed unless for emphasis)
2. **Use consistent arrow types** (stick to Unicode or ASCII, not both)
3. **Align everything** to an invisible grid for clean appearance
4. **Balance spacing** - neither too cramped nor too sparse
5. **Use shading sparingly** - only to emphasize key areas
6. **Keep it readable** - clarity over complexity
