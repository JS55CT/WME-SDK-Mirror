# WME SDK Documentation Mirror

**LLM-ready documentation for the Waze Map Editor SDK** — automatically kept fresh and optimized for Claude Code and AI consumption.

## 🚀 Quick Start: Use the WME SDK Skill

The fastest way to work with WME SDK:

```
/wme-sdk How do I query all venues on the map?
```

**[View the complete skill →](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/skills/SKILL.md)**

The skill includes:
- Real-world WME scripting patterns
- Complete SDK API reference with examples
- Migration guide from legacy W object to modern SDK
- Advanced patterns (layer styling, shortcuts, performance optimization, geometry handling)
- Error handling strategies
- Best practices for Tampermonkey scripts

---

## 📚 Documentation Access

If you prefer raw documentation files, access them here:

### 📖 SDK Documentation Files

All documentation available as bundled Markdown files, optimized for LLM context windows:

| Resource | Link | Purpose |
|----------|------|---------|
| **Master Index** | [index.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/index.md) | Start here — table of contents and overview |
| **Classes** | [classes.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/classes.md) | All SDK classes (DataModel, Map, Shortcuts, Sidebar, etc.) |
| **Interfaces** | [interfaces.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/interfaces.md) | Data shapes and type definitions |
| **Types** | [types.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/types.md) | Enums, unions, and custom types |
| **Functions** | [functions.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/functions.md) | Top-level utility functions |
| **Variables** | [variables.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/variables.md) | Module-level constants |
| **Modules** | [modules.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/modules.md) | Namespace and module structure |

### 🚀 Guides & Tutorials

Learn how to use the SDK with real-world examples:

| Guide | Link | Topics |
|-------|------|--------|
| **Getting Started** | [how-to-get-started-with-the-wmeSDK.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/how-to-get-started-with-the-wmeSDK.md) | SDK initialization, authentication, first steps |
| **Migration Guide** | [migration-guide.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/migration-guide.md) | Migrating from legacy W object to modern SDK |
| **Script Examples** | [script-example-1.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/script-example-1.md) - [script-example-6.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/script-example-6.md) | Working Tampermonkey examples |
| **Geometry Reference** | [geometry-file-converters.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/geometry-file-converters.md) | File format converters and geometry tools |
| **Changelog** | [changelog.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/changelog.md) | SDK version history and breaking changes |

### 📋 Type Definitions & References

Complete TypeScript definitions and external documentation:

| Resource | Link | Purpose |
|----------|------|---------|
| **WME SDK Types** | [wmeSDK_typedefs.d.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/wmeSDK_typedefs.d.md) | Full TypeScript definitions wrapped in markdown |
| **GeoJSON Types** | [geojson_typeddefs.d.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/geojson_typeddefs.d.md) | GeoJSON type definitions |
| **Turf.js Docs** | [Turf-Docs.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/Turf-Docs.md) | Geometry manipulation library (replaces OpenLayers) |
| **GeoJSON RFC 7946** | [GeoJSON-Format-RFC-7946.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/GeoJSON-Format-RFC-7946.md) | Official GeoJSON specification |

## Alternative: Load Raw Documentation into Claude

If you prefer to paste documentation directly into Claude instead of using the skill:

1. **Master Index** — [index.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/index.md) (~50KB, complete overview)
2. **Focused Reference** — [classes.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/classes.md) (~30KB, classes only)
3. **Individual Files** — Any specific doc linked above

### Local Usage

If you clone this repo:

1. The skill will use local paths: `production/latest/output/docs/`
2. No internet needed for documentation access
3. Run the pipeline to keep docs fresh: `cd production/latest/scripts && python cleanup.py; python build-url-list.py; ...`

## 🛠️ Repository Structure

