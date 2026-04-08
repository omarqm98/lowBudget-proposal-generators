---
name: excalidraw-diagrams
description: Generate Excalidraw flowcharts and architecture diagrams from a project brief — system architectures, workflow automations, data flows, and integration maps for AI automation projects. Use when creating diagrams, flowcharts, visual architectures, or process maps.
allowed-tools: Read, Write, Edit, Grep, Glob, Bash
---

# Excalidraw Diagram Generator

## Goal
Take a project brief or description and produce a professional `.excalidraw` diagram file. The output can be opened directly in excalidraw.com or the VS Code Excalidraw extension.

## Inputs
- **Project brief**: Free text, scope-of-work document, or description of the system/workflow
- **Diagram type** (optional — pick the best fit if not specified):
  - **System Architecture**: Services, APIs, databases, and their connections. Top-down or left-to-right.
  - **Workflow / Process Flow**: Sequential steps with decision points. Top-to-bottom or left-to-right.
  - **Data Flow**: Data sources, transformations, and destinations. Left-to-right.
  - **Integration Map**: Central system with external tool connections. Radial/hub-spoke layout.
  - **Client Overview**: High-level phases and deliverables. Clean, minimal, presentation-ready.
- **Style** (optional): `hand-drawn` (default, roughness=1) or `clean` (roughness=0)

## Color Palette

| Role | Hex | Usage |
|------|-----|-------|
| Primary | `#1B2A4A` | Main process/service boxes |
| Accent | `#3B82F6` | Highlights, secondary boxes, output actions |
| AI/Automation | `#10B981` | AI nodes, triggers, automation steps, success |
| Decision | `#F59E0B` | Diamond decision points, conditional paths |
| Neutral | `#64748B` | Supporting elements, databases, fallback paths |
| Container BG | `#F1F5F9` | Group/subsystem background rectangles |
| Text on dark | `#ffffff` | Text inside Primary, Accent, AI, Neutral shapes |
| Text on light | `#1E293B` | Text on light backgrounds, standalone labels |
| Stroke | `#334155` | All shape borders |
| Arrow | `#475569` | Arrow/connector lines |

**Color assignment by element function:**
- Triggers/inputs → AI/Automation (`#10B981`)
- Core processing → Primary (`#1B2A4A`)
- Decision points → Decision (`#F59E0B`)
- Output actions → Accent (`#3B82F6`)
- Databases/storage → Neutral (`#64748B`)
- Fallback/secondary paths → Neutral (`#64748B`)
- Subsystem containers → Container BG (`#F1F5F9`) at 60% opacity

## Layout Constants

```
SHAPE_WIDTH     = 200
SHAPE_HEIGHT    = 80
HORIZONTAL_GAP  = 120
VERTICAL_GAP    = 100
DIAMOND_SIZE    = 120
ELLIPSE_WIDTH   = 160
ELLIPSE_HEIGHT  = 80
```

**Position formulas:**
- Horizontal flow: `element_n.x = start_x + n * (SHAPE_WIDTH + HORIZONTAL_GAP)`
- Vertical flow: `element_n.y = start_y + n * (SHAPE_HEIGHT + VERTICAL_GAP)`
- Radial spoke: `spoke.x = center_x + radius * cos(angle) - SHAPE_WIDTH/2`

## Process

### Step 1: Understand the Brief
Read the project brief. Identify:
- System components (services, APIs, tools, databases)
- Relationships and data flows between them
- Decision points / conditional logic
- Inputs (triggers) and outputs (actions/results)

If key information is missing, ask before generating.

### Step 2: Select Diagram Type
Pick the best diagram type based on the brief. State your choice and why. Default mappings:
- Brief describes a sequential process → **Workflow / Process Flow**
- Brief describes how systems connect → **System Architecture**
- Brief describes tool integrations → **Integration Map**
- Brief describes data movement → **Data Flow**
- Brief is high-level / for a client presentation → **Client Overview**

### Step 3: Plan the Layout
Before writing JSON, plan:
1. List all elements (nodes) and their labels
2. Determine flow direction (top-to-bottom or left-to-right)
3. Assign grid positions using the layout constants
4. Assign colors based on element function (see color assignment table)
5. Identify which elements connect via arrows

### Step 4: Generate Element IDs
Create unique IDs for every element:
- Shapes: `rect_1`, `ellipse_1`, `diamond_1`
- Text: `text_1`, `text_2` (bound text) or `label_1` (standalone)
- Arrows: `arrow_1`, `arrow_2`
- Containers: `container_1`

### Step 5: Write the JSON
Generate the complete `.excalidraw` file. Use the schema reference and templates:
- [Excalidraw Schema Reference](references/excalidraw_schema_reference.md)
- [Diagram Templates](references/diagram_templates.md)

**Output path:** `.tmp/diagrams/{brief_slug}_{YYYYMMDD_HHMMSS}.excalidraw`

Create the `.tmp/diagrams/` directory if it doesn't exist:
```bash
mkdir -p ".tmp/diagrams"
```

### Step 6: Validate
Read the generated file back and verify:
- [ ] Valid JSON (no syntax errors)
- [ ] All arrows have valid `startBinding.elementId` and `endBinding.elementId` referencing real shape IDs
- [ ] All bound text elements have `containerId` pointing to a real shape ID
- [ ] All shapes with bound text list the text in their `boundElements` array
- [ ] All shapes with arrows list those arrows in their `boundElements` array
- [ ] No overlapping elements (check x/y positions + widths don't collide)
- [ ] Title text element exists at the top

### Step 7: Return the File Path
Tell the user:
1. The file path
2. How to open it: drag the file into excalidraw.com, or open with the VS Code Excalidraw extension

## Hard Rules

1. **Unique IDs** — every element gets a unique ID in `{type}_{n}` format
2. **Bidirectional bindings** — if an arrow binds to a shape, the shape must list that arrow in `boundElements`, AND the arrow must reference the shape in `startBinding`/`endBinding`
3. **Bound text consistency** — shape lists text in `boundElements`, text has `containerId` pointing back
4. **No overlapping elements** — calculate all positions using the layout constants
5. **Use the color palette** — no random or arbitrary colors. Map element function → palette role
6. **Default roughness 1** (hand-drawn). Only use 0 if user requests "clean" style
7. **strokeWidth 2** for all shapes and arrows
8. **fontSize 28** for titles, **20** for shape labels, **16** for edge labels / diamond text, **14** for annotations
9. **fontFamily 1** (Virgil) for roughness 1; **fontFamily 3** (Cascadia) for roughness 0
10. **Max 30 shape elements** per diagram — if the architecture is larger, split into multiple diagrams or collapse subsystems into grouped containers
11. **Always include a title** — standalone text at the top, fontSize 28
12. **Element order in array**: containers (bottom) → shapes → bound text → arrows → standalone text → title (top)
13. **Arrow color** always `#475569` — arrows should not use shape colors
14. **File naming**: `{brief_slug}_{YYYYMMDD_HHMMSS}.excalidraw` — slug is lowercase, hyphens, max 40 chars

## JSON Skeleton

Every generated file wraps elements in this structure:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    ... all elements here ...
  ],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
```

## First-Run Setup

Before executing, check if the workspace has a `.gitignore` file. If it doesn't, assume the user is new to this skill. In that case:

1. Ask the user if this is their first time running this skill
2. If yes, walk them through how it works:
   - No API keys needed — this skill generates pure JSON files
   - Output files can be opened at excalidraw.com (drag and drop) or with the VS Code Excalidraw extension
   - Diagrams use a professional color palette suited for client presentations
3. Let them know that Nick wishes them the best!
