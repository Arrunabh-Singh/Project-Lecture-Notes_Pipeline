# Electric Field Intensity, Field Lines, and the Point-Charge Field Formula

**NCERT sections covered:** 1.7, 1.8

## Electric field (NCERT 1.7)

**Concept:** the region around a charge where its effect (a force on another charge) can be felt -- directly analogous to the magnetic field around a magnet (felt by a test magnet, stronger effect closer in, negligible far away).

**Electric field intensity** $\vec E$ is the measurable version of this idea: the force per unit charge experienced by a very small ("test") positive charge $q_0$ placed at a point, in the limit $q_0\to0$ (small enough that it doesn't itself disturb the field being measured):
$$\vec E = \lim_{q_0\to0}\frac{\vec F}{q_0}$$
$\vec E$ is a **vector**, in the same direction as the force on a positive test charge. SI unit: **N/C**. Dimensional formula (from $F=ma$ and $Q=It$): $[E] = M^1L^1T^{-3}A^{-1}$.

### Electric field due to a point charge
Combining $\vec E=\vec F/q_0$ with Coulomb's law $F=\frac{1}{4\pi\varepsilon_0}\frac{Qq_0}{r^2}$:
$$\boxed{\vec E = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\hat r}$$
The $q_0$ cancels out — **$E$ is independent of the test charge used to probe it**, a property of the source charge and the field point alone.

**Graphing $E$ vs $r$:** an inverse-square curve (a "rectangular hyperbola" shape, same family as $PV=\text{const}$ or $xy=\text{const}$). To turn it into a straight line (standard technique, same idea as plotting $V$ vs $I$ for Ohm's law to read off $R$ as the slope): plot $E$ against $1/r^2$ — since $Er^2 = Q/4\pi\varepsilon_0 = \text{const}$, this gives a straight line through the origin.

**Worked numerical:** a charge of $2$ mC at point $O$ — find $E$ at $40$ cm from it:
$$E = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2} = \frac{9\times10^9\times2\times10^{-3}}{(40\times10^{-2})^2}~\text{N/C}$$

## Electric field lines (NCERT 1.8)

Imaginary curves such that the tangent at any point gives the direction of $\vec E$ there, and along which an isolated free positive test charge would tend to move (directly analogous to magnetic field lines, e.g. traced out by iron filings around a magnet). **Crowding** of field lines indicates a **stronger** field.

### Characteristics
1. Field lines **start on positive charges and terminate on negative charges**.
2. Field lines **never form closed loops** — this is the key difference from magnetic field lines, which *always* form closed loops (outside a magnet N$\to$S, inside S$\to$N). A field line running from one charge to a different charge (not back to itself) is not a closed loop, even if it looks curved.

### Patterns for common configurations
- **Isolated point charge:** lines radiate straight outward (for $+q$, terminating charge assumed at infinity) or straight inward (for $-q$, source charge assumed at infinity). A common mistake is drawing lines that curve/converge near the charge — for a true point charge they must be radially straight, never touching or crossing right at the charge.
- **Two like charges** (e.g. $+Q,+Q$ or $+2Q,+Q$): lines repel each other and bend away, never intersecting. A **null point** ($E=0$) exists between them, located **closer to the smaller-magnitude charge** — exactly at the midpoint if the charges are equal.
- **Two unlike charges** (e.g. $+Q,-Q$ or $+2Q,-Q$): lines run from positive to negative, curving toward each other — this is *not* a closed loop (each line terminates once, going from one distinct charge to the other, rather than returning to its own start). Asymmetric magnitudes get proportionally more lines drawn from the larger charge.

---
*Note on this lecture's transcript:* the quantitative point-charge field formula, the E-vs-r graph discussion, the worked numerical, and the independence-from-test-charge point are all grounded from board frames near the true end of the lecture -- the transcript loops back to earlier material there instead of covering them. See the flagged span below.


## Verify these spans
- [39:50–46:14] The transcript's real, non-repeated narration runs continuously and coherently from t=0 to about t=2390s, thoroughly covering the definition of E, field lines, and field-line patterns for point charges and charge pairs. From t=2390s to the transcript's nominal end (t=2771s) it then loops back and re-transcribes the earlier point-charge and like-charges field-line material nearly verbatim -- the same delayed-repetition ASR artifact found elsewhere in this chapter. Unlike some other cases, board frames here show this is NOT just wasted/lost time: floor_000131.jpg (t=2600s) and floor_000138.jpg (t=2740s, the last captured frame, well within the true 2774.87s duration) show substantial genuinely new material -- the quantitative point-charge field formula E=(1/4 pi eps0)(Q/r^2) boxed 'by definition', an E-vs-r graph-linearisation discussion, a worked numerical (2 mC charge, field at 40cm), and a conceptual aside confirming E is independent of the test charge -- none of which appears anywhere in the transcript. The four point-charge-formula/numerical claims above are grounded entirely from these two board frames.