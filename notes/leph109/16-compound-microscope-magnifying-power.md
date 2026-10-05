# Magnifying Power of a Compound Microscope

**NCERT sections covered:** 9.7.1


## Compound microscope: how the image is formed (NCERT 9.7.1)

A compound microscope has two convex lenses:
- a small **objective** of short focal length $f_o$, near the object;
- a larger **eyepiece** of focal length $f_e$, at the eye.

*Memory hook:* the objects viewed through a microscope are small, so the objective is the smaller lens.

**Image formation.**
1. The object AB is placed **between $f_o$ and $2f_o$** of the objective.
2. The objective forms a **real, inverted, magnified** image A′B′ beyond $2f_o$.
3. A′B′ must fall **between the eyepiece's focus $F_e$ and its optical centre $O_e$**. The eyepiece then acts as a simple microscope on it and forms a large **virtual** final image A″B″.

## Magnifying power

As for the simple microscope, $\text{MP} = \beta/\alpha$:
- $\beta$ is the angle subtended at the eye by the final image;
- $\alpha$ is the angle the object would subtend at the least distance of distinct vision $D$.

The angles are small, and $u_e$ is the distance of A′B′ from the eyepiece:

$$\text{MP} = \frac{\tan\beta}{\tan\alpha} = \frac{-A'B'/(-u_e)}{AB/(-D)} = -\frac{A'B'}{AB}\cdot\frac{D}{u_e}$$

A′B′ is inverted, so its height is negative. The board marks the two factors as $m_o$ and $m_e$.

**Magnification of the objective:**
$$\frac{A'B'}{AB} = \frac{v_o}{u_o}$$

So:
$$\boxed{\text{MP} = -\frac{v_o}{u_o}\cdot\frac{D}{u_e}}$$

**The eyepiece term.** The lens formula for the eyepiece, with signs, gives $\dfrac{1}{u_e} = \dfrac{1}{f_e} + \dfrac{1}{v_e}$. Hence
$$\text{MP} = -\frac{v_o}{u_o}\,D\left(\frac{1}{f_e} + \frac{1}{v_e}\right)$$

**Case 1: final image at $D$ ($v_e = D$).**
$$\text{MP} = -\frac{v_o}{u_o}\left(1 + \frac{D}{f_e}\right)$$

**Case 2: final image at infinity ($v_e = \infty$, normal adjustment).**
$$\text{MP} = -\frac{v_o}{u_o}\cdot\frac{D}{f_e}$$

In both cases **MP = $m_o \times m_e$**. The eyepiece is just a simple microscope (lecture 15) looking at the objective's already-magnified image.

## Approximate formula

The object is placed very close to the objective's focus, so $u_o \approx f_o$. The first image forms very close to the eyepiece, so $v_o \approx L$, the **tube length** (the distance between the two lenses). Then

$$\text{MP} \approx -\frac{L}{f_o}\cdot\frac{D}{f_e} = -\frac{DL}{f_o f_e}$$

*(In the recording the teacher reads this out as "−D f_o/f_e", a slip; the board has $-DL/(f_o f_e)$. NCERT defines $L$ as the distance between the objective's second focal point and the eyepiece's first focal point. Taking $L \approx v_o$ is the lecture's simplification.)*

**For a large magnifying power, both $f_o$ and $f_e$ should be small, with $f_e > f_o$.**

**Q.** You are given convex lenses of focal lengths 5 cm, 10 cm, 2 cm and 7 cm. Which two would you choose for a compound microscope, and which would be the objective?

Choose the two shortest, **2 cm and 5 cm**. Use $f_o = 2$ cm as the objective and $f_e = 5$ cm as the eyepiece.

---
*Note on this lecture's transcript:* `gemini-3.5-flash` was in a 503 outage and then out of daily quota when this chapter was processed, so the audio was transcribed by `gemini-3.5-flash-lite` in overlapping five-minute windows, joined where the overlapping speech matches word for word. Lite's clock ran fast (by up to 2x) inside a window; each window was rescaled to its true length, so times quoted here are approximate (roughly ±30 s). Every gap of more than 30 s was re-transcribed on its own to confirm whether speech was missing. Equations are taken from the board frames, not from the transcript.
