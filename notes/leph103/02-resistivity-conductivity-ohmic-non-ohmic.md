# Resistance, Resistivity, Conductivity and Ohmic vs Non-Ohmic Conductors

**NCERT sections covered:** 3.4, 3.5, 3.6, 3.8

## Ohm's law -- macroscopic form (NCERT 3.4)

If a conductor's temperature is constant, potential difference is directly proportional to current:
$$V \propto I \implies V = IR$$
where $R$ is the resistance (unit: ohm, $\Omega$; $1\ \Omega = 1\text{ V}/1\text{ A}$). A $V$-vs-$I$ plot is a straight line through the origin with slope $R$ (matching $y=mx$); an $I$-vs-$V$ plot instead has slope $1/R$ -- worth checking which axis is which before reading off a slope as $R$ or $1/R$.

Physically, resistance is the **hindrance offered to current flow**: microscopically, drifting electrons collide with the fixed positive ions of the lattice. Raising the temperature makes the ions vibrate with larger amplitude, increasing collision frequency and hence resistance.

## Resistivity (NCERT 3.4)

Resistance depends on the conductor's geometry: $R\propto l$ (longer wire, more collisions to traverse) and $R\propto 1/A$ (larger cross-section, more parallel paths, less resistance). Combining:
$$R = \frac{\rho l}{A}$$
where $\rho$, the **resistivity**, depends only on the material's nature and temperature -- crucially, **not** on the wire's dimensions. The teacher's analogy: the density of water is the same whether you take a drop, a glass, or a bucket of it -- resistivity of copper is the same whether the copper wire is thin, thick, long, or shaped as a sheet.

**Resistance vs. resistivity:**

| | depends on dimensions (l, A)? | depends on material & temperature? | SI unit |
|---|---|---|---|
| Resistance $R$ | yes | yes | $\Omega$ |
| Resistivity $\rho$ | no | yes | $\Omega\cdot\text{m}$ |

## Deriving $\rho = m/(ne^2\tau)$ (NCERT 3.5, eq. 3.23)

Starting from the drift-velocity relation $I = nev_dA$ (from the previous lecture) with $v_d = eE\tau/m$ and $E=V/l$:
$$I = neA\cdot\frac{eE\tau}{m} = \frac{ne^2A\tau}{m}\cdot\frac{V}{l}$$
Rearranging for $V$ and comparing with both $V=IR$ and $R=\rho l/A$:
$$R = \frac{m}{ne^2\tau}\cdot\frac{l}{A} \implies \boxed{\rho = \frac{m}{ne^2\tau}}$$
where $n$ is the free-electron (charge) density, $\tau$ the average relaxation time, $e$ the electron's charge and $m$ its mass.

**Temperature dependence (metals):** as $T$ increases, $\tau$ decreases (more frequent collisions), so $\rho$ increases with temperature. Since $\rho\propto 1/n$, a material with higher free-electron density (e.g. copper) has lower resistivity than one with lower density (e.g. an alloy or iron); silver has the least resistivity of common conductors, though copper/aluminium are used for practical wiring.

## Conductance and conductivity

**Conductance** $g = 1/R = I/V$, unit mho -- this specific term is not part of the NCERT chapter text but is a standard reciprocal-of-resistance quantity introduced as useful vocabulary.

**Conductivity** (NCERT-covered, eq. 3.23), the reciprocal of resistivity:
$$\sigma = \frac{1}{\rho} = \frac{ne^2\tau}{m}$$

## Macroscopic vs. microscopic Ohm's law (NCERT eq. 3.3, 3.13)

$V=IR$ relates external, circuit-level quantities (voltage, current, resistance) -- the teacher calls this the **macroscopic form**. There is also a **microscopic form** relating quantities internal to the conductor:
$$\vec{J} = \sigma\vec{E}$$
**Derivation:** from $I=nev_dA$, dividing both sides by $A$ gives $J = nev_d$; substituting $v_d = eE\tau/m$:
$$J = ne\cdot\frac{eE\tau}{m} = \frac{ne^2\tau}{m}E = \sigma E$$

## Ohmic and non-ohmic conductors (NCERT 3.6, "Limitations of Ohm's Law")

Conductors whose $V$-$I$ graph is **linear** (they obey Ohm's law) are **ohmic conductors**. Conductors that do **not** obey Ohm's law are **non-ohmic**, in (at least) three distinct ways:

1. **$V$-$I$ graph is non-linear** -- e.g. metals at high currents.
2. **The relation between $V$ and $I$ depends on the sign of $V$** -- e.g. a junction diode (reversing $V$ does not simply reverse $I$).
3. **The $V$-$I$ relation is non-unique** -- for the same voltage $V$, the current may take two or more values -- e.g. a thyristor (an S-shaped curve with a folded-back region).

This matches NCERT's three limitations (a)-(c) closely, though the board's example for case 3 is a **thyristor** rather than NCERT's GaAs -- both are valid real devices with a non-unique $V$-$I$ curve, just a different illustrative choice.

---
*Note on this lecture's transcript:* the non-adjacent duplicate scan flagged 9 pairs, but every one turned out to be a short, genuinely-reused stock phrase or formula recited at two different points of one continuous, non-repeating derivation (e.g. stating a formula as a derivation's goal, then again once it's actually reached) -- not the delayed re-transcription artifact found elsewhere in this chapter. The one real gap: the transcript's spoken narration essentially stops at the *announcement* of "ohmic and non-ohmic conductors" (its last real content, ending right at the video's true duration), while the board already shows the complete, worked-through NCERT 3.6 content well before that announcement timestamp. The whole ohmic/non-ohmic section above is grounded from board frames alone -- see the flagged span below for the frame-by-frame detail.


## Verify these spans
- [31:25–31:37] The transcript's last two segments (1885-1899s) only ANNOUNCE the topic -- 'when we talk of conductors, there are two types...ohmic...and non-ohmic...here we are going to talk about ohmic and non-ohmic conductors' -- and then the transcript ends (its very last segment's start, 1901s, is already past the true video duration of 1897.5s, inside only the small fixed rounding grace, so essentially nothing more was narrated). The actual ohmic/non-ohmic content -- the definitions and all three NCERT 3.6 sub-cases (i-iii), matching (a)-(c) almost exactly, down to worked diagrams for each -- is fully present on the board, built up progressively across frames floor_000079 (1560s, heading + J=sigma*E just finished) through floor_000089 (1760s, both definitions + case (i) with the metals-at-high-current graph), floor_000091 (1800s, case (ii), junction diode), and floor_000093-floor_000095 (1840-1880s, case (iii) built up step by step with the thyristor S-curve). This board sequence runs from 1560s to 1880s -- i.e. it was mostly already written well BEFORE the transcript's narration even announces starting the topic at ~1885-1901s. That is the reverse of lecture 1's pattern (board slightly ahead of speech near the very end) and large enough (over 300s) that it may reflect ASR timestamp drift accumulating over this single-shot ~32-minute transcription rather than the teacher truly writing 5+ minutes silently ahead of his own explanation. Either way, the automated non-adjacent duplicate scan found no repeated block here (all 9 flagged pairs earlier in this transcript are short, genuinely reused stock phrases/formulas within one continuous derivation, not a re-transcription loop), so this reads as a timestamp/coverage mismatch rather than fabrication. The final ohmic/non-ohmic claim above is grounded entirely from these board frames.