# Lens Ray Diagrams, Lens Formula and Power

**NCERT sections covered:** 9.5.2, 9.5.3, 9.5.4


## Important rays for lens ray diagrams (NCERT 9.5.2)

1. **A ray parallel to the principal axis**
    - **Convex lens:** after refraction it passes through the focus **on the other side** of the lens.
    - **Concave lens:** it *appears* to pass through (diverge from) the focus **on the same side**.
2. **A ray through the focus becomes parallel to the principal axis** after refraction.
    - For a concave lens, this is the ray **directed towards** the focus on the far side.
3. **A ray through the optical centre goes undeviated**, for both lenses.

For a thin lens, show the bending at the centre line of the lens. Two rays locate the image.

## Images formed by a convex lens (NCERT 9.5.2)

Mark O, F and 2F on **both** sides of the lens. For a lens, 2F plays the role that C played for a mirror.

| Position of object | Position of image | Nature and size |
|---|---|---|
| At infinity | At F, on the other side | Real, inverted, **highly diminished** |
| Beyond 2F | Between F and 2F | Real, inverted, **diminished** |
| At 2F | At 2F | Real, inverted, **same size** |
| Between F and 2F | Beyond 2F | Real, inverted, **magnified** |
| At F | At infinity | Real, inverted, **highly magnified** |
| Between O and F | On the **same side** as the object (in front of the lens) | **Virtual, erect, magnified** |

- **At F:** a **point object** gives a parallel beam. For an **extended object**, the parallel ray (through F′) and the ray through O come out parallel, so the image is at infinity.
- **Between O and F:** the two refracted rays diverge. Produced backwards, they meet on the object's side. This is the only case where the image is virtual and on the same side as the object. It is the principle of the **simple microscope** (magnifying glass), the lens a palm-reader holds over your hand. The object must lie between O and F.
- Drawing tips are the same as for mirrors: for the "beyond 2F" case draw the object a little larger, and for "at 2F" mark A′B′ first.

## Images formed by a concave lens

| Position of object | Position of image | Nature and size |
|---|---|---|
| At infinity | Appears to be at F (same side) | Virtual, erect, **highly diminished** |
| Anywhere between infinity and O | Between O and F, same side as the object | Virtual, erect, **diminished** |

## Sign convention for lenses (NCERT 9.5)

1. **All distances are measured from the optical centre O**: $u = OA$, $v = OA'$, $f = OF$.
2. Distances **in the direction of the incident light are positive**; distances against it are negative.
3. Heights **above the principal axis are positive**; heights below it are negative.

| | $u$ | $v$ | $f$ |
|---|---|---|---|
| Convex lens (real image) | − | + | **+** |
| Concave lens | − | − | **−** |

- A convex lens converges rays to the focus on the far side, in the direction of the incident light, so $f > 0$.
- A concave lens's focus is where the rays *appear* to come from, on the incident side, so $f < 0$.
- This fits the "con**vex** → positive $f$, con**cave** → negative $f$" hook from lecture 05.
- Heights: the inverted real image of a convex lens has a negative height. Both $AB$ and $A'B'$ are positive for a concave lens.

## Lens formula and magnification (NCERT 9.5.2)

$$\frac{1}{f} = \frac{1}{v} - \frac{1}{u}, \qquad m = \frac{h_i}{h_o} = \frac{v}{u}$$

Compare the mirror versions, $\dfrac{1}{f} = \dfrac{1}{v} + \dfrac{1}{u}$ and $m = -\dfrac{v}{u}$.

The sign of $m$ gives the nature: $+$ means virtual and erect, $-$ means real and inverted. Its magnitude gives the size: $|h_i| < h_o$ is smaller, $=$ is the same size, $>$ is magnified. For example, $m = +2$ is virtual, erect and magnified; $m = +0.2$ is virtual, erect and smaller; $m = -5$ is real, inverted and magnified.

## Power of a lens (NCERT 9.5.3)

