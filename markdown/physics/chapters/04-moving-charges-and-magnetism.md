# Moving Charges and Magnetism

*Class XII CBSE Physics · Chapter 4 · 8 lectures, in order.*

*NCERT sections covered: 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9.*

*Transcribed from the teacher's recorded lectures and checked against the
board frames and the NCERT text. Equations are board-grounded; any span the
transcript could not resolve confidently is flagged in place.*

---

## Oersted's Experiment, Biot-Savart Law, and Field at the Centre of a Coil

**NCERT sections covered:** 4.1, 4.4, 4.5

### Historical introduction (NCERT 4.1)
Magnetism was first known through **lodestone**, a naturally magnetised form of magnetite (an iron ore, $\text{Fe}_3\text{O}_4$), which attracts small pieces of iron. The realisation that electricity and magnetism are connected -- that electricity can produce a magnetic field and a magnetic field can (in turn) produce an electric field -- gave rise to the unified subject of **electromagnetism**, associated with Faraday and Maxwell. A moving charge, or equivalently a **current element** $I\,d\vec l$ (a small length $d\vec l$ of current-carrying wire), is a source of magnetic field.

#### Oersted's experiment
A compass needle placed near a current-carrying wire deflects when current flows, showing that a current-carrying wire produces a magnetic field around it -- the first experimental link between electricity and magnetism.

**Teacher's 'SNOW' deflection rule** (a memory device, not itself an NCERT term): if current flows from **S**outh to **N**orth and the wire is **O**ver the needle, the needle's north pole deflects toward **W**est. Reversing the current direction (N to S) flips the deflection to East; placing the wire below the needle instead of above it also flips the result. Physically this is just a special case of the general right-hand rule for the circular field around a straight wire, applied to the fixed N-S rest orientation of a compass needle.

### Magnetic field lines
Compared with electric field lines (Chapter 1):
- **Magnetic field lines always close on themselves** (outside a bar magnet they run N $\to$ S; inside the magnet, S $\to$ N) -- there is no starting or ending point.
- **Electric field lines never form closed loops** -- they start on positive charge and terminate on negative charge. This is the key structural difference between the two, and NCERT states it explicitly (Sec. 4.4, and again in the chapter summary).
- Field lines of either kind **never intersect**: at a crossing point the tangent (which gives the field direction) would have to point in two directions at once, which is impossible.
- **Parallel, equally spaced lines** indicate a **uniform** field; **crowded** lines indicate a stronger field magnitude.

### Biot-Savart law (NCERT 4.4)
For a current element $I\,d\vec l$ carrying current $I$, the magnetic field $d\vec B$ it produces at a point $P$, a distance $r$ away, obeys:

1. $dB \propto I\,dl$
2. $dB \propto \sin\theta$, where $\theta$ is the angle between the current element and the line joining the element to $P$
3. $dB \propto \dfrac{1}{r^2}$

