# Inductor, Self Inductance of a Solenoid, Energy Stored, and Intro to Mutual Induction

**NCERT sections covered:** 6.7

## Ideal resistor vs. ideal inductor; self-inductance of a solenoid (NCERT 6.7)

An **ideal resistor** has zero self-inductance; an **ideal inductor** has zero resistance and high self-inductance. An inductor is a tightly wound coil of insulated wire. (Real components are never perfectly ideal.)

### Self-inductance of a solenoid
Solenoid: length $L$, $n$ turns per unit length ($N=nL$ total turns), area $A$, current $I$. Using $B=\mu_0 nI$ (Ampere's law) and flux per turn $\phi=BA$:
$$\phi_\text{total} = N\phi = N A B = (nL)(A)(\mu_0 nI) = \mu_0 n^2 A L\, I$$
Since $\phi_\text{total}=LI$:
$$\boxed{L = \mu_0 n^2 A L}$$
With a magnetic core of relative permeability $\mu_r$: $L=\mu_0\mu_r n^2 A L$ (bigger $L$ opposes current more strongly).

## Energy stored in an inductor

Charging current against the back EMF does work: $dW = E\,dq$. With $E=L\,dI/dt$ and $dq=I\,dt$: $dW = LI\,dI$. Integrating from $0$ to $I$:
$$\boxed{U_M = \frac{1}{2}LI^2 = \frac{1}{2}\phi I}$$

### Energy density (energy per unit volume)
$$u = \frac{U_M}{\text{Volume}} = \frac{\frac12 LI^2}{AL}$$
Substituting $\phi=NAB$, $L=\phi/I$, and $B=\mu_0 nI$ (so $nI=B/\mu_0$), this simplifies to the standard result:
$$\boxed{u = \frac{B^2}{2\mu_0}}$$

## Mutual induction (intro)

**Phenomenon:** inducing a current in a nearby coil (secondary, $S$) due to a changing current in another coil (primary, $P$). Coefficient of mutual induction:
$$\phi_S \propto I_P$$

**Demo:** AC-driven primary coil $A$; secondary coil $B$ with a bulb lights up due to mutual induction. Moving $B$ further from $A$ dims the bulb — flux linking $B$ decreases with separation.

---
*Note on this lecture's transcript:* the derivation of energy density is cut off mid-algebra right at the transcript's own final words, and the introduction to mutual induction (this lecture's own third named topic) never appears in the transcript at all. Both are completed/grounded from a board frame; see the flagged span below.


## Verify these spans
- [20:12–22:12] The transcript's own words are still working through the algebra of the energy-per-unit-volume derivation right up to its very last segment ('I want my answer... I want basically B, I don't want to eliminate B because at the back of the mind I want to prove that this energy per unit volume...'), cutting off before ever stating the final result or reaching mutual induction at all. However, a board frame (floor_000061.jpg) -- whose true video timestamp (t=1200s) falls BEFORE the transcript's own self-reported final segment (which claims to start at t=1336s, already past the video's true 1332.03s duration) -- shows mutual induction already introduced in full: its definition, the coefficient of mutual induction (phi_S proportional to I_P), and a primary/secondary coil demonstration with a bulb. This confirms the transcript's own timestamps drifted later than real video time by the end of the lecture. The final energy-density result (u=B^2/2*mu0) is the direct, expected algebraic completion of the transcript's own work and is standard NCERT content; the mutual-induction claims are grounded entirely from the frame, not the transcript's own words.