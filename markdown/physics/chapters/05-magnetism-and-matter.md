# Magnetism and Matter

*Class XII CBSE Physics · Chapter 5 · 8 lectures, in order.*

*NCERT sections covered: 5.1, 5.2.2, 5.2.3, 5.2.4, 5.3, 5.4, 5.5.*

*Transcribed from the teacher's recorded lectures and checked against the
board frames and the NCERT text. Equations are board-grounded; any span the
transcript could not resolve confidently is flagged in place.*

---

## Magnetism Intro: Gauss's Law, Electrostatic Analogy, and Bar Magnet as Equivalent Solenoid

**NCERT sections covered:** 5.1, 5.2.2, 5.2.3, 5.2.4, 5.3

### Introduction: monopoles and Gauss's law in magnetism (NCERT 5.1, 5.3)
Lodestone (natural magnetite) is introduced as a naturally occurring magnet, and the earth itself is described as behaving like a giant magnet (a freely suspended bar magnet always settles north-south). A key qualitative fact is developed by repeatedly breaking a bar magnet: **magnetic monopoles do not exist** -- however small a piece you cut, it still has both an N and an S pole.

This directly motivates **Gauss's law in magnetism**: since field lines leaving the N pole always curve around and re-enter at S (closed loops, unlike electric field lines which start/end on isolated charges), the net magnetic flux through *any* closed surface is zero:
$$\oint \vec B\cdot d\vec S = 0$$
This is explicitly contrasted with Gauss's law in electrostatics, $\oint \vec E\cdot d\vec S = q/\varepsilon_0$, which is nonzero in general because isolated electric charge does exist.

### Bar magnet vs. solenoid: similarities and differences
Before deriving the equivalence formally, the lecture recaps general field-line properties (closed loops, tangent gives direction, never intersect, density $\propto$ strength) and lists concrete differences/similarities between a bar magnet and a current-carrying solenoid:

- **Differences:** a bar magnet's field strength is fixed once magnetised and its poles cannot be swapped; a solenoid's field $B=\mu_0 nI$ can be tuned via turns-per-length $n$ or current $I$, and its poles reverse if the current direction reverses.
- **Similarities:** both align north-south when freely suspended, both attract small iron pieces, and both have field lines and two poles.

These similarities are the motivation for treating a bar magnet as an "equivalent solenoid" -- the main derivation of this lecture.

### The electrostatic analogy (NCERT 5.2.3, 5.2.4)
A large stretch of the lecture builds up magnetism's dipole formulas entirely by comparison with the already-known electric dipole formulas, introducing a hypothetical **pole strength** $m$ (analogous to charge $q$) purely as a bookkeeping device -- flagged explicitly as *not* physically real, since isolated poles don't exist.

| Electrostatics | Magnetism |
|---|---|
| Charges $q_1,q_2$ | Pole strengths $m_N,\,m_S$ (hypothetical) |
| $F=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1q_2}{r^2}$ | $F=\dfrac{\mu_0}{4\pi}\dfrac{m_1m_2}{r^2}$ |
| $\vec p = q(2\vec l)$, points $-q\to+q$ | $\vec M = m(2\vec l)$, points S$\to$N |
| $\vec\tau=\vec p\times\vec E$ | $\vec\tau=\vec M\times\vec B$ |
| $U=-\vec p\cdot\vec E$ | $U=-\vec M\cdot\vec B$ |
| $E=F/q$ | $B=F/m$ |
| $E=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}$ | $B=\dfrac{\mu_0}{4\pi}\dfrac{m}{r^2}$ |
| $E_\text{axial}=\dfrac{2p}{4\pi\varepsilon_0 r^3}$ | $B_\text{axial}=\dfrac{\mu_0}{4\pi}\dfrac{2M}{r^3}$ |
| $E_\text{equatorial}=\dfrac{-p}{4\pi\varepsilon_0 r^3}$ | $B_\text{equatorial}=-\dfrac{\mu_0}{4\pi}\dfrac{M}{r^3}$ |

The magnetic dipole moment magnitude is pinned down independently by comparing two expressions for the torque on a current loop of $N$ turns, area $A$, in field $B$: $\tau=NIAB\sin\theta$ (from $\tau=I\vec A\times\vec B$, done in the previous chapter) against $\tau=MB\sin\theta$ (the magnetic analogue of $\tau=pE\sin\theta$), giving
$$M = NIA$$
and from $M=m(2l)$ with $[M]=\text{A m}^2$, the SI unit of pole strength $m$ works out to $\text{A m}$.

*Brief aside (not fully worked):* the lecture briefly poses cutting a bar magnet either along its axis or perpendicular to its axis through the centre, noting in both cases you get two smaller magnets, each still with an N and S pole -- reinforcing the "no monopoles" theme -- but does not carry the numerical through to compute the resulting pole strengths/moments.

### Derivation: bar magnet as an equivalent solenoid (NCERT 5.2.2)
**Goal:** prove that at a large axial distance $r$, the magnetic field of a current-carrying solenoid equals the known axial field of a bar magnet, $B=\dfrac{\mu_0}{4\pi}\dfrac{2m}{r^3}$ -- i.e. a solenoid *is* equivalent to a bar magnet of moment $M=NIA$.

