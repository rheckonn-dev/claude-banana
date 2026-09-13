# BlueSky battery · 3D viewer

Source for the published artifact. `battery-3d.html` is the artifact body — the
publisher wraps it in its own `<!doctype html><head>…<body>` skeleton, so the
file starts at `<title>` and has no `<html>`/`<head>`/`<body>` tags of its own.

Everything the shop edits lives in the `CONFIG` block at the top: label sizes in
millimetres, brand, group size, CCA, phone, warning text. Both labels scale from
their own height, so changing a dimension rescales that design whole.

The case is drawn with CSS 3D transforms — six faces in a `preserve-3d` rig,
with the fittings (posts, cell caps, carry strap, lid label) in the box's own 3D
space rather than nested inside the top face, which would tear the shared edge.
Face shading is not painted on: `relight()` takes each face's world normal and
sets the opacity of two overlays, one for the key light up and to the left and
one for the weak fill on the right, so the lights stay in the room while the
case turns.
