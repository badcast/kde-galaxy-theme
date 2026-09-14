## 2024-05-24 - Aurorae Theme Edge Clipping Fix using SVG rects
**Learning:** In KDE Aurorae window decorations, using thin `<line>` elements with sub-pixel coordinates (like `x1="0.5"`) inside wider layout boxes can cause rendering artifacts and clipping on the side edges when KWin stretches or renders them.
**Action:** Replace 1px `<line>` elements with integer-aligned `<rect width="1">` elements to ensure crisp, accurate rendering without clipping. When adding gradients, apply them to the `fill` of these `<rect>`s, rather than changing the `.rc` layout variables unnecessarily.
