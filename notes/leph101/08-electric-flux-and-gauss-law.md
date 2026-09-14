# Correction on Dipole PE, Total Force on a Dipole, Electric Flux, and Gauss's Law

**NCERT sections covered:** 1.9, 1.11, 1.13

## Corrections and follow-ups from the previous lecture

- In the dipole PE numerical, the reference angle $\theta_1$ (where PE is taken as zero) is **$90°$**, not $0°$ — use $\cos90°=0$.
- **Total (net) force on a dipole in a uniform field is zero**: the two equal-and-opposite forces on the charges cancel exactly, so the dipole only *rotates*, it doesn't translate. In a **non-uniform** field, net force is no longer zero, so the dipole undergoes both translational *and* rotational motion.

## Electric flux (NCERT 1.9)

**Area as a vector:** an area element $d\vec S$ has both magnitude and direction — direction given by the **outward-drawn normal** to the surface at that point (e.g. for a cube, the outward normal on each face points away from the enclosed volume).

**Electric flux** $\Phi$ is the number of field lines passing *normally* (perpendicularly) through a given area:
$$\Phi = EA\cos\theta = \vec E\cdot\vec A$$
($\theta$ = angle between $\vec E$ and the area's outward normal.) Maximum when $\vec E$ is parallel to the normal; zero when $\vec E$ lies in the plane of the surface (analogy used in the lecture: water flow through a rotating ring/bangle — maximum flow face-on, zero flow edge-on).

**General definition:** $d\Phi = \vec E\cdot d\vec S$ for a small element, $\Phi = \oint_S \vec E\cdot d\vec S$ over the whole surface. **SI unit:** N$\,$m$^2$C$^{-1}$. Flux is a **scalar** (it's a dot product).

## Gauss's law (NCERT 1.13)

**Statement:** the total electric flux through any closed surface $S$ in vacuum equals $1/\varepsilon_0$ times the total charge enclosed:
$$\boxed{\oint_S \vec E\cdot d\vec S = \frac{Q_\text{enclosed}}{\varepsilon_0}}$$

### Derivation for a point charge (spherical Gaussian surface)
For a point charge $Q$ at the centre of a sphere of radius $r$: $\vec E$ is radial with constant magnitude $\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}$ everywhere on the sphere, and everywhere **parallel** to $d\vec S$ ($\theta=0,\ \cos\theta=1$). So:
$$\oint_S\vec E\cdot d\vec S = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\oint_S dS = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}(4\pi r^2) = \frac{Q}{\varepsilon_0}$$
The $r^2$ cancels — the result is **independent of the sphere's radius**. Though proved here only for a sphere, $\Phi=Q/\varepsilon_0$ holds for a closed surface of **any** shape enclosing the same charge $Q$.

### Flux example: closed cylinder in a uniform field
For a uniform field passing straight through a closed cylinder aligned with the field (entering one flat end, exiting the other, none crossing the curved side): the **total** flux through the closed surface is **zero** — outward flux at the exit face exactly cancels inward flux at the entry face.

---
*Note on this lecture's transcript:* the Gauss's-law derivation and the cylinder example above are grounded entirely from board frames -- the transcript repeats earlier flux-definition material there instead. See the flagged span below.


## Verify these spans
- [30:04–32:02] The transcript re-transcribes the earlier flux-definition material (Phi=EA cos theta, roughly matching t=903-1030s) a second time from about t=1834s to its last segment at t=1918-1947s -- a delayed-repetition artifact, not new content. Board frames tell a different story for this same window: floor_000091.jpg and floor_000095.jpg (both around t=1800-1880s, within this window) show the actual mathematical PROOF of Gauss's law for a point charge using a spherical Gaussian surface (E radial and parallel to dS everywhere, integral reduces via the sphere's surface area 4 pi r^2 to Phi=Q/eps0), generalised to an arbitrary closed surface shape, plus a flux-through-a-closed-cylinder example (net flux zero). None of this derivation or example appears in the transcript, which only ever states Gauss's law verbally without deriving it. The two claims above (the spherical-surface derivation and the cylinder example) are grounded entirely from these board frames.