`Class XII CBSE · Physics · Chapters 1–9`

# Every Physics Formula

*Nine chapters, one hundred entries. Every one carries what its symbols mean and the SI unit it comes out in, because in physics a formula without its units is half a formula. The cue is on the outside and the formula is hidden, so you can read down a chapter and test yourself rather than just re-reading.*

- Entries: 100

- Chapters: 9

- Must be instant: 78

- Constants: 14

### How to use this

**●** means it should arrive before you have finished reading the question. **○** means a few seconds is fine — these are the ones you reconstruct from a derivation rather than recall outright, and the companion page **Physics, Derived** shows how.

Each chapter opens with its own **recognise strip**: every cue in that chapter on one screen. Read the strip cold, name the formula, then tap the entry to check. That drill is worth more than re-reading the page.

Vector arrows are kept where the direction matters and dropped where only magnitude is asked. Where a symbol is overloaded across chapters — $L$ is length, inductance and angular momentum in three different chapters — the entry says which one it means.

## `CH 1` Electric Charges and Fields — *13 entries*

Recognise strip — say it, then open the entry

- `P1.1` Charge is quantised, and conserved

- `P1.2` Force between two point charges

- `P1.3` The same force with a medium in the gap

- `P1.4` Force from several charges at once

- `P1.5` Field of a point charge, and what field means

- `P1.6` Charge spread along a line, over a surface, through a volume

- `P1.7` Dipole moment

- `P1.8` Field on the axis of a dipole

- `P1.9` Field on the equatorial line of a dipole

- `P1.10` Torque and energy of a dipole in a uniform field

- `P1.11` Electric flux, and Gauss's law

- `P1.12` Field of an infinite line charge and of a plane sheet

- `P1.13` Field of a charged spherical shell, inside and out

### ● `P1.1` Charge is quantised, and conserved

$$q = \pm ne \qquad e = 1.6\times10^{-19}\ \text{C}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $q$ | charge on a body | C |
| $n$ | an integer — never a fraction | dimensionless |
| $e$ | elementary charge | 1.6 × 10⁻¹⁹ C |

**Use it when:**

> Asked how many electrons make up a given charge, or whether a stated charge is possible. $1\ \text{C}$ is about $6.25\times10^{18}$ elementary charges — which is why the coulomb is an impractically large unit.

**Trap:**

> Charge is also **conserved** and **additive**: it is a scalar, so charges add algebraically with their signs, never as vectors.

### ● `P1.2` Force between two point charges

$$F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r^2} = k\frac{Q_1Q_2}{r^2} \qquad \vec F_{21} = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r_{12}^2}\hat r_{12}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $F$ | force between the charges | N |
| $k$ | $1/4\pi\varepsilon_0$ | 9 × 10⁹ N m² C⁻² |
| $\varepsilon_0$ | permittivity of free space | 8.854 × 10⁻¹² C² N⁻¹ m⁻² |
| $r$ | separation | m |

**Use it when:**

> Two charges, and a force. Coulomb's law. Valid only for **point charges** — separation much larger than the bodies themselves.

**Trap:**

> Unlike gravitation, this force **depends on the medium** and can be attractive or repulsive. $\vec F_{12} = -\vec F_{21}$ by Newton's third law even when the charges are unequal.

### ○ `P1.3` The same force with a medium in the gap

$$F = \frac{1}{4\pi\varepsilon_0 K}\frac{Q_1Q_2}{r^2}, \qquad K = \varepsilon_r = \frac{\varepsilon}{\varepsilon_0}$$
          $$\text{partly filled: } F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{\left[(r-t)+\sqrt{K}\,t\right]^{2}}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $K$ | dielectric constant (relative permittivity) | dimensionless |
| $t$ | thickness of the dielectric slab | m |
| $\varepsilon$ | absolute permittivity of the medium | C² N⁻¹ m⁻² |

**Use it when:**

> The charges sit in water, oil or a slab rather than vacuum. A dielectric always **reduces** the force, since $K \gt 1$.

**Trap:**

> A slab of thickness $t$ behaves like $\sqrt{K}\,t$ of vacuum — the square root is easy to lose.

### ● `P1.4` Force from several charges at once

$$\vec F_1 = \vec F_{12} + \vec F_{13} + \vec F_{14} + \cdots$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\vec F_{1j}$ | force on charge 1 from charge $j$ alone | N |
| $\vec F_1$ | resultant, by vector addition | N |

**Use it when:**

> Three or more charges. Principle of superposition: compute each pair as if the others were absent, then add as vectors.

**Trap:**

> Add as **vectors**, not magnitudes. For a null-point question, first decide whether the point lies between the charges (same signs) or outside, beyond the weaker one (opposite signs) — then solve.

### ● `P1.5` Field of a point charge, and what field means

$$\vec E = \lim_{q_0\to0}\frac{\vec F}{q_0} \qquad \vec E = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\hat r \qquad \vec F = q\vec E$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\vec E$ | electric field intensity | N C⁻¹ or V m⁻¹ |
| $q_0$ | test charge, taken vanishingly small | C |
| $Q$ | source charge | C |

**Use it when:**

> Anything about field strength at a point. $E$ falls as $1/r^2$; to straighten the graph, plot $E$ against $1/r^2$.

**Trap:**

> The test charge cancels — $E$ is a property of the source and the point, not of what you probe it with. The limit exists so the probe does not disturb the field it measures.

### ○ `P1.6` Charge spread along a line, over a surface, through a volume

$$\lambda = \frac{dq}{dl} \qquad \sigma = \frac{dq}{dS} \qquad \rho = \frac{dq}{dV}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\lambda$ | linear charge density | C m⁻¹ |
| $\sigma$ | surface charge density | C m⁻² |
| $\rho$ | volume charge density | C m⁻³ |

**Use it when:**

> The charge is continuous rather than a set of points — a charged wire, sheet or sphere. These are what turn a sum into an integral, and they feed straight into the Gauss's law applications.

**Trap:**

> On a **conductor** the charge sits entirely on the outer surface, so $\sigma$ is the relevant density even for a solid sphere.

### ● `P1.7` Dipole moment

$$\vec p = Q \times 2\vec l$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\vec p$ | electric dipole moment | C m |
| $Q$ | magnitude of either charge | C |
| $2l$ | separation between the charges | m |

**Use it when:**

> Any dipole question. Direction is **from the negative charge to the positive one** — the opposite of the field it produces between them.

**Trap:**

> The separation is $2l$, not $l$. Losing the 2 halves every subsequent answer.

### ● `P1.8` Field on the axis of a dipole

$$E_{\text{axial}} = \frac{1}{4\pi\varepsilon_0}\frac{2pr}{\left(r^2-l^2\right)^2} \;\xrightarrow{\;r \gg l\;}\; \frac{1}{4\pi\varepsilon_0}\frac{2p}{r^3}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $E_{\text{axial}}$ | field on the dipole's axis | N C⁻¹ |
| $r$ | distance from the dipole's centre | m |
| $p$ | dipole moment | C m |

**Use it when:**

> The point lies on the line through both charges. Direction is **parallel** to $\vec p$.

**Trap:**

> $1/r^3$, not $1/r^2$ — a dipole's field dies faster than a point charge's because the two charges nearly cancel.

### ● `P1.9` Field on the equatorial line of a dipole

$$E_{\text{eq}} = \frac{1}{4\pi\varepsilon_0}\frac{p}{\left(r^2+l^2\right)^{3/2}} \;\xrightarrow{\;r \gg l\;}\; \frac{1}{4\pi\varepsilon_0}\frac{p}{r^3}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $E_{\text{eq}}$ | field on the perpendicular bisector | N C⁻¹ |
| $r$ | distance from the centre | m |

**Use it when:**

> The point is on the perpendicular bisector of the dipole.

**Trap:**

> Exactly **half** the axial field at the same distance, and pointing **antiparallel** to $\vec p$. Both the factor of two and the direction are asked.

### ● `P1.10` Torque and energy of a dipole in a uniform field

$$\vec\tau = \vec p\times\vec E, \quad \tau = pE\sin\theta \qquad U = -\vec p\cdot\vec E = -pE\cos\theta$$
          $$W = pE\left(\cos\theta_1 - \cos\theta_2\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\tau$ | torque | N m |
| $U$ | potential energy of the dipole | J |
| $\theta$ | angle between $\vec p$ and $\vec E$ | rad or ° |

**Use it when:**

> A dipole is placed in a field and asked to rotate. Net **force** in a uniform field is zero — only a torque acts.

**Trap:**

> $\theta = 0$ is stable equilibrium ($U = -pE$, minimum); $\theta = 180°$ is unstable ($U = +pE$). Energy is measured from $\theta = 90°$, where $U = 0$.

### ● `P1.11` Electric flux, and Gauss's law

$$\Phi = \vec E\cdot\vec A = EA\cos\theta \qquad \oint_S \vec E\cdot d\vec S = \frac{Q_{\text{enclosed}}}{\varepsilon_0}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Phi$ | electric flux | N m² C⁻¹ or V m |
| $\vec A$ | area vector, normal to the surface | m² |
| $Q_{\text{enc}}$ | net charge **inside** the closed surface | C |

**Use it when:**

> Symmetry lets you pick a Gaussian surface on which $E$ is constant — a sphere, a cylinder, a pillbox.

**Trap:**

> Only **enclosed** charge counts. A charge outside contributes zero net flux (what enters, leaves) — but it still contributes to $\vec E$ at every point on the surface.

### ● `P1.12` Field of an infinite line charge and of a plane sheet

$$E_{\text{line}} = \frac{\lambda}{2\pi\varepsilon_0 r} \qquad E_{\text{sheet}} = \frac{\sigma}{2\varepsilon_0} \qquad E_{\text{conductor surface}} = \frac{\sigma}{\varepsilon_0}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\lambda$ | linear charge density | C m⁻¹ |
| $\sigma$ | surface charge density | C m⁻² |
| $r$ | perpendicular distance from the wire | m |

**Use it when:**

> A long charged wire, or a large charged plate. Both come straight out of Gauss's law.

**Trap:**

> The sheet field is **independent of distance** — and it is $\sigma/2\varepsilon_0$ for a thin sheet with field on both sides, but $\sigma/\varepsilon_0$ just outside a **conductor**, where the field exists on one side only. Confusing the two is the classic error.

### ● `P1.13` Field of a charged spherical shell, inside and out

$$r \gt R:\ E = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2} \qquad r = R:\ E = \frac{\sigma}{\varepsilon_0} \qquad r \lt R:\ E = 0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $R$ | radius of the shell | m |
| $r$ | distance from the centre | m |
| $q$ | total charge on the shell | C |

