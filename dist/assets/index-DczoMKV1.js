(function(){const t=document.createElement("link").relList;if(t&&t.supports&&t.supports("modulepreload"))return;for(const i of document.querySelectorAll('link[rel="modulepreload"]'))o(i);new MutationObserver(i=>{for(const s of i)if(s.type==="childList")for(const n of s.addedNodes)n.tagName==="LINK"&&n.rel==="modulepreload"&&o(n)}).observe(document,{childList:!0,subtree:!0});function e(i){const s={};return i.integrity&&(s.integrity=i.integrity),i.referrerPolicy&&(s.referrerPolicy=i.referrerPolicy),i.crossOrigin==="use-credentials"?s.credentials="include":i.crossOrigin==="anonymous"?s.credentials="omit":s.credentials="same-origin",s}function o(i){if(i.ep)return;i.ep=!0;const s=e(i);fetch(i.href,s)}})();const m=`
  attribute vec2 aPosition;
  varying vec2 vUv;
  void main() {
    vUv = vec2((aPosition.x + 1.0) * 0.5, 1.0 - (aPosition.y + 1.0) * 0.5);
    gl_Position = vec4(aPosition, 0.0, 1.0);
  }
`,u=`
  precision highp float;
  uniform sampler2D uTexture;
  uniform sampler2D uDepthMap;
  uniform vec2 uMouse;
  uniform vec2 uThreshold;
  uniform float uZoom;
  uniform vec2 uZoomCenter;
  uniform vec2 uAspectCover; // (scaleX, scaleY)
  varying vec2 vUv;

  void main() {
    // 1. Aspect ratio cover transformation
    vec2 coverUv = (vUv - 0.5) * uAspectCover + 0.5;

    // 2. Zoom transformation around target focal point
    vec2 uv = (coverUv - uZoomCenter) / uZoom + uZoomCenter;
    
    if (uv.x < 0.0 || uv.x > 1.0 || uv.y < 0.0 || uv.y > 1.0) {
      gl_FragColor = vec4(0.06, 0.07, 0.11, 1.0);
      return;
    }

    // 3. Sample depth and apply subtle parallax displacement
    float depth = texture2D(uDepthMap, uv).r;
    vec2 displacement = vec2(uMouse.x, -uMouse.y) * uThreshold * (depth - 0.5);
    vec2 finalUv = clamp(uv + displacement, 0.0, 1.0);

    vec4 color = texture2D(uTexture, finalUv);

    // Subtle atmospheric vignette
    vec2 centerOffset = (vUv - 0.5) * 1.2;
    float vignette = 1.0 - dot(centerOffset, centerOffset) * 0.18;
    
    gl_FragColor = vec4(color.rgb * vignette, color.a);
  }
`;class p{constructor(t){this.canvas=t,this.ctx=t.getContext("2d"),this.particles=[],this.numParticles=55,this.init()}init(){this.resize(),this.particles=[];for(let t=0;t<this.numParticles;t++)this.particles.push({x:Math.random()*this.canvas.width,y:Math.random()*this.canvas.height,radius:.8+Math.random()*2.2,vx:(Math.random()-.2)*.4,vy:.15+Math.random()*.45,alpha:.2+Math.random()*.6,pulseSpeed:.02+Math.random()*.03,pulseVal:Math.random()*Math.PI*2})}resize(){this.canvas.width=window.innerWidth,this.canvas.height=window.innerHeight}updateAndDraw(t={x:0,y:0}){this.ctx.clearRect(0,0,this.canvas.width,this.canvas.height);for(let e of this.particles){e.x+=e.vx+t.x*.2,e.y+=e.vy,e.pulseVal+=e.pulseSpeed,e.x<0&&(e.x=this.canvas.width),e.x>this.canvas.width&&(e.x=0),e.y>this.canvas.height&&(e.y=0,e.x=Math.random()*this.canvas.width);const o=e.alpha*(.6+.4*Math.sin(e.pulseVal));this.ctx.beginPath(),this.ctx.arc(e.x,e.y,e.radius,0,Math.PI*2),this.ctx.fillStyle=`rgba(255, 235, 175, ${o})`,this.ctx.shadowColor="rgba(255, 220, 140, 0.8)",this.ctx.shadowBlur=4,this.ctx.fill()}}}class g{constructor(){this.ctx=null,this.muted=!1}init(){if(!this.ctx){const t=window.AudioContext||window.webkitAudioContext;this.ctx=new t}this.ctx.state==="suspended"&&this.ctx.resume()}playHover(){if(this.muted)return;this.init();const t=this.ctx.currentTime,e=this.ctx.createOscillator(),o=this.ctx.createGain();e.type="sine",e.frequency.setValueAtTime(580,t),e.frequency.exponentialRampToValueAtTime(880,t+.06),o.gain.setValueAtTime(.04,t),o.gain.exponentialRampToValueAtTime(.001,t+.06),e.connect(o),o.connect(this.ctx.destination),e.start(t),e.stop(t+.06)}playClick(){if(this.muted)return;this.init();const t=this.ctx.currentTime,e=this.ctx.createOscillator(),o=this.ctx.createGain();e.type="triangle",e.frequency.setValueAtTime(440,t),e.frequency.exponentialRampToValueAtTime(220,t+.09),o.gain.setValueAtTime(.09,t),o.gain.exponentialRampToValueAtTime(.001,t+.09),e.connect(o),o.connect(this.ctx.destination),e.start(t),e.stop(t+.09)}playTerminalKey(){if(this.muted)return;this.init();const t=this.ctx.currentTime,e=this.ctx.createOscillator(),o=this.ctx.createGain(),i=800+Math.random()*400;e.type="square",e.frequency.setValueAtTime(i,t),o.gain.setValueAtTime(.02,t),o.gain.exponentialRampToValueAtTime(1e-4,t+.03),e.connect(o),o.connect(this.ctx.destination),e.start(t),e.stop(t+.03)}playSynthChord(t=0){if(this.muted)return;this.init();const e=this.ctx.currentTime,o=[[261.63,329.63,392,523.25],[293.66,349.23,440,587.33],[329.63,392,493.88,659.25],[349.23,440,523.25,698.46],[392,493.88,587.33,783.99]];o[t%o.length].forEach((s,n)=>{const a=this.ctx.createOscillator(),r=this.ctx.createGain();a.type="sawtooth",a.frequency.setValueAtTime(s,e+n*.04),r.gain.setValueAtTime(.03,e+n*.04),r.gain.exponentialRampToValueAtTime(1e-4,e+.6+n*.04),a.connect(r),r.connect(this.ctx.destination),a.start(e+n*.04),a.stop(e+.7+n*.04)})}playCatPurr(){if(this.muted)return;this.init();const t=this.ctx.currentTime,e=this.ctx.createOscillator(),o=this.ctx.createGain();e.type="sine",e.frequency.setValueAtTime(650,t),e.frequency.exponentialRampToValueAtTime(980,t+.15),e.frequency.exponentialRampToValueAtTime(750,t+.35),o.gain.setValueAtTime(.06,t),o.gain.exponentialRampToValueAtTime(.001,t+.35),e.connect(o),o.connect(this.ctx.destination),e.start(t),e.stop(t+.35)}}const c=new g,f=[{id:"portrait",title:"Andrew Tanny Liem // Profile",category:"Faculty & Researcher Profile",rect:{x:31,y:25.9,w:7.8,h:17.6},action:"open_panel",panel:{tag:"ABOUT THE RESEARCHER",title:"Andrew Tanny Liem",content:`
        <p class="lead">Computer Science Lecturer & AI / EdTech Systems Researcher at <strong>Universitas Klabat</strong>.</p>
        
        <p>I work at the intersection of teaching, research, and software development — with a focus on tools that reduce learning friction.</p>

        <p><strong>Atlverse</strong> is my personal research-and-build space, where papers become prototypes, prototypes become tools, and tools return to real classrooms.</p>

        <blockquote style="margin: 16px 0; padding-left: 12px; border-left: 3px solid var(--accent-cyan); color: #fff; font-style: italic;">
          "The true object of education is to restore the image of God in the soul."<br>
          <span style="font-size: 12px; color: var(--text-dim);">— Ellen G. White</span>
        </blockquote>

        <div class="social-links">
          <a href="https://scholar.google.com/citations?user=UZ-10RkAAAAJ" target="_blank" class="btn-social">📚 Google Scholar Profile →</a>
          <a href="https://blog.atlverse.xyz" target="_blank" class="btn-social">✍️ Read Blog (blog.atlverse.xyz) →</a>
          <a href="https://classroom.atlverse.xyz" target="_blank" class="btn-social">🎓 Open Classroom (classroom.atlverse.xyz) →</a>
        </div>
      `}},{id:"publications_shelf",title:"Clean Futuristic Bookshelf // Research & Data Cubes",category:"Publications & Citations",rect:{x:2.6,y:13,w:24,h:75.9},action:"open_panel",panel:{tag:"RESEARCH & PUBLICATIONS",title:"Publications & Scientific Research",content:`
        <p class="lead">Selected research publications by <strong>Andrew Tanny Liem</strong> connecting AI, intelligent networks, and education-focused systems.</p>
        
        <div class="social-links" style="margin-bottom: 20px;">
          <a href="https://scholar.google.com/citations?user=UZ-10RkAAAAJ" target="_blank" class="btn-social">📚 Google Scholar Profile →</a>
          <a href="https://orcid.org/0000-0002-7167-573X" target="_blank" class="btn-social">🆔 ORCID: 0000-0002-7167-573X →</a>
        </div>

        <h3>Research Domains</h3>
        <div class="card-grid">
          <div class="card">
            <h4>🤖 AI Learning Systems</h4>
            <p>Study assistants, automated feedback architectures, and classroom-ready academic tools.</p>
          </div>
          <div class="card">
            <h4>📡 Intelligent Networks</h4>
            <p>Network optimization, distributed intelligence, and applied computing research.</p>
          </div>
          <div class="card">
            <h4>⚡ Academic Productivity</h4>
            <p>Translating academic papers into functioning software prototypes tested in real classrooms.</p>
          </div>
        </div>
      `}},{id:"diploma",title:"Universitas Klabat // Diploma",category:"Academic Credentials",rect:{x:6,y:46.3,w:11.5,h:14.4},action:"open_panel",panel:{tag:"INSTITUTION",title:"Universitas Klabat (UNKLAB)",content:`
        <p>Faculty of Computer Science, Universitas Klabat, Airmadidi, North Sulawesi, Indonesia.</p>
        <div class="social-links">
          <a href="https://www.unklab.ac.id/" target="_blank" class="btn-social">🏛️ Universitas Klabat Website →</a>
        </div>
      `}},{id:"circuit_poster",title:"Neural Architecture & Blog",category:"Articles & Blog",rect:{x:42.4,y:24.1,w:17.2,h:19.4},action:"open_panel",panel:{tag:"BLOG & RESEARCH ESSAYS",title:"Atlverse Research Blog",content:`
        <p class="lead">Essays on fine-tuning models, building AI-native workflows, and academic computing.</p>
        
        <div class="social-links" style="margin-bottom: 20px;">
          <a href="https://blog.atlverse.xyz" target="_blank" class="btn-social">✍️ Read Blog (blog.atlverse.xyz) →</a>
        </div>

        <div class="card">
          <h4>LoRA Academic Writing Style Revision</h4>
          <p>Fine-tuning a QLoRA model to revise draft academic texts into dissertation-grade academic prose while maintaining strict semantic consistency.</p>
          <a href="https://blog.atlverse.xyz/blog/fine-tuning-lora-academic-writing-style/" target="_blank" style="color:var(--accent-cyan); font-size:12px; display:inline-block; margin-top:6px;">Read Article →</a>
        </div>
      `}},{id:"code_screens",title:"Floating AI Workstation // GitHub",category:"Code & Analytics",rect:{x:35.4,y:44.9,w:27.1,h:18.1},action:"zoom_monitor",description:"Click to explore GitHub repositories, prototypes, and research tools."},{id:"classroom_hud",title:"Classroom HUD // EdTech",category:"Classroom Systems",rect:{x:72.1,y:31.9,w:21.4,h:28.2},action:"open_panel",panel:{tag:"CLASSROOM & TEACHING",title:"Interactive Classroom Systems",content:`
        <p class="lead">Practical learning tools designed and tested against real teaching and learning problems at <strong>Universitas Klabat</strong>.</p>
        
        <div class="social-links" style="margin-bottom: 20px;">
          <a href="https://classroom.atlverse.xyz" target="_blank" class="btn-social">🎓 Open Classroom (classroom.atlverse.xyz) →</a>
        </div>

        <h3>Featured Teaching Frameworks</h3>
        <div class="card">
          <h4>AI-Native App Builder Skill Pack</h4>
          <p>A structured 13-step skill pack that teaches students to build software with AI without becoming superficial "vibe coders", using artifact-based learning and controlled implementation loops.</p>
        </div>
      `}},{id:"ai_bot",title:"AI Companion Drone",category:"Classroom AI",rect:{x:64.1,y:40.3,w:6,h:9.7},action:"pet_bot",description:"Click to interact with the AI assistant drone!"},{id:"contact_window",title:"Sunset City Skyline // Connect",category:"Social & Contact",rect:{x:74,y:64,w:25,h:25},action:"open_panel",panel:{tag:"GET IN TOUCH",title:"Connect with Andrew Tanny Liem",content:`
        <p>Feel free to reach out for academic collaboration, research inquiries, or EdTech discussions:</p>
        <div class="social-links">
          <a href="https://github.com/andrewtliem" target="_blank" class="btn-social">🐙 GitHub (@andrewtliem)</a>
          <a href="https://www.linkedin.com/in/andrew-tanny-liem-4a463736/" target="_blank" class="btn-social">💼 LinkedIn Profile</a>
          <a href="https://scholar.google.com/citations?user=UZ-10RkAAAAJ" target="_blank" class="btn-social">📚 Google Scholar</a>
          <a href="https://orcid.org/0000-0002-7167-573X" target="_blank" class="btn-social">🆔 ORCID Profile</a>
          <a href="https://atlverse.xyz" target="_blank" class="btn-social">🌐 atlverse.xyz</a>
        </div>
      `}}],y=[{title:"AI-Native App Builder Skill Pack",tech:"AI Education • Artifact Loops • Prompt Engineering",desc:"A structured 13-step skill pack teaching students to build software with AI using artifact-based learning and controlled implementation loops.",link:"https://github.com/andrewtliem/ai-native-app-builder-skills"},{title:"LoRA Academic Writing Style Revision",tech:"QLoRA • PyTorch • Fine-Tuning",desc:"Custom QLoRA model to revise draft academic texts into dissertation-grade academic prose while maintaining strict semantic consistency.",link:"https://blog.atlverse.xyz/blog/fine-tuning-lora-academic-writing-style/"},{title:"Intelligent Learning Systems (Classroom)",tech:"Web Applications • EdTech • Realtime Feedback",desc:"Classroom tools and study assistants tested in live CS courses at Universitas Klabat to reduce student learning friction.",link:"https://classroom.atlverse.xyz"},{title:"Intelligent Network Optimization Research",tech:"Applied AI • Distributed Systems • Networks",desc:"Research publications and experimental prototypes in intelligent network routing and systems optimization.",link:"https://scholar.google.com/citations?user=UZ-10RkAAAAJ"}],v=""+new URL("studio-D4gxOVAB.png",import.meta.url).href,x=""+new URL("depth-aFB_VLSN.png",import.meta.url).href;class T{constructor(){if(this.canvas=document.getElementById("webgl-canvas"),this.gl=this.canvas.getContext("webgl")||this.canvas.getContext("experimental-webgl"),!this.gl){alert("WebGL not supported in your browser.");return}this.mouse={x:0,y:0},this.targetMouse={x:0,y:0},this.zoom=1,this.targetZoom=1,this.zoomCenter={x:.5,y:.5},this.targetZoomCenter={x:.5,y:.5},this.synthChordIndex=0,this.isMuted=!1,this.initWebGL(),this.initParticles(),this.initHotspots(),this.initEvents(),this.initTerminal(),this.animate()}initWebGL(){const t=this.gl,e=t.createShader(t.VERTEX_SHADER);t.shaderSource(e,m),t.compileShader(e);const o=t.createShader(t.FRAGMENT_SHADER);t.shaderSource(o,u),t.compileShader(o);const i=t.createProgram();t.attachShader(i,e),t.attachShader(i,o),t.linkProgram(i),t.useProgram(i),this.program=i;const s=t.createBuffer();t.bindBuffer(t.ARRAY_BUFFER,s);const n=new Float32Array([-1,-1,1,-1,-1,1,-1,1,1,-1,1,1]);t.bufferData(t.ARRAY_BUFFER,n,t.STATIC_DRAW);const a=t.getAttribLocation(i,"aPosition");t.enableVertexAttribArray(a),t.vertexAttribPointer(a,2,t.FLOAT,!1,0,0),this.uMouseLoc=t.getUniformLocation(i,"uMouse"),this.uThresholdLoc=t.getUniformLocation(i,"uThreshold"),this.uZoomLoc=t.getUniformLocation(i,"uZoom"),this.uZoomCenterLoc=t.getUniformLocation(i,"uZoomCenter"),this.uAspectCoverLoc=t.getUniformLocation(i,"uAspectCover"),this.uTextureLoc=t.getUniformLocation(i,"uTexture"),this.uDepthMapLoc=t.getUniformLocation(i,"uDepthMap"),t.uniform2f(this.uThresholdLoc,.018,.018),t.uniform1f(this.uZoomLoc,1),t.uniform2f(this.uZoomCenterLoc,.5,.5),this.colorTexture=this.loadTexture(v,0,this.uTextureLoc),this.depthTexture=this.loadTexture(x,1,this.uDepthMapLoc),this.resize()}loadTexture(t,e,o){const i=this.gl,s=i.createTexture();i.activeTexture(i.TEXTURE0+e),i.bindTexture(i.TEXTURE_2D,s),i.texImage2D(i.TEXTURE_2D,0,i.RGBA,1,1,0,i.RGBA,i.UNSIGNED_BYTE,new Uint8Array([20,20,30,255]));const n=new Image;return n.crossOrigin="anonymous",n.src=t,n.onload=()=>{i.activeTexture(i.TEXTURE0+e),i.bindTexture(i.TEXTURE_2D,s),i.texImage2D(i.TEXTURE_2D,0,i.RGBA,i.RGBA,i.UNSIGNED_BYTE,n),i.texParameteri(i.TEXTURE_2D,i.TEXTURE_WRAP_S,i.CLAMP_TO_EDGE),i.texParameteri(i.TEXTURE_2D,i.TEXTURE_WRAP_T,i.CLAMP_TO_EDGE),i.texParameteri(i.TEXTURE_2D,i.TEXTURE_MIN_FILTER,i.LINEAR),i.texParameteri(i.TEXTURE_2D,i.TEXTURE_MAG_FILTER,i.LINEAR),i.uniform1i(o,e)},s}initParticles(){const t=document.getElementById("particles-canvas");this.particles=new p(t)}getRenderBounds(){const t=window.innerWidth,e=window.innerHeight,o=1920/1080,i=t/e;let s,n,a,r,d,h;return i>o?(s=t,n=t/o,a=0,r=(e-n)/2,d=1,h=o/i):(n=e,s=e*o,a=(t-s)/2,r=0,d=i/o,h=1),{renderW:s,renderH:n,offsetX:a,offsetY:r,scaleX:d,scaleY:h}}updateHotspotsLayerPosition(){const t=this.getRenderBounds(),e=document.getElementById("hotspots-layer");e&&(e.style.position="fixed",e.style.left=`${t.offsetX}px`,e.style.top=`${t.offsetY}px`,e.style.width=`${t.renderW}px`,e.style.height=`${t.renderH}px`,this.gl&&this.uAspectCoverLoc&&this.gl.uniform2f(this.uAspectCoverLoc,t.scaleX,t.scaleY))}initHotspots(){const t=document.getElementById("hotspots-layer");t.innerHTML="",f.forEach(e=>{const o=document.createElement("div");o.className="hotspot-box",o.dataset.id=e.id,o.style.left=`${e.rect.x}%`,o.style.top=`${e.rect.y}%`,o.style.width=`${e.rect.w}%`,o.style.height=`${e.rect.h}%`,o.addEventListener("mouseenter",i=>{c.playHover(),this.showTooltip(e,i)}),o.addEventListener("mousemove",i=>{this.positionTooltip(i)}),o.addEventListener("mouseleave",()=>{this.hideTooltip()}),o.addEventListener("click",()=>{c.playClick(),this.handleHotspotClick(e)}),t.appendChild(o)}),this.updateHotspotsLayerPosition()}showTooltip(t,e){const o=document.getElementById("tooltip");o.innerHTML=`
      <span class="tooltip-tag">${t.category}</span>
      <span class="tooltip-title">${t.title}</span>
    `,o.classList.add("active"),this.positionTooltip(e)}positionTooltip(t){const e=document.getElementById("tooltip");if(!e.classList.contains("active"))return;const o=e.offsetWidth||220,i=e.offsetHeight||44;let s=t.clientX,n=t.clientY-16;n-i<65?(n=t.clientY+22,e.style.transform="translate(-50%, 0)"):e.style.transform="translate(-50%, -100%)";const a=20,r=o/2;s-r<a?s=r+a:s+r>window.innerWidth-a&&(s=window.innerWidth-r-a),e.style.left=`${s}px`,e.style.top=`${n}px`}hideTooltip(){document.getElementById("tooltip").classList.remove("active")}handleHotspotClick(t){t.action==="zoom_monitor"?this.openMonitor():t.action==="open_panel"?this.openSidePanel(t.panel):t.action==="pet_bot"&&(c.playHover(),this.showToast('🤖 AI Study Bot: "Systems online. Ready for research!"'))}openSidePanel(t){const e=document.getElementById("side-panel"),o=document.getElementById("side-panel-backdrop");document.getElementById("panel-tag").textContent=t.tag,document.getElementById("panel-title").textContent=t.title,document.getElementById("panel-body").innerHTML=t.content,e.classList.add("active"),o.classList.add("active")}closeSidePanel(){document.getElementById("side-panel").classList.remove("active"),document.getElementById("side-panel-backdrop").classList.remove("active")}openMonitor(){document.getElementById("monitor-modal").classList.add("active"),this.targetZoom=1.35,this.targetZoomCenter={x:.48,y:.52}}closeMonitor(){document.getElementById("monitor-modal").classList.remove("active"),this.targetZoom=1,this.targetZoomCenter={x:.5,y:.5}}initTerminal(){const t=document.getElementById("projects-container");t.innerHTML=y.map(e=>`
      <div class="project-card" onclick="window.sound && window.sound.playTerminalKey()">
        <h4>${e.title}</h4>
        <div class="project-tech">${e.tech}</div>
        <p>${e.desc}</p>
      </div>
    `).join("")}showToast(t){const e=document.getElementById("toast");e.textContent=t,e.classList.add("active"),clearTimeout(this.toastTimer),this.toastTimer=setTimeout(()=>e.classList.remove("active"),2500)}initEvents(){window.addEventListener("resize",()=>{this.resize(),this.updateHotspotsLayerPosition()}),window.addEventListener("mousemove",t=>{this.targetMouse.x=(t.clientX/window.innerWidth-.5)*2,this.targetMouse.y=(t.clientY/window.innerHeight-.5)*2}),window.DeviceOrientationEvent&&window.addEventListener("deviceorientation",t=>{t.gamma!==null&&t.beta!==null&&(this.targetMouse.x=Math.max(-1,Math.min(1,t.gamma/30)),this.targetMouse.y=Math.max(-1,Math.min(1,(t.beta-45)/30)))}),document.getElementById("panel-close-btn").addEventListener("click",()=>this.closeSidePanel()),document.getElementById("side-panel-backdrop").addEventListener("click",()=>this.closeSidePanel()),document.getElementById("terminal-close-btn").addEventListener("click",()=>this.closeMonitor()),document.getElementById("sound-toggle").addEventListener("click",()=>{this.isMuted=!this.isMuted,c.muted=this.isMuted,document.getElementById("sound-toggle").textContent=this.isMuted?"🔇 Audio Off":"🔊 Audio On",this.showToast(this.isMuted?"Audio Muted":"Audio Enabled")}),window.addEventListener("keydown",t=>{t.key==="Escape"&&(this.closeSidePanel(),this.closeMonitor())})}resize(){this.canvas.width=window.innerWidth,this.canvas.height=window.innerHeight,this.gl.viewport(0,0,this.canvas.width,this.canvas.height),this.particles&&this.particles.resize(),this.updateHotspotsLayerPosition()}animate(){requestAnimationFrame(()=>this.animate()),this.mouse.x+=(this.targetMouse.x-this.mouse.x)*.06,this.mouse.y+=(this.targetMouse.y-this.mouse.y)*.06,this.zoom+=(this.targetZoom-this.zoom)*.08,this.zoomCenter.x+=(this.targetZoomCenter.x-this.zoomCenter.x)*.08,this.zoomCenter.y+=(this.targetZoomCenter.y-this.zoomCenter.y)*.08,this.gl.uniform2f(this.uMouseLoc,this.mouse.x,this.mouse.y),this.gl.uniform1f(this.uZoomLoc,this.zoom),this.gl.uniform2f(this.uZoomCenterLoc,this.zoomCenter.x,this.zoomCenter.y),this.gl.drawArrays(this.gl.TRIANGLES,0,6),this.particles&&this.particles.updateAndDraw(this.mouse)}}window.addEventListener("DOMContentLoaded",()=>{window.sound=c,new T});
