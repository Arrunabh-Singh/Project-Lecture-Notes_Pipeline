# Electric Charges and Fields

*Class XII CBSE Physics · Chapter 1 · 9 lectures, in order.*

*NCERT sections covered: 1.2, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 1.10, 1.11, 1.12, 1.13, 1.14.*

*Transcribed from the teacher's recorded lectures and checked against the
board frames and the NCERT text. Equations are board-grounded; any span the
transcript could not resolve confidently is flagged in place.*

---

## Introduction to Electrostatics: Frictional Electricity, the Gold Leaf Electroscope, and Basic Properties of Charge

**NCERT sections covered:** 1.2, 1.4

### Introduction (NCERT 1.1)
Electrostatics = "electro" (charge) + "static" (at rest): the study of charges at rest. This chapter builds up in stages: frictional electricity $\to$ electric field $\to$ electric potential $\to$ applications (capacitors) -- each stage depends on the one before it (e.g. capacitors can't be understood without electric field, which can't be understood without first understanding charge itself).

### Frictional electricity (NCERT 1.2)
Rubbing two different materials against each other transfers charge between them (the everyday "shock" felt in winter, or hair sticking to a comb, are both this phenomenon). Which material ends up positively vs. negatively charged is decided by how tightly each material's valence electrons are bound: the material whose electrons are *easier to pull away* loses electrons (becomes positive); the other gains those electrons (becomes negative).

- **Silk cloth + glass rod:** glass becomes positive, silk becomes negative.
- **Silk cloth + ebonite rod:** silk becomes positive, ebonite becomes negative.

(Silk isn't intrinsically "always negative" -- its sign depends on what it's rubbed against.)

**Naming:** Benjamin Franklin named the two kinds of charge *positive* and *negative*. An atom as a whole is electrically **neutral**: equal numbers of positive and negative charges. SI unit of charge: the **coulomb (C)**.

#### Detecting charge: the Gold Leaf Electroscope
An insulated metal knob (insulation prevents leakage and shields against stray air currents affecting the reading) connects via a wire to two thin gold leaves sealed inside a container. Touching a charged rod to the knob distributes charge onto both leaves; since like charges repel, the leaves diverge from each other. The degree of divergence indicates the strength of the charge present.

### Basic properties of electric charge (NCERT 1.4)

#### 1. Conservation of charge (1.4.2)
Charge can neither be created nor destroyed, only **transferred** from one body to another. Total charge before and after any process (rubbing, a nuclear reaction, etc.) is unchanged.

**Example:** alpha decay $\,^{238}_{92}\text{U} \to \,^{234}_{90}\text{Th} + \,^{4}_{2}\text{He}$ conserves both mass number ($238=234+4$) and atomic/charge number ($92=90+2$).

#### 2. Additivity of charges (1.4.1)
Charges combine like ordinary signed algebraic quantities. Example: $-e,-2e,+3e,+4e$ together give a total charge
$$q = -e-2e+3e+4e = +4e$$

#### 3. Quantisation of charge (1.4.3)
The charge on any body is always an **integral multiple** of the elementary charge $e$ (the electron's charge):
$$q = \pm ne$$
Never a fraction like $e/3$ or $-2e/3$. **Quarks** are the well-known exception, carrying fractional charges ($+e/3$, $-e/3$, $\pm2e/3$) -- but they only ever exist in bound combinations whose *total* charge is again an integral multiple of $e$, so quantisation still holds for every observable free particle.


---

## Electrostatic Induction, Charge Unit Conversions, and Coulomb's Law

**NCERT sections covered:** 1.4, 1.5

### Electrostatic induction

Charging a conducting body **without physical contact**, by bringing a charged rod nearby:

1. Bring a negatively-charged rod near a grounded conducting sphere (mounted on an insulating stand). By induction, positive charge accumulates on the near side (attracted toward the rod) and negative charge on the far side (repelled free electrons).
2. Ground the sphere: the repelled negative charges flow away into the ground (an effectively infinite charge reservoir), while the positive charges stay put, held by attraction to the rod.
3. Remove the ground connection first, *then* remove the rod.
4. The remaining positive charge redistributes itself uniformly over the sphere (charges settle into the configuration of minimum potential energy) — the sphere is now charged **positively**, without ever touching a charged body to it.

(The gold leaf electroscope shows the same effect: bringing a charged rod near *without touching* still induces a charge separation that causes the leaves to diverge.)

### Worked numerical: charge content of water
How many positive and negative (elementary) charges are in $250$ mL of water? Using $1$ mL $=1$ g, water's molar mass $18$ g/mol ($2\times1+16$), Avogadro's number $6.023\times10^{23}$ molecules/mol, and $10$ protons + $10$ electrons per H$_2$O molecule (O contributes 8, each H contributes 1):
$$\text{molecules in } 250\text{ g} = 6.023\times10^{23}\times\frac{250}{18}$$
Total positive charge count = total negative charge count = $10\times$ that number of molecules.

### Coulomb's law (NCERT 1.5)

**Recap — Newton's law of gravitation:** $F = \dfrac{Gm_1m_2}{r^2}$ — always attractive, independent of the medium between the masses (a universal law).

**Coulomb's law:** for two **point charges** $Q_1,Q_2$ (valid only when their separation is much larger than their own physical size — the electrostatic analogue of a "point object") separated by $r$:
$$F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r^2} = k\frac{Q_1Q_2}{r^2},\qquad k=\frac{1}{4\pi\varepsilon_0}=9\times10^9~\text{N m}^2\text{C}^{-2}$$

