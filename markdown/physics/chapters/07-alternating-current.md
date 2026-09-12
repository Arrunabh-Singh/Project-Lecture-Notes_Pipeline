# Alternating Current

*Class XII CBSE Physics · Chapter 7 · 5 lectures, in order.*

*NCERT sections covered: 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9.*

*Transcribed from the teacher's recorded lectures and checked against the
board frames and the NCERT text. Equations are board-grounded; any span the
transcript could not resolve confidently is flagged in place.*

---

## Mean (Average) and RMS Value of Alternating Current

**NCERT sections covered:** 7.1, 7.2

### Introduction to AC

Alternating current varies continuously in magnitude and periodically reverses direction, written as $i = i_0\sin(\omega t)$ (or equivalently $i_0\cos\omega t$, since both sine and cosine are periodic -- the lecture notes both forms are used interchangeably depending on where $t=0$ is taken). Time period $T$ is the time for one cycle; frequency $f = 1/T = \omega/2\pi$.

Domestic AC supply in India is 50 Hz. Since current crosses zero twice per cycle, at 50 Hz a bulb driven by mains current is effectively "off" 100 times a second -- invisible to the eye because of persistence of vision. The lecture notes that at deliberately low frequencies (e.g. a hand-cranked classroom generator) this flicker becomes visible as the bulb visibly switching on and off.

Alternating EMF follows the same form: $e = e_0\sin(\omega t)$ or $e_0\cos(\omega t)$.

### Mean (average) value of AC

Over a **full** cycle the average of a sinusoid is zero (equal area above and below the time axis), so a physically useful "mean value" is instead defined over a **half** cycle, via **charge equivalence**:

> The mean value of AC over half a cycle is that steady direct current which sends the same charge through a circuit in time $T/2$ as the AC sends through the same circuit in the same time $T/2$.

**Derivation.** For the DC side, charge in time $T/2$ is simply
$$Q_{DC} = I_m\left(\frac{T}{2}\right)$$
For the AC side,
$$Q_{AC} = \int_0^{T/2} i_0\sin(\omega t)\,dt = \frac{i_0}{\omega}\Big[-\cos\omega t\Big]_0^{T/2} = \frac{2i_0}{\omega}$$
(using $\cos(\omega T/2) = \cos\pi = -1$ and $\cos 0 = 1$). Equating $Q_{DC}=Q_{AC}$ and substituting $T=2\pi/\omega$:
$$I_m = \frac{2i_0}{\pi} \approx 0.637\,i_0$$
and by the identical argument, mean EMF $= \dfrac{2e_0}{\pi} \approx 0.637\,e_0$. For the negative half cycle the mean is $-0.637i_0$, so the mean over a *full* cycle is indeed zero -- consistent with the reason this half-cycle definition is used in the first place.

*(Note: this half-cycle mean-value derivation was not found in the extracted NCERT chapter text used for cross-checking here -- it is very likely standard supplementary/exam-prep content the teacher adds alongside the syllabus, not a claim that it contradicts NCERT.)*

### RMS (root mean square) value of AC

Since AC changes continuously, a second and more broadly useful "equivalent DC" value is defined via **heat equivalence**:

> RMS current is that value of steady current which would generate the same amount of heat in a given resistance, in a given time, as the AC does when passed through the same resistance for the same time.

**Derivation.** Heat produced by the DC-equivalent current over one period $T$ in resistance $R$:
$$H_{DC} = I_{rms}^2 R T$$
Heat produced by the AC over the same period:
$$H_{AC} = \int_0^T i^2 R\,dt = \int_0^T i_0^2\sin^2(\omega t)\,R\,dt$$
Using $\sin^2\omega t = \dfrac{1-\cos 2\omega t}{2}$:
$$H_{AC} = \frac{i_0^2 R}{2}\left[\int_0^T dt - \int_0^T \cos(2\omega t)\,dt\right] = \frac{i_0^2 R}{2}\,T$$
(the cosine integral vanishes over a full period). Equating $H_{DC}=H_{AC}$:
$$I_{rms}^2 R T = \frac{i_0^2 R T}{2} \quad\Rightarrow\quad \boxed{I_{rms} = \frac{i_0}{\sqrt2} \approx 0.707\,i_0}$$
and identically, $E_{rms} = \dfrac{e_0}{\sqrt2}\approx 0.707\,e_0$.

