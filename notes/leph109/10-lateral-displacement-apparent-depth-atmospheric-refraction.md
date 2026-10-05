# Lateral Displacement, Apparent Depth and Atmospheric Refraction

**NCERT sections covered:** 9.3


## Lateral displacement in a glass slab (NCERT 9.3)

**Setup and what happens to the ray.**

- A ray enters a slab of thickness $t$ at O, with angle of incidence $i$ and angle of refraction $r$.
- It leaves at B. The angle inside at the lower face is again $r$, and the ray emerges at angle $e$.
- The incident and emergent rays are **parallel**, so $i = e$.
- The ray is shifted sideways. The **lateral displacement** $d = BN$ is the perpendicular distance from B to the incident ray produced.

**Thickness** is the distance between the face where the ray enters and the face where it leaves. Turn the slab and the thickness changes with it.

**Derivation (board).** The incident ray, produced forward, makes the angle $i - r$ with the refracted ray OB.

In right $\triangle OBN$:
$$\sin(i - r) = \frac{BN}{OB} = \frac{d}{OB} \qquad (1)$$

In right $\triangle ON'B$, where N′ is the foot of the normal at the lower face:
$$\cos r = \frac{t}{OB} \qquad (2)$$

Dividing (1) by (2) cancels OB:
$$d = \frac{t\,\sin(i - r)}{\cos r}$$

For a given $i$ and slab material, $d \propto t$: the thicker the slab the ray crosses, the larger the lateral displacement. *(NCERT shows the lateral shift only qualitatively, in Fig. 9.9. This expression is an extra from the lecture.)*

## Real and apparent depth (NCERT 9.3)

A coin at the bottom of a water-filled container appears **raised**. Rays from the coin go from water (denser) into air (rarer) and bend **away from the normal**. Traced back, they seem to come from a point above the coin.

Let $h_1$ be the **real depth** and $h_2$ the **apparent depth**. For **normal viewing**, with the eye close to the surface and looking nearly straight down:

$$\frac{n_2}{n_1} = \frac{h_1}{h_2} = \frac{\text{real depth}}{\text{apparent depth}} \qquad\Rightarrow\qquad n = \frac{h_\text{real}}{h_\text{app}}$$

Here $n = n_w/n_a = 1.33$. Since $n > 1$, $h_1 > h_2$. Viewed obliquely, from far off, the calculation is different.

**Shift (how far the coin appears to rise):**
$$\Delta h = h_1 - h_2 = h_1 - \frac{h_1}{n} = h_1\left(1 - \frac{1}{n}\right)$$

*(NCERT names them the other way round, with $h_1$ apparent and $h_2$ real. The relation "apparent depth = real depth ÷ n, for near-normal viewing" is the same.)*

## The observer inside the water: a fish looking at a fisherman

Now the object (the fisherman) is in air and the observer (the fish) is in water. Light from the fisherman goes from rarer to denser, bending **towards** the normal. Traced back, it seems to come from higher up, so **to a fish, the fisherman appears raised (taller)**.

**Master formula (board):**

$$d' = \frac{d}{n_\text{medium}} \times n_\text{observer}$$

Here $d'$ is the apparent distance and $d$ the real distance. $n_\text{medium}$ is the refractive index where the object is, and $n_\text{observer}$ where the eye is.

- **Coin, observer in air:** $d' = d \times 1/n$, which is the result above.
- **Fisherman, fish in water ($n_2$):** $d' = d \times n_2/1$, so $n = \dfrac{d'}{d} = \dfrac{h_\text{app}}{h_\text{real}}$. This is the opposite ratio to the coin case. The master formula handles both without having to remember which is which.

**Several layers.** A coin lies under liquid layers of thicknesses $d_2, d_3, d_4$ and indices $n_2, n_3, n_4$, with the observer in air just above the surface:

$$d' = 1\left(\frac{d_2}{n_2} + \frac{d_3}{n_3} + \frac{d_4}{n_4}\right)$$

If the observer is a height $d_5$ above the surface, add $d_5/1$ (air). The result is then measured from the eye.

## Shift caused by a glass slab

An object is viewed through a slab of thickness $t$ and index $n$ (relative to the surroundings, $n = n_2/n_1$):

1. The first face forms an image O′.
2. O′ acts as the object for the second face, which forms the final image O″.
3. The observer sees the object at O″ (O′ is only an intermediate step).

$$\text{shift} = t\left(1 - \frac{1}{n}\right)$$

The shift is **in the direction of the incident light** (towards the observer).

**Example.** With $t = 1$ cm and $n = 1.5$:
$$\text{shift} = 1\left(1 - \frac{1}{1.5}\right) = \frac{0.5}{1.5} = \frac{1}{3} \text{ cm}$$
An object 5 cm away appears $5 - \tfrac13$ cm away.

### Board-exam question (3 marks)

**(a)** A convex lens forms an image at $v = 10$ cm. A glass slab ($t = 3$ cm, $n = 1.5$) is placed between the lens and the image. Where is the image now?
$$\text{shift} = 3\left(1 - \frac{1}{1.5}\right) = 1 \text{ cm}$$
The shift is along the light, away from the lens. So $v = 10 + 1 = 11$ cm, and the screen must be moved to 11 cm.

**(b)** The same slab is placed between an object (10 cm from the lens) and the lens. The object appears shifted 1 cm towards the lens, to O′. So the lens "sees" $u = 10 - 1 = 9$ cm, and $v$ follows from the lens formula with that $u$.

## Atmospheric refraction (not in the current NCERT text)

Refraction by the Earth's atmosphere. The air is denser, with a higher refractive index, near the ground and rarer higher up.

**1. Advance sunrise and delayed sunset (by about 2 minutes each).**

- When the Sun is just below the horizon, its rays enter the atmosphere going from rarer to denser layers and bend **towards the normal**, curving round towards the Earth.
- An observer sees the Sun at its **apparent position**, above the horizon, while its **real position** is still below it.
- The apparent shift is about **½°**. The Earth turns 360° in 24 h, so ½° takes 2 minutes.
- The Sun is therefore seen 2 min before actual sunrise and 2 min after actual sunset: **about 4 minutes more daylight each day**.

**2. Twinkling of stars.**

- Starlight passes through layers of increasing refractive index on its way down and bends towards the normal again and again. The star is seen at an **apparent position slightly higher** than its real position.
- **The atmosphere is dynamic.** Its layers move, so their density and refractive index keep changing slightly, and the path of the star's light keeps changing.
- **Board text:** "Since atmosphere is dynamic it results in changes in density & refractive index of layers. This causes a change in path of rays coming from the star as they pass through them. Thus sometimes more rays fall upon the eye of the observer & star appears brighter, & sometimes only few rays reach the eye & it appears fainter. Thus star appears twinkling."

---
*Note on this lecture's transcript:* `gemini-3.5-flash` was in a 503 outage and then out of daily quota when this chapter was processed, so the audio was transcribed by `gemini-3.5-flash-lite` in overlapping five-minute windows, joined where the overlapping speech matches word for word. Lite's clock ran fast (by up to 2x) inside a window; each window was rescaled to its true length, so times quoted here are approximate (roughly ±30 s). Every gap of more than 30 s was re-transcribed on its own to confirm whether speech was missing. Equations are taken from the board frames, not from the transcript.
