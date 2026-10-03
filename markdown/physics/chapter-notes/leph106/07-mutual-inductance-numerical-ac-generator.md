# Mutual Inductance of Two Coaxial Solenoids, Worked Numerical, and the AC Generator

**NCERT sections covered:** 6.7, 6.8

## Mutual inductance of two coaxial solenoids (NCERT 6.7)

Two long coaxial solenoids $S_1$ (inner, $n_1$ turns/length, $N_1$ turns, area $A_1$) and $S_2$ (outer, $n_2$, $N_2$, $A_2$), both length $l$. Current $I$ in $S_1$ creates:
$$B_1 = \mu_0 n_1 I = \mu_0\frac{N_1}{l}I$$
Flux linked with $S_2$ (using $A_1$, the area where $B_1$ actually exists):
$$\phi_2 = N_2 B_1 A_1 = \mu_0\frac{N_1 N_2 A_1}{l}I \quad\Rightarrow\quad \boxed{M_{21} = \frac{\mu_0 N_1 N_2 A_1}{l}}$$

**Reciprocity:** a symmetric argument (current in $S_2$ instead, using whichever cross-section is common/smaller) gives $M_{12}=M_{21}$ — the mutual inductance is the same either way.

### Worked numerical (classic two-loop problem)
A circular loop of radius $0.3$ cm lies parallel to a much bigger circular loop of radius $20$ cm, centres $15$ cm apart. (a) Flux linking the bigger loop for $I=0.2$ A in the smaller loop? (b) Mutual inductance?

**Method:** treat the small loop as a point dipole; use the big loop's on-axis field $B=\dfrac{\mu_0}{2}\dfrac{I a_2^2}{(a_2^2+x^2)^{3/2}}$ at the small loop's location, then $\phi = \pi a_1^2 B$ (uniform over the tiny loop's area); $M=\phi/I$.

## The AC generator (NCERT 6.8)

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


## Verify these spans
- [05:03–37:19] This is the most severe delayed-repetition failure found anywhere in this project: after correctly deriving M21 (t=3-303s), the transcript gets stuck setting up the M12=M21 proof ('to calculate M12, consider current flowing through S2... magnetic field generates only in area A2... M12 due to 2... n1 n2 mu0 a2 upon l') and re-transcribes this SAME ~230-second block at least SEVEN times back-to-back, continuing almost verbatim all the way to the transcript's very last word ('flowing', at t=2242.975s, cut off mid-sentence). Essentially the entire remaining 86% of this lecture's real content -- completion of the M12=M21 proof, the worked mutual-inductance numerical (the lecture's own second named topic), and the ENTIRE AC generator topic (construction, working, and the full sinusoidal-EMF derivation -- the lecture's own third named topic) -- is completely absent from the transcript's own words. Board frames confirm all of this content was genuinely taught and written out in full within the true 2239.5s runtime (the numerical at real t~1180s, the complete AC generator section by real t~2220s, near the very end of the video). Every claim in this note beyond the initial M21 derivation is grounded entirely from frames, not the transcript's own words.