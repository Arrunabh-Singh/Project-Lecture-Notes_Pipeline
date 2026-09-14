`Class XII CBSE · Physics · Chapters 1–9`

# Physics, Derived

*Every derivation the paper can ask for, written one algebraic move per line with the reason each move is allowed — and every one with a real drawn figure, because in physics the diagram is usually where the marks start and where a half-remembered derivation falls apart.*

- Derivations: 45

- Figures: 45

- Chapters: 9

- Longest: 5 marks

### How to use this

**Draw the figure first, from the setup paragraph, before you read a single step.** In every board exam the diagram carries marks of its own, and a derivation written without one rarely scores full even when the algebra is right.

The *italic reason* beside a step — *vertically opposite*, *small aperture, so N ≈ P*, *divide throughout by uvf* — is what makes it a proof rather than a list of equations. Those clauses are where examiners look.

Where two derivations share an opening, a dashed **shared setup** note says so. Those pairs are worth learning together: get one and the second costs almost nothing.

## `CH 1` Electric Charges and Fields — *6 derivations*

### `PD1` Electric field on the axis of a dipole — *3 marks*

> A dipole of charges $-q$ at A and $+q$ at B, separated by $2l$, with centre O. The point P lies on the axis, on the $+q$ side, at distance $r$ from O. So P is $(r-l)$ from $+q$ and $(r+l)$ from $-q$. Both fields point along the axis, so this is a scalar subtraction, not a vector sum.

**Figure.** A dipole on a horizontal axis: minus q on the left, plus q on the right, separated by 2l about the centre O. A point P lies further right on the same axis at distance r from O. The field from plus q points right and is larger; the field from minus q points left and is smaller.

*P is nearer the $+q$ charge, so $E_+$ is the larger of the two and the resultant points away from the dipole, parallel to $\vec p$.*

1. $E_{+} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{(r-l)^2}$, directed from B towards P  — *(field of a point charge, P is $(r-l)$ from $+q$)*
2. $E_{-} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{(r+l)^2}$, directed from P towards A  — *(P is $(r+l)$ from $-q$)*
3. Both lie along the same line in opposite senses, so $E = E_+ - E_-$  — *(no vector resolution needed on the axis)*
4. $E = \dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{1}{(r-l)^2} - \dfrac{1}{(r+l)^2}\right]$
5. $= \dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{(r+l)^2 - (r-l)^2}{(r^2-l^2)^2}\right]$  — *(common denominator, using $(r-l)(r+l) = r^2-l^2$)*
6. $(r+l)^2 - (r-l)^2 = 4rl$  — *(difference of two squares)*
7. $E = \dfrac{q}{4\pi\varepsilon_0}\dfrac{4rl}{(r^2-l^2)^2}$
8. $p = q \times 2l$, so $q \times 4rl = 2pr$  — *(introducing the dipole moment)*
9. $E_{\text{axial}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2pr}{(r^2-l^2)^2}$
10. For a **short** dipole, $r \gg l$, so $r^2 - l^2 \approx r^2$  — *(the standard approximation — say it explicitly)*
11. $E_{\text{axial}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2p}{r^3}$

**Result:** $E_{\text{axial}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2p}{r^{3}}$, directed **parallel** to $\vec p$

*$1/r^3$, not $1/r^2$: the two charges almost cancel, so a dipole's field dies faster than a single charge's.*

### `PD2` Electric field on the equatorial line of a dipole — *3 marks*

> The same dipole, but P now sits on the perpendicular bisector, at distance $r$ from the centre O. Both charges are the same distance $\sqrt{r^2+l^2}$ away, so the two fields have equal magnitude — but they point in different directions, so this one *does* need resolution into components.

> **Shared setup with PD1.** Same dipole, same symbols; only the position of P changes. Draw one figure and move P, and you have both derivations.

**Figure.** A dipole on a horizontal axis with point P on the perpendicular bisector above the centre. The field from plus q points away along BP and the field from minus q points towards A along PA; their vertical components cancel and their horizontal components add, giving a resultant antiparallel to the dipole moment.

*The two fields are equal in size. Their components perpendicular to the axis cancel; the components along the axis both point from $+q$ towards $-q$, so they add — and the resultant is **antiparallel** to $\vec p$.*

1. $AP = BP = \sqrt{r^2+l^2}$  — *(P is on the perpendicular bisector)*
2. $E_{+} = E_{-} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2+l^2}$  — *(equal distances, equal magnitudes)*
3. Resolve each into a component along the axis and one perpendicular to it
4. The perpendicular components are equal and opposite, so they cancel  — *(this is why the resultant is parallel to the axis)*
5. $E = E_+\cos\theta + E_-\cos\theta = 2E_+\cos\theta$  — *(the axial components add)*
6. $\cos\theta = \dfrac{l}{\sqrt{r^2+l^2}}$  — *(from the right triangle AOP)*
7. $E = 2\cdot\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2+l^2}\cdot\dfrac{l}{\sqrt{r^2+l^2}}$
8. $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2ql}{\left(r^2+l^2\right)^{3/2}}$
9. $p = q\times2l$, so $2ql = p$
10. $E_{\text{eq}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{p}{\left(r^2+l^2\right)^{3/2}}$
11. Short dipole, $r \gg l$: $\left(r^2+l^2\right)^{3/2} \approx r^3$
12. $E_{\text{eq}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{p}{r^3}$

**Result:** $E_{\text{eq}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{p}{r^{3}}$, directed **antiparallel** to $\vec p$ — exactly half the axial field

### `PD3` Torque on a dipole in a uniform electric field — *2–3 marks*

> A dipole of length $2l$ placed in a uniform field $\vec E$, with its axis at angle $\theta$ to the field. Each charge feels a force $qE$ — equal in size, opposite in direction. Since the field is uniform, these forces do not translate the dipole; they form a couple.

**Figure.** A dipole tilted at angle theta in a uniform horizontal field: force qE acts rightwards on the plus charge and leftwards on the minus charge, forming a couple whose arm is 2l sine theta, the perpendicular distance between the two lines of action.

*Two equal, opposite, non-collinear forces — a couple. Its moment is one force times the perpendicular distance between their lines of action, which the geometry gives as $2l\sin\theta$.*

1. Force on $+q$ is $qE$ along $\vec E$; force on $-q$ is $qE$ opposite to $\vec E$
2. Net force $= qE - qE = 0$  — *(the field is uniform, so the dipole does not translate)*
3. The two forces are equal, opposite and **not collinear**, so they form a couple
4. Torque of a couple $=$ (one force) $\times$ (perpendicular distance between the lines of action)
5. Perpendicular distance $= 2l\sin\theta$  — *(from the right triangle in the figure)*
6. $\tau = qE \times 2l\sin\theta$
7. $p = q\times 2l$
8. $\tau = pE\sin\theta$
9. In vector form, $\vec\tau = \vec p\times\vec E$  — *(the cross product carries both the $\sin\theta$ and the direction)*

**Result:** $\vec\tau = \vec p\times\vec E, \qquad \tau = pE\sin\theta$

*Maximum at $\theta = 90°$, zero at $\theta = 0$ and $180°$. Work done rotating from $\theta_1$ to $\theta_2$ is $W = pE(\cos\theta_1 - \cos\theta_2)$, giving $U = -\vec p\cdot\vec E$ with $U=0$ taken at $90°$.*

### `PD4` Field of an infinite straight charged wire, by Gauss's law — *3 marks*

> An infinitely long straight wire carrying uniform linear charge density $\lambda$. By symmetry the field must point radially outward and have the same magnitude everywhere at distance $r$. Choose a coaxial cylinder of radius $r$ and length $L$ as the Gaussian surface, with flat end caps.

> **Shared method with PD5 and PD6.** All three run the same four moves: pick a surface matching the symmetry, argue where the flux is zero, evaluate $\oint\vec E\cdot d\vec S$ as $E\times(\text{area})$, then set it equal to $q_{\text{enc}}/\varepsilon_0$. Only the surface changes.

**Figure.** An infinite charged wire running horizontally with a coaxial cylindrical Gaussian surface of radius r and length L around it. Field arrows point radially outward through the curved surface, and no flux passes through the two flat end caps because the field there is parallel to the surface.

*The field is everywhere perpendicular to the curved surface and everywhere parallel to the end caps — which is exactly what makes the integral collapse to a multiplication.*

1. By symmetry $\vec E$ is radial and its magnitude depends only on $r$
2. Total flux $= \Phi_{\text{curved}} + \Phi_{\text{cap 1}} + \Phi_{\text{cap 2}}$
3. On the end caps $\vec E \perp d\vec S$, so $\vec E\cdot d\vec S = 0$  — *(field is parallel to the cap, so it contributes no flux)*
4. On the curved surface $\vec E \parallel d\vec S$ and $E$ is constant
5. $\Phi = E \times (\text{curved area}) = E\left(2\pi r L\right)$
6. Charge enclosed $q_{\text{enc}} = \lambda L$  — *(only the length $L$ inside the cylinder counts)*
7. Gauss's law: $\oint\vec E\cdot d\vec S = \dfrac{q_{\text{enc}}}{\varepsilon_0}$
8. $E\left(2\pi r L\right) = \dfrac{\lambda L}{\varepsilon_0}$
9. $L$ cancels from both sides  — *(as it must — the answer cannot depend on how much wire we chose to enclose)*
10. $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$

**Result:** $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$, directed radially — outward for $\lambda \gt 0$

*$E \propto 1/r$, not $1/r^2$. Step 9 is a genuine check on your work: if $L$ survives, something is wrong.*

### `PD5` Field of an infinite charged plane sheet, by Gauss's law — *3 marks*

> An infinite plane sheet with uniform surface charge density $\sigma$. By symmetry the field must be perpendicular to the sheet and the same on both sides. Take a cylindrical pillbox of cross-sectional area $A$ pushed through the sheet, so one flat face sits on each side.

**Figure.** An infinite charged sheet drawn vertically with a cylindrical pillbox pushed through it, one flat face of area A on each side. Field arrows point outward through both flat faces and no flux passes through the curved side, which is parallel to the field.

*Two flat faces, each of area $A$, each contributing $EA$ — which is where the factor of 2 in the flux comes from, and hence the 2 in the denominator of the answer.*

1. By symmetry $\vec E$ is perpendicular to the sheet and equal in magnitude on both sides
2. On the curved side of the pillbox, $\vec E \perp d\vec S$, so no flux passes through it
3. On each flat face $\vec E \parallel d\vec S$ and $E$ is constant
4. $\Phi = EA + EA = 2EA$  — *(both faces contribute, and they are outward on both sides)*
5. Charge enclosed $q_{\text{enc}} = \sigma A$  — *(only the patch of sheet inside the pillbox)*
6. Gauss's law: $2EA = \dfrac{\sigma A}{\varepsilon_0}$
7. $A$ cancels  — *(again, the answer cannot depend on the size of surface we chose)*
8. $E = \dfrac{\sigma}{2\varepsilon_0}$

**Result:** $E = \dfrac{\sigma}{2\varepsilon_0}$ — **independent of distance** from the sheet

*Just outside a **conductor** the answer is $\sigma/\varepsilon_0$, twice as big, because there the field exists on one side only — the other face of the pillbox is inside the metal where $E = 0$, so only one face contributes at step 4.*

### `PD6` Field of a uniformly charged thin spherical shell — *3–5 marks*

> A thin shell of radius $R$ carrying total charge $q$ spread uniformly, so $\sigma = q/4\pi R^2$. By symmetry the field is radial and depends only on distance from the centre. Take a concentric spherical Gaussian surface of radius $r$ — once with $r \gt R$, once with $r \lt R$.

**Figure.** A charged spherical shell of radius R with two concentric dashed Gaussian spheres: one outside of radius r greater than R enclosing the whole charge, and one inside of radius r less than R enclosing no charge at all, so the field inside is zero.

*Outside, the Gaussian sphere encloses all of $q$ and the shell behaves exactly like a point charge at its centre. Inside, it encloses nothing — and Gauss's law then forces $E$ to be zero.*

1. **Case 1: outside, $r \gt R$.** Take a concentric sphere of radius $r$
2. By symmetry $E$ is constant over it and $\vec E \parallel d\vec S$ everywhere
3. $\Phi = E\left(4\pi r^2\right)$  — *(surface area of a sphere)*
4. $q_{\text{enc}} = q$  — *(the whole shell is inside)*
5. $E\left(4\pi r^2\right) = \dfrac{q}{\varepsilon_0}$
6. $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}$  — *(identical to a point charge $q$ at the centre)*
7. **Case 2: on the surface, $r = R$.** Put $r=R$ and $q = \sigma\left(4\pi R^2\right)$
8. $E = \dfrac{\sigma}{\varepsilon_0}$
9. **Case 3: inside, $r \lt R$.** Take a concentric sphere of radius $r \lt R$
10. All the charge lies on the shell, *outside* this surface, so $q_{\text{enc}} = 0$  — *(this is the whole argument)*
11. $E\left(4\pi r^2\right) = \dfrac{0}{\varepsilon_0} = 0$
12. $E = 0$ everywhere inside

**Result:** $r \gt R: E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^{2}} \qquad r = R: E = \dfrac{\sigma}{\varepsilon_0} \qquad r \lt R: E = 0$

*The field is **discontinuous** at the surface, jumping from 0 to $\sigma/\varepsilon_0$. The potential is not — it stays constant inside at the surface value, which is PD8's result.*

## `CH 2` Electrostatic Potential and Capacitance — *7 derivations*

### `PD7` Potential due to a point charge — *2–3 marks*

> A point charge $+q$ at O. Bring a unit positive test charge from infinity to a point P at distance $r$, along the line joining them. At an intermediate distance $x$ the field is $q/4\pi\varepsilon_0x^2$, and the external force needed is equal and opposite to the electric force, so the work done against the field is what we integrate.

**Figure.** A point charge q at O with a test charge being brought in from infinity on the right to a point P at distance r. At an intermediate distance x the small displacement dx is marked, against the outward electric field.

*The test charge moves inward while the field pushes outward, so the work is done *against* the field. The displacement $d\vec x$ and $\vec E$ are antiparallel, which is where the minus sign in $W = -\int \vec E\cdot d\vec x$ comes from.*

1. Field at distance $x$ from the charge: $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{x^2}$
2. Force on a unit positive test charge: $F = E$
3. The external agent must apply $-\vec E$ to move it without acceleration  — *(quasi-static: no kinetic energy gained)*
4. Small work done in moving through $dx$: $dW = -E\,dx$
5. $W = -\displaystyle\int_{\infty}^{r} \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{x^2}\,dx$  — *(integrating from infinity to P)*
6. $= -\dfrac{q}{4\pi\varepsilon_0}\left[-\dfrac{1}{x}\right]_{\infty}^{r}$  — *($\int x^{-2}dx = -x^{-1}$)*
7. $= \dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{1}{x}\right]_{\infty}^{r} = \dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{1}{r} - \dfrac{1}{\infty}\right]$
8. $\dfrac{1}{\infty} = 0$  — *(the convention $V(\infty)=0$ enters here)*
9. $W = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r}$
10. $V = \dfrac{W}{q_0}$ with $q_0 = 1$