**Use it when:**

> A hollow charged sphere or any charged conductor. Outside, it behaves exactly as if all the charge sat at the centre.

**Trap:**

> $E = 0$ inside but the **potential is not zero** — it is constant at the surface value. Zero field means no *change* in potential, not no potential.

## `CH 2` Electrostatic Potential and Capacitance — *14 entries*

Recognise strip

- `P2.1` What potential and potential difference mean

- `P2.2` Potential from the field, and the field back from potential

- `P2.3` Potential of a point charge and of a system

- `P2.4` Potential due to a dipole at any point

- `P2.5` Potential of a charged spherical shell, inside and out

- `P2.6` Energy of a system of point charges

- `P2.7` Energy of a charge, and of a dipole, in an external field

- `P2.8` Capacitance, defined

- `P2.9` Parallel plate capacitor, with and without a dielectric

- `P2.10` A dielectric slab only partly filling the gap

- `P2.11` Spherical and cylindrical capacitors

- `P2.12` Capacitors in series and in parallel

- `P2.13` Energy stored in a capacitor, and energy density

- `P2.14` Two charged capacitors joined together

### ● `P2.1` What potential and potential difference mean

$$V_A - V_B = \frac{W_{B\to A}}{q_0} \qquad V = \frac{W_{\infty\to P}}{q_0}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $V$ | electric potential | V (= J C⁻¹) |
| $W$ | work done by an **external** force, without acceleration | J |
| $q_0$ | test charge moved | C |

**Use it when:**

> Work, energy or volts are involved. Potential is a **scalar**, which is what makes it easier to work with than $\vec E$.

**Trap:**

> "Without acceleration" means the external force exactly balances the electric force, so no kinetic energy is gained. Convention: $V(\infty) = 0$.

### ● `P2.2` Potential from the field, and the field back from potential

$$V = -\int_B^A \vec E\cdot d\vec l \qquad E = -\frac{dV}{dr} \qquad \oint \vec E\cdot d\vec l = 0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $E$ | field component along $r$ | V m⁻¹ |
| $dV/dr$ | potential gradient | V m⁻¹ |

**Use it when:**

> Converting between $E$ and $V$, or asked which of two points is at higher potential.

**Trap:**

> The minus sign says $\vec E$ points toward **decreasing** potential. The closed-loop integral being zero is the statement that the electrostatic field is **conservative**.

### ● `P2.3` Potential of a point charge, and of a system

$$V = \frac{1}{4\pi\varepsilon_0}\frac{q}{r} \qquad V_P = \frac{1}{4\pi\varepsilon_0}\sum_i \frac{q_i}{r_i}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $V$ | potential at distance $r$ | V |
| $q_i$ | each charge, **with its sign** | C |
| $r_i$ | distance from each charge to the point | m |

**Use it when:**

> Potential at a point from one or several charges. Falls as $1/r$, unlike $E$'s $1/r^2$.

**Trap:**

> A **plain algebraic sum** — no vectors. Midway between $+q$ and $-q$, $V = 0$ but $\vec E \ne 0$. $V = 0$ never implies $E = 0$.

### ○ `P2.4` Potential due to a dipole at any point

$$V = \frac{p\cos\theta}{4\pi\varepsilon_0\left(r^2 - l^2\cos^2\theta\right)} \;\xrightarrow{\;r\gg l\;}\; \frac{p\cos\theta}{4\pi\varepsilon_0 r^2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\theta$ | angle from the dipole axis | rad or ° |
| $p$ | dipole moment | C m |
| $r$ | distance from the dipole centre | m |

**Use it when:**

> A general point, not just axial or equatorial. Axial is $\theta = 0$; equatorial is $\theta = 90°$.

**Trap:**

> $V = 0$ everywhere on the **equatorial line** ($\cos 90° = 0$), even though $\vec E$ is not zero there. Potential of a dipole falls as $1/r^2$, faster than a point charge's $1/r$.

### ● `P2.5` Potential of a charged spherical shell, inside and out

$$r \geq R:\ V = \frac{1}{4\pi\varepsilon_0}\frac{q}{r} \qquad r \lt R:\ V = V_{\text{surface}} = \frac{1}{4\pi\varepsilon_0}\frac{q}{R}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $R$ | radius of the shell | m |
| $V$ | potential | V |

**Use it when:**

> Any charged conductor. Sketching $V$ against $r$ is a standard question: flat inside, then $1/r$ outside.

**Trap:**

> **Constant** inside, not zero — even though $E = 0$ there. This pairs with P1.13 and the two are examined together.

### ● `P2.6` Energy of a system of point charges

$$U = \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{12}} \qquad U = \frac{1}{4\pi\varepsilon_0}\left[\frac{q_1q_2}{r_{12}} + \frac{q_1q_3}{r_{13}} + \frac{q_2q_3}{r_{23}}\right]$$

| Symbol | Meaning | Unit |
|---|---|---|
| $U$ | potential energy of the assembled system | J |
| $r_{ij}$ | separation of each pair | m |

**Use it when:**

> "Work done in assembling" a set of charges. Sum over **every distinct pair**, once each.

**Trap:**

> Three charges give three pairs, not three terms of one charge each. Keep the signs — a mixed set can give negative $U$.

### ○ `P2.7` Energy of a charge, and of a dipole, in an external field

$$U = qV(\vec r) \qquad U_{\text{dipole}} = -\vec p\cdot\vec E \qquad 1\ \text{eV} = 1.6\times10^{-19}\ \text{J}$$
          $$U_{\text{two charges in a field}} = q_1V(\vec r_1) + q_2V(\vec r_2) + \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{12}}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $V(\vec r)$ | potential of the external field at that point | V |
| $U$ | potential energy | J or eV |

**Use it when:**

> Charges are placed in a field produced by something else. The last term is the charges' mutual energy — easy to forget.

**Trap:**

> An electron-volt is an energy, not a voltage: the energy one elementary charge gains falling through 1 V.

### ● `P2.8` Capacitance, defined

$$C = \frac{Q}{V} \qquad C_{\text{isolated sphere}} = 4\pi\varepsilon_0 R$$

| Symbol | Meaning | Unit |
|---|---|---|
| $C$ | capacitance | F (farad) |
| $Q$ | charge on either plate | C |
| $V$ | potential difference across it | V |

**Use it when:**

> Any capacitor question. $C$ depends only on geometry and the dielectric — never on $Q$ or $V$.

**Trap:**

> The farad is enormous; real capacitors are μF, nF or pF. $Q$ is the charge on **one** plate, the two being equal and opposite.

### ● `P2.9` Parallel plate capacitor, with and without a dielectric

$$C = \frac{\varepsilon_0 A}{d} \qquad C_{\text{with dielectric}} = \frac{K\varepsilon_0 A}{d}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $A$ | area of one plate | m² |
| $d$ | plate separation | m |
| $K$ | dielectric constant | dimensionless |

**Use it when:**

> The standard capacitor. Inserting a dielectric multiplies $C$ by $K$.

**Trap:**

> What stays fixed depends on the circuit. **Battery connected** → $V$ fixed, so $Q$ rises. **Battery disconnected** → $Q$ fixed, so $V$ falls. Almost every dielectric question turns on this distinction.

### ○ `P2.10` A dielectric slab only partly filling the gap

$$C = \frac{\varepsilon_0 A}{d - t + \dfrac{t}{K}} \qquad \text{several slabs: } C = \frac{\varepsilon_0 A}{\dfrac{t_1}{K_1}+\dfrac{t_2}{K_2}+\cdots}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $t$ | thickness of the slab | m |
| $d$ | plate separation | m |
| $K$ | dielectric constant of the slab | dimensionless |

**Use it when:**

> A slab thinner than the gap is slid in. Setting $t = d$ recovers $K\varepsilon_0A/d$; setting $K=1$ recovers $\varepsilon_0A/d$ — use those two checks.

**Trap:**

> The result does not depend on **where** in the gap the slab sits.

### ○ `P2.11` Spherical and cylindrical capacitors

$$C_{\text{spherical}} = \frac{4\pi\varepsilon_0\,r_1r_2}{r_2-r_1} \qquad C_{\text{cylindrical}} = \frac{2\pi\varepsilon_0 L}{\ln(b/a)}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $r_1, r_2$ | inner and outer radii | m |
| $a, b$ | inner and outer cylinder radii | m |
| $L$ | length of the cylinder | m |

