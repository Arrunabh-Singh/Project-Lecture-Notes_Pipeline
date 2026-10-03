# Current Electricity

*Class XII CBSE Physics · Chapter 3 · 7 lectures, in order.*

*NCERT sections covered: 3.2, 3.3, 3.4, 3.5, 3.5.1, 3.6, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13.*

*Transcribed from the teacher's recorded lectures and checked against the
board frames and the NCERT text. Equations are board-grounded; any span the
transcript could not resolve confidently is flagged in place.*

---

## Electric Current, Current Density, Drift Velocity and Mobility

**NCERT sections covered:** 3.2, 3.3, 3.4, 3.5, 3.5.1

### Electric current (NCERT 3.2)

Current is defined as the rate of flow of charge through a cross-sectional area:
$$I = \frac{Q}{t}, \qquad I = \frac{dQ}{dt}\ \text{(instantaneous form)}$$
SI unit: the **ampere** (A), with $1\text{ A} = 1\text{ C}/1\text{ s}$ -- a current of 1 A means 1 coulomb crosses the cross-section every second.

**Current is a scalar**, not a vector, even though it is conventionally drawn with an arrow: it does not obey the law of vector addition. The teacher's example -- current through a wire is the same value $I$ whether the wire runs straight or is bent/curled -- matches NCERT's own point (a curved path would need vector resolution into components if current were a vector, but the measured current is identical regardless of the wire's shape).

### Current density (NCERT 3.4)

Current density $\vec{J}$ is current per unit area, a **vector** directed along the flow of current:
$$J = \frac{I}{A}$$
If the cross-section is tilted at angle $\theta$ to the current direction, the effective area is $A\cos\theta$, so
$$J = \frac{I}{A\cos\theta}$$
For a conductor whose cross-section changes along its length (same $I$ everywhere by charge conservation, but $A$ -- and hence $J$ -- varies), current density in general varies point to point. Since $\vec{J}$ and $\vec{A}$ are both vectors, the relation is written as a dot product, and in integral form (for $J$ non-uniform over the area):
$$I = \vec{J}\cdot\vec{A}, \qquad I = \int_A \vec{J}\cdot d\vec{A}$$
Unit of current density: $\text{A/m}^2$.

### Random thermal motion of free electrons (NCERT 3.5, cf. Example 3.1(b))

In a conductor with no applied field, free electrons move randomly, colliding with fixed ions. Each electron's thermal speed follows from kinetic theory:
$$\frac{1}{2}mv^2 = \frac{3}{2}k_BT \implies v = \sqrt{\frac{3k_BT}{m}}$$
At room temperature this comes out to about $10^5\ \text{m/s}$ -- very fast, but because the $N$ free electrons' velocities $u_1, u_2, \ldots, u_N$ are randomly oriented, their vector average is zero:
$$\text{average velocity} = \frac{\vec{u}_1+\vec{u}_2+\cdots+\vec{u}_N}{N} = 0$$
So despite the huge thermal speed, there is **no net current** without an applied field.

### Drift velocity (NCERT 3.5, eq. 3.14-3.17)

Switching on an electric field $\vec{E}$ exerts a force on each (negatively charged) electron:
$$\vec{F} = -e\vec{E} \quad(\text{opposite to } \vec{E}), \qquad \vec{a} = \frac{\vec{F}}{m} = -\frac{e\vec{E}}{m}$$
Current direction is conventionally opposite to the direction electrons actually drift. Averaging the velocity gained since each electron's *last collision*, over the average time between collisions (the **relaxation time** $\tau$), gives the drift velocity:
$$\vec{v}_d = \vec{a}\tau = -\frac{e\vec{E}}{m}\tau$$
Plugging in typical numbers gives $v_d \approx 1\ \text{mm/s}$ -- consistent with NCERT's Example 3.1(a) result of $\approx 1.1\ \text{mm/s}$ for a copper wire -- i.e. roughly $10^{-8}$ times the thermal speed, even though it's this tiny drift, not the large thermal motion, that constitutes the current.

### Mobility (NCERT 3.5.1)

Mobility $\mu$ (a scalar) is the magnitude of drift velocity per unit electric field:
$$\mu = \frac{v_d}{E}$$
Substituting $v_d = eE\tau/m$:
$$\boxed{\mu = \frac{e\tau}{m}}$$
Mobility is **independent of $E$** -- it depends only on the electron's charge, mass, and the relaxation time $\tau$. Since $\tau$ decreases as temperature rises (more frequent collisions), $\mu$ also decreases with rising temperature. Combining with the earlier current-density relation gives current density directly in terms of mobility:
$$\vec{J} = -ne\vec{v}_d = ne\mu\vec{E}$$

---
*Note on this lecture's transcript:* coverage checks pass cleanly (ratio 1.02, no adjacent-repetition, and the non-adjacent duplicate scan found zero flagged pairs across all 65 segments) -- this lecture does **not** show the delayed-repetition ASR artifact found in some other lectures in this chapter. However, the transcript's own narration runs out about 12 seconds before the video's true end, right as the teacher begins the formal N-electron derivation of drift velocity. The quantitative drift-velocity result ($v_d=a\tau$, $v_d\approx1$ mm/s) and the entire mobility section above (definition, boxed formula, temperature dependence, and the final $J=ne\mu E$ relation) are grounded entirely from board frames, not narration -- the board runs ahead of the spoken explanation for this last stretch. See the flagged span below for exactly which frames and why this reads as "recording ran out," not a fabrication/repetition artifact.


### Verify these spans
- [30:51–31:03] The transcript's final segment (starting 1851s, 'let us suppose there are n electrons...') cuts off mid-sentence right as the teacher begins the formal N-electron derivation of drift velocity (NCERT eq. 3.16-3.17) -- the transcript never verbally states vd = a*tau = -eE*tau/m, the ~1 mm/s numeric estimate, the mobility definition, mu = e*tau/m, or J = n*e*mu*E. This is NOT the delayed-repetition ASR artifact found elsewhere in this chapter: the non-adjacent duplicate scan found 0 flagged pairs across all 65 segments, coverage passes cleanly (ratio 1.02), and every segment from 1396s onward is distinct, coherent, natural classroom speech (direction-of-current, then F=-eE, then Newton's-second-law acceleration) with no verbatim or near-verbatim repeats -- it reads like real audio that simply runs out at the video's true duration, not fabrication or a re-transcription loop. Board frames, however, show this exact content already written well before the transcript catches up: floor_000063 (1240s) has the boxed vd = -eE*tau/m and vd~1mm/s, and floor_000085 (1680s) through floor_000093 (1840s) show a clean incremental build of the mobility section (heading -> ratio definition -> mu=vd/E -> mu=e*tau/m boxed -> mu independent of E, temperature dependence -> J=neuE) -- a genuine progression, not an out-of-place page, and a direct continuation of the derivation the transcript was mid-way through narrating. The teacher appears to have written ahead of his own narration for this final stretch; all claims above with transcript_span=None are grounded from these frames alone.

