# Alternating Current in Eight Derivations

*Chapter 7 · Alternating Current — inside the 16-mark unit shared with EMI. Source: published page `1e4833b5-4f5c-490c-8b6f-b9bf9a3e972c`. Plain-text maths, not KaTeX. Its eight derivations against the five (PD33–PD37) in **Physics, Derived**; this page also carries the theory, formula strip and question tiers.*

> **Scope.** No scope cut. Eight derivations, and this is the chapter most likely to supply a five-mark question on the paper.

## 01 · Theory

### 1 · Alternating current, mean value, rms value

An alternating current reverses direction periodically and varies in magnitude continuously, written `i = i₀ sin ωt` with a matching voltage `v = v₀ sin ωt`. Here `i₀` is the peak value or current amplitude, `ω = 2πν` the angular frequency.

Averaged over a **complete** cycle the current is zero — the negative half exactly cancels the positive half. That is why a moving-coil ammeter reads nothing on ac. Over **half** a cycle the average is not zero:

- Mean over half a cycle: `i_mean = 2i₀/π = 0.637 i₀`

Because the average is useless, ac is described by its **root mean square** value — the steady direct current that would produce the same heating in the same resistance over the same time. Since heating goes as `i²`, and the mean of `sin²ωt` over a cycle is `½`:

- `I_rms = i₀/√2 = 0.707 i₀` and `V_rms = v₀/√2 = 0.707 v₀`

Every ac meter reads rms, and every stated supply voltage — the 220 V mains — is an rms value. Its peak is 220√2 ≈ 311 V.

### 2 · Reactance, impedance, power factor

- **Reactance** is the opposition offered by an inductor or a capacitor alone. Inductive reactance `X_L = ωL`, capacitive reactance `X_C = 1/ωC`. Both in ohm.
- **Impedance Z** is the total opposition of a circuit containing resistance and reactance together, `Z = V_rms/I_rms`, in ohm.
- **Phase angle φ** is the angle by which the current leads or lags the applied voltage.
- **Power factor** is `cos φ = R/Z`, a pure number between 0 and 1. It is the fraction of the apparent power `V_rms I_rms` that is actually consumed.

Reactance differs from resistance in one crucial way: a resistor dissipates energy, a pure reactance does not. Over one cycle an inductor returns to the source exactly the energy it took, and so does a capacitor. That is why a purely reactive circuit consumes zero power however large the current.

### 3 · The three single elements side by side

| Element | Opposition | Phase of current | Against frequency | Power |
|---|---|---|---|---|
| Resistor R | R, constant | In phase with V | Independent of ν | V_rms I_rms |
| Inductor L | X_L = ωL | Lags V by π/2 | Straight line through origin | Zero |
| Capacitor C | X_C = 1/ωC | Leads V by π/2 | Rectangular hyperbola | Zero |

A memory hook the examiner expects you to use correctly: **CIVIL** — in a **C**apacitor **I** comes before **V**; **V** comes before **I** in an inductor **L**.

Two consequences worth knowing as one-liners: a capacitor blocks dc (at `ν = 0`, `X_C = ∞`) but passes ac; an inductor passes dc freely (at `ν = 0`, `X_L = 0`) but chokes ac, which is what a choke coil is for.

### 4 · Resonance and sharpness

In a series LCR circuit `X_L` rises with frequency and `X_C` falls, so at one frequency they are equal and cancel. There the impedance collapses to its smallest possible value, `Z = R`, the current reaches its largest possible value `v₀/R`, and voltage and current come into phase. That is **resonance**, at `ω₀ = 1/√(LC)`.

Resonance only exists if both L and C are present — with one of them missing there is nothing to cancel.

**Sharpness** is how quickly the current falls away on either side of `ω₀`. It is measured by the quality factor

- `Q = ω₀L/R = (1/R)√(L/C) = ω₀/(ω₂ − ω₁)`, where ω₁ and ω₂ are the half-power frequencies at which the current has dropped to `1/√2` of its peak.

Smaller R means larger Q, a taller and narrower peak, and a circuit that responds to a narrower band of frequencies — which is exactly what tuning a radio to one station requires.

### 5 · Transformer, and why transmission uses high voltage

A transformer changes an alternating voltage up or down. It works on **mutual induction**: alternating current in the primary sets up a changing flux in a shared soft-iron core, and that changing flux induces an alternating emf of the same frequency in the secondary. It cannot work on dc, because a steady current makes no changing flux.

The transmission argument, which is asked directly:

- A power station must deliver a fixed power `P = VI` down a line of resistance R.
- The heat wasted in the line is `I²R`.
- For a fixed P, stepping the voltage up divides the current by the same factor.
- Since the loss goes as `I²`, ten times the voltage means a hundredth of the loss.
- So a step-up transformer at the generating end raises the voltage for the journey, and step-down transformers at the consumer end bring it back to 220 V.

*A step-up transformer does not create energy. Raising the voltage lowers the current by the same factor, so `V_P I_P = V_S I_S` still holds.*

## 02 · Derivations

### D1 · AC through a pure resistor

> A source of alternating voltage `v = v₀ sin ωt` is connected across a pure resistance R, with no inductance or capacitance in the circuit.

1. v = v₀ sin ωt
2. Kirchhoff's loop rule: v − iR = 0
3. i = v / R
4. i = (v₀ sin ωt) / R
5. i = (v₀/R) sin ωt
6. Compare with i = i₀ sin(ωt + φ)
7. i₀ = v₀ / R and φ = 0
8. φ = 0 ⇒ current and voltage are in phase
9. i² = i₀² sin²ωt
10. Mean of sin²ωt over one full cycle = 1/2
11. Mean of i² = i₀² / 2
12. I_rms = √(i₀²/2) = i₀/√2 = 0.707 i₀
13. Likewise V_rms = v₀/√2
14. Dividing: V_rms / I_rms = (v₀/√2) / (i₀/√2) = v₀/i₀ = R
15. Instantaneous power p = vi = (v₀ sin ωt)(i₀ sin ωt)
16. p = v₀ i₀ sin²ωt
17. Average over a cycle: P = v₀ i₀ × (1/2)
18. P = (v₀/√2)(i₀/√2)
19. P = V_rms I_rms

**Result:** i = (v₀/R) sin ωt, φ = 0 · I_rms = i₀/√2 · P = V_rms I_rms

**Graph and phasor:** v and i are sine curves that cross zero together and peak together. On the phasor diagram V₀ and i₀ lie along the same line, angle between them zero.

### D2 · AC through a pure inductor — X_L = ωL

> The same source `v = v₀ sin ωt` across a coil of pure self-inductance L with negligible resistance.

1. v = v₀ sin ωt
2. Induced back emf in the coil: ε = −L di/dt
3. Kirchhoff's loop rule: v + ε = 0
4. v − L (di/dt) = 0
5. L (di/dt) = v₀ sin ωt
6. di/dt = (v₀/L) sin ωt
7. di = (v₀/L) sin ωt dt
8. ∫di = (v₀/L) ∫ sin ωt dt
9. i = (v₀/L) (−cos ωt / ω) + constant
10. The source has no steady component, so the constant of integration = 0
11. i = −(v₀/ωL) cos ωt
12. −cos ωt = sin(ωt − π/2)
13. i = (v₀/ωL) sin(ωt − π/2)
14. Compare with i = i₀ sin(ωt − π/2): i₀ = v₀ / (ωL)
15. Compare with i₀ = v₀ / X_L
16. X_L = ωL = 2πνL
17. Phase of current = ωt − π/2; phase of voltage = ωt
18. Current phase is behind voltage phase by π/2

**Result:** X_L = ωL = 2πνL · i = i₀ sin(ωt − π/2) · current lags V by π/2

**Graph and phasor:** X_L against ν is a straight line through the origin. On the phasor diagram V₀ points up and i₀ is 90° clockwise behind it. On the v–i time graph the current curve peaks a quarter cycle after the voltage curve.

### D3 · AC through a pure capacitor — X_C = 1/ωC

> The same source `v = v₀ sin ωt` across a capacitor of capacitance C.

> **Shared setup:** this is derivation 2 with one substitution. Step 1 is identical, steps 12–18 of D2 map one-to-one onto steps 8–13 here, and the boxed result has the same shape. The only real difference: the inductor needs an *integration* and the capacitor a *differentiation*, and that flips the sign of the π/2.

1. v = v₀ sin ωt
2. Charge on the capacitor at any instant: q = Cv
3. q = C v₀ sin ωt
4. i = dq/dt
5. i = d/dt (C v₀ sin ωt)
6. i = C v₀ ω cos ωt
7. i = [v₀ / (1/ωC)] cos ωt
8. cos ωt = sin(ωt + π/2)
9. i = [v₀ / (1/ωC)] sin(ωt + π/2)
10. Compare with i = i₀ sin(ωt + π/2): i₀ = v₀ / (1/ωC)
11. Compare with i₀ = v₀ / X_C
12. X_C = 1/ωC = 1/(2πνC)
13. Current phase (ωt + π/2) is ahead of voltage phase (ωt) by π/2