**Result:** $V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r}$

*Falls as $1/r$ where $E$ falls as $1/r^2$ — the integral of an inverse square is an inverse first power. For several charges just add these algebraically, signs included: potential is a scalar.*

### `PD8` Potential of a charged spherical shell, inside and out — *3 marks*

> The shell of PD6: radius $R$, total charge $q$. Use the field results already established there and integrate them, splitting the journey at the surface when the point is inside.

> **Shared setup with PD6.** This derivation consumes PD6's three field results. Do them as a pair — the field first, then the potential — and the "$E=0$ but $V\neq0$" question answers itself.

**Figure.** Graph of potential against distance from the centre of a charged shell: constant at the surface value from the centre out to radius R, then falling as one over r beyond R, with no discontinuity at the surface.

*Flat inside, $1/r$ outside, and **continuous** at $r=R$ — unlike the field, which jumps. A flat $V$ is exactly what $E = -dV/dr = 0$ means.*

1. **Outside, $r \gt R$.** $V = -\displaystyle\int_{\infty}^{r}\vec E\cdot d\vec l$ with $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}$  — *(PD6, case 1)*
2. This is the same integral as PD7, so $V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r}$
3. **On the surface, $r=R$.** Put $r=R$: $V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{R}$
4. **Inside, $r \lt R$.** Split the path at the surface:
5. $V = -\displaystyle\int_{\infty}^{R}\vec E\cdot d\vec l \;-\; \int_{R}^{r}\vec E\cdot d\vec l$
6. The first integral is step 3, giving $\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{R}$
7. Inside the shell $E = 0$  — *(PD6, case 3)*
8. So the second integral is zero
9. $V_{\text{inside}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{R} = V_{\text{surface}}$

**Result:** $r \geq R:\ V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r} \qquad r \lt R:\ V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{R}$, constant

*Steps 7–8 are the answer to "the field inside a shell is zero; is the potential zero too?" No — zero field means the potential does not *change*, so it holds its surface value.*

### `PD9` Potential energy of a system of point charges — *2–3 marks*

> Assemble three charges $q_1, q_2, q_3$ at the corners of a triangle, bringing them in one at a time from infinity. The energy of the system is the total work done by the external agent. The trick is that each new charge must be brought in against the field of all the ones already placed.

**Figure.** Three charges at the corners of a triangle with the three pairwise separations r12, r13 and r23 marked along the sides, showing that the system energy is a sum over the three pairs.

*Three charges make exactly three pairs. Each side of the triangle contributes one term — count sides, not corners, and you cannot miscount the terms.*

1. Bring $q_1$ in first. Space is empty, so no work is done: $W_1 = 0$
2. Bring $q_2$ in. It moves in the potential of $q_1$, which at distance $r_{12}$ is $\dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1}{r_{12}}$
3. $W_2 = q_2 V_1 = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1q_2}{r_{12}}$  — *(work = charge × potential at that point)*
4. Bring $q_3$ in. It now moves in the combined potential of $q_1$ **and** $q_2$
5. $W_3 = q_3\left(V_1 + V_2\right) = \dfrac{1}{4\pi\varepsilon_0}\left[\dfrac{q_1q_3}{r_{13}} + \dfrac{q_2q_3}{r_{23}}\right]$  — *(potentials add as scalars)*
6. Total energy $U = W_1 + W_2 + W_3$
7. $U = \dfrac{1}{4\pi\varepsilon_0}\left[\dfrac{q_1q_2}{r_{12}} + \dfrac{q_1q_3}{r_{13}} + \dfrac{q_2q_3}{r_{23}}\right]$
8. In general, $U = \dfrac{1}{4\pi\varepsilon_0}\displaystyle\sum_{i \lt j}\dfrac{q_iq_j}{r_{ij}}$  — *(the restriction $i \lt j$ counts each pair exactly once)*

**Result:** $U = \dfrac{1}{4\pi\varepsilon_0}\left[\dfrac{q_1q_2}{r_{12}} + \dfrac{q_1q_3}{r_{13}} + \dfrac{q_2q_3}{r_{23}}\right]$

*The answer does not depend on the order you bring them in — a good check. Keep the signs: a mixed set of charges gives negative $U$, meaning energy is released on assembly.*

### `PD10` Capacitance of a parallel plate capacitor — *3 marks*

> Two parallel plates of area $A$ separated by $d$, carrying $+Q$ and $-Q$, with $d$ small enough that the field between them is uniform and edge effects are ignored. Find the field, integrate it to get $V$, then divide.

**Figure.** A parallel plate capacitor: two horizontal plates of area A separated by distance d, the top carrying positive charge and the bottom negative, with uniform downward field lines between them and no field outside.

*Each plate alone gives $\sigma/2\varepsilon_0$. Between the plates the two fields point the same way and add; outside they oppose and cancel — which is why the field is confined to the gap.*

1. Surface charge density on each plate: $\sigma = \dfrac{Q}{A}$
2. Field due to the positive plate alone: $\dfrac{\sigma}{2\varepsilon_0}$  — *(PD5, infinite sheet)*
3. Field due to the negative plate alone: $\dfrac{\sigma}{2\varepsilon_0}$, in the **same** direction in the gap
4. Between the plates the two add: $E = \dfrac{\sigma}{2\varepsilon_0} + \dfrac{\sigma}{2\varepsilon_0} = \dfrac{\sigma}{\varepsilon_0}$
5. Outside, they point oppositely and cancel: $E = 0$  — *(worth stating — it justifies ignoring everything outside)*
6. $E = \dfrac{Q}{A\varepsilon_0}$
7. The field is uniform, so $V = Ed$  — *($V = -\int\vec E\cdot d\vec l$ with $E$ constant)*
8. $V = \dfrac{Qd}{A\varepsilon_0}$
9. $C = \dfrac{Q}{V} = \dfrac{Q A\varepsilon_0}{Qd}$
10. $C = \dfrac{\varepsilon_0 A}{d}$

**Result:** $C = \dfrac{\varepsilon_0 A}{d}$

*$Q$ cancels at step 9, which is the proof that capacitance is a property of the **geometry alone** — it does not depend on how much charge you put on.*

### `PD11` Capacitance with a dielectric slab in the gap — *3 marks*

> The same capacitor, now with a slab of dielectric constant $K$ and thickness $t$ inserted, where $t \lt d$. Inside the slab the induced polarisation charges reduce the field by a factor $K$; in the remaining gap it is unchanged. The potential difference is built up piece by piece.

> **Shared setup with PD10.** Identical up to step 6 of that derivation. The only new physics is that the field inside a dielectric is $E/K$.

**Figure.** A parallel plate capacitor with a dielectric slab of thickness t occupying part of the gap of width d. The field is E in the empty parts and the smaller value E over K inside the slab.

*The slab does not change the charge, only the field within its own thickness. Since $V$ is the field integrated across the gap, a smaller field over part of the path means a smaller $V$ — and so a larger $C$.*

1. Field in the empty part of the gap: $E = \dfrac{\sigma}{\varepsilon_0} = \dfrac{Q}{A\varepsilon_0}$  — *(PD10, step 6)*
2. Field inside the dielectric: $E' = \dfrac{E}{K}$  — *(induced charges oppose the applied field, reducing it by $K$)*
3. Thickness of empty gap: $d - t$; thickness of slab: $t$
4. $V = E(d-t) + E'\,t$  — *(add the potential drop across each region)*
5. $V = E(d-t) + \dfrac{E}{K}t = E\left[(d-t) + \dfrac{t}{K}\right]$
6. $V = \dfrac{Q}{A\varepsilon_0}\left[d - t + \dfrac{t}{K}\right]$
7. $C = \dfrac{Q}{V}$
8. $C = \dfrac{\varepsilon_0 A}{d - t + \dfrac{t}{K}}$

**Result:** $C = \dfrac{\varepsilon_0 A}{d - t + \dfrac{t}{K}}$

*Two checks worth quoting: $t = d$ gives $C = K\varepsilon_0A/d$ (fully filled), and $K = 1$ gives $\varepsilon_0A/d$ (no slab). Since $K \gt 1$, the denominator shrinks and $C$ always **increases** — and the result does not depend on where in the gap the slab sits.*

### `PD12` Energy stored in a capacitor, and energy density — *3 marks*

> Charging a capacitor means moving charge from one plate to the other against a rising potential difference. Take the capacitor at an intermediate stage, holding charge $q$ with potential $V' = q/C$, and move one more small charge $dq$ across.

**Figure.** Graph of potential difference against charge on a capacitor: a straight line through the origin of slope one over C, with the shaded triangular area beneath it representing the energy stored, equal to one half Q V.

*The shaded area under the line *is* the work done, since $dW = V'\,dq$. It is a triangle, not a rectangle — which is the whole reason for the factor of $\tfrac12$.*

