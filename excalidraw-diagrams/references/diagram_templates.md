# Diagram Templates — Pre-Built JSON Snippets

Copy and adapt these tested patterns. All use the Autonomise AI color palette.

## Color Palette Quick Reference

| Role | Hex | Use For |
|------|-----|---------|
| Primary | `#1B2A4A` | Main process/service boxes |
| Accent | `#3B82F6` | Highlights, secondary boxes |
| AI/Auto | `#10B981` | AI nodes, automation steps, success |
| Decision | `#F59E0B` | Diamonds, conditional paths |
| Neutral | `#64748B` | Supporting elements, databases |
| Container | `#F1F5F9` | Group backgrounds |
| Text Dark | `#1E293B` | Text on light backgrounds |
| Text Light | `#ffffff` | Text on dark backgrounds |
| Stroke | `#334155` | All shape borders |
| Arrow | `#475569` | Arrow/connector lines |

---

## Template 1: Two Connected Boxes (Horizontal)

The atomic building block. Two rectangles connected by a horizontal arrow.

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
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
    },
    {
      "id": "text_1",
      "type": "text",
      "x": 155,
      "y": 127,
      "width": 90,
      "height": 25,
      "angle": 0,
      "strokeColor": "#ffffff",
      "backgroundColor": "transparent",
      "fillStyle": "solid",
      "strokeWidth": 1,
      "roughness": 1,
      "opacity": 100,
      "seed": 92580,
      "groupIds": [],
      "boundElements": null,
      "roundness": null,
      "isDeleted": false,
      "locked": false,
      "updated": 1,
      "version": 1,
      "versionNonce": 23456,
      "text": "Step A",
      "fontSize": 20,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "rect_1",
      "originalText": "Step A",
      "autoResize": true,
      "lineHeight": 1.25
    },
    {
      "id": "rect_2",
      "type": "rectangle",
      "x": 420,
      "y": 100,
      "width": 200,
      "height": 80,
      "angle": 0,
      "strokeColor": "#334155",
      "backgroundColor": "#3B82F6",
      "fillStyle": "solid",
      "strokeWidth": 2,
      "roughness": 1,
      "opacity": 100,
      "seed": 104925,
      "groupIds": [],
      "boundElements": [
        { "id": "text_2", "type": "text" },
        { "id": "arrow_1", "type": "arrow" }
      ],
      "roundness": { "type": 3 },
      "isDeleted": false,
      "locked": false,
      "updated": 1,
      "version": 1,
      "versionNonce": 34567
    },
    {
      "id": "text_2",
      "type": "text",
      "x": 475,
      "y": 127,
      "width": 90,
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
      "text": "Step B",
      "fontSize": 20,
      "fontFamily": 1,
      "textAlign": "center",
      "verticalAlign": "middle",
      "containerId": "rect_2",
      "originalText": "Step B",
      "autoResize": true,
      "lineHeight": 1.25
    },
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
  ],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