This is the same result as NCERT Eq. (7.6) ($I=i_m/\sqrt2$), reached there via the average-power route ($\overline{\sin^2\omega t}=1/2$) rather than this total-heat/charge-equivalence route -- same physics, different derivation path, and a nice illustration that "root mean square" literally means: square the quantity, take its mean, then take the square root.

### Worked numericals (board-only)

The board (visible from roughly 1780s to the end of the lecture) works through six short problems applying the $i_0=\sqrt2\, I_{rms}$ / $I_{rms}=0.707\,i_0$ relations. These do not have matching spoken narration in the available transcript (see uncertain span below) but are clearly legible on the board:

1. $E_{rms}=220\text{ V}$ (household mains) $\Rightarrow E_0=\sqrt2\times220\approx311\text{ V}$ -- matches NCERT's own worked household-voltage figure exactly.
2. $I_{rms}=10\text{ A}\Rightarrow I_0=\sqrt2\times10\approx14.14\text{ A}$.
3. $i=6\sin(314t)\text{ A}$ (i.e. $\omega=314\text{ rad/s}\approx2\pi\times50\text{ Hz}$) $\Rightarrow I_0=6\text{ A}$, $I_{rms}=0.707\times6\approx4.24\text{ A}$.
4. Given rms voltage during a half cycle, find peak voltage and mean value -- set up the same way as above ($E_0=\sqrt2\,E_{rms}$, $E_m=0.637E_0$).
5. Time for current starting from zero to reach its peak value: $t=T/4$ (one quarter cycle), read directly off the sine waveform.
6. RMS value of a **square wave** alternating between $+2$ A and $-2$ A: since the sinusoidal formula $i_0/\sqrt2$ does not apply to a non-sinusoidal waveform, the board instead applies the defining recipe directly -- square the current, average the squares, take the square root: $I_{rms}=\sqrt{\dfrac{I_0^2+I_0^2+I_0^2}{3}}=2\text{ A}$. This is a good check that the student understands "root-mean-square" as a procedure, not just a formula tied to sine waves.