---

## Resistance, Resistivity, Conductivity and Ohmic vs Non-Ohmic Conductors

**NCERT sections covered:** 3.4, 3.5, 3.6, 3.8

### Ohm's law -- macroscopic form (NCERT 3.4)

If a conductor's temperature is constant, potential difference is directly proportional to current:
$$V \propto I \implies V = IR$$
where $R$ is the resistance (unit: ohm, $\Omega$; $1\ \Omega = 1\text{ V}/1\text{ A}$). A $V$-vs-$I$ plot is a straight line through the origin with slope $R$ (matching $y=mx$); an $I$-vs-$V$ plot instead has slope $1/R$ -- worth checking which axis is which before reading off a slope as $R$ or $1/R$.

Physically, resistance is the **hindrance offered to current flow**: microscopically, drifting electrons collide with the fixed positive ions of the lattice. Raising the temperature makes the ions vibrate with larger amplitude, increasing collision frequency and hence resistance.

### Resistivity (NCERT 3.4)

Resistance depends on the conductor's geometry: $R\propto l$ (longer wire, more collisions to traverse) and $R\propto 1/A$ (larger cross-section, more parallel paths, less resistance). Combining:
$$R = \frac{\rho l}{A}$$
where $\rho$, the **resistivity**, depends only on the material's nature and temperature -- crucially, **not** on the wire's dimensions. The teacher's analogy: the density of water is the same whether you take a drop, a glass, or a bucket of it -- resistivity of copper is the same whether the copper wire is thin, thick, long, or shaped as a sheet.