**Prerequisite** (recalled from the previous chapter): the on-axis field of a single circular current loop of radius $a$ at distance $x$ from its centre is $B=\dfrac{\mu_0 I a^2}{2(a^2+x^2)^{3/2}}$, which reduces to $B=\dfrac{\mu_0 I}{2a}$ at the centre ($x=0$).

**Setup:** a solenoid of radius $a$, total length $2l$, turns per unit length $n$, axis along $x$ with origin $O$ at the centre. Field point $P$ lies on the axis at distance $r$ from $O$ ($r\gg l$, $r\gg a$). Consider a thin slice of width $dx$ at position $x$ from centre, carrying $n\,dx$ turns; its distance from $P$ is $(r-x)$, so treating it as a single loop of $n\,dx$ turns:
$$dB = \frac{\mu_0\, I\, a^2\, n\, dx}{2\big(a^2+(r-x)^2\big)^{3/2}}$$

**Far-field approximation:** since $r\gg x$ and $r\gg a$, the denominator simplifies to just $r^3$:
$$dB \approx \frac{\mu_0\, n\, I\, a^2}{2 r^3}\,dx$$

**Integrate** over the whole solenoid, $x=-l$ to $x=+l$:
$$B=\int_{-l}^{l} dB = \frac{\mu_0\, n\, I\, a^2}{2r^3}(2l)$$

