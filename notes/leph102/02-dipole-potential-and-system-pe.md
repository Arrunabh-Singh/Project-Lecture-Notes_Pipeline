# Potential Due to an Electric Dipole, and Potential Energy of a System of Charges

**NCERT sections covered:** 2.4

## Potential due to an electric dipole (NCERT 2.4)

Unlike the earlier electric-field-intensity treatment (which used axial and equatorial special points), here a **general point** $P$ at polar coordinates $(r,\theta)$ from the dipole's center is considered directly.

By superposition (potential is a scalar, so this is simple addition, not vector addition like $\vec E$):
$$V = V_{+q} + V_{-q} = \frac{1}{4\pi\varepsilon_0}\frac{q}{R_1} - \frac{1}{4\pi\varepsilon_0}\frac{q}{R_2}$$

Using the standard far-field approximation (dropping perpendiculars from each charge to the line $OP$, giving $PN \approx AP$ and $ON = L\cos\theta$):

$$V = \frac{P\cos\theta}{4\pi\varepsilon_0\left(r^2 - l^2\cos^2\theta\right)}$$

For $r \gg l$ (the point far from the dipole compared to its size), this simplifies to:
$$\boxed{V = \frac{P\cos\theta}{4\pi\varepsilon_0 r^2}}$$

Two things worth noting against the point-charge result $V \propto 1/r$: dipole potential falls off **faster** ($1/r^2$), and it's **direction-dependent** through $\cos\theta$ — a point charge's potential has no such angular dependence.

### Special cases
- **Axial** ($\theta = 0$): $V = \dfrac{P}{4\pi\varepsilon_0 r^2}$ (maximum)
- **Equatorial / "broadside"** ($\theta = 90°$): $V = 0$ exactly, since $\cos 90° = 0$ — consistent with the direct superposition argument from the previous lecture (equidistant $+q$ and $-q$ cancel).

### Worked example
$q = 100\times10^{-9}$ C, separation $2L = 2\times10^{-3}$ m (so $P = 2QL = 2\times10^{-10}$ C·m), evaluated at $r=0.5$ m:
- Axial position: $V = 7.2$ V
- Broadside (equatorial) position: $V = 0$

## Potential energy of a system of point charges

Defined as the total work needed to assemble the charge configuration by bringing each charge in from infinity, one at a time, against the field of the charges already in place.

**Two charges:** bringing $q_1$ in first costs nothing (no field exists yet); bringing $q_2$ to a distance $r$ from $q_1$ costs work equal to (potential due to $q_1$) $\times\, q_2$:
$$U = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r}$$

**Three charges:** sum over every pair, in the order each charge is brought in:
$$U = \frac{1}{4\pi\varepsilon_0}\left[\frac{q_1q_2}{r_{12}} + \frac{q_1q_3}{r_{13}} + \frac{q_2q_3}{r_{23}}\right]$$

**General result, $n$ charges:** every pair contributes exactly once:
$$U = \frac{1}{2}\cdot\frac{1}{4\pi\varepsilon_0}\sum_{i=1}^n\sum_{\substack{j=1\\j\ne i}}^n \frac{q_iq_j}{r_{ij}} \;=\; \frac{1}{4\pi\varepsilon_0}\sum_{i<j} \frac{q_iq_j}{r_{ij}}$$
(the two forms are equivalent -- the first double-counts every pair once from each side and divides by 2; the second restricts to $j>i$ so each pair is counted exactly once directly.)

### Worked example
Equilateral triangle of side $a = 0.1$ m, with $q_1=q$, $q_2=2q$, $q_3=-2q$ and $q=10^{-6}$ C:
$$U = \frac{1}{4\pi\varepsilon_0}\frac{q^2}{a}\Big[(1)(2) + (1)(-2) + (2)(-2)\Big]$$
evaluated by the lecture to a negative total (a bound, energy-releasing configuration) — worth re-deriving by hand to check the arithmetic rather than trusting the board's final numeric answer verbatim.
