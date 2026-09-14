# Continuous Charge Distribution (Linear, Surface, Volume), and Numericals on Placing a Third Charge

**NCERT sections covered:** 1.12

## Continuous charge distribution (NCERT 1.12)

For a continuous (non-point) charge distribution: break it into small elements, find the charge $dq$ on each, compute the small force $d\vec F$ on a test charge $q_0$ due to that element via Coulomb's law, then **integrate** over the whole distribution. (Analogy used in the lecture: once you know the cost *per* mango, you can price any quantity without asking again and again — same idea as knowing charge *per unit* length/area/volume.)

### Linear charge density (1-D)
For a wire, or a ring (whose charge lies along its circumference — a *length*, not an area):
$$\lambda = \frac{\text{total charge}}{\text{total length}} = \frac{dq}{dl} \quad\Rightarrow\quad dq = \lambda\,dl$$
Force on $q_0$ from an element $dl$ at distance $r$: $d\vec F = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{q_0\lambda\,dl}{r^2}\hat r$, and the total force is $\vec F = \int d\vec F$ over the whole length.

### Surface charge density (2-D)
For a charged plane sheet, or the surface of a metal solid/hollow sphere:
$$\sigma = \frac{\text{charge}}{\text{area}} = \frac{dq}{ds} \quad\Rightarrow\quad dq = \sigma\,ds$$
**Key point:** any charge given to a metal (conducting) solid sphere migrates entirely to its outer surface (area $4\pi r^2$) — so even though the sphere is a 3-D object, its charge distribution is *surface* (2-D), exactly like a hollow metal sphere.

### Volume charge density (3-D)
For a distribution that genuinely fills a volume:
$$\rho = \frac{\text{charge}}{\text{volume}} = \frac{dq}{dV} \quad\Rightarrow\quad dq = \rho\,dV,\qquad d\vec F = \frac{1}{4\pi\varepsilon_0 K}\frac{q_0\rho\,dV}{r^2}\hat r$$

## Numericals: placing a third charge for zero net force

### Two same-sign charges
$Q_1$ and $Q_2$ (worked case: $Q_2=2Q_1$) separated by $r$ — find where $Q_0$, placed **between** them, feels zero net force. Setting the two force magnitudes equal (distance $x$ from $Q_1$):
$$\frac{Q_1}{x^2} = \frac{Q_2}{(r-x)^2} \;\Rightarrow\; (r-x)^2 = 2x^2 \;\Rightarrow\; r-x=\sqrt2\,x \;\Rightarrow\; \boxed{x = \frac{r}{1+\sqrt2}}$$

### Two opposite-sign charges
$+2Q$ and $-Q$ separated by $r$. A charge $+Q_0$ placed **between** them feels both forces pushing it the *same* direction (repelled by $+2Q$, attracted toward $-Q$) — they can never cancel there. The zero-force point must lie **outside** the segment, beyond the smaller-magnitude charge ($-Q$). At distance $x$ beyond $-Q$:
$$\frac{1}{4\pi\varepsilon_0}\frac{2Q\,Q_0}{x^2} = \frac{1}{4\pi\varepsilon_0}\frac{Q\,Q_0}{(r+x)^2} \;\Rightarrow\; \boxed{x = \frac{r}{\sqrt2-1}}$$

**General technique for this type of problem:** first determine whether the null point can even exist *between* the charges (same sign → yes, between them; opposite sign → no, it's outside, on the far side of the weaker charge), *then* set up and solve the force-balance equation.

---
*Note on this lecture's transcript:* volume charge density and both worked numericals above are grounded entirely from board frames -- the transcript itself falls into a repeated loop of earlier material and never reaches any of this. See the flagged span below.


## Verify these spans
- [14:30–32:22] This lecture's transcript is unusually badly corrupted: after the surface-charge-density/metal-sphere material (ending around t=870s), the ASR falls into a repeating loop, re-transcribing the SAME linear/surface charge density content 3-4 times over with shifted timestamps (a delayed-repetition artifact matching the pattern found across this chapter's sibling chapters), all the way to the transcript's nominal end near t=1942s. As a result the transcript never once mentions volume charge density (rho) at all, and never mentions the lecture's own second named topic -- 'numerical on placing of third charge' -- anywhere. Board frames tell the real story: floor_000050.jpg (t=980s) shows all three charge-density types (linear, surface, volume) laid out together on one page, confirming volume charge density genuinely was covered (most likely in the real, un-transcribed audio around t=870-980s); frames from t=1120s through t=1900s (floor_000057, floor_000065-66, floor_000072-74, floor_000096) show at least two distinct fully-worked numericals on where to place a third charge for zero net force -- one for two same-sign charges (null point between them), one for two opposite-sign charges (null point outside the segment) -- spanning what is likely more than half of this lecture's real running time. The volume-charge-density claim and both numerical claims above are grounded entirely from board frames, not the transcript.