### Verify these spans
- [29:39–32:49] Delayed-repetition ASR artifact: segment starting 1779.5s ('Now, see here, in this case, let's try to understand this definition first...') is repeated almost verbatim at 1944.3s, with segments 65-66 in between (1845.9-1944.3s) re-covering the same 'same amount of heat in a given resistance' phrasing already said at 1720.7s. Net effect is only a short (~165s) block of redundant/looped narration around the RMS heat-definition setup, not a loss of new content -- board frames (floor_000064 at 1260s onward) show the derivation already fully written and progressing steadily, so nothing appears to have been dropped.
- [37:15–38:25] Transcript ends mid-sentence ('Now for AC what you can do is heat produced by AC circuit in time T') without ever verbally stating the final RMS-current derivation or its conclusion I_rms = i0/√2. The segment's declared end (2305.8s) also overshoots the reported lecture duration (2261.8s) by ~44s, suggesting either truncation or an imprecise end-timestamp for the final utterance. However, board frames from ~1580s onward (floor_000080, floor_000083) already show this exact derivation completed and boxed (I_rms = i0/√2 = 0.707 i0, E_rms = 0.707 e0), and frames from 1780s-2240s show it being applied confidently across six solved numericals ending with a non-sinusoidal square-wave example -- so the material was clearly taught in this lecture even though the ASR did not capture the teacher saying the final conclusion aloud. Grounded from frames per the workflow's guidance for this exact failure pattern.
- [25:19–26:10] Segments 56-57 consist of the short phrase 'So, mean or average value of AC is that direction' repeated verbatim ~38 times in a row (a stutter/loop artifact within the ASR output itself, distinct from the delayed-repetition pattern above). Segment durations (21-30s) are plausible for real elapsed time, and the derivation resumes cleanly on both sides (Im=2i0/pi immediately before, 0.637i0 immediately after), so this looks like a local ASR glitch rather than missing content -- flagging for awareness, not treated as a content gap.

---

## AC Circuits with Only R and Only L (Phasors, Resistor, Pure Inductor)

**NCERT sections covered:** 7.2, 7.3, 7.4

### Phasors

A phasor is a vector that rotates about the origin with angular speed $\omega$. Its vertical (projected) component at any instant gives the instantaneous value of the quantity it represents. Both current and voltage in an AC circuit are represented as phasors -- $i_0$ and $e_0$ are the phasor lengths (amplitudes), and the projection onto the vertical axis traces out $i_0\sin\omega t$ or $e_0\sin\omega t$ as the phasor sweeps around.

### AC circuit with only a resistor

For an ideal resistor $R$ on source $e=e_0\sin\omega t$, Kirchhoff's law gives directly
$$e_0\sin\omega t = iR \quad\Rightarrow\quad i = i_0\sin\omega t,\quad i_0=\frac{e_0}{R}$$
Current and voltage are **in phase** -- same $\sin\omega t$ dependence, zero phase difference. On a phasor diagram the $E_0$ and $I_0$ phasors point along the same line; on a $y$-$t$ graph the two sinusoids rise and fall together.

**Aside -- why AC needs its own ammeter design.** A DC ammeter placed in an AC circuit reads the *mean* current, which is zero over a full cycle, so it shows a zero reading. Purpose-built AC ammeters instead exploit the **heating effect** of current ($H\propto i^2Rt$): since $i^2$ is never negative, this gives a genuine non-zero reading, but because the response is proportional to $i^2$ rather than $i$, the scale spacing on an AC ammeter is unequal -- markings spread further apart at higher readings -- rather than the evenly-spaced scale on a DC ammeter.

### AC circuit with only (pure) inductance

For an ideal inductor $L$ (no resistance) on the same source, the induced EMF is $e=-L\,di/dt$, so by Kirchhoff's law
$$e = L\frac{di}{dt} \quad\Rightarrow\quad di = \frac{1}{L}e\,dt \quad\Rightarrow\quad i = \frac{1}{L}\int e_0\sin(\omega t)\,dt = \frac{e_0}{\omega L}\big[-\cos\omega t\big]$$
Rewriting $-\cos\omega t$ as $\sin(\omega t - \pi/2)$ (worked out on the board via $\sin(\pi/2-\omega t)=\cos\omega t$, then reversing sign) gives the standard form
$$i = \frac{e_0}{\omega L}\sin\left(\omega t - \frac{\pi}{2}\right) = i_0\sin\left(\omega t-\frac{\pi}{2}\right),\qquad i_0=\frac{e_0}{\omega L}$$
Defining **inductive reactance** $X_L=\omega L$ (unit ohm, playing the same role $R$ plays for a resistor), this is $i_0=e_0/X_L$.

**Phase relationship.** Current **lags** voltage by $\pi/2$ (a quarter cycle) in a pure inductor -- when the voltage is at its peak, current is zero, and when voltage is zero, current is at its peak. This is the opposite of the resistor case and is drawn on the board both as an $e,i$-vs-$t$ graph and as a phasor diagram with the $I_0$ phasor sitting $90°$ behind $E_0$.

### Worked numericals (board)

1. **Pure resistance, R = 10 Ω, 230 V–50 Hz supply.** $I_{rms}=V_{rms}/R=230/10=23\text{ A}$. With $\omega=2\pi(50)=100\pi\text{ rad/s}$: $e=230\sqrt2\sin(100\pi t)$, $i=23\sqrt2\sin(100\pi t)$ -- same phase, as expected for a resistor.
2. **Pure inductive coil, I_rms = 10 A from the same 230 V–50 Hz supply, find X_L and L.** $X_L=V_{rms}/I_{rms}=230/10=23\ \Omega$, so $L=X_L/\omega=23/(2\pi\times50)\approx0.073\text{ H}$. Current equation written with the lag explicit: $i=10\sqrt2\sin(100\pi t-\pi/2)$.
3. **A third coil problem** ($L=1.4$ H, $f=50$ Hz, a given peak current, asking for pd across the coil and its rms value) appears on the last sampled board frames but the intermediate arithmetic could not be reliably read off the image -- see the uncertain span below. Only the problem's existence and setup are recorded here, not a solved answer.


### Verify these spans
- [25:55–27:13] CONFIRMED delayed-repetition ASR corruption, and this one produces a physically WRONG statement, not just redundant text. Segments here ('equation one and two implies... E and I are in phase... E0 upon r is I0') are a near-verbatim duplicate (similarity ratio 0.82-0.99) of segments 23-25 from the RESISTOR section (491-535s) -- but they have been grafted onto the tail of the INDUCTOR derivation, where the just-completed board work (i = i0 sin(wt - pi/2), see floor_000047) unambiguously shows current LAGGING voltage by pi/2, not 'in phase'. This claim is NOT used anywhere in this note. Board frames covering this exact video-time window (floor_000077 at 1520s through floor_000089 at 1760s) show the real content that was almost certainly on the audio here: two fully worked numericals (pure-R circuit: R=10 ohm, 230V-50Hz -> Irms=23A; pure-inductive-coil circuit: Irms=10A, 230V-50Hz -> XL=23 ohm, L=0.073H) that have NO transcript representation at all -- neither these substituted segments nor any segment before/after mentions numeric values 10, 23, 230, or 0.073. Both numericals are grounded from frames only in this note (see the two worked-example claims above).
- [31:00–32:26] A third worked numerical appears on the last two sampled board frames (floor_000094, floor_000097, both past the last indexed frame at 1860s and un-timestamped beyond that): a pure inductive coil with L=1.4 H, f=50 Hz and a given I0, asking for the pd across the coil and its rms value. The intermediate working shown (e0 = I0(wL) = 10 x 2*pi*50 x 1.4) does not cleanly match the I0 value legible elsewhere on the same frame (I0=2A), so the arithmetic could not be confidently reconciled from the image alone -- possibly a board transcription-of-handwriting misread on my part, possibly the teacher's own slip, possibly a leftover value from the previous problem. No transcript coverage exists for this region at all (last transcript segment ends at 1941.4-1980.4s describing the general inductor phasor diagram, not this specific numerical) to cross-check against. Left out of the grounded claims above rather than asserting an unverified number; the problem's existence and setup (not its solved answer) is the only thing confidently established here.
- [10:12–13:29] Segments 28-35 repeat an identical short description of the resistor phase diagram ('this is the phase diagram... they are in the same phase... now if I draw a phase diagram...') four times in a row. Unlike the corruption above, this looks like genuine repeated in-class narration rather than a content-hiding artifact: the board (floor_000030 at 580s) already shows the complete resistor phasor diagram and waveform sketch fully drawn, consistent with the teacher recapping the same simple diagram while students copy it down. Flagged for awareness only; no claim in this note depends on distinguishing the four repeats from each other.

---

## AC Circuits: Pure Capacitor, Power in L/C, LR Circuit, RC Circuit, Numericals

**NCERT sections covered:** 7.5, 7.6, 7.7

### AC circuit with a pure capacitor (NCERT 7.5)

With $E=E_0\sin(\omega t)$: $q=CE_0\sin(\omega t)$, $i=dq/dt=\omega C E_0\cos(\omega t) = E_0\omega C\sin(\omega t+\pi/2)$.

**Current leads EMF by $\pi/2$** (opposite the inductor case). Writing $i=I_0\sin(\omega t+\pi/2)$ with $I_0=E_0/X_C$:
$$\boxed{X_C = \frac{1}{\omega C}} \quad\text{(capacitive reactance, unit: ohm)}$$

$X_C f = \dfrac{1}{2\pi C}=$ const $\Rightarrow$ $X_C$ vs. $f$ is a rectangular hyperbola. At $f=0$ (DC), $X_C\to\infty$ — **a capacitor blocks DC**.

**Worked numerical:** $318\,\mu$F, $230$ V, $50$ Hz. $X_C\approx10\,\Omega$; $I_\text{rms}=E_\text{rms}/X_C=230/10=23$ A; $i=I_0\sin(\omega t+\pi/2)$, $E_0=\sqrt2\,E_\text{rms}$.

### Average power in pure L or C: zero (wattless current) (NCERT 7.7)

For a pure inductor, $P=EI=E_0I_0\sin(\omega t)\sin(\omega t-\pi/2) = -\tfrac12 E_0I_0\sin(2\omega t)$ — averages to **zero** over a full cycle. Current still flows despite zero power dissipation: this is **wattless current**. (Same result, opposite sign, for a pure capacitor.)

**Practical use:** to reduce AC current with (ideally) no power loss, prefer an inductor over a resistor — old tube lights used a **choke coil** for exactly this reason.

### LR circuit (extends NCERT 7.6's phasor method)

$V_R$ and $V_L$ add as **phasors**, not algebraically (they're $90°$ out of phase — $V_L$ leads $V_R$):
$$E = \sqrt{V_R^2+V_L^2} = I\sqrt{R^2+X_L^2} = IZ, \qquad Z=\sqrt{R^2+X_L^2}~\text{(impedance)}$$
$$\phi = \tan^{-1}\frac{X_L}{R}, \qquad E = E_0\sin(\omega t+\phi)$$

**Worked numerical:** coil $L=0.5$ H, $R=100\,\Omega$, on $240$ V, $50$ Hz AC. $Z_L=\sqrt{R^2+(\omega L)^2}$; max current $I_0=E_0/Z_L\approx1.82$ A; phase angle $\phi=\tan^{-1}(\omega L/R)\approx57.5°$; **time lag** $=\phi/\omega\approx3.19\times10^{-3}$ s (current peaks this long after voltage peaks).

### RC circuit (extends NCERT 7.6's phasor method)

By analogous phasor reasoning (now $I$ leads $\varepsilon$, since current leads voltage across $C$):
$$\varepsilon = \sqrt{V_R^2+V_C^2} = I\sqrt{R^2+X_C^2} = IZ_C, \qquad Z_C=\sqrt{R^2+\frac{1}{\omega^2C^2}}$$
$$\tan\phi = \frac{X_C}{R}=\frac{1}{\omega CR}, \qquad \phi = \tan^{-1}\left(\frac{1}{\omega CR}\right)$$

**Worked numerical (setup + method):** circuit on $20$ V, $50$ Hz takes $10$ A, current leading voltage by $T/12$. $\phi = 360°/12=30°$; $R=Z_C\cos\phi$ (with $Z_C=E_\text{rms}/I_\text{rms}$); $X_C$ and hence $C$ follow similarly.

**Second numerical (unfinished in available material):** a $100$ V, $60$ W lamp operated on $220$ V, $50$ Hz mains — find $R$, $X_C$, and $C$ (a lamp-in-series-with-capacitor circuit, used to drop voltage without wasting power in a resistor).

---
*Note on this lecture's transcript:* the LR-circuit derivation repeats nearly verbatim six times back-to-back, consuming roughly 1000 seconds and drifting the transcript's own timestamps for everything after it. As a result, the entire RC-circuit derivation and its own worked numerical are completely absent from the transcript's words and are grounded here from a board frame; the final lamp-and-capacitor numerical is left unsolved since neither the transcript nor the available frames capture its resolution.


### Verify these spans
- [18:41–37:09] The LR-circuit phasor derivation (from setting up the vector-addition argument through the full phasor diagram and phase-angle formula) is transcribed correctly once, then re-transcribed nearly verbatim FIVE more times back-to-back (roughly repeating every ~150-230s from t~1262s through t~2229s) -- another instance of the severe delayed-repetition pattern found throughout this project. This consumed roughly 1000 seconds of transcript time narrating what is a single, short derivation, and appears to have drifted the transcript's own internal timestamps for everything that follows.
- [43:48–46:03] After the LR-circuit numerical, the transcript's own words move directly into setting up a second numerical (a 100V, 60W lamp operated on 220V, 50Hz mains, asked to find resistance, capacitive reactance, and capacitance) but cut off mid-question at 'and capacitance of' -- never reaching the RC-circuit derivation or its own worked numerical at all. However, a board frame (floor_000134.jpg, true video timestamp t=2660s) shows a complete RC-circuit phasor derivation AND a distinct worked numerical (a 20V/50Hz/10A circuit with current leading by T/12) already substantially solved. Since this content cannot fit within the transcript's own (drifted) timeline after the LR numerical, this confirms the earlier repetition pushed the transcript's self-reported timestamps for its final third well behind real video time. The RC-circuit derivation and this second numerical are grounded entirely from the frame; the lamp-and-capacitor numerical remains only partially stated (never solved) in the available material, so no answer is given for it here.

---

## LCR Series Circuit, Resonance, Q Factor, and LC Oscillations

**NCERT sections covered:** 7.7, 7.8, 7.9

### LCR series circuit (NCERT 7.7)

$V_R=IR$ (in phase with $I$), $V_L=IX_L$ (leads $I$ by $90°$), $V_C=IX_C$ (lags $I$ by $90°$). Since $V_L$, $V_C$ are $180°$ apart, their resultant is $V_L-V_C$ (say $V_L>V_C$), perpendicular to $V_R$:
$$E = \sqrt{V_R^2+(V_L-V_C)^2} = I\sqrt{R^2+(X_L-X_C)^2} = IZ$$
$$Z=\sqrt{R^2+(X_L-X_C)^2}~\text{(impedance)}, \qquad \tan\phi=\frac{X_L-X_C}{R}$$

### Resonance (NCERT 7.8)

When $X_L=X_C$ ($\omega L = 1/\omega C$): **resonance**. Here $Z=R$ (minimum), $\phi=0$ (purely resistive behavior), and current is **maximum**, $I_\text{max}=E/R$.
$$\boxed{\omega_r = \frac{1}{\sqrt{LC}}}$$

**Resonance curve** ($I_0$ vs. $\omega$): peaks at $\omega_r$. Smaller $R$ $\Rightarrow$ sharper peak $\Rightarrow$ more **selective** — exactly the property used to tune a radio/TV to one station among many overlapping frequencies.

#### Quality factor (Q)
$$Q = \frac{V_L\text{ (or }V_C\text{) at resonance}}{V_R\text{ at resonance}} = \frac{\omega_r L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$$
High $Q$ needs large $L$, small $R,C$.

**Half-power points** $\omega_1,\omega_2$: where $I=I_0/\sqrt2$. **Bandwidth** $BW=\omega_2-\omega_1$ (smaller for sharper curves). Second definition:
$$Q = \frac{\omega_r}{BW}$$

### LC oscillations (NCERT 7.9)

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


### Verify these spans
- [37:16–40:00] There is a genuine ~164-second gap in the transcript with no segments at all (jumping directly from the definition of LC oscillations, ending mid-sentence around t=2236s, to a segment at t=2400s that is itself mid-sentence: 'c and Um is equal to zero'). This is where the initial circuit setup (capacitor charged, connected via switch to the inductor) and the first two energy states (t=0: U_E max, U_M=0; t=T/4: U_E=0, U_M max) must have been explained, based on both the surrounding context and a board frame (floor_000123.jpg) that shows exactly this content -- the t=0 and t=T/4 circuit diagrams with their energy formulas. The initial-setup claim above is grounded from this frame rather than the transcript's own words, since no transcript segments exist for this stretch.

---

## Power in AC Circuits, Power Factor, Wattless Current, and the Transformer

**NCERT sections covered:** 7.7, 7.8

### Average power in an AC circuit (NCERT 7.7)

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

### Wattless current (general case)

Resolving $I_\text{rms}$ relative to $E_\text{rms}$ (angle $\phi$): the parallel component $I_\text{rms}\cos\phi$ delivers real power ($P_\text{avg}=E_\text{rms}I_\text{rms}\cos\phi$); the perpendicular component $I_\text{rms}\sin\phi$ delivers **zero** power (angle $90°$ to $E_\text{rms}$). This perpendicular component is the **wattless current** — current that flows without consuming power over a cycle.

### The transformer (NCERT 7.8)

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


### Verify these spans
- [24:20–28:18] The transcript's own words never get past explaining the transformer's construction (soft iron core, lamination to reduce eddy currents, coil winding) -- its last available segment ends mid-explanation of lamination/eddy currents. However, board frames confirm that, within the true video duration, the lecture goes on to derive the transformer's key working equations (epsilon_s/epsilon_p=Ns/Np=Ip/Is, step-up vs. step-down) and lists all four types of energy losses in a real transformer (flux leakage, winding resistance, eddy currents, hysteresis losses) -- none of which appear in the transcript's own words at all. Both the working-equations claim and the energy-losses claim above are grounded entirely from frames.
