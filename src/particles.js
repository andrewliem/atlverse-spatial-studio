// Ambient floating dust particles system in the sunbeam

export class ParticleSystem {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
    this.particles = [];
    this.numParticles = 55;
    this.init();
  }

  init() {
    this.resize();
    this.particles = [];
    for (let i = 0; i < this.numParticles; i++) {
      this.particles.push({
        x: Math.random() * this.canvas.width,
        y: Math.random() * this.canvas.height,
        radius: 0.8 + Math.random() * 2.2,
        vx: (Math.random() - 0.2) * 0.4,
        vy: 0.15 + Math.random() * 0.45,
        alpha: 0.2 + Math.random() * 0.6,
        pulseSpeed: 0.02 + Math.random() * 0.03,
        pulseVal: Math.random() * Math.PI * 2
      });
    }
  }

  resize() {
    this.canvas.width = window.innerWidth;
    this.canvas.height = window.innerHeight;
  }

  updateAndDraw(mouseOffset = { x: 0, y: 0 }) {
    this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);

    for (let p of this.particles) {
      p.x += p.vx + mouseOffset.x * 0.2;
      p.y += p.vy;
      p.pulseVal += p.pulseSpeed;

      // Wrap around bounds
      if (p.x < 0) p.x = this.canvas.width;
      if (p.x > this.canvas.width) p.x = 0;
      if (p.y > this.canvas.height) {
        p.y = 0;
        p.x = Math.random() * this.canvas.width;
      }

      const currentAlpha = p.alpha * (0.6 + 0.4 * Math.sin(p.pulseVal));

      this.ctx.beginPath();
      this.ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
      this.ctx.fillStyle = `rgba(255, 235, 175, ${currentAlpha})`;
      this.ctx.shadowColor = 'rgba(255, 220, 140, 0.8)';
      this.ctx.shadowBlur = 4;
      this.ctx.fill();
    }
  }
}
