# Electrostatic Potential and Capacitance

*Class XII CBSE Physics · Chapter 2 · 8 lectures, in order.*

*NCERT sections covered: 2.2, 2.3, 2.4, 2.5, 2.6, 2.8, 2.10, 2.11, 2.12, 2.13, 2.14, 2.15.*

*Transcribed from the teacher's recorded lectures and checked against the
board frames and the NCERT text. Equations are board-grounded; any span the
transcript could not resolve confidently is flagged in place.*

---

## Electric Potential: Definition, Relation to Field, Potential Due to a Point Charge and a System of Charges

**NCERT sections covered:** 2.2, 2.3, 2.5

### Electric potential

#### Definition (NCERT 2.2)
Building on electric field intensity (force-based, from the previous chapter), this lecture switches to a work-based description.

**Electric potential difference:**
$$V_A - V_B = \frac{W_{B \to A}}{q_0}$$
the work done by an *external* force per unit charge in moving a test charge from $B$ to $A$, **without acceleration** -- meaning the external force exactly balances the electric force at every point along the path, so the process is quasi-static and no kinetic energy is gained or lost.

**Unit:** $1~\text{volt} = 1~\text{joule/coulomb}$.

**Electric potential at a point** (not just a difference) is the special case where the charge is brought from infinity, with the convention $V(\infty) = 0$:
$$V = \frac{W_{\infty \to P}}{q_0}$$

**Physical significance:** a positive charge moves from high to low potential; a negative charge moves from low to high potential -- the electrical analogue of water flowing from high to low level, or heat flowing from hot to cold.

#### Potential as a line integral of the field
$$V = -\int_B^A \vec{E}\cdot d\vec{l}$$
Derived from $dW = -q_0\vec{E}\cdot d\vec{l}$ (external force is equal and opposite to the electric force) and $V = W/q_0$. Called out in the lecture as a must-know result ("your 2 AM formula").

**Corollary -- the electrostatic field is conservative:**
$$\oint \vec{E}\cdot d\vec{l} = 0$$
Any closed-loop line integral of $\vec E$ vanishes, since the potential difference between two points doesn't depend on the path taken between them.

#### Potential due to a point charge (NCERT 2.3)
$$V(r) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}$$
Falls off as $1/r$ (compare to $E \propto 1/r^2$).

#### Potential due to a system of charges (NCERT 2.5)
Potential obeys superposition -- being a **scalar**, it's a plain sum (no vector addition needed, unlike $\vec E$):
$$V_P = \frac{1}{4\pi\varepsilon_0}\sum_i \frac{q_i}{r_i}$$
with each $q_i$ carrying its own sign.

**Worked example:** at the point $P$ midway between a $+q$ and a $-q$ charge (equidistant, distance $r$ from each):
$$V_P = \frac{1}{4\pi\varepsilon_0}\frac{q}{r} - \frac{1}{4\pi\varepsilon_0}\frac{q}{r} = 0$$
even though $\vec E \ne 0$ at that point. This is the key conceptual takeaway of the section: **potential and field are not simply proportional point-by-point** -- $V=0$ at a point says nothing about whether $E=0$ there, and vice versa.

---
*Note on this lecture's transcript:* the segment covering the point-charge and system-of-charges derivations (roughly the last 2 minutes of the lecture) is not reliable in the ASR transcript -- see the flagged span below. Those claims above are grounded directly in the board frames instead.


### Verify these spans
- [37:15–39:15] Transcript is unreliable here: instead of transcribing the real content actually on the board in this window (potential due to a point charge, then due to a system of charges -- confirmed from frames at t=2140-2320s), the ASR output regresses to repeating the 'significance of potential / high-to-low potential' material from around t=1200s almost verbatim. This looks like a distinct ASR failure mode (content substitution rather than truncation or tail fabrication) -- the claims for this section are grounded entirely in the board frames, not the transcript.

---

## Potential Due to an Electric Dipole, and Potential Energy of a System of Charges

**NCERT sections covered:** 2.4

### Potential due to an electric dipole (NCERT 2.4)

Unlike the earlier electric-field-intensity treatment (which used axial and equatorial special points), here a **general point** $P$ at polar coordinates $(r,\theta)$ from the dipole's center is considered directly.

