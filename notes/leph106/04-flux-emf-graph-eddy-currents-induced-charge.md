# Flux/EMF Graph Numerical, Induced Charge, Induced Electric Field, Eddy Currents

**NCERT sections covered:** 6.4, 6.5, 6.6, 6.8

## Worked numerical: flux, EMF, force, and power vs. distance (NCERT 6.4)

Classic NCERT-style problem: the arm PQ of a rectangular conductor is moved from $x=0$ outwards. A uniform field $B$ is perpendicular to the plane, present for $0\le x\le b$ and zero for $x>b$; only PQ (length $l$) has resistance $r$. PQ is pulled from $x=0$ to $x=2b$, then back to $x=0$, at constant speed $v$.

| Quantity | $0\le x<b$ | $b\le x<2b$ |
|---|---|---|
| Flux $\phi$ | $Blx$ (linear) | $Blb$ (constant) |
| EMF $\varepsilon=-d\phi/dt$ | $-Blv$ | $0$ |
| Force to pull PQ | $F=I l B=\dfrac{B^2l^2v}{r}$ | $0$ |
| Power dissipated | $P=I^2r=\dfrac{B^2l^2v^2}{r}$ | $0$ |

(Same pattern retraces, sign-flipped, on the return trip from $2b$ back to $0$.)

## Induced charge is independent of time (NCERT 6.4)

From $\varepsilon=-N\dfrac{d\phi}{dt}$ and $I=\varepsilon/R$: charge in a small interval $dt$ is $dq = I\,dt = \dfrac{N}{R}d\phi$. Over a finite interval:
$$\boxed{q = \frac{N}{R}\,\Delta\phi}$$
The time interval cancels out completely — induced charge depends only on $N$, $R$, and the *total* flux change, never on how fast it happens.

## Induced electric field (NCERT 6.4)

Unlike an **electrostatic** field (conservative: $\oint\vec E\cdot d\vec l=0$), an **induced** electric field arises from a time-varying $B$ and is **non-conservative**: $\oint\vec E\cdot d\vec l = -\dfrac{d\phi}{dt} \ne 0$.

## Eddy (Foucault) currents (NCERT 6.5)

**Definition:** induced circulating currents produced *within* a metal itself, due to a change in flux linked with the metal; direction given by Lenz's law.

- **Damping example:** a metal plate oscillating in/out of a field comes to rest quickly — eddy currents oppose the motion. Slotting the plate lengthens the current path (more resistance, less current), reducing damping.
- **Jumping ring/disc:** an AC-driven coil induces eddy currents in a nearby disc; by Lenz's law the induced pole repels the coil's pole, making the disc jump.
- **Falling magnet in a tube:** dropping a magnet through a copper tube vs. a plastic tube of the same length — eddy currents in the copper brake the fall ($a<g$), while the plastic tube (non-conductive, no eddy currents) lets it fall freely ($a=g$).
- **Disadvantages:** energy loss as heat; unwanted damping.
- **Applications:** induction furnaces, speedometers, dead-beat galvanometers, electric braking (e.g. trains).

## Third way to induce EMF: changing coil orientation (NCERT 6.8, intro to AC generator)

$$\phi = AB\cos\theta$$
where $\theta$ is the angle between the coil's area vector $\hat n$ and $\vec B$. With $\theta=\omega t$:
$$\phi = AB\cos(\omega t), \qquad \varepsilon = -\frac{d\phi}{dt} = AB\omega\sin(\omega t)$$
For an $N$-turn coil: $\varepsilon = NAB\omega\sin(\omega t)$ — the sinusoidal EMF of an **AC generator**.

---
*Note on this lecture's transcript:* the numerical's force and power parts (announced at the start but never narrated), the conclusion of the falling-magnet demonstration (cut off mid-sentence), and the final step of the AC-generator derivation are all grounded from board frames rather than the transcript's own words. See the flagged spans below.


## Verify these spans
- [00:45–10:05] At the very start of this numerical (t=29s), the transcript explicitly announces that FOUR quantities will be found: flux, EMF, force, and power. The transcript's actual narration, however, only ever works through flux and EMF (with their graphs) before moving on (at t=605s) to a completely different topic (proving induced charge is independent of time interval) -- the force and power parts are never spoken at all. A board frame (floor_000030.jpg, t=580s -- chronologically before even the transcript's own EMF-graph discussion concludes) shows the complete solution already written for all four parts, including force (F=B^2l^2v/r) and power (P=B^2l^2v^2/r) with their own graphs vs. x. The force and power claims above are grounded entirely from this frame, not the transcript's own words.
- [29:40–30:07] The transcript describes a falling-magnet demonstration (dropping a magnet through a copper pipe vs. a plastic pipe of the same length, to see which one it exits first) but cuts off mid-sentence ('when it is coming down...') right as it should explain the actual physical conclusion, then abruptly jumps to a new topic ('advantages and disadvantages of eddy currents') with an out-of-order timestamp (the next segment's reported start, 1800s, is earlier than the cut-off segment's own start of 1801s) -- suggesting a dropped/skipped segment rather than a natural transition. A board frame (floor_000092.jpg) shows the resolution: the copper-tube magnet falls with a<g (eddy-current braking) while the plastic-tube magnet falls with a=g (free fall, no eddy currents possible in a non-conductor). This conclusion is grounded entirely from the frame.
- [34:33–36:28] The transcript's own words, in their final segments, introduce flux=AB*cos(theta) and identify theta as the angle between the area vector and B, but never reach the point of substituting theta=omega*t or taking the derivative to get the sinusoidal EMF form. A board frame (floor_000105.jpg) shows this next step already written (phi=AB cos(omega t), epsilon=-dphi/dt, with the derivative rule for cos(omega t) noted alongside) -- the direct, expected continuation of what the transcript itself sets up. The final AC-generator EMF formula claim above is grounded from this frame rather than the transcript's own words.