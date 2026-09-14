# Electromagnetic Waves

*Class XII CBSE Physics · Chapter 8 · 5 lectures, in order.*

*NCERT sections covered: 8.1, 8.2, 8.3, 8.4, 8.5.*

*Transcribed from the teacher's recorded lectures and checked against the
board frames and the NCERT text. Equations are board-grounded; any span the
transcript could not resolve confidently is flagged in place.*

---

## Displacement Current and Maxwell's Equations

**NCERT sections covered:** 8.1, 8.2

### The problem with Ampere's circuital law (NCERT 8.2)

Ampere's circuital law states $\oint \vec{B}\cdot d\vec{l} = \mu_0 I$, where $I$ is the current
enclosed by the Amperian loop.

Consider a capacitor being charged by a time-varying current $i(t)$. Draw a loop around one of
the connecting wires, and consider two different surfaces bounded by that same loop:

- **$C_1$**: a small "pot"-shaped surface that stays outside the capacitor gap -- the wire's
  conduction current $I$ pierces it, so Ampere's law gives $\oint \vec{B}\cdot d\vec{l} = \mu_0 I$.
- **$C_2$**: a larger surface bulging through *between* the plates -- no conduction current
  crosses it (charge does not jump the gap), so Ampere's law gives $\oint \vec{B}\cdot d\vec{l} = 0$.

Both surfaces share the same boundary loop, so $\vec{B}$ integrated around that loop cannot
have two different values -- Ampere's law as stated is inconsistent. The lecture also frames
this as an apparent violation of Kirchhoff's junction rule: current $I$ flows in at a point $P$
just before one plate, seems to vanish across the gap, and reappears at a point $Q$ past the
other plate.

### Maxwell's resolution: displacement current (NCERT 8.2)

Maxwell's fix: there must be a second current term active precisely in the gap where the
conduction current is zero. Between the plates, the electric flux is

$$\Phi_E = \vec E \cdot \vec A = \frac{\sigma}{\varepsilon_0}A = \frac{Q}{\varepsilon_0}$$

using the field between capacitor plates $E = \sigma/\varepsilon_0 = Q/(A\varepsilon_0)$.
Differentiating with respect to time,

$$\varepsilon_0\frac{d\Phi_E}{dt} = \frac{dQ}{dt}$$

and since $dQ/dt$ is a current by definition, Maxwell named this the **displacement current**,

$$I_d = \varepsilon_0 \frac{d\Phi_E}{dt}$$

Outside the plates only conduction current flows ($I_d = 0$); inside the gap only displacement
current flows ($I_c = 0$); together they form one continuous total current $I = I_c + I_d$ that
never actually breaks at the gap -- resolving the Kirchhoff-rule paradox as well. This gives the
corrected, general form of Ampere's law (the Ampere-Maxwell law):

$$\oint \vec B \cdot d\vec l = \mu_0\left(I_c + \varepsilon_0\frac{d\Phi_E}{dt}\right)$$

### Maxwell's four equations (NCERT 8.2, boxed summary)

The board closes the lecture by collecting the complete set of Maxwell's equations in vacuum:

1. **Gauss's law of electrostatics:** $\oint \vec E \cdot d\vec A = Q/\varepsilon_0$
2. **Gauss's law of magnetostatics:** $\oint \vec B \cdot d\vec A = 0$
3. **Faraday's law of EMI:** $\oint \vec E \cdot d\vec l = -\dfrac{d\Phi_B}{dt}$ (i.e. $\varepsilon = -d\phi/dt$)
4. **Modified (Ampere-Maxwell) circuital law:** $\oint \vec B \cdot d\vec l = \mu_0\left(I_c + \varepsilon_0\dfrac{d\Phi_E}{dt}\right)$

This is exactly NCERT's boxed list in section 8.2, same four laws, same order.

### A note on this lecture's transcript

