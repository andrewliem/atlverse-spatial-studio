// Interactive Hotspots Configuration for Andrew Tanny Liem // Atlverse (atlverse.xyz)

export const HOTSPOTS = [
  {
    id: "portrait",
    title: "Andrew Tanny Liem // Profile",
    category: "Faculty & Researcher Profile",
    // Measured exact pixel bounds: x=31.0%, y=25.9%, w=7.8%, h=17.6%
    rect: { x: 31.0, y: 25.9, w: 7.8, h: 17.6 },
    action: "open_panel",
    panel: {
      tag: "ABOUT THE RESEARCHER",
      title: "Andrew Tanny Liem",
      content: `
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
      `
    }
  },
  {
    id: "publications_shelf",
    title: "Clean Futuristic Bookshelf // Research & Data Cubes",
    category: "Publications & Citations",
    // Measured exact pixel bounds: x=2.6%, y=13.0%, w=24.0%, h=75.9%
    rect: { x: 2.6, y: 13.0, w: 24.0, h: 75.9 },
    action: "open_panel",
    panel: {
      tag: "RESEARCH & PUBLICATIONS",
      title: "Publications & Scientific Research",
      content: `
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
      `
    }
  },
  {
    id: "diploma",
    title: "Universitas Klabat // Diploma",
    category: "Academic Credentials",
    // Measured exact bounds inside shelf: x=6.0%, y=46.3%, w=11.5%, h=14.4%
    rect: { x: 6.0, y: 46.3, w: 11.5, h: 14.4 },
    action: "open_panel",
    panel: {
      tag: "INSTITUTION",
      title: "Universitas Klabat (UNKLAB)",
      content: `
        <p>Faculty of Computer Science, Universitas Klabat, Airmadidi, North Sulawesi, Indonesia.</p>
        <div class="social-links">
          <a href="https://www.unklab.ac.id/" target="_blank" class="btn-social">🏛️ Universitas Klabat Website →</a>
        </div>
      `
    }
  },
  {
    id: "circuit_poster",
    title: "Neural Architecture & Blog",
    category: "Articles & Blog",
    // Measured exact bounds: x=42.4%, y=24.1%, w=17.2%, h=19.4%
    rect: { x: 42.4, y: 24.1, w: 17.2, h: 19.4 },
    action: "open_panel",
    panel: {
      tag: "BLOG & RESEARCH ESSAYS",
      title: "Atlverse Research Blog",
      content: `
        <p class="lead">Essays on fine-tuning models, building AI-native workflows, and academic computing.</p>
        
        <div class="social-links" style="margin-bottom: 20px;">
          <a href="https://blog.atlverse.xyz" target="_blank" class="btn-social">✍️ Read Blog (blog.atlverse.xyz) →</a>
        </div>

        <div class="card">
          <h4>LoRA Academic Writing Style Revision</h4>
          <p>Fine-tuning a QLoRA model to revise draft academic texts into dissertation-grade academic prose while maintaining strict semantic consistency.</p>
          <a href="https://blog.atlverse.xyz/blog/fine-tuning-lora-academic-writing-style/" target="_blank" style="color:var(--accent-cyan); font-size:12px; display:inline-block; margin-top:6px;">Read Article →</a>
        </div>
      `
    }
  },
  {
    id: "code_screens",
    title: "Floating AI Workstation // GitHub",
    category: "Code & Analytics",
    // Measured exact bounds: x=35.4%, y=44.9%, w=27.1%, h=18.1%
    rect: { x: 35.4, y: 44.9, w: 27.1, h: 18.1 },
    action: "zoom_monitor",
    description: "Click to explore GitHub repositories, prototypes, and research tools."
  },
  {
    id: "classroom_hud",
    title: "Classroom HUD // EdTech",
    category: "Classroom Systems",
    // Measured exact bounds: x=72.1%, y=31.9%, w=21.4%, h=28.2%
    rect: { x: 72.1, y: 31.9, w: 21.4, h: 28.2 },
    action: "open_panel",
    panel: {
      tag: "CLASSROOM & TEACHING",
      title: "Interactive Classroom Systems",
      content: `
        <p class="lead">Practical learning tools designed and tested against real teaching and learning problems at <strong>Universitas Klabat</strong>.</p>
        
        <div class="social-links" style="margin-bottom: 20px;">
          <a href="https://classroom.atlverse.xyz" target="_blank" class="btn-social">🎓 Open Classroom (classroom.atlverse.xyz) →</a>
        </div>

        <h3>Featured Teaching Frameworks</h3>
        <div class="card">
          <h4>AI-Native App Builder Skill Pack</h4>
          <p>A structured 13-step skill pack that teaches students to build software with AI without becoming superficial "vibe coders", using artifact-based learning and controlled implementation loops.</p>
        </div>
      `
    }
  },
  {
    id: "ai_bot",
    title: "AI Companion Drone",
    category: "Classroom AI",
    // Measured exact bounds: x=64.1%, y=40.3%, w=6.0%, h=9.7%
    rect: { x: 64.1, y: 40.3, w: 6.0, h: 9.7 },
    action: "pet_bot",
    description: "Click to interact with the AI assistant drone!"
  },
  {
    id: "contact_window",
    title: "Sunset City Skyline // Connect",
    category: "Social & Contact",
    rect: { x: 74.0, y: 64.0, w: 25.0, h: 25.0 },
    action: "open_panel",
    panel: {
      tag: "GET IN TOUCH",
      title: "Connect with Andrew Tanny Liem",
      content: `
        <p>Feel free to reach out for academic collaboration, research inquiries, or EdTech discussions:</p>
        <div class="social-links">
          <a href="https://github.com/andrewtliem" target="_blank" class="btn-social">🐙 GitHub (@andrewtliem)</a>
          <a href="https://www.linkedin.com/in/andrew-tanny-liem-4a463736/" target="_blank" class="btn-social">💼 LinkedIn Profile</a>
          <a href="https://scholar.google.com/citations?user=UZ-10RkAAAAJ" target="_blank" class="btn-social">📚 Google Scholar</a>
          <a href="https://orcid.org/0000-0002-7167-573X" target="_blank" class="btn-social">🆔 ORCID Profile</a>
          <a href="https://atlverse.xyz" target="_blank" class="btn-social">🌐 atlverse.xyz</a>
        </div>
      `
    }
  }
];

export const PROJECTS_DATA = [
  {
    title: "AI-Native App Builder Skill Pack",
    tech: "AI Education • Artifact Loops • Prompt Engineering",
    desc: "A structured 13-step skill pack teaching students to build software with AI using artifact-based learning and controlled implementation loops.",
    link: "https://github.com/andrewtliem/ai-native-app-builder-skills"
  },
  {
    title: "LoRA Academic Writing Style Revision",
    tech: "QLoRA • PyTorch • Fine-Tuning",
    desc: "Custom QLoRA model to revise draft academic texts into dissertation-grade academic prose while maintaining strict semantic consistency.",
    link: "https://blog.atlverse.xyz/blog/fine-tuning-lora-academic-writing-style/"
  },
  {
    title: "Intelligent Learning Systems (Classroom)",
    tech: "Web Applications • EdTech • Realtime Feedback",
    desc: "Classroom tools and study assistants tested in live CS courses at Universitas Klabat to reduce student learning friction.",
    link: "https://classroom.atlverse.xyz"
  },
  {
    title: "Intelligent Network Optimization Research",
    tech: "Applied AI • Distributed Systems • Networks",
    desc: "Research publications and experimental prototypes in intelligent network routing and systems optimization.",
    link: "https://scholar.google.com/citations?user=UZ-10RkAAAAJ"
  }
];
