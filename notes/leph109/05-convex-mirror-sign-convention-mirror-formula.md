# Convex Mirror Images, Sign Convention and the Mirror Formula

**NCERT sections covered:** 9.2.1, 9.2.3


## Images formed by a convex mirror (NCERT 9.2.3)

A convex mirror has only two cases.

| Position of object | Position of image | Nature and size |
|---|---|---|
| At infinity | At F, behind the mirror | Virtual, erect, **highly diminished** |
| Anywhere between infinity and P | Between P and F, behind the mirror | Virtual, erect, **diminished** |

The parallel rays from an object at infinity reflect so that they *appear* to come from F. Draw the backward extensions dashed. Wherever the object is, a convex mirror's image is always **virtual, erect and smaller** than the object. (In the recording the teacher twice says "convex lens" while drawing the mirror, and once calls the outside car mirror "concave". The board and the argument are about a **convex mirror** both times.)

## Why convex mirrors are used as rear-view mirrors

This is a common exam question. The mirror outside the driver's door bulges outwards, so it is a convex mirror. There are two reasons:

1. **The image is always erect.** The driver never sees a car or a person upside down.
2. **It gives a wider field of view.** Because it curves outwards, rays from objects at large angles behind the car still reflect into the driver's eye. The images are small, so a **large area behind is covered** in one small mirror.

With a plane mirror only rays within a narrow angle reach the eye, so the field of view is smaller. A concave mirror narrows it further. The convex mirror gives the widest view. *(Rear-view mirrors are not discussed in the current NCERT Class 12 text.)*

## New Cartesian sign convention (NCERT 9.2.1)

For an object AB in front of a mirror with image A′B′:
- **object distance** $u = PA$ (distance of the object from the pole)
- **image distance** $v = PA'$
- **focal length** $f = PF$, **radius of curvature** $R = PC$

**Rules**
1. **All distances are measured from the pole.** Write PA, PA′, PF, never AP, A′P or FP.
2. Distances measured **in the direction of the incident ray are positive**. Distances measured **opposite to it are negative**. Draw the incident light travelling left to right.
3. Heights measured **above the principal axis are positive**, and heights **below are negative**.

| | $u$ | $v$ | $f$ | $R$ |
|---|---|---|---|---|
| Concave mirror (real image) | − | − | − | − |
| Convex mirror | − | + | + | + |

The object height $h$ (AB, measured upwards) is positive. An inverted real image A′B′ is below the axis, so its height is negative. The erect virtual image of a convex mirror has a positive height.

*Memory hook from the lecture:* "con**vex**" gives a **positive** focal length, and "con**cave**" a **negative** one. This holds for lenses too. The hook is only for the sign of $f$.

## Mirror formula and magnification (NCERT 9.2.3)

The **mirror formula** relates the image distance, object distance and focal length:

$$\frac{1}{f} = \frac{1}{v} + \frac{1}{u}$$

**Magnification** $m$ is the ratio of the image height to the object height:

$$m = \frac{h_i}{h_o} = -\frac{v}{u}$$

(Both are to be remembered here; they are derived in lecture 09.)

**Reading $m$:** the **sign** tells you real or virtual, and the **magnitude** tells you the size.
- $m > 0$: virtual and erect. $m < 0$: real and inverted.
- $|m| < 1$: smaller. $|m| = 1$: same size. $|m| > 1$: magnified.

| $m$ | Image |
|---|---|
| $+2$ | magnified, erect, virtual |
| $+0.2$ | smaller, erect, virtual |
| $-3$ | magnified, real, inverted |
| $-0.3$ | smaller, real, inverted |

A common mistake is to read "+" as magnified and "−" as diminished. The sign only says virtual/erect or real/inverted.

## Numericals (textbook exercise questions 12–15, solved on the board)

**Q12.** An object is 10 cm from a convex mirror of focal length 15 cm. Find the position and nature of the image.
$u = -10$ cm, $f = +15$ cm.
$$\frac{1}{v} = \frac{1}{f} - \frac{1}{u} = \frac{1}{15} + \frac{1}{10} = \frac{1}{6} \;\Rightarrow\; v = +6 \text{ cm}$$
The image is 6 cm **behind** the mirror, so it is virtual and erect. $m = -v/u = -\dfrac{6}{-10} = +0.6$: virtual, erect, smaller. *(The teacher first writes $m = -0.6$, then notices that $u$ is $-10$ and corrects it to $+0.6$.)*

**Q13.** A plane mirror's magnification is $+1$. The "+" means virtual and erect, and the "1" means the same size.

**Q14.** An object 5.0 cm long is 20 cm in front of a convex mirror of radius of curvature 30 cm.
$h_o = +5$ cm, $u = -20$ cm, $R = +30$ cm, so $f = R/2 = +15$ cm.
$$\frac{1}{v} = \frac{1}{15} + \frac{1}{20} = \frac{7}{60} \;\Rightarrow\; v = +\frac{60}{7} \approx +8.6 \text{ cm}$$
The image is behind the mirror, so it is virtual and erect. $m = -v/u = +\dfrac{3}{7}$, so it is smaller. Its height is $h_i = m\,h_o = \dfrac{15}{7} \approx 2.1$ cm.

**Q15.** An object 7.0 cm tall is 27 cm in front of a concave mirror of focal length 18 cm. Where should the screen be placed for a sharp image?
$h_o = +7$ cm, $u = -27$ cm, $f = -18$ cm.
$$\frac{1}{v} = -\frac{1}{18} + \frac{1}{27} = \frac{18 - 27}{27 \times 18} = -\frac{1}{54} \;\Rightarrow\; v = -54 \text{ cm}$$
The negative $v$ means the image is **in front of** the mirror, so it is real and inverted. Place the screen 54 cm in front of the mirror. $m = -v/u = -2$: real, inverted, magnified. $h_i = m\,h_o = -14$ cm (the minus means inverted).

Rule of thumb from the lecture: an image formed in front of the mirror is real and inverted, and one formed behind it is virtual and erect.

---
*Note on this lecture's transcript:* `gemini-3.5-flash` was in a 503 outage and then out of daily quota when this chapter was processed, so the audio was transcribed by `gemini-3.5-flash-lite` in overlapping five-minute windows, joined where the overlapping speech matches word for word. Lite's clock ran fast (by up to 2x) inside a window; each window was rescaled to its true length, so times quoted here are approximate (roughly ±30 s). Every gap of more than 30 s was re-transcribed on its own to confirm whether speech was missing. The rear-view-mirror passage (about 03:48–04:51) was missing from the merged windows and was spliced in from a separate transcription of that stretch. Equations are taken from the board frames, not from the transcript.


## Verify these spans
- [08:00–08:45] Segment times collapse here (several stamped 08:12) in the plane- vs concave-mirror field-of-view comparison; the text reads in order but its times are rough.