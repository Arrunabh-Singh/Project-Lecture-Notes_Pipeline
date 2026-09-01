# LCR Series Circuit, Resonance, Q Factor, and LC Oscillations

**NCERT sections covered:** 7.7, 7.8, 7.9

## LCR series circuit (NCERT 7.7)

$V_R=IR$ (in phase with $I$), $V_L=IX_L$ (leads $I$ by $90°$), $V_C=IX_C$ (lags $I$ by $90°$). Since $V_L$, $V_C$ are $180°$ apart, their resultant is $V_L-V_C$ (say $V_L>V_C$), perpendicular to $V_R$:
$$E = \sqrt{V_R^2+(V_L-V_C)^2} = I\sqrt{R^2+(X_L-X_C)^2} = IZ$$
$$Z=\sqrt{R^2+(X_L-X_C)^2}~\text{(impedance)}, \qquad \tan\phi=\frac{X_L-X_C}{R}$$

## Resonance (NCERT 7.8)

When $X_L=X_C$ ($\omega L = 1/\omega C$): **resonance**. Here $Z=R$ (minimum), $\phi=0$ (purely resistive behavior), and current is **maximum**, $I_\text{max}=E/R$.
$$\boxed{\omega_r = \frac{1}{\sqrt{LC}}}$$

**Resonance curve** ($I_0$ vs. $\omega$): peaks at $\omega_r$. Smaller $R$ $\Rightarrow$ sharper peak $\Rightarrow$ more **selective** — exactly the property used to tune a radio/TV to one station among many overlapping frequencies.

### Quality factor (Q)
$$Q = \frac{V_L\text{ (or }V_C\text{) at resonance}}{V_R\text{ at resonance}} = \frac{\omega_r L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$$
High $Q$ needs large $L$, small $R,C$.

**Half-power points** $\omega_1,\omega_2$: where $I=I_0/\sqrt2$. **Bandwidth** $BW=\omega_2-\omega_1$ (smaller for sharper curves). Second definition:
$$Q = \frac{\omega_r}{BW}$$

## LC oscillations (NCERT 7.9)

Charged capacitor + inductor, no resistor: $\dfrac{Q}{C} - L\dfrac{dI}{dt}=0$ with $I=-dQ/dt$ gives
$$\frac{d^2Q}{dt^2} + \frac{Q}{LC} = 0$$
— the SHM equation, with $\omega=1/\sqrt{LC}$. Solution: $Q=Q_0\cos(\omega t)$, $I=I_0\sin(\omega t)$ ($I_0=\omega Q_0$).

**Electrical oscillations** produced by energy exchange between the capacitor ($U_E$, electric) and inductor ($U_M$, magnetic):

| $t$ | $0$ | $T/4$ | $T/2$ | $3T/4$ | $T$ |
|---|---|---|---|---|---|
| $U_E$ | $\frac12 Q_0^2/C$ (max) | $0$ | max (reversed polarity) | $0$ | back to start |
| $U_M$ | $0$ | $\frac12 LI_0^2$ (max) | $0$ | max (reversed current) | $0$ |

Total energy $U_E+U_M$ constant (energy conservation) — only the split oscillates.

**Mechanical analogy:** spring-mass system — max displacement (PE max, KE zero) $\leftrightarrow$ max charge ($U_E$ max, $U_M=0$); mean position (KE max, PE zero) $\leftrightarrow$ max current ($U_M$ max, $U_E=0$).

**Why real oscillations damp:** (1) finite resistance dissipates energy as heat; (2) an accelerated charge radiates electromagnetic waves, carrying energy away. Both cause the amplitude to decay over time.

---
*Note on this lecture's transcript:* this is one of the cleanest, most complete transcripts found in this project. The one gap is a genuine ~164-second silent stretch with no transcript segments at all, covering the initial LC-circuit setup (t=0 and t=T/4 energy states) — grounded from a board frame; see the flagged span below.


## Verify these spans
- [37:16–40:00] There is a genuine ~164-second gap in the transcript with no segments at all (jumping directly from the definition of LC oscillations, ending mid-sentence around t=2236s, to a segment at t=2400s that is itself mid-sentence: 'c and Um is equal to zero'). This is where the initial circuit setup (capacitor charged, connected via switch to the inductor) and the first two energy states (t=0: U_E max, U_M=0; t=T/4: U_E=0, U_M max) must have been explained, based on both the surrounding context and a board frame (floor_000123.jpg) that shows exactly this content -- the t=0 and t=T/4 circuit diagrams with their energy formulas. The initial-setup claim above is grounded from this frame rather than the transcript's own words, since no transcript segments exist for this stretch.