**Compared with gravity:** both are central forces (act along the line joining the two objects) and both obey Newton's third law ($\vec F_{12}=-\vec F_{21}$) — but Coulomb's force can be attractive *or* repulsive (gravity is always attractive), and it *depends on the medium* between the charges (gravity doesn't).

#### Definition of 1 coulomb
Setting $Q_1=Q_2=1$ C, $r=1$ m: $F = 9\times10^9$ N. So **1 coulomb** is the charge that, placed 1 m from an identical charge in vacuum, repels it with a force of $9\times10^9$ N — evidently an enormous unit for practical electrostatics.

#### A note on mass and charging
Charging a body very slightly changes its mass: charging it **negatively** (adding electrons) **increases** mass; charging it **positively** (removing electrons) **decreases** mass.

#### Why the coulomb is "too big" a unit, and sub-units (NCERT 1.4)
Practical electrostatics uses smaller sub-units: $1~\text{mC}=10^{-3}$ C, $1~\mu\text{C}=10^{-6}$ C, $1~\text{nC}=10^{-9}$ C. Since charge is quantised ($Q=ne$), 1 coulomb corresponds to
$$n = \frac{1}{1.6\times10^{-19}} = \frac{10^{19}}{1.6} \approx 6.25\times10^{18}$$
elementary charges — consistent with NCERT's own statement that there are about $6\times10^{18}$ electrons in a charge of $-1$ C.

---
*Note on this lecture's transcript:* the unit-conversion / electron-count material just above is grounded entirely from a board frame near the true end of the lecture -- the transcript itself loops back and repeats the water-numerical and gravitation recap instead of transcribing it. See the flagged span below.


### Verify these spans
- [30:29–36:24] The raw ASR transcript loops back after finishing the Coulomb's-law derivation (ending around t=1829s with F=9e9 N for the 1-coulomb definition) and re-transcribes the earlier 'how many charges in 250mL of water' numerical and Newton's-gravitation recap almost verbatim from t=1854s to the transcript's last segment at t=2182s -- a delayed-repetition artifact matching the pattern found repeatedly in this chapter's sibling chapter (Ch2). Board frames tell a different story: floor_000109.jpg (t=2160s, the last captured frame, well within this window) shows a page titled with a '5C, 1C -> very very large value' remark, unit conversions (1mC/microC/nC), and a worked calculation of how many electrons make up 1 coulomb (n=10^19/1.6) -- standard NCERT Section 1.4 content on why the coulomb is an impractically large unit -- none of which appears anywhere in the transcript. The unit-conversion and electron-count claim above is grounded entirely from that board frame.

---

## Dielectric Constant, Coulomb's Law in Vector Form, and the Superposition Principle

**NCERT sections covered:** 1.5, 1.6

### Dielectric constant

#### Force in a medium other than vacuum
$$F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r^2}\quad\text{(vacuum)} \qquad F = \frac{1}{4\pi\varepsilon}\frac{Q_1Q_2}{r^2}\quad\text{(medium, absolute permittivity }\varepsilon\text{)}$$

**Relative permittivity** $\varepsilon_r = \varepsilon/\varepsilon_0$ is preferred to quoting $\varepsilon$ directly, for the same reason density is usually quoted relative to water (density of water $=1$ g/cm$^3$, mercury $=13.6$, kerosene $=0.8$): a dimensionless ratio against a fixed, universal reference is more useful than an absolute value with units.

**Dielectric constant** $K$ is just another name for relative permittivity — there is no physical difference between the two terms:
$$\boxed{F = \frac{1}{4\pi\varepsilon_0 K}\frac{Q_1Q_2}{r^2}}, \qquad K=\varepsilon_r=\varepsilon/\varepsilon_0$$

