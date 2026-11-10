import re, pathlib
src = pathlib.Path("src-page.html").read_text()
def rep(old, new, count=1):
    global src
    assert old in src, old
    src = src.replace(old, new, count)
rep('<script src="https://user.uploads.dev/file/7120a1e5e4aad372dc70cfe94a0b59fa.js"></script>', '<script src="bundles/cookie-clicker.js"></script>')
rep('<script src="https://user.uploads.dev/file/0d76e2ee9b49afdcc98cf86bb7cbfe0b.js"></script>', '<script src="bundles/crimson-keep.js"></script>')
rep('<script src="https://user.uploads.dev/file/d3b8d3655f3e0a4c10b56e4fa3ee3316.js"></script>', '<script src="bundles/js-bridge.js"></script>')
rep('<span class="sub">Web Editor</span>', '<span class="sub">BlackNode Engine</span>')
rep('<p class="eyebrow">Embedded Web Editor</p>', '<p class="eyebrow">BlackNode Engine &middot; Godot 4.7.2</p>')
rep('function updateLinks() { var h = urlFor(currentVersion()); openLink.href = h; openLinkHome.href = h; }',
    'function updateLinks() { var h = "https://editor.godotengine.org/releases/" + currentVersion() + "/"; openLink.href = h; openLinkHome.href = h; }')
rep('(the engine is fetched from editor.godotengine.org)', '(the engine is served from this site)')
rep("escapeHtml(urlFor(currentVersion()))", 'escapeHtml("https://editor.godotengine.org/releases/" + currentVersion() + "/")')
src = src.replace("~92&nbsp;MB", "~92&nbsp;MB")
head = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>BlackNode Engine</title>
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#101218">
<meta name="description" content="BlackNode Engine: Josh's personal Godot 4.7.2 game engine editor, running in the browser.">
<link rel="icon" href="icon.svg" type="image/svg+xml">
<script src="coi-serviceworker.js"></script>
<script>
// Stand-in for the Perchance runtime this page was built on.
(function () {
  function list(items) { return { selectAll: items.map(function (s) { return { evaluateItem: s }; }),
    get selectOne() { return { evaluateItem: items[Math.floor(Math.random() * items.length)] }; } }; }
  window.root = {
    editorOrigin: new URL("engine/", location.href).href,
    engineFiles: list(["godot.editor.js","godot.editor.audio.worklet.js","godot.editor.audio.position.worklet.js","godot.editor.wasm"]),
    defaultVersion: "4.7.2.stable",
    versions: list(["4.7.2.stable@4.7.2 (stable)"]),
    superFetch: function (u, o) { return fetch(u, o); },
    tips: list([
      "GDScript is Python-like - a great first language for games.",
      "Scene = a tree of Nodes. Everything in Godot is a node.",
      "Signals are Godot's built-in event system - connect them in the editor's Node tab.",
      "Press F5 in the editor to play your project; F6 plays the current scene.",
      "You can preload an existing project as a ZIP on the editor's start screen.",
      "GDScript reaches page JavaScript with JavaScriptBridge.eval(\\"1+1\\") - window.GodotJs helpers are ready to call."
    ])
  };
})();
</script>
</head>
<body>
'''
pathlib.Path("index.html").write_text(head + src + "\n</body>\n</html>\n")
print("ok", len(src))
