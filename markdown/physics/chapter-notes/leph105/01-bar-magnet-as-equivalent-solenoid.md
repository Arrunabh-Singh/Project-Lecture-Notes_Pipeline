# Magnetism Intro: Gauss's Law, Electrostatic Analogy, and Bar Magnet as Equivalent Solenoid

**NCERT sections covered:** 5.1, 5.2.2, 5.2.3, 5.2.4, 5.3

## Introduction: monopoles and Gauss's law in magnetism (NCERT 5.1, 5.3)
Lodestone (natural magnetite) is introduced as a naturally occurring magnet, and the earth itself is described as behaving like a giant magnet (a freely suspended bar magnet always settles north-south). A key qualitative fact is developed by repeatedly breaking a bar magnet: **magnetic monopoles do not exist** -- however small a piece you cut, it still has both an N and an S pole.

This directly motivates **Gauss's law in magnetism**: since field lines leaving the N pole always curve around and re-enter at S (closed loops, unlike electric field lines which start/end on isolated charges), the net magnetic flux through *any* closed surface is zero:
$$\oint \vec B\cdot d\vec S = 0$$
This is explicitly contrasted with Gauss's law in electrostatics, $\oint \vec E\cdot d\vec S = q/\varepsilon_0$, which is nonzero in general because isolated electric charge does exist.

## Bar magnet vs. solenoid: similarities and differences
Before deriving the equivalence formally, the lecture recaps general field-line properties (closed loops, tangent gives direction, never intersect, density $\propto$ strength) and lists concrete differences/similarities between a bar magnet and a current-carrying solenoid:

- **Differences:** a bar magnet's field strength is fixed once magnetised and its poles cannot be swapped; a solenoid's field $B=\mu_0 nI$ can be tuned via turns-per-length $n$ or current $I$, and its poles reverse if the current direction reverses.
- **Similarities:** both align north-south when freely suspended, both attract small iron pieces, and both have field lines and two poles.

These similarities are the motivation for treating a bar magnet as an "equivalent solenoid" -- the main derivation of this lecture.

## The electrostatic analogy (NCERT 5.2.3, 5.2.4)
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

## Derivation: bar magnet as an equivalent solenoid (NCERT 5.2.2)
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