*(Aside: in the CGS system, the Coulomb's-law constant is taken as exactly $1$, and charge is measured in electrostatic units/statcoulombs, with $1$ C $=3\times10^9$ esu. Mentioned for context; SI is used throughout this course.)*

#### Partly-dielectric, partly-vacuum gap
For two charges separated by distance $r$, with a dielectric slab of thickness $t$ (constant $K$) occupying part of the gap and the rest ($r-t$) vacuum: replace the dielectric segment with an **equivalent vacuum distance** $r_0=\sqrt{K}\,t$ (found by equating the force through the real dielectric thickness to the force through an unknown vacuum thickness), then treat the whole path as vacuum with total effective separation $(r-t)+\sqrt{K}t$:
$$F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{\left[(r-t)+\sqrt{K}\,t\right]^2}$$

### Coulomb's law in vector form (NCERT 1.5)

For charges $Q_1$ at $\vec r_1$ and $Q_2$ at $\vec r_2$, the force on $Q_2$ due to $Q_1$:
$$\vec F_{21} = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2(\vec r_2-\vec r_1)}{|\vec r_2-\vec r_1|^3} = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r_{12}^2}\hat r_{12}$$
By Newton's third law, $\vec F_{12}=-\vec F_{21}$.

### Principle of superposition (NCERT 1.6)

The net force on any one charge due to several others is the **vector sum** of the individual pairwise Coulomb forces, each computed independently as though only that one pair of charges existed, then combined via the triangle/parallelogram law of vector addition. For charges $Q_1,\dots,Q_5$, the force on $Q_4$:
$$\vec F_4 = \vec F_{41}+\vec F_{42}+\vec F_{43}+\vec F_{45}$$


---

## Continuous Charge Distribution (Linear, Surface, Volume), and Numericals on Placing a Third Charge

**NCERT sections covered:** 1.12

### Continuous charge distribution (NCERT 1.12)

For a continuous (non-point) charge distribution: break it into small elements, find the charge $dq$ on each, compute the small force $d\vec F$ on a test charge $q_0$ due to that element via Coulomb's law, then **integrate** over the whole distribution. (Analogy used in the lecture: once you know the cost *per* mango, you can price any quantity without asking again and again — same idea as knowing charge *per unit* length/area/volume.)

#### Linear charge density (1-D)
For a wire, or a ring (whose charge lies along its circumference — a *length*, not an area):
$$\lambda = \frac{\text{total charge}}{\text{total length}} = \frac{dq}{dl} \quad\Rightarrow\quad dq = \lambda\,dl$$
Force on $q_0$ from an element $dl$ at distance $r$: $d\vec F = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{q_0\lambda\,dl}{r^2}\hat r$, and the total force is $\vec F = \int d\vec F$ over the whole length.

#### Surface charge density (2-D)
For a charged plane sheet, or the surface of a metal solid/hollow sphere:
$$\sigma = \frac{\text{charge}}{\text{area}} = \frac{dq}{ds} \quad\Rightarrow\quad dq = \sigma\,ds$$
**Key point:** any charge given to a metal (conducting) solid sphere migrates entirely to its outer surface (area $4\pi r^2$) — so even though the sphere is a 3-D object, its charge distribution is *surface* (2-D), exactly like a hollow metal sphere.

#### Volume charge density (3-D)
For a distribution that genuinely fills a volume:
$$\rho = \frac{\text{charge}}{\text{volume}} = \frac{dq}{dV} \quad\Rightarrow\quad dq = \rho\,dV,\qquad d\vec F = \frac{1}{4\pi\varepsilon_0 K}\frac{q_0\rho\,dV}{r^2}\hat r$$

### Numericals: placing a third charge for zero net force

#### Two same-sign charges
$Q_1$ and $Q_2$ (worked case: $Q_2=2Q_1$) separated by $r$ — find where $Q_0$, placed **between** them, feels zero net force. Setting the two force magnitudes equal (distance $x$ from $Q_1$):
$$\frac{Q_1}{x^2} = \frac{Q_2}{(r-x)^2} \;\Rightarrow\; (r-x)^2 = 2x^2 \;\Rightarrow\; r-x=\sqrt2\,x \;\Rightarrow\; \boxed{x = \frac{r}{1+\sqrt2}}$$