**Result:** X_C = 1/ωC = 1/(2πνC) · i = i₀ sin(ωt + π/2) · current leads V by π/2

**Graph and phasor:** X_C against ν is a rectangular hyperbola, falling steeply and never touching either axis. On the phasor diagram i₀ is 90° ahead of V₀. At ν = 0 the reactance is infinite, which is the statement that a capacitor blocks dc.

### D4 · Series LCR circuit by phasor diagram

> R, L and C in series across `v = v₀ sin ωt`. Being in series, the same instantaneous current flows through all three, so the current is taken as the reference phasor.

1. Same current I through R, L and C
2. Draw the current phasor I along the reference axis
3. V_R = I R, in phase with I — drawn along I
4. V_L = I X_L, leading I by π/2 — drawn 90° ahead
5. V_C = I X_C, lagging I by π/2 — drawn 90° behind
6. V_L and V_C are opposite in direction, so they partly cancel
7. Their resultant has magnitude (V_L − V_C), along V_L when V_L > V_C
8. V_R and (V_L − V_C) are perpendicular
9. The applied voltage V is the resultant of these two perpendicular phasors
10. V² = V_R² + (V_L − V_C)²
11. V = √(V_R² + (V_L − V_C)²)
12. Substituting V_R = IR, V_L = IX_L, V_C = IX_C:
13. V = √((IR)² + (IX_L − IX_C)²)
14. V = √(I²[R² + (X_L − X_C)²])
15. V = I √(R² + (X_L − X_C)²)
16. Impedance is defined as Z = V / I
17. Z = √(R² + (X_L − X_C)²)
18. Substituting X_L = ωL and X_C = 1/ωC:
19. Z = √(R² + (ωL − 1/ωC)²)
20. From the phasor triangle, tan φ = (V_L − V_C) / V_R
21. tan φ = (I X_L − I X_C) / (I R)
22. tan φ = (X_L − X_C) / R
23. φ = tan⁻¹[(X_L − X_C) / R]
24. Peak current i₀ = v₀ / Z
25. i = [v₀ / √(R² + (ωL − 1/ωC)²)] sin(ωt − φ)

**Result:** Z = √(R² + (X_L − X_C)²) · tan φ = (X_L − X_C)/R

**Phasor diagram:** current along the horizontal reference axis; V_R along it; V_L straight up; V_C straight down; (V_L − V_C) as the surviving vertical; the hypotenuse from the origin is V, and the angle it makes with V_R is φ.

*X_L > X_C: φ positive, circuit is inductive, current lags. X_C > X_L: φ negative, circuit is capacitive, current leads. X_L = X_C: φ = 0, resonance.*

### D5 · Resonance in a series LCR circuit

> The circuit of derivation 4, with R, L and C fixed and the frequency ω of the source varied. Starts from the boxed result of D4, so quote that line first in the exam.

1. From D4: Z = √(R² + (ωL − 1/ωC)²)
2. i₀ = v₀ / Z
3. v₀ is fixed, so i₀ is maximum when Z is minimum
4. R is fixed; the only term that changes with ω is (ωL − 1/ωC)²
5. (ωL − 1/ωC)² ≥ 0 for every ω, and its least value is 0
6. Z is minimum when ωL − 1/ωC = 0
7. ωL = 1/ωC
8. ω²LC = 1
9. ω² = 1/(LC)
10. ω₀ = 1/√(LC)
11. ν₀ = ω₀/2π = 1/(2π√(LC))
12. At ω = ω₀: X_L = X_C, so X_L − X_C = 0
13. Z_min = √(R² + 0) = R
14. i₀(max) = v₀ / R
15. From D4: tan φ = (X_L − X_C)/R = 0/R = 0
16. φ = 0 ⇒ current and applied voltage are in phase
17. The circuit behaves as though only R were present

**Result:** ω₀ = 1/√(LC), ν₀ = 1/(2π√(LC)) · Z = R · i₀(max) = v₀/R

**Graph:** i₀ against ν rises to a peak at ν₀ and falls away on both sides. Draw two curves for two values of R: the smaller R gives the taller, sharper peak. Mark the half-power frequencies ν₁ and ν₂ where the current is i₀(max)/√2, and label the width (ν₂ − ν₁).

