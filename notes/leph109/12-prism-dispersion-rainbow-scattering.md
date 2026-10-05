# Prism, Dispersion, Rainbow and Scattering

**NCERT sections covered:** 9.6


## Prism and dispersion

**Prism (board).** A homogeneous transparent medium, such as glass, enclosed by two plane refracting surfaces is called a prism. A glass prism has **3 rectangular faces and 2 triangular faces**.

**Dispersion (board).** The splitting of white light into its constituent colours when it passes through a prism. The colours spread out as **VIBGYOR**, with **violet deviated the most and red the least**: $\delta_V > \delta_R$.

**Why does dispersion happen?** The refractive index of a medium is **different for different colours**. "$n_g = 1.5$" is only a typical value. Cauchy's formula gives

$$n = A + \frac{B}{\lambda^2} + \frac{C}{\lambda^4} + \dots \qquad (A, B, C \text{ constants})$$

so $n$ decreases as wavelength increases (the lecture writes this loosely as $n \propto 1/\lambda$). Since $\lambda_R > \lambda_V$, we get $n_V > n_R$, and violet bends more. *(Current NCERT mentions dispersion only in the chapter summary. Cauchy's formula is an extra.)*

## Rainbow (not in the current NCERT text)

A rainbow is natural dispersion.

**Conditions:**
- tiny water droplets must be suspended in the air, after rain or near a garden fountain; the droplets act as prisms;
- **the observer's back must face the Sun**.

**Primary rainbow.**
- Sunlight is refracted on entering a drop, **reflected once** inside it, and refracted again on leaving.
- Violet reaches the eye at about **40°** to the anti-solar direction and red at about **42°**, so the band is about 2° wide.
- The colours are in the usual order, **red on the outside and violet on the inside**.

**Secondary rainbow.**
- The light enters the lower part of the drop and is **reflected twice** inside it.
- The angles are about **50°–53°**, a band of about 3°, seen **above** the primary.
- Its **colours are reversed**: violet is on the outside.

*(The lecture calls the reflections inside the drop "total internal reflection". For the rays that form the bow, the angle inside the drop, about 40°, is below water's critical angle of about 49°. So the reflection is really ordinary partial reflection, which is also why rainbows are faint.)*

Usually we see only an **arc**, because the ground cuts off the rest of the circle. From an aircraft, a **full circular rainbow** can be seen.

## Refraction through a prism (NCERT 9.6)

**Setup.**
- A ray strikes the first face at angle of incidence $i$ and is refracted at $r_1$.
- It meets the second face at $r_2$ and emerges at angle of emergence $e$.
- The deviation at the first face is $\delta_1 = i - r_1$, and at the second face $\delta_2 = e - r_2$.
- The total deviation $\delta$ is the exterior angle of the triangle formed by the incident ray produced and the emergent ray produced back, so
$$\delta = \delta_1 + \delta_2 = (i - r_1) + (e - r_2) = i + e - (r_1 + r_2)$$

**Angle of prism A:** the angle between the two refracting (rectangular) faces.

**Showing $r_1 + r_2 = A$.** Let N be the point where the two normals meet inside the prism.
- In the quadrilateral formed by the apex, the two points of incidence and N, the angles at the two points of incidence are 90° (each normal is perpendicular to its face). The angles sum to 360°, so
$$90° + A + 90° + \angle N = 360° \;\Rightarrow\; A + \angle N = 180°$$
- In the triangle formed by the two points of incidence and N, $r_1 + r_2 + \angle N = 180°$.
- Comparing the two:
$$\boxed{r_1 + r_2 = A}$$

Substituting into the deviation:
$$\boxed{\delta = i + e - A} \qquad\text{or}\qquad \delta + A = i + e$$

## Angle of minimum deviation

Measure $\delta$ for $i = 30°, 35°, 40°, \dots$ and plot $\delta$ against $i$. The deviation **falls, reaches a minimum $\delta_m$, then rises**.

**At $\delta = \delta_m$:**
1. $i = e$;
2. the ray inside the prism travels **parallel to the base**;
3. $r_1 = r_2 = r$, and since $r_1 + r_2 = A$, $2r = A$, so $r = A/2$.

*Board slip: the board boxes this as "$A = r/2$". The correct relation is $r = A/2$, and the teacher corrects herself a minute later when using it.*

**Prism formula.**
- From $i + e = A + \delta_m$ with $i = e$: $\quad i = \dfrac{A + \delta_m}{2}$.
- Snell's law at the first face, $n_1 \sin i = n_2 \sin r$, then gives

$$\boxed{n_{21} = \frac{n_2}{n_1} = \frac{\sin\left(\dfrac{A + \delta_m}{2}\right)}{\sin\left(\dfrac{A}{2}\right)}}$$

The 2s in the numerator and denominator **cannot be cancelled**, because each sits inside a sine.

## Deviation by a thin prism (NCERT 9.6)

A prism with **$A < 10°$** is a **thin prism**, and all its angles are small, so $\sin\theta \approx \theta$.

**Snell's law at the two faces:** $n_1 i = n_2 r_1$ and $n_2 r_2 = n_1 e$. So, with $n = n_2/n_1$,
$$i = n r_1, \qquad e = n r_2$$

**Deviation:**
$$\delta = i + e - A = n(r_1 + r_2) - A = nA - A \;\Rightarrow\; \boxed{\delta = (n - 1)A}$$

For a thin prism the deviation depends only on $A$ and $n$. It is **independent of the angle of incidence**, whereas for a general prism $\delta$ depends on $i$ and $e$.

## Angular dispersion and dispersive power (not in the current NCERT text)

**Angular dispersion.** The angle between the emergent rays of two colours (violet and red):
$$\theta = \delta_V - \delta_R$$
For a thin prism:
$$\theta = (n_V - 1)A - (n_R - 1)A = (n_V - n_R)A$$
It depends on the angle of the prism.

**Dispersive power ($\omega$).** The ratio of the angular dispersion to the **mean deviation**, taken as the deviation of yellow light:
$$\omega = \frac{\delta_V - \delta_R}{\delta_Y} = \frac{(n_V - n_R)A}{(n_Y - 1)A} = \frac{n_V - n_R}{n_Y - 1}$$

- $\omega$ is **independent of the angle of prism** and depends only on the material.
- A prism that spreads white light over a wider fan has the greater dispersive power.
- $n_\text{flint} > n_\text{crown}$, and $\omega_\text{flint} > \omega_\text{crown}$.
- If a numerical does not give $n_Y$, take $n_Y = \dfrac{n_V + n_R}{2}$.

## Scattering of light (not in the current NCERT text)

**What scattering is.** Air molecules, dust and smoke particles in the atmosphere deflect light from its path. This happens through the interaction of the light wave's electric field with the particle. The deflected light is **scattered light**.

**Rayleigh scattering.** For particles **smaller than (or about equal to) the wavelength**, the scattered intensity is
$$I \propto \frac{1}{\lambda^4}$$
So fine particles scatter violet and blue far more strongly than red.

**Blue sky.** Blue and violet are scattered strongly all over the sky. Violet is partly lost on the way by further scattering, so the scattered skylight reaching us is rich in **blue**.
- **With no atmosphere, the sky would look black** even in daytime, because there would be nothing to scatter the light.

**White clouds.** Cloud droplets are **much larger than the wavelength**. Then all colours are scattered about equally, and the clouds look **white**.

**Red Sun at sunrise and sunset (board).** At sunrise and sunset, sunlight travels a **longer path** through the atmosphere before it reaches the observer's eye directly. Violet and blue are strongly scattered out on the way, so the light reaching the observer is deprived of violet and blue and mostly red reaches the eye. Thus the Sun at sunrise and sunset appears **red**.

---
*Note on this lecture's transcript:* `gemini-3.5-flash` was in a 503 outage and then out of daily quota when this chapter was processed, so the audio was transcribed by `gemini-3.5-flash-lite` in overlapping five-minute windows, joined where the overlapping speech matches word for word. Lite's clock ran fast (by up to 2x) inside a window; each window was rescaled to its true length, so times quoted here are approximate (roughly ±30 s). Every gap of more than 30 s was re-transcribed on its own to confirm whether speech was missing. The opening minutes came back looped from the first five-minute window, so 0–4 min was re-transcribed in one-minute clips, and a left-over copy of that loop was removed during verification. Two short stretches (about 19:52–20:34 and 39:29–40:00) were spliced in from separate transcriptions; their duplicated sentences were removed. Equations are taken from the board frames, not from the transcript.