```
/
├── README.md                            # This file (directory index)
├── CLAUDE.md                            # Claude Code configuration & workflow
├── .gitignore                           # Git ignore rules
└── production/latest/
    ├── .git/                            # Version control (tracks SDK updates)
    ├── .gitignore                       # Output files to ignore
    ├── scripts/
    │   ├── README.md                    # Workflow guide for the pipeline
    │   ├── cleanup.py                   # Step 1: Clean old output
    │   ├── build-url-list.py            # Step 2: Discover all SDK doc URLs
    │   ├── download-pages.py            # Step 3: Download fresh HTML + typings
    │   ├── extract-to-md.py             # Step 4: Convert HTML to Markdown
    │   ├── create-grouped-md-files.py   # Step 5: Bundle docs for LLM
    │   └── update-skill.py              # Step 6: Sync WME SDK skill
    ├── source/                          # Downloaded HTML and static content
    │   ├── classes/, interfaces/, types/        # Individual doc pages
    │   ├── functions/, variables/, modules/     # (same structure)
    │   ├── documents/, guides/, externalDocs/   # Static content
    │   ├── TypeDefs/                    # TypeScript definitions
    │   └── index.html                   # Downloaded SPA homepage
    └── output/
        ├── docs/                        # Generated LLM-ready docs (served via GitHub Pages)
        └── skills/                      # Synced WME SDK skill
```

## 🔄 Keeping Docs Fresh

Run the automated pipeline to refresh documentation whenever the SDK updates:

```powershell
cd production/latest/scripts
py cleanup.py; py build-url-list.py; py download-pages.py; py extract-to-md.py; py create-grouped-md-files.py; py update-skill.py
```

For detailed setup and options, see [production/latest/scripts/README.md](production/latest/scripts/README.md).

## ✨ Key Features

- **Automated SPA Crawling** — Decodes TypeDoc's JavaScript navigation bundle to discover all documentation pages dynamically (not just `index.html`)
- **Incremental Updates** — Only re-downloads changed pages; full pipeline takes ~30 seconds
- **LLM-Optimized Bundling** — Groups documentation by topic (classes, interfaces, types, etc.) for efficient token usage
- **Skill Integration** — Automatically syncs documentation with the custom WME SDK Claude Code skill
- **Dual-Path Fallback** — Works offline with local repo clone or online via GitHub Pages
- **Version Control** — Git history tracks SDK version bumps and documentation changes over time

## 🚀 Quick Start

### For Claude Code Users

1. Use the **WME SDK skill** directly:
   ```
   @wme-sdk Show me how to query venues
   ```

2. Or, load docs into context:
   - Copy any file from [GitHub Pages](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/)
   - Paste into Claude's context window

### For Developers

1. Clone the repo:
   ```bash
   git clone https://github.com/JS55CT/WME-SDK-Mirror.git
   cd WME-SDK-Mirror/production/latest/scripts
   ```

2. Install Python dependencies:
   ```bash
   py -m pip install requests beautifulsoup4 lxml
   ```

3. Run the pipeline:
   ```bash
   py cleanup.py; py build-url-list.py; py download-pages.py; py extract-to-md.py; py create-grouped-md-files.py; py update-skill.py
   ```

## 📖 Documentation Index by Topic

### Getting Started
- [SDK Initialization](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/how-to-get-started-with-the-wmeSDK.md)
- [Migration from Legacy Code](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/migration-guide.md)
- [Working Examples](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/script-example-1.md)

### API Reference
- [Classes & Main APIs](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/classes.md) — Map, DataModel, Shortcuts, Sidebar, Events, etc.
- [Data Types & Interfaces](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/interfaces.md) — GeoJSON, Feature, Node, Segment, etc.
- [Type Definitions](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/types.md) — Enums, unions, custom types
- [Functions](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/functions.md) — Utility functions

### Advanced Topics
- [Geometry & Turf.js](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/Turf-Docs.md) — Geometry operations (replaces OpenLayers)
- [GeoJSON Format](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/GeoJSON-Format-RFC-7946.md) — Specification and examples
- [Geometry File Converters](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/geometry-file-converters.md) — SHP, KML, GeoJSON tools
- [Version Changelog](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/changelog.md) — SDK version history

## 🔗 External Links

- **Live SDK Docs** — https://www.waze.com/editor/sdk/
- **GitHub Repository** — https://github.com/JS55CT/WME-SDK-Mirror
- **Raw Markdown Files** — https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/
- **Browse Files on GitHub** — https://github.com/JS55CT/WME-SDK-Mirror/tree/master/production/latest/output/docs
- **Waze Map Editor** — https://www.waze.com/editor

## 📝 License

This is a documentation mirror of the Waze Map Editor SDK. See the original SDK documentation for usage rights and terms.

---

**Last Updated:** See git history in `production/latest/.git/`  
**SDK Version:** Check [index.md](https://js55ct.github.io/WME-SDK-Mirror/production/latest/output/docs/index.md) for current version
