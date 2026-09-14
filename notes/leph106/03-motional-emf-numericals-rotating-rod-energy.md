# Motional EMF: Polarity, Numericals, Rotating Rod, and Energy Consideration

**NCERT sections covered:** 6.6

## Motional EMF: polarity, and worked numericals (NCERT 6.6)

**Finding polarity:** for a rod moving with velocity $v$ through field $B$, using $\vec F=q\vec v\times\vec B$ on the rod's free charges, positive charge accumulates at one end and negative at the other, until the resulting internal electric field balances the magnetic force ($F_E=F_M$ at equilibrium). The rod then behaves like a fictitious battery — no battery is actually present, only charge separation.

### Worked numerical: jet plane in Earth's field
A jet, wingspan $l=25$ m, flies west at $v=1800$ km/hr. Only Earth's **horizontal** field component $B_H$ matters (the vertical component $B_V$ is parallel to $l$, so contributes nothing — $v$, $l$, $B$ must all be mutually perpendicular). With $B=5\times10^{-4}$ T, dip angle $\delta=30°$:
$$B_H = B\cos\delta = 5\times10^{-4}\times\frac{\sqrt3}{2}$$
$$\varepsilon = B_H\, l\, v \qquad (v \text{ in m/s, via} \times 5/18)$$
Polarity found the same way as above via $\vec F=q\vec v\times\vec B$.

## EMF from a rotating conductor

A rod of length $l$, hinged at the centre and free at the other end, rotates with angular velocity $\omega$ in a uniform field $B$ parallel to the rotation axis:
$$\boxed{\varepsilon = \frac{1}{2}B\omega l^2}$$

**Worked numerical:** rod length $1$ m, rotated at $50$ rev/s, hinged at the centre of a ring of radius $1$ m, $B=1$ T parallel to the axis. $\omega=2\pi\nu=2\pi(50)$ rad/s:
$$\varepsilon = \frac{1}{2}(1)(2\pi\times50)(1)^2 = 50\pi~\text{V}$$

**Second numerical (setup):** a wheel with $10$ metallic spokes, each $0.5$ m long, rotated at $120$ rev/min in a plane normal to Earth's horizontal field $H_E=0.4$ gauss.

## Energy consideration in motional EMF (NCERT 6.6)

Conducting rod $ab$ (length $l$) slides with velocity $v$ on rails, closed through resistance $R$, in field $B$:
$$\varepsilon = Blv, \qquad i = \frac{Blv}{R}$$
Magnetic force on the current-carrying rod, opposing $v$ (Lenz's law / Fleming's left-hand rule):
$$F_m = BIl = \frac{B^2l^2v}{R}$$
To keep the rod moving at **constant velocity**, an equal and opposite applied force $F=B^2l^2v/R$ is needed. Rate of work done by this applied force:
$$P_\text{applied} = Fv = \frac{B^2l^2v^2}{R}$$
Rate of electrical energy dissipated in the circuit:
$$P_\text{dissipated} = I^2R = \left(\frac{Blv}{R}\right)^2 R = \frac{B^2l^2v^2}{R}$$
$$\boxed{P_\text{applied} = P_\text{dissipated}}$$
confirming energy conservation: mechanical work done pushing the rod converts exactly into dissipated electrical energy.

---
*Note on this lecture's transcript:* the jet-plane numerical is transcribed correctly once, then repeated nearly verbatim a second time, which drifted the transcript's own self-reported timestamps well behind real video time. As a result, three major topics that the board confirms were fully taught within the true ~1958s runtime — the completed rotating-rod derivation and its two numericals, and the entire "energy consideration" topic (this lecture's own second named topic) — never appear in the transcript's own words at all. All are grounded entirely from frames; see the flagged spans below.


## Verify these spans
- [10:54–29:35] The jet-plane numerical (motional EMF, Earth's field) is transcribed correctly once (~t=654-1226s), but the ASR then re-transcribes essentially the same explanation nearly verbatim a second time (~t=1226-1775s) -- the same delayed-repetition pattern found repeatedly in this chapter's and Ch5's lectures. Board frames show that by real video time t=1260s the class has already finished this numerical AND completed the rotating-rod EMF derivation (epsilon=(1/2)*B*omega*l^2) plus solved a full worked numerical on it (metallic rod, 50 rev/s, giving 50*pi V) and started a second one (wheel with 10 spokes) -- meaning the transcript's self-reported timestamps for its second half are significantly drifted later than real video time due to this internal duplication. The rotating-rod claims above are grounded from frames rather than the transcript's own words, since the transcript (in its own, drifted timeline) only reaches the point of setting up the rotating-conductor problem before cutting off.
- [29:35–32:38] The transcript's own words never get past setting up the rotating-rod problem (its last segment describes the rod and asks for the EMF between a and b, without deriving or solving it). Board frames, however, show that -- likely well within the true 1958s runtime, given the timestamp drift documented above -- the class not only completes the rotating-rod derivation and two numericals but goes on to a full 'Energy consideration in motional EMF' derivation (floor_000079.jpg, floor_000096.jpg): the magnetic braking force on the rod, the applied force needed to sustain constant velocity, and the equality of applied mechanical power and dissipated electrical power. This entire topic -- named directly in this lecture's own filename ('numericals, energy consideration') -- is completely absent from the transcript's own words and is grounded here entirely from frames.