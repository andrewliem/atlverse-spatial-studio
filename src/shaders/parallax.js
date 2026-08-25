export const vertexShaderSource = `
  attribute vec2 aPosition;
  varying vec2 vUv;
  void main() {
    vUv = vec2((aPosition.x + 1.0) * 0.5, 1.0 - (aPosition.y + 1.0) * 0.5);
    gl_Position = vec4(aPosition, 0.0, 1.0);
  }
`;

export const fragmentShaderSource = `
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
`;
