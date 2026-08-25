import { vertexShaderSource, fragmentShaderSource } from './shaders/parallax.js';
import { ParticleSystem } from './particles.js';
import { sound } from './audio.js';
import { HOTSPOTS, PROJECTS_DATA } from './hotspots.js';

class SpatialRoom {
  constructor() {
    this.canvas = document.getElementById('webgl-canvas');
    this.gl = this.canvas.getContext('webgl') || this.canvas.getContext('experimental-webgl');
    
    if (!this.gl) {
      alert('WebGL not supported in your browser.');
      return;
    }

    this.mouse = { x: 0, y: 0 };
    this.targetMouse = { x: 0, y: 0 };
    this.zoom = 1.0;
    this.targetZoom = 1.0;
    this.zoomCenter = { x: 0.5, y: 0.5 };
    this.targetZoomCenter = { x: 0.5, y: 0.5 };

    this.synthChordIndex = 0;
    this.isMuted = false;

    this.initWebGL();
    this.initParticles();
    this.initHotspots();
    this.initEvents();
    this.initTerminal();
    this.animate();
  }

  initWebGL() {
    const gl = this.gl;

    // Compile Shaders
    const vertShader = gl.createShader(gl.VERTEX_SHADER);
    gl.shaderSource(vertShader, vertexShaderSource);
    gl.compileShader(vertShader);

    const fragShader = gl.createShader(gl.FRAGMENT_SHADER);
    gl.shaderSource(fragShader, fragmentShaderSource);
    gl.compileShader(fragShader);

    const program = gl.createProgram();
    gl.attachShader(program, vertShader);
    gl.attachShader(program, fragShader);
    gl.linkProgram(program);
    gl.useProgram(program);
    this.program = program;

    // Setup Quad Geometry
    const positionBuffer = gl.createBuffer();
    gl.bindBuffer(gl.ARRAY_BUFFER, positionBuffer);
    const positions = new Float32Array([
      -1, -1,
       1, -1,
      -1,  1,
      -1,  1,
       1, -1,
       1,  1,
    ]);
    gl.bufferData(gl.ARRAY_BUFFER, positions, gl.STATIC_DRAW);

    const posLoc = gl.getAttribLocation(program, 'aPosition');
    gl.enableVertexAttribArray(posLoc);
    gl.vertexAttribPointer(posLoc, 2, gl.FLOAT, false, 0, 0);

    // Uniform locations
    this.uMouseLoc = gl.getUniformLocation(program, 'uMouse');
    this.uThresholdLoc = gl.getUniformLocation(program, 'uThreshold');
    this.uZoomLoc = gl.getUniformLocation(program, 'uZoom');
    this.uZoomCenterLoc = gl.getUniformLocation(program, 'uZoomCenter');
    this.uAspectCoverLoc = gl.getUniformLocation(program, 'uAspectCover');
    this.uTextureLoc = gl.getUniformLocation(program, 'uTexture');
    this.uDepthMapLoc = gl.getUniformLocation(program, 'uDepthMap');

    // Default uniform values
    gl.uniform2f(this.uThresholdLoc, 0.018, 0.018);
    gl.uniform1f(this.uZoomLoc, 1.0);
    gl.uniform2f(this.uZoomCenterLoc, 0.5, 0.5);

    // Load Textures
    this.colorTexture = this.loadTexture('/assets/studio.png', 0, this.uTextureLoc);
    this.depthTexture = this.loadTexture('/assets/depth.png', 1, this.uDepthMapLoc);

    this.resize();
  }

  loadTexture(src, textureUnit, uniformLoc) {
    const gl = this.gl;
    const texture = gl.createTexture();
    gl.activeTexture(gl.TEXTURE0 + textureUnit);
    gl.bindTexture(gl.TEXTURE_2D, texture);

    // Placeholder 1x1 pixel while loading
    gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, 1, 1, 0, gl.RGBA, gl.UNSIGNED_BYTE, new Uint8Array([20, 20, 30, 255]));

