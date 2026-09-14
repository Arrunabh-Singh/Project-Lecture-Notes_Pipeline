# N Identical Cells, Kirchhoff's Rules, Wheatstone Bridge, and Resistors in Series/Parallel

**NCERT sections covered:** 3.11, 3.12, 3.13

## N identical cells in series and parallel (NCERT 3.11)

### In series (with external resistance $R$)
$$I = \frac{N\mathcal E}{R+Nr}$$
- $R\gg Nr$: $I \approx N\mathcal E/R = N\times$(current from one cell) — worth connecting in series.
- $R\ll Nr$: $I\approx \mathcal E/r$, same as a single cell — no benefit.

**Conclusion:** connect cells in series only when external resistance is much greater than total internal resistance.

### In parallel (with external resistance $R$)
Net EMF $=\mathcal E$ (all cells share the same EMF between the junction points), net internal resistance $=r/N$:
$$I = \frac{\mathcal E}{R+r/N}$$
- $R\gg r/N$: $I\approx\mathcal E/R$, same as a single cell — no benefit.
- $R\ll r/N$: $I\approx N\mathcal E/r = N\times$(current from one cell) — worth connecting in parallel.

**Conclusion:** connect cells in parallel only when external resistance is much smaller than internal resistance.

## Kirchhoff's rules (NCERT 3.12)

**First law (junction rule):** $\sum I = 0$ at any junction — current in equals current out. Assume a direction for each unknown current before solving; a wrong guess simply comes out negative in the answer.

**Second law (loop rule):** around any closed loop, $\sum(\text{EMFs and }IR\text{ drops}) = 0$ (conservation of energy). **Sign convention:** a potential *drop* in the direction you're tracing (same as assumed current, or through a cell $+\to-$) is negative; a *rise* is positive. Pick one convention and use it consistently for the whole problem — mixing conventions mid-solution gives wrong answers.

**Solving a circuit:** assign unknown currents using the junction rule (reduces the count of unknowns needed), then write loop equations for enough independent loops to match the number of remaining unknowns, and solve simultaneously.

## Wheatstone bridge (NCERT 3.13)

Four resistors $R_1,R_2,R_3,R_4$ in a diamond/bridge arrangement, galvanometer (resistance $G$) across the diagonal. **Balance condition:**
$$\boxed{\frac{R_1}{R_2} = \frac{R_3}{R_4}}$$
When balanced, the galvanometer's two ends are at equal potential, so **no current flows through it** ($I_G=0$) — provable by applying the loop rule to two loops of the bridge and setting $I_G=0$.

**Practical use:** in a balanced bridge, the galvanometer-arm resistor can simply be dropped from the circuit for equivalent-resistance calculations, leaving a simpler series-parallel network.

## Resistors in series and parallel: worked simplifications

- Two resistors in parallel: $R_{eff} = \dfrac{R_1R_2}{R_1+R_2}$ (only valid for exactly two).
- For symmetric networks, first check whether multiple labelled points are actually the *same* electrical node (connected by plain, zero-resistance wire) — relabelling them can reveal resistors are secretly all in parallel between the same two effective points. Example: three $1\,\Omega$ resistors that turn out to all sit between the same two nodes $A,B$ give $R_{eff}=1/3\,\Omega$ by the reciprocal rule.

---
*Note on this lecture's transcript:* the final worked example (a 5-resistor bridge-shaped network) is left unsolved -- the recording ends with it redrawn in equivalent bridge form, before a numeric answer is reached in either the transcript or the board frames. See the flagged span below.


## Verify these spans
- [47:35–48:09] This is a clean truncation at the natural end of the recording rather than a repetition or substitution artifact: the transcript's last segment ends mid-sentence while labelling a new 5-resistor (R1-R5) network for one final effective-resistance example, and the last board frame (floor_000144.jpg, at the true end of the recording) shows that same network redrawn in its equivalent Wheatstone-bridge diamond shape, ready for balance-condition analysis -- but the lecture simply ends there, with no numeric answer worked out in either the transcript or any captured frame. This final example is therefore left unsolved in this note rather than guessed at.