**Use it when:**

> Concentric shells or coaxial cylinders. Both are derived by integrating $E$ between the conductors to get $V$, then $C = Q/V$.

**Trap:**

> Here $L$ is a **length**. In Chapter 6 the same letter is self-inductance — check which chapter the question is in.

### ● `P2.12` Capacitors in series and in parallel

$$\text{series: } \frac{1}{C_s} = \frac{1}{C_1}+\frac{1}{C_2}+\cdots \qquad \text{parallel: } C_p = C_1+C_2+\cdots$$

| Symbol | Meaning | Unit |
|---|---|---|
| series | same **charge**, voltages add | F |
| parallel | same **voltage**, charges add | F |

**Use it when:**

> A network of capacitors. Reduce it stepwise.

**Trap:**

> The rules are the **opposite way round** from resistors. Series capacitance is always smaller than the smallest one in the chain.

### ● `P2.13` Energy stored in a capacitor, and energy density

$$U = \frac{1}{2}CV^2 = \frac{1}{2}QV = \frac{Q^2}{2C} \qquad u = \frac{1}{2}\varepsilon_0E^2$$

| Symbol | Meaning | Unit |
|---|---|---|
| $U$ | energy stored | J |
| $u$ | energy per unit volume of field | J m⁻³ |
| $E$ | field between the plates | V m⁻¹ |

**Use it when:**

> Energy, or work done in charging. Pick whichever of the three forms matches what the question gives you.

**Trap:**

> The factor of $\tfrac12$ is because $V$ rises from 0 to its final value as charge accumulates — the work is not simply $QV$.

### ○ `P2.14` Two charged capacitors joined together

$$V_{\text{common}} = \frac{C_1V_1 + C_2V_2}{C_1+C_2} \qquad \Delta U = \frac{C_1C_2\left(V_1-V_2\right)^2}{2\left(C_1+C_2\right)}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $V_{\text{common}}$ | shared potential after connecting | V |
| $\Delta U$ | energy **lost** in the process | J |

**Use it when:**

> Two charged capacitors are connected plate to plate. Charge is conserved; energy is not.

**Trap:**

> Energy is **always lost** (the expression is a square), dissipated as heat and radiation in the connecting wires — even ideal ones. Being asked to explain that loss is common.

## `CH 3` Current Electricity — *14 entries*

Recognise strip

- `P3.1` Current, and current density

- `P3.2` Drift velocity, and the current it produces

- `P3.3` Mobility

- `P3.4` Ohm's law, and resistance from dimensions

- `P3.5` Resistivity from what the electrons are doing

- `P3.6` Conductivity, and Ohm's law in microscopic form

- `P3.7` Resistance changing with temperature

- `P3.8` Resistors in series and parallel

- `P3.9` Emf, terminal voltage and internal resistance

- `P3.10` Cells combined in series and in parallel

- `P3.11` Electrical power and energy

- `P3.12` Kirchhoff's two rules

- `P3.13` Wheatstone bridge, and the metre bridge

- `P3.14` Potentiometer — comparing emfs and finding internal resistance

### ● `P3.1` Current, and current density

$$I = \frac{Q}{t} = \frac{dQ}{dt} \qquad \vec J = \frac{I}{A}\hat n, \qquad I = \int_A \vec J\cdot d\vec A$$

| Symbol | Meaning | Unit |
|---|---|---|
| $I$ | current — a **scalar** | A |
| $\vec J$ | current density — a **vector** | A m⁻² |
| $A$ | cross-sectional area | m² |

**Use it when:**

> Charge flow. $1\ \text{A}$ is one coulomb per second.

**Trap:**

> Current is drawn with an arrow but is **not a vector** — it does not obey vector addition. Bending a wire does not change the current through it. Current density is the vector.

### ● `P3.2` Drift velocity, and the current it produces

$$\vec v_d = -\frac{e\vec E}{m}\tau \qquad I = neAv_d$$

| Symbol | Meaning | Unit |
|---|---|---|
| $v_d$ | drift velocity | m s⁻¹ |
| $n$ | free electron number density | m⁻³ |
| $\tau$ | relaxation time between collisions | s |
| $e$ | electronic charge | 1.6 × 10⁻¹⁹ C |

**Use it when:**

> Linking the microscopic picture to the measured current.

**Trap:**

> Drift velocity is tiny — around $10^{-4}\ \text{m s}^{-1}$ — while random thermal speed is about $10^{5}\ \text{m s}^{-1}$. The lamp lights instantly because the **field** propagates at nearly $c$, not the electrons.

### ○ `P3.3` Mobility

$$\mu = \frac{v_d}{E} = \frac{e\tau}{m}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\mu$ | mobility | m² V⁻¹ s⁻¹ |
| $m$ | mass of the charge carrier | kg |
| $\tau$ | relaxation time | s |

**Use it when:**

> Drift speed per unit field is asked, or comparing carriers in a semiconductor.

**Trap:**

> Defined as a positive magnitude even for electrons, which drift opposite to $\vec E$.

### ● `P3.4` Ohm's law, and resistance from dimensions

$$V = IR \qquad R = \frac{\rho l}{A}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $R$ | resistance | Ω |
| $\rho$ | resistivity — a material property | Ω m |
| $l$ | length of the conductor | m |
| $A$ | cross-sectional area | m² |

**Use it when:**

> Almost every circuit question. Stretching a wire keeps its **volume** constant, so doubling the length quarters the area and quadruples $R$.

**Trap:**

> $R$ depends on the specimen's shape; $\rho$ does not. Ohm's law holds only for ohmic conductors at constant temperature.

### ● `P3.5` Resistivity from what the electrons are doing

$$\rho = \frac{m}{ne^2\tau}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\rho$ | resistivity | Ω m |
| $n$ | free electron density | m⁻³ |
| $\tau$ | relaxation time | s |
| $m$ | electron mass | 9.1 × 10⁻³¹ kg |

**Use it when:**

> Explaining *why* resistance changes — the standard 3-mark derivation, and the basis of every temperature-dependence answer.

**Trap:**

> Heating a **metal** shortens $\tau$, so $\rho$ rises. Heating a **semiconductor** raises $n$ far more than it cuts $\tau$, so $\rho$ falls. Same formula, opposite behaviour.

### ○ `P3.6` Conductivity, and Ohm's law in microscopic form

$$\sigma = \frac{1}{\rho} = \frac{ne^2\tau}{m} \qquad \vec J = \sigma\vec E$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\sigma$ | conductivity | S m⁻¹ |
| $\vec J$ | current density | A m⁻² |
| $\vec E$ | field inside the conductor | V m⁻¹ |

**Use it when:**

> Asked for Ohm's law in vector form, or to relate $J$ and $E$ without mentioning a circuit.

**Trap:**

> This $\sigma$ is conductivity. In Chapter 1 the same letter is surface charge density.

### ● `P3.7` Resistance changing with temperature

$$R_t = R_0\left(1 + \alpha\,\Delta T\right) \qquad \alpha = \frac{R_t - R_0}{R_0\,\Delta T}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\alpha$ | temperature coefficient of resistance | K⁻¹ or °C⁻¹ |
| $R_0$ | resistance at the reference temperature | Ω |
| $\Delta T$ | temperature rise | K |

**Use it when:**

> A resistance is quoted at two temperatures.

**Trap:**

> $\alpha$ is **positive** for metals, **negative** for semiconductors and insulators, and nearly zero for alloys like nichrome and manganin — which is exactly why they are used for standard resistors.

### ● `P3.8` Resistors in series and parallel

$$R_s = R_1+R_2+\cdots \qquad \frac{1}{R_p} = \frac{1}{R_1}+\frac{1}{R_2}+\cdots$$

| Symbol | Meaning | Unit |
|---|---|---|
| series | same **current**, voltages add | Ω |
| parallel | same **voltage**, currents add | Ω |

**Use it when:**

> Reducing any network. Two in parallel: $R_p = R_1R_2/(R_1+R_2)$.

**Trap:**

> The opposite of the capacitor rules. Parallel resistance is always **less** than the smallest resistor present.

### ● `P3.9` Emf, terminal voltage and internal resistance

$$\mathcal{E} = V + Ir \qquad V = \mathcal{E} - Ir \qquad I = \frac{\mathcal{E}}{R+r}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\mathcal{E}$ | emf of the cell | V |
| $V$ | terminal potential difference | V |
| $r$ | internal resistance | Ω |

**Use it when:**

> A real cell is driving a circuit.

**Trap:**

> $V \lt \mathcal{E}$ while discharging, $V = \mathcal{E}$ only in open circuit, and $V \gt \mathcal{E}$ while the cell is being **charged** (current reversed).

### ○ `P3.10` Cells combined in series and in parallel

