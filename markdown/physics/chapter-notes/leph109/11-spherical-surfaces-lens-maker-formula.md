# Refraction at Spherical Surfaces and the Lens-Maker's Formula

**NCERT sections covered:** 9.5.1, 9.5.2


## Refraction at a spherical surface (NCERT 9.5.1)

**Assumptions.** In optics these must be stated before any derivation:

1. The object is a **point object on the principal axis**.
2. The angles made by the incident and refracted rays with the principal axis are **small**.
3. The **aperture is small**.

### (a) Convex spherical surface, light going from $n_1$ (rarer) to $n_2$ (denser)

**Setup.**

- A ray from the point object O strikes the surface at N.
- CN is the normal (C is the centre of curvature). The ray bends towards the normal and meets the axis at the image I.
- Drop NP′ perpendicular to the axis. With a small aperture, P′ coincides with the pole P.
- Angles with the axis: $\alpha$ for the incident ray, $\beta$ for the refracted ray, $\gamma$ for the normal.
- Distances: $PO = u$, $PI = v$, $PC = R$.

**Exterior-angle property** (exterior angle = sum of the interior opposite angles):
$$\triangle ONC:\; i = \alpha + \gamma \qquad\qquad \triangle NCI:\; \gamma = r + \beta \;\Rightarrow\; r = \gamma - \beta$$

**Snell's law at N.** The rule "each angle goes with the index of its own medium" gives $n_1 \sin i = n_2 \sin r$. For small angles $\sin i \approx i$ and $\sin r \approx r$:
$$n_1(\alpha + \gamma) = n_2(\gamma - \beta)$$

**Small angles, so each angle ≈ its tangent:**
$$n_1(\tan\alpha + \tan\gamma) = n_2(\tan\gamma - \tan\beta)$$
$$n_1\left(\frac{NP}{-u} + \frac{NP}{R}\right) = n_2\left(\frac{NP}{R} - \frac{NP}{v}\right)$$

The signs used are $u < 0$, $R > 0$, $v > 0$. Cancel NP and rearrange:

$$\boxed{\frac{n_2}{v} - \frac{n_1}{u} = \frac{n_2 - n_1}{R}}$$

**Memory hint.** Start from the lens formula $\frac1f = \frac1v - \frac1u$:

- put the index of the medium each distance lies in on top: $v$ is in $n_2$ and $u$ is in $n_1$;
- the right side is (index you are going **to** − index you are coming **from**) over $R$.

Numericals are set on this formula.

### (b) Concave spherical surface, light going from $n_2$ (denser) to $n_1$ (rarer)

The assumptions are the same. The object O is in $n_2$, with the centre of curvature on the same side. The ray bends **away** from the normal and forms a real image I in $n_1$.

**Angle relations:**
$$\triangle ONC:\; \alpha + i = \gamma \Rightarrow i = \gamma - \alpha \qquad\qquad \triangle CNI:\; r = \gamma + \beta$$

**Snell's law, then the small-angle step:** $n_2 \sin i = n_1 \sin r$ becomes $n_2 i = n_1 r$. Then
$$n_2\left(\frac{NP}{-R} - \frac{NP}{-u}\right) = n_1\left(\frac{NP}{-R} + \frac{NP}{v}\right)$$

The signs are $R < 0$ (C lies against the incident light), $u < 0$, $v > 0$. This gives:

$$\boxed{\frac{n_1}{v} - \frac{n_2}{u} = \frac{n_1 - n_2}{R}}$$

The result is the same formula with $n_1 \leftrightarrow n_2$ swapped, because the light now goes from $n_2$ to $n_1$. Whether the image is real or virtual, the equation is unchanged.

## Lens-maker's formula (NCERT 9.5.2)

**Assumptions:** the same as above, **plus the lens is thin**. All distances can then be measured from the optical centre O, since P₁ and P₂ almost coincide.

**Setup.** A lens of index $n_2$ sits in a medium of index $n_1$. Its first surface $LP_1M$ has radius $R_1$, and its second surface $LP_2M$ has radius $R_2$.

