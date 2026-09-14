# Magnetic Field on the Axis of a Coil, and Ampere's Circuital Law

**NCERT sections covered:** 4.5, 4.6

## Magnetic field on the axis of a circular current loop (NCERT 4.5)
Building on the previous lecture's centre-of-coil result, this lecture derives the field at a general point $P$ on the **axis** of a circular loop of radius $R$ carrying current $I$, at distance $x$ from the centre $O$.

**Setup.** A current element $I\,d\vec l$ at point $A$ on the loop is at distance $r$ from $P$. Since the loop lies in a plane through $O$ perpendicular to the axis, $d\vec l$ and the displacement vector $\vec r$ (from the element to $P$) are (very nearly) perpendicular, so $\sin\theta \approx 1$ and the Biot-Savart law gives
$$dB = \frac{\mu_0}{4\pi}\frac{I\,dl}{r^2}$$
$d\vec B$ is perpendicular to the plane containing $d\vec l$ and $\vec r$, and can be resolved into a component $dB\sin\alpha$ along the axis and $dB\cos\alpha$ perpendicular to it, where $\alpha$ is the angle between $\vec r$ and the axis.

**Symmetry argument.** For every element, the diametrically opposite element (same distance $r$, same $\alpha$) produces a field whose perpendicular component is equal and opposite -- so all perpendicular ($\cos\alpha$) components cancel around the full loop, while the axial ($\sin\alpha$) components all add. Hence the net field lies entirely along the axis:
$$B = \oint dB\sin\alpha$$

**Completing the integral.** Using $\sin\alpha = R/r$ and $r=(R^2+x^2)^{1/2}$ (Pythagoras), and $\oint dl = 2\pi R$:
$$B = \frac{\mu_0}{4\pi}\frac{I}{r^2}\cdot\frac{R}{r}\cdot 2\pi R = \frac{\mu_0}{4\pi}\frac{I\,(2\pi R)\,R}{(R^2+x^2)^{3/2}}$$
$$\boxed{B = \frac{\mu_0\, I\, R^2}{2\,(R^2+x^2)^{3/2}}}$$
Setting $x=0$ recovers $B=\dfrac{\mu_0 I}{2R}$, matching the direct centre-of-coil derivation from the previous lecture -- exactly the check NCERT itself makes in Sec. 4.5.

## Ampere's Circuital Law and its first application (NCERT 4.6)
*(This entire section is grounded from board frames only -- the transcript does not narrate it. See the flagged span below for why, and the strong corroborating evidence from the very next lecture.)*

**Statement.** The line integral of the magnetic field along the boundary of any closed path (an "Amperian loop") equals $\mu_0$ times the net current enclosed by that path:
$$\oint \vec B \cdot d\vec l = \mu_0 I_e$$

**Application: infinitely long straight current-carrying wire.** Take a circular Amperian loop of radius $r$ centred on the wire. By symmetry $B$ is constant in magnitude on the loop and everywhere tangential to it (parallel to $d\vec l$, so $\vec B\cdot d\vec l = B\,dl$):
$$\oint \vec B\cdot d\vec l = B\oint dl = B(2\pi r) = \mu_0 I \quad\Rightarrow\quad \boxed{B = \frac{\mu_0 I}{2\pi r}}$$
This is the same result NCERT reaches via Ampere's law in Sec. 4.6 (Eq. 4.14).

**Finite-wire generalisation.** For a straight wire of finite length, with $P$ at perpendicular distance $r$ and the two ends subtending angles $\alpha_1,\alpha_2$ at $P$:
$$B = \frac{\mu_0 I}{4\pi r}\left(\sin\alpha_1 + \sin\alpha_2\right)$$
As the wire becomes infinite, $\alpha_1,\alpha_2 \to 90^\circ$, so $\sin\alpha_1+\sin\alpha_2\to 2$ and the formula correctly reduces to $B=\dfrac{\mu_0 I}{2\pi r}$ -- the board explicitly checks this consistency between the Biot-Savart (finite-wire) and Ampere's-law (infinite-wire) results.


## Verify these spans
- [15:40–23:29] This lecture's filename promises both 'B at axis of coil' AND 'Ampere circuital law', but the transcript (85 segments, clean coverage ratio 1.012, zero flagged near-duplicate pairs from the delayed-repetition scan) never once mentions Ampere, 'circuital', or an enclosed/boundary current -- every single segment, right up to the last one ending at 1426.7s, narrates only the on-axis-of-a-coil derivation (culminating in the x=0 sanity check against the earlier centre-of-coil result). Board frames tell a different story: by t=940s (floor_000048) the page has already turned to a heading 'Ampere circuital law:'; by t=1040s (floor_000053) the full boxed statement (closed-loop integral of B.dl = mu0*I_e) is written; and by t=1240-1380s (floor_000063/67/70, still comfortably inside the true 1409.8s duration) a complete first application -- straight-wire Amperian loop giving B=mu0*I/(2*pi*r), plus the finite-wire generalisation B=(mu0*I/4*pi*r)(sin a1+sin a2) checked against the infinite-wire limit -- is fully worked out with diagrams. This is corroborated independently by the very next lecture in this chapter (file 1xP2VppJSiqby6nk4Gys--lX5GeM1TGNg, 'Solenoid and toroid'), whose transcript opens mid-thought with 'let us try to see the SECOND application of your ampere circuital law that is magnetic field due to a solenoid' -- confirming a first application (straight wire, via Ampere's law) really was taught, immediately before that. So the real audio almost certainly does contain the Ampere's-law statement and straight-wire derivation somewhere in this lecture's second half; the ASR simply never transcribes it, instead only ever narrating the coil-axis algebra, all the way to the true duration boundary. Neither the coverage check nor the adjacent/delayed-duplicate detectors catch this, because nothing is fabricated or repeated -- real content is silently missing rather than replaced by a copy. All three Ampere's-law claims above are grounded from board frames (and the lecture-3 cross-reference) alone, with no transcript span.