*Sharpness is measured by `Q = ω₀L/R = (1/R)√(L/C) = ω₀/(ω₂ − ω₁)`. Resonance is impossible unless both L and C are present.*

### D6 · Average power in an AC circuit, and wattless current

> A voltage `v = v₀ sin ωt` drives a current `i = i₀ sin(ωt − φ)` through any ac circuit, φ being the phase difference between them.

1. Instantaneous power p = v i
2. p = v₀ sin ωt · i₀ sin(ωt − φ)
3. p = v₀ i₀ sin ωt sin(ωt − φ)
4. p = (v₀ i₀ / 2) · 2 sin ωt sin(ωt − φ)
5. Identity: 2 sin A sin B = cos(A − B) − cos(A + B)
6. Here A = ωt and B = ωt − φ
7. A − B = φ and A + B = 2ωt − φ
8. 2 sin ωt sin(ωt − φ) = cos φ − cos(2ωt − φ)
9. p = (v₀ i₀ / 2)[cos φ − cos(2ωt − φ)]
10. Average over one complete cycle: P = (v₀ i₀ / 2)[cos φ − ⟨cos(2ωt − φ)⟩]
11. ⟨cos(2ωt − φ)⟩ over one complete cycle = 0
12. P = (v₀ i₀ / 2) cos φ
13. P = (v₀/√2)(i₀/√2) cos φ
14. P = V_rms I_rms cos φ
15. Purely resistive: φ = 0, cos φ = 1, P = V_rms I_rms — maximum
16. Purely inductive or purely capacitive: φ = π/2, cos φ = 0
17. P = V_rms I_rms × 0 = 0
18. Current flows but no power is consumed — the current is wattless
19. Wattless component of the current = I_rms sin φ

**Result:** P = V_rms I_rms cos φ · cos φ = R/Z is the power factor

**Graph:** plot v, i and p on one set of axes. The power curve oscillates at twice the frequency of v and i; when φ = π/2 it spends equal time above and below the axis, so its average is zero.

*Note that P = 0 for a pure reactance is not because the resistance is zero, but because voltage and current are 90° out of phase.*

### D7 · Transformer — turns ratio, and the four losses

> Two coils, N_P turns in the primary and N_S in the secondary, wound on a common laminated soft-iron core. Assume no flux leakage, so the same flux φ links every turn of both coils, and negligible primary resistance.

1. Flux through each turn of either coil = φ
2. Faraday's law for the primary: ε_P = −N_P (dφ/dt)
3. Faraday's law for the secondary: ε_S = −N_S (dφ/dt)
4. Divide the second by the first: ε_S / ε_P = [−N_S (dφ/dt)] / [−N_P (dφ/dt)]
5. ε_S / ε_P = N_S / N_P
6. Primary resistance negligible ⇒ ε_P = V_P
7. Secondary on open circuit ⇒ ε_S = V_S
8. V_S / V_P = N_S / N_P = r — *(r = turns ratio)*
9. For an ideal transformer, output power = input power
10. V_S I_S = V_P I_P
11. I_P / I_S = V_S / V_P
12. I_P / I_S = N_S / N_P = r
13. I_S / I_P = N_P / N_S = 1/r

**Result:** V_S/V_P = N_S/N_P = I_P/I_S

*`N_S > N_P` is a step-up transformer: voltage rises, current falls. `N_S < N_P` is a step-down: voltage falls, current rises. Efficiency = (V_S I_S / V_P I_P) × 100%.*

#### The four energy losses, and the fix for each

| Loss | What is happening | The fix |
|---|---|---|
| Copper loss | Joule heating i²R in the primary and secondary windings | Use thick copper wire of low resistance |
| Iron loss (eddy currents) | The changing flux induces circulating currents in the solid iron core, which heat it | Laminate the core — thin sheets, insulated from one another, so the eddy loops are broken |
| Flux leakage | Not all the flux made by the primary reaches the secondary | Wind the two coils one over the other on the same core |
| Hysteresis loss | The core is magnetised and demagnetised every cycle and energy is dissipated each time round the loop | Use a soft magnetic material — soft iron or silicon steel — with a thin hysteresis loop |

*Xam Idea adds a fifth, humming loss — energy lost as sound when the core vibrates. Give the four above unless the question asks for five.*

### D8 · AC generator — the emf equation

> A coil of N turns, each of area A, rotates with constant angular speed ω about an axis perpendicular to a uniform magnetic field B. At `t = 0` the plane of the coil is perpendicular to the field, so the area vector is along B.