**Resistance vs. resistivity:**

| | depends on dimensions (l, A)? | depends on material & temperature? | SI unit |
|---|---|---|---|
| Resistance $R$ | yes | yes | $\Omega$ |
| Resistivity $\rho$ | no | yes | $\Omega\cdot\text{m}$ |

### Deriving $\rho = m/(ne^2\tau)$ (NCERT 3.5, eq. 3.23)

Starting from the drift-velocity relation $I = nev_dA$ (from the previous lecture) with $v_d = eE\tau/m$ and $E=V/l$:
$$I = neA\cdot\frac{eE\tau}{m} = \frac{ne^2A\tau}{m}\cdot\frac{V}{l}$$
Rearranging for $V$ and comparing with both $V=IR$ and $R=\rho l/A$:
$$R = \frac{m}{ne^2\tau}\cdot\frac{l}{A} \implies \boxed{\rho = \frac{m}{ne^2\tau}}$$
where $n$ is the free-electron (charge) density, $\tau$ the average relaxation time, $e$ the electron's charge and $m$ its mass.

**Temperature dependence (metals):** as $T$ increases, $\tau$ decreases (more frequent collisions), so $\rho$ increases with temperature. Since $\rho\propto 1/n$, a material with higher free-electron density (e.g. copper) has lower resistivity than one with lower density (e.g. an alloy or iron); silver has the least resistivity of common conductors, though copper/aluminium are used for practical wiring.

### Conductance and conductivity

**Conductance** $g = 1/R = I/V$, unit mho -- this specific term is not part of the NCERT chapter text but is a standard reciprocal-of-resistance quantity introduced as useful vocabulary.

**Conductivity** (NCERT-covered, eq. 3.23), the reciprocal of resistivity:
$$\sigma = \frac{1}{\rho} = \frac{ne^2\tau}{m}$$

### Macroscopic vs. microscopic Ohm's law (NCERT eq. 3.3, 3.13)

$V=IR$ relates external, circuit-level quantities (voltage, current, resistance) -- the teacher calls this the **macroscopic form**. There is also a **microscopic form** relating quantities internal to the conductor:
$$\vec{J} = \sigma\vec{E}$$
**Derivation:** from $I=nev_dA$, dividing both sides by $A$ gives $J = nev_d$; substituting $v_d = eE\tau/m$:
$$J = ne\cdot\frac{eE\tau}{m} = \frac{ne^2\tau}{m}E = \sigma E$$

### Ohmic and non-ohmic conductors (NCERT 3.6, "Limitations of Ohm's Law")