Combining these (in exact analogy with Coulomb's law, replacing $\frac{1}{4\pi\varepsilon_0}$ with $\frac{\mu_0}{4\pi}$):
$$dB = \frac{\mu_0}{4\pi}\,\frac{I\,dl\sin\theta}{r^2}$$

In vector form, since the $\sin\theta$ dependence signals a cross product:
$$d\vec B = \frac{\mu_0}{4\pi}\,\frac{I\,d\vec l \times \hat r}{r^2} = \frac{\mu_0}{4\pi}\,\frac{I\,d\vec l \times \vec r}{r^3}$$

#### Finding the direction of $d\vec B$
Three equivalent right-hand rules were used on the board:
1. **Right-hand palm rule:** point the thumb along the current, the centre finger toward $P$; the palm then faces the direction the field emerges from (out of the page $\odot$, or into the page $\otimes$).
2. **Right-hand thumb rule (for a straight wire):** hold the wire with the thumb pointing along the current; the curled fingers give the sense of circulation of $\vec B$ around the wire.
3. **Right-hand screw rule:** $\vec B$ is perpendicular to the plane containing $d\vec l$ and $\hat r$, in the sense obtained by imagining the rotation carrying $d\vec l$ toward $\hat r$ -- this is the exact rule NCERT itself gives as a footnote to the Biot-Savart law. This rule, and the label "$\mu_0$ = permeability of free space", appear worked out on the board but are **not narrated in the transcript at all** -- see the flagged span below.

**Worked example** (from the board): for a vertical wire carrying current downward, with $P$ to its side, the palm-rule construction (thumb down, centre finger toward $P$) gives a palm facing outward, so $\vec B$ at $P$ points out of the page.

### Magnetic field at the centre of a current-carrying circular coil (NCERT 4.5, special case)
For a circular coil of radius $R$ carrying current $I$, every current element $I\,dl$ on the coil is at the same perpendicular distance $R$ from the centre, with $\theta = 90^\circ$ (so $\sin\theta = 1$). By the Biot-Savart law,
$$dB = \frac{\mu_0}{4\pi}\frac{I\,dl}{R^2}$$
Integrating around the full circumference ($\oint dl = 2\pi R$):
$$B = \oint dB = \frac{\mu_0}{4\pi}\frac{I}{R^2}(2\pi R)$$
$$\boxed{B = \frac{\mu_0 I}{2R}}$$
This matches NCERT's own derivation in Sec. 4.5, which reaches the same field-at-the-centre result as the $x=0$ special case of the more general on-axis formula $B = \dfrac{\mu_0 I R^2}{2(x^2+R^2)^{3/2}}$ (the general axis formula itself is developed in the next lecture). The board also sketches the closed-loop field-line pattern threading through a current-carrying loop, consistent with NCERT Fig. 4.10.


### Verify these spans
- [36:50–37:17] Board frames (floor_000068 at 1340s, floor_000077 at 1520s) show a third direction rule -- the 'right-hand screw rule', with a diagram and the label 'mu0 = permeability of free space' -- fully written out on the same page as rules 1 and 2. The transcript, however, never narrates this rule or these words at all ('screw' and 'permeability' have zero hits across the full 141-segment transcript): after finishing rule 2 (right-hand thumb rule, ending ~2210s) it jumps directly to a worked direction example at 2237s and then on to the coil derivation. Automated coverage and repetition checks both pass cleanly here (no duplicated block, no duration overshoot) -- this is a case of the ASR silently skipping real board content rather than looping, not a duration or repetition failure. The screw-rule claim above is grounded from the board frames alone.

---

## Magnetic Field on the Axis of a Coil, and Ampere's Circuital Law

**NCERT sections covered:** 4.5, 4.6

### Magnetic field on the axis of a circular current loop (NCERT 4.5)
Building on the previous lecture's centre-of-coil result, this lecture derives the field at a general point $P$ on the **axis** of a circular loop of radius $R$ carrying current $I$, at distance $x$ from the centre $O$.

**Setup.** A current element $I\,d\vec l$ at point $A$ on the loop is at distance $r$ from $P$. Since the loop lies in a plane through $O$ perpendicular to the axis, $d\vec l$ and the displacement vector $\vec r$ (from the element to $P$) are (very nearly) perpendicular, so $\sin\theta \approx 1$ and the Biot-Savart law gives
$$dB = \frac{\mu_0}{4\pi}\frac{I\,dl}{r^2}$$
$d\vec B$ is perpendicular to the plane containing $d\vec l$ and $\vec r$, and can be resolved into a component $dB\sin\alpha$ along the axis and $dB\cos\alpha$ perpendicular to it, where $\alpha$ is the angle between $\vec r$ and the axis.

**Symmetry argument.** For every element, the diametrically opposite element (same distance $r$, same $\alpha$) produces a field whose perpendicular component is equal and opposite -- so all perpendicular ($\cos\alpha$) components cancel around the full loop, while the axial ($\sin\alpha$) components all add. Hence the net field lies entirely along the axis:
$$B = \oint dB\sin\alpha$$

**Completing the integral.** Using $\sin\alpha = R/r$ and $r=(R^2+x^2)^{1/2}$ (Pythagoras), and $\oint dl = 2\pi R$:
$$B = \frac{\mu_0}{4\pi}\frac{I}{r^2}\cdot\frac{R}{r}\cdot 2\pi R = \frac{\mu_0}{4\pi}\frac{I\,(2\pi R)\,R}{(R^2+x^2)^{3/2}}$$
$$\boxed{B = \frac{\mu_0\, I\, R^2}{2\,(R^2+x^2)^{3/2}}}$$
Setting $x=0$ recovers $B=\dfrac{\mu_0 I}{2R}$, matching the direct centre-of-coil derivation from the previous lecture -- exactly the check NCERT itself makes in Sec. 4.5.

### Ampere's Circuital Law and its first application (NCERT 4.6)
*(This entire section is grounded from board frames only -- the transcript does not narrate it. See the flagged span below for why, and the strong corroborating evidence from the very next lecture.)*

**Statement.** The line integral of the magnetic field along the boundary of any closed path (an "Amperian loop") equals $\mu_0$ times the net current enclosed by that path:
$$\oint \vec B \cdot d\vec l = \mu_0 I_e$$

**Application: infinitely long straight current-carrying wire.** Take a circular Amperian loop of radius $r$ centred on the wire. By symmetry $B$ is constant in magnitude on the loop and everywhere tangential to it (parallel to $d\vec l$, so $\vec B\cdot d\vec l = B\,dl$):
$$\oint \vec B\cdot d\vec l = B\oint dl = B(2\pi r) = \mu_0 I \quad\Rightarrow\quad \boxed{B = \frac{\mu_0 I}{2\pi r}}$$
This is the same result NCERT reaches via Ampere's law in Sec. 4.6 (Eq. 4.14).

**Finite-wire generalisation.** For a straight wire of finite length, with $P$ at perpendicular distance $r$ and the two ends subtending angles $\alpha_1,\alpha_2$ at $P$:
$$B = \frac{\mu_0 I}{4\pi r}\left(\sin\alpha_1 + \sin\alpha_2\right)$$
As the wire becomes infinite, $\alpha_1,\alpha_2 \to 90^\circ$, so $\sin\alpha_1+\sin\alpha_2\to 2$ and the formula correctly reduces to $B=\dfrac{\mu_0 I}{2\pi r}$ -- the board explicitly checks this consistency between the Biot-Savart (finite-wire) and Ampere's-law (infinite-wire) results.


### Verify these spans
- [15:40–23:29] This lecture's filename promises both 'B at axis of coil' AND 'Ampere circuital law', but the transcript (85 segments, clean coverage ratio 1.012, zero flagged near-duplicate pairs from the delayed-repetition scan) never once mentions Ampere, 'circuital', or an enclosed/boundary current -- every single segment, right up to the last one ending at 1426.7s, narrates only the on-axis-of-a-coil derivation (culminating in the x=0 sanity check against the earlier centre-of-coil result). Board frames tell a different story: by t=940s (floor_000048) the page has already turned to a heading 'Ampere circuital law:'; by t=1040s (floor_000053) the full boxed statement (closed-loop integral of B.dl = mu0*I_e) is written; and by t=1240-1380s (floor_000063/67/70, still comfortably inside the true 1409.8s duration) a complete first application -- straight-wire Amperian loop giving B=mu0*I/(2*pi*r), plus the finite-wire generalisation B=(mu0*I/4*pi*r)(sin a1+sin a2) checked against the infinite-wire limit -- is fully worked out with diagrams. This is corroborated independently by the very next lecture in this chapter (file 1xP2VppJSiqby6nk4Gys--lX5GeM1TGNg, 'Solenoid and toroid'), whose transcript opens mid-thought with 'let us try to see the SECOND application of your ampere circuital law that is magnetic field due to a solenoid' -- confirming a first application (straight wire, via Ampere's law) really was taught, immediately before that. So the real audio almost certainly does contain the Ampere's-law statement and straight-wire derivation somewhere in this lecture's second half; the ASR simply never transcribes it, instead only ever narrating the coil-axis algebra, all the way to the true duration boundary. Neither the coverage check nor the adjacent/delayed-duplicate detectors catch this, because nothing is fabricated or repeated -- real content is silently missing rather than replaced by a copy. All three Ampere's-law claims above are grounded from board frames (and the lecture-3 cross-reference) alone, with no transcript span.