#### Two opposite-sign charges
$+2Q$ and $-Q$ separated by $r$. A charge $+Q_0$ placed **between** them feels both forces pushing it the *same* direction (repelled by $+2Q$, attracted toward $-Q$) — they can never cancel there. The zero-force point must lie **outside** the segment, beyond the smaller-magnitude charge ($-Q$). At distance $x$ beyond $-Q$:
$$\frac{1}{4\pi\varepsilon_0}\frac{2Q\,Q_0}{x^2} = \frac{1}{4\pi\varepsilon_0}\frac{Q\,Q_0}{(r+x)^2} \;\Rightarrow\; \boxed{x = \frac{r}{\sqrt2-1}}$$

**General technique for this type of problem:** first determine whether the null point can even exist *between* the charges (same sign → yes, between them; opposite sign → no, it's outside, on the far side of the weaker charge), *then* set up and solve the force-balance equation.

---
*Note on this lecture's transcript:* volume charge density and both worked numericals above are grounded entirely from board frames -- the transcript itself falls into a repeated loop of earlier material and never reaches any of this. See the flagged span below.


### Verify these spans
- [14:30–32:22] This lecture's transcript is unusually badly corrupted: after the surface-charge-density/metal-sphere material (ending around t=870s), the ASR falls into a repeating loop, re-transcribing the SAME linear/surface charge density content 3-4 times over with shifted timestamps (a delayed-repetition artifact matching the pattern found across this chapter's sibling chapters), all the way to the transcript's nominal end near t=1942s. As a result the transcript never once mentions volume charge density (rho) at all, and never mentions the lecture's own second named topic -- 'numerical on placing of third charge' -- anywhere. Board frames tell the real story: floor_000050.jpg (t=980s) shows all three charge-density types (linear, surface, volume) laid out together on one page, confirming volume charge density genuinely was covered (most likely in the real, un-transcribed audio around t=870-980s); frames from t=1120s through t=1900s (floor_000057, floor_000065-66, floor_000072-74, floor_000096) show at least two distinct fully-worked numericals on where to place a third charge for zero net force -- one for two same-sign charges (null point between them), one for two opposite-sign charges (null point outside the segment) -- spanning what is likely more than half of this lecture's real running time. The volume-charge-density claim and both numerical claims above are grounded entirely from board frames, not the transcript.

---

## Electric Field Intensity, Field Lines, and the Point-Charge Field Formula

**NCERT sections covered:** 1.7, 1.8

### Electric field (NCERT 1.7)

**Concept:** the region around a charge where its effect (a force on another charge) can be felt -- directly analogous to the magnetic field around a magnet (felt by a test magnet, stronger effect closer in, negligible far away).