Conductors whose $V$-$I$ graph is **linear** (they obey Ohm's law) are **ohmic conductors**. Conductors that do **not** obey Ohm's law are **non-ohmic**, in (at least) three distinct ways:

1. **$V$-$I$ graph is non-linear** -- e.g. metals at high currents.
2. **The relation between $V$ and $I$ depends on the sign of $V$** -- e.g. a junction diode (reversing $V$ does not simply reverse $I$).
3. **The $V$-$I$ relation is non-unique** -- for the same voltage $V$, the current may take two or more values -- e.g. a thyristor (an S-shaped curve with a folded-back region).

This matches NCERT's three limitations (a)-(c) closely, though the board's example for case 3 is a **thyristor** rather than NCERT's GaAs -- both are valid real devices with a non-unique $V$-$I$ curve, just a different illustrative choice.

---
*Note on this lecture's transcript:* the non-adjacent duplicate scan flagged 9 pairs, but every one turned out to be a short, genuinely-reused stock phrase or formula recited at two different points of one continuous, non-repeating derivation (e.g. stating a formula as a derivation's goal, then again once it's actually reached) -- not the delayed re-transcription artifact found elsewhere in this chapter. The one real gap: the transcript's spoken narration essentially stops at the *announcement* of "ohmic and non-ohmic conductors" (its last real content, ending right at the video's true duration), while the board already shows the complete, worked-through NCERT 3.6 content well before that announcement timestamp. The whole ohmic/non-ohmic section above is grounded from board frames alone -- see the flagged span below for the frame-by-frame detail.


### Verify these spans
- [31:25–31:37] The transcript's last two segments (1885-1899s) only ANNOUNCE the topic -- 'when we talk of conductors, there are two types...ohmic...and non-ohmic...here we are going to talk about ohmic and non-ohmic conductors' -- and then the transcript ends (its very last segment's start, 1901s, is already past the true video duration of 1897.5s, inside only the small fixed rounding grace, so essentially nothing more was narrated). The actual ohmic/non-ohmic content -- the definitions and all three NCERT 3.6 sub-cases (i-iii), matching (a)-(c) almost exactly, down to worked diagrams for each -- is fully present on the board, built up progressively across frames floor_000079 (1560s, heading + J=sigma*E just finished) through floor_000089 (1760s, both definitions + case (i) with the metals-at-high-current graph), floor_000091 (1800s, case (ii), junction diode), and floor_000093-floor_000095 (1840-1880s, case (iii) built up step by step with the thyristor S-curve). This board sequence runs from 1560s to 1880s -- i.e. it was mostly already written well BEFORE the transcript's narration even announces starting the topic at ~1885-1901s. That is the reverse of lecture 1's pattern (board slightly ahead of speech near the very end) and large enough (over 300s) that it may reflect ASR timestamp drift accumulating over this single-shot ~32-minute transcription rather than the teacher truly writing 5+ minutes silently ahead of his own explanation. Either way, the automated non-adjacent duplicate scan found no repeated block here (all 9 flagged pairs earlier in this transcript are short, genuinely reused stock phrases/formulas within one continuous derivation, not a re-transcription loop), so this reads as a timestamp/coverage mismatch rather than fabrication. The final ohmic/non-ohmic claim above is grounded entirely from these board frames.

---

## Joule's Law, Electric Power, Bulb Ratings, kWh, and Temperature Coefficient of Resistance

**NCERT sections covered:** 3.8, 3.9

### Joule's law of heating (NCERT 3.9)

Current through a resistor converts electrical energy into heat. For charge $dQ$ moved across potential difference $V$ in time $dt$: $dW = V\,dQ = VI\,dt$. Total work (constant $V,I$) over time $t$:
$$W = \int VI\,dt = VIt$$
Using $V=IR$, this heat can also be written:
$$W = I^2Rt = \frac{V^2}{R}t$$

### Electric power (NCERT 3.9)

$$P = \frac{W}{t} = VI = I^2R = \frac{V^2}{R}$$
SI unit: **watt** (W) $=$ J/s.

#### Bulb rating numerical
A bulb rated $220$ V, (worked example: $20$ W) consumes that many joules per second at $220$ V.
- **Max permissible current:** $I = P/V$ (e.g. $20/220 = 1/11$ A)
- **Filament resistance:** from $P=V^2/R$, $R = V^2/P$ (e.g. $220\times220/20\ \Omega$)

#### Kilowatt-hour
Electricity bills measure energy in **kilowatt-hours (kWh)**, not joules: energy $=$ power (kW) $\times$ time (h). $1$ kWh is the energy an appliance rated $1$ kW consumes running for $1$ hour:
$$1~\text{kWh} = 1000~\text{W}\times3600~\text{s} = 3.6\times10^6~\text{J}$$

### Temperature coefficient of resistance (NCERT 3.8)

$$\Delta R \propto R\,\Delta T \;\Rightarrow\; \alpha = \frac{\Delta R}{R\,\Delta T} = \frac{R_t-R_0}{R_0\,\Delta T} \;\Rightarrow\; \boxed{R_t = R_0(1+\alpha\,\Delta T)}$$
The same relation holds for resistivity $\rho$: $\rho_t=\rho_0(1+\alpha\,\Delta T)$. (This mirrors the general pattern for thermal expansion coefficients: $\alpha=\Delta L/L_0\Delta T$, $\beta=\Delta A/A_0\Delta T$, $\gamma=\Delta V/V_0\Delta T$, with $\alpha:\beta:\gamma=1:2:3$.)

#### By material class
- **Metals:** $\alpha$ positive, comparatively large — resistivity **rises** with temperature.
- **Semiconductors:** $\alpha$ **negative** — resistivity **falls** as temperature rises (more charge carriers become available at higher $T$).
- **Alloys** (manganin, constantan, nichrome): $\alpha$ very small — resistance is nearly temperature-independent, which is exactly why these are the materials chosen for precision resistors and heating elements.

---
*Note on this lecture's transcript:* the entire temperature-coefficient section above is grounded from board frames -- the transcript itself never reaches it in words, instead getting sidetracked into a kWh digression and stopping there. See the flagged span below. "Carbon resistor" (also named in this lecture's filename) was not found in either the transcript or the sampled frames and is not covered in this note.


