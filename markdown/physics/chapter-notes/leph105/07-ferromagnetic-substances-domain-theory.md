# Ferromagnetic Substances and Domain Theory

**NCERT sections covered:** 5.5

## Ferromagnetic substances and domain theory (NCERT 5.5)

**Ferromagnetic substances** get **strongly** magnetized in the direction of an external field (contrast: paramagnetic substances are only feebly magnetized). Examples: iron, cobalt, nickel, and the alloy **Alnico** (Al, Ni, Co, Fe, and some Cu).

### Domain theory
Each atom has a magnetic dipole moment (as in a paramagnetic substance), but here neighbouring atomic dipoles **interact strongly** and spontaneously align in a common direction over a macroscopic volume called a **domain**. Each domain has its own net dipole moment, but domain directions vary randomly across the sample, so the substance's overall $M_\text{net}=0$ when $B=0$. (This is the key structural difference from paramagnetic substances, which don't form domains at all — there, each individual *atom* is independently randomly oriented.)

When placed in an external field $\vec B$: the domains themselves **orient toward $\vec B$ and grow** — domain boundaries shift so smaller domains merge into bigger ones, approaching one giant domain aligned with $B$. With the domains now aligned, $M_\text{net}\ne0$: the substance behaves as a magnet.

### Worked numerical (Curie's law, paramagnetic salt)
*(NCERT exercise, pre-rationalisation numbering 5.13)*

A paramagnetic salt has $2\times10^{24}$ dipoles, each of moment $1.5\times10^{-23}$ J/T. Placed in $B_1=0.64$ T, cooled to $T_1=4.2$ K, it reaches $15\%$ magnetic saturation. Find the total dipole moment at $B_2=0.98$ T, $T_2=2.8$ K (assume Curie's law).

- Fully-saturated total moment: $(2\times10^{24})(1.5\times10^{-23}) = 30$ J/T
- At $15\%$ saturation: $M_1 = 0.15\times30 = 4.5$ J/T
- By Curie's law ($M\propto B/T$): $M_2 = M_1\times\dfrac{B_2}{B_1}\times\dfrac{T_1}{T_2}$

---
*Note on this lecture's transcript:* the domain-theory explanation above is transcribed correctly on its first pass, but the ASR then re-transcribes the *same* explanation nearly verbatim four more times back-to-back, filling almost the entire second half of the lecture. Board frames show that, during this same stretch, the teacher had actually moved on to the worked Curie's-law numerical above — none of which made it into the transcript's own words. The numerical is grounded entirely from frames; see the flagged span below.


## Verify these spans
- [06:41–25:51] This transcript has a severe, repeated delayed-repetition problem: the same ~230-word domain-theory explanation ('this domain theory... individual atoms possess dipole moment... they interact... align... called domain... each domain has net M but it varies domain to domain... M net of whole substance is zero... place in external field... domains orient... grow... form giant domain...') is transcribed essentially verbatim FIVE separate times, at approximately t=91-399s (first, genuine pass, matching the board diagrams in floor_000019.jpg), then re-transcribed nearly word-for-word again at t=625-916s, t=918-1143s, t=1129-1371s (this one partially overlapping/out-of-order with the previous), and t=1396-1560s. Only the first pass reflects new content; the other four are ASR hallucinated repeats that silently displaced whatever the teacher actually said during those stretches. Board frames confirm real new content WAS being taught during this displaced time: from floor_000061.jpg (t=1200s) onward, the board shows a full worked Curie's-law numerical (a paramagnetic-salt problem, apparently NCERT exercise 5.13 in the pre-rationalisation numbering) being written and solved, continuing through the last available frame (floor_000074.jpg, t=1460s) -- none of which appears anywhere in the transcript's own words. The numerical is grounded entirely from these frames; the method for the final step (M2 via Curie's law ratio) is the direct, expected completion of the givens shown, but the frames do not show a final computed value for M2, so none is stated here.