1. Angle between B and the area vector at time t: θ = ωt
2. Flux through one turn: φ = B A cos θ
3. φ = B A cos ωt
4. Flux linkage through N turns: Nφ = N B A cos ωt
5. Faraday's law: ε = −d(Nφ)/dt
6. ε = −d/dt (N B A cos ωt)
7. N, B and A are constants: ε = −N B A · d/dt (cos ωt)
8. d/dt (cos ωt) = −ω sin ωt
9. ε = −N B A (−ω sin ωt)
10. ε = N B A ω sin ωt
11. sin ωt has maximum magnitude 1
12. Peak emf ε₀ = N B A ω
13. ε = ε₀ sin ωt
14. With ω = 2πν: ε = ε₀ sin 2πνt

**Result:** ε = NBAω sin ωt = ε₀ sin ωt, with ε₀ = NBAω

**Graph:** ε against t is a sine curve, one complete cycle per revolution of the coil, zero when the coil plane is perpendicular to B and peak when the plane is parallel to B.

*Four parts to name in the diagram: field magnet, armature coil, slip rings, carbon brushes. The output can be raised by increasing N, increasing B, increasing A, or spinning faster. A moving-coil galvanometer cannot read this current, because its average over a cycle is zero.*

## 03 · Formula strip

*● must be instant · ○ a few seconds is fine*

### ● rms value of an alternating current or voltage

`I_rms = i₀/√2 = 0.707 i₀ · V_rms = v₀/√2` — i₀, v₀ = peak values. I in ampere (A), V in volt (V). This is what every ac meter reads.

### ○ Mean value of an alternating current over half a cycle

`i_mean = 2i₀/π = 0.637 i₀` — in ampere (A). Over a *full* cycle the mean is zero.

### ● Inductive reactance

`X_L = ωL = 2πνL` — L = self-inductance in henry (H), ν = frequency in hertz (Hz), ω = 2πν in rad s⁻¹. X_L in ohm (Ω).

### ● Capacitive reactance

`X_C = 1/ωC = 1/(2πνC)` — C = capacitance in farad (F). X_C in ohm (Ω). Infinite at ν = 0, which is why a capacitor blocks dc.

### ● Impedance of a series LCR circuit

`Z = √(R² + (X_L − X_C)²)` — R, X_L, X_C, Z all in ohm (Ω). Reduces to R alone at resonance.

### ● Phase angle of a series LCR circuit

`tan φ = (X_L − X_C)/R` — φ in radian or degree. Positive φ means the current lags; negative means it leads.

### ● Power factor, in terms of the circuit constants

`cos φ = R / Z` — a pure number between 0 and 1. Equal to 1 for a pure resistance and at resonance, 0 for a pure reactance.

### ● Average power consumed in any ac circuit

`P = V_rms I_rms cos φ` — P in watt (W). V_rms I_rms alone is the apparent power; only the cos φ fraction of it is consumed.

### ○ Wattless component of the current

`I_wattless = I_rms sin φ` — in ampere (A). This component transfers no net energy over a cycle.

### ● Resonant frequency of a series LCR circuit

`ω₀ = 1/√(LC) · ν₀ = 1/(2π√(LC))` — L in henry (H), C in farad (F). ω₀ in rad s⁻¹, ν₀ in hertz (Hz).

### ○ Quality factor, all three forms

`Q = ω₀L/R = (1/R)√(L/C) = ω₀/(ω₂ − ω₁)` — a pure number, no unit. ω₁ and ω₂ are the half-power frequencies. Larger Q means a sharper resonance.

### ● Transformer equation, all three ratios

`V_S/V_P = N_S/N_P = I_P/I_S` — N = number of turns (no unit), V in volt (V), I in ampere (A). Note the current ratio is inverted.

### ○ Efficiency of a transformer

`η = (V_S I_S) / (V_P I_P) × 100%` — output power over input power, as a percentage. Always below 100% in practice.

### ● emf generated by an ac generator

`ε = NBAω sin ωt = ε₀ sin ωt, ε₀ = NBAω` — N = turns, B in tesla (T), A in m², ω in rad s⁻¹. ε in volt (V).

### ○ Net voltage across a series LCR circuit from the three drops

`V = √(V_R² + (V_L − V_C)²)` — all in volt (V). This is why the three readings can add to more than the source voltage — they add as phasors, not as numbers.

### ○ Power wasted as heat in a transmission line