Send parallel rays into two convex lenses. Lens 1 bends the ray through a larger angle ($\theta > \theta'$), so its **degree of convergence** is greater. We say lens 1 has the greater **power**. The bigger bend brings the ray to the axis sooner, so its focal length is shorter ($f_1 < f_2$).

**Power is the reciprocal of focal length:**

$$P = \frac{1}{f}\qquad (f \text{ in metres})$$

The SI unit of power is the **dioptre (D)**; $1\,\text{D} = 1\,\text{m}^{-1}$.

- $f > 0$ gives $P > 0$: a **convex** lens.
- $f < 0$ gives $P < 0$: a **concave** lens. A lens of power $-1$ D is concave.
- **Always convert $f$ to metres** before taking the reciprocal. Forgetting is the most common mistake.

**Example.** Find the power of a concave lens of focal length 50 cm.
$f = -50 \text{ cm} = -0.5$ m, so $P = 1/f = -2$ D.

Rule of thumb from the lecture: a thick spectacle lens has a higher power and a shorter focal length, and a thin one has a lower power and a longer focal length. Strictly, the focal length depends on how curved the surfaces are; see the lens-maker formula in lecture 11.

## Lenses in contact (NCERT 9.5.4)

For thin lenses in contact (here convex $f_1$, convex $f_2$, concave $f_3$):

$$\frac{1}{f_\text{eff}} = \frac{1}{f_1} + \frac{1}{f_2} + \frac{1}{f_3}, \qquad P_\text{eff} = P_1 + P_2 + P_3$$

**Example:** $f_1 = 5$ cm, $f_2 = 10$ cm, $f_3 = -2$ cm.

$$\frac{1}{f_\text{eff}} = \frac{1}{5} + \frac{1}{10} - \frac{1}{2} = \frac{4 + 2 - 10}{20} = -\frac{4}{20} = -\frac{1}{5}$$

so $f_\text{eff} = -5$ cm $= -0.05$ m and $P_\text{eff} = -20$ D. The combination acts as a diverging lens.

*Board slip:* the board (and the recording) gives $4 + 2 - 10 = -2$, which leads to $f_\text{eff} = -10$ cm and $P = -10$ D. The correct values are $-5$ cm and $-20$ D. Cross-check with powers: $+20 + 10 - 50 = -20$ D.

## Textbook questions solved in the lecture

**Q9. One half of a convex lens is covered with black paper. Does it still form a complete image?**
**Yes.** Every part of the lens sends rays from every point of the object to the image. The two rays in a diagram are only the convenient ones for locating it. Covering half the lens removes half the rays, so the image is complete but its **intensity (brightness) is reduced, to about half**.

**Q10.** An object 5 cm tall is 25 cm from a converging lens of focal length 10 cm. ($2F = 20$ cm, so the object is beyond 2F.)
$h_o = +5$ cm, $u = -25$ cm, $f = +10$ cm.
$$\frac{1}{v} = \frac{1}{f} + \frac{1}{u} = \frac{1}{10} - \frac{1}{25} = \frac{3}{50} \;\Rightarrow\; v = +\frac{50}{3} \approx 16.7 \text{ cm}$$
The image is on the other side: real and inverted. $m = v/u = -\tfrac{2}{3} \approx -0.67$, so it is smaller. $h_i = m\,h_o = -\tfrac{10}{3} \approx -3.3$ cm.

**Q11.** A concave lens of focal length 15 cm forms an image 10 cm from the lens. How far is the object?
$f = -15$ cm, $v = -10$ cm.
$$\frac{1}{u} = \frac{1}{v} - \frac{1}{f} = -\frac{1}{10} + \frac{1}{15} = -\frac{1}{30} \;\Rightarrow\; u = -30 \text{ cm}$$
The object is 30 cm in front of the lens.

**Q16.** Find the focal length of a lens of power $-2.0$ D.
$f = 1/P = -0.5$ m $= -50$ cm, a diverging (concave) lens.

**Q17.** A doctor prescribes a corrective lens of power $+1.5$ D. Find its focal length; is it converging or diverging?
$f = 1/1.5$ m $= 200/3 \approx +66.7$ cm. Positive, so it is **converging** (convex).

---
*Note on this lecture's transcript:* `gemini-3.5-flash` was in a 503 outage and then out of daily quota when this chapter was processed, so the audio was transcribed by `gemini-3.5-flash-lite` in overlapping five-minute windows, joined where the overlapping speech matches word for word. Lite's clock ran fast (by up to 2x) inside a window; each window was rescaled to its true length, so times quoted here are approximate (roughly ±30 s). Every gap of more than 30 s was re-transcribed on its own to confirm whether speech was missing. The concave-lens ray diagrams (about 18:46–20:10) were missing from the merged windows and were spliced in from a separate transcription of that stretch. Equations are taken from the board frames, not from the transcript.
