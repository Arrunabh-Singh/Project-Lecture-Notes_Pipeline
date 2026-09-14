# Self Induction (Inertia of Electricity) and Self Inductance

**NCERT sections covered:** 6.7

## Self induction: inertia of electricity (NCERT 6.7)

When a coil is switched on, current takes time to rise to its maximum value rather than jumping instantly: the changing current produces changing flux through the coil itself, inducing a **back EMF** (by Lenz's law) that opposes the current's growth. At switch-off, the coil similarly opposes the current's decay. This resistance to *any change* in its own current — analogous to mechanical inertia — is why self-induction is called the **inertia of electricity**.

**Definition:** self-induction is the property of a coil by virtue of which it opposes the growth or decay of current flowing through it.

### Conceptual example
Battery + key feed two parallel branches: inductor $L$ + bulb $B_1$, and resistor $R$ + bulb $B_2$.
- **On switch-close:** $L$ opposes current growth, $R$ doesn't $\Rightarrow$ $B_2$ glows **immediately**; $B_1$ brightens gradually.
- **On switch-open** (after both are steady): $L$ opposes the current's decrease $\Rightarrow$ $B_1$ glows **for longer**.

### Sparking and non-inductive winding
Rapid voltage change at switching ($0\to230$ V or back) induces a large EMF, ionizing the air gap at switch contacts $\Rightarrow$ a spark (why circuits should never be switched near a gas leak). Modern switches add a small resistor between contacts to reduce this. Household AC wires are **twisted** together so current in adjacent opposite-direction sections is equal and opposite, cancelling the magnetic field — a **non-inductive coil**, minimizing self-induction.

## Self-inductance $L$

Flux linked with a coil is proportional to current: $\phi \propto i \Rightarrow \phi = Li$, where $L$ is the **coefficient of self-induction** (self-inductance).

**Three equivalent definitions:**
1. Setting $i=1$ A: $L=\phi$ — flux linked with the coil per unit current.
2. From $e=-d\phi/dt = -d(Li)/dt$: $\boxed{e = -L\dfrac{di}{dt}}$
3. Setting $di/dt=1$ A/s: $L=e$ — the EMF induced per unit rate of change of current.

**Units:** $L=\phi/I \Rightarrow$ Wb/A $=$ **Henry (H)**; also $L=e/(di/dt)\Rightarrow$ V$\cdot$A$^{-1}\cdot$s. $1\text{ H} = 1\text{ V}\cdot\text{A}^{-1}\cdot\text{s} = 1\text{ Wb}\cdot\text{A}^{-1}$.
**Dimensional formula:** $[L] = [ML^2T^{-2}A^{-2}]$

---
*Note on this lecture's transcript:* this is one of the cleanest transcripts found in this chapter. The only gap is at the very end — the video cuts off just as a third phrasing of $L$'s definition is announced; that phrasing and the units/dimensional formula are grounded from a board frame just past the transcript's own last words.


## Verify these spans
- [24:14–24:14] The transcript's very last words are 'So, now let's try to define L' -- suggesting a third phrasing of the definition is about to be given, right as the video ends. A board frame (floor_000069.jpg) shows this third definition already written out (L=e when di/dt=1), along with the units of L (Wb/A = Henry; V.A^-1.s) and its dimensional formula [ML^2T^-2A^-2]. Since the transcript itself never speaks these words, the third-definition and units/dimensions claims above are grounded from the frame -- the direct, expected continuation of what the transcript's own final sentence announces.