`P_loss = I²R` — I = line current in ampere (A), R = total line resistance in ohm (Ω), P_loss in watt (W). Ten times the voltage means a hundredth of the loss.

## 04 · Questions to attempt

*Question numbers only, from Xam Idea Chapter 7 and the NCERT questions reprinted inside it. Section names are Xam Idea's own.*

### Tier 1 — must do

*15 questions · these are the 3-mark and 5-mark slots*

| Question | Page | Why |
|---|---|---|
| Long Answer Q1 | p. 249 | Inductor derivation, full |
| Long Answer Q2 | p. 250 | LCR phasor, both variants |
| Long Answer Q3 | p. 252 | Capacitor derivation, disguised |
| Long Answer Q4 | p. 253 | Average power derivation |
| Long Answer Q5 | p. 253 | Resonance plus graph |
| Long Answer Q6 | p. 254 | Generator, three variants |
| Long Answer Q7 | p. 255 | Transformer plus losses |
| Long Answer Q9 | p. 258 | Sharpness and Q |
| Short Answer Q1 | p. 241 | Capacitor in 3 marks |
| Short Answer Q2 | p. 241 | Minimum Z, wattless |
| Short Answer Q3 | p. 241 | Transformer plus transmission |
| Short Answer Q6 | p. 242 | The voltage paradox |
| Short Answer Q8 | p. 243 | Resonance numerical, complete |
| Short Answer Q18 | p. 247 | Three drops, phasor sum |
| NCERT Q8 | p. 230 | Everything at once |

### Tier 2 — if time

*extra pattern coverage, mostly 1 and 2 marks*

| Question | Page | Why |
|---|---|---|
| NCERT Q1–Q7 | p. 228–229 | rms and power drills |
| Assertion–Reason 1–10 | p. 234 | Whole set, ten minutes |
| MCQ 7, 8, 16 | p. 231–232 | Average-power one-markers |
| MCQ 11, 12, 13, 17, 25, 26 | p. 231–233 | LCR and phasor reasoning |
| MCQ 3, 15, 18, 22, 23, 24 | p. 231–233 | Waveform and reactance graphs |
| MCQ 5, 10, 21 | p. 231–232 | Transformer and transmission |
| Very Short Ans Q1, Q3–Q6 | p. 236–237 | Definitions, written out |
| Very Short Ans Q11 | p. 238 | Black box plus phasor |
| Very Short Ans Q12, Q13 | p. 238 | Generator numericals |
| Very Short Ans Q19, Q20 | p. 240 | Transformer, line loss |
| Short Answer Q4, Q7, Q12 | p. 242–244 | Brightness reasoning |
| Short Answer Q5, Q9, Q10, Q13 | p. 242–245 | Impedance numericals |
| Short Answer Q11, Q19 | p. 244, 248 | Transformer numericals |
| Short Answer Q14, Q16, Q17 | p. 246–247 | Resonance and graphs |
| Long Answer Q8 | p. 257 | Reasoning plus numerical |

### Tier 3 — skip unless revising

*off-pattern, over-difficult, or a repeat of something above*

**Off the pattern of this unit:** Case Study `Q1` (p. 235) is an RC charging transient — exponential decay in a dc circuit, not an alternating-current question. Very Short Answer `Q9` and `Q10` (p. 237) derive mean and rms values by integration; the paper will give you the results, not ask you to integrate them.

**Duplicates — do one of each pair, not both:** NCERT `Q3` ≡ Very Short Answer `Q17`. NCERT `Q7` ≡ Short Answer `Q8`. NCERT `Q8` ≡ Short Answer `Q14`. NCERT `Q6` is just the resonance formula with numbers in it.

**Already covered by the theory section:** Very Short Answer `Q2, Q7, Q8, Q15, Q16` and Short Answer `Q15` are pure recall you will have from Section 01. Read the answers, do not write them out.

### The five numerical types this chapter can ask

1. **Peak to rms, and the power a single element takes** — `I_rms = i₀/√2`, then `P = V_rms I_rms cos φ`
2. **Reactance of a coil or capacitor at a stated frequency** — `X_L = 2πνL · X_C = 1/(2πνC)`
3. **Impedance, current and phase angle of a series LCR circuit** — `Z = √(R² + (X_L − X_C)²)`
4. **Resonance: the frequency, the peak current, the individual voltage drops** — `ω₀ = 1/√(LC)`, with Z = R there
5. **Transformer turns and currents, or loss in a transmission line** — `V_S/V_P = N_S/N_P = I_P/I_S`, and `P_loss = I²R`
