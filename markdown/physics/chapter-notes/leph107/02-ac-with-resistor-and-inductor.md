# AC Circuits with Only R and Only L (Phasors, Resistor, Pure Inductor)

**NCERT sections covered:** 7.2, 7.3, 7.4

## Phasors

A phasor is a vector that rotates about the origin with angular speed $\omega$. Its vertical (projected) component at any instant gives the instantaneous value of the quantity it represents. Both current and voltage in an AC circuit are represented as phasors -- $i_0$ and $e_0$ are the phasor lengths (amplitudes), and the projection onto the vertical axis traces out $i_0\sin\omega t$ or $e_0\sin\omega t$ as the phasor sweeps around.

## AC circuit with only a resistor

For an ideal resistor $R$ on source $e=e_0\sin\omega t$, Kirchhoff's law gives directly
$$e_0\sin\omega t = iR \quad\Rightarrow\quad i = i_0\sin\omega t,\quad i_0=\frac{e_0}{R}$$
Current and voltage are **in phase** -- same $\sin\omega t$ dependence, zero phase difference. On a phasor diagram the $E_0$ and $I_0$ phasors point along the same line; on a $y$-$t$ graph the two sinusoids rise and fall together.

**Aside -- why AC needs its own ammeter design.** A DC ammeter placed in an AC circuit reads the *mean* current, which is zero over a full cycle, so it shows a zero reading. Purpose-built AC ammeters instead exploit the **heating effect** of current ($H\propto i^2Rt$): since $i^2$ is never negative, this gives a genuine non-zero reading, but because the response is proportional to $i^2$ rather than $i$, the scale spacing on an AC ammeter is unequal -- markings spread further apart at higher readings -- rather than the evenly-spaced scale on a DC ammeter.

## AC circuit with only (pure) inductance

For an ideal inductor $L$ (no resistance) on the same source, the induced EMF is $e=-L\,di/dt$, so by Kirchhoff's law
$$e = L\frac{di}{dt} \quad\Rightarrow\quad di = \frac{1}{L}e\,dt \quad\Rightarrow\quad i = \frac{1}{L}\int e_0\sin(\omega t)\,dt = \frac{e_0}{\omega L}\big[-\cos\omega t\big]$$
Rewriting $-\cos\omega t$ as $\sin(\omega t - \pi/2)$ (worked out on the board via $\sin(\pi/2-\omega t)=\cos\omega t$, then reversing sign) gives the standard form
$$i = \frac{e_0}{\omega L}\sin\left(\omega t - \frac{\pi}{2}\right) = i_0\sin\left(\omega t-\frac{\pi}{2}\right),\qquad i_0=\frac{e_0}{\omega L}$$
Defining **inductive reactance** $X_L=\omega L$ (unit ohm, playing the same role $R$ plays for a resistor), this is $i_0=e_0/X_L$.

**Phase relationship.** Current **lags** voltage by $\pi/2$ (a quarter cycle) in a pure inductor -- when the voltage is at its peak, current is zero, and when voltage is zero, current is at its peak. This is the opposite of the resistor case and is drawn on the board both as an $e,i$-vs-$t$ graph and as a phasor diagram with the $I_0$ phasor sitting $90°$ behind $E_0$.

## Worked numericals (board)

1. **Pure resistance, R = 10 Ω, 230 V–50 Hz supply.** $I_{rms}=V_{rms}/R=230/10=23\text{ A}$. With $\omega=2\pi(50)=100\pi\text{ rad/s}$: $e=230\sqrt2\sin(100\pi t)$, $i=23\sqrt2\sin(100\pi t)$ -- same phase, as expected for a resistor.
2. **Pure inductive coil, I_rms = 10 A from the same 230 V–50 Hz supply, find X_L and L.** $X_L=V_{rms}/I_{rms}=230/10=23\ \Omega$, so $L=X_L/\omega=23/(2\pi\times50)\approx0.073\text{ H}$. Current equation written with the lag explicit: $i=10\sqrt2\sin(100\pi t-\pi/2)$.
3. **A third coil problem** ($L=1.4$ H, $f=50$ Hz, a given peak current, asking for pd across the coil and its rms value) appears on the last sampled board frames but the intermediate arithmetic could not be reliably read off the image -- see the uncertain span below. Only the problem's existence and setup are recorded here, not a solved answer.


## Verify these spans
- [25:55–27:13] CONFIRMED delayed-repetition ASR corruption, and this one produces a physically WRONG statement, not just redundant text. Segments here ('equation one and two implies... E and I are in phase... E0 upon r is I0') are a near-verbatim duplicate (similarity ratio 0.82-0.99) of segments 23-25 from the RESISTOR section (491-535s) -- but they have been grafted onto the tail of the INDUCTOR derivation, where the just-completed board work (i = i0 sin(wt - pi/2), see floor_000047) unambiguously shows current LAGGING voltage by pi/2, not 'in phase'. This claim is NOT used anywhere in this note. Board frames covering this exact video-time window (floor_000077 at 1520s through floor_000089 at 1760s) show the real content that was almost certainly on the audio here: two fully worked numericals (pure-R circuit: R=10 ohm, 230V-50Hz -> Irms=23A; pure-inductive-coil circuit: Irms=10A, 230V-50Hz -> XL=23 ohm, L=0.073H) that have NO transcript representation at all -- neither these substituted segments nor any segment before/after mentions numeric values 10, 23, 230, or 0.073. Both numericals are grounded from frames only in this note (see the two worked-example claims above).
- [31:00–32:26] A third worked numerical appears on the last two sampled board frames (floor_000094, floor_000097, both past the last indexed frame at 1860s and un-timestamped beyond that): a pure inductive coil with L=1.4 H, f=50 Hz and a given I0, asking for the pd across the coil and its rms value. The intermediate working shown (e0 = I0(wL) = 10 x 2*pi*50 x 1.4) does not cleanly match the I0 value legible elsewhere on the same frame (I0=2A), so the arithmetic could not be confidently reconciled from the image alone -- possibly a board transcription-of-handwriting misread on my part, possibly the teacher's own slip, possibly a leftover value from the previous problem. No transcript coverage exists for this region at all (last transcript segment ends at 1941.4-1980.4s describing the general inductor phasor diagram, not this specific numerical) to cross-check against. Left out of the grounded claims above rather than asserting an unverified number; the problem's existence and setup (not its solved answer) is the only thing confidently established here.
- [10:12–13:29] Segments 28-35 repeat an identical short description of the resistor phase diagram ('this is the phase diagram... they are in the same phase... now if I draw a phase diagram...') four times in a row. Unlike the corruption above, this looks like genuine repeated in-class narration rather than a content-hiding artifact: the board (floor_000030 at 580s) already shows the complete resistor phasor diagram and waveform sketch fully drawn, consistent with the teacher recapping the same simple diagram while students copy it down. Flagged for awareness only; no claim in this note depends on distinguishing the four repeats from each other.