**Electric field intensity** $\vec E$ is the measurable version of this idea: the force per unit charge experienced by a very small ("test") positive charge $q_0$ placed at a point, in the limit $q_0\to0$ (small enough that it doesn't itself disturb the field being measured):
$$\vec E = \lim_{q_0\to0}\frac{\vec F}{q_0}$$
$\vec E$ is a **vector**, in the same direction as the force on a positive test charge. SI unit: **N/C**. Dimensional formula (from $F=ma$ and $Q=It$): $[E] = M^1L^1T^{-3}A^{-1}$.

#### Electric field due to a point charge
Combining $\vec E=\vec F/q_0$ with Coulomb's law $F=\frac{1}{4\pi\varepsilon_0}\frac{Qq_0}{r^2}$:
$$\boxed{\vec E = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\hat r}$$
The $q_0$ cancels out — **$E$ is independent of the test charge used to probe it**, a property of the source charge and the field point alone.

**Graphing $E$ vs $r$:** an inverse-square curve (a "rectangular hyperbola" shape, same family as $PV=\text{const}$ or $xy=\text{const}$). To turn it into a straight line (standard technique, same idea as plotting $V$ vs $I$ for Ohm's law to read off $R$ as the slope): plot $E$ against $1/r^2$ — since $Er^2 = Q/4\pi\varepsilon_0 = \text{const}$, this gives a straight line through the origin.

**Worked numerical:** a charge of $2$ mC at point $O$ — find $E$ at $40$ cm from it:
$$E = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2} = \frac{9\times10^9\times2\times10^{-3}}{(40\times10^{-2})^2}~\text{N/C}$$

### Electric field lines (NCERT 1.8)

Imaginary curves such that the tangent at any point gives the direction of $\vec E$ there, and along which an isolated free positive test charge would tend to move (directly analogous to magnetic field lines, e.g. traced out by iron filings around a magnet). **Crowding** of field lines indicates a **stronger** field.

#### Characteristics
1. Field lines **start on positive charges and terminate on negative charges**.
2. Field lines **never form closed loops** — this is the key difference from magnetic field lines, which *always* form closed loops (outside a magnet N$\to$S, inside S$\to$N). A field line running from one charge to a different charge (not back to itself) is not a closed loop, even if it looks curved.

#### Patterns for common configurations
- **Isolated point charge:** lines radiate straight outward (for $+q$, terminating charge assumed at infinity) or straight inward (for $-q$, source charge assumed at infinity). A common mistake is drawing lines that curve/converge near the charge — for a true point charge they must be radially straight, never touching or crossing right at the charge.
- **Two like charges** (e.g. $+Q,+Q$ or $+2Q,+Q$): lines repel each other and bend away, never intersecting. A **null point** ($E=0$) exists between them, located **closer to the smaller-magnitude charge** — exactly at the midpoint if the charges are equal.
- **Two unlike charges** (e.g. $+Q,-Q$ or $+2Q,-Q$): lines run from positive to negative, curving toward each other — this is *not* a closed loop (each line terminates once, going from one distinct charge to the other, rather than returning to its own start). Asymmetric magnitudes get proportionally more lines drawn from the larger charge.

---
*Note on this lecture's transcript:* the quantitative point-charge field formula, the E-vs-r graph discussion, the worked numerical, and the independence-from-test-charge point are all grounded from board frames near the true end of the lecture -- the transcript loops back to earlier material there instead of covering them. See the flagged span below.


### Verify these spans
- [39:50–46:14] The transcript's real, non-repeated narration runs continuously and coherently from t=0 to about t=2390s, thoroughly covering the definition of E, field lines, and field-line patterns for point charges and charge pairs. From t=2390s to the transcript's nominal end (t=2771s) it then loops back and re-transcribes the earlier point-charge and like-charges field-line material nearly verbatim -- the same delayed-repetition ASR artifact found elsewhere in this chapter. Unlike some other cases, board frames here show this is NOT just wasted/lost time: floor_000131.jpg (t=2600s) and floor_000138.jpg (t=2740s, the last captured frame, well within the true 2774.87s duration) show substantial genuinely new material -- the quantitative point-charge field formula E=(1/4 pi eps0)(Q/r^2) boxed 'by definition', an E-vs-r graph-linearisation discussion, a worked numerical (2 mC charge, field at 40cm), and a conceptual aside confirming E is independent of the test charge -- none of which appears anywhere in the transcript. The four point-charge-formula/numerical claims above are grounded entirely from these two board frames.

---

## Null-Point Numerical, Electric Dipole, and E Due to a Dipole at Axial and Equatorial Positions

**NCERT sections covered:** 1.10

### Worked numerical: null point between two like charges

Charges $+Q$ and $+2Q$ separated by $r=2$ m — find the null point's position measured **from $+2Q$**. Setting the null point at distance $x$ from $+Q$ (so $2-x$ from $+2Q$) and equating magnitudes:
$$\frac{Q}{x^2} = \frac{2Q}{(2-x)^2} \;\Rightarrow\; (2-x)^2 = 2x^2 \;\xrightarrow{\sqrt{\ }}\; 2-x=\sqrt2\,x \;\Rightarrow\; x = \frac{2}{1+\sqrt2}$$
Since the question asks for the distance from $+2Q$, the answer is $2-x$, **not** $x$ — read the question carefully. As expected, the null point sits closer to the smaller-magnitude charge ($+Q$).

### Electric dipole (NCERT 1.10)

A pair of equal and opposite point charges $+Q,-Q$ separated by a small distance $2L$. **Net charge is always zero.** Strength is measured by the **dipole moment**:
$$p = Q\times 2L,\qquad \text{SI unit: coulomb-metre (C m)}$$
(Write "C m", not "m C" — the latter reads as millicoulomb.) An **ideal dipole** is the limit $Q\to\infty,\ 2L\to0$ such that $p=2QL$ stays finite and well-defined.

#### Axial (end-on) position
Point $P$ on the line through both charges, distance $r$ from the dipole's centre $O$. By superposition (valid for $\vec E$ just as for forces):
$$\vec E = \frac{2Pr}{4\pi\varepsilon_0(r^2-L^2)^2}\hat p$$
— pointing the **same** direction as $\vec p$. For $r\gg L$ ($L^2$ negligible):
$$\boxed{E_\text{axial} = \frac{2P}{4\pi\varepsilon_0 r^3}}$$
Falls off as $1/r^3$ — faster than a point charge's $1/r^2$ (visible on an $E$-vs-$r$ graph as a noticeably steeper drop).

#### Equatorial (broadside-on) position
Point $P$ on the perpendicular bisector of the dipole, distance $r$ from $O$. $E_{+Q}$ and $E_{-Q}$ have equal magnitude $\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2+L^2}$ but different directions; by symmetry their components perpendicular to the dipole axis cancel exactly, leaving only the components along the (negative) axis direction to add:
$$E_\text{eq} = 2E_{+Q}\cos\theta = \frac{2QL}{4\pi\varepsilon_0(r^2+L^2)^{3/2}},\qquad \cos\theta=\frac{L}{\sqrt{r^2+L^2}}$$
For $r\gg L$:
$$\boxed{E_\text{eq} = \frac{P}{4\pi\varepsilon_0 r^3}}$$
— exactly **half** the axial-point value at the same $r$, and pointing **antiparallel** to $\vec p$ (opposite direction from the axial-point field).


