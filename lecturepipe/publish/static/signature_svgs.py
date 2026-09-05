"""One hand-authored inline-SVG "signature diagram" per chapter -- not a
per-lecture or per-claim illustration, but the single most central mechanism
of that chapter, drawn as a real diagram rather than a labeled box. Follows
the artifact-diagramming conventions: sized by viewBox, themed via currentColor
(so it reads correctly in both light and dark without any JS), arrowheads as
<marker> defs, short on-diagram labels with the fuller explanation left to the
<figcaption>. Self-contained (no <script>/<style>/<foreignObject> inside the
<svg>, no external references) so it can be pasted verbatim into the page.

Keyed by chapter_id ("leph101".."leph108"); html.py looks up its own chapter's
entry and wraps it in a <figure> with role="img" + aria-label.
"""
from __future__ import annotations

SIGNATURE_SVGS: dict[str, dict[str, str]] = {
    "leph101": {
        "caption": "An electric dipole: two equal, opposite charges +q and −q "
                    "separated by 2a, and the field lines running from + to − "
                    "that give the dipole its field pattern.",
        "svg": """
<svg viewBox="0 0 480 220" role="img" aria-label="Electric dipole: charges +q and -q separated by distance 2a, with curved field lines running from the positive to the negative charge, and the dipole moment vector p pointing from -q to +q.">
  <defs>
    <marker id="d101-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 Z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="70" y1="110" x2="410" y2="110" stroke="currentColor" stroke-width="1.5" stroke-dasharray="3 4" opacity="0.5"/>
  <path d="M 130 110 C 160 60, 220 60, 250 110" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#d101-arrow)" opacity="0.85"/>
  <path d="M 130 110 C 160 160, 220 160, 250 110" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#d101-arrow)" opacity="0.85"/>
  <path d="M 100 110 C 150 30, 260 30, 320 90" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#d101-arrow)" opacity="0.6"/>
  <path d="M 100 110 C 150 190, 260 190, 320 130" fill="none" stroke="currentColor" stroke-width="1.3" marker-end="url(#d101-arrow)" opacity="0.6"/>
  <circle cx="130" cy="110" r="16" fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="130" y="116" text-anchor="middle" font-size="16" font-weight="600" fill="currentColor">+q</text>
  <circle cx="250" cy="110" r="16" fill="none" stroke="currentColor" stroke-width="2"/>
  <line x1="243" y1="110" x2="257" y2="110" stroke="currentColor" stroke-width="2.5"/>
  <text x="250" y="145" text-anchor="middle" font-size="13" fill="currentColor">−q</text>
  <line x1="130" y1="70" x2="250" y2="70" stroke="currentColor" stroke-width="1" marker-end="url(#d101-arrow)"/>
  <text x="190" y="58" text-anchor="middle" font-size="13" fill="currentColor">2a</text>
  <line x1="250" y1="110" x2="370" y2="110" stroke="currentColor" stroke-width="2" marker-end="url(#d101-arrow)"/>
  <text x="345" y="100" text-anchor="middle" font-size="14" font-style="italic" fill="currentColor">p</text>
</svg>
""",
    },
    "leph102": {
        "caption": "Parallel-plate capacitor: a uniform field E between two "
                    "oppositely charged plates of separation d, giving V = Ed.",
        "svg": """
<svg viewBox="0 0 420 220" role="img" aria-label="Parallel plate capacitor cross-section: two plates separated by distance d with a uniform electric field E pointing from the positive plate to the negative plate, and potential difference V = E times d.">
  <defs>
    <marker id="d102-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 Z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="120" y1="30" x2="120" y2="190" stroke="currentColor" stroke-width="4"/>
  <line x1="300" y1="30" x2="300" y2="190" stroke="currentColor" stroke-width="4"/>
  <text x="120" y="20" text-anchor="middle" font-size="13" font-weight="600" fill="currentColor">+ + + +</text>
  <text x="300" y="20" text-anchor="middle" font-size="13" font-weight="600" fill="currentColor">− − − −</text>
  <g opacity="0.85">
    <line x1="150" y1="65" x2="270" y2="65" stroke="currentColor" stroke-width="1.4" marker-end="url(#d102-arrow)"/>
    <line x1="150" y1="95" x2="270" y2="95" stroke="currentColor" stroke-width="1.4" marker-end="url(#d102-arrow)"/>
    <line x1="150" y1="125" x2="270" y2="125" stroke="currentColor" stroke-width="1.4" marker-end="url(#d102-arrow)"/>
    <line x1="150" y1="155" x2="270" y2="155" stroke="currentColor" stroke-width="1.4" marker-end="url(#d102-arrow)"/>
  </g>
  <text x="210" y="82" text-anchor="middle" font-size="14" font-style="italic" fill="currentColor">E</text>
  <line x1="120" y1="205" x2="300" y2="205" stroke="currentColor" stroke-width="1" marker-end="url(#d102-arrow)"/>
  <text x="210" y="220" text-anchor="middle" font-size="13" fill="currentColor">d</text>
  <text x="360" y="115" text-anchor="middle" font-size="14" fill="currentColor">V = Ed</text>
</svg>
""",
    },
    "leph103": {
        "caption": "The Wheatstone bridge: four resistors P, Q, R, S with a "
                    "galvanometer across the bridge, balanced when P/Q = R/S "
                    "(zero galvanometer deflection).",
        "svg": """
<svg viewBox="0 0 420 260" role="img" aria-label="Wheatstone bridge circuit: resistors P, Q, R, S arranged in a diamond with a galvanometer G across the bridge and a cell driving current through the whole network, balanced when P/Q equals R/S.">
  <polygon points="210,30 340,130 210,230 80,130" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <line x1="210" y1="30" x2="340" y2="130" stroke="currentColor" stroke-width="1.6"/>
  <text x="290" y="72" text-anchor="middle" font-size="14" fill="currentColor">P</text>
  <line x1="340" y1="130" x2="210" y2="230" stroke="currentColor" stroke-width="1.6"/>
  <text x="290" y="192" text-anchor="middle" font-size="14" fill="currentColor">Q</text>
  <line x1="210" y1="230" x2="80" y2="130" stroke="currentColor" stroke-width="1.6"/>
  <text x="130" y="192" text-anchor="middle" font-size="14" fill="currentColor">R</text>
  <line x1="80" y1="130" x2="210" y2="30" stroke="currentColor" stroke-width="1.6"/>
  <text x="130" y="72" text-anchor="middle" font-size="14" fill="currentColor">S</text>
  <line x1="210" y1="30" x2="210" y2="230" stroke="currentColor" stroke-width="1.4" stroke-dasharray="4 3" opacity="0.85"/>
  <circle cx="210" cy="130" r="18" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <text x="210" y="135" text-anchor="middle" font-size="13" fill="currentColor">G</text>
  <line x1="80" y1="130" x2="30" y2="130" stroke="currentColor" stroke-width="1.4"/>
  <line x1="340" y1="130" x2="390" y2="130" stroke="currentColor" stroke-width="1.4"/>
  <path d="M30,130 L30,190 L390,190 L390,130" fill="none" stroke="currentColor" stroke-width="1.4"/>
  <line x1="195" y1="185" x2="225" y2="185" stroke="currentColor" stroke-width="3"/>
  <line x1="202" y1="195" x2="218" y2="195" stroke="currentColor" stroke-width="1.6"/>
  <text x="210" y="250" text-anchor="middle" font-size="13" fill="currentColor">balanced: P/Q = R/S</text>
</svg>
""",
    },
    "leph104": {
        "caption": "Cyclotron: a charged particle spirals outward through two "
                    "dees under a magnetic field into the page, gaining energy "
                    "each time it crosses the gap between them.",
        "svg": """
<svg viewBox="0 0 420 260" role="img" aria-label="Cyclotron schematic: two D-shaped dees with a gap between them, a uniform magnetic field into the page marked with crosses, and a charged particle's spiral path growing in radius each half-turn.">
  <path d="M 210 40 A 90 90 0 0 0 210 220 L 210 190 A 60 60 0 0 1 210 70 Z" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <path d="M 220 40 A 90 90 0 0 1 220 220 L 220 190 A 60 60 0 0 0 220 70 Z" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <g stroke="currentColor" stroke-width="1.2" opacity="0.5">
    <line x1="130" y1="70" x2="140" y2="80"/><line x1="140" y1="70" x2="130" y2="80"/>
    <line x1="170" y1="60" x2="180" y2="70"/><line x1="180" y1="60" x2="170" y2="70"/>
    <line x1="130" y1="180" x2="140" y2="190"/><line x1="140" y1="180" x2="130" y2="190"/>
    <line x1="290" y1="70" x2="300" y2="80"/><line x1="300" y1="70" x2="290" y2="80"/>
    <line x1="250" y1="60" x2="260" y2="70"/><line x1="260" y1="60" x2="250" y2="70"/>
    <line x1="290" y1="180" x2="300" y2="190"/><line x1="300" y1="180" x2="290" y2="190"/>
  </g>
  <path d="M 215 130 A 8 8 0 1 1 215 130.1" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M 215 130 A 20 20 0 1 1 215 130.1" fill="none" stroke="currentColor" stroke-width="1.8" transform="rotate(70 215 130)"/>
  <path d="M 215 130 A 34 34 0 1 1 215 130.1" fill="none" stroke="currentColor" stroke-width="1.8" transform="rotate(150 215 130)"/>
  <path d="M 215 130 A 50 50 0 0 1 215 129.9" fill="none" stroke="currentColor" stroke-width="1.8" transform="rotate(240 215 130)" marker-end="url(#d104-arrow)"/>
  <defs>
    <marker id="d104-arrow" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 Z" fill="currentColor"/>
    </marker>
  </defs>
  <text x="150" y="130" text-anchor="middle" font-size="14" fill="currentColor">D₁</text>
  <text x="280" y="130" text-anchor="middle" font-size="14" fill="currentColor">D₂</text>
  <text x="210" y="245" text-anchor="middle" font-size="13" fill="currentColor">B into page, ω = Bq/m constant</text>
</svg>
""",
    },
    "leph105": {
        "caption": "Hysteresis loop: B lags H through a full magnetisation "
                    "cycle -- OA is the saturation path, OB is retentivity, "
                    "OC is coercivity.",
        "svg": """
<svg viewBox="0 0 420 260" role="img" aria-label="Hysteresis loop: a B versus H curve, starting at the origin, rising to saturation at point A, retaining a non-zero B at H=0 (point B, retentivity), crossing zero B at a negative H (point C, coercivity), reaching negative saturation at D, and closing back through E, F to A.">
  <line x1="40" y1="130" x2="390" y2="130" stroke="currentColor" stroke-width="1.2" marker-end="url(#d105-arrow)"/>
  <line x1="210" y1="240" x2="210" y2="20" stroke="currentColor" stroke-width="1.2" marker-end="url(#d105-arrow)"/>
  <text x="385" y="122" font-size="13" fill="currentColor">H</text>
  <text x="218" y="28" font-size="13" fill="currentColor">B</text>
  <defs>
    <marker id="d105-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 Z" fill="currentColor"/>
    </marker>
  </defs>
  <path d="M 210 130 C 250 100, 280 50, 320 45" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M 320 45 C 280 60, 240 65, 210 70" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M 210 70 C 170 78, 130 100, 105 130" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M 105 130 C 130 165, 160 210, 100 215" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M 100 215 C 130 200, 170 190, 210 190" fill="none" stroke="currentColor" stroke-width="2"/>
  <path d="M 210 190 C 250 182, 285 165, 315 130" fill="none" stroke="currentColor" stroke-width="2" marker-end="url(#d105-arrow)"/>
  <circle cx="320" cy="45" r="3.5" fill="currentColor"/><text x="330" y="42" font-size="13" fill="currentColor">A</text>
  <circle cx="210" cy="70" r="3.5" fill="currentColor"/><text x="218" y="65" font-size="13" fill="currentColor">B</text>
  <circle cx="105" cy="130" r="3.5" fill="currentColor"/><text x="70" y="128" font-size="13" fill="currentColor">C</text>
  <circle cx="100" cy="215" r="3.5" fill="currentColor"/><text x="65" y="222" font-size="13" fill="currentColor">D</text>
  <circle cx="210" cy="190" r="3.5" fill="currentColor"/><text x="218" y="205" font-size="13" fill="currentColor">E</text>
  <text x="210" y="250" text-anchor="middle" font-size="12" fill="currentColor">OB = retentivity, OC = coercivity</text>
</svg>
""",
    },
    "leph106": {
        "caption": "Lenz's law: a bar magnet moved toward a coil induces a "
                    "current whose magnetic field opposes the increasing flux -- "
                    "the induced field points to repel the approaching magnet.",
        "svg": """
<svg viewBox="0 0 440 220" role="img" aria-label="Bar magnet with north pole approaching a wound coil connected to a galvanometer. The increasing flux through the coil induces a current, shown circulating in the coil, whose own magnetic field opposes the magnet's approach by presenting a north pole toward it.">
  <rect x="30" y="90" width="70" height="34" fill="none" stroke="currentColor" stroke-width="1.8"/>
  <line x1="65" y1="90" x2="65" y2="124" stroke="currentColor" stroke-width="1.8"/>
  <text x="47" y="112" text-anchor="middle" font-size="15" font-weight="600" fill="currentColor">N</text>
  <text x="83" y="112" text-anchor="middle" font-size="15" font-weight="600" fill="currentColor">S</text>
  <line x1="100" y1="107" x2="170" y2="107" stroke="currentColor" stroke-width="1.6" marker-end="url(#d106-arrow)"/>
  <text x="135" y="98" text-anchor="middle" font-size="12" fill="currentColor">v</text>
  <defs>
    <marker id="d106-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 Z" fill="currentColor"/>
    </marker>
    <marker id="d106-arrow-sm" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 Z" fill="currentColor"/>
    </marker>
  </defs>
  <g stroke="currentColor" stroke-width="2" fill="none">
    <ellipse cx="255" cy="107" rx="18" ry="55"/>
    <ellipse cx="285" cy="107" rx="18" ry="55"/>
    <ellipse cx="315" cy="107" rx="18" ry="55"/>
  </g>
  <path d="M 300 60 A 18 12 0 0 1 330 60" fill="none" stroke="currentColor" stroke-width="1.8" marker-end="url(#d106-arrow-sm)"/>
  <text x="320" y="45" text-anchor="middle" font-size="13" font-weight="600" fill="currentColor">N</text>
  <line x1="315" y1="162" x2="315" y2="195" stroke="currentColor" stroke-width="1.4"/>
  <line x1="255" y1="162" x2="255" y2="195" stroke="currentColor" stroke-width="1.4"/>
  <line x1="255" y1="195" x2="380" y2="195" stroke="currentColor" stroke-width="1.4"/>
  <line x1="315" y1="195" x2="380" y2="195" stroke="currentColor" stroke-width="1.4" opacity="0"/>
  <circle cx="380" cy="160" r="20" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <text x="380" y="165" text-anchor="middle" font-size="13" fill="currentColor">G</text>
  <line x1="380" y1="195" x2="380" y2="180" stroke="currentColor" stroke-width="1.4"/>
  <line x1="380" y1="140" x2="380" y2="107" stroke="currentColor" stroke-width="1.4"/>
  <line x1="380" y1="107" x2="333" y2="107" stroke="currentColor" stroke-width="1.4"/>
  <text x="255" y="215" text-anchor="middle" font-size="12" fill="currentColor">induced current opposes the approach</text>
</svg>
""",
    },
    "leph107": {
        "caption": "LCR phasor triangle: Vₗ and Vᴄ act along the same line "
                    "but opposite senses; their resultant, combined with Vᵣ, "
                    "gives the impedance triangle and phase angle φ.",
        "svg": """
<svg viewBox="0 0 380 260" role="img" aria-label="LCR phasor diagram: current I along the horizontal axis, voltage across the resistor VR in phase with it, voltage across the inductor VL ninety degrees ahead, voltage across the capacitor VC ninety degrees behind (opposite VL), their difference VL minus VC combining at right angles with VR to give the resultant EMF E at phase angle phi.">
  <defs>
    <marker id="d107-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 Z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="60" y1="210" x2="330" y2="210" stroke="currentColor" stroke-width="1" opacity="0.4"/>
  <line x1="60" y1="210" x2="60" y2="30" stroke="currentColor" stroke-width="1" opacity="0.4"/>
  <line x1="60" y1="210" x2="220" y2="210" stroke="currentColor" stroke-width="2" marker-end="url(#d107-arrow)"/>
  <text x="140" y="228" text-anchor="middle" font-size="13" fill="currentColor">I, Vᵣ</text>
  <line x1="60" y1="210" x2="60" y2="80" stroke="currentColor" stroke-width="2" marker-end="url(#d107-arrow)"/>
  <text x="30" y="90" text-anchor="middle" font-size="13" fill="currentColor">Vₗ−Vᴄ</text>
  <line x1="220" y1="210" x2="220" y2="80" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6"/>
  <line x1="60" y1="80" x2="220" y2="80" stroke="currentColor" stroke-width="1" stroke-dasharray="3 3" opacity="0.6"/>
  <line x1="60" y1="210" x2="220" y2="80" stroke="currentColor" stroke-width="2.2" marker-end="url(#d107-arrow)"/>
  <text x="230" y="140" text-anchor="middle" font-size="14" fill="currentColor">E</text>
  <path d="M 95 210 A 35 35 0 0 1 84 184" fill="none" stroke="currentColor" stroke-width="1.3"/>
  <text x="105" y="195" font-size="13" font-style="italic" fill="currentColor">φ</text>
  <text x="195" y="252" text-anchor="middle" font-size="12" fill="currentColor">tan φ = (Xₗ−Xᴄ)/R, Z = E/I</text>
</svg>
""",
    },
    "leph108": {
        "caption": "A propagating electromagnetic wave: E, B and the direction "
                    "of travel are mutually perpendicular, both fields "
                    "oscillating in phase along the wave's path.",
        "svg": """
<svg viewBox="0 0 440 240" role="img" aria-label="Electromagnetic wave propagating along the x-axis, with the electric field E oscillating in the y-axis (vertical plane) and the magnetic field B oscillating in the z-axis (horizontal plane), both perpendicular to each other and to the direction of propagation.">
  <defs>
    <marker id="d108-arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M0,0 L10,5 L0,10 Z" fill="currentColor"/>
    </marker>
  </defs>
  <line x1="30" y1="140" x2="410" y2="140" stroke="currentColor" stroke-width="1.6" marker-end="url(#d108-arrow)"/>
  <text x="400" y="160" text-anchor="middle" font-size="13" fill="currentColor">x (propagation)</text>
  <path d="M 60 140 C 90 70, 120 70, 150 140 C 180 210, 210 210, 240 140 C 270 70, 300 70, 330 140 C 355 195, 375 195, 390 150"
        fill="none" stroke="currentColor" stroke-width="2"/>
  <text x="95" y="60" text-anchor="middle" font-size="13" fill="currentColor">E (y)</text>
  <path d="M 60 140 C 80 140, 90 118, 120 118 C 150 118, 160 162, 190 162 C 220 162, 230 118, 260 118 C 290 118, 300 162, 330 162 C 355 162, 365 145, 390 140"
        fill="none" stroke="currentColor" stroke-width="1.6" opacity="0.6" stroke-dasharray="1 0"/>
  <text x="360" y="180" text-anchor="middle" font-size="13" fill="currentColor" opacity="0.75">B (z)</text>
  <line x1="60" y1="140" x2="60" y2="60" stroke="currentColor" stroke-width="1" opacity="0.35"/>
  <line x1="60" y1="140" x2="20" y2="118" stroke="currentColor" stroke-width="1" opacity="0.35"/>
  <text x="200" y="225" text-anchor="middle" font-size="12" fill="currentColor">E ⊥ B ⊥ direction of propagation, c = E₀/B₀</text>
</svg>
""",
    },
}
