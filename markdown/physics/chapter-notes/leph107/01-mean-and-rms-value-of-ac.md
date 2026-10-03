# Mean (Average) and RMS Value of Alternating Current

**NCERT sections covered:** 7.1, 7.2

## Introduction to AC

Alternating current varies continuously in magnitude and periodically reverses direction, written as $i = i_0\sin(\omega t)$ (or equivalently $i_0\cos\omega t$, since both sine and cosine are periodic -- the lecture notes both forms are used interchangeably depending on where $t=0$ is taken). Time period $T$ is the time for one cycle; frequency $f = 1/T = \omega/2\pi$.

Domestic AC supply in India is 50 Hz. Since current crosses zero twice per cycle, at 50 Hz a bulb driven by mains current is effectively "off" 100 times a second -- invisible to the eye because of persistence of vision. The lecture notes that at deliberately low frequencies (e.g. a hand-cranked classroom generator) this flicker becomes visible as the bulb visibly switching on and off.

Alternating EMF follows the same form: $e = e_0\sin(\omega t)$ or $e_0\cos(\omega t)$.

## Mean (average) value of AC

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

## RMS (root mean square) value of AC

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

## Worked numericals (board-only)

The board (visible from roughly 1780s to the end of the lecture) works through six short problems applying the $i_0=\sqrt2\, I_{rms}$ / $I_{rms}=0.707\,i_0$ relations. These do not have matching spoken narration in the available transcript (see uncertain span below) but are clearly legible on the board:

1. $E_{rms}=220\text{ V}$ (household mains) $\Rightarrow E_0=\sqrt2\times220\approx311\text{ V}$ -- matches NCERT's own worked household-voltage figure exactly.
2. $I_{rms}=10\text{ A}\Rightarrow I_0=\sqrt2\times10\approx14.14\text{ A}$.
3. $i=6\sin(314t)\text{ A}$ (i.e. $\omega=314\text{ rad/s}\approx2\pi\times50\text{ Hz}$) $\Rightarrow I_0=6\text{ A}$, $I_{rms}=0.707\times6\approx4.24\text{ A}$.
4. Given rms voltage during a half cycle, find peak voltage and mean value -- set up the same way as above ($E_0=\sqrt2\,E_{rms}$, $E_m=0.637E_0$).
5. Time for current starting from zero to reach its peak value: $t=T/4$ (one quarter cycle), read directly off the sine waveform.
6. RMS value of a **square wave** alternating between $+2$ A and $-2$ A: since the sinusoidal formula $i_0/\sqrt2$ does not apply to a non-sinusoidal waveform, the board instead applies the defining recipe directly -- square the current, average the squares, take the square root: $I_{rms}=\sqrt{\dfrac{I_0^2+I_0^2+I_0^2}{3}}=2\text{ A}$. This is a good check that the student understands "root-mean-square" as a procedure, not just a formula tied to sine waves.


## Verify these spans
- [29:39–32:49] Delayed-repetition ASR artifact: segment starting 1779.5s ('Now, see here, in this case, let's try to understand this definition first...') is repeated almost verbatim at 1944.3s, with segments 65-66 in between (1845.9-1944.3s) re-covering the same 'same amount of heat in a given resistance' phrasing already said at 1720.7s. Net effect is only a short (~165s) block of redundant/looped narration around the RMS heat-definition setup, not a loss of new content -- board frames (floor_000064 at 1260s onward) show the derivation already fully written and progressing steadily, so nothing appears to have been dropped.
- [37:15–38:25] Transcript ends mid-sentence ('Now for AC what you can do is heat produced by AC circuit in time T') without ever verbally stating the final RMS-current derivation or its conclusion I_rms = i0/√2. The segment's declared end (2305.8s) also overshoots the reported lecture duration (2261.8s) by ~44s, suggesting either truncation or an imprecise end-timestamp for the final utterance. However, board frames from ~1580s onward (floor_000080, floor_000083) already show this exact derivation completed and boxed (I_rms = i0/√2 = 0.707 i0, E_rms = 0.707 e0), and frames from 1780s-2240s show it being applied confidently across six solved numericals ending with a non-sinusoidal square-wave example -- so the material was clearly taught in this lecture even though the ASR did not capture the teacher saying the final conclusion aloud. Grounded from frames per the workflow's guidance for this exact failure pattern.
- [25:19–26:10] Segments 56-57 consist of the short phrase 'So, mean or average value of AC is that direction' repeated verbatim ~38 times in a row (a stutter/loop artifact within the ASR output itself, distinct from the delayed-repetition pattern above). Segment durations (21-30s) are plausible for real elapsed time, and the derivation resumes cleanly on both sides (Im=2i0/pi immediately before, 0.637i0 immediately after), so this looks like a local ASR glitch rather than missing content -- flagging for awareness, not treated as a content gap.