---

## Torque and Potential Energy of a Dipole in a Uniform Electric Field

**NCERT sections covered:** 1.11

### Recap: torque
$$\vec\tau = \vec R\times\vec F,\qquad |\vec\tau| = RF\sin\theta$$
Direction perpendicular to the plane of $\vec R,\vec F$, via the right-hand curl rule. Equivalently, for a **couple** (two equal and opposite forces): $\tau = F\times(\text{perpendicular distance between their lines of action})$.

### Torque on a dipole in a uniform field (NCERT 1.11)

Dipole (charges $+Q,-Q$, length $2L$, moment $p=2QL$) at angle $\theta$ to a uniform field $\vec E$. Each charge feels an equal-magnitude force $F=EQ$, but in different directions (since $\vec E$ points from $+$ to $-$) — a couple. The perpendicular distance between the two forces' lines of action is $2L\sin\theta$, so:
$$\tau = F\times 2L\sin\theta = EQ\times2L\sin\theta = PE\sin\theta$$
In vector form:
$$\boxed{\vec\tau = \vec p\times\vec E}$$
direction perpendicular to the plane of $\vec p,\vec E$ (right-hand curl rule, fingers curling from $\vec p$ to $\vec E$).

**Extremes:** torque is **maximum** ($=PE$) at $\theta=90°$ ($\vec p\perp\vec E$); torque is **zero** at $\theta=0°$ or $180°$ ($\vec p$ parallel or antiparallel to $\vec E$) — even though forces still act on each charge individually, there's no net turning effect once aligned.

### Potential energy of a dipole (NCERT 1.11)

Small work done rotating the dipole by $d\theta$: $dW = \tau\,d\theta = PE\sin\theta\,d\theta$ (rotational analogue of $dW=F\,dx$). Integrating from $\theta_1$ to $\theta_2$ (using $\int\sin\theta\,d\theta=-\cos\theta$):
$$W = PE\left[\cos\theta_1-\cos\theta_2\right]$$
This work is stored as potential energy. Taking $\theta_1=90°$ (where $\cos90°=0$) as the zero-PE reference:
$$\boxed{U = -PE\cos\theta = -\vec p\cdot\vec E}$$

#### Worked numerical
A dipole with charge $1~\mu\text{C}$, separated by $1$ cm, placed in $E=2\times10^6$ N/C:
- **(i)** Dipole moment: $p = Q\times2L = 10^{-6}\times10^{-2} = 10^{-8}$ C$\cdot$m
- **(ii)** Maximum torque: $\tau_\max = PE = 10^{-8}\times2\times10^6 = 2\times10^{-2}$ N$\cdot$m
- **(iii)** Work done rotating through $180°$ starting from $\theta=0$: $W = PE[\cos0°-\cos180°] = PE[1-(-1)] = 2PE$

---
*Note on this lecture's transcript:* the worked numerical above is grounded entirely from a board frame near the true end of the lecture -- the transcript repeats earlier material there and then stops well short of the lecture's actual end. See the flagged span below.


### Verify these spans
- [25:06–34:06] Two separate transcript problems compound here. First, from roughly t=1506s the transcript re-transcribes the potential-energy derivation (theta1-to-theta2 rotation, the sin/cos integration, U=-PE cos theta) almost verbatim a second time -- a delayed-repetition artifact, not real re-teaching -- before cutting off mid-sentence at t=1883.7s. Second, and more seriously, this transcript's own timestamped coverage stops there entirely: it has NO segments at all for the final ~163 seconds of the lecture's true 2046.5s duration (a genuine truncation, not just a hidden-by-repetition gap). Board frames fill in what was lost: the last captured frame (floor_000102.jpg, t=2020s, well inside the untranscribed window) shows a 'stable eqm' heading (visible only as a two-word label -- the supporting derivation, if any, is off the top of the captured frame and not recoverable from the sampled images) followed by a fully worked numerical (dipole moment, maximum torque, and work done rotating through 180 degrees from theta=0) plus a small formula-summary box. The worked-numerical claim above is grounded entirely from that frame; the stable-equilibrium point is mentioned only as a heading seen on the board, not as a verified claim, since its derivation isn't visible in any captured frame.

