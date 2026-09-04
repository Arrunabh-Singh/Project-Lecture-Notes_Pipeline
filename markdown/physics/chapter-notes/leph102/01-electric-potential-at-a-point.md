# Electric Potential: Definition, Relation to Field, Potential Due to a Point Charge and a System of Charges

**NCERT sections covered:** 2.2, 2.3, 2.5

## Electric potential

### Definition (NCERT 2.2)
Building on electric field intensity (force-based, from the previous chapter), this lecture switches to a work-based description.

**Electric potential difference:**
$$V_A - V_B = \frac{W_{B \to A}}{q_0}$$
the work done by an *external* force per unit charge in moving a test charge from $B$ to $A$, **without acceleration** -- meaning the external force exactly balances the electric force at every point along the path, so the process is quasi-static and no kinetic energy is gained or lost.

**Unit:** $1~\text{volt} = 1~\text{joule/coulomb}$.

**Electric potential at a point** (not just a difference) is the special case where the charge is brought from infinity, with the convention $V(\infty) = 0$:
$$V = \frac{W_{\infty \to P}}{q_0}$$

**Physical significance:** a positive charge moves from high to low potential; a negative charge moves from low to high potential -- the electrical analogue of water flowing from high to low level, or heat flowing from hot to cold.

### Potential as a line integral of the field
$$V = -\int_B^A \vec{E}\cdot d\vec{l}$$
Derived from $dW = -q_0\vec{E}\cdot d\vec{l}$ (external force is equal and opposite to the electric force) and $V = W/q_0$. Called out in the lecture as a must-know result ("your 2 AM formula").

**Corollary -- the electrostatic field is conservative:**
$$\oint \vec{E}\cdot d\vec{l} = 0$$
Any closed-loop line integral of $\vec E$ vanishes, since the potential difference between two points doesn't depend on the path taken between them.

### Potential due to a point charge (NCERT 2.3)
$$V(r) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}$$
Falls off as $1/r$ (compare to $E \propto 1/r^2$).

### Potential due to a system of charges (NCERT 2.5)
Potential obeys superposition -- being a **scalar**, it's a plain sum (no vector addition needed, unlike $\vec E$):
$$V_P = \frac{1}{4\pi\varepsilon_0}\sum_i \frac{q_i}{r_i}$$
with each $q_i$ carrying its own sign.

**Worked example:** at the point $P$ midway between a $+q$ and a $-q$ charge (equidistant, distance $r$ from each):
$$V_P = \frac{1}{4\pi\varepsilon_0}\frac{q}{r} - \frac{1}{4\pi\varepsilon_0}\frac{q}{r} = 0$$
even though $\vec E \ne 0$ at that point. This is the key conceptual takeaway of the section: **potential and field are not simply proportional point-by-point** -- $V=0$ at a point says nothing about whether $E=0$ there, and vice versa.

---
*Note on this lecture's transcript:* the segment covering the point-charge and system-of-charges derivations (roughly the last 2 minutes of the lecture) is not reliable in the ASR transcript -- see the flagged span below. Those claims above are grounded directly in the board frames instead.


## Verify these spans
- [37:15–39:15] Transcript is unreliable here: instead of transcribing the real content actually on the board in this window (potential due to a point charge, then due to a system of charges -- confirmed from frames at t=2140-2320s), the ASR output regresses to repeating the 'significance of potential / high-to-low potential' material from around t=1200s almost verbatim. This looks like a distinct ASR failure mode (content substitution rather than truncation or tail fabrication) -- the claims for this section are grounded entirely in the board frames, not the transcript.