---

## Magnetic Field Due to a Solenoid and a Toroid, and Inside/Outside a Current-Carrying Conductor

**NCERT sections covered:** 4.6, 4.7

### The solenoid (NCERT 4.7)

A long wire wound as a closely-packed helix. If closely wound (no gaps) and long, individual turns' fields add up along the axis to give a **uniform field inside**. Applying Ampere's circuital law with a rectangular Amperian loop (one side of length $l$ inside the solenoid parallel to the axis, the opposite side far outside where $B\approx0$, the two connecting sides perpendicular to $\vec B$ so $\vec B\cdot d\vec l=0$ there):
$$Bl = \mu_0(nl)I \quad\Rightarrow\quad \boxed{B = \mu_0 n I}$$
where $n$ = turns per unit length.

**Determining polarity from winding:** viewed end-on, current flowing **clockwise** at a face $\Rightarrow$ that face is a **south** pole (field lines converge/enter); **anticlockwise** $\Rightarrow$ **north** pole (field lines emerge) — consistent with field lines running south-to-north inside the solenoid.

### The toroid (application of Ampere's law, NCERT 4.6)

An **endless solenoid**: a solenoid bent into a closed ring. Current enters at one point on the cross-section and exits diametrically opposite, alternating dots/crosses around the ring; field lines inside the core form **concentric circles**.