By superposition (potential is a scalar, so this is simple addition, not vector addition like $\vec E$):
$$V = V_{+q} + V_{-q} = \frac{1}{4\pi\varepsilon_0}\frac{q}{R_1} - \frac{1}{4\pi\varepsilon_0}\frac{q}{R_2}$$

Using the standard far-field approximation (dropping perpendiculars from each charge to the line $OP$, giving $PN \approx AP$ and $ON = L\cos\theta$):

$$V = \frac{P\cos\theta}{4\pi\varepsilon_0\left(r^2 - l^2\cos^2\theta\right)}$$

For $r \gg l$ (the point far from the dipole compared to its size), this simplifies to:
$$\boxed{V = \frac{P\cos\theta}{4\pi\varepsilon_0 r^2}}$$

Two things worth noting against the point-charge result $V \propto 1/r$: dipole potential falls off **faster** ($1/r^2$), and it's **direction-dependent** through $\cos\theta$ — a point charge's potential has no such angular dependence.

#### Special cases
- **Axial** ($\theta = 0$): $V = \dfrac{P}{4\pi\varepsilon_0 r^2}$ (maximum)
- **Equatorial / "broadside"** ($\theta = 90°$): $V = 0$ exactly, since $\cos 90° = 0$ — consistent with the direct superposition argument from the previous lecture (equidistant $+q$ and $-q$ cancel).

#### Worked example
$q = 100\times10^{-9}$ C, separation $2L = 2\times10^{-3}$ m (so $P = 2QL = 2\times10^{-10}$ C·m), evaluated at $r=0.5$ m:
- Axial position: $V = 7.2$ V
- Broadside (equatorial) position: $V = 0$

### Potential energy of a system of point charges

Defined as the total work needed to assemble the charge configuration by bringing each charge in from infinity, one at a time, against the field of the charges already in place.

**Two charges:** bringing $q_1$ in first costs nothing (no field exists yet); bringing $q_2$ to a distance $r$ from $q_1$ costs work equal to (potential due to $q_1$) $\times\, q_2$:
$$U = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r}$$

**Three charges:** sum over every pair, in the order each charge is brought in:
$$U = \frac{1}{4\pi\varepsilon_0}\left[\frac{q_1q_2}{r_{12}} + \frac{q_1q_3}{r_{13}} + \frac{q_2q_3}{r_{23}}\right]$$

**General result, $n$ charges:** every pair contributes exactly once:
$$U = \frac{1}{2}\cdot\frac{1}{4\pi\varepsilon_0}\sum_{i=1}^n\sum_{\substack{j=1\\j\ne i}}^n \frac{q_iq_j}{r_{ij}} \;=\; \frac{1}{4\pi\varepsilon_0}\sum_{i<j} \frac{q_iq_j}{r_{ij}}$$
(the two forms are equivalent -- the first double-counts every pair once from each side and divides by 2; the second restricts to $j>i$ so each pair is counted exactly once directly.)

#### Worked example
Equilateral triangle of side $a = 0.1$ m, with $q_1=q$, $q_2=2q$, $q_3=-2q$ and $q=10^{-6}$ C:
$$U = \frac{1}{4\pi\varepsilon_0}\frac{q^2}{a}\Big[(1)(2) + (1)(-2) + (2)(-2)\Big]$$
evaluated by the lecture to a negative total (a bound, energy-releasing configuration) — worth re-deriving by hand to check the arithmetic rather than trusting the board's final numeric answer verbatim.


---

## Potential Energy in an External Field, and Potential Due to a Charged Sphere

**NCERT sections covered:** 2.5, 2.8

### Potential energy in an external field (NCERT 2.8)

Distinct from Section 2.7 (potential energy of a system of charges due to *their own* mutual field): here the field $E$ (and potential $V$) is produced by **external sources**, not by the charge(s) whose energy we're computing.

#### Potential energy of a single charge (NCERT 2.8.1)
Work done in bringing charge $q$ from infinity to a point at position $\vec r$, against the external potential $V(\vec r)$:
$$\boxed{PE = qV(\vec r)}$$

