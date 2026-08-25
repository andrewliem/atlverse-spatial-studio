// Zero-dependency Web Audio API Sound Effects Synthesizer

class SoundEngine {
  constructor() {
    this.ctx = null;
    this.muted = false;
  }

  init() {
    if (!this.ctx) {
      const AudioContext = window.AudioContext || window.webkitAudioContext;
      this.ctx = new AudioContext();
    }
    if (this.ctx.state === 'suspended') {
      this.ctx.resume();
    }
  }

  playHover() {
    if (this.muted) return;
    this.init();
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(580, now);
    osc.frequency.exponentialRampToValueAtTime(880, now + 0.06);

    gain.gain.setValueAtTime(0.04, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.06);

    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.start(now);
    osc.stop(now + 0.06);
  }

  playClick() {
    if (this.muted) return;
    this.init();
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc.type = 'triangle';
    osc.frequency.setValueAtTime(440, now);
    osc.frequency.exponentialRampToValueAtTime(220, now + 0.09);

    gain.gain.setValueAtTime(0.09, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.09);

    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.start(now);
    osc.stop(now + 0.09);
  }

  playTerminalKey() {
    if (this.muted) return;
    this.init();
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    const baseFreq = 800 + Math.random() * 400;
    osc.type = 'square';
    osc.frequency.setValueAtTime(baseFreq, now);

    gain.gain.setValueAtTime(0.02, now);
    gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.03);

    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.start(now);
    osc.stop(now + 0.03);
  }

  playSynthChord(chordIdx = 0) {
    if (this.muted) return;
    this.init();
    const now = this.ctx.currentTime;
    const chordFrequencies = [
      [261.63, 329.63, 392.00, 523.25], // C Major
      [293.66, 349.23, 440.00, 587.33], // D Minor
      [329.63, 392.00, 493.88, 659.25], // E Minor
      [349.23, 440.00, 523.25, 698.46], // F Major
      [392.00, 493.88, 587.33, 783.99]  // G Major
    ];

    const notes = chordFrequencies[chordIdx % chordFrequencies.length];
    notes.forEach((freq, i) => {
      const osc = this.ctx.createOscillator();
      const gain = this.ctx.createGain();

      osc.type = 'sawtooth';
      osc.frequency.setValueAtTime(freq, now + i * 0.04);

      gain.gain.setValueAtTime(0.03, now + i * 0.04);
      gain.gain.exponentialRampToValueAtTime(0.0001, now + 0.6 + i * 0.04);

      osc.connect(gain);
      gain.connect(this.ctx.destination);

      osc.start(now + i * 0.04);
      osc.stop(now + 0.7 + i * 0.04);
    });
  }

  playCatPurr() {
    if (this.muted) return;
    this.init();
    const now = this.ctx.currentTime;
    const osc = this.ctx.createOscillator();
    const gain = this.ctx.createGain();

    osc.type = 'sine';
    osc.frequency.setValueAtTime(650, now);
    osc.frequency.exponentialRampToValueAtTime(980, now + 0.15);
    osc.frequency.exponentialRampToValueAtTime(750, now + 0.35);

    gain.gain.setValueAtTime(0.06, now);
    gain.gain.exponentialRampToValueAtTime(0.001, now + 0.35);

    osc.connect(gain);
    gain.connect(this.ctx.destination);

    osc.start(now);
    osc.stop(now + 0.35);
  }
}

export const sound = new SoundEngine();
