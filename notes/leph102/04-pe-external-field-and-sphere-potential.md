# Potential Energy in an External Field, and Potential Due to a Charged Sphere

**NCERT sections covered:** 2.5, 2.8

## Potential energy in an external field (NCERT 2.8)

Distinct from Section 2.7 (potential energy of a system of charges due to *their own* mutual field): here the field $E$ (and potential $V$) is produced by **external sources**, not by the charge(s) whose energy we're computing.

### Potential energy of a single charge (NCERT 2.8.1)
Work done in bringing charge $q$ from infinity to a point at position $\vec r$, against the external potential $V(\vec r)$:
$$\boxed{PE = qV(\vec r)}$$

**Electron-volt:** if a charge of magnitude $e = 1.6\times10^{-19}$ C is accelerated through a potential difference of 1 V, it gains energy $1.6\times10^{-19}$ J -- this quantity of energy is defined as **1 electron-volt**:
$$1~\text{eV} = 1.6\times10^{-19}~\text{J}$$
(A unit of *energy*, built from the volt but not itself a unit of potential.)

### Potential energy of a system of two charges (NCERT 2.8.2)
Assemble $q_1$ then $q_2$ into the external field region, positions $\vec r_1,\vec r_2$:
- Bringing $q_1$ to $\vec r_1$ costs $q_1V(\vec r_1)$ (work against the external field alone).
- Bringing $q_2$ to $\vec r_2$ costs work against **both** the external field *and* the field now due to $q_1$:
$$W_{q_2} = q_2V(\vec r_2) + \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{12}}$$

Total potential energy of the assembled system:
$$\boxed{PE = q_1V(\vec r_1) + q_2V(\vec r_2) + \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{12}}}$$

*(For reference, the board also carries the dipole-in-external-field result derived from this same equation: $PE = -\vec p\cdot\vec E$ -- covered in more depth in a separate lecture on dipole potential energy.)*

## Electric potential due to a uniformly charged sphere (NCERT 2.5)

### On the surface
Outside a uniformly charged sphere (charge $q$, radius $R$), the field is identical to that of a point charge $q$ at the centre: $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}$. Integrating from infinity in to the surface:
$$V = -\int_\infty^R \vec E\cdot d\vec l = \frac{1}{4\pi\varepsilon_0}\frac{q}{R}$$
Same value a point charge $q$ at the centre would produce at distance $R$.

### Inside the sphere
Split the line integral at the surface -- from infinity to $R$ (as above), plus from $R$ inward to the field point:
$$V = -\int_\infty^R \vec E\cdot d\vec l \;+\; \left(-\int_R^{r} \vec E\cdot d\vec l\right)$$
The second term vanishes because $E = 0$ everywhere inside a charged conducting sphere. So:
$$\boxed{V_\text{inside} = V_\text{surface} = \frac{1}{4\pi\varepsilon_0}\frac{q}{R}}$$

**Key takeaway:** potential inside the sphere is *constant*, equal to the surface value -- even though the field itself is zero throughout the interior. (Zero field means no *change* in potential, not zero potential; this is the same field/potential distinction flagged in the very first lecture of this chapter.)

---
*Note on this lecture's transcript:* the final ~340 seconds, covering the sphere derivation above, are not reliably transcribed -- see the flagged span below. Those two claims are grounded directly in the board frames instead.


## Verify these spans
- [17:40–23:20] Board frames (floor_000054 at t=1060s: blank new page; floor_000055 at t=1080s: 'Electric potential on surface of sphere' heading just begun; floor_000063 at t=1240s and floor_000067 at t=1320s: the full surface-and-inside-sphere derivation, reaching a concluding statement) show this final ~340s of the lecture is spent on the sphere-potential derivation named in the lecture's own title. The ASR transcript never once mentions a sphere, surface, or conductor anywhere in its 38 segments -- instead its last ~30 segments (from roughly 790s to the claimed end at 1421s) continue elaborating the two-charges-in-external-field material, well past where the board shows that topic was finished (page 1, visible complete by ~t=520s) and a new page begun. This reads as sustained content substitution: real audio about the sphere derivation went untranscribed, replaced by an extended rehash of already-covered material. Automated coverage checks (duration-fabrication and repetition-loop detectors) did not catch it, since the substituted text is paraphrased rather than verbatim-repeated and its final timestamp (1421.1s) is close to the true 1400.47s duration. The two sphere claims above are grounded entirely in the board frames, not the transcript.