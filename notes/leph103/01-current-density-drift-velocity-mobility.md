# Electric Current, Current Density, Drift Velocity and Mobility

**NCERT sections covered:** 3.2, 3.3, 3.4, 3.5, 3.5.1

## Electric current (NCERT 3.2)

Current is defined as the rate of flow of charge through a cross-sectional area:
$$I = \frac{Q}{t}, \qquad I = \frac{dQ}{dt}\ \text{(instantaneous form)}$$
SI unit: the **ampere** (A), with $1\text{ A} = 1\text{ C}/1\text{ s}$ -- a current of 1 A means 1 coulomb crosses the cross-section every second.

**Current is a scalar**, not a vector, even though it is conventionally drawn with an arrow: it does not obey the law of vector addition. The teacher's example -- current through a wire is the same value $I$ whether the wire runs straight or is bent/curled -- matches NCERT's own point (a curved path would need vector resolution into components if current were a vector, but the measured current is identical regardless of the wire's shape).

## Current density (NCERT 3.4)

Current density $\vec{J}$ is current per unit area, a **vector** directed along the flow of current:
$$J = \frac{I}{A}$$
If the cross-section is tilted at angle $\theta$ to the current direction, the effective area is $A\cos\theta$, so
$$J = \frac{I}{A\cos\theta}$$
For a conductor whose cross-section changes along its length (same $I$ everywhere by charge conservation, but $A$ -- and hence $J$ -- varies), current density in general varies point to point. Since $\vec{J}$ and $\vec{A}$ are both vectors, the relation is written as a dot product, and in integral form (for $J$ non-uniform over the area):
$$I = \vec{J}\cdot\vec{A}, \qquad I = \int_A \vec{J}\cdot d\vec{A}$$
Unit of current density: $\text{A/m}^2$.

## Random thermal motion of free electrons (NCERT 3.5, cf. Example 3.1(b))

In a conductor with no applied field, free electrons move randomly, colliding with fixed ions. Each electron's thermal speed follows from kinetic theory:
$$\frac{1}{2}mv^2 = \frac{3}{2}k_BT \implies v = \sqrt{\frac{3k_BT}{m}}$$
At room temperature this comes out to about $10^5\ \text{m/s}$ -- very fast, but because the $N$ free electrons' velocities $u_1, u_2, \ldots, u_N$ are randomly oriented, their vector average is zero:
$$\text{average velocity} = \frac{\vec{u}_1+\vec{u}_2+\cdots+\vec{u}_N}{N} = 0$$
So despite the huge thermal speed, there is **no net current** without an applied field.

## Drift velocity (NCERT 3.5, eq. 3.14-3.17)

Switching on an electric field $\vec{E}$ exerts a force on each (negatively charged) electron:
$$\vec{F} = -e\vec{E} \quad(\text{opposite to } \vec{E}), \qquad \vec{a} = \frac{\vec{F}}{m} = -\frac{e\vec{E}}{m}$$
Current direction is conventionally opposite to the direction electrons actually drift. Averaging the velocity gained since each electron's *last collision*, over the average time between collisions (the **relaxation time** $\tau$), gives the drift velocity:
$$\vec{v}_d = \vec{a}\tau = -\frac{e\vec{E}}{m}\tau$$
Plugging in typical numbers gives $v_d \approx 1\ \text{mm/s}$ -- consistent with NCERT's Example 3.1(a) result of $\approx 1.1\ \text{mm/s}$ for a copper wire -- i.e. roughly $10^{-8}$ times the thermal speed, even though it's this tiny drift, not the large thermal motion, that constitutes the current.

## Mobility (NCERT 3.5.1)

Mobility $\mu$ (a scalar) is the magnitude of drift velocity per unit electric field:
$$\mu = \frac{v_d}{E}$$
Substituting $v_d = eE\tau/m$:
$$\boxed{\mu = \frac{e\tau}{m}}$$
Mobility is **independent of $E$** -- it depends only on the electron's charge, mass, and the relaxation time $\tau$. Since $\tau$ decreases as temperature rises (more frequent collisions), $\mu$ also decreases with rising temperature. Combining with the earlier current-density relation gives current density directly in terms of mobility:
$$\vec{J} = -ne\vec{v}_d = ne\mu\vec{E}$$

---
*Note on this lecture's transcript:* coverage checks pass cleanly (ratio 1.02, no adjacent-repetition, and the non-adjacent duplicate scan found zero flagged pairs across all 65 segments) -- this lecture does **not** show the delayed-repetition ASR artifact found in some other lectures in this chapter. However, the transcript's own narration runs out about 12 seconds before the video's true end, right as the teacher begins the formal N-electron derivation of drift velocity. The quantitative drift-velocity result ($v_d=a\tau$, $v_d\approx1$ mm/s) and the entire mobility section above (definition, boxed formula, temperature dependence, and the final $J=ne\mu E$ relation) are grounded entirely from board frames, not narration -- the board runs ahead of the spoken explanation for this last stretch. See the flagged span below for exactly which frames and why this reads as "recording ran out," not a fabrication/repetition artifact.


## Verify these spans
- [30:51–31:03] The transcript's final segment (starting 1851s, 'let us suppose there are n electrons...') cuts off mid-sentence right as the teacher begins the formal N-electron derivation of drift velocity (NCERT eq. 3.16-3.17) -- the transcript never verbally states vd = a*tau = -eE*tau/m, the ~1 mm/s numeric estimate, the mobility definition, mu = e*tau/m, or J = n*e*mu*E. This is NOT the delayed-repetition ASR artifact found elsewhere in this chapter: the non-adjacent duplicate scan found 0 flagged pairs across all 65 segments, coverage passes cleanly (ratio 1.02), and every segment from 1396s onward is distinct, coherent, natural classroom speech (direction-of-current, then F=-eE, then Newton's-second-law acceleration) with no verbatim or near-verbatim repeats -- it reads like real audio that simply runs out at the video's true duration, not fabrication or a re-transcription loop. Board frames, however, show this exact content already written well before the transcript catches up: floor_000063 (1240s) has the boxed vd = -eE*tau/m and vd~1mm/s, and floor_000085 (1680s) through floor_000093 (1840s) show a clean incremental build of the mobility section (heading -> ratio definition -> mu=vd/E -> mu=e*tau/m boxed -> mu independent of E, temperature dependence -> J=neuE) -- a genuine progression, not an out-of-place page, and a direct continuation of the derivation the transcript was mid-way through narrating. The teacher appears to have written ahead of his own narration for this final stretch; all claims above with transcript_span=None are grounded from these frames alone.