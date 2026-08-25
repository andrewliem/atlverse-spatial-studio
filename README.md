# Atlverse // Interactive 2.5D Spatial Studio

An interactive, high-performance 2.5D spatial studio website for **Andrew Tanny Liem** ([atlverse.xyz](https://atlverse.xyz/)), built with **WebGL GLSL depth-displacement parallax**, zero-dependency **Web Audio API** sound synthesis, ambient particle systems, responsive hotspot modals, and SEO metadata.

---

## 🚀 Features

- **2.5D WebGL Depth Parallax**: Real-time pixel displacement powered by mouse movement and mobile device orientation (gyroscope).
- **Interactive Hotspots**:
  - **Research & Publications**: Data-prism bookshelf linking to Google Scholar and ORCID.
  - **Universitas Klabat Credentials**: Digital insignia and academic credentials.
  - **Classroom Systems**: Smart board linking to [classroom.atlverse.xyz](https://classroom.atlverse.xyz).
  - **Research Blog**: Hologram displaying AI fine-tuning essays from [blog.atlverse.xyz](https://blog.atlverse.xyz).
  - **Research Workstation**: Interactive code terminal showcasing GitHub repositories.
  - **AI Companion Drone**: Interactive study assistant bot with synthesized audio responses.
  - **Sunset Skyline**: Panoramic city view with social/contact links.
- **Synthesized Audio Engine**: Zero-dependency Web Audio API sound generator for UI chirps, clicks, and chords.
- **Ambient Particles**: Floating dust motes drifting across the room lighting.
- **SEO & Accessibility**: Semantic `<main class="crawl">` layer and Schema.org JSON-LD structured data.

---

## 🛠️ Project Structure

```
├── assets/
│   ├── studio.png            # 16-bit hi-bit pixel art room illustration
│   ├── depth.png             # 2.5D grayscale depth map texture
│   └── center.png            # Portrait reference image
├── src/
│   ├── main.js               # WebGL engine, mouse lerp damping & hotspot coordinator
│   ├── styles.css            # Glassmorphism UI, terminal modal, tooltips & HUD
│   ├── audio.js              # Web Audio API sound effects synthesizer
│   ├── particles.js          # Sunlight dust particle engine
│   ├── hotspots.js           # Responsive hotspot bounding boxes & panel data
│   └── shaders/
│       └── parallax.js       # GLSL vertex & fragment shaders with aspect-ratio cover
├── index.html                # Main application entry point & SEO metadata
└── package.json
```

---

## 💻 Local Development

```bash
# Start with Python
python3 -m http.server 3000

# Or start with Vite
npm install
npm run dev
```

Open [http://localhost:3000](http://localhost:3000) in your browser.