1. At an intermediate stage the capacitor holds charge $q$ at potential $V' = \dfrac{q}{C}$
2. Work to move a further small charge $dq$: $dW = V'\,dq = \dfrac{q}{C}dq$
3. $W = \displaystyle\int_0^Q \dfrac{q}{C}\,dq$  — *(summing from uncharged to fully charged)*
4. $= \dfrac{1}{C}\left[\dfrac{q^2}{2}\right]_0^Q$
5. $U = \dfrac{Q^2}{2C}$
6. Using $Q = CV$: $U = \dfrac{1}{2}CV^2 = \dfrac{1}{2}QV$  — *(three equivalent forms — use whichever the question gives you)*
7. **Energy density.** Substitute $C = \dfrac{\varepsilon_0A}{d}$ and $V = Ed$:
8. $U = \dfrac{1}{2}\cdot\dfrac{\varepsilon_0A}{d}\cdot E^2d^2 = \dfrac{1}{2}\varepsilon_0E^2\left(Ad\right)$
9. $Ad$ is the volume between the plates  — *(where the field actually lives)*
10. $u = \dfrac{U}{Ad} = \dfrac{1}{2}\varepsilon_0E^2$

**Result:** $U = \dfrac{1}{2}CV^{2} = \dfrac{1}{2}QV = \dfrac{Q^{2}}{2C} \qquad u = \dfrac{1}{2}\varepsilon_0E^{2}$

*The $\tfrac12$ is not decoration: the last charge crosses at the full $V$, the first at almost nothing, and the average is $V/2$. The energy-density form says the energy is stored in the **field**, not on the plates.*

### `PD13` Capacitors in series and in parallel — *3 marks*

> Two capacitors and a battery of voltage $V$. In **series** the same charge sits on every plate and the voltages add; in **parallel** both feel the same voltage and the charges add. Each combination follows from noting which quantity is shared.

**Figure.** Two circuit diagrams: on the left two capacitors in series across a battery carrying the same charge Q with voltages V1 and V2 adding; on the right two capacitors in parallel across a battery sharing the same voltage V with charges Q1 and Q2 adding.

*Which quantity is shared is the whole derivation. In series the charge has nowhere else to go, so it is common; in parallel both sit across the same two nodes, so the voltage is common.*

1. **Series.** The inner plates are isolated, so induction puts the same charge $Q$ on every plate
2. The voltages add: $V = V_1 + V_2$  — *(going round the loop)*
3. $V_1 = \dfrac{Q}{C_1}$, $V_2 = \dfrac{Q}{C_2}$, and $V = \dfrac{Q}{C_s}$
4. $\dfrac{Q}{C_s} = \dfrac{Q}{C_1} + \dfrac{Q}{C_2}$
5. $Q$ cancels: $\dfrac{1}{C_s} = \dfrac{1}{C_1} + \dfrac{1}{C_2}$
6. **Parallel.** Both capacitors are across the same two points, so both have voltage $V$
7. The charges add: $Q = Q_1 + Q_2$  — *(charge supplied by the battery splits between them)*
8. $Q_1 = C_1V$, $Q_2 = C_2V$, and $Q = C_pV$
9. $C_pV = C_1V + C_2V$
10. $V$ cancels: $C_p = C_1 + C_2$

**Result:** series: $\dfrac{1}{C_s} = \dfrac{1}{C_1}+\dfrac{1}{C_2}$  ·  parallel: $C_p = C_1 + C_2$

*Opposite to the resistor rules, and for a reason you can state: capacitors in series effectively increase the plate *separation*, while in parallel they increase the plate *area*.*

## `CH 3` Current Electricity — *5 derivations*

### `PD14` Current in terms of drift velocity — *2–3 marks*

> A conductor of cross-sectional area $A$ carrying current $I$, with $n$ free electrons per unit volume all drifting at average speed $v_d$. Count how much charge crosses a chosen cross-section in time $\Delta t$ by asking which electrons are close enough to make it.

**Figure.** A cylindrical conductor of cross-sectional area A with electrons drifting to the right. In time delta t every electron within a distance v-d delta t of the chosen cross-section crosses it, so the relevant volume is A times v-d delta t.

*Only electrons within $v_d\,\Delta t$ of the cross-section can reach it in time $\Delta t$. That slab of conductor is the entire content of the derivation.*

1. In time $\Delta t$, an electron travels a distance $v_d\,\Delta t$  — *(drift is a steady average motion)*
2. So every electron within $v_d\,\Delta t$ of the cross-section crosses it, and no others do
3. Volume of that slab $= A \times v_d\,\Delta t$
4. Number of electrons in it $= n \times A v_d\,\Delta t$  — *($n$ is the number per unit volume)*
5. Charge crossing $= \Delta Q = neAv_d\,\Delta t$
6. $I = \dfrac{\Delta Q}{\Delta t}$
7. $I = neAv_d$
8. Also $J = \dfrac{I}{A} = nev_d$  — *(current density)*

**Result:** $I = neAv_d \qquad J = nev_d$

*Drift speed is around $10^{-4}\ \ce{m s^-1}$ — slower than walking — while random thermal speed is about $10^{5}$. A lamp lights instantly because the **field** is established through the wire at nearly the speed of light, not because electrons rush along it.*

### `PD15` Ohm's law from drift velocity, and resistivity — *3–5 marks*

> The same conductor, length $l$ and area $A$, with a potential difference $V$ across it. Between collisions each electron accelerates in the field; after each collision its drift is randomised. The average time between collisions is the relaxation time $\tau$.

> **Shared setup with PD14.** This picks up exactly where that one stops, by asking what sets $v_d$ in the first place.

**Figure.** A conductor of length l and area A with a potential difference V across it. The uniform field E equals V over l inside, and an electron zig-zags between collisions while drifting slowly against the field direction.

*The zig-zag is the fast random thermal motion; the slow, steady leftward creep superposed on it is the drift. Only the drift carries current.*