**Electron-volt:** if a charge of magnitude $e = 1.6\times10^{-19}$ C is accelerated through a potential difference of 1 V, it gains energy $1.6\times10^{-19}$ J -- this quantity of energy is defined as **1 electron-volt**:
$$1~\text{eV} = 1.6\times10^{-19}~\text{J}$$
(A unit of *energy*, built from the volt but not itself a unit of potential.)

#### Potential energy of a system of two charges (NCERT 2.8.2)
Assemble $q_1$ then $q_2$ into the external field region, positions $\vec r_1,\vec r_2$:
- Bringing $q_1$ to $\vec r_1$ costs $q_1V(\vec r_1)$ (work against the external field alone).
- Bringing $q_2$ to $\vec r_2$ costs work against **both** the external field *and* the field now due to $q_1$:
$$W_{q_2} = q_2V(\vec r_2) + \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{12}}$$

Total potential energy of the assembled system:
$$\boxed{PE = q_1V(\vec r_1) + q_2V(\vec r_2) + \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{12}}}$$

*(For reference, the board also carries the dipole-in-external-field result derived from this same equation: $PE = -\vec p\cdot\vec E$ -- covered in more depth in a separate lecture on dipole potential energy.)*

### Electric potential due to a uniformly charged sphere (NCERT 2.5)

#### On the surface
Outside a uniformly charged sphere (charge $q$, radius $R$), the field is identical to that of a point charge $q$ at the centre: $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}$. Integrating from infinity in to the surface:
$$V = -\int_\infty^R \vec E\cdot d\vec l = \frac{1}{4\pi\varepsilon_0}\frac{q}{R}$$
Same value a point charge $q$ at the centre would produce at distance $R$.

#### Inside the sphere
Split the line integral at the surface -- from infinity to $R$ (as above), plus from $R$ inward to the field point:
$$V = -\int_\infty^R \vec E\cdot d\vec l \;+\; \left(-\int_R^{r} \vec E\cdot d\vec l\right)$$
The second term vanishes because $E = 0$ everywhere inside a charged conducting sphere. So:
$$\boxed{V_\text{inside} = V_\text{surface} = \frac{1}{4\pi\varepsilon_0}\frac{q}{R}}$$

**Key takeaway:** potential inside the sphere is *constant*, equal to the surface value -- even though the field itself is zero throughout the interior. (Zero field means no *change* in potential, not zero potential; this is the same field/potential distinction flagged in the very first lecture of this chapter.)

---
*Note on this lecture's transcript:* the final ~340 seconds, covering the sphere derivation above, are not reliably transcribed -- see the flagged span below. Those two claims are grounded directly in the board frames instead.


### Verify these spans
- [17:40–23:20] Board frames (floor_000054 at t=1060s: blank new page; floor_000055 at t=1080s: 'Electric potential on surface of sphere' heading just begun; floor_000063 at t=1240s and floor_000067 at t=1320s: the full surface-and-inside-sphere derivation, reaching a concluding statement) show this final ~340s of the lecture is spent on the sphere-potential derivation named in the lecture's own title. The ASR transcript never once mentions a sphere, surface, or conductor anywhere in its 38 segments -- instead its last ~30 segments (from roughly 790s to the claimed end at 1421s) continue elaborating the two-charges-in-external-field material, well past where the board shows that topic was finished (page 1, visible complete by ~t=520s) and a new page begun. This reads as sustained content substitution: real audio about the sphere derivation went untranscribed, replaced by an extended rehash of already-covered material. Automated coverage checks (duration-fabrication and repetition-loop detectors) did not catch it, since the substituted text is paraphrased rather than verbatim-repeated and its final timestamp (1421.1s) is close to the true 1400.47s duration. The two sphere claims above are grounded entirely in the board frames, not the transcript.

---

## Equipotential Surfaces, and an Introduction to Dielectric Polarisation

**NCERT sections covered:** 2.6, 2.10

### Equipotential surfaces (NCERT 2.6)

#### Definition
A surface drawn in an electric field such that the electric potential is the same at every point of it. For points $A,B,C,D$ all on one such surface around a charge $q$:
$$V_A = V_B = V_C = V_D$$