### Verify these spans
- [27:44–35:29] The transcript's real narration (43 segments, no detected repetition) runs through a coherent introduction to 'different types of resistors' (t=1530-1664s: 'standard coil resistors...') before pivoting to a kilowatt-hour digression ('before understanding [resistor types], I just missed out one more thing...') that then runs to the transcript's last segment, ending mid-explanation of the kWh-to-joules conversion. The transcript never returns to resistor types, and never mentions temperature coefficient of resistance in words at all. Board frames tell a fuller story: floor_000071.jpg through floor_000095.jpg (spanning roughly t=1400-1880s, overlapping and extending past the transcript's own covered range) show a complete, thorough 'temperature coefficient of resistance' derivation plus a three-way comparison of metals, semiconductors, and alloys -- none of it narrated in the available transcript. All temperature-coefficient claims above are grounded entirely from these frames. Separately, 'carbon resistor' -- named in this lecture's own filename alongside temperature coefficient -- was NOT found in either the transcript or any of the 32 sampled board frames; rather than guess at its content, it is omitted from this note entirely.

---

## Internal Resistance, EMF, Terminal PD, and Combination of Cells

**NCERT sections covered:** 3.10, 3.11

### Internal resistance (NCERT 3.10)

A cell's electrolyte hinders current flow just like an external resistor. Internal resistance $r$ depends on the electrolyte's nature, temperature, and concentration; it is directly proportional to electrode separation $l$ and inversely proportional to immersed electrode area $A$:
$$r = \frac{cl}{A}\quad\text{(at a given temperature)}$$
$r$ **decreases** with increasing temperature, and **increases** as a cell ages with use.

### EMF and terminal potential difference (NCERT 3.10)

**EMF** ($\mathcal E$): despite the name, has nothing to do with force — unit is the **volt**, not newton (a historical misnomer). Defined as work done per unit charge; equals the potential difference across a cell's terminals when **no current is drawn** (open circuit).

**Terminal PD** ($V$): once current flows through an external resistor $R$ (closed circuit), the measured PD across the cell's terminals:
$$\mathcal E = V + Ir \quad\Leftrightarrow\quad V = \mathcal E - Ir$$
During **discharging** (normal use), $\mathcal E > V$. Rearranged forms: $I = \dfrac{\mathcal E}{R+r}$, and $r = \dfrac{\mathcal E - V}{V}R$ (this last form is reused later for the potentiometer method of measuring internal resistance).

**During charging**, current direction through the cell reverses: $V = \mathcal E + Ir$, so $V > \mathcal E$.

### Combination of cells (NCERT 3.11)

**Sign-convention / potential-walk method:** pick a current direction; a potential *drop* in the direction of current is negative, a *rise* is positive. Walking from one circuit point to another, sum each EMF and $Ir$ term with its sign — e.g. $V_A - V_B = \mathcal E_1 - ir_1$ for one branch. (This same method is reused later for potentiometer problems.)

#### Cells in parallel
Two cells $(\mathcal E_1,r_1)$ and $(\mathcal E_2,r_2)$ between the same points $A,B$, supplying $I_1=\dfrac{\mathcal E_1-V}{r_1}$, $I_2=\dfrac{\mathcal E_2-V}{r_2}$, with $I=I_1+I_2$. Solving for $V$ in terms of total current $I$ gives an equivalent single cell:
$$\mathcal E_{eq} = \frac{\mathcal E_1 r_2+\mathcal E_2 r_1}{r_1+r_2}, \qquad \frac{1}{r_{eq}} = \frac{1}{r_1}+\frac{1}{r_2}\quad(\text{i.e. } r_{eq}=\frac{r_1 r_2}{r_1+r_2})$$
$$V = \mathcal E_{eq} - I\,r_{eq}$$
Internal resistances combine exactly like the reciprocal (parallel) rule for resistors; the equivalent EMF is a resistance-weighted combination of the two.

---
*Note on this lecture's transcript:* the cells-in-parallel derivation above is grounded entirely from a board frame near the true end of the lecture -- the transcript's own narration stops mid-way through setting up the series case. See the flagged span below.


### Verify these spans
- [23:41–33:10] The transcript's real (non-repeated) narration introduces 'combination of cells' and demonstrates the sign-convention potential-walk method for a series-like arrangement (deriving VA-VB=E1-ir1 and VB-VC=E2-ir2 for two cells), then cuts off exactly at the true end of the recording, right as a new worked-numerical circuit is being set up. Board frames extend past this: floor_000088.jpg through floor_000097.jpg (t=1740-1920s, within the true duration) show a full 'cells in parallel' page already in progress and then complete, deriving the equivalent EMF and equivalent internal resistance for two cells in parallel -- none of it narrated in the available transcript. The cells-in-parallel claim above is grounded entirely from the final frame. The corresponding final compact formula for cells in SERIES (which would logically precede the parallel case, analogous to E_eq=E1+E2, r_eq=r1+r2 for aligned cells) was not found written out on any sampled frame either, so it is intentionally left out of this note rather than assumed from the general pattern.

---

## N Identical Cells, Kirchhoff's Rules, Wheatstone Bridge, and Resistors in Series/Parallel

**NCERT sections covered:** 3.11, 3.12, 3.13

### N identical cells in series and parallel (NCERT 3.11)

#### In series (with external resistance $R$)
$$I = \frac{N\mathcal E}{R+Nr}$$
- $R\gg Nr$: $I \approx N\mathcal E/R = N\times$(current from one cell) — worth connecting in series.
- $R\ll Nr$: $I\approx \mathcal E/r$, same as a single cell — no benefit.

**Conclusion:** connect cells in series only when external resistance is much greater than total internal resistance.

#### In parallel (with external resistance $R$)
Net EMF $=\mathcal E$ (all cells share the same EMF between the junction points), net internal resistance $=r/N$:
$$I = \frac{\mathcal E}{R+r/N}$$
- $R\gg r/N$: $I\approx\mathcal E/R$, same as a single cell — no benefit.
- $R\ll r/N$: $I\approx N\mathcal E/r = N\times$(current from one cell) — worth connecting in parallel.

**Conclusion:** connect cells in parallel only when external resistance is much smaller than internal resistance.

### Kirchhoff's rules (NCERT 3.12)

**First law (junction rule):** $\sum I = 0$ at any junction — current in equals current out. Assume a direction for each unknown current before solving; a wrong guess simply comes out negative in the answer.

**Second law (loop rule):** around any closed loop, $\sum(\text{EMFs and }IR\text{ drops}) = 0$ (conservation of energy). **Sign convention:** a potential *drop* in the direction you're tracing (same as assumed current, or through a cell $+\to-$) is negative; a *rise* is positive. Pick one convention and use it consistently for the whole problem — mixing conventions mid-solution gives wrong answers.

**Solving a circuit:** assign unknown currents using the junction rule (reduces the count of unknowns needed), then write loop equations for enough independent loops to match the number of remaining unknowns, and solve simultaneously.

### Wheatstone bridge (NCERT 3.13)

Four resistors $R_1,R_2,R_3,R_4$ in a diamond/bridge arrangement, galvanometer (resistance $G$) across the diagonal. **Balance condition:**
$$\boxed{\frac{R_1}{R_2} = \frac{R_3}{R_4}}$$
When balanced, the galvanometer's two ends are at equal potential, so **no current flows through it** ($I_G=0$) — provable by applying the loop rule to two loops of the bridge and setting $I_G=0$.

**Practical use:** in a balanced bridge, the galvanometer-arm resistor can simply be dropped from the circuit for equivalent-resistance calculations, leaving a simpler series-parallel network.

### Resistors in series and parallel: worked simplifications

- Two resistors in parallel: $R_{eff} = \dfrac{R_1R_2}{R_1+R_2}$ (only valid for exactly two).
- For symmetric networks, first check whether multiple labelled points are actually the *same* electrical node (connected by plain, zero-resistance wire) — relabelling them can reveal resistors are secretly all in parallel between the same two effective points. Example: three $1\,\Omega$ resistors that turn out to all sit between the same two nodes $A,B$ give $R_{eff}=1/3\,\Omega$ by the reciprocal rule.

---
*Note on this lecture's transcript:* the final worked example (a 5-resistor bridge-shaped network) is left unsolved -- the recording ends with it redrawn in equivalent bridge form, before a numeric answer is reached in either the transcript or the board frames. See the flagged span below.


### Verify these spans
- [47:35–48:09] This is a clean truncation at the natural end of the recording rather than a repetition or substitution artifact: the transcript's last segment ends mid-sentence while labelling a new 5-resistor (R1-R5) network for one final effective-resistance example, and the last board frame (floor_000144.jpg, at the true end of the recording) shows that same network redrawn in its equivalent Wheatstone-bridge diamond shape, ready for balance-condition analysis -- but the lecture simply ends there, with no numeric answer worked out in either the transcript or any captured frame. This final example is therefore left unsolved in this note rather than guessed at.

---

## Resistance of a Cube Network, and the Metre Bridge

**NCERT sections covered:** 3.13

### Resistance of a cube network (worked numerical)

A cube with an identical resistor $R$ on each of its 12 edges — find the effective resistance between two opposite corners along a **body diagonal** ($X$ and $Y$).

**Symmetry argument:** current $I$ entering at $X$ splits equally into three paths of $I/3$ (three edges meet at $X$). At each of the next three vertices, $I/3$ splits further into $I/6+I/6$ (two edges lead onward toward $Y$'s neighbourhood). The six $I/6$ branches recombine in pairs back into three $I/3$ branches, converging at $Y$.

**Applying Kirchhoff's loop rule** along one $X\to Y$ path (edges carrying $I/3$, then $I/6$, then $I/3$, each of resistance $R$), back through the battery (EMF $\mathcal E$):
$$\mathcal E = IR\left(\frac13+\frac16+\frac13\right) = IR\cdot\frac{2+1+2}{6} = \frac56 IR$$
Using $I=\mathcal E/R_\text{eff}$:
$$\boxed{R_\text{eff} = \frac{5}{6}R}$$
— the classic result for a cube's body-diagonal resistance when every edge carries the same $R$.

### The metre bridge (NCERT 3.13, application of the Wheatstone bridge)

A practical device based on the Wheatstone bridge, used to find an **unknown resistance** $X$.

**Method:** take a known resistance $R$ from a resistance box; connect $R$ and $X$ as the two "gap" resistors of the bridge. The other two bridge arms are formed by a $100$ cm resistance wire $AB$ (typically nichrome) stretched over a metre scale. Tap a jockey along the wire until the galvanometer shows **zero deflection** (the null/balance point) at position $C$, splitting the wire into length $l$ (from $A$) and $100-l$ (from $C$ to $B$).

**Balance condition:** the two wire segments act as resistances $R'=\rho l/A$ and $R''=\rho(100-l)/A$ ($\rho$ = wire resistivity, $A$ = cross-sectional area), forming a bridge with $R$ and $X$. The resistivity/area factors cancel in the balance ratio, giving:
$$\boxed{X = \frac{R(100-l)}{l}}$$

**Practical note:** for the best accuracy, the null point $l$ should fall near the **centre** of the wire (around $50$ cm).

---
*Note on this lecture's transcript:* the entire metre bridge section above is grounded from board frames -- the transcript's own 20 segments describe only the cube-resistance problem, with no mention of the metre bridge anywhere. See the flagged span below.


### Verify these spans
- [00:00–17:42] This is an unusually total content-omission failure: the transcript's 20 segments, spanning essentially the entire lecture from t=0 to its stated end, describe ONLY the resistance-of-a-cube numerical -- the metre bridge, the lecture's own second named topic, is never mentioned even once in the transcript. Board frames tell a completely different story: floor_000041.jpg (t=800s) already shows the full metre-bridge setup (heading, method description, and circuit diagram) essentially complete, and floor_000052.jpg (t=1020s, near the true end) shows the full derivation through to the boxed final formula X=R(100-l)/l, plus a practical note about keeping the null point near the wire's centre for accuracy. Since the transcript's own timestamps leave no visible gap for this material (it reads as one continuous narration of the cube problem throughout), this looks like the ASR silently failing to transcribe an entire audio segment covering a real second topic, rather than a duration-truncation or delayed-repetition case seen elsewhere in this project. All metre-bridge claims above are grounded entirely from the two board frames.

---

## The Potentiometer: Principle, Sensitivity, and Comparing EMFs

### Why a potentiometer, not a voltmeter, for measuring EMF

EMF is defined as the potential difference across a cell's terminals when **no current** is drawn. A real voltmeter has finite (not infinite) resistance, so it always draws a small current, meaning its reading is never *exactly* EMF. A potentiometer, based on the **null-deflection method**, draws no current from the cell at its balance point — so it measures true EMF exactly.

### Principle of the potentiometer

For a wire of uniform cross-sectional area carrying a **steady current**, the fall of potential across any portion is directly proportional to that portion's length. Since $V=IR=I\rho L/A$ and $I,\rho,A$ are all constant:
$$V = KL, \qquad K = \frac{V}{L} = \text{potential gradient (fall of potential per unit length)}$$
(Analogous to other length-based rate quantities, e.g. temperature gradient $dT/dx$.)

### Sensitivity

The smallest potential difference the potentiometer can detect. Smaller $K$ (potential gradient) $\Rightarrow$ finer resolution $\Rightarrow$ **higher** sensitivity (e.g. $0.1$ V/cm is more sensitive than $1$ V/cm). Increase sensitivity by:
1. **Increasing** the total wire length, or
2. **Decreasing** the potential difference (equivalently, current) across the wire — in practice, by adding a series rheostat in the main circuit.

### Apparatus

A long uniform wire (e.g. $4$ m) from $A$ to $B$, connected in the main circuit to a driver battery, key, and optional rheostat. The two cells being compared connect via a **commutator** (three-way switch, only one cell in the galvanometer branch at a time), with a protective resistance in series with the galvanometer, and a **jockey** to tap along the wire and find the null point.

### Use 1: comparing EMFs of two cells

Connect $\mathcal E_1$ to the galvanometer branch ($\mathcal E_2$ left open); tap the jockey to find the null point (zero galvanometer deflection $\Rightarrow$ zero current drawn from $\mathcal E_1$) at length $L_1$: $\mathcal E_1 = KL_1$. Repeat with $\mathcal E_2$ to get $\mathcal E_2=KL_2$. Then:
$$\boxed{\frac{\mathcal E_1}{\mathcal E_2} = \frac{L_1}{L_2}}$$

**Precaution:** the positive terminal of each cell must connect to the *same* positive terminal of the main circuit — wrong polarity means the potentials add instead of oppose, and no null point will ever be found.

### Use 2: internal resistance of a cell (setup only)

A board heading and circuit diagram show a second use beginning: finding a cell's internal resistance using the potentiometer, with a resistance box added in the cell-and-galvanometer branch, alongside a reminder of $r=\dfrac{(\mathcal E-V)}{V}R$ (a formula derived in an earlier lecture of this chapter specifically for this purpose). Only the setup is confirmed here — see the flagged span below for why the worked derivation isn't included.

---
**A note on syllabus status:** the Potentiometer topic covered in this lecture does not appear anywhere in the current (rationalised) NCERT Class 12 Physics textbook's Current Electricity chapter -- it was one of the topics removed in the CBSE 2022-23 rationalisation. It may still be relevant depending on your specific school's or exam's syllabus, but it is not in the current official NCERT text, so no NCERT section number is cited for any claim in this note.


### Verify these spans
- [32:08–34:07] The transcript's real narration (247 unique segments) runs coherently through the potentiometer's principle, sensitivity, apparatus, and the EMF-comparison use, ending naturally on the positive-terminal precaution at t=1928.7s -- about 119 seconds before the recording's true end. The last captured board frame (floor_000096.jpg, t=1900s) shows a second use of the potentiometer just beginning: 'Find internal resistance of cell using potentiometer', with a circuit diagram (resistance box, galvanometer) and a reminder of the r=[(E-V)/V]R formula derived in an earlier lecture -- but only the heading and circuit setup are visible, with no further frames available to confirm a worked derivation. This second use is included above only as what is directly visible (the setup), not as a completed derivation, since neither the transcript nor any later frame confirms how far it was carried.
