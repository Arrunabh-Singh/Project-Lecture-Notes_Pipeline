# Recap of Refraction and TIR; the World as Seen by a Fish

**NCERT sections covered:** 9.3, 9.4, 9.4.1


## What this recording is

This 70-minute video is the teacher's unnumbered "Exp. for Lateral Displ., apparent depth, atmospheric refraction, TIR, Examples of TIR"; here it is numbered 14. It is **one continuous recording of the same lesson that lectures 10 and 13 were cut from**: the same words and the same board pages. Only its last seven minutes are new.

| Time in this video | Topic | Full notes |
|---|---|---|
| 00:00–06:00 | Lateral displacement in a glass slab, $d = t\sin(i - r)/\cos r$ | note 10 |
| 06:00–17:06 | Real and apparent depth, the fish and fisherman, master formula $d' = d\,n_\text{observer}/n_\text{medium}$, stacked layers | note 10 |
| 17:06–27:37 | Shift $t(1 - 1/n)$ due to a glass slab; the 3-mark board question | note 10 |
| 27:37–36:33 | Atmospheric refraction: advance sunrise and delayed sunset, twinkling of stars | note 10 |
| 36:33–44:04 | Total internal reflection, conditions, critical angle $\sin C = 1/n$ | note 13 |
| 44:04–56:18 | Applications: diamonds, optical fibres, total reflecting prisms | note 13 |
| 56:18–62:40 | Mirage and looming | note 13 |
| **62:40–70:00** | **World as seen by a fish** (below) | this note |

The recording runs a few seconds ahead of lecture 10 at its start. It also includes the opening of the TIR lesson, which lecture 13's file begins just after, and a fuller description of looming. In cold regions the air in contact with the sea is cooler and denser, with rarer air above, so a ship appears **hanging in the air**, an optical illusion.

## World as seen by a fish

**Light from under the water (principle of reversibility).**

- A bulb S at depth $h$ under water sends rays up to the surface.
- Rays meeting the surface at less than the critical angle $C$ escape.
- Rays beyond $C$ are totally internally reflected back into the water.
- So **only a circle of the surface is lit**: its edge is where the rays meet the surface at exactly $C$.

From the right triangle with the bulb at depth $h$ below the centre of the circle:
$$\tan C = \frac{r}{h} \;\Rightarrow\; r = h\tan C \qquad (r \propto h)$$

**What the fish sees.** Run the rays the other way:

- Light from objects outside reaches the fish only through that circle.
- Even rays **grazing the air–water interface**, from objects near the surface at the horizon, enter the water and bend towards the normal.
- They reach the fish's eye at the critical angle $C$.

For water, $n = 1.33$ gives $C \approx 49°$, so (board):

> The rays grazing the air–water interface, starting from objects near the surface, enter water and reach the eye of the fish making critical angle $C = 49°$ and become visible to the fish. To a fish the outside region is symmetrical. The whole outside world appears to it within a cone of apex angle $2C = 98°$. The radius $r$ on the surface is $r = h\tan C$, $r \propto h$.

So the Sun, trees, people on the bank, everything above the water, is squeezed into a cone of apex angle about 98° above the fish. Divers looking up see the same thing: **a bright circular window** of sunlight, with the rest of the surface looking dark or mirror-like.

**Formula for numericals.**

- $\sin C = \dfrac{1}{n}$, so $\cos^2 C = 1 - \sin^2 C = 1 - \dfrac{1}{n^2} = \dfrac{n^2 - 1}{n^2}$.
- Therefore $\tan C = \dfrac{\sin C}{\cos C} = \dfrac{1}{\sqrt{n^2 - 1}}$.

$$r = h\tan C = \frac{h}{\sqrt{n^2 - 1}}$$

*(Check with water: $\sqrt{1.33^2 - 1} \approx 0.88$, so $r \approx 1.14\,h$, which matches $\tan 49° \approx 1.15$.)*

---
*Note on this lecture's transcript:* `gemini-3.5-flash` was in a 503 outage and then out of daily quota when this chapter was processed, so the audio was transcribed by `gemini-3.5-flash-lite` in overlapping five-minute windows, joined where the overlapping speech matches word for word. Lite's clock ran fast (by up to 2x) inside a window; each window was rescaled to its true length, so times quoted here are approximate (roughly ±30 s). Every gap of more than 30 s was re-transcribed on its own to confirm whether speech was missing. One stretch of the TIR section (about 39:08–40:00) was missing from the merged windows and was spliced in from a separate transcription. Equations are taken from the board frames, not from the transcript.