    const image = new Image();
    image.crossOrigin = "anonymous";
    image.src = src;
    image.onload = () => {
      gl.activeTexture(gl.TEXTURE0 + textureUnit);
      gl.bindTexture(gl.TEXTURE_2D, texture);
      gl.texImage2D(gl.TEXTURE_2D, 0, gl.RGBA, gl.RGBA, gl.UNSIGNED_BYTE, image);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_S, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_WRAP_T, gl.CLAMP_TO_EDGE);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MIN_FILTER, gl.LINEAR);
      gl.texParameteri(gl.TEXTURE_2D, gl.TEXTURE_MAG_FILTER, gl.LINEAR);
      gl.uniform1i(uniformLoc, textureUnit);
    };
    return texture;
  }

  initParticles() {
    const pCanvas = document.getElementById('particles-canvas');
    this.particles = new ParticleSystem(pCanvas);
  }

  getRenderBounds() {
    const winW = window.innerWidth;
    const winH = window.innerHeight;
    const imgAspect = 1920 / 1080;
    const winAspect = winW / winH;

    let renderW, renderH, offsetX, offsetY, scaleX, scaleY;

    if (winAspect > imgAspect) {
      // Screen is wider than 16:9 (crop top/bottom)
      renderW = winW;
      renderH = winW / imgAspect;
      offsetX = 0;
      offsetY = (winH - renderH) / 2;
      scaleX = 1.0;
      scaleY = imgAspect / winAspect;
    } else {
      // Screen is taller than 16:9 (crop left/right)
      renderH = winH;
      renderW = winH * imgAspect;
      offsetX = (winW - renderW) / 2;
      offsetY = 0;
      scaleX = winAspect / imgAspect;
      scaleY = 1.0;
    }

    return { renderW, renderH, offsetX, offsetY, scaleX, scaleY };
  }

  updateHotspotsLayerPosition() {
    const bounds = this.getRenderBounds();
    const layer = document.getElementById('hotspots-layer');
    if (!layer) return;

    layer.style.position = 'fixed';
    layer.style.left = `${bounds.offsetX}px`;
    layer.style.top = `${bounds.offsetY}px`;
    layer.style.width = `${bounds.renderW}px`;
    layer.style.height = `${bounds.renderH}px`;

    if (this.gl && this.uAspectCoverLoc) {
      this.gl.uniform2f(this.uAspectCoverLoc, bounds.scaleX, bounds.scaleY);
    }
  }

  initHotspots() {
    const container = document.getElementById('hotspots-layer');
    container.innerHTML = '';

    HOTSPOTS.forEach(spot => {
      const box = document.createElement('div');
      box.className = 'hotspot-box';
      box.dataset.id = spot.id;
      box.style.left = `${spot.rect.x}%`;
      box.style.top = `${spot.rect.y}%`;
      box.style.width = `${spot.rect.w}%`;
      box.style.height = `${spot.rect.h}%`;

      box.addEventListener('mouseenter', (e) => {
        sound.playHover();
        this.showTooltip(spot, e);
      });

      box.addEventListener('mousemove', (e) => {
        this.positionTooltip(e);
      });

      box.addEventListener('mouseleave', () => {
        this.hideTooltip();
      });

      box.addEventListener('click', () => {
        sound.playClick();
        this.handleHotspotClick(spot);
      });

      container.appendChild(box);
    });

    this.updateHotspotsLayerPosition();
  }

  showTooltip(spot, e) {
    const tooltip = document.getElementById('tooltip');
    tooltip.innerHTML = `
      <span class="tooltip-tag">${spot.category}</span>
      <span class="tooltip-title">${spot.title}</span>
    `;
    tooltip.classList.add('active');
    this.positionTooltip(e);
  }

  positionTooltip(e) {
    const tooltip = document.getElementById('tooltip');
    if (!tooltip.classList.contains('active')) return;

    const tooltipWidth = tooltip.offsetWidth || 220;
    const tooltipHeight = tooltip.offsetHeight || 44;

    let posX = e.clientX;
    let posY = e.clientY - 16;

    // Flip below cursor if close to top header/window boundary
    if (posY - tooltipHeight < 65) {
      posY = e.clientY + 22;
      tooltip.style.transform = 'translate(-50%, 0)';
    } else {
      tooltip.style.transform = 'translate(-50%, -100%)';
    }

    // Horizontal edge clamping to ensure 100% visibility
    const padding = 20;
    const halfWidth = tooltipWidth / 2;
    if (posX - halfWidth < padding) {
      posX = halfWidth + padding;
    } else if (posX + halfWidth > window.innerWidth - padding) {
      posX = window.innerWidth - halfWidth - padding;
    }

    tooltip.style.left = `${posX}px`;
    tooltip.style.top = `${posY}px`;
  }

  hideTooltip() {
    const tooltip = document.getElementById('tooltip');
    tooltip.classList.remove('active');
  }

  handleHotspotClick(spot) {
    if (spot.action === 'zoom_monitor') {
      this.openMonitor();
    } else if (spot.action === 'open_panel') {
      this.openSidePanel(spot.panel);
    } else if (spot.action === 'pet_bot') {
      sound.playHover();
      this.showToast('🤖 AI Study Bot: "Systems online. Ready for research!"');
    }
  }

  openSidePanel(panelData) {
    const panel = document.getElementById('side-panel');
    const backdrop = document.getElementById('side-panel-backdrop');
    document.getElementById('panel-tag').textContent = panelData.tag;
    document.getElementById('panel-title').textContent = panelData.title;
    document.getElementById('panel-body').innerHTML = panelData.content;

    panel.classList.add('active');
    backdrop.classList.add('active');
  }

  closeSidePanel() {
    document.getElementById('side-panel').classList.remove('active');
    document.getElementById('side-panel-backdrop').classList.remove('active');
  }

  openMonitor() {
    const modal = document.getElementById('monitor-modal');
    modal.classList.add('active');
    this.targetZoom = 1.35;
    this.targetZoomCenter = { x: 0.48, y: 0.52 };
  }

  closeMonitor() {
    const modal = document.getElementById('monitor-modal');
    modal.classList.remove('active');
    this.targetZoom = 1.0;
    this.targetZoomCenter = { x: 0.5, y: 0.5 };
  }

  initTerminal() {
    const container = document.getElementById('projects-container');
    container.innerHTML = PROJECTS_DATA.map(p => `
      <div class="project-card" onclick="window.sound && window.sound.playTerminalKey()">
        <h4>${p.title}</h4>
        <div class="project-tech">${p.tech}</div>
        <p>${p.desc}</p>
      </div>
    `).join('');
  }

  showToast(msg) {
    const toast = document.getElementById('toast');
    toast.textContent = msg;
    toast.classList.add('active');
    clearTimeout(this.toastTimer);
    this.toastTimer = setTimeout(() => toast.classList.remove('active'), 2500);
  }

  initEvents() {
    window.addEventListener('resize', () => {
      this.resize();
      this.updateHotspotsLayerPosition();
    });

    // Mouse Parallax Track
    window.addEventListener('mousemove', (e) => {
      this.targetMouse.x = (e.clientX / window.innerWidth - 0.5) * 2.0;
      this.targetMouse.y = (e.clientY / window.innerHeight - 0.5) * 2.0;
    });

    // Mobile Gyroscope tilt
    if (window.DeviceOrientationEvent) {
      window.addEventListener('deviceorientation', (e) => {
        if (e.gamma !== null && e.beta !== null) {
          this.targetMouse.x = Math.max(-1, Math.min(1, e.gamma / 30));
          this.targetMouse.y = Math.max(-1, Math.min(1, (e.beta - 45) / 30));
        }
      });
    }

    // Close buttons & backdrop clicks
    document.getElementById('panel-close-btn').addEventListener('click', () => this.closeSidePanel());
    document.getElementById('side-panel-backdrop').addEventListener('click', () => this.closeSidePanel());
    document.getElementById('terminal-close-btn').addEventListener('click', () => this.closeMonitor());

    // Mute toggle
    document.getElementById('sound-toggle').addEventListener('click', () => {
      this.isMuted = !this.isMuted;
      sound.muted = this.isMuted;
      document.getElementById('sound-toggle').textContent = this.isMuted ? '🔇 Audio Off' : '🔊 Audio On';
      this.showToast(this.isMuted ? 'Audio Muted' : 'Audio Enabled');
    });

    // ESC key to close any modal
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this.closeSidePanel();
        this.closeMonitor();
      }
    });
  }

  resize() {
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
    this.gl.viewport(0, 0, this.canvas.width, this.canvas.height);
    if (this.particles) this.particles.resize();
    this.updateHotspotsLayerPosition();
  }

  animate() {
    requestAnimationFrame(() => this.animate());

    // Smooth Lerp Mouse Offset
    this.mouse.x += (this.targetMouse.x - this.mouse.x) * 0.06;
    this.mouse.y += (this.targetMouse.y - this.mouse.y) * 0.06;

    // Smooth Lerp Zoom
    this.zoom += (this.targetZoom - this.zoom) * 0.08;
    this.zoomCenter.x += (this.targetZoomCenter.x - this.zoomCenter.x) * 0.08;
    this.zoomCenter.y += (this.targetZoomCenter.y - this.zoomCenter.y) * 0.08;

    // Pass to Shaders
    this.gl.uniform2f(this.uMouseLoc, this.mouse.x, this.mouse.y);
    this.gl.uniform1f(this.uZoomLoc, this.zoom);
    this.gl.uniform2f(this.uZoomCenterLoc, this.zoomCenter.x, this.zoomCenter.y);

    // Draw Quad
    this.gl.drawArrays(this.gl.TRIANGLES, 0, 6);

    // Update Particles
    if (this.particles) {
      this.particles.updateAndDraw(this.mouse);
    }
  }
}

window.addEventListener('DOMContentLoaded', () => {
  window.sound = sound;
  new SpatialRoom();
});
