# BlackNode Engine

Josh's personal game engine: the official Godot 4.7.2 web editor, self-hosted on GitHub Pages and wrapped in the UI from his Perchance "Godot Web Editor" generator (`vuhtodow3c`).

Live: https://blacknodedev.github.io/blacknode-engine/

- Engine files are served from `engine/4.7.2.stable/` (official Godot Foundation build, MIT).
- `coi-serviceworker.js` (MIT, gzuidhof) gives the page cross-origin isolation, which the engine's threads need, since Pages can't set headers.
- Demo projects (Cookie Clicker, Crimson Keep, JS Bridge) are in `bundles/`.
- Edit `src-page.html`, then run `python3 build.py` to regenerate `index.html`.

First load downloads ~92 MB and caches it. Projects save in the browser.
