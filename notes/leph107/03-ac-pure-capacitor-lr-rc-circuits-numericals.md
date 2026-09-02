# AC Circuits: Pure Capacitor, Power in L/C, LR Circuit, RC Circuit, Numericals

**NCERT sections covered:** 7.5, 7.6, 7.7

## AC circuit with a pure capacitor (NCERT 7.5)

With $E=E_0\sin(\omega t)$: $q=CE_0\sin(\omega t)$, $i=dq/dt=\omega C E_0\cos(\omega t) = E_0\omega C\sin(\omega t+\pi/2)$.

**Current leads EMF by $\pi/2$** (opposite the inductor case). Writing $i=I_0\sin(\omega t+\pi/2)$ with $I_0=E_0/X_C$:
$$\boxed{X_C = \frac{1}{\omega C}} \quad\text{(capacitive reactance, unit: ohm)}$$

$X_C f = \dfrac{1}{2\pi C}=$ const $\Rightarrow$ $X_C$ vs. $f$ is a rectangular hyperbola. At $f=0$ (DC), $X_C\to\infty$ — **a capacitor blocks DC**.

**Worked numerical:** $318\,\mu$F, $230$ V, $50$ Hz. $X_C\approx10\,\Omega$; $I_\text{rms}=E_\text{rms}/X_C=230/10=23$ A; $i=I_0\sin(\omega t+\pi/2)$, $E_0=\sqrt2\,E_\text{rms}$.

## Average power in pure L or C: zero (wattless current) (NCERT 7.7)

For a pure inductor, $P=EI=E_0I_0\sin(\omega t)\sin(\omega t-\pi/2) = -\tfrac12 E_0I_0\sin(2\omega t)$ — averages to **zero** over a full cycle. Current still flows despite zero power dissipation: this is **wattless current**. (Same result, opposite sign, for a pure capacitor.)

**Practical use:** to reduce AC current with (ideally) no power loss, prefer an inductor over a resistor — old tube lights used a **choke coil** for exactly this reason.

## LR circuit (extends NCERT 7.6's phasor method)

$V_R$ and $V_L$ add as **phasors**, not algebraically (they're $90°$ out of phase — $V_L$ leads $V_R$):
$$E = \sqrt{V_R^2+V_L^2} = I\sqrt{R^2+X_L^2} = IZ, \qquad Z=\sqrt{R^2+X_L^2}~\text{(impedance)}$$
$$\phi = \tan^{-1}\frac{X_L}{R}, \qquad E = E_0\sin(\omega t+\phi)$$

**Worked numerical:** coil $L=0.5$ H, $R=100\,\Omega$, on $240$ V, $50$ Hz AC. $Z_L=\sqrt{R^2+(\omega L)^2}$; max current $I_0=E_0/Z_L\approx1.82$ A; phase angle $\phi=\tan^{-1}(\omega L/R)\approx57.5°$; **time lag** $=\phi/\omega\approx3.19\times10^{-3}$ s (current peaks this long after voltage peaks).

## RC circuit (extends NCERT 7.6's phasor method)

By analogous phasor reasoning (now $I$ leads $\varepsilon$, since current leads voltage across $C$):
$$\varepsilon = \sqrt{V_R^2+V_C^2} = I\sqrt{R^2+X_C^2} = IZ_C, \qquad Z_C=\sqrt{R^2+\frac{1}{\omega^2C^2}}$$
$$\tan\phi = \frac{X_C}{R}=\frac{1}{\omega CR}, \qquad \phi = \tan^{-1}\left(\frac{1}{\omega CR}\right)$$

**Worked numerical (setup + method):** circuit on $20$ V, $50$ Hz takes $10$ A, current leading voltage by $T/12$. $\phi = 360°/12=30°$; $R=Z_C\cos\phi$ (with $Z_C=E_\text{rms}/I_\text{rms}$); $X_C$ and hence $C$ follow similarly.

**Second numerical (unfinished in available material):** a $100$ V, $60$ W lamp operated on $220$ V, $50$ Hz mains — find $R$, $X_C$, and $C$ (a lamp-in-series-with-capacitor circuit, used to drop voltage without wasting power in a resistor).

---
*Note on this lecture's transcript:* the LR-circuit derivation repeats nearly verbatim six times back-to-back, consuming roughly 1000 seconds and drifting the transcript's own timestamps for everything after it. As a result, the entire RC-circuit derivation and its own worked numerical are completely absent from the transcript's words and are grounded here from a board frame; the final lamp-and-capacitor numerical is left unsolved since neither the transcript nor the available frames capture its resolution.


## Verify these spans
- [18:41–37:09] The LR-circuit phasor derivation (from setting up the vector-addition argument through the full phasor diagram and phase-angle formula) is transcribed correctly once, then re-transcribed nearly verbatim FIVE more times back-to-back (roughly repeating every ~150-230s from t~1262s through t~2229s) -- another instance of the severe delayed-repetition pattern found throughout this project. This consumed roughly 1000 seconds of transcript time narrating what is a single, short derivation, and appears to have drifted the transcript's own internal timestamps for everything that follows.
- [43:48–46:03] After the LR-circuit numerical, the transcript's own words move directly into setting up a second numerical (a 100V, 60W lamp operated on 220V, 50Hz mains, asked to find resistance, capacitive reactance, and capacitance) but cut off mid-question at 'and capacitance of' -- never reaching the RC-circuit derivation or its own worked numerical at all. However, a board frame (floor_000134.jpg, true video timestamp t=2660s) shows a complete RC-circuit phasor derivation AND a distinct worked numerical (a 20V/50Hz/10A circuit with current leading by T/12) already substantially solved. Since this content cannot fit within the transcript's own (drifted) timeline after the LR numerical, this confirms the earlier repetition pushed the transcript's self-reported timestamps for its final third well behind real video time. The RC-circuit derivation and this second numerical are grounded entirely from the frame; the lamp-and-capacitor numerical remains only partially stated (never solved) in the available material, so no answer is given for it here.