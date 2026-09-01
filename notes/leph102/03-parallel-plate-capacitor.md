# The Parallel Plate Capacitor (with and without dielectric)

**NCERT sections covered:** 2.12, 2.13

## Capacitance of a parallel plate capacitor

### Without dielectric (NCERT 2.12)
Plate separation $d$, plate area $A$, charges $\pm Q$ (surface charge density $\sigma = Q/A$).
Field between the plates: $E = \dfrac{\sigma}{\varepsilon_0} = \dfrac{Q}{A\varepsilon_0}$.
Potential difference: $V = Ed$. Capacitance:
$$C = \frac{Q}{V} = \frac{A\varepsilon_0}{d}$$
Matches NCERT Eq. (2.43) exactly.

### Completely filled with dielectric, constant $k$ (NCERT 2.13)
Inside a dielectric the field is reduced by a factor $k$: $E = \dfrac{\sigma}{k\varepsilon_0}$. Repeating the same steps:
$$C = \frac{kA\varepsilon_0}{d}$$
This is why real capacitors use a dielectric between the plates -- it raises capacitance by a factor of $k$ for the same geometry. The lecture names three practical types built this way: **paper capacitors**, **mica capacitors**, and **electrolytic capacitors**.

### Partially filled with dielectric
A slab of thickness $t < d$ and dielectric constant $k$ sits in the gap; the remaining $(d-t)$ is air.
- Field in the air gap: $E_{air} = \sigma/\varepsilon_0$
- Field in the dielectric: $E_{diel} = \sigma/(k\varepsilon_0)$

$$V = (d-t)\frac{\sigma}{\varepsilon_0} + t\frac{\sigma}{k\varepsilon_0} = \frac{Q}{A\varepsilon_0}\left[(d-t) + \frac{t}{k}\right]$$
$$C = \frac{A\varepsilon_0}{(d-t) + t/k}$$

**Memory shortcut taught in the lecture:** treat each layer (air included, with $k=1$) as a slab of thickness $T_i$ and constant $K_i$, and sum:
$$C = \frac{A\varepsilon_0}{\sum_i T_i/K_i}$$

### Special case: a metal slab bridging the gap
If the inserted slab is a conductor (not a dielectric) and it touches both plates, that is the $t \to d$, $k \to \infty$ limit of the formula above -- the two plates are effectively short-circuited through the metal, so $C \to \infty$. This is the board's shorthand ("$K=\infty$ for metals") for that specific boundary case, not a general claim that any metal slab makes $C$ infinite -- a metal slab of thickness $t<d$ that does **not** touch both plates instead just reduces the effective air gap to $(d-t)$, giving the ordinary partial-fill result with $k\to\infty$ applied only to that slab's own term (which drops out, leaving $C = A\varepsilon_0/(d-t)$).