**Step 1: refraction at $LP_1M$.** Pretend the lens material fills all the space to the right. The first surface alone forms an image I′ at distance $v'$, inside $n_2$:
$$\frac{n_2}{v'} - \frac{n_1}{u} = \frac{n_2 - n_1}{R_1} \qquad (1)$$

**Step 2: refraction at $LP_2M$.** I′ acts as a **virtual object** for the second surface (it lies in $n_2$). The final image I is at $v$, in $n_1$:
$$\frac{n_1}{v} - \frac{n_2}{v'} = \frac{n_1 - n_2}{R_2} \qquad (2)$$

**Adding (1) and (2).** The $n_2/v'$ terms cancel:
$$\frac{n_1}{v} - \frac{n_1}{u} = (n_2 - n_1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$
$$\frac{1}{v} - \frac{1}{u} = \frac{n_2 - n_1}{n_1}\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

The left side is $1/f$ (lens formula), so:

$$\boxed{\frac{1}{f} = \frac{n_2 - n_1}{n_1}\left(\frac{1}{R_1} - \frac{1}{R_2}\right)}$$

This is the **lens-maker's formula**, used to design lenses of a desired focal length. Here $n_1$ is the index of the **surrounding medium**. In NCERT's notation, $\frac{n_2 - n_1}{n_1} = n_{21} - 1$.

*Note: when you substitute signed radii, do not cancel $\frac{1}{R_1}$ against $\frac{1}{R_2}$. For a biconvex lens $R_2$ is negative, so the two terms add.*

## Can a convex lens behave as a diverging lens?

Take a convex lens of glass, $n_2 = 1.5$. For a convex lens, $\left(\frac{1}{R_1} - \frac{1}{R_2}\right) > 0$.

1. **$n_2 > n_1$** (in air, $n_1 = 1$):
$$\frac1f = \frac{1.5 - 1}{1}\left(\frac{1}{R_1} - \frac{1}{R_2}\right) > 0$$
$f$ is positive: a **converging** lens, the normal case.

2. **$n_2 = n_1$** (in a liquid of index 1.5):
$$\frac1f = \frac{1.5 - 1.5}{1.5}(\dots) = 0 \;\Rightarrow\; f = \infty$$
The rays go straight through: it behaves as **plane glass**.

3. **$n_2 < n_1$** (in a liquid of index 1.6):
$$\frac1f = \frac{1.5 - 1.6}{1.6}\left(\frac{1}{R_1} - \frac{1}{R_2}\right) = -\frac{0.1}{1.6}(\dots)$$
$f$ is negative: the convex lens behaves as a **diverging (concave) lens**.

**Q. An air bubble inside water: does it behave as a convex or a concave lens?**
The bubble is the "lens" ($n_2 = 1$) and the water is the surroundings ($n_1 = 1.33$). It is bulging, so $(1/R_1 - 1/R_2) > 0$:
$$\frac1f = \frac{1 - 1.33}{1.33}\left(\frac{1}{R_1} - \frac{1}{R_2}\right) = -\frac{0.33}{1.33}(\dots) < 0$$
$f$ is negative, so the air bubble behaves as a **concave (diverging) lens**.

## Can a concave lens behave as a converging lens?

| Case | Behaviour |
|---|---|
| $n_2 > n_1$ (normal) | diverging lens (concave) |
| $n_2 = n_1$ | plane glass, $f = \infty$ |
| $n_1 > n_2$ (e.g. lens 1.5 in liquid 1.6) | **converging** lens: both factors are negative, so $f > 0$ |

## Lens vs mirror

A lens's focal length depends on the refractive indices through the factor $\frac{n_2 - n_1}{n_1}$. It can be positive, negative or infinite depending on the medium the lens is in. Put a lens in water and its focal length changes.

A mirror's focal length, $f = R/2$, has **no refractive index in it**. A mirror's focal length is the same in water as in air.

---
*Note on this lecture's transcript:* `gemini-3.5-flash` was in a 503 outage and then out of daily quota when this chapter was processed, so the audio was transcribed by `gemini-3.5-flash-lite` in overlapping five-minute windows, joined where the overlapping speech matches word for word. Lite's clock ran fast (by up to 2x) inside a window; each window was rescaled to its true length, so times quoted here are approximate (roughly ±30 s). Every gap of more than 30 s was re-transcribed on its own to confirm whether speech was missing. The start of the concave-surface derivation (about 11:26–12:02) was partly missing from the merged windows and was spliced in from a separate transcription; a few sentences there appear twice in the transcript. Equations are taken from the board frames, not from the transcript.