#### E is always perpendicular to an equipotential surface
If $\vec E$ had any component *along* the surface, moving a test charge in that direction would require work -- but work done between any two points of an equipotential surface is zero (no potential difference between them, by definition). So $\vec E$ can have no tangential component: it must be purely normal to the surface everywhere.

**Corollary:** the surface of a conductor in electrostatic equilibrium is itself an equipotential surface (no tangential $E$ on/inside a conductor at equilibrium).

#### Reading direction and relative magnitude of V from E = -dV/dr
$$\vec E = -\frac{dV}{dr}$$
The **negative sign** means $\vec E$ points in the direction of *decreasing* potential -- not increasing. This gives a fast way to answer "which of two points is at higher potential / which way does $E$ point" questions: follow the field lines from high potential to low potential (for $-q$: field lines point *into* the charge, so potential increases as you move away from it; for $+q$: field lines point *away*, so potential decreases as you move away).

#### Spacing between equipotential surfaces
For a **fixed** potential difference $dV$ between successive equipotential surfaces, the spacing $dr$ between them is set by $E = -dV/dr$, i.e. $dr \propto 1/E$:
- Where the field is **stronger**, equipotential surfaces are drawn **closer together**.
- Where the field is **weaker**, they are drawn **farther apart**.

This is the visual companion to field-line density: both crowd together where $E$ is large.

#### Equipotential surfaces for a uniform field
For a uniform $\vec E$ (e.g. between parallel plates), equipotential surfaces are **planes perpendicular to $\vec E$**, equally spaced (since $E$ doesn't vary, equal $dV$ steps mean equal $dr$ steps throughout).

### Electric polarisation -- introduction (NCERT 2.10)

**Free charges** exist in conductors (metals) and are free to move through the material. **Bound charges** are the electrons and ions bound within the atoms/molecules of an insulator -- they cannot move freely through the material. Insulators are also called **dielectrics**.

**Electric polarisation:** when a dielectric is placed in an external electric field, each molecule's positive and negative charge get displaced relative to each other (a simplified picture of an induced dipole forming), even though no charge actually leaves the material. This relative displacement, summed across the dielectric, is what's meant by polarisation.

---
*Note on this lecture's transcript:* the transcript stops right at the introduction of polarisation -- board pages visible later in this same recording carry more advanced dielectric material (polar/non-polar molecule classification, a quantitative polarisation formula) that the transcript's own narration never reaches, and at least one other visible page (an "electrostatic shielding" page) doesn't belong to this lecture's spoken content at all. See the flagged span below -- only the qualitative polarisation definition above, independently confirmed by the transcript's own words, is treated as covered by this lecture.


### Verify these spans
- [34:00–45:40] Board frames in this window (e.g. floor_000103 at t=2040s: polar vs non-polar molecule classification with examples H2O/HCl/CO, induced-charge diagram; floor_000138 at t=2740s: polarisation vector P = q_i.t/(A.t) = q_i/A with SI unit C/m^2, and 'susceptibility of a dielectric') show substantially more advanced dielectric material than the transcript's own narrated content ever reaches -- the transcript's last 51st segment (2900.5-2955.6s) is still at the introductory 'one molecule gets displaced, simplified model' stage. Two other frames sampled in this same document (floor_000066 at t=1300s and floor_000074 at t=1460s) show an unrelated 'electrostatic shielding / Faraday's cage' page that has no correspondence anywhere in this lecture's transcript at all, confirming this recording's slide document contains material from other classes that the teacher scrolls past or pre-writes without narrating in this particular video. For that reason the polar/non-polar classification and the P=q_i/A formula are NOT included as grounded claims above -- only the qualitative polarisation definition that the transcript itself independently states is included.

---

## Capacitors and Capacitance: Basics, Isolated Sphere, Spherical Capacitor, Cylindrical Capacitor

**NCERT sections covered:** 2.11

### Capacitors and capacitance (NCERT 2.11)

#### Capacitance of a conductor
As charge $Q$ on a conductor increases, its potential $V$ rises proportionally: $Q \propto V$, so
$$Q = CV$$
where $C$, the **capacitance**, is a constant depending only on the conductor's geometry (independent of $Q$ and $V$ themselves). On a $Q$–$V$ graph this is a straight line through the origin; its slope gives $C$.

**Unit:** $1~\text{farad} = 1~\text{coulomb/volt}$ (named for Faraday). **Worked example:** $Q = 10~\mu\text{C}$ raising the potential by $2.5$ V gives $C = Q/V = 4\times10^{-6}$ F.

#### Why two plates, not one
A single charged plate's potential rises so much (for a modest amount of charge) that the surrounding air can ionise and charge starts leaking away. Bringing a second, **grounded** plate close by induces opposite charge on it, which sharply lowers the first plate's potential for the *same* stored charge — allowing far more charge to be stored before breakdown. A **capacitor** is this pair of two neighbouring conductors carrying equal and opposite charge. Common shapes: parallel-plate, spherical, and cylindrical (coaxial) capacitors.

#### What capacitance depends on
$C$ does **not** depend on $Q$ or $V$ individually (only their ratio) — it depends purely on **geometry**: plate area (directly proportional), separation $d$ (inversely proportional), and the medium between the plates (increases with dielectric constant $K$). For a parallel plate capacitor, $C = K\varepsilon_0 A/d$ (stated here; derived from first principles in a later lecture).

#### Capacitance of an isolated spherical conductor
A single charged sphere (charge $Q$, radius $R$), with the "other plate" taken at infinity:
$$V = V_A - V_B = \frac{Q}{4\pi\varepsilon_0 R} - 0 \quad\Rightarrow\quad C = \frac{Q}{V} = 4\pi\varepsilon_0 R \;\;(\text{or } 4\pi\varepsilon_0 KR \text{ with a dielectric of constant } K)$$
So $C \propto R$. **Worked example:** modelling Earth as a spherical conductor of radius $6400$ km gives $C_\text{Earth} \approx 711~\mu\text{F}$.

#### Capacitance of a spherical capacitor
Two concentric spherical conductors: inner sphere charge $+Q$ at radius $r_1$, outer shell $-Q$ (grounded) at radius $r_2$. Using a Gaussian surface at radius $r$ between them ($E = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}$ in that region only):
$$V = -\int_{r_1}^{r_2}\vec E\cdot d\vec r = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{r_1}-\frac{1}{r_2}\right) = \frac{Q}{4\pi\varepsilon_0}\frac{r_2-r_1}{r_1 r_2}$$
$$\boxed{C = \frac{Q}{V} = \frac{4\pi\varepsilon_0\, r_1 r_2}{r_2-r_1}}$$

