# Null-Point Numerical, Electric Dipole, and E Due to a Dipole at Axial and Equatorial Positions

**NCERT sections covered:** 1.10

## Worked numerical: null point between two like charges

Charges $+Q$ and $+2Q$ separated by $r=2$ m — find the null point's position measured **from $+2Q$**. Setting the null point at distance $x$ from $+Q$ (so $2-x$ from $+2Q$) and equating magnitudes:
$$\frac{Q}{x^2} = \frac{2Q}{(2-x)^2} \;\Rightarrow\; (2-x)^2 = 2x^2 \;\xrightarrow{\sqrt{\ }}\; 2-x=\sqrt2\,x \;\Rightarrow\; x = \frac{2}{1+\sqrt2}$$
Since the question asks for the distance from $+2Q$, the answer is $2-x$, **not** $x$ — read the question carefully. As expected, the null point sits closer to the smaller-magnitude charge ($+Q$).

## Electric dipole (NCERT 1.10)

A pair of equal and opposite point charges $+Q,-Q$ separated by a small distance $2L$. **Net charge is always zero.** Strength is measured by the **dipole moment**:
$$p = Q\times 2L,\qquad \text{SI unit: coulomb-metre (C m)}$$
(Write "C m", not "m C" — the latter reads as millicoulomb.) An **ideal dipole** is the limit $Q\to\infty,\ 2L\to0$ such that $p=2QL$ stays finite and well-defined.

### Axial (end-on) position
Point $P$ on the line through both charges, distance $r$ from the dipole's centre $O$. By superposition (valid for $\vec E$ just as for forces):
$$\vec E = \frac{2Pr}{4\pi\varepsilon_0(r^2-L^2)^2}\hat p$$
— pointing the **same** direction as $\vec p$. For $r\gg L$ ($L^2$ negligible):
$$\boxed{E_\text{axial} = \frac{2P}{4\pi\varepsilon_0 r^3}}$$
Falls off as $1/r^3$ — faster than a point charge's $1/r^2$ (visible on an $E$-vs-$r$ graph as a noticeably steeper drop).

### Equatorial (broadside-on) position
Point $P$ on the perpendicular bisector of the dipole, distance $r$ from $O$. $E_{+Q}$ and $E_{-Q}$ have equal magnitude $\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2+L^2}$ but different directions; by symmetry their components perpendicular to the dipole axis cancel exactly, leaving only the components along the (negative) axis direction to add:
$$E_\text{eq} = 2E_{+Q}\cos\theta = \frac{2QL}{4\pi\varepsilon_0(r^2+L^2)^{3/2}},\qquad \cos\theta=\frac{L}{\sqrt{r^2+L^2}}$$
For $r\gg L$:
$$\boxed{E_\text{eq} = \frac{P}{4\pi\varepsilon_0 r^3}}$$
— exactly **half** the axial-point value at the same $r$, and pointing **antiparallel** to $\vec p$ (opposite direction from the axial-point field).