The automated coverage check reports 107% coverage and passes cleanly, but that is misleading
here -- see the uncertain span below. The ASR transcript's real content stalls mid-derivation
(still building $\Phi_E = E\cdot A$) and its last captured sentence cuts off mid-word. It never
narrates the differentiation step, the $I=I_c+I_d$ statement, or Maxwell's four equations by
name at all, even though the board frames show all of this written out, in a natural progressive
build on the same page, well within the lecture's verified 980.19s duration. The final three
claims above (differentiation/$I_d$, and Maxwell's four equations) are therefore grounded from
board frames only.


### Verify these spans
- [13:50–16:20] The transcript's own final segment is timestamped 968.0-1056.0s, which overshoots the video's verified true duration (980.19s) by ~76s -- exactly the 'coverage looks clean but isn't' trap: check_coverage() reports 107% coverage and passes, yet the segment's text cuts off mid-word ('...electric field direction is this is the direction o'), and the delayed-duplicate scanner found no repeated block (0 flagged pairs), so this is neither of the two previously-catalogued failure modes cleanly -- it looks like a silent truncation whose tail segment was also given a stretched/overshot timestamp. Either way, the transcript's real captured content stalls partway through the displacement-current derivation (still building Phi_E = E.A) and never reaches the differentiation step (I_d = eps0 dPhi_E/dt), the I=Ic+Id statement, or any mention of 'Maxwell's equations' / 'Gauss's law' / 'Faraday's law' by name. The board frames, however, show this content completed and written out in full: floor_000030 (sampled at video t=580s -- notably BEFORE the transcript's own claimed timestamp for the Phi_E=E.A discussion, another sign the transcript's internal timestamps are not reliable in this stretch) already has the differentiation and I=Ic+Id; floor_000043 (t=840s) has Maxwell's equations 1-2 being written; floor_000049 (t=960s, near the true end) has all four complete. These three frames sit on the same continuously-built board page as the earlier, transcript-confirmed derivation (visible progression, not a jump to an unrelated page), which is why they are trusted as belonging to this lecture despite having no matching transcript span -- grounded from board frames alone, per claims 7 and 8 above.

---

## Displacement Current, Maxwell's Equations, and the E-B Symmetry

**NCERT sections covered:** 8.1, 8.2

### Relationship to the other Displacement-Current lecture in this chapter

This lecture (`Displacement and maxwell Eqns..mkv`, 1063.3s) covers essentially the same
material as the shorter `#1Displacement current and Maxwell Eqns.mp4` (980.19s, see
`01-displacement-current-and-maxwells-equations.md`) -- same opening line almost verbatim, the
identical pot/tiffin-box two-surface argument, the identical Kirchhoff-paradox framing, and (from
the board) what looks like literally the same handwritten page for the first half of the
derivation. It is **not** a duplicate file (different sha256, different duration, different
Gemini cache key -- see the chapter's file-list note), and it is meaningfully more complete: it
continues past the point where lecture 01's transcript stalls, explicitly *narrating* (not just
writing on the board) all four of Maxwell's equations one at a time by name and formula, and
closes with a spoken resolution of the apparent Kirchhoff violation and a short discussion of the
symmetry between Faraday's law and the displacement-current result that lecture 01 does not have
in its transcript at all. It also continues slightly further, into a one-line preview of "light is
an EM wave" that bridges into the chapter's next topic. Whether this is an independent retake or
an extended second pass over the same board is not determinable from the available material, but
for note-taking purposes this version supersedes lecture 01 in coverage -- if a student only had
time for one of the two, this is the more complete one.

### The problem with Ampere's circuital law (NCERT 8.2)

Ampere's circuital law states $\oint \vec B \cdot d\vec l = \mu_0 I$. For a capacitor being
charged by a time-varying current $i(t)$, two different surfaces bounded by the same loop give
different answers: a small surface $C_1$ that the wire's conduction current pierces gives
$\oint \vec B\cdot d\vec l = \mu_0 I$, while a larger surface $C_2$ bulging through the capacitor
gap (where no conduction current crosses) gives $\oint \vec B \cdot d\vec l = 0$. Same loop, same
law, two different results -- and the same picture looks like it violates Kirchhoff's junction
rule too, since current flowing in at a point $P$ seems to vanish across the gap and reappear at
a point $Q$ on the other plate.

### Displacement current and the modified Ampere-Maxwell law (NCERT 8.2)

Between the plates, $\Phi_E = \vec E\cdot\vec A = Q/\varepsilon_0$. As the current varies, the
charge on the plates -- and hence $\Phi_E$ -- changes with time. Outside the plates only
conduction current flows; inside the gap only **displacement current**,

$$I_d = \varepsilon_0\frac{d\Phi_E}{dt}$$

flows, with $I_c = I_d$. This gives the corrected, general Ampere-Maxwell law:

$$\oint \vec B \cdot d\vec l = \mu_0 I_c + \mu_0\varepsilon_0\frac{d\Phi_E}{dt} = \mu_0(I_c + I_d)$$

With displacement current in the picture, Kirchhoff's rule is no longer violated -- current just
outside $P$ is conduction current, current in the gap is displacement current, and the two are
equal, so the total current is continuous through the whole loop after all.

#### A symmetry worth noting
The lecture pauses here to connect this back to electromagnetic induction (Ch. 7): a
time-varying **magnetic** field generates an **electric** field (Faraday's law). The
displacement-current result just derived shows the converse also holds -- a time-varying
**electric** field generates a **magnetic** field. The two effects are symmetric/interchangeable,
which is part of why light (an oscillating $E$ and $B$ sustaining each other) can propagate
without a medium.

### Maxwell's four equations (NCERT 8.2, boxed summary)

1. **Gauss's law of electrostatics:** $\oint \vec E\cdot d\vec s = Q/\varepsilon_0$
2. **Gauss's law of magnetostatics:** $\oint \vec B\cdot d\vec s = 0$
3. **Faraday's law of EMI:** $\text{emf} = -d\Phi/dt$, i.e. $\oint \vec E\cdot d\vec l = -d\Phi_B/dt$
4. **Modified Ampere-Maxwell law:** $\oint \vec B\cdot d\vec l = \mu_0\left(I_c + \varepsilon_0\dfrac{d\Phi_E}{dt}\right)$

Matches NCERT's boxed list in 8.2 exactly, same four laws and order. The board's final line for
this lecture -- "light is EM waves $\Rightarrow$ it consists of electric field and magnetic field
intensities" -- previews the chapter's next topic (NCERT 8.1's remark that Maxwell's predicted EM
wave speed matching light's speed is what identifies light itself as an electromagnetic wave).

### A note on this lecture's transcript

Coverage checks report 103.5% and pass cleanly, but (as with lecture 01) that is misleading --
the transcript's real content cuts off mid-sentence while defining EMF, before the fourth
equation is explicitly re-stated in the summary and before the "light is EM waves" note. Both are
grounded from board frames only -- see the uncertain span below. Unlike lecture 01, though, this
transcript *does* narrate all four equations by name and formula, and derives displacement
current with a fully spoken formula, before that late cutoff -- so the gap here is much smaller
and confined to the closing recap.


### Verify these spans
- [16:40–17:43] check_coverage() reports 103.5% coverage and passes cleanly (the last segment is timestamped 1036.5-1101.1s, overshooting the video's verified true duration of 1063.3s by ~38s) -- the same 'clean-looking but misleading' pattern seen in the companion lecture 01. The delayed-duplicate scanner found no repeated block here either (only one short flagged pair, segments 27 vs 30 at ratio 0.73, which is just the teacher naturally repeating the short phrase 'modified ampere circuited law' a few sentences apart, not a real loop). The transcript's actual content, however, cuts off mid-sentence while defining EMF from Faraday's law ('...we can also write EMF as...'). Two things past that cutoff are grounded from board frames only: the explicit restatement of Maxwell's 4th equation in the summary list (already independently derived and narrated earlier in the lecture, at ~610-655s, so this is a recap gap, not a missing-content gap), and the 'light is EM waves' bridging note, which is not spoken anywhere in the available transcript at all. Frame floor_000052 (t=1020s), close to the true end of the video, is a direct continuation of the same board page built up continuously from floor_000041 onward, so it is trusted as belonging to this lecture.

---

## Hertz's Experiment

### Hertz's experiment

*Not covered in the current NCERT textbook* -- included here as background on how electromagnetic waves were first produced and detected experimentally, since most EM waves (radio, TV, UV, X-rays, etc.) are invisible to the eye.

**Core idea:** an oscillating charge is an accelerated charge, and an accelerated charge radiates electromagnetic energy.

#### Apparatus
Two metal plates (copper or zinc), $60$ cm apart, connected via metal spheres $S_1$, $S_2$ with an air gap between them, fed by a high-voltage induction coil (several thousand volts).

#### Working
The very high potential difference ionizes the air gap between $S_1$ and $S_2$, making it briefly conducting — producing a spark, and hence an **oscillating current**. This oscillating current produces an oscillating magnetic field, which induces a large oscillating EMF at a separate detector (points $C$, $D$ on a nearby ring), itself large enough to produce a second spark there — with no direct wire connecting the two. This demonstrates that electromagnetic energy was **radiated through space** from $S_1$–$S_2$ and picked up at the detector.

#### Frequency
The two metal plates act as a capacitor ($C$); the connecting wires contribute a small inductance ($L$). The oscillator's frequency (and hence the radiated EM wave's frequency) is:
$$\nu = \frac{1}{2\pi\sqrt{LC}}$$

#### Detector orientation
The detector ring must be oriented so the oscillating magnetic field is **perpendicular to the plane of the ring** — this is what produces the large induced EMF (and visible spark) at $C$–$D$.

---
*Note on this lecture's transcript:* the explanation of why the detector sparks is transcribed once correctly, then repeated nearly verbatim a second time (~95s of this 682s lecture). The transcript's own final sentence is also cut off mid-word; its completion is grounded from a board frame.


### Verify these spans
- [04:43–08:55] The explanation of why sparking occurs at the detector (oscillating current -> oscillating magnetic field -> large induced EMF between C and D -> detector spark, demonstrating radiated EM energy) is transcribed once (~t=283-378s) and then re-transcribed nearly verbatim a second time (~t=444-535s) -- a shorter instance of the delayed-repetition pattern found throughout this project. No content appears to have been lost here (the two passes say the same thing), but roughly 95 of this short lecture's 682 seconds are duplicated explanation rather than new material.
- [11:10–11:22] The transcript's own final segment cuts off mid-sentence ('...such that the magnetic field produced by oscillating current'). A board frame (floor_000030.jpg) shows the completed sentence: the detector ring is held such that the oscillating magnetic field is perpendicular to the plane of the ring, which is what produces the large induced EMF across C and D. The detector-orientation claim above completes this from the frame.

---

## Sources, Properties, and Equation of Electromagnetic Waves

**NCERT sections covered:** 8.3, 8.4

### Sources of electromagnetic waves (NCERT 8.3)

A stationary charge produces only an electric field; a charge moving at constant velocity produces a time-independent magnetic field. An **accelerated** charge (non-uniform velocity) is a source of EM waves — its E and B fields vary with time. An oscillating LC circuit is one way to produce EM waves (the capacitor's charge varies with time, i.e. is being accelerated).

### Properties of electromagnetic waves (NCERT 8.3)

1. **Transverse** in nature.
2. Frequency of the EM wave = frequency of its source.
3. Energy of the wave comes **at the expense of the source's energy**.
4. Travel through vacuum at the **speed of light**, $c$.
5. **Electrically neutral** — not made of charged particles, so NOT deflected by electric or magnetic fields.
6. Show ordinary wave phenomena: reflection, refraction, interference, diffraction, polarization.

### Field relations and energy (NCERT 8.4)

$$c = \frac{E_0}{B_0}$$
In a medium: $v = \dfrac{1}{\sqrt{\mu\varepsilon}}$; in vacuum, $c=\dfrac{1}{\sqrt{\mu_0\varepsilon_0}}$.

**Equal energy density:** $U_E = U_M$ everywhere in an EM wave. Total energy density $U=U_E+U_M$ (expressible via $\varepsilon_0 E^2$).

### Momentum and radiation pressure

EM waves carry momentum as well as energy, so they exert **radiation pressure**. If total energy $U$ is transferred to a surface (fully absorbed) in time $t$:
$$p = \frac{U}{c}$$

**Example:** sunlight on your hand — you feel the energy (warmth), but the momentum transferred is imperceptibly small (since $c$ is so large).

**Importance:** carrying energy from one place to another — radio/TV signals, and light carrying energy from the Sun to the Earth.

**Historical note:** the best modern electronic oscillator circuits reach only $\sim10^{11}$ Hz, far below visible light's frequency — so light's electromagnetic nature couldn't be demonstrated the same way Hertz demonstrated radio waves.

### Equation of an electromagnetic wave (NCERT 8.3)

$E$, $B$, and the direction of propagation are mutually perpendicular. For propagation along $x$, $E$ along $y$, $B$ along $z$:
$$E_y = E_0\sin(\omega t - kx), \qquad B_z = B_0\sin(\omega t - kx), \qquad k=\frac{2\pi}{\lambda}$$
Direction of propagation given by $\hat E\times\hat B$ (e.g. $\hat\jmath\times\hat k=\hat\imath$).

---
*Note on this lecture's transcript:* properties, field-magnitude ratio, energy density, and momentum/radiation-pressure are all transcribed cleanly. However, the "equation of EM waves" half of this lecture's own title — the explicit sinusoidal $E_y$/$B_z$ component equations and the propagation-direction rule — never appears anywhere in the transcript at all, despite being clearly present on the board near the end of the true video. Grounded entirely from frames; see the flagged span below.


### Verify these spans
- [27:40–30:18] Board frames (floor_000084.jpg, floor_000088.jpg, both within the video's true 1818.37s duration) show a substantial 'Propagation of EM waves' section -- explicit sinusoidal component equations for E and B (Ey=E0*sin(omega*t-kx), Bz=B0*sin(omega*t-kx)), the propagation constant k=2*pi/lambda, and the cross-product rule for the direction of propagation -- that never appears anywhere in the available transcript at all, despite the lecture's own title explicitly naming 'equation of EM waves' as a topic (the transcript covers only the qualitative 'properties' half of the title). Given the frames' timestamps are near the very end of the true video duration while the transcript's own final words are on a different topic (comparing oscillator vs. visible-light frequency), this content was most likely taught near the end of the lecture but never captured by the ASR at all -- a total omission rather than a timestamp-drift artifact, since no transcript segments reference it anywhere. This whole claim is grounded entirely from the frames.

---

## Electromagnetic Spectrum: Production and Uses of EM Waves

**NCERT sections covered:** 8.5

### The electromagnetic spectrum (NCERT 8.5)

Ordered by wavelength around the visible range ($\approx400$–$700$ nm):

| Band | Wavelength range |
|---|---|
| Radio waves | $0.3$ m – $10^5$ m |
| Microwaves | $1$ mm – $0.3$ m |
| Infrared | $700$ nm – $1$ mm |
| **Visible** | $400$ nm – $700$ nm |
| UV | $10$ nm – $400$ nm |
| X-rays | $1$ Å – $100$ Å |
| Gamma rays | $10^{-3}$ Å – $1$ Å |

No sharp boundaries — adjacent bands overlap, and cited boundary values vary slightly by source. Moving from visible toward shorter wavelength, frequency increases; toward longer wavelength, frequency decreases. (Common exam question: arrange given radiation types in ascending/descending order of frequency.)

#### Production and uses, band by band

**Radio waves** — produced by accelerated charges in a conducting wire. Radio/TV communication: AM band $500$–$1710$ kHz, TV $\approx54$–$890$ MHz, FM band $88$–$108$ MHz; mobile phones use even higher (ultra-high) frequencies.

**Microwaves** — produced by klystrons/magnetrons. Used in **radar** (short wavelength $\Rightarrow$ high energy, good directionality, minimal diffraction, straight-line travel) and **microwave ovens** (frequency tuned to water molecules' resonant frequency for efficient energy transfer, heating food).

**Infrared** — produced by hot bodies/molecules; also called *heat waves* (water molecules readily absorb IR, raising thermal motion). Used in physiotherapy lamps, remote controls. Also explains the **greenhouse effect**: incoming solar UV/energy is absorbed and re-radiated as IR, which greenhouse gases (CH$_4$, H$_2$O, CO$_2$) trap in the atmosphere, warming the surface (analogous to a closed car heating in sunlight).

**Visible light** — produced by lamps, ionized gases. Lets us see objects (light emitted/reflected carries information about the world); also used to study molecular structure and electron arrangement.

**UV rays** — produced by special lamps and very hot bodies (the Sun). Used in LASIK eye surgery, water purification (killing germs), detecting forged documents/fingerprints. **Caution:** ozone-layer depletion by CFCs is a concern, since ozone normally filters harmful UV.

**X-rays** — produced by high-energy electrons bombarding a heavy metal target (Coolidge tube). Used diagnostically in medicine, in cancer treatment, and in scientific research (revealing molecular structure) — exposure kept brief since prolonged exposure harms healthy cells.

**Gamma rays** — wavelength $<10^{-3}$ nm, the highest-energy band; produced in nuclear reactions/emitted by radioactive nuclei. Used in medicine to destroy cancer cells, to study atomic nuclei, and (due to their high energy) to induce nuclear reactions.

---
*Note on this lecture's transcript:* this is an exceptionally clean and thorough transcript, covering radio through X-rays in full detail. The one gap is the gamma-rays uses section — the lecture opens by promising to cover production *and* uses for every band, and a board frame confirms the gamma-rays uses were written out (alongside X-rays) within the true video duration, but the transcript's own words never reach this content. Grounded from that frame; see the flagged span below.

*This lecture exists as two byte-identical duplicate files in the source library (confirmed via matching SHA-256 hashes); only one copy was transcribed and noted.*


### Verify these spans
- [36:40–39:10] The transcript's own words, right up through their final available segment, cover only the wavelength range, production method, and uses of X-rays -- despite the lecture opening (t=5s) explicitly promising to cover production and uses for ALL bands including gamma rays, and despite gamma rays being introduced (briefly, as produced by nuclear reactions) at the very start. A board frame (floor_000116.jpg), whose true video timestamp (t=2300s) falls before the video's true 2350.27s duration, shows a full 'gamma rays' section already written alongside the X-rays section: wavelength <10^-3 nm, produced in nuclear reactions / emitted by radioactive nuclei, and used in medicine to destroy cancer cells, to study atomic nuclei, and to produce nuclear reactions. None of this gamma-ray-uses content appears in the transcript's own words at all -- it is grounded entirely from this frame.