1. Field inside the conductor: $E = \dfrac{V}{l}$  — *(uniform field over length $l$)*
2. Force on an electron: $F = eE$, so acceleration $a = \dfrac{eE}{m}$
3. After a collision the drift velocity is randomised to zero on average  — *(collisions destroy the accumulated drift)*
4. So the average drift gained in time $\tau$ is $v_d = a\tau = \dfrac{eE\tau}{m}$
5. $I = neAv_d$  — *(PD14)*
6. $I = neA\cdot\dfrac{eE\tau}{m} = \dfrac{ne^2A\tau}{m}E$
7. Substituting $E = \dfrac{V}{l}$: $I = \dfrac{ne^2A\tau}{ml}V$
8. So $V = \left(\dfrac{ml}{ne^2A\tau}\right)I$ — that is, $V \propto I$  — *(everything in the bracket is constant at fixed temperature: **this is Ohm's law**)*
9. Comparing with $V = IR$: $R = \dfrac{ml}{ne^2A\tau}$
10. Comparing with $R = \dfrac{\rho l}{A}$:
11. $\rho = \dfrac{m}{ne^2\tau}$
12. And $\sigma = \dfrac{1}{\rho} = \dfrac{ne^2\tau}{m}$, giving $\vec J = \sigma\vec E$

**Result:** $\rho = \dfrac{m}{ne^{2}\tau} \qquad \sigma = \dfrac{ne^{2}\tau}{m} \qquad \vec J = \sigma\vec E$

*Step 8 is the real content: Ohm's law is not assumed, it *comes out*. And the result explains the temperature behaviour of both material classes — heating a metal shortens $\tau$ so $\rho$ rises; heating a semiconductor raises $n$ far more than it cuts $\tau$, so $\rho$ falls.*

### `PD16` Resistors in series and in parallel — *2–3 marks*

> Two resistors and a cell of emf $V$. In **series** there is only one path, so the current is common and the voltages add. In **parallel** both are across the same two nodes, so the voltage is common and the currents add.

**Figure.** Two circuit diagrams: on the left two resistors in series carrying the same current I with voltages V1 and V2 adding; on the right two resistors in parallel across the same voltage V with currents I1 and I2 adding.

*Again the derivation is just "which quantity is shared". One path means one current; one pair of nodes means one voltage.*

1. **Series.** One path, so the same current $I$ flows through both
2. The potential drops add: $V = V_1 + V_2$  — *(Kirchhoff's loop rule)*
3. $IR_s = IR_1 + IR_2$  — *(Ohm's law on each)*
4. $I$ cancels: $R_s = R_1 + R_2$
5. **Parallel.** Both are across the same two points, so both have the same $V$
6. The current splits: $I = I_1 + I_2$  — *(Kirchhoff's junction rule — conservation of charge)*
7. $\dfrac{V}{R_p} = \dfrac{V}{R_1} + \dfrac{V}{R_2}$
8. $V$ cancels: $\dfrac{1}{R_p} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$

**Result:** series: $R_s = R_1+R_2$  ·  parallel: $\dfrac{1}{R_p} = \dfrac{1}{R_1}+\dfrac{1}{R_2}$

*$R_s$ is larger than either resistor; $R_p$ is smaller than both. If your answer breaks either rule, you have used the wrong formula.*

### `PD17` Balance condition of a Wheatstone bridge — *3 marks*

> Four resistances $P, Q, R, S$ in a quadrilateral ABCD, with a cell across the diagonal AC and a galvanometer across BD. The bridge is **balanced** when the galvanometer shows no deflection. That single condition is what makes the algebra collapse.

**Figure.** A Wheatstone bridge drawn as a diamond: resistances P and Q in the upper two arms and R and S in the lower two, a cell across the horizontal diagonal from A to C, and a galvanometer across the vertical diagonal from B to D reading zero at balance.

*At balance no current crosses BD, so B and D sit at the same potential. The bridge then behaves as two independent series pairs — P with Q, and R with S — carrying currents $I_1$ and $I_2$.*

1. At balance the galvanometer reads zero, so no current flows through BD
2. Therefore $V_B = V_D$  — *(no current through a resistanceless branch means no potential difference across it)*
3. Since no current leaves at B, the whole of $I_1$ that flows through P continues through Q
4. Likewise the whole of $I_2$ through R continues through S
5. $V_A - V_B = I_1P$ and $V_A - V_D = I_2R$
6. But $V_B = V_D$, so $I_1P = I_2R$  …(i)
7. $V_B - V_C = I_1Q$ and $V_D - V_C = I_2S$
8. Again $V_B = V_D$, so $I_1Q = I_2S$  …(ii)
9. Divide (i) by (ii): $\dfrac{I_1P}{I_1Q} = \dfrac{I_2R}{I_2S}$  — *(the unknown currents cancel — this is why we divide)*
10. $\dfrac{P}{Q} = \dfrac{R}{S}$

**Result:** $\dfrac{P}{Q} = \dfrac{R}{S}$ at balance

*In the **metre bridge**, P and Q are the two parts of a uniform wire, so their ratio is $l : (100-l)$ and the unknown becomes $X = R(100-l)/l$. The bridge is most sensitive when all four arms are comparable, so aim for a balance point near the middle of the wire.*

### `PD18` Internal resistance of a cell, using a potentiometer — *3 marks*

> A potentiometer wire carries a steady current from a driver cell, so the potential falls uniformly along it at a rate $K$ volts per unit length. The cell under test is balanced twice: once on open circuit, and once with a known resistance $R$ across it.

**Figure.** A potentiometer: a long uniform wire AB fed by a driver cell, with the test cell and a galvanometer connected to a sliding jockey. The balance point is at length l1 with the shunt key open and at the shorter length l2 with resistance R connected across the cell.

*At balance no current is drawn from the test cell, so the potentiometer reads its true **emf** — which is exactly what a voltmeter cannot do.*

1. The potential falls uniformly along the wire at $K$ volts per unit length  — *(steady current through a uniform wire)*
2. **Key open.** No current is drawn from the test cell, so it balances against its full emf
3. $\mathcal{E} = K l_1$  …(i)
4. **Key closed**, with $R$ across the cell. Now the cell drives a current, so the balance is against its **terminal voltage**
5. $V = K l_2$  …(ii)  — *($l_2 \lt l_1$, because $V \lt \mathcal{E}$)*
6. Divide (i) by (ii): $\dfrac{\mathcal{E}}{V} = \dfrac{l_1}{l_2}$  — *($K$ cancels, so it never has to be measured*
7. For a cell delivering current through $R$: $\mathcal{E} = I(R+r)$ and $V = IR$
8. $\dfrac{\mathcal{E}}{V} = \dfrac{R+r}{R}$  — *($I$ cancels)*
9. $\dfrac{l_1}{l_2} = \dfrac{R+r}{R}$
10. $\dfrac{l_1}{l_2} - 1 = \dfrac{r}{R}$
11. $r = R\left(\dfrac{l_1 - l_2}{l_2}\right)$

**Result:** $r = R\left(\dfrac{l_1-l_2}{l_2}\right)$

*Steps 6 and 8 both work by cancelling a quantity you never measured — $K$ and $I$. The same two-balance trick with two cells gives $\mathcal{E}_1/\mathcal{E}_2 = l_1/l_2$. Sensitivity improves with a **longer** wire, because that lowers $K$.*

## `CH 4` Moving Charges and Magnetism — *6 derivations*

### `PD19` Field at the centre of a circular current loop — *2–3 marks*

> A circular loop of radius $R$ carrying current $I$. Take a small element $d\vec l$ anywhere on the loop. Every element is the same distance $R$ from the centre, and every element is perpendicular to the line joining it to the centre — the two facts that make this the easiest Biot–Savart application.

**Figure.** A circular current loop of radius R with a small element dl on its circumference. The radius from the element to the centre is perpendicular to the element, so the angle between them is ninety degrees, and every element contributes a field into the page at the centre.

*Every element sits at the same distance $R$ and at $90°$ to its own radius, so $\sin\theta = 1$ throughout — and every contribution points the same way, so the vector integral becomes a plain sum of magnitudes.*

1. Biot–Savart: $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl\sin\theta}{r^2}$
2. For every element, $r = R$  — *(all points of a circle are equidistant from the centre)*
3. $d\vec l$ is tangential and $\hat r$ is radial, so $\theta = 90°$ and $\sin\theta = 1$
4. $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl}{R^2}$
5. By the right-hand rule every element's contribution points the same way (along the axis)  — *(so the magnitudes simply add — no resolution needed)*
6. $B = \displaystyle\oint dB = \dfrac{\mu_0}{4\pi}\dfrac{I}{R^2}\oint dl$
7. $\displaystyle\oint dl = 2\pi R$  — *(total circumference)*
8. $B = \dfrac{\mu_0}{4\pi}\dfrac{I}{R^2}\left(2\pi R\right)$
9. $B = \dfrac{\mu_0 I}{2R}$
10. For $N$ turns, $B = \dfrac{\mu_0 NI}{2R}$

**Result:** $B = \dfrac{\mu_0 I}{2R}$, directed along the axis by the right-hand rule

*For an **arc** subtending angle $\phi$ radians at the centre, step 7 becomes $R\phi$ instead of $2\pi R$, giving $B = \mu_0 I\phi/4\pi R$. A semicircle is the $\phi = \pi$ case.*

### `PD20` Field on the axis of a circular current loop — *3–5 marks*

> The same loop, but the field point P now sits on the axis at distance $x$ from the centre. Each element is $r = \sqrt{R^2+x^2}$ from P. Now the contributions do *not* all point the same way — they sweep round a cone — so this one needs resolution into components.

> **Shared setup with PD19.** Same loop, same element; only P moves off the centre. Putting $x=0$ in the final answer must return PD19's result, and that is your check.

**Figure.** A circular loop seen edge-on with a point P on its axis at distance x from the centre. The field contribution from an element at the top and its diametrically opposite partner at the bottom have perpendicular components that cancel and axial components that add.

*Take elements in diametrically opposite pairs. Their components perpendicular to the axis point oppositely and cancel; their axial components both point along the axis and add. Only the $\cos\theta$ part survives.*

1. Distance from any element to P: $r = \sqrt{R^2+x^2}$  — *(right triangle with legs $R$ and $x$)*
2. $d\vec l$ is perpendicular to $\hat r$ for every element, so $\sin\theta = 1$ again
3. $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl}{R^2+x^2}$
4. $d\vec B$ is perpendicular to $\vec r$, so it makes angle $\theta$ with the axis
5. Resolve: $dB\cos\theta$ along the axis, $dB\sin\theta$ perpendicular to it
6. For each element there is a diametrically opposite one whose perpendicular component is equal and opposite, so all perpendicular components cancel  — *(this is the key symmetry argument — state it)*
7. $B = \displaystyle\oint dB\cos\theta$
8. $\cos\theta = \dfrac{R}{\sqrt{R^2+x^2}}$  — *(from the same right triangle)*
9. $B = \dfrac{\mu_0}{4\pi}\dfrac{I}{R^2+x^2}\cdot\dfrac{R}{\sqrt{R^2+x^2}}\displaystyle\oint dl$
10. $\displaystyle\oint dl = 2\pi R$
11. $B = \dfrac{\mu_0}{4\pi}\dfrac{I\,R\,(2\pi R)}{\left(R^2+x^2\right)^{3/2}}$
12. $B = \dfrac{\mu_0 I R^2}{2\left(R^2+x^2\right)^{3/2}}$

**Result:** $B = \dfrac{\mu_0 I R^{2}}{2\left(R^{2}+x^{2}\right)^{3/2}}$, along the axis  ($\times N$ for $N$ turns)

*Check: $x = 0$ gives $\mu_0I/2R$, which is PD19. Far away, $x \gg R$, it becomes $\dfrac{\mu_0}{4\pi}\dfrac{2M}{x^3}$ with $M = IA$ — the loop is a magnetic dipole, which is the bridge into Chapter 5.*

### `PD21` Field of a long straight wire, by Ampère's law — *2–3 marks*

> An infinitely long straight wire carrying current $I$. By symmetry the field lines are concentric circles centred on the wire, with $B$ constant on any one circle. Choose such a circle of radius $r$ as the Amperian loop.

> **Shared method with PD22.** Both are Ampère's law: choose a loop matching the symmetry, evaluate $\oint\vec B\cdot d\vec l$ as $B\times(\text{path length})$, count the enclosed current. Only the loop shape changes.

**Figure.** A long straight wire seen end-on carrying current out of the page, with a circular Amperian loop of radius r around it. The magnetic field is tangential to the circle everywhere and constant in magnitude on it.

*The circle is chosen precisely because $\vec B$ is parallel to $d\vec l$ at every point of it and constant in magnitude — the two conditions that turn the line integral into a multiplication.*

1. By symmetry, field lines are circles around the wire and $B$ has the same magnitude at every point of a given circle
2. Choose that circle, radius $r$, as the Amperian loop
3. At every point $\vec B \parallel d\vec l$, so $\vec B\cdot d\vec l = B\,dl$  — *(the angle between them is zero)*
4. $\displaystyle\oint\vec B\cdot d\vec l = B\oint dl$  — *($B$ constant, so it comes out of the integral)*
5. $\displaystyle\oint dl = 2\pi r$
6. $\displaystyle\oint\vec B\cdot d\vec l = B\left(2\pi r\right)$
7. Current enclosed $= I$
8. Ampère's law: $B\left(2\pi r\right) = \mu_0 I$
9. $B = \dfrac{\mu_0 I}{2\pi r}$

**Result:** $B = \dfrac{\mu_0 I}{2\pi r}$, tangential, sense given by the right-hand thumb rule

*$B \propto 1/r$. Note the structural echo of PD4, the electric field of a line charge — same geometry, same $1/r$, different law.*

### `PD22` Field inside a long solenoid, by Ampère's law — *3 marks*

> A long solenoid with $n$ turns per unit length carrying current $I$. Inside it the field is uniform and along the axis; outside a long solenoid it is negligible. Take a rectangular Amperian loop with one side of length $L$ inside the solenoid and the opposite side outside it.

**Figure.** A long solenoid in cross-section with a rectangular Amperian loop. The side of length L inside the solenoid lies along the uniform axial field; the opposite side is outside where the field is zero; the two short sides are perpendicular to the field so contribute nothing.

*Three of the loop's four sides contribute nothing — one because the field is zero out there, two because they run perpendicular to it. Only the inside side of length $L$ survives.*

1. Inside a long solenoid the field is uniform and parallel to the axis; outside it is negligible
2. Take a rectangular loop with the side of length $L$ inside, parallel to the axis
3. Along that side, $\vec B\parallel d\vec l$ and $B$ is constant, contributing $BL$
4. Along the opposite side, outside the solenoid, $B = 0$, contributing nothing
5. Along the two short sides, $\vec B \perp d\vec l$, contributing nothing  — *(the dot product vanishes)*
6. $\displaystyle\oint\vec B\cdot d\vec l = BL$
7. Number of turns threaded by the loop $= nL$
8. Current enclosed $= \left(nL\right)I$  — *(each turn carries $I$ through the loop)*
9. Ampère's law: $BL = \mu_0 nLI$
10. $L$ cancels: $B = \mu_0 nI$

**Result:** $B = \mu_0 n I$ — uniform, independent of position inside

*At the **end** of a solenoid the field is half this, $\mu_0nI/2$. For a **toroid** the same argument with a circular loop gives the same formula with $n = N/2\pi r$.*

### `PD23` Force between two parallel currents, and the definition of the ampere — *3 marks*

> Two long parallel wires, separation $r$, carrying $I_1$ and $I_2$ in the same direction. Each sits in the field of the other. Compute the field of the first at the position of the second, then the force that field exerts on a length $L$ of the second.

**Figure.** Two parallel wires carrying currents in the same direction. The field of the first wire at the position of the second points into the page, and the resulting force on the second wire points towards the first, so the wires attract.

*Wire 1's field at wire 2 points into the page; applying $\vec F = I(\vec L\times\vec B)$ to wire 2 gives a force pointing back towards wire 1. Parallel currents attract — the opposite of what like charges do.*

1. Field of wire 1 at the position of wire 2: $B_1 = \dfrac{\mu_0 I_1}{2\pi r}$  — *(PD21)*
2. Force on a length $L$ of wire 2 in that field: $F = B_1 I_2 L\sin\theta$
3. The wire is perpendicular to the field, so $\theta = 90°$ and $\sin\theta = 1$
4. $F = B_1 I_2 L = \dfrac{\mu_0 I_1}{2\pi r}I_2 L$
5. $\dfrac{F}{L} = \dfrac{\mu_0 I_1 I_2}{2\pi r}$
6. By Fleming's left-hand rule the force on wire 2 points towards wire 1, and by Newton's third law wire 1 is pulled equally towards wire 2  — *(so currents in the same direction attract)*
7. **Definition of the ampere.** Put $I_1 = I_2 = 1\ \text{A}$ and $r = 1\ \text{m}$:
8. $\dfrac{F}{L} = \dfrac{4\pi\times10^{-7}\times1\times1}{2\pi\times1}$
9. $\dfrac{F}{L} = 2\times10^{-7}\ \ce{N m^-1}$

**Result:** $\dfrac{F}{L} = \dfrac{\mu_0 I_1I_2}{2\pi r}$  ·  one ampere is the current which, in two infinitely long parallel wires 1 m apart in vacuum, produces a force of $2\times10^{-7}\ \ce{N m^-1}$

*Currents in **opposite** directions repel. Steps 7–9 are the whole answer to "define the ampere", and are worth writing out in that form.*

### `PD24` Torque on a current loop in a magnetic field — *3 marks*

> A rectangular loop of sides $l$ and $b$, carrying current $I$, placed in a uniform field $\vec B$ with its plane making angle $\theta$ between the normal to the loop and the field. The two sides of length $l$ carry forces that form a couple; the other two produce forces along the same line that simply cancel.

**Figure.** A rectangular current loop seen edge-on in a horizontal magnetic field, tilted so that its normal makes angle theta with the field. Forces I l B act out of and into the page on the two long sides, forming a couple whose arm is b sine theta.

*Seen edge-on, the loop is a line. One long side carries force out of the page, the other into it — equal, opposite, and separated by the perpendicular distance $b\sin\theta$.*

1. Force on a current-carrying side: $F = BIl\sin\alpha$, with $\alpha$ the angle between the side and $\vec B$
2. The two sides of length $l$ are perpendicular to $\vec B$, so each feels $F = BIl$
3. These two forces are equal, opposite and not collinear — a couple
4. The other two sides feel forces along the same line, equal and opposite, which cancel and give no torque  — *(state this, or the derivation is incomplete)*
5. Perpendicular distance between the lines of action of the couple $= b\sin\theta$  — *(from the edge-on geometry)*
6. $\tau = F \times b\sin\theta = \left(BIl\right)b\sin\theta$
7. $lb = A$, the area of the loop
8. $\tau = BIA\sin\theta$
9. For $N$ turns, $\tau = NBIA\sin\theta$
10. Writing $M = NIA$: $\tau = MB\sin\theta$, or $\vec\tau = \vec M\times\vec B$

**Result:** $\vec\tau = \vec M\times\vec B, \qquad \tau = NIAB\sin\theta, \qquad M = NIA$

*Maximum when the loop's **plane** is parallel to $\vec B$ ($\theta = 90°$), zero when the plane is perpendicular. Net force is always zero in a uniform field — the loop rotates but does not drift. This is the working principle of the motor and the moving-coil galvanometer.*

## `CH 5` Magnetism and Matter — *3 derivations*

### `PD25` A bar magnet behaves as an equivalent solenoid — *3–5 marks*

> A solenoid of radius $a$, length $2l$, with $n$ turns per unit length carrying current $I$. Find its field at a point P on the axis, far away at distance $r$ from the centre. Treat the solenoid as a stack of circular loops, use PD20 for each, and integrate along the length.

> **Shared setup with PD20.** Each slice of the solenoid is one circular loop, so PD20's axial-field result is the integrand here.

**Figure.** A solenoid of radius a and half-length l drawn in section, with a thin slice of width dx at distance x from the centre. A point P lies on the axis far to the right at distance r from the centre, so the slice is r minus x from P.

*The shaded slice of width $dx$ holds $n\,dx$ turns and acts as one loop. Summing all such slices from $-l$ to $+l$ turns the solenoid into a single dipole.*

1. Take a slice of width $dx$ at distance $x$ from the centre; it contains $n\,dx$ turns
2. Its distance from P is $(r-x)$
3. Axial field of one loop: $dB = \dfrac{\mu_0\,I\,a^2\,(n\,dx)}{2\left(a^2 + (r-x)^2\right)^{3/2}}$  — *(PD20, with $N \to n\,dx$)*
4. P is far away, so $r \gg a$ and $r \gg x$  — *(the far-field approximation — state it)*
5. Then $a^2 + (r-x)^2 \approx r^2$
6. $dB \approx \dfrac{\mu_0\,n\,I\,a^2}{2r^3}\,dx$
7. $B = \displaystyle\int_{-l}^{+l}\dfrac{\mu_0 n I a^2}{2r^3}\,dx$
8. $B = \dfrac{\mu_0 n I a^2}{2r^3}\left(2l\right)$  — *(the integrand is now constant, so the integral is just the length $2l$)*
9. $B = \dfrac{\mu_0}{4\pi}\cdot\dfrac{2\left(n\,2l\right)I\left(\pi a^2\right)}{r^3}$  — *(regrouping to expose $N$ and $A$)*
10. Total turns $N = n(2l)$, and cross-sectional area $A = \pi a^2$, so $M = NIA$
11. $B = \dfrac{\mu_0}{4\pi}\dfrac{2M}{r^3}$

**Result:** $B = \dfrac{\mu_0}{4\pi}\dfrac{2M}{r^{3}}$ — identical to the axial field of a bar magnet of moment $M$

*This is the whole point: a solenoid's far field is indistinguishable from a bar magnet's, which is what licenses treating magnets as dipoles throughout the chapter. Compare the form with PD1 — the electric axial dipole field — and note they differ only in the constant.*

### `PD26` A magnetic dipole oscillating in a uniform field performs SHM — *3 marks*

> A bar magnet of moment $M$ and moment of inertia $I$ suspended so it can rotate freely in a uniform field $\vec B$. Displace it by a small angle $\theta$ from the field direction and release. The restoring torque is the magnetic one; show it is proportional to $-\theta$, which is the definition of SHM.

**Figure.** A bar magnet suspended by a thread, displaced by a small angle theta from the horizontal field direction. The magnetic torque acts to restore it towards alignment, producing simple harmonic oscillation.

*The torque always acts to pull the magnet back towards alignment. For small $\theta$ it is proportional to the displacement itself — which is exactly the condition for simple harmonic motion.*

1. Torque on the magnet: $\tau = -MB\sin\theta$  — *(the minus sign says it opposes the displacement)*
2. Newton's second law for rotation: $\tau = I\alpha$, with $\alpha = \dfrac{d^2\theta}{dt^2}$
3. $I\dfrac{d^2\theta}{dt^2} = -MB\sin\theta$
4. For **small** $\theta$, $\sin\theta \approx \theta$ in radians  — *(this approximation is what makes the motion harmonic, and it must be stated)*
5. $I\dfrac{d^2\theta}{dt^2} = -MB\theta$
6. $\dfrac{d^2\theta}{dt^2} = -\dfrac{MB}{I}\theta$
7. Compare with the SHM equation $\dfrac{d^2\theta}{dt^2} = -\omega^2\theta$
8. $\omega^2 = \dfrac{MB}{I}$
9. $T = \dfrac{2\pi}{\omega} = 2\pi\sqrt{\dfrac{I}{MB}}$
10. Rearranged for the field: $B = \dfrac{4\pi^2 I}{MT^2}$

**Result:** $T = 2\pi\sqrt{\dfrac{I}{MB}} \qquad B = \dfrac{4\pi^{2}I}{MT^{2}}$

*Here $I$ is the **moment of inertia**, not current — for a bar of mass $m$ and length $L$ about its centre, $I = mL^2/12$. This is how a vibration magnetometer measures the horizontal component of the Earth's field.*

### `PD27` Magnetic moment of an electron in a circular orbit — *2–3 marks*

> An electron of charge $e$ and mass $m$ circling a nucleus in an orbit of radius $r$ with speed $v$. A circulating charge is a current loop, so it has a magnetic moment. Relate that moment to the electron's angular momentum — the link that underlies all atomic magnetism.

**Figure.** An electron orbiting a nucleus in a circle of radius r with speed v. The electron circulates one way, so the conventional current runs the opposite way, and the resulting magnetic moment points opposite to the orbital angular momentum.

*The electron circulates one way; conventional current runs the other. That single sign flip is why the magnetic moment points opposite to the angular momentum.*

1. Period of one orbit: $T = \dfrac{2\pi r}{v}$
2. The charge $e$ passes any point once per period, so $I = \dfrac{e}{T} = \dfrac{ev}{2\pi r}$  — *(a circulating charge *is* a current)*
3. Magnetic moment of a single loop: $M = IA$
4. $A = \pi r^2$
5. $M = \dfrac{ev}{2\pi r}\times\pi r^2 = \dfrac{evr}{2}$
6. Orbital angular momentum: $L = mvr$
7. So $vr = \dfrac{L}{m}$
8. $M = \dfrac{e}{2}\cdot\dfrac{L}{m} = \dfrac{e}{2m}L$
9. The electron's charge is negative, so $\vec M$ is antiparallel to $\vec L$: $\vec M = -\dfrac{e}{2m}\vec L$
10. Bohr's quantisation gives $L = \dfrac{nh}{2\pi}$
11. $M = \dfrac{e}{2m}\cdot\dfrac{nh}{2\pi} = \dfrac{neh}{4\pi m}$
12. For $n=1$: $M = \dfrac{eh}{4\pi m} = \mu_B = 9.27\times10^{-24}\ \ce{A m^2}$

**Result:** $\vec M = -\dfrac{e}{2m}\vec L \qquad \mu_B = \dfrac{eh}{4\pi m} = 9.27\times10^{-24}\ \ce{A m^{2}}$

*The ratio $e/2m$ is the **gyromagnetic ratio**, the same for every electron orbit. $\mu_B$, the Bohr magneton, is the natural unit of atomic magnetic moment.*

## `CH 6` Electromagnetic Induction — *5 derivations*

### `PD28` Motional emf, and the energy balance behind it — *3–5 marks*

> A conducting rod of length $l$ slides with velocity $v$ along two parallel rails in a uniform field $\vec B$ perpendicular to the plane of the circuit, with a resistance $R$ closing the loop. As the rod moves, the enclosed area grows, so the flux grows.

**Figure.** A conducting rod sliding to the right on two horizontal rails in a magnetic field into the page, with a resistance R closing the circuit on the left. The area of the loop increases as the rod moves, and an induced current flows opposing the motion.

*Moving the rod by $dx$ sweeps out extra area $l\,dx$, and it is that growing area — not a changing $B$ — which changes the flux here.*

1. Flux through the circuit: $\Phi_B = B\,A = B\,l\,x$
2. Moving the rod by $dx$ increases the area by $l\,dx$, so $d\Phi_B = B\,l\,dx$
3. Faraday's law: $\varepsilon = -\dfrac{d\Phi_B}{dt} = -Bl\dfrac{dx}{dt}$
4. $\dfrac{dx}{dt} = v$
5. $\varepsilon = -Blv$, of magnitude $Blv$  — *(the minus sign is Lenz's law: the induced effect opposes the growth in flux)*
6. Induced current: $I = \dfrac{\varepsilon}{R} = \dfrac{Blv}{R}$
7. That current, in the same field, makes the rod feel a force $F = BIl$  — *(a current-carrying conductor in a field — PD24's starting point)*
8. $F = B\left(\dfrac{Blv}{R}\right)l = \dfrac{B^2l^2v}{R}$, directed **opposing** the motion
9. Power the agent must supply to keep $v$ constant: $P_{\text{applied}} = Fv = \dfrac{B^2l^2v^2}{R}$
10. Power dissipated in the resistance: $P = I^2R = \left(\dfrac{Blv}{R}\right)^2R = \dfrac{B^2l^2v^2}{R}$
11. The two are equal  — *(so the electrical energy came from the mechanical work — nothing was created)*

**Result:** $\varepsilon = Blv, \quad I = \dfrac{Blv}{R}, \quad F = \dfrac{B^{2}l^{2}v}{R}, \quad P_{\text{applied}} = P_{\text{dissipated}}$

*Steps 9–11 are the answer to "show that Lenz's law follows from conservation of energy". If the induced force *helped* the motion you would get free energy — which is why the minus sign must be there.*

### `PD29` Self-inductance of a long solenoid — *2–3 marks*

> A long solenoid of length $l$, cross-sectional area $A$, with $N$ total turns ($n = N/l$ per unit length) carrying current $I$. Self-inductance is defined by $N\Phi = LI$, so find the flux linkage and divide by the current.

> **Shared setup with PD22.** The field inside is $\mu_0nI$ from that derivation; everything here is bookkeeping on top of it.

**Figure.** A solenoid of length l and cross-sectional area A with N turns carrying current I. The uniform internal field mu-zero n I threads all N turns, giving a total flux linkage N times B times A.

*The same uniform field threads every one of the $N$ turns, so the flux *linkage* is $N$ times the flux through one turn. That factor of $N$, on top of the $n$ already inside $B$, is why $L$ goes as $N^2$.*

1. Field inside the solenoid: $B = \mu_0 n I$  — *(PD22)*
2. Flux through one turn: $\Phi = BA = \mu_0 n I A$
3. The same flux threads all $N$ turns, so total flux linkage $= N\Phi$
4. $N\Phi = N\mu_0 n I A$
5. By definition $N\Phi = LI$
6. $LI = N\mu_0 n I A$
7. $I$ cancels: $L = \mu_0 n N A$  — *(as it must — inductance is a property of the coil, not of the current in it)*
8. $N = nl$
9. $L = \mu_0 n^2 A l$, equivalently $L = \dfrac{\mu_0 N^2 A}{l}$
10. With a core of relative permeability $\mu_r$, multiply by $\mu_r$

**Result:** $L = \mu_0 n^{2} A l = \dfrac{\mu_0 N^{2}A}{l}$  ($\times\mu_r$ with a core)

*Note the symbol clash: $L$ on the left is **inductance**, $l$ on the right is **length**. Doubling the turns quadruples $L$, because $N$ enters twice — once in the field, once in the linkage.*

### `PD30` Mutual inductance of two coaxial solenoids — *3 marks*

> Two long coaxial solenoids of the same length $l$: an inner one of $N_1$ turns and area $A$, and an outer one of $N_2$ turns. Pass a current $I_1$ through the inner one and find the flux it links through the outer one.

> **Shared setup with PD29.** Same field, same flux; the only change is that the flux is now counted through a *second* coil.

**Figure.** Two coaxial solenoids of the same length: an inner one of N1 turns and area A carrying current I1, surrounded by an outer one of N2 turns. The field of the inner solenoid threads the outer coil, linking flux through it.

*Only the inner solenoid's own cross-section carries field, so it is the **inner** area $A$ that appears in the answer — not the outer coil's larger area.*

1. Field produced by the inner solenoid: $B_1 = \mu_0 n_1 I_1 = \mu_0\dfrac{N_1}{l}I_1$  — *(PD22)*
2. This field exists only inside the inner solenoid, over area $A$
3. Flux through one turn of the **outer** coil: $\Phi = B_1 A$  — *(the outer turn encloses the inner solenoid, so it links exactly this flux)*
4. Total flux linkage of the outer coil: $N_2\Phi = N_2B_1A$
5. $N_2\Phi = \mu_0\dfrac{N_1N_2A}{l}I_1$
6. By definition $N_2\Phi = M I_1$
7. $I_1$ cancels
8. $M = \dfrac{\mu_0 N_1N_2A}{l}$

**Result:** $M = \dfrac{\mu_0 N_1N_2A}{l}$, and $M_{12} = M_{21}$

*Running the argument the other way — current in the outer coil, flux through the inner — gives the same $M$, which is the reciprocity theorem. This is the principle of the transformer.*

### `PD31` Energy stored in an inductor, and magnetic energy density — *3 marks*

> Building up a current in an inductor means working against the back emf it produces. Take the current at an intermediate value $i$, when the back emf is $L\,di/dt$, and compute the work done pushing a further $dq$ through against it.

> **Shared shape with PD12.** Exactly the capacitor argument with $L$ for $C$ and $i$ for $q$: the opposing quantity grows as you build up, so the energy carries a factor of $\tfrac12$.

**Figure.** Graph of back emf against current in an inductor: a straight line through the origin of slope L over the time constant, with the shaded triangular area beneath representing the energy stored, equal to one half L I squared.

*Same triangle as the capacitor's. The last increment of current is pushed against the full back emf, the first against almost none — so the average is half, and the energy is $\tfrac12LI^2$.*

1. Back emf when the current is $i$: $\varepsilon = -L\dfrac{di}{dt}$
2. The source must supply $+L\dfrac{di}{dt}$ to keep the current growing  — *(work is done against the back emf)*
3. Work in time $dt$: $dW = \varepsilon\,i\,dt = L\dfrac{di}{dt}\,i\,dt$
4. $dW = L\,i\,di$  — *($dt$ cancels)*
5. $W = \displaystyle\int_0^I L\,i\,di$
6. $W = L\left[\dfrac{i^2}{2}\right]_0^I$
7. $U = \dfrac{1}{2}LI^2$
8. **Energy density.** For a solenoid, $L = \mu_0n^2Al$ and $B = \mu_0nI$, so $I = \dfrac{B}{\mu_0 n}$
9. $U = \dfrac{1}{2}\left(\mu_0n^2Al\right)\left(\dfrac{B}{\mu_0n}\right)^2 = \dfrac{B^2}{2\mu_0}\left(Al\right)$
10. $Al$ is the volume inside the solenoid  — *(where the field actually is)*
11. $u = \dfrac{U}{Al} = \dfrac{B^2}{2\mu_0}$

**Result:** $U = \dfrac{1}{2}LI^{2} \qquad u = \dfrac{B^{2}}{2\mu_0}$

*Compare with PD12: $\tfrac12CV^2 \leftrightarrow \tfrac12LI^2$ and $\tfrac12\varepsilon_0E^2 \leftrightarrow B^2/2\mu_0$. Note $\mu_0$ sits in the denominator where $\varepsilon_0$ sat in the numerator.*

### `PD32` Emf of an AC generator — *3 marks*

> A coil of $N$ turns and area $A$ rotating with angular velocity $\omega$ in a uniform field $\vec B$. The field does not change and the area does not change — what changes is the *angle*, and that alone is enough to induce an emf.

**Figure.** A rectangular coil rotating in a uniform horizontal magnetic field, with its normal at angle omega t to the field. Below, a sine curve shows the induced emf against time, peaking when the coil's plane is parallel to the field.

*Nothing about the field or the coil changes — only the orientation. The emf peaks where the flux is momentarily zero but changing fastest, which is when the coil's plane lies *along* the field.*

1. At time $t$ the normal to the coil makes angle $\theta = \omega t$ with $\vec B$
2. Flux through one turn: $\Phi = BA\cos\omega t$  — *(the angle is measured from the normal, not the plane)*
3. Flux linkage of $N$ turns: $N\Phi = NBA\cos\omega t$
4. Faraday's law: $\varepsilon = -\dfrac{d}{dt}\left(N\Phi\right)$
5. $\varepsilon = -NBA\dfrac{d}{dt}\left(\cos\omega t\right)$
6. $\dfrac{d}{dt}\cos\omega t = -\omega\sin\omega t$
7. $\varepsilon = NBA\omega\sin\omega t$
8. Writing $\varepsilon_0 = NBA\omega$: $\varepsilon = \varepsilon_0\sin\omega t$
9. Current through resistance $R$: $I = \dfrac{\varepsilon_0}{R}\sin\omega t$

**Result:** $\varepsilon = NBA\omega\sin\omega t = \varepsilon_0\sin\omega t, \qquad \varepsilon_0 = NBA\omega$

*Emf is **maximum** when $\omega t = 90°$ — the coil's plane parallel to $\vec B$, flux instantaneously zero. It is **zero** when the plane is perpendicular and the flux is maximum. That inversion is the standard trap, and it follows from $\varepsilon$ depending on the *rate of change* of flux, not the flux.*

## `CH 7` Alternating Current — *5 derivations*

### `PD33` RMS value of an alternating current — *3 marks*

> An alternating current $i = i_0\sin\omega t$ passes through a resistance $R$. Its average over a full cycle is zero, so the average current cannot be what a meter reads. Instead define the **rms** value as the steady DC current that would produce the same heating in the same time.

**Figure.** Two curves over one cycle: the sinusoidal current, which is negative for half the cycle and averages to zero, and the squared current, which is positive throughout and averages to half the square of the peak.

*Squaring is what rescues the average. The current itself spends half its time negative; its square never does, and its mean value is exactly half the peak squared.*

1. Heat produced by a steady current $I_{\text{rms}}$ in time $T$: $H_{DC} = I_{\text{rms}}^2RT$
2. Heat produced by the alternating current in the same time: $H_{AC} = \displaystyle\int_0^T i^2R\,dt$
3. $H_{AC} = \displaystyle\int_0^T i_0^2\sin^2(\omega t)\,R\,dt$
4. $\sin^2\omega t = \dfrac{1 - \cos 2\omega t}{2}$  — *(the identity that makes this integrable)*
5. $H_{AC} = \dfrac{i_0^2R}{2}\left[\displaystyle\int_0^T dt - \int_0^T \cos2\omega t\,dt\right]$
6. $\displaystyle\int_0^T\cos2\omega t\,dt = 0$  — *(a cosine integrated over a whole number of cycles vanishes)*
7. $H_{AC} = \dfrac{i_0^2RT}{2}$
8. Setting $H_{DC} = H_{AC}$: $I_{\text{rms}}^2RT = \dfrac{i_0^2RT}{2}$
9. $I_{\text{rms}}^2 = \dfrac{i_0^2}{2}$
10. $I_{\text{rms}} = \dfrac{i_0}{\sqrt2} \approx 0.707\,i_0$

**Result:** $I_{\text{rms}} = \dfrac{i_0}{\sqrt2} \qquad E_{\text{rms}} = \dfrac{e_0}{\sqrt2}$

*Mains "220 V" is rms, so the peak is $220\sqrt2 \approx 311\ \text{V}$. The **mean over a half cycle** is a different quantity, $2i_0/\pi \approx 0.637i_0$; over a full cycle the mean is zero.*

### `PD34` AC through a pure inductor — reactance and phase lag — *3 marks*

> A source $e = e_0\sin\omega t$ across a pure inductance $L$ with no resistance. The inductor produces a back emf $L\,di/dt$; with no resistance to drop voltage across, the applied emf must exactly balance that back emf at every instant.

**Figure.** Voltage and current curves for a pure inductor: the current sine wave lags the voltage sine wave by a quarter of a cycle, reaching its peak ninety degrees after the voltage does.

*The current peaks a quarter cycle after the voltage does. The inductor resists *changes* in current, so the current is always playing catch-up.*

1. Applied emf: $e = e_0\sin\omega t$
2. Back emf across the inductor: $-L\dfrac{di}{dt}$
3. With no resistance, the net emf round the loop is zero: $e = L\dfrac{di}{dt}$  — *(there is nothing else to drop voltage across)*
4. $di = \dfrac{e_0}{L}\sin(\omega t)\,dt$
5. $i = \dfrac{e_0}{L}\displaystyle\int\sin\omega t\,dt = \dfrac{e_0}{L}\left(-\dfrac{\cos\omega t}{\omega}\right)$
6. $i = -\dfrac{e_0}{\omega L}\cos\omega t$
7. $-\cos\omega t = \sin\left(\omega t - \dfrac{\pi}{2}\right)$  — *(rewriting so the phase relation is visible)*
8. $i = \dfrac{e_0}{\omega L}\sin\left(\omega t - \dfrac{\pi}{2}\right)$
9. Comparing with $i = i_0\sin\left(\omega t - \phi\right)$: $i_0 = \dfrac{e_0}{\omega L}$ and $\phi = \dfrac{\pi}{2}$
10. Comparing $i_0 = e_0/\omega L$ with Ohm's law form $i_0 = e_0/X$: $X_L = \omega L$

**Result:** $X_L = \omega L = 2\pi f L$, and the current **lags** the voltage by $\dfrac{\pi}{2}$

*$X_L \propto f$, so an inductor blocks high frequencies and passes DC freely — at $f=0$, $X_L = 0$. That is why it is called a choke.*

### `PD35` AC through a pure capacitor — reactance and phase lead — *3 marks*

> The same source across a pure capacitance $C$. Here the applied emf equals the potential difference across the plates at every instant, and the current is the rate at which charge accumulates on them.

> **Mirror of PD34.** There the voltage was a derivative of the current; here the current is a derivative of the voltage. That single swap is why the phase shift reverses.

**Figure.** Voltage and current curves for a pure capacitor: the current sine wave leads the voltage sine wave by a quarter of a cycle, reaching its peak ninety degrees before the voltage does.

*The current peaks a quarter cycle *before* the voltage. Charge has to flow onto the plates before a potential difference can appear across them, so the current runs ahead.*

1. Applied emf equals the plate potential difference: $e_0\sin\omega t = \dfrac{q}{C}$
2. $q = Ce_0\sin\omega t$
3. $i = \dfrac{dq}{dt}$  — *(current is the rate of charge accumulation)*
4. $i = Ce_0\omega\cos\omega t$
5. $\cos\omega t = \sin\left(\omega t + \dfrac{\pi}{2}\right)$
6. $i = \omega Ce_0\sin\left(\omega t + \dfrac{\pi}{2}\right)$
7. Comparing with $i = i_0\sin\left(\omega t + \phi\right)$: $i_0 = \omega Ce_0$ and $\phi = +\dfrac{\pi}{2}$
8. Writing $i_0 = \dfrac{e_0}{X_C}$: $X_C = \dfrac{1}{\omega C}$

**Result:** $X_C = \dfrac{1}{\omega C} = \dfrac{1}{2\pi f C}$, and the current **leads** the voltage by $\dfrac{\pi}{2}$

*$X_C \propto 1/f$, the opposite of the inductor: a capacitor blocks DC completely and passes high frequencies. Remember the pair as **CIVIL** — in **C**, **I** leads **V**; **V** leads **I** in **L**.*

### `PD36` Series LCR circuit — impedance, phase angle and resonance — *5 marks*

> R, L and C in series across $e = e_0\sin\omega t$. The same current flows through all three, but each develops its voltage at a different phase — $V_R$ in phase with $I$, $V_L$ leading by $90°$, $V_C$ lagging by $90°$. So the three voltages must be added as **phasors**, not as numbers.

**Figure.** A phasor diagram for a series LCR circuit: V-R along the horizontal current direction, V-L pointing up, V-C pointing down, their difference combining with V-R by Pythagoras to give the applied voltage E at phase angle phi.

*$V_L$ and $V_C$ point in exactly opposite directions, so they subtract before combining with $V_R$ at right angles. That single geometric fact is the entire derivation.*

1. The same current $I$ flows through all three elements  — *(series)*
2. $V_R = IR$, in phase with $I$
3. $V_L = IX_L$, leading $I$ by $90°$  — *(PD34)*
4. $V_C = IX_C$, lagging $I$ by $90°$  — *(PD35)*
5. $V_L$ and $V_C$ are antiparallel, so their resultant has magnitude $\left|V_L - V_C\right|$
6. That resultant is perpendicular to $V_R$, so combine by Pythagoras:
7. $E = \sqrt{V_R^2 + \left(V_L-V_C\right)^2}$
8. $E = \sqrt{\left(IR\right)^2 + \left(IX_L - IX_C\right)^2} = I\sqrt{R^2+\left(X_L-X_C\right)^2}$
9. Comparing with $E = IZ$: $Z = \sqrt{R^2+\left(X_L-X_C\right)^2}$
10. From the same triangle, $\tan\phi = \dfrac{V_L-V_C}{V_R} = \dfrac{X_L-X_C}{R}$
11. **Resonance.** $Z$ is least when $X_L = X_C$  — *(the squared term vanishes, and it can never be negative)*
12. $\omega L = \dfrac{1}{\omega C}$, so $\omega^2 = \dfrac{1}{LC}$
13. $\omega_r = \dfrac{1}{\sqrt{LC}}$, $f_r = \dfrac{1}{2\pi\sqrt{LC}}$
14. At resonance $Z = R$ (minimum), $I = E/R$ (maximum) and $\phi = 0$

**Result:** $Z = \sqrt{R^{2}+(X_L-X_C)^{2}}, \quad \tan\phi = \dfrac{X_L-X_C}{R}, \quad \omega_r = \dfrac{1}{\sqrt{LC}}$

*$X_L \gt X_C$ makes the circuit inductive and the current lag; $X_L \lt X_C$ makes it capacitive and the current lead. Because $V_L$ and $V_C$ oppose, either can exceed the supply voltage — that is not an error.*

### `PD37` Average power in an AC circuit, and the wattless current — *3 marks*

> A circuit in which the current lags (or leads) the voltage by $\phi$. Instantaneous power is $ei$, but that oscillates; what a meter and an electricity bill record is its average over a full cycle.

**Figure.** A phasor diagram resolving the current into two components: one along the voltage, I cosine phi, which carries all the power, and one perpendicular to it, I sine phi, the wattless component which carries none.

*Only the component of current *along* the voltage does net work over a cycle. The perpendicular component stores energy for a quarter cycle and gives it all back in the next — hence "wattless".*

1. $e = e_0\sin\omega t$ and $i = i_0\sin(\omega t - \phi)$
2. Instantaneous power: $P = ei = e_0i_0\sin\omega t\,\sin(\omega t-\phi)$
3. $\sin A\sin B = \tfrac12\left[\cos(A-B) - \cos(A+B)\right]$  — *(product-to-sum identity)*
4. $P = \dfrac{e_0i_0}{2}\left[\cos\phi - \cos(2\omega t - \phi)\right]$
5. Average over a full cycle: the second term averages to zero  — *(a cosine of $2\omega t$ over a whole number of cycles)*
6. $P_{\text{avg}} = \dfrac{e_0i_0}{2}\cos\phi$
7. $\dfrac{e_0i_0}{2} = \dfrac{e_0}{\sqrt2}\cdot\dfrac{i_0}{\sqrt2} = E_{\text{rms}}I_{\text{rms}}$  — *(PD33)*
8. $P_{\text{avg}} = E_{\text{rms}}I_{\text{rms}}\cos\phi$
9. $\cos\phi$ is the **power factor**, equal to $\dfrac{R}{Z}$  — *(from PD36's triangle)*
10. For a pure inductor or capacitor $\phi = 90°$, so $\cos\phi = 0$ and $P_{\text{avg}} = 0$

**Result:** $P_{\text{avg}} = E_{\text{rms}}I_{\text{rms}}\cos\phi, \qquad \cos\phi = \dfrac{R}{Z}$

*Step 10 is the wattless-current result: a pure reactance consumes **no average power at all**. Energy flows into it for a quarter cycle and back out in the next. At resonance $\phi = 0$ and the power factor is 1.*

## `CH 8` Electromagnetic Waves — *1 derivation*

### `PD38` Displacement current, and the inconsistency it repairs — *3 marks*

> A parallel plate capacitor being charged. Apply Ampère's circuital law to a loop around the connecting wire — but evaluate it over two *different* surfaces bounded by that same loop: one cutting the wire, one bulging out to pass between the plates. Ampère's law as it stands gives two different answers, which cannot both be right.

**Figure.** A charging capacitor with an Amperian loop around the connecting wire. Surface one is a flat disc cut by the wire and carrying conduction current; surface two is a bag-shaped surface bounded by the same loop that passes between the plates where no charge flows, yet the changing electric flux there supplies an equal displacement current.

*Both dashed surfaces are bounded by the *same* loop, so Ampère's law must give the same answer for both. $S_1$ is pierced by the wire; $S_2$ passes through the empty gap. Something must be flowing through $S_2$ too.*

1. Ampère's law: $\displaystyle\oint\vec B\cdot d\vec l = \mu_0 I$, where $I$ is the current crossing *any* surface bounded by the loop
2. Take $S_1$, the flat disc cut by the wire: current crossing it is $I_c$, so the law gives $\mu_0I_c$
3. Take $S_2$, bounded by the same loop but passing between the plates: **no charge crosses it at all**, so the law gives $0$
4. The same left-hand side cannot equal two different things — Ampère's law as stated is **incomplete**  — *(this contradiction is the point of the derivation)*
5. Between the plates, $E = \dfrac{\sigma}{\varepsilon_0} = \dfrac{Q}{\varepsilon_0 A}$
6. Electric flux through $S_2$: $\Phi_E = EA = \dfrac{Q}{\varepsilon_0}$
7. Differentiating: $\dfrac{d\Phi_E}{dt} = \dfrac{1}{\varepsilon_0}\dfrac{dQ}{dt}$
8. $\dfrac{dQ}{dt} = I_c$  — *(the charge arriving on the plate is carried by the conduction current)*
9. $\varepsilon_0\dfrac{d\Phi_E}{dt} = I_c$
10. Define the **displacement current** $I_d = \varepsilon_0\dfrac{d\Phi_E}{dt}$; then $I_d = I_c$, and both surfaces now agree
11. Ampère–Maxwell law: $\displaystyle\oint\vec B\cdot d\vec l = \mu_0\left(I_c + \varepsilon_0\dfrac{d\Phi_E}{dt}\right)$

**Result:** $I_d = \varepsilon_0\dfrac{d\Phi_E}{dt} \qquad \oint\vec B\cdot d\vec l = \mu_0\left(I_c + I_d\right)$

*Displacement current is not a flow of charge — it is a changing electric field acting like one. Its consequence is the whole chapter: a changing $\vec E$ makes a $\vec B$, a changing $\vec B$ makes an $\vec E$, and the pair propagates as a wave at $c = 1/\sqrt{\mu_0\varepsilon_0}$.*

## `CH 9` Ray Optics and Optical Instruments — *7 derivations*

*Written from NCERT and from the published **Ray Optics to 9.4** page, pending processing of this chapter's eighteen lecture videos. The physics is settled; only the teacher's own emphasis is still to come.*

### `PD39` Mirror formula for a concave mirror — *3–5 marks*

> A concave mirror with pole P, focus F and centre of curvature C. Object AB stands on the principal axis beyond C, B on the axis; a real inverted image A′B′ forms. Ray AD leaves the top of the object parallel to the axis, strikes the mirror at D and reflects through F. DN is the perpendicular from D to the axis. The aperture is small.

**Figure.** A concave mirror with object arrow AB beyond the centre of curvature and a smaller inverted real image A prime B prime between C and F. One ray runs parallel to the axis and reflects through F; a second passes through C and returns along itself. The similar triangle pairs used in the derivation are visible.

*Two pairs of similar triangles do all the work: △ABC with △A′B′C (vertically opposite at C), and △DNF with △A′B′F (vertically opposite at F). The small-aperture assumption is what lets N be treated as coincident with P.*

1. In △ABC and △A′B′C: $\angle ABC = \angle A'B'C = 90°$
2. $\angle ACB = \angle A'CB'$  — *(vertically opposite)*
3. So △ABC ~ △A′B′C
4. $\dfrac{AB}{A'B'} = \dfrac{BC}{B'C}$  …(i)
5. In △DNF and △A′B′F: $\angle DNF = \angle A'B'F = 90°$
6. $\angle DFN = \angle A'FB'$  — *(vertically opposite)*
7. So △DNF ~ △A′B′F, giving $\dfrac{DN}{A'B'} = \dfrac{NF}{B'F}$
8. $DN = AB$  — *(DN is the height of the parallel ray, equal to the object height)*
9. $\dfrac{AB}{A'B'} = \dfrac{NF}{B'F}$  …(ii)
10. From (i) and (ii): $\dfrac{BC}{B'C} = \dfrac{NF}{B'F}$
11. Small aperture, so N lies very close to P and $NF \approx PF$  — *(the one approximation — state it)*
12. $\dfrac{BC}{B'C} = \dfrac{PF}{B'F}$
13. $BC = PB - PC$, $B'C = PC - PB'$, $B'F = PB' - PF$
14. Sign convention: $PB = -u$, $PB' = -v$, $PF = -f$, $PC = -R = -2f$
15. $\dfrac{-u+2f}{-2f+v} = \dfrac{-f}{-v+f}$
16. Cross-multiplying: $(-u+2f)(-v+f) = (-f)(-2f+v)$
17. $uv - uf - 2fv + 2f^2 = 2f^2 - fv$
18. $uv - uf - 2fv = -fv$
19. $uv - uf - fv = 0$
20. $uv = uf + fv$
21. Divide throughout by $uvf$: $\dfrac{1}{f} = \dfrac{1}{v} + \dfrac{1}{u}$

**Result:** $\dfrac{1}{v} + \dfrac{1}{u} = \dfrac{1}{f}$

*Note the **plus** sign — the lens formula has a minus. Magnification follows from the ray striking the pole, where the axis is the normal: $m = h'/h = -v/u$.*

### `PD40` Refraction at a single spherical surface — *3 marks*

> A single convex refracting surface of radius $R$ separating a medium of index $n_1$ from one of index $n_2$. A point object O on the axis gives an image at I. Take a ray OM striking the surface at M, close to the pole P so all angles are small.

> **Shared setup with PD41.** The lens maker's formula is this derivation applied twice — once at each face of the lens. Learn this one properly and the next is bookkeeping.

**Figure.** A convex refracting surface separating medium n1 on the left from n2 on the right, with centre of curvature C. A ray from the object O on the axis meets the surface at M, bends towards the normal, and converges to the image I; the angles alpha, beta and gamma are marked at O, I and C.

*The normal at M is the radius MC, so the angles $\alpha$, $\beta$ and $\gamma$ at O, I and C are what connect the ray geometry to Snell's law. All are small, so each equals its own tangent.*

1. MC is the normal at M  — *(a radius always meets a sphere at right angles)*
2. Angle of incidence $i = \alpha + \gamma$  — *(exterior angle of △OMC)*
3. Angle of refraction $r = \gamma - \beta$  — *(exterior angle of △MCI)*
4. Snell's law: $n_1\sin i = n_2\sin r$
5. All angles are small, so $\sin i \approx i$ and $\sin r \approx r$  — *(paraxial approximation)*
6. $n_1\left(\alpha+\gamma\right) = n_2\left(\gamma-\beta\right)$
7. For small angles, $\alpha \approx \tan\alpha = \dfrac{MP}{PO}$, $\beta \approx \dfrac{MP}{PI}$, $\gamma \approx \dfrac{MP}{PC}$
8. $n_1\left(\dfrac{MP}{PO} + \dfrac{MP}{PC}\right) = n_2\left(\dfrac{MP}{PC} - \dfrac{MP}{PI}\right)$
9. $MP$ cancels throughout  — *(which is why the result holds for every paraxial ray, not just this one)*
10. Sign convention: $PO = -u$, $PI = +v$, $PC = +R$
11. $n_1\left(\dfrac{1}{-u} + \dfrac{1}{R}\right) = n_2\left(\dfrac{1}{R} - \dfrac{1}{v}\right)$
12. $-\dfrac{n_1}{u} + \dfrac{n_1}{R} = \dfrac{n_2}{R} - \dfrac{n_2}{v}$
13. $\dfrac{n_2}{v} - \dfrac{n_1}{u} = \dfrac{n_2 - n_1}{R}$

**Result:** $\dfrac{n_2}{v} - \dfrac{n_1}{u} = \dfrac{n_2-n_1}{R}$

### `PD41` Lens maker's formula, and the thin lens formula — *5 marks*

> A thin lens of material index $n$ in air, with surfaces of radii $R_1$ and $R_2$. Refraction happens twice. Treat the first surface alone: it would form an image $I_1$. Then feed that image in as the *object* for the second surface, which produces the final image I.

**Figure.** A thin biconvex lens with an object O on the left. The first surface of radius R1 would form an intermediate image I1 to the right; that image acts as the object for the second surface of radius R2, which forms the final image I.

*The intermediate image $I_1$ never actually forms — the second surface intercepts the light first. But treating it as the object for that second refraction is exactly what makes the two-step calculation work.*

1. **At the first surface** ($n_1 = 1$ air, $n_2 = n$ glass, radius $R_1$), the image is at $v_1$:
2. $\dfrac{n}{v_1} - \dfrac{1}{u} = \dfrac{n-1}{R_1}$  …(i)  — *(PD40)*
3. **At the second surface**, light goes from glass into air, so $n_1 = n$ and $n_2 = 1$, radius $R_2$
4. The object for it is $I_1$, at distance $v_1$  — *(the lens is thin, so both surfaces are effectively at the same place)*
5. $\dfrac{1}{v} - \dfrac{n}{v_1} = \dfrac{1-n}{R_2}$  …(ii)
6. Add (i) and (ii): the $\dfrac{n}{v_1}$ terms cancel  — *(this cancellation is the point of doing it in two steps)*
7. $\dfrac{1}{v} - \dfrac{1}{u} = \dfrac{n-1}{R_1} + \dfrac{1-n}{R_2}$
8. $\dfrac{1}{v} - \dfrac{1}{u} = (n-1)\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right)$
9. For an object at infinity, $u = \infty$ and $v = f$ by definition of focal length
10. $\dfrac{1}{f} = (n-1)\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right)$  — *(the lens maker's formula)*
11. Substituting back into step 8: $\dfrac{1}{v} - \dfrac{1}{u} = \dfrac{1}{f}$

**Result:** $\dfrac{1}{f} = (n-1)\left(\dfrac{1}{R_1}-\dfrac{1}{R_2}\right) \qquad \dfrac{1}{v}-\dfrac{1}{u} = \dfrac{1}{f}$

*$n$ is the index of the lens **relative to its surroundings**. A glass lens in water has a much longer focal length; if the two indices matched, $1/f$ would be zero and the lens would disappear optically.*

### `PD42` Two thin lenses in contact — *2–3 marks*

> Two thin lenses of focal lengths $f_1$ and $f_2$ placed in contact. The image formed by the first acts as the object for the second — the same chaining trick as PD41, one level up.

**Figure.** Two thin lenses in contact with an object on the left. The first lens alone would form an intermediate image, which then serves as the object for the second lens, giving the final image closer in.

*The intermediate image $I_1$ is the object for the second lens. Because the lenses touch, its distance is measured from the same point for both — which is what lets the terms cancel.*

1. **First lens:** $\dfrac{1}{v_1} - \dfrac{1}{u} = \dfrac{1}{f_1}$  …(i)
2. **Second lens:** its object is $I_1$ at distance $v_1$, and its image is the final one at $v$
3. $\dfrac{1}{v} - \dfrac{1}{v_1} = \dfrac{1}{f_2}$  …(ii)
4. Add (i) and (ii): the $\dfrac{1}{v_1}$ terms cancel
5. $\dfrac{1}{v} - \dfrac{1}{u} = \dfrac{1}{f_1} + \dfrac{1}{f_2}$
6. But for the equivalent single lens, $\dfrac{1}{v} - \dfrac{1}{u} = \dfrac{1}{F}$
7. $\dfrac{1}{F} = \dfrac{1}{f_1} + \dfrac{1}{f_2}$
8. Since $P = 1/f$: $P = P_1 + P_2$

**Result:** $\dfrac{1}{F} = \dfrac{1}{f_1}+\dfrac{1}{f_2} \qquad P = P_1+P_2$

*Powers simply add, which is why optometrists work in dioptres. $f$ must be in **metres** for $P$ to come out in dioptres.*

### `PD43` Refraction through a prism, and minimum deviation — *5 marks*

> A prism of refracting angle $A$. A ray enters at angle $i$, refracts to $r_1$ inside, travels to the second face where it meets it at $r_2$, and emerges at $e$. The total deviation is $\delta$. Two quadrilateral/triangle angle sums give the whole result.

**Figure.** A triangular prism with a ray entering the left face at angle i, bending to r1 inside, meeting the right face at r2 and emerging at angle e. The prism angle A is at the apex and the total deviation delta is the angle between the incident ray produced and the emergent ray.

*The ray bends towards the normal entering the denser prism and away from it on leaving, so both bends turn it the same way — which is why the deviations add rather than cancel.*

1. In the quadrilateral formed by the two faces and the two normals, the angles at the two faces are $90°$ each
2. So the angle between the normals is $180° - A$
3. In the triangle formed by the two normals and the ray inside: $r_1 + r_2 + (180° - A) = 180°$
4. $r_1 + r_2 = A$  …(i)  — *(the first key relation)*
5. Deviation at the first face is $(i - r_1)$; at the second face $(e - r_2)$
6. Total deviation $\delta = (i - r_1) + (e - r_2)$  — *(both bends turn the ray the same way, so they add)*
7. $\delta = (i+e) - (r_1+r_2)$
8. Using (i): $\delta = i + e - A$
9. $A + \delta = i + e$  …(ii)  — *(the second key relation)*
10. **At minimum deviation** the ray passes symmetrically: $i = e$ and $r_1 = r_2 = r$
11. From (i): $2r = A$, so $r = \dfrac{A}{2}$
12. From (ii): $A + \delta_m = 2i$, so $i = \dfrac{A+\delta_m}{2}$
13. Snell's law at the first face: $n = \dfrac{\sin i}{\sin r}$
14. $n = \dfrac{\sin\left(\dfrac{A+\delta_m}{2}\right)}{\sin\left(\dfrac{A}{2}\right)}$

**Result:** $r_1+r_2 = A, \quad A+\delta = i+e, \quad n = \dfrac{\sin\!\left(\frac{A+\delta_m}{2}\right)}{\sin\!\left(\frac{A}{2}\right)}$

*For a **thin** prism all angles are small, $\sin\theta\approx\theta$, and this collapses to $\delta = (n-1)A$. The graph of $\delta$ against $i$ is a curve with one minimum, so every deviation except $\delta_m$ corresponds to two different angles of incidence.*

### `PD44` Magnifying power of a compound microscope — *5 marks*

> Two converging lenses: an objective of short focal length $f_o$ forming a real, inverted, magnified image inside the tube, and an eyepiece of focal length $f_e$ used as a simple magnifier on that image. The total magnification is the product of the two.

**Figure.** A compound microscope: the object just outside the objective's focus forms a real inverted enlarged image inside the tube, and the eyepiece magnifies that intermediate image to give the final much larger virtual image seen by the eye.

*The objective does the first magnification and hands its real image to the eyepiece, which magnifies again. Two stages in series, so the magnifications multiply.*

1. Magnification of the objective: $m_o = \dfrac{h'}{h} = \dfrac{v_o}{u_o}$  — *(linear magnification of a lens)*
2. The eyepiece is used as a simple magnifier on that intermediate image
3. For a simple magnifier with the final image at the near point $D$: $m_e = 1 + \dfrac{D}{f_e}$
4. Total magnification $m = m_o \times m_e$  — *(two stages in series multiply)*
5. $m = \dfrac{v_o}{u_o}\left(1 + \dfrac{D}{f_e}\right)$
6. For the **relaxed eye**, the final image is at infinity and $m_e = \dfrac{D}{f_e}$
7. $m = \dfrac{v_o}{u_o}\cdot\dfrac{D}{f_e}$
8. In practice the object sits just outside $F_o$, so $u_o \approx f_o$, and the image forms near the eyepiece, so $v_o \approx L$, the tube length
9. $m \approx \dfrac{L}{f_o}\cdot\dfrac{D}{f_e}$

**Result:** $m = \dfrac{v_o}{u_o}\left(1+\dfrac{D}{f_e}\right)$  ·  relaxed eye: $m \approx \dfrac{L}{f_o}\cdot\dfrac{D}{f_e}$

*High magnification needs **both** $f_o$ and $f_e$ small — that is why microscope lenses are tiny. $D = 25\ \text{cm}$, the least distance of distinct vision.*

### `PD45` Magnifying power of an astronomical telescope — *3–5 marks*

> A telescope viewing a distant object, so the rays arrive parallel and subtend angle $\alpha$ at the objective. The objective forms a real image at its focal plane; the eyepiece views that image, and it subtends the larger angle $\beta$ at the eye. Magnifying power is the ratio of those two angles.

**Figure.** An astronomical telescope in normal adjustment: parallel rays from a distant object arrive at angle alpha, the objective forms a real inverted image at its focal plane, and the eyepiece placed one focal length beyond sends parallel rays to the eye at the larger angle beta.

*A telescope cannot make a distant star bigger — it makes it subtend a bigger *angle*. That is why magnifying power here is a ratio of angles, not of lengths.*

1. Magnifying power $m = \dfrac{\beta}{\alpha}$  — *(angle subtended by the image at the eye ÷ angle subtended by the object)*
2. Both angles are small, so $\alpha \approx \tan\alpha$ and $\beta \approx \tan\beta$
3. The intermediate image has height $h$ at the objective's focal plane
4. $\tan\alpha = \dfrac{h}{f_o}$  — *(the object is at infinity, so its image forms at the focal plane)*
5. **Normal adjustment**: the final image is at infinity, so the intermediate image sits at the eyepiece's focus
6. $\tan\beta = \dfrac{h}{f_e}$
7. $m = \dfrac{h/f_e}{h/f_o}$
8. $h$ cancels: $m = \dfrac{f_o}{f_e}$
9. Length of the telescope $L = f_o + f_e$  — *(the two focal points coincide in normal adjustment)*
10. If instead the final image is at the near point: $m = \dfrac{f_o}{f_e}\left(1 + \dfrac{f_e}{D}\right)$

**Result:** $m = \dfrac{f_o}{f_e}$,  $L = f_o+f_e$  (normal adjustment)

*The exact **opposite** requirement from a microscope: a telescope objective wants a **long** focal length, a microscope objective a short one. A large objective also gathers more light, which is why research telescopes are big. A reflecting telescope replaces the objective lens with a concave mirror and so has no chromatic aberration at all.*

Built from the notes for Chapters 1–8 in this repository, which were grounded against the lecture board frames rather than the ASR transcripts. Chapter 9 is written from NCERT and from the published **Ray Optics to 9.4** page, pending processing of that chapter's eighteen lecture videos.

Every result here also appears, without its proof, on the companion page **Every Physics Formula**.
