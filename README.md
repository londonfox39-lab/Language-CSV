# Language-CSV

## Wrapped Gift Terrain (AI + Dialogues Project)

Professional JSON-driven scene and camera animation:

- Open `WrapGift.html` through a local server.
- Scene config is embedded directly inside `WrapGift.html` in `<script type="application/json" id="scene-config">`.
- Click **Record 16s WebM** in the overlay to export a presentation-ready video.

### Quick Run

From project root:

```bash
python3 -m http.server 8000
```

Then open:

- `http://localhost:8000/WrapGift.html`

### Customize

Edit the JSON block inside `WrapGift.html` to adjust:

- camera path (`camera.path`)
- loop length (`timeline.durationSec`)
- terrain scale/noise/colors (`terrain`)
- sculpture forms (`forms`)

### Use Your Own Terrain File (OBJ)

Inside the JSON `terrain` object in `WrapGift.html`:

- set `"source": "obj"`
- set `"objUrl": "./assets/your-terrain.obj"`
- optionally tune `objScale`, `objPosition`, and `objRotation` (degrees)

Then place your `.obj` in an `assets/` folder at project root.