#### Capacitance of a cylindrical capacitor
Two coaxial cylinders of length $L$: inner radius $a$ carrying linear charge density $+\lambda$, outer radius $b$ carrying $-\lambda$ (grounded). Between them, Gauss's law gives $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$:
$$V = -\int_b^a \vec E\cdot d\vec r = \frac{\lambda}{2\pi\varepsilon_0}\ln\!\left(\frac{b}{a}\right)$$
With $\lambda = Q/L$:
$$\boxed{C = \frac{Q}{V} = \frac{2\pi\varepsilon_0 L}{\ln(b/a)}}$$

---
*Note on this lecture's transcript:* the two derivations above (spherical capacitor, cylindrical capacitor) are grounded entirely in board frames -- the transcript itself does not contain them at all; see the flagged span below for what happened instead. Also note: NCERT's core text (Section 2.11) covers capacitance of a single (isolated) conductor and states the general definition, but does not itself carry closed-form spherical/cylindrical capacitor derivations -- these two results are standard board/exam extensions beyond the strict textbook section, not verified against an NCERT-stated formula, though they follow directly from the same first principles ($V=-\int\vec E\cdot d\vec l$, Gauss's law) taught earlier in the chapter.


### Verify these spans
- [17:40–32:06] This is the most severe transcript failure found in this chapter so far. Board frames show the isolated-sphere derivation is essentially complete by t=1060s (floor_000054); by t=1220s (floor_000062) the board has already moved on to a NEW page titled 'capacitance of a spherical capacitor' with a two-conductor Gaussian-surface diagram; by t=1440s (floor_000073) that derivation is fully worked out to a boxed capacitance formula; by t=1700s (floor_000086) a further new page 'capacitance of a cylindrical capacitor' has begun; and by t=1900s (floor_000096, just 26s before the lecture's true end) that derivation too is complete with a boxed final formula -- exactly the two topics ('spherical, cylindrical') named in this lecture's own filename. The ASR transcript, however, does not follow any of this: from roughly t=1092s to t=1866s it transcribes the SAME 'isolated spherical conductor' derivation (including the identical Earth/711-microfarad example, down to near-identical sentence wording) TWICE in a row, then cuts off mid-sentence at t=1925s ('And say this is the second sphere, okay, surrounding it') just as it appears to begin the topic the board had already finished twenty minutes of board-time earlier. Automated coverage checks did not flag this: the repeated block is not adjacent-duplicate text (a few short transitional segments separate the two copies) so the repetition-loop detector missed it, and the final timestamp lands within the true duration so the duration-fabrication check also passed. The two capacitor-formula claims above (spherical and cylindrical) are grounded entirely from board frames, with no transcript corroboration at all.

---

## Capacitance of a Parallel Plate Capacitor: No Dielectric, Fully Filled, Partially Filled

**NCERT sections covered:** 2.12, 2.13

### Capacitance of a parallel plate capacitor (NCERT 2.12, 2.13)

#### Without dielectric (medium = air/vacuum)
Plates of area $A$, separation $D$. Field between the plates: $E = \dfrac{\sigma}{\varepsilon_0} = \dfrac{Q}{A\varepsilon_0}$. Since $Q=CV$ and (for a uniform field) $V = ED$:
$$V = \frac{QD}{A\varepsilon_0} \quad\Rightarrow\quad \boxed{C = \frac{A\varepsilon_0}{D}}$$

#### With dielectric completely filling the gap (dielectric constant $K$)
Inside the dielectric the field is reduced by a factor of $K$: $E = \dfrac{\sigma}{K\varepsilon_0} = \dfrac{Q}{AK\varepsilon_0}$. The same route as above gives:
$$\boxed{C = \frac{KA\varepsilon_0}{D}}$$
Capacitance increases by a factor of $K$ compared to the no-dielectric case. (Real capacitors are commonly built this way -- e.g. paper capacitors, electrolytic capacitors -- using a dielectric layer between the plates.)

#### With a dielectric slab partially filling the gap
Slab of thickness $t < D$ and dielectric constant $K$ inserted between the plates (remaining $D-t$ is air). The field is $\sigma/\varepsilon_0$ across the air gap and $\sigma/(K\varepsilon_0)$ across the slab; adding the two potential-drop contributions:
$$V = \frac{Q}{A\varepsilon_0}\left[(D-t) + \frac{t}{K}\right] \quad\Rightarrow\quad \boxed{C = \frac{A\varepsilon_0}{D-t+\dfrac{t}{K}}}$$

**General shortcut** for any number of stacked layers (dielectric slabs and/or air gaps) between the plates:
$$C = \frac{A\varepsilon_0}{\dfrac{t_1}{K_1}+\dfrac{t_2}{K_2}+\cdots}$$
where each $t_i$ is a layer's thickness and $K_i$ its dielectric constant (air is just a layer with $K=1$). The single-slab case above is the special case $t_1=t,\,K_1=K$ and $t_2=D-t,\,K_2=1$.

#### Consistency checks
- Setting $t=D$ (slab fills the entire gap) in the partially-filled formula reduces it to $C = KA\varepsilon_0/D$ -- matching the fully-filled result, as it must.
- If the inserted slab is a **metal** rather than a dielectric, that's the limit $K\to\infty$: $C \to \infty$.

---
*Note on this lecture's transcript:* the two consistency-check results above are grounded from a board frame near the true end of the audio; the transcript itself doesn't reach them. See the flagged span below.


### Verify these spans
- [11:00–13:22] Board frame floor_000034.jpg (t=660s, comfortably within the true 802.67s duration) shows two consistency checks worked out after the main partially-filled-dielectric formula: substituting t=D to recover the fully-filled result, and the K->infinity (metal slab) limit giving C->infinity. Neither appears anywhere in the transcript's 37 segments, which end (at a coherent, naturally-concluding sentence) on the T1/K1+T2/K2 shortcut applied to this lecture's specific numbers. This is a much smaller gap than the severe substitution found in the previous lecture (14 ch2 capacitors) -- most likely a short board-only aside that went untranscribed near the true end of the audio, rather than sustained content substitution. The metal-slab/K-to-infinity claim above is grounded from the board frame only.

---

## Force Between Capacitor Plates, Energy Stored, Energy Density, and Combination of Capacitors

**NCERT sections covered:** 2.14, 2.15

### Force between the plates of a capacitor (NCERT 2.14 context)

The force on plate 1 is due to the field produced by plate 2 *alone* (a plate cannot exert a net force on its own charge), so the relevant field is $E = \sigma/2\varepsilon_0$, not the full inter-plate field $\sigma/\varepsilon_0$:
$$F = \left(\frac{\sigma}{2\varepsilon_0}\right)q = \frac{q^2}{2A\varepsilon_0}$$
The plates attract each other with this force.

### Energy stored in a capacitor (NCERT 2.15)

Charging a capacitor means moving successive small charges $dQ$ onto it against the potential $V=Q/C$ already built up. Total work done charging from $0$ to final charge $q$:
$$U = \int_0^q \frac{Q}{C}\,dQ = \frac{q^2}{2C} = \frac{1}{2}CV^2 = \frac{1}{2}qV$$

**Subtlety worth remembering for exams:** the battery does total work $QV$, but only **half** of that, $\frac{1}{2}QV$, ends up stored as the capacitor's potential energy. The other half is dissipated as heat in the connecting wires during charging -- both statements are correct simultaneously, they're just different quantities.

#### Energy density
Starting from $U = \frac{1}{2}Q^2/C$ with $C = K\varepsilon_0 A/d$ and $Q = K\varepsilon_0 E A$ (from $\sigma = Q/A = K\varepsilon_0 E$), and using $\text{volume} = Ad$:
$$\boxed{u = \frac{U}{Ad} = \frac{1}{2}K\varepsilon_0 E^2}$$
the electrostatic energy stored per unit volume of the field region (NCERT states the vacuum case $u=\frac12\varepsilon_0E^2$; this is the direct generalisation for a linear dielectric medium of constant $K$, using the field actually present inside it).

### Combination of capacitors (NCERT 2.14)

#### Series (2.14.1)
Every capacitor in series carries the **same charge** $Q$ (by induction at each junction — the series analogue of current, not voltage, being shared in series resistors), while voltages **add**:
$$V = V_1+V_2+V_3 = \frac{Q}{C_1}+\frac{Q}{C_2}+\frac{Q}{C_3} \quad\Rightarrow\quad \boxed{\frac{1}{C_\text{eff}} = \frac{1}{C_1}+\frac{1}{C_2}+\frac{1}{C_3}}$$
Structurally the *opposite* of series resistors, where $R_\text{eff}=R_1+R_2+R_3$ directly.

#### Parallel (2.14.2)
Every capacitor sees the **same voltage** $V$; capacitances simply add:
$$\boxed{C_\text{eff} = C' + C''}$$

#### Balanced Wheatstone-bridge network of capacitors
For a bridge arrangement of five capacitors $C_1,\dots,C_5$ ($C_5$ bridging the two midpoints), if
$$\frac{C_1}{C_2} = \frac{C_3}{C_4}$$
the bridge is **balanced** and $C_5$ carries no charge — it can simply be removed from the circuit, leaving a plain series–parallel reduction of $C_1$–$C_4$.

---
*Note on this lecture's transcript:* the raw ASR transcript repeats the energy-density derivation (the "$\frac12K\varepsilon_0E^2$" section, roughly t=934s onward) two-to-three times in a row with different timestamps before moving on -- a delayed-repetition artifact, not a sign the teacher re-taught it live (a single board frame, floor_000038.jpg, shows the derivation written out exactly once). The physics content above reflects that single, real derivation; the duplicate text was not used for anything beyond confirming the same content twice.


---

## Redistribution of Charges, Dielectric Strength, and Kirchhoff's Laws for Capacitor Networks

**NCERT sections covered:** 2.11

### Redistribution of charges (NCERT 2.11, cf. Example 2.10)

Two capacitors, separately charged ($Q_1=C_1V_1$, $Q_2=C_2V_2$), connected together (positive plate to positive plate): once connected, charge redistributes until both reach the **same potential** $V$. This makes them effectively **parallel** (same $V$, different $Q_1', Q_2'$), even though the connection can visually resemble a series arrangement.

By charge conservation, $Q_1+Q_2 = Q_1'+Q_2'$, and the common potential is:
$$V = \frac{Q_1+Q_2}{C_1+C_2} = \frac{C_1V_1+C_2V_2}{C_1+C_2}$$

#### Energy loss on redistribution
Even though charge is conserved, energy is **not**. Using $U=\frac12CV^2$ for the initial (separate) and final (common-potential) states and simplifying:
$$\Delta U = U_i - U_f = \frac{1}{2}\frac{C_1C_2}{C_1+C_2}(V_1-V_2)^2$$
This is always $\geq 0$ (a squared quantity), so $U_i \geq U_f$ whenever $V_1\neq V_2$ — the "lost" energy is dissipated as heat in the connecting wires during the transient redistribution. Nothing about this process is free.

**Worked numerical** (matching the structure of NCERT Example 2.10): a $10~\mu\text{F}$ capacitor charged by $30$ V DC is connected to an uncharged $50~\mu\text{F}$ capacitor — find the common potential, the initial and final energies, and account for the difference.

#### Worked example: which way do charges flow?
Two spheres — radius $r$ with charge $+q$, radius $R$ with charge $+Q$ — connected by a wire. Using potential-inside-a-sphere-equals-potential-on-surface (from an earlier lecture):
$$V_A - V_B = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{r}-\frac{1}{R}\right)$$
Since $r<R$, this is positive, so $V_A > V_B$: charges flow from the **smaller** sphere to the **larger** one. The general rule is charges flow from **higher to lower potential**, not simply from "more charge" to "less charge" — the two are not the same thing.

### Dielectric strength (NCERT 2.11)

Distinct from dielectric constant $K$ (dimensionless): the **dielectric strength** of a material is the maximum electric field it can withstand without breakdown of its insulating property. Vacuum's dielectric strength is infinite (nothing there to ionise); air's is about $3\times10^6$ V/m. Beyond this field, bound charges get torn free and the material starts conducting, letting stored charge leak away — this is why a capacitor's practical charge-storage limit is set by breakdown, not just by $C=Q/V$ alone.

### Kirchhoff's laws for capacitor networks

1. **Charge conservation in an isolated system:** the net charge is constant, $\sum Q = 0$ for any change.
2. **Loop rule:** around any closed loop in a capacitor network, $\sum V + \sum \dfrac{Q}{C} = 0$ — the capacitor-network analogue of Kirchhoff's voltage law used for resistor circuits (covered in the Current Electricity chapter).

---
*Note on this lecture's transcript:* the Kirchhoff's-laws section above is grounded entirely from a board frame -- the transcript's own narration never reaches it, instead getting stuck repeating a dielectric-strength worked example and ending on an unresolved question. See the flagged span below.


### Verify these spans
- [38:00–43:10] Board frames show a page titled 'Kirchhoff's laws in capacitors' beginning to be written at t=2120s (floor_000107, page still blank) and fully complete with both stated laws and a worked circuit by t=2240s (floor_000113) -- comfortably within this lecture's own duration and matching the third topic named in its filename. The transcript, however, never once mentions Kirchhoff -- its own narration is still mid-way through the dielectric-strength discussion (vacuum/air breakdown fields, a paper-capacitor breakdown example, and a 'can you charge a 1m-radius sphere with 1 coulomb?' worked question) right up to its last segment at t=2603s, with the paper-breakdown example itself repeated near-verbatim twice (t=2378-2467s and again t=2499-2581s) before the transcript ends without ever resolving the sphere-charging question. This matches the same delayed-repetition-then-substitution pattern found in other lectures in this chapter. The Kirchhoff's-laws claim above is grounded entirely from the board frame; the dielectric-strength claim above uses only the transcript's first (non-duplicated) pass through that material.