---

## Correction on Dipole PE, Total Force on a Dipole, Electric Flux, and Gauss's Law

**NCERT sections covered:** 1.9, 1.11, 1.13

### Corrections and follow-ups from the previous lecture

- In the dipole PE numerical, the reference angle $\theta_1$ (where PE is taken as zero) is **$90°$**, not $0°$ — use $\cos90°=0$.
- **Total (net) force on a dipole in a uniform field is zero**: the two equal-and-opposite forces on the charges cancel exactly, so the dipole only *rotates*, it doesn't translate. In a **non-uniform** field, net force is no longer zero, so the dipole undergoes both translational *and* rotational motion.

### Electric flux (NCERT 1.9)

**Area as a vector:** an area element $d\vec S$ has both magnitude and direction — direction given by the **outward-drawn normal** to the surface at that point (e.g. for a cube, the outward normal on each face points away from the enclosed volume).

**Electric flux** $\Phi$ is the number of field lines passing *normally* (perpendicularly) through a given area:
$$\Phi = EA\cos\theta = \vec E\cdot\vec A$$
($\theta$ = angle between $\vec E$ and the area's outward normal.) Maximum when $\vec E$ is parallel to the normal; zero when $\vec E$ lies in the plane of the surface (analogy used in the lecture: water flow through a rotating ring/bangle — maximum flow face-on, zero flow edge-on).

**General definition:** $d\Phi = \vec E\cdot d\vec S$ for a small element, $\Phi = \oint_S \vec E\cdot d\vec S$ over the whole surface. **SI unit:** N$\,$m$^2$C$^{-1}$. Flux is a **scalar** (it's a dot product).

### Gauss's law (NCERT 1.13)

**Statement:** the total electric flux through any closed surface $S$ in vacuum equals $1/\varepsilon_0$ times the total charge enclosed:
$$\boxed{\oint_S \vec E\cdot d\vec S = \frac{Q_\text{enclosed}}{\varepsilon_0}}$$

#### Derivation for a point charge (spherical Gaussian surface)
For a point charge $Q$ at the centre of a sphere of radius $r$: $\vec E$ is radial with constant magnitude $\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}$ everywhere on the sphere, and everywhere **parallel** to $d\vec S$ ($\theta=0,\ \cos\theta=1$). So:
$$\oint_S\vec E\cdot d\vec S = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\oint_S dS = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}(4\pi r^2) = \frac{Q}{\varepsilon_0}$$
The $r^2$ cancels — the result is **independent of the sphere's radius**. Though proved here only for a sphere, $\Phi=Q/\varepsilon_0$ holds for a closed surface of **any** shape enclosing the same charge $Q$.

#### Flux example: closed cylinder in a uniform field
For a uniform field passing straight through a closed cylinder aligned with the field (entering one flat end, exiting the other, none crossing the curved side): the **total** flux through the closed surface is **zero** — outward flux at the exit face exactly cancels inward flux at the entry face.

---
*Note on this lecture's transcript:* the Gauss's-law derivation and the cylinder example above are grounded entirely from board frames -- the transcript repeats earlier flux-definition material there instead. See the flagged span below.


### Verify these spans
- [30:04–32:02] The transcript re-transcribes the earlier flux-definition material (Phi=EA cos theta, roughly matching t=903-1030s) a second time from about t=1834s to its last segment at t=1918-1947s -- a delayed-repetition artifact, not new content. Board frames tell a different story for this same window: floor_000091.jpg and floor_000095.jpg (both around t=1800-1880s, within this window) show the actual mathematical PROOF of Gauss's law for a point charge using a spherical Gaussian surface (E radial and parallel to dS everywhere, integral reduces via the sphere's surface area 4 pi r^2 to Phi=Q/eps0), generalised to an arbitrary closed surface shape, plus a flux-through-a-closed-cylinder example (net flux zero). None of this derivation or example appears in the transcript, which only ever states Gauss's law verbally without deriving it. The two claims above (the spherical-surface derivation and the cylinder example) are grounded entirely from these board frames.

---

## Applications of Gauss's Law: Cube Flux Numericals, Infinite Wire, Infinite Sheet, Charged Spherical Shell