```

**Position math:**
- `rect_1`: x=100, width=200 → right edge at 300
- `arrow_1`: starts at x=300 (right edge of rect_1), gap=120
- `rect_2`: x=420 (300 + 120 gap)
- All at y=100, height=80 → vertical center at y=140

---

## Template 2: Three-Step Vertical Flow

```json
[
  {
    "id": "rect_1", "type": "rectangle",
    "x": 200, "y": 100, "width": 200, "height": 80,
    "strokeColor": "#334155", "backgroundColor": "#1B2A4A",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 80235, "angle": 0, "groupIds": [],
    "boundElements": [{"id": "text_1", "type": "text"}, {"id": "arrow_1", "type": "arrow"}],
    "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 12345
  },
  {
    "id": "text_1", "type": "text",
    "x": 255, "y": 127, "width": 90, "height": 25,
    "strokeColor": "#ffffff", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
    "seed": 92580, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
    "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 23456,
    "text": "Step 1", "fontSize": 20, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "rect_1", "originalText": "Step 1", "autoResize": true, "lineHeight": 1.25
  },
  {
    "id": "rect_2", "type": "rectangle",
    "x": 200, "y": 280, "width": 200, "height": 80,
    "strokeColor": "#334155", "backgroundColor": "#3B82F6",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 104925, "angle": 0, "groupIds": [],
    "boundElements": [{"id": "text_2", "type": "text"}, {"id": "arrow_1", "type": "arrow"}, {"id": "arrow_2", "type": "arrow"}],
    "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 34567
  },
  {
    "id": "text_2", "type": "text",
    "x": 255, "y": 307, "width": 90, "height": 25,
    "strokeColor": "#ffffff", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
    "seed": 117270, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
    "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 45678,
    "text": "Step 2", "fontSize": 20, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "rect_2", "originalText": "Step 2", "autoResize": true, "lineHeight": 1.25
  },
  {
    "id": "rect_3", "type": "rectangle",
    "x": 200, "y": 460, "width": 200, "height": 80,
    "strokeColor": "#334155", "backgroundColor": "#10B981",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 141960, "angle": 0, "groupIds": [],
    "boundElements": [{"id": "text_3", "type": "text"}, {"id": "arrow_2", "type": "arrow"}],
    "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 56789
  },
  {
    "id": "text_3", "type": "text",
    "x": 255, "y": 487, "width": 90, "height": 25,
    "strokeColor": "#ffffff", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
    "seed": 154305, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
    "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 67890,
    "text": "Step 3", "fontSize": 20, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "rect_3", "originalText": "Step 3", "autoResize": true, "lineHeight": 1.25
  },
  {
    "id": "arrow_1", "type": "arrow",
    "x": 300, "y": 180, "width": 0, "height": 100,
    "strokeColor": "#475569", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 166650, "angle": 0, "groupIds": [], "boundElements": null,
    "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 78901,
    "points": [[0, 0], [0, 100]],
    "startBinding": {"elementId": "rect_1", "focus": 0, "gap": 1},
    "endBinding": {"elementId": "rect_2", "focus": 0, "gap": 1},
    "startArrowhead": null, "endArrowhead": "arrow", "lastCommittedPoint": null
  },
  {
    "id": "arrow_2", "type": "arrow",
    "x": 300, "y": 360, "width": 0, "height": 100,
    "strokeColor": "#475569", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 178995, "angle": 0, "groupIds": [], "boundElements": null,
    "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 89012,
    "points": [[0, 0], [0, 100]],
    "startBinding": {"elementId": "rect_2", "focus": 0, "gap": 1},
    "endBinding": {"elementId": "rect_3", "focus": 0, "gap": 1},
    "startArrowhead": null, "endArrowhead": "arrow", "lastCommittedPoint": null
  }
]
```

**Vertical spacing math:**
- Row 1: y=100, bottom edge = 180
- Arrow 1: y=180, height=100
- Row 2: y=280 (180 + 100), bottom edge = 360
- Arrow 2: y=360, height=100
- Row 3: y=460 (360 + 100)
- All centered at x=200, width=200 → center at x=300

---

## Template 3: Decision Diamond Pattern

Rectangle → Diamond → two branches (Yes/No).

```json
[
  {
    "id": "rect_1", "type": "rectangle",
    "x": 200, "y": 100, "width": 200, "height": 80,
    "strokeColor": "#334155", "backgroundColor": "#1B2A4A",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 80235, "angle": 0, "groupIds": [],
    "boundElements": [{"id": "text_1", "type": "text"}, {"id": "arrow_1", "type": "arrow"}],
    "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 12345
  },
  {
    "id": "text_1", "type": "text",
    "x": 248, "y": 127, "width": 104, "height": 25,
    "strokeColor": "#ffffff", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
    "seed": 92580, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
    "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 23456,
    "text": "Process", "fontSize": 20, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "rect_1", "originalText": "Process", "autoResize": true, "lineHeight": 1.25
  },
  {
    "id": "diamond_1", "type": "diamond",
    "x": 240, "y": 280, "width": 120, "height": 120,
    "strokeColor": "#334155", "backgroundColor": "#F59E0B",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 104925, "angle": 0, "groupIds": [],
    "boundElements": [{"id": "text_2", "type": "text"}, {"id": "arrow_1", "type": "arrow"}, {"id": "arrow_2", "type": "arrow"}, {"id": "arrow_3", "type": "arrow"}],
    "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 34567
  },
  {
    "id": "text_2", "type": "text",
    "x": 275, "y": 327, "width": 50, "height": 25,
    "strokeColor": "#1E293B", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
    "seed": 117270, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
    "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 45678,
    "text": "Check?", "fontSize": 16, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "diamond_1", "originalText": "Check?", "autoResize": true, "lineHeight": 1.25
  },
  {
    "id": "rect_yes", "type": "rectangle",
    "x": 50, "y": 500, "width": 200, "height": 80,
    "strokeColor": "#334155", "backgroundColor": "#10B981",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 129615, "angle": 0, "groupIds": [],
    "boundElements": [{"id": "text_yes", "type": "text"}, {"id": "arrow_2", "type": "arrow"}],
    "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 56789
  },
  {
    "id": "text_yes", "type": "text",
    "x": 120, "y": 527, "width": 60, "height": 25,
    "strokeColor": "#ffffff", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
    "seed": 141960, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
    "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 67890,
    "text": "Yes Path", "fontSize": 20, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "rect_yes", "originalText": "Yes Path", "autoResize": true, "lineHeight": 1.25
  },
  {
    "id": "rect_no", "type": "rectangle",
    "x": 350, "y": 500, "width": 200, "height": 80,
    "strokeColor": "#334155", "backgroundColor": "#64748B",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 154305, "angle": 0, "groupIds": [],
    "boundElements": [{"id": "text_no", "type": "text"}, {"id": "arrow_3", "type": "arrow"}],
    "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 78901
  },
  {
    "id": "text_no", "type": "text",
    "x": 420, "y": 527, "width": 60, "height": 25,
    "strokeColor": "#ffffff", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
    "seed": 166650, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
    "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 89012,
    "text": "No Path", "fontSize": 20, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "rect_no", "originalText": "No Path", "autoResize": true, "lineHeight": 1.25
  },
  {
    "id": "arrow_1", "type": "arrow",
    "x": 300, "y": 180, "width": 0, "height": 100,
    "strokeColor": "#475569", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 178995, "angle": 0, "groupIds": [], "boundElements": null,
    "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 90123,
    "points": [[0, 0], [0, 100]],
    "startBinding": {"elementId": "rect_1", "focus": 0, "gap": 1},
    "endBinding": {"elementId": "diamond_1", "focus": 0, "gap": 1},
    "startArrowhead": null, "endArrowhead": "arrow", "lastCommittedPoint": null
  },
  {
    "id": "arrow_2", "type": "arrow",
    "x": 240, "y": 340, "width": -90, "height": 160,
    "strokeColor": "#475569", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 191340, "angle": 0, "groupIds": [], "boundElements": null,
    "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 1234,
    "points": [[0, 0], [-90, 160]],
    "startBinding": {"elementId": "diamond_1", "focus": 0, "gap": 1},
    "endBinding": {"elementId": "rect_yes", "focus": 0, "gap": 1},
    "startArrowhead": null, "endArrowhead": "arrow", "lastCommittedPoint": null
  },
  {
    "id": "arrow_3", "type": "arrow",
    "x": 360, "y": 340, "width": 90, "height": 160,
    "strokeColor": "#475569", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 203685, "angle": 0, "groupIds": [], "boundElements": null,
    "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 2345,
    "points": [[0, 0], [90, 160]],
    "startBinding": {"elementId": "diamond_1", "focus": 0, "gap": 1},
    "endBinding": {"elementId": "rect_no", "focus": 0, "gap": 1},
    "startArrowhead": null, "endArrowhead": "arrow", "lastCommittedPoint": null
  },
  {
    "id": "label_yes", "type": "text",
    "x": 170, "y": 400, "width": 30, "height": 20,
    "strokeColor": "#10B981", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
    "seed": 216030, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
    "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 3456,
    "text": "Yes", "fontSize": 16, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "top",
    "containerId": null, "originalText": "Yes", "autoResize": true, "lineHeight": 1.25
  },
  {
    "id": "label_no", "type": "text",
    "x": 400, "y": 400, "width": 20, "height": 20,
    "strokeColor": "#64748B", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
    "seed": 228375, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
    "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 4567,
    "text": "No", "fontSize": 16, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "top",
    "containerId": null, "originalText": "No", "autoResize": true, "lineHeight": 1.25
  }
]
```

**Key patterns:**
- Diamond at center, branches go diagonally to left (Yes) and right (No)
- Arrow from diamond left edge: `x = diamond.x`, points go negative-x and positive-y
- Arrow from diamond right edge: `x = diamond.x + diamond.width`, points go positive-x and positive-y
- "Yes"/"No" labels are standalone text positioned near the arrow midpoints

---

## Template 4: Hub-and-Spoke Integration Map

Central node with radial connections. 5 spokes at equal angles.

**Positioning formula for spokes:**
```
angle_step = 2 * PI / num_spokes
spoke_n.x = center_x + radius * cos(n * angle_step) - spoke_width / 2
spoke_n.y = center_y + radius * sin(n * angle_step) - spoke_height / 2
```

For 5 spokes with center at (500, 400) and radius 280:
| Spoke | Angle (rad) | x | y |
|-------|-------------|---|---|
| 0 | 0.00 | 680 | 360 |
| 1 | 1.26 | 587 | 628 |
| 2 | 2.51 | 310 | 565 |
| 3 | 3.77 | 310 | 195 |
| 4 | 5.03 | 587 | 132 |

```json
[
  {
    "id": "hub", "type": "ellipse",
    "x": 420, "y": 360, "width": 160, "height": 80,
    "strokeColor": "#334155", "backgroundColor": "#1B2A4A",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 80235, "angle": 0, "groupIds": [],
    "boundElements": [
      {"id": "hub_text", "type": "text"},
      {"id": "arrow_0", "type": "arrow"},
      {"id": "arrow_1", "type": "arrow"},
      {"id": "arrow_2", "type": "arrow"},
      {"id": "arrow_3", "type": "arrow"},
      {"id": "arrow_4", "type": "arrow"}
    ],
    "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 12345
  },
  {
    "id": "hub_text", "type": "text",
    "x": 450, "y": 387, "width": 100, "height": 25,
    "strokeColor": "#ffffff", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
    "seed": 92580, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
    "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 23456,
    "text": "Core System", "fontSize": 20, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "hub", "originalText": "Core System", "autoResize": true, "lineHeight": 1.25
  },
  {
    "id": "spoke_0", "type": "rectangle",
    "x": 680, "y": 360, "width": 200, "height": 80,
    "strokeColor": "#334155", "backgroundColor": "#3B82F6",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 104925, "angle": 0, "groupIds": [],
    "boundElements": [{"id": "spoke_text_0", "type": "text"}, {"id": "arrow_0", "type": "arrow"}],
    "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 34567
  },
  {
    "id": "spoke_text_0", "type": "text",
    "x": 730, "y": 387, "width": 100, "height": 25,
    "strokeColor": "#ffffff", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
    "seed": 117270, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
    "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 45678,
    "text": "Service A", "fontSize": 20, "fontFamily": 1,
    "textAlign": "center", "verticalAlign": "middle",
    "containerId": "spoke_0", "originalText": "Service A", "autoResize": true, "lineHeight": 1.25
  },
  {
    "id": "arrow_0", "type": "arrow",
    "x": 580, "y": 400, "width": 100, "height": 0,
    "strokeColor": "#475569", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 129615, "angle": 0, "groupIds": [], "boundElements": null,
    "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 56789,
    "points": [[0, 0], [100, 0]],
    "startBinding": {"elementId": "hub", "focus": 0, "gap": 1},
    "endBinding": {"elementId": "spoke_0", "focus": 0, "gap": 1},
    "startArrowhead": null, "endArrowhead": "arrow", "lastCommittedPoint": null
  }
]
```

**Note:** This shows the hub + 1 spoke. Replicate the spoke pattern for all 5 positions from the table above. Each spoke gets its own rect, text, and arrow. All arrows bind back to the hub.

---

## Template 5: Grouped Architecture Block

A light container rectangle with sub-elements inside, sharing a groupId.

```json
[
  {
    "id": "container_1", "type": "rectangle",
    "x": 80, "y": 80, "width": 660, "height": 200,
    "strokeColor": "#334155", "backgroundColor": "#F1F5F9",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 60,
    "seed": 80235, "angle": 0, "groupIds": [],
    "boundElements": null,
    "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 12345
  },
  {
    "id": "container_label", "type": "text",
    "x": 90, "y": 85, "width": 150, "height": 20,
    "strokeColor": "#64748B", "backgroundColor": "transparent",
    "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
    "seed": 92580, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
    "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 23456,
    "text": "Backend Services", "fontSize": 14, "fontFamily": 1,
    "textAlign": "left", "verticalAlign": "top",
    "containerId": null, "originalText": "Backend Services", "autoResize": true, "lineHeight": 1.25
  },
  {
    "id": "inner_1", "type": "rectangle",
    "x": 100, "y": 120, "width": 180, "height": 70,
    "strokeColor": "#334155", "backgroundColor": "#1B2A4A",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 104925, "angle": 0, "groupIds": ["group_backend"],
    "boundElements": [{"id": "inner_text_1", "type": "text"}],
    "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 34567
  },
  {
    "id": "inner_2", "type": "rectangle",
    "x": 320, "y": 120, "width": 180, "height": 70,
    "strokeColor": "#334155", "backgroundColor": "#3B82F6",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 117270, "angle": 0, "groupIds": ["group_backend"],
    "boundElements": [{"id": "inner_text_2", "type": "text"}],
    "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 45678
  },
  {
    "id": "inner_3", "type": "rectangle",
    "x": 540, "y": 120, "width": 180, "height": 70,
    "strokeColor": "#334155", "backgroundColor": "#10B981",
    "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
    "seed": 129615, "angle": 0, "groupIds": ["group_backend"],
    "boundElements": [{"id": "inner_text_3", "type": "text"}],
    "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 56789
  }
]
```

**Pattern:** Container at lower opacity (60), label as standalone text at top-left, inner elements share `groupIds: ["group_backend"]`. The container is NOT in the group — it's just a visual backdrop.

---

## Template 6: Complete Workflow — AI Lead Qualification

Full working diagram using all patterns and the color palette.

**Scenario:** WhatsApp message → AI qualifies → Decision → CRM or Nurture sequence

This is a complete `.excalidraw` file you can copy in its entirety:

```json
{
  "type": "excalidraw",
  "version": 2,
  "source": "https://excalidraw.com",
  "elements": [
    {
      "id": "title", "type": "text",
      "x": 180, "y": 30, "width": 400, "height": 35,
      "strokeColor": "#1E293B", "backgroundColor": "transparent",
      "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
      "seed": 10000, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
      "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 10001,
      "text": "AI Lead Qualification Flow", "fontSize": 28, "fontFamily": 1,
      "textAlign": "center", "verticalAlign": "top",
      "containerId": null, "originalText": "AI Lead Qualification Flow", "autoResize": true, "lineHeight": 1.25
    },
    {
      "id": "rect_trigger", "type": "rectangle",
      "x": 100, "y": 120, "width": 200, "height": 80,
      "strokeColor": "#334155", "backgroundColor": "#10B981",
      "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
      "seed": 20000, "angle": 0, "groupIds": [],
      "boundElements": [{"id": "text_trigger", "type": "text"}, {"id": "arrow_1", "type": "arrow"}],
      "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 20001
    },
    {
      "id": "text_trigger", "type": "text",
      "x": 115, "y": 135, "width": 170, "height": 50,
      "strokeColor": "#ffffff", "backgroundColor": "transparent",
      "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
      "seed": 20002, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
      "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 20003,
      "text": "WhatsApp\nMessage", "fontSize": 20, "fontFamily": 1,
      "textAlign": "center", "verticalAlign": "middle",
      "containerId": "rect_trigger", "originalText": "WhatsApp\nMessage", "autoResize": true, "lineHeight": 1.25
    },
    {
      "id": "rect_ai", "type": "rectangle",
      "x": 100, "y": 300, "width": 200, "height": 80,
      "strokeColor": "#334155", "backgroundColor": "#1B2A4A",
      "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
      "seed": 30000, "angle": 0, "groupIds": [],
      "boundElements": [{"id": "text_ai", "type": "text"}, {"id": "arrow_1", "type": "arrow"}, {"id": "arrow_2", "type": "arrow"}],
      "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 30001
    },
    {
      "id": "text_ai", "type": "text",
      "x": 120, "y": 315, "width": 160, "height": 50,
      "strokeColor": "#ffffff", "backgroundColor": "transparent",
      "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
      "seed": 30002, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
      "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 30003,
      "text": "AI Agent\nQualifies Lead", "fontSize": 20, "fontFamily": 1,
      "textAlign": "center", "verticalAlign": "middle",
      "containerId": "rect_ai", "originalText": "AI Agent\nQualifies Lead", "autoResize": true, "lineHeight": 1.25
    },
    {
      "id": "diamond_qual", "type": "diamond",
      "x": 140, "y": 480, "width": 120, "height": 120,
      "strokeColor": "#334155", "backgroundColor": "#F59E0B",
      "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
      "seed": 40000, "angle": 0, "groupIds": [],
      "boundElements": [{"id": "text_qual", "type": "text"}, {"id": "arrow_2", "type": "arrow"}, {"id": "arrow_yes", "type": "arrow"}, {"id": "arrow_no", "type": "arrow"}],
      "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 40001
    },
    {
      "id": "text_qual", "type": "text",
      "x": 155, "y": 522, "width": 90, "height": 35,
      "strokeColor": "#1E293B", "backgroundColor": "transparent",
      "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
      "seed": 40002, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
      "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 40003,
      "text": "Qualified?", "fontSize": 16, "fontFamily": 1,
      "textAlign": "center", "verticalAlign": "middle",
      "containerId": "diamond_qual", "originalText": "Qualified?", "autoResize": true, "lineHeight": 1.25
    },
    {
      "id": "rect_crm", "type": "rectangle",
      "x": -150, "y": 680, "width": 200, "height": 80,
      "strokeColor": "#334155", "backgroundColor": "#3B82F6",
      "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
      "seed": 50000, "angle": 0, "groupIds": [],
      "boundElements": [{"id": "text_crm", "type": "text"}, {"id": "arrow_yes", "type": "arrow"}],
      "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 50001
    },
    {
      "id": "text_crm", "type": "text",
      "x": -130, "y": 695, "width": 160, "height": 50,
      "strokeColor": "#ffffff", "backgroundColor": "transparent",
      "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
      "seed": 50002, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
      "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 50003,
      "text": "Add to CRM\n+ Book Call", "fontSize": 20, "fontFamily": 1,
      "textAlign": "center", "verticalAlign": "middle",
      "containerId": "rect_crm", "originalText": "Add to CRM\n+ Book Call", "autoResize": true, "lineHeight": 1.25
    },
    {
      "id": "rect_nurture", "type": "rectangle",
      "x": 350, "y": 680, "width": 200, "height": 80,
      "strokeColor": "#334155", "backgroundColor": "#64748B",
      "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
      "seed": 60000, "angle": 0, "groupIds": [],
      "boundElements": [{"id": "text_nurture", "type": "text"}, {"id": "arrow_no", "type": "arrow"}],
      "roundness": {"type": 3}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 60001
    },
    {
      "id": "text_nurture", "type": "text",
      "x": 370, "y": 695, "width": 160, "height": 50,
      "strokeColor": "#ffffff", "backgroundColor": "transparent",
      "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
      "seed": 60002, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
      "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 60003,
      "text": "Nurture\nSequence", "fontSize": 20, "fontFamily": 1,
      "textAlign": "center", "verticalAlign": "middle",
      "containerId": "rect_nurture", "originalText": "Nurture\nSequence", "autoResize": true, "lineHeight": 1.25
    },
    {
      "id": "arrow_1", "type": "arrow",
      "x": 200, "y": 200, "width": 0, "height": 100,
      "strokeColor": "#475569", "backgroundColor": "transparent",
      "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
      "seed": 70000, "angle": 0, "groupIds": [], "boundElements": null,
      "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 70001,
      "points": [[0, 0], [0, 100]],
      "startBinding": {"elementId": "rect_trigger", "focus": 0, "gap": 1},
      "endBinding": {"elementId": "rect_ai", "focus": 0, "gap": 1},
      "startArrowhead": null, "endArrowhead": "arrow", "lastCommittedPoint": null
    },
    {
      "id": "arrow_2", "type": "arrow",
      "x": 200, "y": 380, "width": 0, "height": 100,
      "strokeColor": "#475569", "backgroundColor": "transparent",
      "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
      "seed": 70002, "angle": 0, "groupIds": [], "boundElements": null,
      "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 70003,
      "points": [[0, 0], [0, 100]],
      "startBinding": {"elementId": "rect_ai", "focus": 0, "gap": 1},
      "endBinding": {"elementId": "diamond_qual", "focus": 0, "gap": 1},
      "startArrowhead": null, "endArrowhead": "arrow", "lastCommittedPoint": null
    },
    {
      "id": "arrow_yes", "type": "arrow",
      "x": 140, "y": 540, "width": -240, "height": 140,
      "strokeColor": "#475569", "backgroundColor": "transparent",
      "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
      "seed": 70004, "angle": 0, "groupIds": [], "boundElements": null,
      "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 70005,
      "points": [[0, 0], [-240, 140]],
      "startBinding": {"elementId": "diamond_qual", "focus": 0, "gap": 1},
      "endBinding": {"elementId": "rect_crm", "focus": 0, "gap": 1},
      "startArrowhead": null, "endArrowhead": "arrow", "lastCommittedPoint": null
    },
    {
      "id": "arrow_no", "type": "arrow",
      "x": 260, "y": 540, "width": 190, "height": 140,
      "strokeColor": "#475569", "backgroundColor": "transparent",
      "fillStyle": "solid", "strokeWidth": 2, "roughness": 1, "opacity": 100,
      "seed": 70006, "angle": 0, "groupIds": [], "boundElements": null,
      "roundness": {"type": 2}, "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 70007,
      "points": [[0, 0], [190, 140]],
      "startBinding": {"elementId": "diamond_qual", "focus": 0, "gap": 1},
      "endBinding": {"elementId": "rect_nurture", "focus": 0, "gap": 1},
      "startArrowhead": null, "endArrowhead": "arrow", "lastCommittedPoint": null
    },
    {
      "id": "label_yes", "type": "text",
      "x": 10, "y": 590, "width": 30, "height": 20,
      "strokeColor": "#10B981", "backgroundColor": "transparent",
      "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
      "seed": 80000, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
      "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 80001,
      "text": "Yes", "fontSize": 16, "fontFamily": 1,
      "textAlign": "center", "verticalAlign": "top",
      "containerId": null, "originalText": "Yes", "autoResize": true, "lineHeight": 1.25
    },
    {
      "id": "label_no", "type": "text",
      "x": 370, "y": 590, "width": 20, "height": 20,
      "strokeColor": "#64748B", "backgroundColor": "transparent",
      "fillStyle": "solid", "strokeWidth": 1, "roughness": 1, "opacity": 100,
      "seed": 80002, "angle": 0, "groupIds": [], "boundElements": null, "roundness": null,
      "isDeleted": false, "locked": false, "updated": 1, "version": 1, "versionNonce": 80003,
      "text": "No", "fontSize": 16, "fontFamily": 1,
      "textAlign": "center", "verticalAlign": "top",
      "containerId": null, "originalText": "No", "autoResize": true, "lineHeight": 1.25
    }
  ],
  "appState": {
    "gridSize": null,
    "viewBackgroundColor": "#ffffff"
  },
  "files": {}
}
```

**Color mapping in this example:**
- Trigger (WhatsApp) → Emerald `#10B981` (input/trigger)
- AI Processing → Deep Navy `#1B2A4A` (core process)
- Decision → Amber `#F59E0B` (conditional)
- CRM Action → Electric Blue `#3B82F6` (output/action)
- Nurture (fallback) → Slate `#64748B` (secondary path)
- Yes label → Emerald (positive path)
- No label → Slate (neutral/fallback path)
