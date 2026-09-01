# Power in AC Circuits, Power Factor, Wattless Current, and the Transformer

**NCERT sections covered:** 7.7, 7.8

## Average power in an AC circuit (NCERT 7.7)

$P=EI$, $E=E_0\sin(\omega t)$, $I=I_0\sin(\omega t+\phi)$. Expanding and averaging over a full cycle (oscillating terms vanish):
$$\boxed{P_\text{avg} = E_\text{rms}I_\text{rms}\cos\phi}$$

$\cos\phi$ is the **power factor**; $E_\text{rms}I_\text{rms}$ (without $\cos\phi$) is the **apparent power** — average power = apparent power $\times$ power factor.

**Power factor by circuit type:**
| Circuit | $\cos\phi$ | $P_\text{avg}$ |
|---|---|---|
| Pure $R$ | $1$ | $E_\text{rms}I_\text{rms}$ (max) |
| Pure $L$ or $C$ | $0$ ($\phi=90°$) | $0$ |
| $LR$ | $R/\sqrt{R^2+X_L^2}=R/Z$ | — |
| $RC$ | $R/\sqrt{R^2+X_C^2}=R/Z$ | — |
| $LCR$ | $R/Z$, $Z=\sqrt{R^2+(X_L-X_C)^2}$ | — |

## Wattless current (general case)

Resolving $I_\text{rms}$ relative to $E_\text{rms}$ (angle $\phi$): the parallel component $I_\text{rms}\cos\phi$ delivers real power ($P_\text{avg}=E_\text{rms}I_\text{rms}\cos\phi$); the perpendicular component $I_\text{rms}\sin\phi$ delivers **zero** power (angle $90°$ to $E_\text{rms}$). This perpendicular component is the **wattless current** — current that flows without consuming power over a cycle.

## The transformer (NCERT 7.8)

Converts high-voltage/low-current AC to low-voltage/high-current AC, or vice versa (**step-up**: e.g. 20 V $\to$ 200 V; **step-down**: the reverse). **Principle:** mutual induction. **Construction:** laminated soft iron core (thin insulated sheets, to reduce eddy currents) with primary and secondary coils wound on it, insulated from each other. $N_s>N_p\Rightarrow$ step-up; $N_s<N_p\Rightarrow$ step-down.

**Working equations:**
$$\frac{\varepsilon_s}{\varepsilon_p} = \frac{N_s}{N_p}$$
Assuming no losses, input power = output power ($\varepsilon_p I_p=\varepsilon_s I_s$):
$$\boxed{\frac{\varepsilon_s}{\varepsilon_p} = \frac{I_p}{I_s} = \frac{N_s}{N_p}}$$
(step-up $\Rightarrow$ lower secondary current, and vice versa).

**Energy losses (4 types):**
1. **Flux leakage** — reduced by winding one coil over the other
2. **Resistance of windings** ($I^2R$ heating) — reduced by thick wire
3. **Eddy currents** in the core — reduced by laminating the core
4. **Hysteresis losses** — core repeatedly (de)magnetized each cycle — reduced by a low-hysteresis-loss core material (e.g. soft iron)

---
*Note on this lecture's transcript:* power/power-factor/wattless-current is transcribed cleanly throughout, but the transcript's own words stop partway through the transformer's construction, before ever reaching its working equations or the four energy-loss mechanisms. Both are grounded from board frames; see the flagged span below.


## Verify these spans
- [24:20–28:18] The transcript's own words never get past explaining the transformer's construction (soft iron core, lamination to reduce eddy currents, coil winding) -- its last available segment ends mid-explanation of lamination/eddy currents. However, board frames confirm that, within the true video duration, the lecture goes on to derive the transformer's key working equations (epsilon_s/epsilon_p=Ns/Np=Ip/Is, step-up vs. step-down) and lists all four types of energy losses in a real transformer (flux leakage, winding resistance, eddy currents, hysteresis losses) -- none of which appear in the transcript's own words at all. Both the working-equations claim and the energy-losses claim above are grounded entirely from frames.