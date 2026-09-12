# Electromagnetic Induction

*Class XII CBSE Physics · Chapter 6 · 7 lectures, in order.*

*NCERT sections covered: 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8.*

*Transcribed from the teacher's recorded lectures and checked against the
board frames and the NCERT text. Equations are board-grounded; any span the
transcript could not resolve confidently is flagged in place.*

---

## Faraday and Henry's Experiments, Magnetic Flux, Faraday's Law

**NCERT sections covered:** 6.1, 6.2, 6.3, 6.4

### Motivation and setup (NCERT 6.1)
Oersted and Ampere had already shown that a moving charge (current) produces a magnetic field. Faraday and Henry's ~1830 experiments asked the converse question: can a magnetic field produce a current? The chapter's answer is yes -- **electromagnetic induction**.

### Magnetic flux (NCERT 6.3)
For a plane area $A$ sitting in a uniform field $\vec B$, with the area's normal at angle $\theta$ to $\vec B$:
$$\Phi_B = \vec A \cdot \vec B = BA\cos\theta$$
$\Phi_B$ is a **scalar**. SI unit: **weber** (Wb); since $\Phi_B = BA$, $\text{Wb} = \text{T}\cdot\text{m}^2$.

**Dimensional formula (board derivation, exam-technique aside, not itself an NCERT-numbered result):** using $B = \tau/(IA)$ from $\tau = MB\sin\theta$ (with $M=IA$), and $\tau$ in N·m:
$$[\Phi_B] = [M][A] = \left[\frac{N\cdot m}{A\cdot m^2}\right][m^2] = [M^1 L^2 T^{-2} A^{-1}]$$
(A short board loop repeats this sub-derivation once before continuing -- see flagged span below; it doesn't affect the final result.)

**Magnetic flux density:** $B = \Phi_B/A$, so $B$ can equivalently be expressed in Wb/m$^2$ as well as tesla.

### Faraday and Henry's experiments (NCERT 6.2)
Three experiments, each showing current is induced in a coil connected to a galvanometer (no battery in the coil circuit itself):

**Experiment 1.** A bar magnet is moved towards, then away from, a coil $C$ wired to a galvanometer $G$. A deflection appears only *while the magnet is moving* -- faster motion gives a larger deflection -- and the deflection reverses direction when the motion (or the facing pole) reverses. A stationary magnet, however close, gives zero deflection.

**Experiment 2.** The bar magnet is replaced by a second coil $C_2$ carrying a steady current from a battery (so $C_2$ itself has a magnetic field and plays the magnet's role). Moving $C_2$ towards/away from $C_1$ (or vice versa) reproduces exactly the same deflection behaviour as Experiment 1. This shows relative motion between the flux source and the coil is what matters, not that the source specifically be a permanent magnet.

**Experiment 3.** Both coils are now held **stationary**. $C_1$ is wired to a battery through a key $K$; $C_2$ to the galvanometer. Closing the key produces a brief deflection that decays to zero once the current in $C_1$ becomes steady; opening the key produces a brief deflection in the *opposite* direction. Inserting an iron rod through the coils strengthens the effect (it strengthens the coupling field).

**What ties the three together:** in every case, current is induced only when the magnetic flux linked with the coil is *changing* -- via relative motion in Experiments 1-2, or via the current (and hence field) switching on/off/settling in Experiment 3. A coil sitting in any steady flux, however large, shows no induced current.

### Faraday's Law of electromagnetic induction (NCERT 6.4)
*(Grounded from board frames -- see the flagged span below for what the transcript does instead over this stretch.)*

**First law (qualitative):** whenever the magnetic flux linked with a coil changes, an emf is induced in it.

**Second law (quantitative), as boarded:** the induced emf's magnitude is directly proportional to the rate of change of flux linkage:
$$|\varepsilon| = N\frac{d\Phi_B}{dt} \approx N\frac{\Delta\Phi_B}{\Delta t}, \qquad I = \frac{\varepsilon}{R} = \frac{N}{R}\frac{d\Phi_B}{dt}$$
This lecture boards the **magnitude-only** form -- NCERT's Eq. 6.4 carries a minus sign, $\varepsilon = -N\,d\Phi_B/dt$, whose direction is Lenz's law; that sign/direction is explicitly deferred to the next lecture ("#2 Lenz law and motional emf"), so treat this as the teacher intentionally splitting magnitude from direction across two lectures rather than a factual gap.

**Worked example 1 (board only):** flux through a 500-turn coil falls from $0.8$ Wb to $0$ in $0.02$ s.
$$|\varepsilon| = N\frac{d\Phi}{dt} = 500\times\frac{0-0.8}{0.02} = 20{,}000~\text{V} = 20~\text{kV}$$

**Worked example 2 (board only, unfinished at the recording's end):** a 100-turn coil of area $0.1~\text{m}^2$ sits in a field growing from $0$ to $4\times10^{-3}$ Wb/m$^2$ over $4$ s, after which the coil is reversed through $180°$.
$$\Phi_1 = BA\cos 0° = BA, \qquad \Phi_2 = BA\cos 180° = -BA, \qquad \Delta\Phi = \Phi_2-\Phi_1 = -2BA$$
The board was mid-substitution ($|\varepsilon| = 2BA/t = 2\times(4\times10^{-3})/\ldots$) when the frame set ends, so the final numeric answer isn't recoverable from the available material.

---
*Note on this lecture's transcript:* the ASR transcript covers Experiments 1-3 and the flux/dimensional-analysis material solidly, corroborated closely by the board. But it never reaches Faraday's Law by name, never states the quantitative $N\,d\Phi/dt$ form, and never transcribes either worked numerical -- even though all of that is written on the board well inside the verified 1386.6s duration, and is exactly the "...and law" this lecture's own filename promises. See the flagged span below for the full timeline and why the automated coverage/repetition checks didn't catch it.


### Verify these spans
- [04:43–05:46] Minor delayed-duplicate: the flagged pair-scan catches segments 22-26 (283.9-312.8s, 'torque is MB sin(theta)... B = tau/M... M=IA...') repeated almost verbatim as segments 27-32 (313.3-346.7s), separated by no true new content in between. Unlike the severe cases found elsewhere in this chapter, this one does NOT swallow any missing material -- the dimensional derivation resumes correctly right after (segment 33, 'so this will cancel out') and completes normally by t=433.8s, matching the board (floor_000018-000019). Left un-grounded rather than double-counted as a claim.
- [18:00–23:06] The lecture's own promised final topic ('...and law') -- Faraday's Second Law in quantitative form and both worked numericals -- is missing from the ASR transcript entirely, despite being fully present on the board and on schedule well within the verified duration (1386.6s). Board timeline: floor_000055 (t=1080s) is the first frame showing a 'Faraday's law of em induction' heading with the qualitative first law; floor_000057 (t=1120s) shows the complete quantitative second law (|eps|=N dPhi/dt, I=eps/R) on a fresh page; floor_000059 (t=1160s) already has the first worked numerical's question written ('coil of 500 turns varies...'); floor_000063/000065 (t=1240-1280s) show it fully solved (20 kV); floor_000067/000069 (t=1320-1360s) show a second numerical (100 turns, 0.1 m^2, field reversed through 180 degrees) set up and half-solved, right where the frame set ends (only 26.6s of true runtime remains after the last extracted frame). The transcript, however, over this same interval (segments 75-92, t=998.4-1400.9s) stays on a qualitative re-explanation of experiments 1-3 and 'change in flux causes current' (itself somewhat repetitive across segments 83-91, though not an exact loop) and never once contains the words 'law', 'emf', 'proportional', '500', or 'turns'. Automated checks do not catch this: coverage_ratio is 1.010 (comfortably 'passed'), and check_coverage/sanitize_segments report repetition_detected=False, because the transcript's final ~400s is a paraphrase of earlier ground rather than a verbatim repeat of adjacent segments. The second-law equation, both worked numericals, and the phrase 'Faraday's law' itself are grounded from board frames alone in this note.

---

## Lenz's Law and Motional EMF

**NCERT sections covered:** 6.4, 6.5, 6.6

### Recap: Faraday's law gives magnitude only (NCERT 6.4)
$$|\varepsilon| = N\frac{d\Phi_B}{dt}$$
This tells you *how much* emf is induced, but not its *direction* -- for that, we need **Lenz's law**.

### Lenz's Law (NCERT 6.5)
**Statement:** the direction of an induced emf (and the current it drives) is always such that it **opposes the cause that produces it**.

**Why -- derived from energy conservation, not asserted:** bring the north pole of a magnet towards a coil.
- *Suppose* the coil's near face became a **south** pole. South attracts north, so the coil would pull the magnet in on its own, with **no work done by you** -- yet a current (energy) would appear. That is a free lunch, forbidden by conservation of energy.
- So the near face **must** become **north** instead. You now have to do mechanical work pushing the magnet in *against* this repulsion -- and it is exactly that mechanical work which converts into the induced electrical energy.

Run the same argument with the magnet being *withdrawn*: the near face must become attractive (opposite pole), so you do work pulling it away against attraction -- which is also why the induced current reverses direction between approach and withdrawal (matching Experiment 1 from Lecture 1). **Lenz's law is thus a restatement of conservation of energy**, and the minus sign in $\varepsilon = -N\,d\Phi_B/dt$ (restored explicitly later this lecture) is its mathematical signature.

#### Worked Lenz's-law problems (direction-finding practice)
The board works through several loop-crossing-a-field-boundary problems using the right-hand rule (curl fingers along the trial current, thumb gives the field that current would create; the real current must be whichever direction makes that field **oppose** the actual flux change):
- A triangular loop $ABC$ dragged through a field region into the page: **anti-clockwise** while entering (opposing increasing flux), **no current** while fully inside and flux is momentarily steady, **clockwise** while leaving (opposing decreasing flux).
- The same technique repeated for circular and square loops crossing a field boundary.
- A straight current-carrying wire next to a small coil: coil current is clockwise when the wire's current (and hence its field) is increasing.
- A coil approaching a bar magnet's field region, solved by the pole-facing method.

*(These worked examples are grounded from board frames -- see the flagged spans below for why the transcript is not a reliable source for this material.)*

### Motional EMF (NCERT 6.6)
**Setup:** since $\Phi_B = BA\cos\theta$, emf can be induced by changing $B$, changing $A$, or changing $\theta$. Changing $B$ is the Faraday/Lenz case just covered; changing the **area** is new and gives **motional emf**.

**Derivation (flux rule).** A conducting rod $ab$ of length $l$ slides with velocity $v$ along rails, in a uniform field $B$ into the page. In time $dt$ it sweeps extra area $dA = l\,dx$:
$$d\Phi_B = B\,dA = B\,l\,dx \quad\Rightarrow\quad \varepsilon = -\frac{d\Phi_B}{dt} = -Bl\frac{dx}{dt} = -Blv$$
Because the emf here comes from the conductor's own **motion** (not a changing $B$), this is called **motional emf**:
$$\boxed{\varepsilon = -Blv} \qquad (B, l, v \text{ mutually perpendicular})$$

**Direction -- Fleming's Right Hand Rule (FRHR):** thumb = direction of motion ($v$), forefinger = magnetic field ($B$), centre finger = induced current.

**Special and general cases:**
- If $v \parallel B$: **no emf is induced** (the rod's motion has no component driving charges along its length relative to the field).
- If the rod and its velocity are both inclined at angle $\theta$ to $B$ (the fully general case): $\varepsilon = Blv\sin\theta$.

---
*Note on this lecture's transcript:* the opening recap and the Lenz's-law energy-conservation argument (roughly the first 950 seconds of real content) are well corroborated by both transcript and board frames. Past that point, the transcript becomes unreliable -- a large block of earlier material gets re-transcribed a second and even a third time with fabricated later timestamps, silently standing in for the real audio. As a direct result, **every worked Lenz's-law practice problem past the ABC-loop case, the explicit $\varepsilon=-N\,d\Phi_B/dt$ recombination, and this lecture's entire motional-emf derivation (its own named second topic) are grounded from board frames alone.** See the flagged spans below for the full timeline and why the automated coverage/repetition checks did not catch it.


### Verify these spans
- [10:46–35:34] Severe delayed-duplication, worse than a single repeat: the same block of content (magnet-withdrawal Lenz argument through the ABC-loop right-hand-rule problem, corresponding to real segments ~44-100) appears to have been re-transcribed by the model a SECOND time as segments 101-132 (timestamps 1632.2-1888.8s) and a THIRD time as segments 133-167 (timestamps 1888.8-2134.8s, i.e. running to and past the true 2129.8s end) -- e.g. segment 71@1070s / 143@1966s / 159@2072s are a near-verbatim ratio=1.00 triple, as are several dozen other pairs the delayed-duplicate scan flagged (54 pairs total, ratios 0.71-1.00). check_coverage()/sanitize_segments() do not catch this: duration coverage is ~100% and repetition_detected is False, because none of the duplicate segments are ADJACENT to their earlier twin -- each recurrence is separated by many segments, exactly the blind spot this scan exists for.
- [15:50–35:29] Consequence of the above: essentially everything the board shows from floor_000049 (t=960s) onward is missing from the ASR transcript, which spends that entire real-time window re-outputting earlier material under fabricated later timestamps instead. No transcript segment anywhere in this 168-segment transcript contains the words 'motional', 'Blv', 'Fleming', or 'Lorentz' -- despite 'motional emf' being this lecture's own named second topic, and despite a complete board derivation of it existing on schedule, well inside the verified 2129.8s duration. Board timeline used to ground this note: floor_000049 (960s) circle/square/triangle Lenz practice problems; floor_000059 (1160s) current-carrying-wire-and-coil problem; floor_000063/65 (1240-1280s) coil-approaching-magnet problem; floor_000071/73 (1400-1440s) Faraday+Lenz recombined WITH the minus sign, then 'ways to induce emf'; floor_000077-87 (1520-1720s) the full motional-emf flux-rule derivation to eps=-Blv; floor_000089/91 (1760-1800s) Fleming's Right Hand Rule; floor_000095-106 (1880-2100s, the last extracted frame) the v-parallel-to-B null case and the general eps=Blv*sin(theta) case, which is where the board's own content ends, matching the lecture's true runtime closely. Every claim in this note past 'the ABC-loop problem' is grounded from board frames alone for exactly this reason.

---

## Motional EMF: Polarity, Numericals, Rotating Rod, and Energy Consideration

**NCERT sections covered:** 6.6

### Motional EMF: polarity, and worked numericals (NCERT 6.6)

**Finding polarity:** for a rod moving with velocity $v$ through field $B$, using $\vec F=q\vec v\times\vec B$ on the rod's free charges, positive charge accumulates at one end and negative at the other, until the resulting internal electric field balances the magnetic force ($F_E=F_M$ at equilibrium). The rod then behaves like a fictitious battery — no battery is actually present, only charge separation.

#### Worked numerical: jet plane in Earth's field
A jet, wingspan $l=25$ m, flies west at $v=1800$ km/hr. Only Earth's **horizontal** field component $B_H$ matters (the vertical component $B_V$ is parallel to $l$, so contributes nothing — $v$, $l$, $B$ must all be mutually perpendicular). With $B=5\times10^{-4}$ T, dip angle $\delta=30°$:
$$B_H = B\cos\delta = 5\times10^{-4}\times\frac{\sqrt3}{2}$$
$$\varepsilon = B_H\, l\, v \qquad (v \text{ in m/s, via} \times 5/18)$$
Polarity found the same way as above via $\vec F=q\vec v\times\vec B$.

### EMF from a rotating conductor

A rod of length $l$, hinged at the centre and free at the other end, rotates with angular velocity $\omega$ in a uniform field $B$ parallel to the rotation axis:
$$\boxed{\varepsilon = \frac{1}{2}B\omega l^2}$$

**Worked numerical:** rod length $1$ m, rotated at $50$ rev/s, hinged at the centre of a ring of radius $1$ m, $B=1$ T parallel to the axis. $\omega=2\pi\nu=2\pi(50)$ rad/s:
$$\varepsilon = \frac{1}{2}(1)(2\pi\times50)(1)^2 = 50\pi~\text{V}$$

**Second numerical (setup):** a wheel with $10$ metallic spokes, each $0.5$ m long, rotated at $120$ rev/min in a plane normal to Earth's horizontal field $H_E=0.4$ gauss.

### Energy consideration in motional EMF (NCERT 6.6)

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


### Verify these spans
- [10:54–29:35] The jet-plane numerical (motional EMF, Earth's field) is transcribed correctly once (~t=654-1226s), but the ASR then re-transcribes essentially the same explanation nearly verbatim a second time (~t=1226-1775s) -- the same delayed-repetition pattern found repeatedly in this chapter's and Ch5's lectures. Board frames show that by real video time t=1260s the class has already finished this numerical AND completed the rotating-rod EMF derivation (epsilon=(1/2)*B*omega*l^2) plus solved a full worked numerical on it (metallic rod, 50 rev/s, giving 50*pi V) and started a second one (wheel with 10 spokes) -- meaning the transcript's self-reported timestamps for its second half are significantly drifted later than real video time due to this internal duplication. The rotating-rod claims above are grounded from frames rather than the transcript's own words, since the transcript (in its own, drifted timeline) only reaches the point of setting up the rotating-conductor problem before cutting off.
- [29:35–32:38] The transcript's own words never get past setting up the rotating-rod problem (its last segment describes the rod and asks for the EMF between a and b, without deriving or solving it). Board frames, however, show that -- likely well within the true 1958s runtime, given the timestamp drift documented above -- the class not only completes the rotating-rod derivation and two numericals but goes on to a full 'Energy consideration in motional EMF' derivation (floor_000079.jpg, floor_000096.jpg): the magnetic braking force on the rod, the applied force needed to sustain constant velocity, and the equality of applied mechanical power and dissipated electrical power. This entire topic -- named directly in this lecture's own filename ('numericals, energy consideration') -- is completely absent from the transcript's own words and is grounded here entirely from frames.

---

## Flux/EMF Graph Numerical, Induced Charge, Induced Electric Field, Eddy Currents

**NCERT sections covered:** 6.4, 6.5, 6.6, 6.8

### Worked numerical: flux, EMF, force, and power vs. distance (NCERT 6.4)

Classic NCERT-style problem: the arm PQ of a rectangular conductor is moved from $x=0$ outwards. A uniform field $B$ is perpendicular to the plane, present for $0\le x\le b$ and zero for $x>b$; only PQ (length $l$) has resistance $r$. PQ is pulled from $x=0$ to $x=2b$, then back to $x=0$, at constant speed $v$.

| Quantity | $0\le x<b$ | $b\le x<2b$ |
|---|---|---|
| Flux $\phi$ | $Blx$ (linear) | $Blb$ (constant) |
| EMF $\varepsilon=-d\phi/dt$ | $-Blv$ | $0$ |
| Force to pull PQ | $F=I l B=\dfrac{B^2l^2v}{r}$ | $0$ |
| Power dissipated | $P=I^2r=\dfrac{B^2l^2v^2}{r}$ | $0$ |

(Same pattern retraces, sign-flipped, on the return trip from $2b$ back to $0$.)

### Induced charge is independent of time (NCERT 6.4)

From $\varepsilon=-N\dfrac{d\phi}{dt}$ and $I=\varepsilon/R$: charge in a small interval $dt$ is $dq = I\,dt = \dfrac{N}{R}d\phi$. Over a finite interval:
$$\boxed{q = \frac{N}{R}\,\Delta\phi}$$
The time interval cancels out completely — induced charge depends only on $N$, $R$, and the *total* flux change, never on how fast it happens.

### Induced electric field (NCERT 6.4)

Unlike an **electrostatic** field (conservative: $\oint\vec E\cdot d\vec l=0$), an **induced** electric field arises from a time-varying $B$ and is **non-conservative**: $\oint\vec E\cdot d\vec l = -\dfrac{d\phi}{dt} \ne 0$.

### Eddy (Foucault) currents (NCERT 6.5)

**Definition:** induced circulating currents produced *within* a metal itself, due to a change in flux linked with the metal; direction given by Lenz's law.

- **Damping example:** a metal plate oscillating in/out of a field comes to rest quickly — eddy currents oppose the motion. Slotting the plate lengthens the current path (more resistance, less current), reducing damping.
- **Jumping ring/disc:** an AC-driven coil induces eddy currents in a nearby disc; by Lenz's law the induced pole repels the coil's pole, making the disc jump.
- **Falling magnet in a tube:** dropping a magnet through a copper tube vs. a plastic tube of the same length — eddy currents in the copper brake the fall ($a<g$), while the plastic tube (non-conductive, no eddy currents) lets it fall freely ($a=g$).
- **Disadvantages:** energy loss as heat; unwanted damping.
- **Applications:** induction furnaces, speedometers, dead-beat galvanometers, electric braking (e.g. trains).

### Third way to induce EMF: changing coil orientation (NCERT 6.8, intro to AC generator)

$$\phi = AB\cos\theta$$
where $\theta$ is the angle between the coil's area vector $\hat n$ and $\vec B$. With $\theta=\omega t$:
$$\phi = AB\cos(\omega t), \qquad \varepsilon = -\frac{d\phi}{dt} = AB\omega\sin(\omega t)$$
For an $N$-turn coil: $\varepsilon = NAB\omega\sin(\omega t)$ — the sinusoidal EMF of an **AC generator**.

---
*Note on this lecture's transcript:* the numerical's force and power parts (announced at the start but never narrated), the conclusion of the falling-magnet demonstration (cut off mid-sentence), and the final step of the AC-generator derivation are all grounded from board frames rather than the transcript's own words. See the flagged spans below.


### Verify these spans
- [00:45–10:05] At the very start of this numerical (t=29s), the transcript explicitly announces that FOUR quantities will be found: flux, EMF, force, and power. The transcript's actual narration, however, only ever works through flux and EMF (with their graphs) before moving on (at t=605s) to a completely different topic (proving induced charge is independent of time interval) -- the force and power parts are never spoken at all. A board frame (floor_000030.jpg, t=580s -- chronologically before even the transcript's own EMF-graph discussion concludes) shows the complete solution already written for all four parts, including force (F=B^2l^2v/r) and power (P=B^2l^2v^2/r) with their own graphs vs. x. The force and power claims above are grounded entirely from this frame, not the transcript's own words.
- [29:40–30:07] The transcript describes a falling-magnet demonstration (dropping a magnet through a copper pipe vs. a plastic pipe of the same length, to see which one it exits first) but cuts off mid-sentence ('when it is coming down...') right as it should explain the actual physical conclusion, then abruptly jumps to a new topic ('advantages and disadvantages of eddy currents') with an out-of-order timestamp (the next segment's reported start, 1800s, is earlier than the cut-off segment's own start of 1801s) -- suggesting a dropped/skipped segment rather than a natural transition. A board frame (floor_000092.jpg) shows the resolution: the copper-tube magnet falls with a<g (eddy-current braking) while the plastic-tube magnet falls with a=g (free fall, no eddy currents possible in a non-conductor). This conclusion is grounded entirely from the frame.
- [34:33–36:28] The transcript's own words, in their final segments, introduce flux=AB*cos(theta) and identify theta as the angle between the area vector and B, but never reach the point of substituting theta=omega*t or taking the derivative to get the sinusoidal EMF form. A board frame (floor_000105.jpg) shows this next step already written (phi=AB cos(omega t), epsilon=-dphi/dt, with the derivative rule for cos(omega t) noted alongside) -- the direct, expected continuation of what the transcript itself sets up. The final AC-generator EMF formula claim above is grounded from this frame rather than the transcript's own words.

---

## Self Induction (Inertia of Electricity) and Self Inductance

**NCERT sections covered:** 6.7

### Self induction: inertia of electricity (NCERT 6.7)

When a coil is switched on, current takes time to rise to its maximum value rather than jumping instantly: the changing current produces changing flux through the coil itself, inducing a **back EMF** (by Lenz's law) that opposes the current's growth. At switch-off, the coil similarly opposes the current's decay. This resistance to *any change* in its own current — analogous to mechanical inertia — is why self-induction is called the **inertia of electricity**.

**Definition:** self-induction is the property of a coil by virtue of which it opposes the growth or decay of current flowing through it.

#### Conceptual example
Battery + key feed two parallel branches: inductor $L$ + bulb $B_1$, and resistor $R$ + bulb $B_2$.
- **On switch-close:** $L$ opposes current growth, $R$ doesn't $\Rightarrow$ $B_2$ glows **immediately**; $B_1$ brightens gradually.
- **On switch-open** (after both are steady): $L$ opposes the current's decrease $\Rightarrow$ $B_1$ glows **for longer**.

#### Sparking and non-inductive winding
Rapid voltage change at switching ($0\to230$ V or back) induces a large EMF, ionizing the air gap at switch contacts $\Rightarrow$ a spark (why circuits should never be switched near a gas leak). Modern switches add a small resistor between contacts to reduce this. Household AC wires are **twisted** together so current in adjacent opposite-direction sections is equal and opposite, cancelling the magnetic field — a **non-inductive coil**, minimizing self-induction.

### Self-inductance $L$

Flux linked with a coil is proportional to current: $\phi \propto i \Rightarrow \phi = Li$, where $L$ is the **coefficient of self-induction** (self-inductance).

**Three equivalent definitions:**
1. Setting $i=1$ A: $L=\phi$ — flux linked with the coil per unit current.
2. From $e=-d\phi/dt = -d(Li)/dt$: $\boxed{e = -L\dfrac{di}{dt}}$
3. Setting $di/dt=1$ A/s: $L=e$ — the EMF induced per unit rate of change of current.

**Units:** $L=\phi/I \Rightarrow$ Wb/A $=$ **Henry (H)**; also $L=e/(di/dt)\Rightarrow$ V$\cdot$A$^{-1}\cdot$s. $1\text{ H} = 1\text{ V}\cdot\text{A}^{-1}\cdot\text{s} = 1\text{ Wb}\cdot\text{A}^{-1}$.
**Dimensional formula:** $[L] = [ML^2T^{-2}A^{-2}]$

---
*Note on this lecture's transcript:* this is one of the cleanest transcripts found in this chapter. The only gap is at the very end — the video cuts off just as a third phrasing of $L$'s definition is announced; that phrasing and the units/dimensional formula are grounded from a board frame just past the transcript's own last words.


### Verify these spans
- [24:14–24:14] The transcript's very last words are 'So, now let's try to define L' -- suggesting a third phrasing of the definition is about to be given, right as the video ends. A board frame (floor_000069.jpg) shows this third definition already written out (L=e when di/dt=1), along with the units of L (Wb/A = Henry; V.A^-1.s) and its dimensional formula [ML^2T^-2A^-2]. Since the transcript itself never speaks these words, the third-definition and units/dimensions claims above are grounded from the frame -- the direct, expected continuation of what the transcript's own final sentence announces.

---

## Inductor, Self Inductance of a Solenoid, Energy Stored, and Intro to Mutual Induction

**NCERT sections covered:** 6.7

### Ideal resistor vs. ideal inductor; self-inductance of a solenoid (NCERT 6.7)

An **ideal resistor** has zero self-inductance; an **ideal inductor** has zero resistance and high self-inductance. An inductor is a tightly wound coil of insulated wire. (Real components are never perfectly ideal.)

#### Self-inductance of a solenoid
Solenoid: length $L$, $n$ turns per unit length ($N=nL$ total turns), area $A$, current $I$. Using $B=\mu_0 nI$ (Ampere's law) and flux per turn $\phi=BA$:
$$\phi_\text{total} = N\phi = N A B = (nL)(A)(\mu_0 nI) = \mu_0 n^2 A L\, I$$
Since $\phi_\text{total}=LI$:
$$\boxed{L = \mu_0 n^2 A L}$$
With a magnetic core of relative permeability $\mu_r$: $L=\mu_0\mu_r n^2 A L$ (bigger $L$ opposes current more strongly).

### Energy stored in an inductor

Charging current against the back EMF does work: $dW = E\,dq$. With $E=L\,dI/dt$ and $dq=I\,dt$: $dW = LI\,dI$. Integrating from $0$ to $I$:
$$\boxed{U_M = \frac{1}{2}LI^2 = \frac{1}{2}\phi I}$$

#### Energy density (energy per unit volume)
$$u = \frac{U_M}{\text{Volume}} = \frac{\frac12 LI^2}{AL}$$
Substituting $\phi=NAB$, $L=\phi/I$, and $B=\mu_0 nI$ (so $nI=B/\mu_0$), this simplifies to the standard result:
$$\boxed{u = \frac{B^2}{2\mu_0}}$$

### Mutual induction (intro)

**Phenomenon:** inducing a current in a nearby coil (secondary, $S$) due to a changing current in another coil (primary, $P$). Coefficient of mutual induction:
$$\phi_S \propto I_P$$

**Demo:** AC-driven primary coil $A$; secondary coil $B$ with a bulb lights up due to mutual induction. Moving $B$ further from $A$ dims the bulb — flux linking $B$ decreases with separation.

---
*Note on this lecture's transcript:* the derivation of energy density is cut off mid-algebra right at the transcript's own final words, and the introduction to mutual induction (this lecture's own third named topic) never appears in the transcript at all. Both are completed/grounded from a board frame; see the flagged span below.


### Verify these spans
- [20:12–22:12] The transcript's own words are still working through the algebra of the energy-per-unit-volume derivation right up to its very last segment ('I want my answer... I want basically B, I don't want to eliminate B because at the back of the mind I want to prove that this energy per unit volume...'), cutting off before ever stating the final result or reaching mutual induction at all. However, a board frame (floor_000061.jpg) -- whose true video timestamp (t=1200s) falls BEFORE the transcript's own self-reported final segment (which claims to start at t=1336s, already past the video's true 1332.03s duration) -- shows mutual induction already introduced in full: its definition, the coefficient of mutual induction (phi_S proportional to I_P), and a primary/secondary coil demonstration with a bulb. This confirms the transcript's own timestamps drifted later than real video time by the end of the lecture. The final energy-density result (u=B^2/2*mu0) is the direct, expected algebraic completion of the transcript's own work and is standard NCERT content; the mutual-induction claims are grounded entirely from the frame, not the transcript's own words.

---

## Mutual Inductance of Two Coaxial Solenoids, Worked Numerical, and the AC Generator

**NCERT sections covered:** 6.7, 6.8

### Mutual inductance of two coaxial solenoids (NCERT 6.7)

Two long coaxial solenoids $S_1$ (inner, $n_1$ turns/length, $N_1$ turns, area $A_1$) and $S_2$ (outer, $n_2$, $N_2$, $A_2$), both length $l$. Current $I$ in $S_1$ creates:
$$B_1 = \mu_0 n_1 I = \mu_0\frac{N_1}{l}I$$
Flux linked with $S_2$ (using $A_1$, the area where $B_1$ actually exists):
$$\phi_2 = N_2 B_1 A_1 = \mu_0\frac{N_1 N_2 A_1}{l}I \quad\Rightarrow\quad \boxed{M_{21} = \frac{\mu_0 N_1 N_2 A_1}{l}}$$

**Reciprocity:** a symmetric argument (current in $S_2$ instead, using whichever cross-section is common/smaller) gives $M_{12}=M_{21}$ — the mutual inductance is the same either way.

#### Worked numerical (classic two-loop problem)
A circular loop of radius $0.3$ cm lies parallel to a much bigger circular loop of radius $20$ cm, centres $15$ cm apart. (a) Flux linking the bigger loop for $I=0.2$ A in the smaller loop? (b) Mutual inductance?

**Method:** treat the small loop as a point dipole; use the big loop's on-axis field $B=\dfrac{\mu_0}{2}\dfrac{I a_2^2}{(a_2^2+x^2)^{3/2}}$ at the small loop's location, then $\phi = \pi a_1^2 B$ (uniform over the tiny loop's area); $M=\phi/I$.

### The AC generator (NCERT 6.8)

**Principle:** electromagnetic induction — converts mechanical energy to electrical energy.

**Construction:**
1. **Armature** — many turns of insulated copper wire wound on a metallic frame
2. **Slip rings** $(S_1, S_2)$ — rotate with the armature
3. **Carbon brushes** $(B_1, B_2)$ — contact between rotating slip rings and the external circuit
4. **Field magnet** (N–S) — provides the field the armature rotates in

**Working:** after every half rotation, the current's direction through the armature reverses — this alternation is what produces AC.

**Theory:** $\phi = AB\cos\theta = AB\cos(\omega t)$, so:
$$\varepsilon = -N\frac{d\phi}{dt} = NAB\omega\sin(\omega t) = \varepsilon_0\sin(\omega t), \qquad \varepsilon_0 = NAB\omega$$
$$I = \frac{\varepsilon}{R} = \frac{NAB\omega}{R}\sin(\omega t)$$

| $\omega t$ | $0$ | $90°$ | $180°$ | $270°$ | $360°$ |
|---|---|---|---|---|---|
| $\varepsilon$ | $0$ | $\varepsilon_0$ | $0$ | $-\varepsilon_0$ | $0$ |

tracing the standard sinusoidal AC waveform.

---
*Note on this lecture's transcript:* after correctly deriving $M_{21}$, the ASR gets stuck re-transcribing the same ~230-second "now let's calculate $M_{12}$" setup at least seven times, all the way to the transcript's final (cut-off) word. As a result, the completed $M_{12}=M_{21}$ proof, the worked numerical, and the ENTIRE AC generator topic — construction, working, and the full EMF derivation — never appear in the transcript's own words at all, despite board frames confirming all of it was taught within the true runtime. Everything past the initial $M_{21}$ derivation above is grounded entirely from frames; see the flagged span below.


### Verify these spans
- [05:03–37:19] This is the most severe delayed-repetition failure found anywhere in this project: after correctly deriving M21 (t=3-303s), the transcript gets stuck setting up the M12=M21 proof ('to calculate M12, consider current flowing through S2... magnetic field generates only in area A2... M12 due to 2... n1 n2 mu0 a2 upon l') and re-transcribes this SAME ~230-second block at least SEVEN times back-to-back, continuing almost verbatim all the way to the transcript's very last word ('flowing', at t=2242.975s, cut off mid-sentence). Essentially the entire remaining 86% of this lecture's real content -- completion of the M12=M21 proof, the worked mutual-inductance numerical (the lecture's own second named topic), and the ENTIRE AC generator topic (construction, working, and the full sinusoidal-EMF derivation -- the lecture's own third named topic) -- is completely absent from the transcript's own words. Board frames confirm all of this content was genuinely taught and written out in full within the true 2239.5s runtime (the numerical at real t~1180s, the complete AC generator section by real t~2220s, near the very end of the video). Every claim in this note beyond the initial M21 derivation is grounded entirely from frames, not the transcript's own words.