**Substitute** $n = N/(2l)$ (so the $2l$'s cancel) and multiply/divide by $\pi$ to turn $Ia^2$ into $I(\pi a^2) = I\!\cdot\!(\text{loop area})$, i.e. the magnetic moment $M=NIA=NI\pi a^2$:
$$\boxed{B = \frac{\mu_0}{4\pi}\frac{2M}{r^3}}$$

This is exactly the bar-magnet axial field formula the derivation set out to reproduce (matching NCERT Eq. 5.1) -- so at large axial distances, a current-carrying solenoid of moment $M=NIA$ behaves identically to a bar magnet of the same moment, completing the proof.

---
*Note on this lecture:* the transcript and board frames agree closely throughout -- the derivation completes on the board (boxed final result, `floor_000097.jpg`) right at the very end of the lecture's true duration, matching the transcript's own conclusion at essentially the same point. No delayed-repetition or missing-topic issue was found in this lecture; the automated non-adjacent-duplicate scan flagged only two short, low-length phrase pairs (natural verbal repetition of brief labelling statements), not a genuine content loop.


---

## A Dipole in a Uniform Magnetic Field Performs SHM

**NCERT sections covered:** 5.2.3

### Recap: the spring-mass SHM condition (Class 11 link)
Before proving the magnetic result, the lecture re-derives the spring-mass SHM condition as a template: a spring stretched by $x$ has restoring force $F=-kx$, so $ma=-kx \Rightarrow a=-\dfrac{k}{m}x=-\omega^2x$. Since acceleration is proportional to $-(\text{displacement})$, this is simple harmonic motion, obeying the general equation
$$\frac{d^2x}{dt^2}+\omega^2 x = 0$$
The same logic carries over to *angular* quantities: replacing $x\to\theta$ and $a\to\alpha$ (angular acceleration), if $\alpha\propto-\theta$ then $\dfrac{d^2\theta}{dt^2}+\omega^2\theta=0$ and the angular motion is SHM too. This angular version is what the main derivation below needs.

### Derivation: a dipole in a uniform field performs SHM (NCERT 5.2.3)
A magnetic dipole (a short bar magnet, moment $\vec M$) is placed in a uniform field $\vec B$, making angle $\theta$ with it. It experiences a **deflecting torque**
$$\vec\tau = \vec M\times \vec B, \qquad \tau = MB\sin\theta$$
By the rotational analogue of Newton's second law ($F=ma \to \tau=I\alpha$, with moment of inertia $I$ in place of mass and angular acceleration $\alpha$ in place of linear acceleration):
$$I\alpha = -MB\sin\theta$$
The minus sign is because the **restoring** torque set up by the field acts opposite to the deflecting displacement -- exactly like $F=-kx$ in the spring case.

For small angular displacement, $\sin\theta\approx\theta$, so
$$I\alpha = -MB\theta \quad\Rightarrow\quad \alpha = -\frac{MB}{I}\theta$$
Since $\alpha\propto-\theta$, this **is** SHM, with
$$\omega^2 = \frac{MB}{I}, \qquad T = 2\pi\sqrt{\frac{I}{MB}} \quad\left(\text{equivalently } B=\frac{4\pi^2 I}{MT^2}\right)$$
This last rearranged form is useful whenever a problem gives the period of oscillation and asks for the unknown field or moment.

### Worked numerical 1: field from an oscillating magnetic needle
A magnetic needle has moment $M=6.7\times10^{-2}$ A m$^2$ and moment of inertia $I=7.5\times10^{-6}$ kg m$^2$, and completes 10 oscillations in 6.7 s.

**Time period:** $T = \dfrac{6.7}{10} = 0.67$ s.

**Field:** using $B=\dfrac{4\pi^2 I}{MT^2}$,
$$B \approx 0.01~\text{T}$$

### Worked numerical 2: bar magnet vs. equal-moment solenoid (3 parts)
A short bar magnet, axis at $30^\circ$ to an external field $B=800$ G, experiences torque $\tau=0.016$ N m. First convert the field to SI: $1$ T $=10^4$ G, so $B = 800\times10^{-4}~\text{T} = 0.08$ T.

**(i) Find $M$:** from $\tau = MB\sin\theta$,
$$M = \frac{\tau}{B\sin\theta} = \frac{0.016}{0.08\times\sin30^\circ} = 0.4~\text{A m}^2$$

**(ii) Work done moving the magnet from its most stable to its most unstable position.** Most stable is $\vec M\parallel\vec B$ ($\theta_1=0^\circ$); most unstable is $\vec M$ antiparallel to $\vec B$ ($\theta_2=180^\circ$). Work done against the restoring torque:
$$W = \int_{\theta_1}^{\theta_2}\tau\,d\theta = \int_{\theta_1}^{\theta_2}MB\sin\theta\,d\theta = MB\big[\cos\theta_1-\cos\theta_2\big] = MB\big(1-(-1)\big) = 2MB = 0.064~\text{J}$$

**(iii) Same magnet replaced by a solenoid of the same moment $M$**, with cross-sectional area $A=2\times10^{-4}$ m$^2$ and $N=1000$ turns. From $M=NIA$:
$$I = \frac{M}{NA} = \frac{0.4}{1000\times2\times10^{-4}} = 2~\text{A}$$

---
*Note on this lecture:* part (i) of numerical 2 is confirmed in both transcript and board frames, but the transcript audio track trails off mid-sentence right as parts (ii) and (iii) begin, well before reaching either result -- see the flagged span below. Both results were recovered directly from later board frames (`floor_000048.jpg`, `floor_000053.jpg`) that exist in the frames folder on disk but were dropped from the coverage-floor sampler's deduped `index.json` list (likely misjudged as near-duplicates of the preceding frame by the perceptual-hash dedupe step, since the board changes only incrementally as new lines are added below existing text) -- worth flagging upstream, since it means `index.json` alone is not a reliable guide to what content exists in a lecture's frame folder.


### Verify these spans
- [14:48–17:33] The transcript trails off mid-sentence at its last segment ('unstable position means unstable position means', ending 1060s) right as the teacher is setting up part (ii) of the second numerical (most-stable-to-most-unstable work done) -- it never reaches the computation of W, nor part (iii) (replacing the bar magnet with a solenoid to find the current). This does not look like the delayed-repeat fabrication loop (no earlier block is re-transcribed) -- it reads like the ASR response simply ran out/was cut short near the true end of the audio. The board-frame coverage-floor sampler's deduped index (index.json) also stops at t=880s (floor_000045), but the raw frames directory retains later, non-deduped frames (floor_000046 through floor_000053) that a direct check confirms DO carry new content -- floor_000048.jpg shows part (ii)'s full work-done derivation (W=2MB=0.064 J) and floor_000053.jpg shows part (iii)'s solenoid current result (I=2 A) freshly added beside it. Both of the two claims above for parts (ii) and (iii) are grounded from these board-only frames, with no transcript corroboration -- the physics is standard and consistent with the board's own part (i) answer and the given N, A, so treated as reliable, but flagged here since it could not be cross-checked against narration.

---

## The Earth's Magnetism: Dynamo Effect, Magnetic Axis, and Elements of the Field

### A note on syllabus scope
**This entire lecture covers material that has been removed from the current (rationalised, 2022-23 onward) NCERT Class 12 Physics syllabus.** The current NCERT Chapter 5 raw text jumps directly from Section 5.3 (Magnetism and Gauss's Law) to Section 5.4 (Magnetisation and Magnetic Intensity), with no "Earth's Magnetism" section at all -- in the pre-rationalisation NCERT this was Section 5.4, covering exactly the dynamo-effect theory, magnetic vs. geographic axis, and the three elements (declination, dip, horizontal component) taught in this lecture. Every claim below is therefore given `ncert_section=None` rather than forced onto a current-syllabus number; nothing here should be treated as CBSE-examinable under the present syllabus, though it remains standard, correct physics and is commonly retained in classroom teaching for conceptual completeness (and because some boards/older question banks still reference it).

### Why the earth behaves as a magnet: the dynamo effect
Two historical explanations are contrasted. A "huge bar magnet buried inside the earth" is ruled out, since the core's temperature is far above any material's Curie point -- a permanent magnet simply could not survive there. The accepted picture instead is the **dynamo effect**: the earth's core contains molten iron and nickel existing as mobile ions; their large-scale motion constitutes electric currents, and a moving charge always produces a magnetic field -- this circulating current system is the real source of the earth's magnetism.

### Magnetic axis vs. geographic axis
Treating the earth as though it contains an internal short bar magnet, its **magnetic axis** (through the magnetic N/S poles) is tilted at **11.3°** to the **geographic axis** (the earth's rotation axis, through the true/geographic N/S poles). Since a freely suspended compass needle's own north pole always swings toward geographic north (opposite poles attract), the pole of the earth's "internal magnet" lying near geographic north must, strictly, be a south pole -- but by long-standing convention it is still labelled the earth's "magnetic north pole."

**Field-line direction examples:** with field lines running (loosely) from geographic south to geographic north outside the earth,
- at a place near the geographic south (e.g. **Australia**), field lines appear to emerge **out of** the ground;
- at a place near the geographic north (e.g. **Britain**), field lines appear to go **into** the ground.

### Geographic vs. magnetic: axis, equator, meridian
| Geographic | Magnetic |
|---|---|
| **Axis:** line through geographic N & S poles (earth's rotation axis) | **Axis:** line through magnetic N & S poles |
| **Equator:** great circle perpendicular to the geographic axis | **Equator:** great circle perpendicular to the magnetic axis |
| **Meridian:** vertical plane containing the geographic axis at a place | **Meridian:** vertical plane containing the magnetic axis at a place |

At any given place, the geographic meridian and magnetic meridian planes generally differ by some angle -- which is precisely the first "element" of earth's magnetic field, below.

### The three elements of earth's magnetic field
These three quantities together completely specify the earth's magnetic field (magnitude and direction) at any place:

**1. Angle of declination ($\alpha$):** the angle at a place between the magnetic meridian and the geographic meridian. Knowing $\alpha$ tells you exactly where the magnetic meridian lies relative to true north.

**2. Angle of dip / magnetic inclination ($\delta$):** the angle at a place, measured within the magnetic meridian plane, between the earth's total field $\vec B$ and the horizontal. It is measured using a **dip circle**.

**3. Horizontal component ($B_H$):** the component of the earth's total field lying in the horizontal plane (within the magnetic meridian). Resolving $\vec B$ using the dip angle $\delta$:
$$B_H = B\cos\delta, \qquad B_V = B\sin\delta, \qquad B=\sqrt{B_V^2+B_H^2}, \qquad \tan\delta=\frac{B_V}{B_H}$$

**Special cases:**
- **At the magnetic equator:** $\delta=0^\circ$, so $B_V=0$ and $B=B_H$ -- the field is entirely horizontal.
- **At the magnetic poles:** $\delta=90^\circ$, so $B_H=B\cos 90^\circ=0$ and $B_V=B$ -- the field is entirely vertical. A compass needle, which normally settles by rotating in the horizontal plane to align with $B_H$, has no horizontal field to align with at the poles and so points in an arbitrary horizontal direction there.

---
*Note on this lecture:* the transcript covers the dynamo effect, the magnetic-vs-geographic axis/equator/meridian geometry, and element 1 (declination) cleanly and in full, matching the board closely throughout. However, the transcript's audio track runs out right as element 2 (angle of dip) is first named, and never reaches its definition or element 3 (horizontal component) at all -- see the flagged span below. Both were recovered from later board frames that exist in the frames folder on disk but, as in lecture 2 of this chapter, were dropped from the coverage-floor sampler's deduped `index.json` (last indexed frame stops at t=1200s, 177s before the lecture's true end at 1377.1s) -- the same upstream dedupe-drops-real-tail-content issue found there.


### Verify these spans
- [22:49–22:57] The transcript's last segment (index 92, 1369.5-1405.7s) only NAMES 'angle of dip, also known as magnetic inclination' and then stops entirely -- it never defines the term, never introduces the horizontal component (the 3rd of the '3 elements' the teacher explicitly enumerates at segment 78), and never derives the B_H/B_V/tan(delta) relations or the equator/pole special cases. This does not look like the delayed-repeat fabrication loop (nothing upstream is re-transcribed) -- it reads as the ASR response simply running out near the true end of the audio, similar to lecture 2 in this chapter. The coverage-floor sampler's deduped index.json also stops at t=1200s (floor_000061), but as in lecture 2, the raw frames folder retains later non-deduped frames (up to floor_000069, confirmed to exist and checked directly) that show the angle-of-dip definition fully written out plus the entire horizontal-component derivation with all four equations and both special-case results -- this is a real, temporally progressive board build-up (declination alone at t~860s and t~1140s, dip's definition text complete by the 65th raw frame, horizontal-component equations and special cases added afterward at the 66th-69th raw frames), not an isolated out-of-place frame. Both element-2 and element-3 claims above are grounded from these board-only frames, with no transcript corroboration at all -- flagged here since narration could not confirm them, though the content is standard and consistent with the board's own stated 3-element structure.

---

## Earth's Magnetism Numericals, Null Point Problems, and the Atom as a Magnetic Dipole

### Earth's magnetism: worked numericals

**Not present in the current rationalised NCERT syllabus** for this chapter -- checking the extracted textbook text (`data/ncert/raw/leph105.txt`), Chapter 5 "Magnetism and Matter" runs 5.1 Introduction, 5.2 The Bar Magnet, 5.3 Magnetism and Gauss's Law, 5.4 Magnetisation and Magnetic Intensity, 5.5 Magnetic Properties of Materials -- there is no Earth's-magnetism section at all (the pre-rationalisation NCERT's Earth's magnetism sub-chapter, including angle of dip/declination and null-point problems, was removed). This content is covered here as extra material the teacher chose to include, not because it is examinable under the current syllabus.

Using $B_H = B\cos\delta$ and $B_V=B\sin\delta$ ($\delta$ = angle of dip):
- Given $B_H$ and $\delta$: $B = B_H/\cos\delta$ (e.g. $B_H=0.35$ gauss, $\delta=22°$ $\Rightarrow B=0.35/0.92$).
- Given $B_H, B_V$: $\tan\delta = B_V/B_H$, then solve for $B$.
- **Full 3-D direction of $\vec B$:** first locate the *magnetic meridian* using the angle of **declination** (between geographic and magnetic meridian), then specify the angle within that vertical plane using the angle of **dip**.

### Null point problems

A null point is where a bar magnet's field exactly cancels Earth's horizontal field $B_H$. Its location depends on the magnet's orientation:
- **North pole toward geographic south:** null points lie on the magnet's **axial** line. $\left(\dfrac{\mu_0}{4\pi}\dfrac{2M}{d^3}=B_H\right)$
- **North pole toward geographic north:** null points lie on the **equatorial** line instead. $\left(\dfrac{\mu_0}{4\pi}\dfrac{M}{d^3}=B_H\right)$

Worked examples solve for the null-point distance (e.g. $14$ cm axial, $11.1$ cm equatorial in two separate problems), including a variant asking for the *new* null-point location after the magnet is turned $180°$ (which swaps axial $\leftrightarrow$ equatorial per the rule above).

### The atom as a magnetic dipole

**Also not present in the current rationalised NCERT syllabus** for this chapter (no section derives an atomic/orbital magnetic moment or the Bohr magneton) -- again extra material beyond the current textbook, included here for completeness since it was taught.

Every atom behaves as a tiny magnet: an orbiting electron is a tiny current loop (**orbital** magnetic moment); electron spin contributes a **spin** magnetic moment too (about double the orbital contribution for the same angular momentum, per this lecture). **Direction:** curl the right hand's fingers in the direction of *conventional current* (opposite the electron's actual motion) — thumb gives the direction of $\vec M$, pointing from the loop's south to north face.

#### Orbital magnetic moment derivation
Electron (charge $e$, angular speed $\omega$) in a circular orbit radius $r$: equivalent current $I=e/T=e\omega/2\pi$, loop area $A=\pi r^2$:
$$M = IA = \frac{e\omega}{2\pi}\cdot\pi r^2 = \frac{1}{2}e\omega r^2$$

#### Connecting to Bohr's theory
Angular momentum is quantised: $mvr = \dfrac{nh}{2\pi}$. Using $v=r\omega$: $mr^2\omega = \dfrac{nh}{2\pi}$. Substituting:
$$M = \frac{neh}{4\pi m}$$
For $n=1$ (ground state), this defines the **Bohr magneton**:
$$\boxed{M = \frac{eh}{4\pi m} = \mu_B = 9.27\times10^{-24}~\text{A}\cdot\text{m}^2}$$

#### Alternative form via angular momentum
Since $L = \vec r\times\vec p = mvr = mr^2\omega$, the same result rewrites as:
$$\boxed{M = \frac{e}{2m}L}, \qquad \vec M = -\frac{e}{2m}\vec L~\text{(electron's negative charge flips the direction)}$$
$e/2m$ is the **gyromagnetic ratio** — magnetic moment is directly proportional to angular momentum.


### Verify these spans
- [36:40–39:38] The transcript's real narration follows the Bohr-quantisation derivation closely and reaches M = (1/2)e * (nh/2*pi*m) as its very last segment, essentially arriving at the Bohr magneton result but never simplifying it to the named 'Bohr magneton' with its numerical value, and never mentioning the alternative angular-momentum form M=(e/2m)L or the gyromagnetic ratio at all. A board frame (floor_000116.jpg, t=2300s, within the transcript's own covered time range) shows both of these already written out: the boxed 'for n=1, M=eh/4*pi*m=mu_B=Bohr magneton' with its value 9.27e-24 A.m^2, and a separate derivation via L=r x p leading to M=(e/2m)L (vector form with a minus sign for the electron) plus a right-hand-rule statement for the direction of M. The Bohr-magneton-value and angular-momentum-form claims above are grounded from this frame rather than the transcript's own words.

---

## Magnetizing Intensity, Intensity of Magnetization, Permeability, and Susceptibility

**NCERT sections covered:** 5.4

### Magnetizing intensity, intensity of magnetization, and permeability (NCERT 5.4)

**Magnetizing intensity $H$:** from the solenoid result $B_0=\mu_0 nI$, the quantity $nI$ (turns/length $\times$ current), independent of any material, is called $H$. So $B_0=\mu_0 H$ for an air/vacuum core, or generally $B=\mu H$ with a material core. SI unit: A/m.

**Intensity of magnetization $I$ (or $M$):** a vector, defined as magnetic moment per unit volume of a material placed in the magnetizing field — the material's atomic dipoles align with the field:
$$I = \frac{m}{V}$$
Same SI unit as $H$ (A/m), despite representing a different physical quantity (external coil/current setup vs. the material's own response).

**Magnetic permeability $\mu$:** quantifies how readily a magnetic field can penetrate a material (e.g. an iron bar between magnet poles draws field lines through it far more than air would). $\mu = B/H$. SI units: T$\cdot$m$\cdot$A$^{-1}$ (equivalently Wb$\cdot$m$^{-1}\cdot$A$^{-1}$).

#### Relation between permeability and susceptibility
Total field $B = B_0+B_m = \mu_0 H + \mu_0 I$ (the material's own contribution $B_m=\mu_0 I$ adds to the bare $\mu_0 H$). **Magnetic susceptibility** $\chi_m = I/H$, so $I=\chi_m H$:
$$B = \mu_0 H(1+\chi_m)$$
Comparing with $B=\mu H$:
$$\boxed{\mu = \mu_0(1+\chi_m)}, \qquad \mu_r = \frac{\mu}{\mu_0} = 1+\chi_m$$

#### Worked numericals
- **Rowland ring:** mean radius $15$ cm, $3500$ turns on a ferromagnetic core ($\mu_r=800$), current $1.2$ A. $n=N/2\pi r$, $B=\mu_0\mu_r nI = 4.48$ T.
- **Steel magnet:** $M=2.5$ A$\cdot$m$^2$, mass $6.6$ g, density $7.9\times10^3$ kg/m$^3$. Find $I$: get volume from mass/density, then $I=M/V$.
- **Iron rod:** cross-section $0.2$ cm$^2$, $H=1200$ A/m, $\chi_m=599$. Find $\mu$ and flux $\phi$: $\mu_r=1+\chi_m=600$, $\mu=\mu_0(1+\chi_m)=7.536\times10^{-4}$ T$\cdot$m$\cdot$A$^{-1}$; then $\phi=BA$ with $B=\mu H$.

---
*Note on this lecture's transcript:* the susceptibility relation and all three worked numericals above are grounded entirely from board frames -- the transcript itself never mentions susceptibility at all, instead getting stuck repeating the permeability and magnetization definitions several times over. See the flagged span below.


### Verify these spans
- [07:32–23:52] This is one of the most severely corrupted transcripts found in this project: after cleanly covering magnetizing intensity H and intensity of magnetization I, the transcript's narration of 'magnetic permeability' repeats itself at least four to five times over (near-identical short phrases like 'to which magnetic field can penetrate a material' and 'mu is equal to B upon H' recur at t=452s, 623s, 814s, 997s, and 1129s), then the 'intensity of magnetization' definition is re-transcribed a second time (t=1160-1420s) nearly verbatim from its first pass (t=194-445s) -- all classic delayed-repetition artifacts. Crucially, the transcript NEVER once mentions magnetic susceptibility, despite board frames showing it is thoroughly covered: floor_000047.jpg (t=920s) shows the full permeability-susceptibility relation derivation (chi_m=I/H, mu=mu0(1+chi_m)); floor_000050.jpg through floor_000060.jpg (t=980-1180s) show a complete Rowland-ring numerical; and floor_000060.jpg through floor_000069.jpg (t=1180-1360s) show a magnet intensity-of-magnetization numerical and an iron-rod susceptibility numerical, both fully worked. Roughly the back half of this lecture (everything from the susceptibility relation onward) is grounded entirely from these frames.

---

## Diamagnetic and Paramagnetic Substances, and Curie's Law

**NCERT sections covered:** 5.5

### Diamagnetic, paramagnetic, and (introduced) ferromagnetic substances (NCERT 5.5)

#### Diamagnetic substances
When placed in an external magnetic field, diamagnetic substances get feebly magnetized in the direction **opposite** to the magnetizing field (repelled by a magnet). Examples: Bi, Cu, Sb, Pb, Au, Ag, H$_2$O.

**Explanation:** each atom acts as a magnetic dipole (orbiting electrons contribute dipole moments). In a diamagnetic substance the electrons are *paired* — one clockwise, one anticlockwise — so their dipole moments cancel: $M_\text{net}=0$ with no field. When a field $\vec B$ is applied, the perturbed electron motion gives each atom a net dipole moment **opposite** to $\vec B$.

**Properties:**
1. They move from the **stronger** to the **weaker** part of an external field.
2. When placed in a field, they **expel field lines**: $B<B_0 \Rightarrow \mu<\mu_0 \Rightarrow \mu_r<1$. **Superconductors** are the most extreme (exotic) diamagnets — no field lines pass through at all, $\mu_r=0 \Rightarrow \chi_m=-1$ (from $\mu_r=1+\chi_m$).
3. They are **independent of temperature** — since each diamagnetic molecule is not itself a magnetic dipole, random thermal motion doesn't affect the (induced) magnetization.
4. Freely suspended in a uniform field, they align with their **longest axis perpendicular to $B$** (the minimum-energy orientation, since the material "wants" to expel field lines).

#### Paramagnetic substances
When placed in an external field, paramagnetic substances get feebly magnetized in the **same** direction as $B$ (feebly attracted). Examples: Al, Cr, Li, Mg, Na, K.

**Explanation:** unlike diamagnetic substances, paramagnetic atoms have *unpaired* electrons, so each atom already has a permanent magnetic dipole moment. With no field, thermal motion randomises these — $M_\text{net}=0$. In a field $\vec B$, the dipoles align with $\vec B$, giving $M_\text{net}\ne0$.

**Properties** (opposite of the diamagnetic case):
1. They move from the **weaker** to the **stronger** part of an external field.
2. Field lines **prefer to pass through** them (rather than being expelled).

#### Curie's law
$$I \propto B, \qquad I\propto\frac{1}{T} \quad\Rightarrow\quad I\propto\frac{B}{T}$$
Using $B=\mu H$: $I\propto H/T$, so $I/H \propto 1/T$. Since susceptibility $\chi_m = I/H$:
$$\boxed{\chi_m = \frac{C}{T}}$$
where $C$ is the **Curie constant** — magnetic susceptibility of a paramagnetic material is inversely proportional to absolute temperature.

**Graphs:** $1/\chi_m$ vs. $T$ is a straight line through the origin (slope $1/C$); $I$ vs. $H$ at fixed $T$ is also a straight line through the origin.

---
*Note on this lecture's transcript:* two whole properties sections — diamagnetic property 3 (temperature-independence) and paramagnetic properties 1–2 (weaker→stronger field, field lines preferring to pass through) — are visible on the board but never spoken in the transcript at all, a total-omission gap rather than a timestamp gap. A third graph (I vs. H/T, showing **saturation magnetization** — the real departure from Curie's law at high field/low temperature) is drawn on the board just past where the transcript's own narration stops. All three are grounded from frames alone; see the flagged spans below.


### Verify these spans
- [18:44–20:00] A third property of diamagnetic substances -- 'they are independent of temperature, since (unlike a paramagnetic atom) each diamagnetic molecule is not a magnetic dipole in itself, so random thermal motion of molecules does not affect their magnetization' -- appears clearly on the board (floor_000059.jpg, t=1160s, squarely inside the transcript's own covered timespan 1105-1234s) but is never spoken in the transcript at all: the transcript jumps from discussing superconductors/chi_m=-1 (ending ~1124-1136s) directly to property 4 (alignment perpendicular to B, starting ~1200s) with no trace of this temperature-independence property in between. This claim is grounded entirely from the frame.
- [28:10–30:25] Two properties of paramagnetic substances, directly parallel to (and the opposite of) the diamagnetic properties covered earlier in this same lecture -- (1) they move from the WEAKER to the STRONGER part of an external magnetic field, and (2) field lines prefer to pass through them (rather than being expelled) -- appear clearly on the board (floor_000087.jpg, t=1720s, inside the transcript's covered span 1690-1825s) but are never spoken: the transcript goes directly from 'M net will not be equal to zero' to 'individual atoms of a paramagnetic substance possess permanent magnetic dipole moment... thus M net is equal to zero... curie's law', skipping this properties section entirely.
- [35:47–37:45] The transcript's own narration, in its final segments, describes only two graphs following from Curie's law: 1/chi_m vs T, and I vs H (both straight lines through the origin). A later board frame (floor_000110.jpg, t=2180s, still within the transcript's nominal duration) shows a THIRD graph drawn after the first two: I vs H/T, which rises and then flattens out, explicitly labelled 'saturation magnetization' -- this shows that at sufficiently high field / low temperature, a real paramagnetic material's magnetization saturates rather than continuing to grow linearly as Curie's law (I proportional to H/T) would predict. The transcript's final segment (ending 2301s, itself slightly past the video's measured duration) never reaches this third graph or the word 'saturation' at all, so this content is grounded entirely from the frame and is not independently confirmed by the transcript's own words.

---

## Ferromagnetic Substances and Domain Theory

**NCERT sections covered:** 5.5

### Ferromagnetic substances and domain theory (NCERT 5.5)

**Ferromagnetic substances** get **strongly** magnetized in the direction of an external field (contrast: paramagnetic substances are only feebly magnetized). Examples: iron, cobalt, nickel, and the alloy **Alnico** (Al, Ni, Co, Fe, and some Cu).

#### Domain theory
Each atom has a magnetic dipole moment (as in a paramagnetic substance), but here neighbouring atomic dipoles **interact strongly** and spontaneously align in a common direction over a macroscopic volume called a **domain**. Each domain has its own net dipole moment, but domain directions vary randomly across the sample, so the substance's overall $M_\text{net}=0$ when $B=0$. (This is the key structural difference from paramagnetic substances, which don't form domains at all — there, each individual *atom* is independently randomly oriented.)

When placed in an external field $\vec B$: the domains themselves **orient toward $\vec B$ and grow** — domain boundaries shift so smaller domains merge into bigger ones, approaching one giant domain aligned with $B$. With the domains now aligned, $M_\text{net}\ne0$: the substance behaves as a magnet.

#### Worked numerical (Curie's law, paramagnetic salt)
*(NCERT exercise, pre-rationalisation numbering 5.13)*

A paramagnetic salt has $2\times10^{24}$ dipoles, each of moment $1.5\times10^{-23}$ J/T. Placed in $B_1=0.64$ T, cooled to $T_1=4.2$ K, it reaches $15\%$ magnetic saturation. Find the total dipole moment at $B_2=0.98$ T, $T_2=2.8$ K (assume Curie's law).

- Fully-saturated total moment: $(2\times10^{24})(1.5\times10^{-23}) = 30$ J/T
- At $15\%$ saturation: $M_1 = 0.15\times30 = 4.5$ J/T
- By Curie's law ($M\propto B/T$): $M_2 = M_1\times\dfrac{B_2}{B_1}\times\dfrac{T_1}{T_2}$

---
*Note on this lecture's transcript:* the domain-theory explanation above is transcribed correctly on its first pass, but the ASR then re-transcribes the *same* explanation nearly verbatim four more times back-to-back, filling almost the entire second half of the lecture. Board frames show that, during this same stretch, the teacher had actually moved on to the worked Curie's-law numerical above — none of which made it into the transcript's own words. The numerical is grounded entirely from frames; see the flagged span below.


### Verify these spans
- [06:41–25:51] This transcript has a severe, repeated delayed-repetition problem: the same ~230-word domain-theory explanation ('this domain theory... individual atoms possess dipole moment... they interact... align... called domain... each domain has net M but it varies domain to domain... M net of whole substance is zero... place in external field... domains orient... grow... form giant domain...') is transcribed essentially verbatim FIVE separate times, at approximately t=91-399s (first, genuine pass, matching the board diagrams in floor_000019.jpg), then re-transcribed nearly word-for-word again at t=625-916s, t=918-1143s, t=1129-1371s (this one partially overlapping/out-of-order with the previous), and t=1396-1560s. Only the first pass reflects new content; the other four are ASR hallucinated repeats that silently displaced whatever the teacher actually said during those stretches. Board frames confirm real new content WAS being taught during this displaced time: from floor_000061.jpg (t=1200s) onward, the board shows a full worked Curie's-law numerical (a paramagnetic-salt problem, apparently NCERT exercise 5.13 in the pre-rationalisation numbering) being written and solved, continuing through the last available frame (floor_000074.jpg, t=1460s) -- none of which appears anywhere in the transcript's own words. The numerical is grounded entirely from these frames; the method for the final step (M2 via Curie's law ratio) is the direct, expected completion of the givens shown, but the frames do not show a final computed value for M2, so none is stated here.

---

## Hysteresis Curve: Retentivity, Coercivity, and Soft Iron vs. Steel

**NCERT sections covered:** 5.5

### The hysteresis curve (NCERT 5.5)

A solenoid carries current $I$ with an iron rod (magnetizing material) inside. The **hysteresis curve** plots $B$ (total field inside the material — related to how many of its dipoles are aligned) against $H$ (related to the coil current).

**Tracing the loop:**
- **O:** initially $B=0$, $H=0$ (no current).
- **O$\to$A:** current increased $\Rightarrow$ $H$ increases $\Rightarrow$ $B$ increases (domains align with $B$). At **A**, $B$ stops increasing however much $H$ increases further — this is the **saturation point** (all domains now aligned).
- **A$\to$B:** current (and $H$) decreased back toward zero — but $B$ does *not* retrace the same path. When $H=0$, $B$ is still non-zero: $OB$ is the **retentivity** (residual magnetism) — the material stays magnetized after the current is switched off.
- **B$\to$C:** to bring $B$ back to zero, the current must be **reversed** and increased. Where $B=0$ (with $H\ne0$, reversed) is point $C$: $OC$ is the **coercivity** — the reverse field needed to fully demagnetize. Larger coercivity $\Rightarrow$ harder to demagnetize.
- **C$\to$D$\to$...$\to$A:** increasing the reversed current further reaches negative saturation at $D$; repeating the same steps in the forward direction (through $E$, $F$) closes the loop back at $A$.

**Hysteresis:** the phenomenon of $B$ *lagging behind* $H$ when a magnetic specimen is taken through a cycle of magnetisation. The closed $B$–$H$ curve traced is the **hysteresis loop**.

**Area of the loop** = energy dissipated per unit volume, per cycle (the substance heats up) — the bigger the loop, the greater the dissipation.

### Soft iron vs. steel

Comparing their hysteresis loops (steel's is visibly wider):
1. Retentivity: **steel < soft iron**
2. Coercivity: **steel > soft iron** $\Rightarrow$ steel is used for **permanent magnets** (harder to demagnetize)
3. Loop area: **steel > soft iron** $\Rightarrow$ hysteresis loss in soft iron is **less** $\Rightarrow$ soft iron is used in **electromagnets** (repeatedly (de)magnetized, so low loss matters)

#### Making a permanent magnet
1. Hold an iron/steel rod in the N–S direction and hammer it repeatedly.
2. Hold a steel rod and stroke it repeatedly (many times), always in the same sense, with one end of a bar magnet.

---
*Note on this lecture's transcript:* the loop-construction explanation (saturation, retentivity, coercivity) is transcribed correctly once, then repeated nearly verbatim a second time -- inflating the transcript's own timestamps past the video's true duration. The final soft-iron-vs-steel comparison and the two permanent-magnet methods are visible in full on the board but never make it into the transcript's own words at all (it cuts off announcing the topic). Both are grounded entirely from frames; see the flagged spans below.


### Verify these spans
- [03:53–17:40] The full explanation of the hysteresis curve's construction (saturation at A, decreasing H giving retentivity at B, reversing current to reach coercivity at C, the fourth/fifth steps) is transcribed once correctly (~t=233-660s) and then transcribed a SECOND time nearly verbatim (~t=692-1015s) -- the same delayed-repetition pattern found repeatedly in this chapter's lectures. This inflated the transcript's own self-reported timestamps: its last segment claims to end at 1724.84s even though the video's true duration is only 1661.0s, confirming the internal duplication pushed later timestamps out of sync with real video time. Content-wise nothing appears lost here (the two passes say the same thing), but the timestamps attached to claims in the back half of this note should be read as approximate.
- [26:46–27:41] The transcript's own words announce the final topic twice ('Now we have hysteresis curve for soft iron and steel', repeated) and then cut off mid-sentence while just starting to draw a B-H curve ('I have a curve something like this... A curve main aise draw kar rahi hoon'), giving the impression the lecture ends before this comparison is actually taught. However, a board frame (floor_000067.jpg) -- whose own true video timestamp (t=1320s) falls chronologically BEFORE this final transcript segment's self-reported (drifted, see the span above) timestamp -- shows the soft-iron-vs-steel comparison already fully written out: three comparison properties (retentivity, coercivity, loop area/hysteresis loss) plus two practical methods for making a permanent magnet. This confirms the teacher did complete this topic on the board within the true 1661s runtime; the transcript simply never captured the spoken explanation of it. All of the soft-iron/steel and permanent-magnet content in this note is grounded entirely from that frame, not from the transcript's own words.
