# Faraday and Henry's Experiments, Magnetic Flux, Faraday's Law

**NCERT sections covered:** 6.1, 6.2, 6.3, 6.4

## Motivation and setup (NCERT 6.1)
Oersted and Ampere had already shown that a moving charge (current) produces a magnetic field. Faraday and Henry's ~1830 experiments asked the converse question: can a magnetic field produce a current? The chapter's answer is yes -- **electromagnetic induction**.

## Magnetic flux (NCERT 6.3)
For a plane area $A$ sitting in a uniform field $\vec B$, with the area's normal at angle $\theta$ to $\vec B$:
$$\Phi_B = \vec A \cdot \vec B = BA\cos\theta$$
$\Phi_B$ is a **scalar**. SI unit: **weber** (Wb); since $\Phi_B = BA$, $\text{Wb} = \text{T}\cdot\text{m}^2$.

**Dimensional formula (board derivation, exam-technique aside, not itself an NCERT-numbered result):** using $B = \tau/(IA)$ from $\tau = MB\sin\theta$ (with $M=IA$), and $\tau$ in N·m:
$$[\Phi_B] = [M][A] = \left[\frac{N\cdot m}{A\cdot m^2}\right][m^2] = [M^1 L^2 T^{-2} A^{-1}]$$
(A short board loop repeats this sub-derivation once before continuing -- see flagged span below; it doesn't affect the final result.)

**Magnetic flux density:** $B = \Phi_B/A$, so $B$ can equivalently be expressed in Wb/m$^2$ as well as tesla.

## Faraday and Henry's experiments (NCERT 6.2)
Three experiments, each showing current is induced in a coil connected to a galvanometer (no battery in the coil circuit itself):

**Experiment 1.** A bar magnet is moved towards, then away from, a coil $C$ wired to a galvanometer $G$. A deflection appears only *while the magnet is moving* -- faster motion gives a larger deflection -- and the deflection reverses direction when the motion (or the facing pole) reverses. A stationary magnet, however close, gives zero deflection.

**Experiment 2.** The bar magnet is replaced by a second coil $C_2$ carrying a steady current from a battery (so $C_2$ itself has a magnetic field and plays the magnet's role). Moving $C_2$ towards/away from $C_1$ (or vice versa) reproduces exactly the same deflection behaviour as Experiment 1. This shows relative motion between the flux source and the coil is what matters, not that the source specifically be a permanent magnet.

**Experiment 3.** Both coils are now held **stationary**. $C_1$ is wired to a battery through a key $K$; $C_2$ to the galvanometer. Closing the key produces a brief deflection that decays to zero once the current in $C_1$ becomes steady; opening the key produces a brief deflection in the *opposite* direction. Inserting an iron rod through the coils strengthens the effect (it strengthens the coupling field).

**What ties the three together:** in every case, current is induced only when the magnetic flux linked with the coil is *changing* -- via relative motion in Experiments 1-2, or via the current (and hence field) switching on/off/settling in Experiment 3. A coil sitting in any steady flux, however large, shows no induced current.

## Faraday's Law of electromagnetic induction (NCERT 6.4)
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


## Verify these spans
- [04:43–05:46] Minor delayed-duplicate: the flagged pair-scan catches segments 22-26 (283.9-312.8s, 'torque is MB sin(theta)... B = tau/M... M=IA...') repeated almost verbatim as segments 27-32 (313.3-346.7s), separated by no true new content in between. Unlike the severe cases found elsewhere in this chapter, this one does NOT swallow any missing material -- the dimensional derivation resumes correctly right after (segment 33, 'so this will cancel out') and completes normally by t=433.8s, matching the board (floor_000018-000019). Left un-grounded rather than double-counted as a claim.
- [18:00–23:06] The lecture's own promised final topic ('...and law') -- Faraday's Second Law in quantitative form and both worked numericals -- is missing from the ASR transcript entirely, despite being fully present on the board and on schedule well within the verified duration (1386.6s). Board timeline: floor_000055 (t=1080s) is the first frame showing a 'Faraday's law of em induction' heading with the qualitative first law; floor_000057 (t=1120s) shows the complete quantitative second law (|eps|=N dPhi/dt, I=eps/R) on a fresh page; floor_000059 (t=1160s) already has the first worked numerical's question written ('coil of 500 turns varies...'); floor_000063/000065 (t=1240-1280s) show it fully solved (20 kV); floor_000067/000069 (t=1320-1360s) show a second numerical (100 turns, 0.1 m^2, field reversed through 180 degrees) set up and half-solved, right where the frame set ends (only 26.6s of true runtime remains after the last extracted frame). The transcript, however, over this same interval (segments 75-92, t=998.4-1400.9s) stays on a qualitative re-explanation of experiments 1-3 and 'change in flux causes current' (itself somewhat repetitive across segments 83-91, though not an exact loop) and never once contains the words 'law', 'emf', 'proportional', '500', or 'turns'. Automated checks do not catch this: coverage_ratio is 1.010 (comfortably 'passed'), and check_coverage/sanitize_segments report repetition_detected=False, because the transcript's final ~400s is a paraphrase of earlier ground rather than a verbatim repeat of adjacent segments. The second-law equation, both worked numericals, and the phrase 'Faraday's law' itself are grounded from board frames alone in this note.