**NCERT sections covered:** 1.13, 1.14

### Gauss's law: flux numericals with a cube

**Charge near one face:** a point charge $10$ cm from the centre of one face of a cube — flux through the whole (closed) cube is $q/\varepsilon_0$; since a cube has 6 identical faces, flux through just that one face is $\dfrac{1}{6}\dfrac{q}{\varepsilon_0}$.

**Charge at special points of a cube:**
- **Body centre:** charge fully enclosed by one cube $\Rightarrow$ flux $=q/\varepsilon_0$.
- **Face centre:** charge sits on the boundary shared with one neighbouring cube $\Rightarrow$ effective enclosed charge $q/2$, flux $=\dfrac{q}{2\varepsilon_0}$.
- **Edge centre:** charge shared among the $8$ cubes meeting at that edge $\Rightarrow$ effective enclosed charge $q/8$, flux $=\dfrac{q}{8\varepsilon_0}$.

### Applications of Gauss's law (NCERT 1.14)

Gauss's law gives a shortcut to find $E$ for highly symmetric continuous charge distributions: choose a Gaussian surface matching the symmetry, so $E$ can be pulled outside the flux integral.

#### Field due to an infinitely long charged wire (1.14.1)
Linear charge density $\lambda$, field point at perpendicular distance $r$. Gaussian surface: a coaxial cylinder of radius $r$, length $L$. By symmetry $E$ is radial and constant on the curved surface (parallel to its area vector, $\theta=0$), and perpendicular to the two flat end-caps ($\theta=90°$, zero contribution):
$$E(2\pi rL) = \frac{\lambda L}{\varepsilon_0} \;\Rightarrow\; \boxed{E = \frac{\lambda}{2\pi\varepsilon_0 r}}$$
($L$ cancels.) Inversely proportional to $r$ — same rectangular-hyperbola-shaped $E$-vs-$r$ graph family as the point charge and the dipole.

#### Field due to an infinite plane sheet (1.14.2)
Surface charge density $\sigma$; field is perpendicular to the sheet, equal magnitude both sides. Gaussian surface: a thin "pillbox" cylinder straddling the sheet, flat circular end-caps of area $A$ parallel to the sheet. $E$ parallel to both end-caps ($\theta=0$, contributing $EA$ each) and perpendicular to the curved side (zero):
$$2EA = \frac{\sigma A}{\varepsilon_0} \;\Rightarrow\; \boxed{E = \frac{\sigma}{2\varepsilon_0}}$$
($A$ cancels.) **Independent of distance** from the sheet — a flat horizontal line on an $E$-vs-$r$ graph.

#### Field due to a uniformly charged thin spherical shell (1.14.3)
Total charge $q$, radius $R$.
- **Outside / on the surface** ($r\geq R$, Gaussian sphere concentric with the shell): the whole charge behaves as if concentrated at the centre, exactly like a point charge:
$$E = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\ (r>R), \qquad E = \frac{1}{4\pi\varepsilon_0}\frac{q}{R^2}\ (r=R)$$
- **Inside** ($r<R$): a Gaussian sphere strictly inside the shell encloses **zero** charge (all the shell's charge sits on its outer surface). Since the flux integral's surface-area factor $4\pi r^2$ is never zero for $r>0$, this forces:
$$\boxed{E = 0 \text{ everywhere strictly inside a uniformly charged shell}}$$

---
*Note on this lecture's transcript:* both the outside/surface and inside results for the charged spherical shell above are grounded entirely from board frames near the true end of this (very long, 48-minute) lecture -- the transcript itself stops right at the sentence introducing this final application, with no further segments. See the flagged span below.


### Verify these spans
- [46:20–47:38] This is a straightforward truncation rather than a repetition/substitution artifact: the transcript's own last segment is the single sentence 'So, what we do is we consider a thin spherical shell, let us suppose we consider this as a thin spherical shell,' right at the very start of the third application (field due to a charged spherical shell), and no further segments follow even though this was clearly meant to be a full derivation (matching this very long, 48-minute lecture's own title, 'application of gauss th'). Board frames fill the gap completely: floor_000134.jpg and floor_000138.jpg (both well within the true 2858s duration, after the transcript's own cutoff) show the full three-case derivation -- outside/on the surface (Gauss's law with a Gaussian sphere of radius r>=R, giving the point-charge-like result), and inside (Gaussian sphere r<R encloses zero charge, forcing E=0) -- reaching clean, boxed final results in each case. Both spherical-shell claims above are grounded entirely from these two board frames.
