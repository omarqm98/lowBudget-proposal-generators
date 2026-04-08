# Excalidraw JSON Schema Reference

## File Wrapper

Every `.excalidraw` file is JSON with this structure:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
```

All elements go in the `elements` array.

---

## Common Properties (all element types)

| Property | Type | Description |
|----------|------|-------------|
| `id` | string | Unique identifier. Use `{type}_{n}` format (e.g., `rect_1`, `arrow_3`) |
| `type` | string | `"rectangle"`, `"ellipse"`, `"diamond"`, `"text"`, `"arrow"`, `"line"` |
| `x` | number | X position (top-left corner) |
| `y` | number | Y position (top-left corner) |
| `width` | number | Element width in pixels |
| `height` | number | Element height in pixels |
| `angle` | number | Rotation in radians. Always `0` unless rotating |
| `strokeColor` | string | Border/stroke hex color |
| `backgroundColor` | string | Fill hex color, or `"transparent"` |
| `fillStyle` | string | `"solid"`, `"hachure"`, `"cross-hatch"` |
| `strokeWidth` | number | Border thickness. Use `2` for shapes, `2` for arrows |
| `roughness` | number | `1` = hand-drawn (default), `0` = clean/polished |
| `opacity` | number | `100` = fully opaque |
| `seed` | number | Random int for hand-drawn rendering. Use `index * 12345 + 67890` |
| `groupIds` | array | Array of group ID strings. Empty `[]` if ungrouped |
| `boundElements` | array | Array of `{id, type}` objects for bound text/arrows. `null` if none |
| `isDeleted` | boolean | Always `false` |
| `locked` | boolean | Always `false` |
| `roundness` | object | Shape-specific. See per-element docs below |
| `updated` | number | Timestamp in ms. Use `1` |
| `version` | number | Element version. Use `1` |
| `versionNonce` | number | Random int. Use same formula as seed |

---

## Rectangle

For process steps, service boxes, containers.

```json
{
  "id": "rect_1",
  "type": "rectangle",
  "x": 100,
  "y": 100,
  "width": 200,
  "height": 80,
  "angle": 0,
  "strokeColor": "#334155",
  "backgroundColor": "#1B2A4A",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "opacity": 100,
  "seed": 80235,
  "groupIds": [],
  "boundElements": [
    { "id": "text_1", "type": "text" },
    { "id": "arrow_1", "type": "arrow" }
  ],
  "roundness": { "type": 3 },
  "isDeleted": false,
  "locked": false,
  "updated": 1,
  "version": 1,
  "versionNonce": 12345
}
```

**Notes:**
- `roundness: { "type": 3 }` gives slightly rounded corners (Excalidraw default for rectangles)
- List ALL bound text elements and arrows in `boundElements`

---

## Ellipse

For databases, data stores, start/end nodes.

```json
{
  "id": "ellipse_1",
  "type": "ellipse",
  "x": 100,
  "y": 100,
  "width": 160,
  "height": 80,
  "angle": 0,
  "strokeColor": "#334155",
  "backgroundColor": "#64748B",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "opacity": 100,
  "seed": 92580,
  "groupIds": [],
  "boundElements": [
    { "id": "text_2", "type": "text" }
  ],
  "roundness": { "type": 2 },
  "isDeleted": false,
  "locked": false,
  "updated": 1,
  "version": 1,
  "versionNonce": 23456
}
```

**Notes:**
- `roundness: { "type": 2 }` is the Excalidraw default for ellipses
- Width/height define the bounding box; the ellipse is inscribed

---

## Diamond

For decision points, conditional logic.

```json
{
  "id": "diamond_1",
  "type": "diamond",
  "x": 140,
  "y": 100,
  "width": 120,
  "height": 120,
  "angle": 0,
  "strokeColor": "#334155",
  "backgroundColor": "#F59E0B",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "opacity": 100,
  "seed": 104925,
  "groupIds": [],
  "boundElements": [
    { "id": "text_3", "type": "text" },
    { "id": "arrow_2", "type": "arrow" },
    { "id": "arrow_3", "type": "arrow" }
  ],
  "roundness": { "type": 2 },
  "isDeleted": false,
  "locked": false,
  "updated": 1,
  "version": 1,
  "versionNonce": 34567
}
```

**Notes:**
- Width and height should be equal for a proper diamond shape
- The diamond is inscribed in the bounding box
- Decision diamonds typically have 2+ outgoing arrows (Yes/No branches)

---

## Text

Two variants: **standalone** and **bound to a shape**.

### Bound Text (inside a shape)

The shape must list the text in its `boundElements`. The text must reference the shape via `containerId`.

```json
{
  "id": "text_1",
  "type": "text",
  "x": 135,
  "y": 127,
  "width": 130,
  "height": 25,
  "angle": 0,
  "strokeColor": "#ffffff",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "roughness": 1,
  "opacity": 100,
  "seed": 117270,
  "groupIds": [],
  "boundElements": null,
  "roundness": null,
  "isDeleted": false,
  "locked": false,
  "updated": 1,
  "version": 1,
  "versionNonce": 45678,
  "text": "Process Step",
  "fontSize": 20,
  "fontFamily": 1,
  "textAlign": "center",
  "verticalAlign": "middle",
  "containerId": "rect_1",
  "originalText": "Process Step",
  "autoResize": true,
  "lineHeight": 1.25
}
```

### Position Calculation for Bound Text

The text x/y positions are calculated from the parent shape:

```
text.x = parent.x + (parent.width / 2) - (text.width / 2)
text.y = parent.y + (parent.height / 2) - (text.height / 2)
```

**Width estimation:**
- Approximate `text.width` as `text.length * fontSize * 0.6`
- Approximate `text.height` as `fontSize * lineHeight` per line (multiply by number of lines)

### Standalone Text (labels, titles, annotations)

Same as bound text but:
- `containerId`: `null`
- `textAlign`: `"left"` or `"center"`
- `verticalAlign`: `"top"`
- Position via x/y directly

**Font sizes:**
- Title: `fontSize: 28`
- Shape labels: `fontSize: 20`
- Arrow/edge labels: `fontSize: 16`
- Annotations: `fontSize: 14`

**Font families:**
- `1` = Virgil (hand-drawn) — use with roughness 1
- `2` = Helvetica — use for clean style
- `3` = Cascadia (monospace) — use for code/technical labels

---

## Arrow

Arrows connect elements. This is the most complex element — bindings must be correct.

```json
{
  "id": "arrow_1",
  "type": "arrow",
  "x": 300,
  "y": 140,
  "width": 120,
  "height": 0,
  "angle": 0,
  "strokeColor": "#475569",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 2,
  "roughness": 1,
  "opacity": 100,
  "seed": 129615,
  "groupIds": [],
  "boundElements": null,
  "roundness": { "type": 2 },
  "isDeleted": false,
  "locked": false,
  "updated": 1,
  "version": 1,
  "versionNonce": 56789,
  "points": [[0, 0], [120, 0]],
  "startBinding": {
    "elementId": "rect_1",
    "focus": 0,
    "gap": 1
  },
  "endBinding": {
    "elementId": "rect_2",
    "focus": 0,
    "gap": 1
  },
  "startArrowhead": null,
  "endArrowhead": "arrow",
  "lastCommittedPoint": null
}
```

### Arrow Binding Rules

**Three-way consistency is REQUIRED:**
1. Arrow's `startBinding.elementId` → source shape ID
2. Arrow's `endBinding.elementId` → target shape ID
3. Source shape's `boundElements` must include `{ "id": "arrow_1", "type": "arrow" }`
4. Target shape's `boundElements` must include `{ "id": "arrow_1", "type": "arrow" }`

If any of these are missing, the arrow won't snap to the shapes.

### Binding Properties

| Property | Type | Description |
|----------|------|-------------|
| `elementId` | string | ID of the shape this end binds to |
| `focus` | number | -1 to 1. `0` = center of the shape edge. Negative = left/top, positive = right/bottom |
| `gap` | number | Pixel gap between arrow tip and shape edge. Use `1` |

### Arrow Position & Points Calculation

The arrow's `x`/`y` is the **start point** of the arrow. The `points` array defines the path relative to that start.

**Horizontal arrow (left-to-right):**
```
arrow.x = source.x + source.width    (right edge of source)
arrow.y = source.y + source.height/2  (vertical center of source)
points = [[0, 0], [gap_distance, 0]]
gap_distance = target.x - (source.x + source.width)
arrow.width = gap_distance
arrow.height = 0
```

**Vertical arrow (top-to-bottom):**
```
arrow.x = source.x + source.width/2   (horizontal center of source)
arrow.y = source.y + source.height     (bottom edge of source)
points = [[0, 0], [0, gap_distance]]
gap_distance = target.y - (source.y + source.height)
arrow.width = 0
arrow.height = gap_distance
```

**Diagonal arrow:**
```
arrow.x = source.x + source.width     (or appropriate edge)
arrow.y = source.y + source.height/2
dx = target.x - arrow.x               (or target center - arrow start)
dy = (target.y + target.height/2) - arrow.y
points = [[0, 0], [dx, dy]]
arrow.width = abs(dx)
arrow.height = abs(dy)
```

### Arrow Labels

To label an arrow, create a standalone text element positioned at the arrow's midpoint:

```
label.x = arrow.x + (points[1][0] / 2) - (label.width / 2)
label.y = arrow.y + (points[1][1] / 2) - label.height - 5
```

The label is NOT bound to the arrow — it's a separate standalone text element positioned nearby.

### Arrowhead Options

| Value | Description |
|-------|-------------|
| `"arrow"` | Standard arrowhead (default for `endArrowhead`) |
| `"triangle"` | Filled triangle |
| `"bar"` | Flat bar/line |
| `null` | No arrowhead (default for `startArrowhead`) |

---

## Line

For decorative separators, borders. Same as arrow but no bindings.

```json
{
  "id": "line_1",
  "type": "line",
  "x": 100,
  "y": 300,
  "width": 600,
  "height": 0,
  "points": [[0, 0], [600, 0]],
  "strokeColor": "#334155",
  "backgroundColor": "transparent",
  "fillStyle": "solid",
  "strokeWidth": 1,
  "roughness": 1,
  "opacity": 50,
  "seed": 141960,
  "groupIds": [],
  "boundElements": null,
  "roundness": { "type": 2 },
  "isDeleted": false,
  "locked": false,
  "updated": 1,
  "version": 1,
  "versionNonce": 67890,
  "startBinding": null,
  "endBinding": null,
  "startArrowhead": null,
  "endArrowhead": null,
  "lastCommittedPoint": null
}
```

---

## Grouping Elements

To visually group elements, assign the same group ID string to their `groupIds` array:

```json
// Element A
"groupIds": ["group_backend"]

// Element B
"groupIds": ["group_backend"]
```

Nested groups: `"groupIds": ["inner_group", "outer_group"]` — list from innermost to outermost.

---

## Element Order

Elements are rendered in array order (first = bottom, last = top). Recommended order:
1. Container/background rectangles (bottom layer)
2. Shape elements (rectangles, ellipses, diamonds)
3. Bound text elements (must come after their parent shape)
4. Arrows
5. Standalone text (labels, annotations, title)
6. Title text (topmost)