**Three regions:**
1. **Empty space enclosed by the ring** (the "hole"): no current enclosed $\Rightarrow B=0$.
2. **Outside the toroid entirely:** $B=0$.
3. **Inside the toroid's wound core** — the only region with field:
$$B = \mu_0 n I, \qquad n = \frac{N}{2\pi R_\text{avg}}$$
(same form as a straight solenoid, using the average of the toroid's inner and outer radii for $R_\text{avg}$).

### Field inside/outside a long straight current-carrying conductor (Ampere's law application)

A cylindrical conductor of radius $a$ carries current $I$, uniformly distributed over its cross-section. Using a circular Amperian loop of radius $r$:

- **Outside** ($r>a$): full current $I$ enclosed: $B(2\pi r)=\mu_0 I \Rightarrow \boxed{B=\dfrac{\mu_0 I}{2\pi r}}$ — same as a thin wire, $\propto 1/r$.
- **Inside** ($r<a$): only the enclosed fraction of current counts (uniform current density): $I_\text{enc} = I\dfrac{r^2}{a^2}$, giving $B(2\pi r) = \mu_0 I\dfrac{r^2}{a^2} \Rightarrow \boxed{B = \dfrac{\mu_0 I r}{2\pi a^2}}$ — $\propto r$.
- **At the surface** ($r=a$): both expressions agree, $B=\dfrac{\mu_0 I}{2\pi a}$, the **maximum** value.

$B$-vs-$r$ graph: a straight line rising from the centre to the surface, then a $1/r$ curve falling off outside.


---

## Force on a Moving Charge in a Magnetic Field, the Lorentz Force, the Velocity Selector, and Helical Motion

**NCERT sections covered:** 4.2, 4.3

### Force on a moving charge in a magnetic field (NCERT 4.2)

$$\vec F = Q(\vec v\times\vec B)$$
- **Maximum** at $\theta=90°$ (angle between $v$ and $B$): $F_\max = BQv$.
- **Zero** at $\theta=0°$ or $180°$ (velocity parallel/antiparallel to $B$) — and also zero if $v=0$ (a stationary charge feels no magnetic force).
- **Direction:** perpendicular to the plane of $\vec v$ and $\vec B$, via the right-hand curl rule (curl fingers from $\vec v$ to $\vec B$, thumb gives $\vec F$).

#### The Lorentz force
When a charge moves through both an electric field $\vec E$ and a magnetic field $\vec B$ simultaneously, the electric force $Q\vec E$ and magnetic force $Q(\vec v\times\vec B)$ combine as a vector sum:
$$\boxed{\vec F = Q\vec E + Q(\vec v\times\vec B)}$$

#### Velocity selector (setup)
Uses **crossed** electric and magnetic fields ($\vec E\perp\vec B$). A charge $+q$ moving with velocity $v$ (say along the $x$-axis) experiences both an electric force and a magnetic force simultaneously, generally in different directions — the basis of a device that only lets through particles of one specific speed (where the two forces exactly balance).

### Helical motion (NCERT 4.3)

For velocity $\vec v$ at angle $\theta$ to $\vec B$, decompose it:
- $v\cos\theta$, **parallel** to $\vec B$ — unaffected by the magnetic force, giving uniform straight-line motion along $\vec B$.
- $v\sin\theta$, **perpendicular** to $\vec B$ — causes circular motion (same $\vec v\times\vec B$ analysis as for purely perpendicular velocity).

The combination of straight-line motion along $\vec B$ and circular motion around it traces a **helix**. The distance moved along $\vec B$ in one full rotation is the **pitch**:
$$p = v_\parallel T = v\cos\theta\cdot\frac{2\pi m}{Bq}$$
The radius of the helix equals the radius of its circular component of motion.


### Verify these spans
- [26:40–30:06] The transcript's real narration continues describing the velocity-selector's cross-product setup (unit vectors i, j, k) right up to its last segment at t=1827s (just past the true 1806.9s duration), never once using the word 'helix' or describing helical motion -- despite it being the second topic explicitly named in this lecture's own filename ('force on charge, helix'). Board frames tell a different story: floor_000081.jpg (t=1600s) already shows the helix topic's introduction (decomposing v into components parallel and perpendicular to B), and floor_000090.jpg (t=1780s, essentially at the true end) shows the complete derivation through to the pitch formula and the radius-of-helix statement, plus a one-line preview of 'cyclotron' (the next lecture's topic in this same chapter). The helical-motion claim above is grounded entirely from these two frames; the velocity selector's final balancing condition (which would follow directly as qE=qvB, i.e. v=E/B, from the setup that IS confirmed in the transcript) is not separately asserted here since neither the transcript nor a frame explicitly states that concluding line.

---

## The Cyclotron

**NCERT sections covered:** 4.3

### The cyclotron (NCERT 4.3)

A device (developed by Lawrence) that accelerates **positively charged particles** (proton, deuteron, alpha particle) to high energies using repeated passes through a comparatively small oscillating electric field, combined with a strong magnetic field.

#### Construction
Two hollow, evacuated D-shaped metal chambers ("Dees", $D_1,D_2$) separated by a small gap, connected to a high-frequency oscillator (providing the oscillating field across the gap), placed in a strong magnetic field perpendicular to the Dees' plane.

#### Working
A positive charge injected near the centre accelerates across the gap into one Dee, traces a **semicircular path** inside it (magnetic force only — no field inside a hollow conducting Dee), returns to the gap just as the oscillator's polarity reverses, gets accelerated again, and traces a **larger** semicircle in the next Dee (higher speed now). This repeats — spiralling outward — until the particle exits through a window with high velocity and strikes a target.

#### Mathematics
Inside a Dee, the magnetic force supplies centripetal force:
$$Bqv = \frac{mv^2}{r} \;\Rightarrow\; r = \frac{mv}{Bq}$$
Using $v=r\omega$:
$$\boxed{\omega = \frac{Bq}{m}}, \qquad T = \frac{2\pi m}{Bq}$$
$\omega$ (and $T$) are **independent of radius** $r$ — as the radius grows with each pass, speed grows proportionally, keeping each semicircle's transit time constant. This is exactly why the oscillator, tuned to this fixed period, stays synchronized with the particle across every pass.

#### Why not electrons?
An electron's tiny rest mass means it reaches relativistic speeds almost immediately, so its **relativistic mass** $m=m_0/\sqrt{1-v^2/c^2}$ grows with speed rather than staying constant. Since $T=2\pi m/(Bq)$ depends on mass, a growing mass breaks the match with the fixed-frequency oscillator — the electron drifts **out of phase** and stops being properly accelerated. Heavier particles (protons, deuterons, alpha particles) are far less affected by this at cyclotron energies, so cyclotrons work well for them but not for electrons.


---

## Numerical: Identifying Proton, Alpha Particle, and Electron by Radius in a Magnetic Field

**NCERT sections covered:** 4.3

### Worked numerical: identifying particles by radius in a magnetic field

Three particles -- a **proton**, an **alpha particle**, and an **electron** -- all moving with the same velocity $v$, enter a uniform magnetic field $B$ and trace three visibly different curved paths. Identify which is which.

**Step 1 -- sign of charge:** proton and alpha particle are both positive; the electron is negative, so it curves the *opposite* way from the other two. This immediately identifies the electron.

**Step 2 -- radius comparison for the two positive particles:**
$$r = \frac{mv}{Bq} = \frac{v}{B(q/m)} \quad\Rightarrow\quad r \propto \frac{1}{q/m}$$
- **Proton** ($^1_1\text{H}$): charge $+e$, mass $m$ $\Rightarrow q/m = e/m$
- **Alpha particle** ($^4_2\text{He}$, a helium nucleus): charge $+2e$, mass $4m$ $\Rightarrow q/m = 2e/4m = e/2m$

Since $e/m > e/2m$, the proton has the larger charge-to-mass ratio, hence the **smaller** radius: $r_\text{proton} < r_\text{alpha particle}$. The particle tracing the smaller-radius curve is the proton; the larger-radius one is the alpha particle.

#### Reading charge and mass from isotope notation
For $^A_Z X$: the subscript $Z$ (atomic number) gives charge $+Ze$; the superscript $A$ (mass number) gives mass $\approx Am$ (one nucleon mass each). Example: deuteron ($^2_1\text{H}$) and tritium ($^3_1\text{H}$) share the same charge $+e$ (both hydrogen, $Z=1$) but different masses ($2m$ and $3m$, from their different mass numbers).

---
*Note: this recording continues past this numerical into the start of the next topic (force on a current-carrying conductor in an external magnetic field) — that derivation is covered fully in the following lecture's own note, not duplicated here.*


---

## Force on a Current-Carrying Conductor, Fleming's Left-Hand Rule, Force Between Parallel Wires, and the Ampere

**NCERT sections covered:** 4.2, 4.8

### Force on a current-carrying conductor (NCERT 4.2)

Each conduction electron (drift velocity $v_d$) feels $\vec f = (-e)(\vec v_d\times\vec B)$. With electron density $n$, a conductor of length $L$, area $A$ has $nAL$ electrons, total charge $-enAL$:
$$\vec F = (-enAL)(\vec v_d\times\vec B)$$
Using $I=neAv_d$ (and that $\vec v_d$ points opposite to conventional current), the signs resolve to:
$$\boxed{\vec F = I(\vec L\times\vec B)}$$
where $\vec L$ points along the current, magnitude = conductor length.

#### Fleming's left-hand rule
Hold thumb, first (index), and centre (middle) fingers of the **left** hand mutually perpendicular: centre finger = current direction, first finger = field direction, **thumb = force direction**. (Equivalently, evaluate $I\vec L\times\vec B$ directly with unit vectors.)

### Force between two parallel current-carrying wires (NCERT 4.8)

Two infinitely long, straight, parallel wires, currents $I_1,I_2$, separated by $r$. Field due to wire 1 at wire 2's location: $B_1 = \dfrac{\mu_0 I_1}{2\pi r}$. Force on wire 2 (length $L$) in this field: $F_2 = I_2LB_1$ (angle $90°$), giving **force per unit length**:
$$\boxed{\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi r}}$$
(By symmetry, the same expression gives the force per unit length on wire 1 due to wire 2.)

**Direction:** currents in the **same** direction $\Rightarrow$ wires **attract**; currents in **opposite** directions $\Rightarrow$ wires **repel**.

#### Definition of the ampere
Setting $I_1=I_2=1$ A and $r=1$ m in the force-per-unit-length formula, with $\mu_0=4\pi\times10^{-7}$ T·m/A:
$$\frac{F}{L} = \frac{\mu_0}{2\pi}(1)(1) = 2\times10^{-7}~\text{N/m}$$
**One ampere** is the constant current which, if maintained in each of two infinitely long, straight, parallel conductors of negligible cross-section placed 1 metre apart in vacuum, would produce a force of exactly $2\times10^{-7}$ newton per metre of length between them.


### Verify these spans
- [26:20–26:39] The transcript's real narration ends mid-sentence right after stating the force-per-unit-length formula and beginning to plug in numbers ('this value will be 2x10^-7 ne[wton]...'), cutting off just short of formally stating the definition of 1 ampere -- the lecture's own second named topic. No board frame is available past t=1300s to confirm the exact wording used for this definition. Since the numerical ingredients (mu0/(2 pi) = 2x10^-7 N/A^2, from mu0=4*pi*10^-7) are already given directly in the transcript's own final segments, the definition of 1 ampere is stated in this note as the direct, unavoidable algebraic completion of what the transcript itself already establishes -- setting I1=I2=1 A and r=1 m in the just-derived formula -- rather than as independently confirmed content.

---

## Torque on a Current-Carrying Loop in a Uniform Magnetic Field

**NCERT sections covered:** 4.9

### Torque on a current-carrying loop (NCERT 4.9)

#### Special case: B in the plane of the loop (normal $\perp B$)
Rectangular loop (sides $PQ=RS=l$, $QR=SP=b$, current $I$), $\vec B$ lying in the loop's plane. Forces on the two sides parallel to $B$ (SR, QP) are zero ($I\vec L\times\vec B=0$ there). Forces on the two sides perpendicular to $B$ (PS, RQ) are each $ILB$, equal and opposite but acting along **different** lines — a couple.

$$\tau = (\text{force})\times(\text{perpendicular distance between lines of action}) = (ILB)(b) = I(lb)B = \boxed{IAB}$$
where $A=lb$ is the loop's area. Direction: perpendicular to the plane of $\vec A$ and $\vec B$ (right-hand cross-product rule).

*Mnemonic used in the lecture:* force $=I\vec L\times\vec B$ ("I love Bhopal"), torque $=I\vec A\times\vec B$ ("I admire Bhopal").

#### General case: normal at angle $\theta$ to $B$
Now the loop's normal makes angle $\theta$ (not $90°$) with $\vec B$. Forces on the sides perpendicular to the *original* orientation (QR, SP) turn out equal, opposite, and **collinear** — their resultant is zero. Forces on the other pair (PQ, RS) are equal, opposite, but **not collinear** — these constitute the torque:
$$\tau = (ILB\sin\theta)\times b = IAB\sin\theta$$
$$\boxed{\vec\tau = I(\vec A\times\vec B)}, \qquad |\tau| = IAB\sin\theta$$
The special case above ($\theta=90°$, $\sin\theta=1$, $\tau=IAB$) is the **maximum-torque** special case of this general result.


### Verify these spans
- [25:26–25:29] The transcript's last segment ends right as the general-case torque setup is completed ('force on PQ and RS... will constitute torque') but before the final formula is spoken. A board frame just past this point (floor_000072.jpg, t=1420s) shows the completed derivation and the boxed general result torque=I*A*B*sin(theta) (vector form tau=I(A x B)), so the final general-torque claim above is grounded from that frame rather than the transcript's own words, though it is the direct, expected algebraic completion of what the transcript does establish.