$$\text{series: } I = \frac{N\mathcal{E}}{R+Nr} \qquad \text{parallel: } I = \frac{\mathcal{E}}{R + r/N}$$
          $$\text{two unequal cells: } \mathcal{E}_{eq} = \frac{\mathcal{E}_1r_2 + \mathcal{E}_2r_1}{r_1+r_2}, \qquad r_{eq} = \frac{r_1r_2}{r_1+r_2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $N$ | number of identical cells | dimensionless |
| $\mathcal{E}_{eq}$ | equivalent emf | V |
| $r_{eq}$ | equivalent internal resistance | Ω |

**Use it when:**

> A battery of cells. Series wins when $R \gg r$; parallel wins when $R \ll r$.

**Trap:**

> In series the internal resistances add too — which is why stacking cells does not raise the current indefinitely.

### ● `P3.11` Electrical power and energy

$$P = VI = I^2R = \frac{V^2}{R} \qquad W = VIt \qquad 1\ \text{kWh} = 3.6\times10^{6}\ \text{J}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $P$ | power dissipated | W |
| $W$ | energy consumed | J or kWh |
| $t$ | time | s |

**Use it when:**

> Heating, power ratings, or an electricity bill.

**Trap:**

> Choose the right form. In **series** the current is shared so $P = I^2R$ applies and the largest resistor dissipates most; in **parallel** the voltage is shared so $P = V^2/R$ applies and the *smallest* resistor dissipates most.

### ● `P3.12` Kirchhoff's two rules

$$\text{junction: } \sum I = 0 \qquad \text{loop: } \sum \Delta V = 0$$

| Symbol | Meaning | Unit |
|---|---|---|
| junction rule | conservation of **charge** | A |
| loop rule | conservation of **energy** | V |

**Use it when:**

> A network that series and parallel reduction cannot simplify. Naming which conservation law each rule expresses is usually worth a mark on its own.

**Trap:**

> Fix a sign convention before you start and keep it. Going through a resistor along the current gives $-IR$; entering a cell at its negative terminal gives $+\mathcal{E}$.

### ● `P3.13` Wheatstone bridge, and the metre bridge

$$\frac{R_1}{R_2} = \frac{R_3}{R_4} \qquad \text{metre bridge: } X = \frac{R\,(100-l)}{l}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $X$ | unknown resistance | Ω |
| $R$ | known resistance in the other gap | Ω |
| $l$ | balancing length from the left end | cm |

**Use it when:**

> A galvanometer reads zero — the balance condition. At balance, no current flows through the galvanometer arm, so it can be removed entirely.

**Trap:**

> The bridge is most sensitive when all four resistances are comparable, which is why the balance point should sit near the middle of the wire.

### ● `P3.14` Potentiometer — comparing emfs and finding internal resistance

$$V = Kl, \quad K = \frac{V}{L} \qquad \frac{\mathcal{E}_1}{\mathcal{E}_2} = \frac{l_1}{l_2} \qquad r = R\left(\frac{l_1 - l_2}{l_2}\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $K$ | potential gradient along the wire | V m⁻¹ or V cm⁻¹ |
| $l_1$ | balancing length with the cell open | cm |
| $l_2$ | balancing length with $R$ across the cell | cm |

**Use it when:**

> Comparing two emfs, or measuring internal resistance.

**Trap:**

> A potentiometer beats a voltmeter because at balance it draws **no current** from the cell, so it measures true emf rather than terminal voltage. Sensitivity improves with a **longer** wire — a smaller potential gradient.

## `CH 4` Moving Charges and Magnetism — *12 entries*

Recognise strip

- `P4.1` Biot–Savart law

- `P4.2` Field at the centre of a circular loop

- `P4.3` Field on the axis of a circular loop

- `P4.4` Ampère's circuital law

- `P4.5` Field of a long straight wire

- `P4.6` Field inside a solenoid and a toroid

- `P4.7` Force on a moving charge, and the Lorentz force

- `P4.8` Radius and period of a charged particle's circular path

- `P4.9` Force on a current-carrying conductor

- `P4.10` Force between two parallel currents, and the ampere

- `P4.11` Torque on a current loop, and magnetic moment

- `P4.12` Galvanometer, and converting it to an ammeter or voltmeter

### ● `P4.1` Biot–Savart law

$$dB = \frac{\mu_0}{4\pi}\frac{I\,dl\sin\theta}{r^2} \qquad d\vec B = \frac{\mu_0}{4\pi}\frac{I\,d\vec l\times\hat r}{r^2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $dB$ | field from one current element | T |
| $\mu_0$ | permeability of free space | 4π × 10⁻⁷ T m A⁻¹ |
| $dl$ | length of the current element | m |
| $\theta$ | angle between $d\vec l$ and $\hat r$ | rad or ° |

**Use it when:**

> Deriving the field of any current shape. The magnetic analogue of Coulomb's law.

**Trap:**

> $dB = 0$ straight ahead of the element ($\theta = 0$) and maximum sideways ($\theta = 90°$) — unlike the electric field, which is maximum along the line.

### ● `P4.2` Field at the centre of a circular loop

$$B = \frac{\mu_0 I}{2R} \qquad \text{for } N \text{ turns: } B = \frac{\mu_0 NI}{2R}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $B$ | magnetic field at the centre | T |
| $R$ | radius of the loop | m |
| $N$ | number of turns | dimensionless |

**Use it when:**

> A circular coil and the field at its centre. For an arc subtending angle $\phi$ radians, multiply by $\phi/2\pi$.

**Trap:**

> Only for the **centre**. Off-axis needs P4.3, and $R$ is the radius, not the diameter.

### ○ `P4.3` Field on the axis of a circular loop

$$B = \frac{\mu_0 I R^2}{2\left(R^2+x^2\right)^{3/2}} \qquad \text{for } N \text{ turns, multiply by } N$$

| Symbol | Meaning | Unit |
|---|---|---|
| $x$ | distance along the axis from the centre | m |
| $R$ | loop radius | m |

**Use it when:**

> The point is on the axis but not at the centre. Setting $x=0$ recovers P4.2 — use that as your check.

**Trap:**

> Far away ($x \gg R$) this becomes $\mu_0 \cdot 2M/4\pi x^3$ with $M = NIA$ — the loop behaves as a magnetic dipole.

### ● `P4.4` Ampère's circuital law

$$\oint \vec B\cdot d\vec l = \mu_0 I_{\text{enclosed}}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $I_{\text{enc}}$ | current threading the closed loop | A |
| $d\vec l$ | element of the Amperian loop | m |

**Use it when:**

> Symmetry lets you choose a loop on which $B$ is constant — the magnetic counterpart of Gauss's law.

**Trap:**

> Only **enclosed** current counts, and only the component of $\vec B$ along the path contributes. In Chapter 8 this law gains a second term.

### ● `P4.5` Field of a long straight wire

$$B = \frac{\mu_0 I}{2\pi r} \qquad \text{finite wire: } B = \frac{\mu_0 I}{4\pi r}\left(\sin\alpha_1 + \sin\alpha_2\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $r$ | perpendicular distance from the wire | m |
| $\alpha_1,\alpha_2$ | angles subtended by the wire's two ends | rad or ° |

**Use it when:**

> A straight current-carrying wire. Field lines are concentric circles; direction by the right-hand thumb rule.

**Trap:**

> $1/r$, not $1/r^2$. The infinite-wire form is the finite one with both angles at $90°$.

### ● `P4.6` Field inside a solenoid and a toroid

$$B_{\text{solenoid}} = \mu_0 n I \qquad B_{\text{toroid}} = \mu_0 n I, \quad n = \frac{N}{2\pi r}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $n$ | turns per unit length | m⁻¹ |
| $N$ | total number of turns | dimensionless |
| $r$ | mean radius of the toroid | m |

**Use it when:**

> A long solenoid or a toroid. The field is uniform inside and essentially zero outside.

**Trap:**

> $n$ is turns per **metre**, not the total. At the **end** of a solenoid the field is half the interior value.

### ● `P4.7` Force on a moving charge, and the Lorentz force

$$\vec F = q\left(\vec v\times\vec B\right) \qquad \vec F = q\vec E + q\left(\vec v\times\vec B\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\vec F$ | force on the charge | N |
| $\vec v$ | velocity | m s⁻¹ |
| $\vec B$ | magnetic field | T |

**Use it when:**

> A charge moves through a magnetic field. In a velocity selector the two forces balance, giving $v = E/B$.

**Trap:**

> The magnetic force is always perpendicular to $\vec v$, so it **does no work** and cannot change the particle's speed — only its direction. A charge at rest, or moving parallel to $\vec B$, feels no magnetic force at all.

### ● `P4.8` Radius and period of a charged particle's circular path

$$r = \frac{mv}{qB} \qquad T = \frac{2\pi m}{qB} \qquad \omega = \frac{qB}{m}$$
          $$\text{pitch of the helix } p = v\cos\theta \cdot \frac{2\pi m}{qB}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $r$ | radius of the circular path | m |
| $T$ | period of revolution | s |
| $\omega$ | cyclotron angular frequency | rad s⁻¹ |

**Use it when:**

> A charge enters a field perpendicular to it. If it enters at an angle, the path is a helix and the pitch formula applies.

**Trap:**

> $T$ and $\omega$ are **independent of speed and radius** — that is the whole principle of the cyclotron.

### ● `P4.9` Force on a current-carrying conductor

$$\vec F = I\left(\vec L\times\vec B\right), \qquad F = BIL\sin\theta$$

| Symbol | Meaning | Unit |
|---|---|---|
| $L$ | length of conductor in the field | m |
| $I$ | current | A |
| $\theta$ | angle between the conductor and $\vec B$ | rad or ° |

**Use it when:**

> A wire in a magnetic field. Direction by Fleming's left-hand rule.

**Trap:**

> Zero when the wire is **parallel** to the field, maximum when perpendicular. This is the same force as P4.7 summed over all the drifting charges.

### ● `P4.10` Force between two parallel currents, and the ampere

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi r} \qquad \text{for } I_1=I_2=1\ \text{A},\ r=1\ \text{m}: \frac{F}{L} = 2\times10^{-7}\ \text{N m}^{-1}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $F/L$ | force per unit length | N m⁻¹ |
| $r$ | separation of the wires | m |

**Use it when:**

> Two parallel wires. This relation is the **definition of the ampere** — quoting the $2\times10^{-7}$ case is the answer to "define the ampere".

**Trap:**

> Currents in the **same** direction **attract**; opposite directions repel. That is the reverse of what charges do, and it is asked.

### ● `P4.11` Torque on a current loop, and magnetic moment

$$\vec\tau = \vec M\times\vec B, \qquad \tau = NIAB\sin\theta \qquad M = NIA$$

| Symbol | Meaning | Unit |
|---|---|---|
| $M$ | magnetic dipole moment | A m² |
| $A$ | area of the loop | m² |
| $N$ | number of turns | dimensionless |
| $\theta$ | angle between $\vec M$ and $\vec B$ | rad or ° |

**Use it when:**

> A coil in a magnetic field — the working principle of the motor and the galvanometer.

**Trap:**

> Torque is maximum when the coil's **plane** is parallel to $\vec B$ (so $\vec M$ is perpendicular to it), and zero when the plane is perpendicular. Net force is zero in a uniform field.

### ● `P4.12` Galvanometer, and converting it to an ammeter or voltmeter

$$I = \frac{NBA}{k}\phi \qquad \text{shunt: } S = \frac{I_g G}{I - I_g} \qquad \text{series: } R = \frac{V}{I_g} - G$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\phi$ | deflection | rad or div |
| $k$ | torsional constant of the suspension | N m rad⁻¹ |
| $G$ | galvanometer resistance | Ω |
| $I_g$ | current for full-scale deflection | A |

**Use it when:**

> Sensitivity, or converting the meter. **Current sensitivity** is $NBA/k$; **voltage sensitivity** is $NBA/kG$.

**Trap:**

> Raising current sensitivity does **not** automatically raise voltage sensitivity — adding turns raises $N$ but also raises $G$. An ammeter needs a **small** shunt in parallel; a voltmeter needs a **large** resistance in series.

## `CH 5` Magnetism and Matter — *9 entries*

Recognise strip

- `P5.1` Gauss's law for magnetism

- `P5.2` Magnetic moment of a bar magnet and of a coil

- `P5.3` Field of a bar magnet, axial and equatorial

- `P5.4` Torque, energy and work for a magnetic dipole

- `P5.5` A magnet oscillating in a field

- `P5.6` Earth's magnetic field and the angle of dip

- `P5.7` Magnetisation, magnetising field and susceptibility

- `P5.8` Permeability and its relation to susceptibility

- `P5.9` Curie's law, and the three kinds of magnetic material

### ● `P5.1` Gauss's law for magnetism

$$\oint_S \vec B\cdot d\vec S = 0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\vec B$ | magnetic field | T |
| $d\vec S$ | element of any closed surface | m² |

**Use it when:**

> Asked why magnetic monopoles do not exist, or to contrast with the electric Gauss's law.

**Trap:**

> Always exactly zero, because magnetic field lines are **closed loops** — every line entering a surface leaves it. Cutting a magnet in half gives two magnets, never an isolated pole.

### ● `P5.2` Magnetic moment of a bar magnet and of a coil

$$M = m \times 2l \qquad M = NIA$$

| Symbol | Meaning | Unit |
|---|---|---|
| $M$ | magnetic dipole moment | A m² or J T⁻¹ |
| $m$ | pole strength | A m |
| $2l$ | magnetic length | m |
| $N, I, A$ | turns, current, area of a coil | —, A, m² |

**Use it when:**

> Any dipole calculation. A current loop and a bar magnet are interchangeable once you know $M$.

**Trap:**

> Magnetic length is about $\tfrac{5}{6}$ of the geometric length of a bar magnet. Direction runs **S to N** inside the magnet.

### ● `P5.3` Field of a bar magnet, axial and equatorial

$$B_{\text{axial}} = \frac{\mu_0}{4\pi}\frac{2M}{r^3} \qquad B_{\text{equatorial}} = \frac{\mu_0}{4\pi}\frac{M}{r^3}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $B$ | field at distance $r$ | T |
| $M$ | magnetic moment | A m² |
| $r$ | distance from the centre, $r \gg l$ | m |

**Use it when:**

> A short bar magnet, far from it. Identical in form to the electric dipole (P1.8, P1.9) with $\mu_0/4\pi$ replacing $1/4\pi\varepsilon_0$.

**Trap:**

> Axial is **twice** equatorial, and the two point in opposite senses. The same factor of 2 as in electrostatics.

### ● `P5.4` Torque, energy and work for a magnetic dipole

$$\vec\tau = \vec M\times\vec B, \quad \tau = MB\sin\theta \qquad U = -\vec M\cdot\vec B$$
          $$W = MB\left(\cos\theta_1 - \cos\theta_2\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\tau$ | torque on the magnet | N m |
| $U$ | potential energy | J |
| $W$ | work to turn from $\theta_1$ to $\theta_2$ | J |

**Use it when:**

> A magnet is rotated in a field. Turning from aligned to fully reversed costs $W = 2MB$.

**Trap:**

> Structurally identical to the electric dipole (P1.10). $\theta = 0$ stable, $\theta = 180°$ unstable.

### ○ `P5.5` A magnet oscillating in a field

$$T = 2\pi\sqrt{\frac{I}{MB}} \qquad B = \frac{4\pi^2 I}{MT^2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $T$ | period of oscillation | s |
| $I$ | moment of **inertia**, not current | kg m² |
| $M$ | magnetic moment | A m² |

**Use it when:**

> A magnet is displaced slightly and released — a vibration magnetometer. Small angles only, so that $\sin\theta \approx \theta$.

**Trap:**

> $I$ here is moment of inertia. For a bar of mass $m$ and length $L$ about its centre, $I = mL^2/12$.

### ○ `P5.6` Earth's magnetic field and the angle of dip

$$B_H = B\cos\delta, \quad B_V = B\sin\delta \qquad \tan\delta = \frac{B_V}{B_H}, \quad B = \sqrt{B_H^2+B_V^2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $B_H$ | horizontal component | T |
| $B_V$ | vertical component | T |
| $\delta$ | angle of dip (inclination) | ° |

**Use it when:**

> Earth's field is resolved. The three elements are declination, dip and horizontal component.

**Trap:**

> $\delta = 0$ at the magnetic equator and $90°$ at the poles. At the equator the field is entirely horizontal, so a dip needle rests flat.

### ○ `P5.7` Magnetisation, magnetising field and susceptibility

$$I = \frac{M}{V} \qquad \chi_m = \frac{I}{H} \qquad B = \mu_0\left(H + I\right) = \mu_0 H\left(1+\chi_m\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $I$ | intensity of magnetisation | A m⁻¹ |
| $H$ | magnetising field intensity | A m⁻¹ |
| $\chi_m$ | magnetic susceptibility | dimensionless |

**Use it when:**

> A material is placed in a field. $\chi_m$ is small and negative for diamagnetics, small and positive for paramagnetics, and very large for ferromagnetics.

**Trap:**

> This $I$ is magnetisation — the third meaning of the letter in this chapter, after current and moment of inertia. $H$ and $I$ share a unit; $B$ does not.

### ○ `P5.8` Permeability and its relation to susceptibility

$$\mu = \mu_0\left(1+\chi_m\right) \qquad \mu_r = \frac{\mu}{\mu_0} = 1+\chi_m$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\mu$ | absolute permeability | T m A⁻¹ |
| $\mu_r$ | relative permeability | dimensionless |
| $\mu_0$ | permeability of free space | 4π × 10⁻⁷ T m A⁻¹ |

**Use it when:**

> Converting between susceptibility and permeability. $\mu_r \lt 1$ diamagnetic, slightly $\gt 1$ paramagnetic, $\gg 1$ ferromagnetic.

**Trap:**

> $\chi_m$ is dimensionless but $\mu$ is not — and $\mu_r$ is the one that has no unit.

### ● `P5.9` Curie's law, and the three kinds of magnetic material

$$\chi_m = \frac{C}{T} \qquad \text{(paramagnetic; ferromagnetic above } T_C: \chi_m = \frac{C}{T-T_C})$$

| Symbol | Meaning | Unit |
|---|---|---|
| $C$ | Curie constant | K |
| $T$ | absolute temperature | K |
| $T_C$ | Curie temperature | K |

**Use it when:**

> Susceptibility against temperature. Heating randomises the aligned dipoles, so $\chi_m$ falls.

**Trap:**

> Above $T_C$ a ferromagnet becomes **paramagnetic**, not diamagnetic. Diamagnetism alone is **temperature-independent** — Curie's law does not apply to it.

## `CH 6` Electromagnetic Induction — *9 entries*

Recognise strip

- `P6.1` Magnetic flux

- `P6.2` Faraday's law and Lenz's law

- `P6.3` Motional emf from a rod moving in a field

- `P6.4` A rod rotating about one end

- `P6.5` Charge that flows during a flux change

- `P6.6` Self-inductance, and that of a solenoid

- `P6.7` Mutual inductance of two coaxial solenoids

- `P6.8` Energy stored in an inductor, and magnetic energy density

- `P6.9` The AC generator

### ● `P6.1` Magnetic flux

$$\Phi_B = \vec B\cdot\vec A = BA\cos\theta$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Phi_B$ | magnetic flux | Wb (weber) |
| $A$ | area of the loop | m² |
| $\theta$ | angle between $\vec B$ and the area **normal** | rad or ° |

**Use it when:**

> Anything about induction — flux is the quantity whose change drives everything in this chapter.

**Trap:**

> $\theta$ is measured from the **normal** to the plane, not from the plane itself. A coil lying flat in a vertical field has $\theta = 0$ and maximum flux, not zero.

### ● `P6.2` Faraday's law and Lenz's law

$$\varepsilon = -N\frac{d\Phi_B}{dt} \qquad I = \frac{\varepsilon}{R} = -\frac{N}{R}\frac{d\Phi_B}{dt}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\varepsilon$ | induced emf | V |
| $N$ | number of turns | dimensionless |
| $d\Phi_B/dt$ | rate of change of flux | Wb s⁻¹ |

**Use it when:**

> Flux changes for any reason — $B$ changing, $A$ changing, or the coil rotating.

**Trap:**

> The minus sign **is** Lenz's law: the induced current opposes the change that produced it. It is a consequence of **conservation of energy** — that is the answer when asked to justify it.

### ● `P6.3` Motional emf from a rod moving in a field

$$\varepsilon = Blv \qquad I = \frac{Blv}{R}, \quad F = \frac{B^2l^2v}{R}, \quad P = \frac{B^2l^2v^2}{R}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $l$ | length of the rod in the field | m |
| $v$ | speed of the rod | m s⁻¹ |
| $F$ | opposing force needed to keep it moving | N |

**Use it when:**

> A conductor slides on rails. $B$, $l$ and $v$ must be mutually perpendicular.

**Trap:**

> Power applied equals power dissipated — the mechanical work done against the opposing force **is** the electrical energy produced. That equality is a favourite question.

### ○ `P6.4` A rod rotating about one end

$$\varepsilon = \frac{1}{2}B\omega l^2$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\omega$ | angular velocity | rad s⁻¹ |
| $l$ | length of the rod | m |
| $\varepsilon$ | emf between centre and rim | V |

**Use it when:**

> A rod or disc spins in a perpendicular field.

**Trap:**

> The $\tfrac12$ comes from the average speed along the rod — the far end moves fastest, the pivot not at all. $\omega = 2\pi f$, so a rod at 50 rev/s has $\omega = 100\pi$.

### ○ `P6.5` Charge that flows during a flux change

$$q = \frac{N\,\Delta\Phi_B}{R}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $q$ | total charge circulated | C |
| $\Delta\Phi_B$ | total change in flux | Wb |
| $R$ | total circuit resistance | Ω |

**Use it when:**

> Asked for charge rather than current — a magnet dropped through a coil, or a coil flipped over.

**Trap:**

> Independent of **how fast** the change happens. Flipping a coil through $180°$ changes flux by $2BA$, not $BA$.

### ● `P6.6` Self-inductance, and that of a solenoid

$$N\Phi = LI \qquad \varepsilon = -L\frac{dI}{dt} \qquad L = \mu_0 n^2 A l = \frac{\mu_0 N^2 A}{l}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $L$ | self-inductance | H (henry) |
| $l$ | length of the solenoid | m |
| $n$ | turns per unit length, $N/l$ | m⁻¹ |
| $A$ | cross-sectional area | m² |

**Use it when:**

> A coil opposes a change in its own current — electrical inertia. A core of relative permeability $\mu_r$ multiplies $L$ by $\mu_r$.

**Trap:**

> Here $l$ is **length** and $L$ is **inductance** — the two are easy to collide. $L$ goes as $N^2$, so doubling the turns quadruples the inductance.

### ○ `P6.7` Mutual inductance of two coaxial solenoids

$$\varepsilon_2 = -M\frac{dI_1}{dt} \qquad M = \frac{\mu_0 N_1 N_2 A}{l} \qquad M_{12} = M_{21}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $M$ | mutual inductance | H |
| $N_1, N_2$ | turns on each solenoid | dimensionless |
| $A$ | area of the **inner** solenoid | m² |

**Use it when:**

> Two coupled coils — the basis of the transformer.

**Trap:**

> Use the area of the **inner** coil, since that is all the flux the outer one links. $M_{12} = M_{21}$ always, however different the two coils are.

### ● `P6.8` Energy stored in an inductor, and magnetic energy density

$$U = \frac{1}{2}LI^2 \qquad u = \frac{B^2}{2\mu_0}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $U$ | energy stored in the magnetic field | J |
| $u$ | energy per unit volume | J m⁻³ |
| $B$ | field inside the inductor | T |

**Use it when:**

> Energy in a coil. Exactly parallel to the capacitor: $\tfrac12 CV^2 \leftrightarrow \tfrac12 LI^2$, and $\tfrac12\varepsilon_0E^2 \leftrightarrow B^2/2\mu_0$.

**Trap:**

> Note $\mu_0$ is in the **denominator** for magnetic energy density, where $\varepsilon_0$ is in the numerator for electric.

### ● `P6.9` The AC generator

$$\varepsilon = NAB\omega\sin(\omega t) = \varepsilon_0\sin(\omega t), \qquad \varepsilon_0 = NAB\omega$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\varepsilon_0$ | peak emf | V |
| $\omega$ | angular frequency of rotation, $2\pi f$ | rad s⁻¹ |
| $N, A, B$ | turns, coil area, field | —, m², T |

**Use it when:**

> A coil rotates in a uniform field. Converts mechanical energy into electrical.

**Trap:**

> Emf is **maximum** when the coil's plane is *parallel* to $\vec B$ (flux momentarily zero but changing fastest), and zero when the plane is perpendicular. The intuition runs backwards from most students' first guess.

## `CH 7` Alternating Current — *11 entries*

Recognise strip

- `P7.1` RMS and mean values of an alternating quantity

- `P7.2` AC through a pure resistor

- `P7.3` AC through a pure inductor

- `P7.4` AC through a pure capacitor

- `P7.5` Series LCR — impedance and phase angle

- `P7.6` Resonance in a series LCR circuit

- `P7.7` Sharpness of resonance — the Q factor

- `P7.8` Average power, power factor and wattless current

- `P7.9` LC oscillations

- `P7.10` The transformer

- `P7.11` Why transformers lose energy

### ● `P7.1` RMS and mean values of an alternating quantity

$$I_{\text{rms}} = \frac{i_0}{\sqrt2} \approx 0.707\,i_0 \qquad I_{\text{mean}} = \frac{2i_0}{\pi} \approx 0.637\,i_0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $i_0$ | peak current | A |
| $I_{\text{rms}}$ | root-mean-square (virtual) current | A |
| $I_{\text{mean}}$ | mean over a **half** cycle | A |

**Use it when:**

> Converting between peak and stated values. Mains "220 V" is the rms value, so the peak is about 311 V.

**Trap:**

> The mean over a **full** cycle is **zero** — which is exactly why rms exists. Every ammeter and voltmeter reads rms.

### ● `P7.2` AC through a pure resistor

$$i = i_0\sin\omega t, \qquad i_0 = \frac{e_0}{R}, \qquad \phi = 0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\phi$ | phase difference between $V$ and $I$ | rad |
| $R$ | resistance | Ω |

**Use it when:**

> Only a resistor is present. Current and voltage are **in phase**.

**Trap:**

> Resistance does not depend on frequency, unlike both reactances.

### ● `P7.3` AC through a pure inductor

$$X_L = \omega L = 2\pi f L \qquad i = i_0\sin\left(\omega t - \frac{\pi}{2}\right), \qquad i_0 = \frac{e_0}{X_L}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $X_L$ | inductive reactance | Ω |
| $L$ | inductance | H |
| $f$ | frequency | Hz |

**Use it when:**

> A coil in an AC circuit. Current **lags** voltage by $90°$.

**Trap:**

> $X_L \propto f$, so an inductor blocks high frequencies and passes DC ($f=0$, $X_L=0$) freely. It is a choke.

### ● `P7.4` AC through a pure capacitor

$$X_C = \frac{1}{\omega C} = \frac{1}{2\pi f C} \qquad i = i_0\sin\left(\omega t + \frac{\pi}{2}\right), \qquad i_0 = \frac{e_0}{X_C}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $X_C$ | capacitive reactance | Ω |
| $C$ | capacitance | F |

**Use it when:**

> A capacitor in an AC circuit. Current **leads** voltage by $90°$.

**Trap:**

> $X_C \propto 1/f$, the opposite of the inductor: a capacitor blocks DC completely ($f=0$, $X_C \to \infty$) and passes high frequencies. Remember the order as **CIVIL** — in C, I leads V; V leads I in L.

### ● `P7.5` Series LCR — impedance and phase angle

$$Z = \sqrt{R^2 + \left(X_L - X_C\right)^2} \qquad \tan\phi = \frac{X_L - X_C}{R} \qquad E = IZ$$

| Symbol | Meaning | Unit |
|---|---|---|
| $Z$ | impedance | Ω |
| $\phi$ | phase angle between $E$ and $I$ | rad or ° |
| $X_L, X_C$ | the two reactances | Ω |

**Use it when:**

> R, L and C in series. Found from the phasor diagram, where $V_L$ and $V_C$ are antiparallel so they subtract.

**Trap:**

> $X_L \gt X_C$ → inductive, current lags. $X_L \lt X_C$ → capacitive, current leads. Because $V_L$ and $V_C$ oppose, the voltage across one of them can **exceed the supply voltage** — which is not an error.

### ● `P7.6` Resonance in a series LCR circuit

$$X_L = X_C \;\Rightarrow\; \omega_r = \frac{1}{\sqrt{LC}}, \qquad f_r = \frac{1}{2\pi\sqrt{LC}}$$
          $$\text{at resonance: } Z = R \text{ (minimum)}, \quad I = \frac{E}{R} \text{ (maximum)}, \quad \phi = 0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\omega_r$ | resonant angular frequency | rad s⁻¹ |
| $f_r$ | resonant frequency | Hz |

**Use it when:**

> The circuit is tuned — a radio receiver selecting a station.

**Trap:**

> At resonance the circuit is purely **resistive** and power factor is 1. Resonance only exists in a series circuit if both L and C are present — an RL or RC circuit never resonates.

### ○ `P7.7` Sharpness of resonance — the Q factor

$$Q = \frac{\omega_r L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{\omega_r}{\Delta\omega}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $Q$ | quality factor | dimensionless |
| $\Delta\omega$ | bandwidth | rad s⁻¹ |
| $R$ | resistance in the circuit | Ω |

**Use it when:**

> Asked how sharply the circuit is tuned. High $Q$ means a narrow, selective peak.

**Trap:**

> $Q$ rises as $R$ **falls** — a low-resistance circuit is the sharply tuned one.

### ● `P7.8` Average power, power factor and wattless current

$$P_{\text{avg}} = E_{\text{rms}}I_{\text{rms}}\cos\phi \qquad \text{power factor} = \cos\phi = \frac{R}{Z}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $P_{\text{avg}}$ | average power consumed | W |
| $\cos\phi$ | power factor | dimensionless |
| $Z$ | impedance | Ω |

**Use it when:**

> Power in any AC circuit. Only the resistance dissipates energy.

**Trap:**

> In a **pure** inductor or capacitor $\phi = 90°$, so $\cos\phi = 0$ and the average power is **zero** — the current is called **wattless**. Energy is stored and returned each quarter cycle, never consumed.

### ○ `P7.9` LC oscillations

$$\frac{d^2q}{dt^2} + \frac{q}{LC} = 0 \qquad \omega = \frac{1}{\sqrt{LC}} \qquad U = \frac{q^2}{2C} + \frac{1}{2}Li^2 = \text{constant}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $q$ | charge on the capacitor | C |
| $\omega$ | angular frequency of oscillation | rad s⁻¹ |
| $U$ | total energy, constant if $R=0$ | J |

**Use it when:**

> A charged capacitor is connected across an inductor. Energy sloshes between the electric field of C and the magnetic field of L, exactly like a mass on a spring.

**Trap:**

> Undamped only in the idealised $R = 0$ case. Any real circuit has resistance, so the oscillations decay.

### ● `P7.10` The transformer

$$\frac{\varepsilon_s}{\varepsilon_p} = \frac{N_s}{N_p} = \frac{I_p}{I_s} \qquad \text{ideal: } \varepsilon_p I_p = \varepsilon_s I_s$$

| Symbol | Meaning | Unit |
|---|---|---|
| $N_p, N_s$ | turns on primary and secondary | dimensionless |
| $\varepsilon_p, \varepsilon_s$ | primary and secondary voltages | V |
| $I_p, I_s$ | primary and secondary currents | A |

**Use it when:**

> Voltage is stepped up or down. Step-up means more secondary turns — and correspondingly **less** secondary current.

**Trap:**

> A transformer works on **AC only** — DC produces no changing flux, so no induced emf. It never creates energy: what it gains in voltage it loses in current.

### ○ `P7.11` Why transformers lose energy

$$\eta = \frac{\text{output power}}{\text{input power}} \times 100\%$$

| Symbol | Meaning | Unit |
|---|---|---|
| flux leakage | not all primary flux links the secondary | — |
| copper loss | $I^2R$ heating in the windings | W |
| eddy currents | induced loops in the core — reduced by **laminating** it | W |
| hysteresis | repeated remagnetisation of the core | W |

**Use it when:**

> "State four energy losses in a transformer and how each is minimised" — a standing question with four recallable answers.

**Trap:**

> Each loss has its own remedy: thick copper wire for copper loss, a laminated core for eddy currents, a soft-iron core for hysteresis, and winding one coil over the other for flux leakage.

## `CH 8` Electromagnetic Waves — *5 entries*

Recognise strip

- `P8.1` Displacement current

- `P8.2` Ampère–Maxwell law

- `P8.3` Speed of an electromagnetic wave

- `P8.4` The wave itself — fields, energy and momentum

- `P8.5` The electromagnetic spectrum, in order

### ● `P8.1` Displacement current

$$I_d = \varepsilon_0\frac{d\Phi_E}{dt}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $I_d$ | displacement current | A |
| $\Phi_E$ | electric flux | V m |
| $\varepsilon_0$ | permittivity of free space | 8.854 × 10⁻¹² F m⁻¹ |

**Use it when:**

> A charging capacitor. It exists in the **gap between the plates**, where no charge flows, and is exactly equal to the conduction current in the wires.

**Trap:**

> It is not a flow of charge. Maxwell introduced it to fix an inconsistency in Ampère's law: two surfaces bounded by the same loop gave different answers, one passing through the wire and one through the gap.

### ● `P8.2` Ampère–Maxwell law

$$\oint \vec B\cdot d\vec l = \mu_0\left(I_c + \varepsilon_0\frac{d\Phi_E}{dt}\right) = \mu_0\left(I_c + I_d\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $I_c$ | conduction current | A |
| $I_d$ | displacement current | A |

**Use it when:**

> Asked for the modified Ampère's law or to state Maxwell's equations. This is P4.4 with the new term added.

**Trap:**

> The consequence is the whole chapter: a changing electric field produces a magnetic field, and a changing magnetic field produces an electric field — so the two sustain each other and propagate as a wave.

### ● `P8.3` Speed of an electromagnetic wave

$$c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = 3\times10^{8}\ \text{m s}^{-1} \qquad v = \frac{1}{\sqrt{\mu\varepsilon}} = \frac{c}{n}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $c$ | speed in vacuum | m s⁻¹ |
| $v$ | speed in a medium | m s⁻¹ |
| $n$ | refractive index of the medium | dimensionless |

**Use it when:**

> Asked why light is an electromagnetic wave — Maxwell's predicted speed matched the measured speed of light, which is what identified them.

**Trap:**

> Built from two constants measured in purely electric and magnetic experiments, with no light involved. That is what made the result so striking.

### ● `P8.4` The wave itself — fields, energy and momentum

$$E_y = E_0\sin(\omega t - kx), \quad B_z = B_0\sin(\omega t - kx), \quad k = \frac{2\pi}{\lambda}$$
          $$c = \frac{E_0}{B_0} \qquad p = \frac{U}{c} \qquad u_{\text{avg}} = \frac{1}{2}\varepsilon_0E_0^2 = \frac{B_0^2}{2\mu_0}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $E_0, B_0$ | peak field amplitudes | V m⁻¹, T |
| $k$ | wave number | m⁻¹ |
| $p$ | momentum delivered | kg m s⁻¹ |
| $U$ | energy delivered | J |

**Use it when:**

> Given one field amplitude and asked for the other, or asked about radiation pressure.

**Trap:**

> $\vec E$, $\vec B$ and the direction of propagation are **mutually perpendicular**, in that order, and the two fields are **in phase**. Energy is shared equally between them. For a *totally reflecting* surface the momentum delivered is $2U/c$.

### ● `P8.5` The electromagnetic spectrum, in order

$$c = f\lambda \qquad E = hf$$

| Symbol | Meaning | Unit |
|---|---|---|
| order | radio → microwave → infrared → visible → UV → X-ray → γ-ray | — |
| $\lambda$ | decreases along that order | m |
| $f$, $E$ | increase along that order | Hz, J |
| visible | about 400 nm (violet) to 700 nm (red) | nm |

**Use it when:**

> Ordering by wavelength or frequency, or naming a source and use. Radio from oscillating circuits; microwaves from klystrons, used in radar and ovens; infrared from hot bodies, used in therapy and remote controls; UV from the sun and arcs; X-rays from decelerating electrons; γ-rays from nuclei.

**Trap:**

> All travel at the **same speed** $c$ in vacuum. Only wavelength and frequency differ, and they always move in opposite directions along the list.

## `CH 9` Ray Optics and Optical Instruments — *12 entries*

*Written from NCERT and the published **Ray Optics to 9.4** page. The lecture transcripts for this chapter are not yet processed, so the emphasis here follows the textbook rather than the teacher; it will be revisited once those are in.*

Recognise strip

- `P9.1` Mirror formula and magnification

- `P9.2` Focal length from radius of curvature

- `P9.3` Snell's law and refractive index

- `P9.4` Real depth, apparent depth and the shift

- `P9.5` Critical angle and total internal reflection

- `P9.6` Refraction at a single spherical surface

- `P9.7` Lens maker's formula

- `P9.8` Thin lens formula and magnification

- `P9.9` Power of a lens, and lenses in contact

- `P9.10` Refraction through a prism

- `P9.11` Magnifying power of a simple and compound microscope

- `P9.12` Magnifying power of a telescope

### ● `P9.1` Mirror formula and magnification

$$\frac{1}{v} + \frac{1}{u} = \frac{1}{f} \qquad m = \frac{h'}{h} = -\frac{v}{u} = \frac{f}{f-u} = \frac{f-v}{f}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $u$ | object distance, from the pole | m |
| $v$ | image distance | m |
| $f$ | focal length | m |
| $m$ | linear magnification | dimensionless |

**Use it when:**

> Any spherical mirror. All distances are measured from the **pole** under the New Cartesian convention.

**Trap:**

> Note the **plus** sign between $1/v$ and $1/u$ — the lens formula has a minus. Negative $m$ means real and inverted; concave $f$ is negative, convex $f$ positive.

### ● `P9.2` Focal length from radius of curvature

$$f = \frac{R}{2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $R$ | radius of curvature | m |
| $f$ | focal length | m |

**Use it when:**

> A mirror is described by its radius rather than its focal length.

**Trap:**

> Holds for **small aperture** only, and for mirrors — not for lenses, where the lens maker's formula applies instead.

### ● `P9.3` Snell's law and refractive index

$$\frac{\sin i}{\sin r} = {}_1n_2 = \frac{n_2}{n_1} \quad\Longleftrightarrow\quad n_1\sin i = n_2\sin r$$
          $$n = \frac{c}{v} = \frac{\lambda_{\text{air}}}{\lambda_{\text{medium}}} \qquad {}_1n_2 = \frac{1}{{}_2n_1}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $i, r$ | angles of incidence and refraction | ° |
| $n$ | refractive index | dimensionless |
| $v$ | speed of light in the medium | m s⁻¹ |

**Use it when:**

> Light crosses a boundary. Some papers write $\mu$ instead of $n$ — same quantity.

**Trap:**

> **Frequency does not change** on refraction — it is fixed by the source. Since $v = f\lambda$, it is the wavelength that shortens in the denser medium.

### ● `P9.4` Real depth, apparent depth and the shift

$$n = \frac{\text{real depth}}{\text{apparent depth}} \qquad \text{shift } x = t\left(1 - \frac{1}{n}\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $t$ | real depth or slab thickness | m |
| $x$ | apparent shift | m |
| $n$ | refractive index of the denser medium | dimensionless |

**Use it when:**

> A coin in water, a pin under a glass slab, a pool that looks shallower than it is.

**Trap:**

> Valid for **near-normal viewing** only. The shift does not depend on where the slab sits between object and eye.

### ● `P9.5` Critical angle and total internal reflection

$$\sin C = \frac{n_{\text{rarer}}}{n_{\text{denser}}} = \frac{1}{n} \qquad C = \sin^{-1}\left(\frac{1}{n}\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $C$ | critical angle | ° |
| $n$ | index of the denser medium w.r.t. the rarer | dimensionless |

**Use it when:**

> Optical fibres, mirages, the brilliance of diamond ($C \approx 24°$), totally reflecting prisms.

**Trap:**

> Two conditions, both required: light must travel **denser to rarer**, and $i$ must **exceed** $C$. Since $n$ is larger for violet, violet has the smallest $C$ and is totally reflected first.

### ○ `P9.6` Refraction at a single spherical surface

$$\frac{n_2}{v} - \frac{n_1}{u} = \frac{n_2-n_1}{R}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $n_1$ | index of the medium the light starts in | dimensionless |
| $n_2$ | index of the medium it enters | dimensionless |
| $R$ | radius of curvature of the surface | m |

**Use it when:**

> One curved refracting surface. Applying it twice, once at each face, is what produces the lens maker's formula.

**Trap:**

> Distances are measured from the **pole of the surface**, and the sign convention still applies to $R$.

### ● `P9.7` Lens maker's formula

$$\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $n$ | index of the lens w.r.t. the surrounding medium | dimensionless |
| $R_1$ | radius of the first surface met | m |
| $R_2$ | radius of the second surface | m |

**Use it when:**

> Focal length from the lens's shape and material, or explaining what happens when a lens is moved into water.

**Trap:**

> It is $n$ **relative to the surroundings**. A glass lens ($n=1.5$) in water ($n=1.33$) has a much longer focal length; if the surrounding medium had the same index as the lens, $f$ would be infinite and the lens would vanish optically.

### ● `P9.8` Thin lens formula and magnification

$$\frac{1}{v} - \frac{1}{u} = \frac{1}{f} \qquad m = \frac{h'}{h} = \frac{v}{u}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $u, v$ | object and image distances from the optical centre | m |
| $f$ | focal length — positive convex, negative concave | m |
| $m$ | magnification | dimensionless |

**Use it when:**

> Any thin lens.

**Trap:**

> **Minus** for lenses, **plus** for mirrors — and the magnification is $+v/u$ for a lens but $-v/u$ for a mirror. Both differences are exam-critical.

### ● `P9.9` Power of a lens, and lenses in contact

$$P = \frac{1}{f\ \text{in metres}} \qquad P = P_1 + P_2 + \cdots \qquad \frac{1}{F} = \frac{1}{f_1}+\frac{1}{f_2}+\cdots$$

| Symbol | Meaning | Unit |
|---|---|---|
| $P$ | power of the lens | D (dioptre) |
| $f$ | focal length — **must be in metres** | m |
| $F$ | focal length of the combination | m |

**Use it when:**

> Spectacle prescriptions, or two lenses stuck together.

**Trap:**

> $f$ in **metres**, not centimetres — a 20 cm lens is 5 D, not 0.05 D. Converging power is positive, diverging negative.

### ● `P9.10` Refraction through a prism

$$A + \delta = i + e \qquad r_1 + r_2 = A \qquad n = \frac{\sin\left(\dfrac{A+\delta_m}{2}\right)}{\sin\left(\dfrac{A}{2}\right)}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $A$ | angle of the prism | ° |
| $\delta$ | angle of deviation | ° |
| $\delta_m$ | minimum deviation | ° |
| $i, e$ | angles of incidence and emergence | ° |

**Use it when:**

> A prism. At minimum deviation the ray passes **symmetrically**: $i = e$ and $r_1 = r_2 = A/2$.

**Trap:**

> For a **thin** prism the formula simplifies to $\delta = (n-1)A$. The graph of $\delta$ against $i$ is a curve with a single minimum, not a straight line.

### ● `P9.11` Magnifying power of a simple and compound microscope

$$\text{simple: } m = 1 + \frac{D}{f} \ \text{(image at }D) \qquad m = \frac{D}{f}\ \text{(image at }\infty)$$
          $$\text{compound: } m = \frac{v_o}{u_o}\left(1+\frac{D}{f_e}\right) \approx \frac{L}{f_o}\cdot\frac{D}{f_e}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $D$ | least distance of distinct vision | 25 cm |
| $f_o, f_e$ | focal lengths of objective and eyepiece | m or cm |
| $L$ | tube length (separation of the lenses) | m or cm |

**Use it when:**

> A magnifier or a microscope. High magnification needs **both** focal lengths short.

**Trap:**

> Two cases for every instrument — image at $D$ (relaxed formula has the $1+$) and image at infinity (no $1+$). Read which the question wants.

### ● `P9.12` Magnifying power of a telescope

$$m = \frac{f_o}{f_e} \ \text{(normal adjustment)}, \quad L = f_o + f_e \qquad m = \frac{f_o}{f_e}\left(1+\frac{f_e}{D}\right)\ \text{(image at }D)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $f_o$ | objective focal length — **long** | m or cm |
| $f_e$ | eyepiece focal length — **short** | m or cm |
| $L$ | length of the telescope | m or cm |

**Use it when:**

> An astronomical telescope. A large objective also gathers more light, improving resolution and brightness.

**Trap:**

> Exactly the **opposite** requirement from a microscope: the telescope objective wants a **long** focal length, the microscope objective a short one. A reflecting telescope replaces the objective lens with a concave mirror, avoiding chromatic aberration entirely.

## `CONST` Constants and conversions — *know the units too*

### ● `K` Every constant this paper can hand you, with its unit

| Symbol | Meaning | Value and unit |
|---|---|---|
| $e$ | elementary charge | 1.6 × 10⁻¹⁹ C |
| $m_e$ | electron mass | 9.1 × 10⁻³¹ kg |
| $\varepsilon_0$ | permittivity of free space | 8.854 × 10⁻¹² F m⁻¹ |
| $1/4\pi\varepsilon_0$ | Coulomb constant | 9 × 10⁹ N m² C⁻² |
| $\mu_0$ | permeability of free space | 4π × 10⁻⁷ T m A⁻¹ |
| $\mu_0/4\pi$ | the form used in Biot–Savart | 10⁻⁷ T m A⁻¹ |
| $c$ | speed of light in vacuum | 3 × 10⁸ m s⁻¹ |
| $h$ | Planck constant | 6.63 × 10⁻³⁴ J s |
| $k_B$ | Boltzmann constant | 1.38 × 10⁻²³ J K⁻¹ |
| $\mu_B$ | Bohr magneton | 9.27 × 10⁻²⁴ A m² |
| 1 eV | electron-volt | 1.6 × 10⁻¹⁹ J |
| 1 kWh | unit of electrical energy | 3.6 × 10⁶ J |
| $D$ | least distance of distinct vision | 25 cm |
| $B_E$ | Earth's magnetic field, order of magnitude | ~10⁻⁵ T |

**Trap:**

> Watch the letters that mean different things in different chapters: $L$ is length (Ch 2, 4), self-inductance (Ch 6) and tube length (Ch 9); $I$ is current, moment of inertia (Ch 5) and magnetisation (Ch 5); $\sigma$ is surface charge density (Ch 1) and conductivity (Ch 3); $\mu$ is mobility (Ch 3) and permeability (Ch 5).

Built from the notes for Chapters 1–8 in this repository, which were themselves grounded against the lecture board frames rather than the ASR transcripts — the extracted NCERT text flattens equations during PDF conversion and is unreliable for them, so NCERT was used here only for units, constants and symbol names. Chapter 9 is written from NCERT and from the published **Ray Optics to 9.4** page, pending processing of that chapter's eighteen lecture videos.

Derivations for the entries marked ○, and for many marked ●, are on the companion page **Physics, Derived**.
