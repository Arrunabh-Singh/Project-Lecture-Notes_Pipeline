# Magnifying Power of a Refracting Telescope

**NCERT sections covered:** 9.7.2


## Refracting (astronomical) telescope (NCERT 9.7.2)

A telescope also uses two convex lenses, but the other way round from a microscope.
- The **objective is the bigger lens**, with a large focal length $f_o$ and a large aperture. *Memory hook:* the objects viewed through a telescope are big.
- The **eyepiece is the smaller lens**, with a short focal length $f_e$.

**Image formation.**
1. The object is very far away, so the rays from it arrive **parallel**.
2. The objective brings them to a real, inverted image A′B′ in its **focal plane**, at distance $f_o$.
3. The eyepiece, at distance $u_e$ from A′B′, magnifies this into the final image A″B″.

## Magnifying power

$$\text{MP} = \frac{\beta}{\alpha}$$
- $\beta$ is the angle subtended at the eye by the final image.
- $\alpha$ is the angle subtended by the **object at the eye**. The object cannot be brought to the least distance of distinct vision. Because the tube is short compared with the object's distance, the angle at the objective equals the angle at the eye.

The angles are small, so:
$$\tan\beta = \frac{A'B'}{u_e}, \qquad \tan\alpha = \frac{A'B'}{f_o}$$
$$\text{MP} = \frac{\tan\beta}{\tan\alpha} = -\frac{f_o}{u_e}$$
The minus sign comes from the sign convention (A′B′ and $u_e$ are negative).

**The eyepiece term.** The lens formula for the eyepiece, with signs, gives $\dfrac{1}{u_e} = \dfrac{1}{f_e} + \dfrac{1}{v_e}$. So
$$\text{MP} = -f_o\left(\frac{1}{f_e} + \frac{1}{v_e}\right)$$

**Case 1: final image at the least distance of distinct vision ($v_e = D$).**
$$\text{MP} = -f_o\left(\frac{1}{f_e} + \frac{1}{D}\right) = -\frac{f_o}{f_e}\left(1 + \frac{f_e}{D}\right)$$

**Case 2: final image at infinity ($v_e = \infty$, normal adjustment).**
$$\text{MP} = -\frac{f_o}{f_e} \qquad\text{(magnitude } f_o/f_e\text{, the NCERT result)}$$

So $\text{MP} \propto f_o$ and $\propto 1/f_e$. Use an objective of **large** focal length and an eyepiece of **small** focal length.

**Q.** Given convex lenses of focal lengths 2 cm, 5 cm, 10 cm and 7 cm, which two make the best telescope?

**$f_o = 10$ cm** (largest) and **$f_e = 2$ cm** (smallest).

## Length of the tube

The tube length is the distance between the two lenses:
$$L = f_o + u_e$$

In normal adjustment ($v_e = \infty$), the intermediate image must be at the eyepiece's focus, so $u_e = f_e$. The focal points of the two lenses coincide, and

$$\boxed{L = f_o + f_e}, \qquad \text{MP} = \frac{f_o}{f_e}$$

Many exam numericals combine these two equations.

---
*Note on this lecture's transcript:* `gemini-3.5-flash` was in a 503 outage and then out of daily quota when this chapter was processed, so the audio was transcribed by `gemini-3.5-flash-lite` in overlapping five-minute windows, joined where the overlapping speech matches word for word. Lite's clock ran fast (by up to 2x) inside a window; each window was rescaled to its true length, so times quoted here are approximate (roughly ±30 s). Every gap of more than 30 s was re-transcribed on its own to confirm whether speech was missing. Equations are taken from the board frames, not from the transcript.
