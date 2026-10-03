`NCERT Class XII Chemistry · Chapter 3 · Chemical Kinetics`

# Chemical Kinetics — Complete Notes

*13 marks. Almost pure numerical territory — order from data, integrated rate equations, half-life, activation energy. Four formulas do nearly all the work; the marks go to knowing which one the question is pointing at.*

## What kinetics answers — *and what it deliberately doesn't*

Three different questions about a reaction, three different branches:

| Question | Answered by |
|---|---|
| Is it feasible? ($\Delta G < 0$) | Thermodynamics |
| How far does it go? | Chemical equilibrium ($K$) |
| How fast, and by what mechanism? | **Chemical kinetics** |

The standard illustration: thermodynamics says diamond → graphite is feasible. Kinetics explains why your ring is safe — the conversion is immeasurably slow.

## Rate of reaction — *average, instantaneous, and the coefficient division*

Rate = change in concentration per unit time. Reactant concentration falls, so its rate carries a minus sign to keep the rate positive:

$$\text{rate} = -\frac{\Delta[R]}{\Delta t} = +\frac{\Delta[P]}{\Delta t}$$

**Average rate** uses $\Delta$ over a finite interval. **Instantaneous rate** is the slope of the tangent at one moment: $-\dfrac{d[R]}{dt}$.

#### When coefficients differ — divide by them

For $aA + bB \rightarrow cC + dD$:

$$\text{rate} = -\frac{1}{a}\frac{d[A]}{dt} = -\frac{1}{b}\frac{d[B]}{dt} = \frac{1}{c}\frac{d[C]}{dt} = \frac{1}{d}\frac{d[D]}{dt}$$

> **Trap:** "rate of reaction" and "rate of disappearance of B" are different numbers whenever B's coefficient isn't 1. Read which one is asked — this is the entire content of a 2-marker that runs most years.

Worked · 2022 — rate of reaction vs rate of disappearance

$\ce{N2 + 3H2 -> 2NH3}$, rate of formation of $\ce{NH3} = 3.6\times10^{-4}$ mol L⁻¹ s⁻¹. Find the rate of reaction and the rate of disappearance of $\ce{H2}$.

$$\text{rate} = \tfrac{1}{2}\frac{\Delta[\ce{NH3}]}{\Delta t} = \tfrac{1}{2}(3.6\times10^{-4}) = 1.8\times10^{-4}$$
 $$-\frac{\Delta[\ce{H2}]}{\Delta t} = 3 \times \text{rate} = 5.4\times10^{-4}\ \text{mol L}^{-1}\text{s}^{-1}$$

**Examiner asks:** this exact shape, with $\ce{N2}/\ce{H2}/\ce{NH3}$ or $A + 3B \to 2C$. Near-guaranteed 2–3 marker.

## Rate law and finding the order from data — *the standard 3-marker, step by step*

The rate law is **experimental** — powers are not read off the balanced equation:

$$\text{rate} = k[A]^x[B]^y$$

$x$ and $y$ may or may not equal the stoichiometric coefficients. **Order** = $x + y$. Order can be zero, fractional, or negative; molecularity cannot.

#### Getting x and y from a data table — the method

1. Pick two experiments where **one** concentration is held constant and the other changes.
2. Write the rate law for each; divide one by the other. $k$ and the constant term cancel.
3. Read off the power that makes the ratio work.
4. Repeat with a different pair for the other exponent.
5. Substitute any single experiment back to find $k$.

> **Trap:** choosing two experiments where *both* concentrations change. Nothing cancels and the algebra becomes unsolvable. Scan the table for the constant column first.

#### Order vs molecularity — the comparison they ask for

| Order | Molecularity |
|---|---|
| Sum of powers in the experimental rate law | Number of species colliding in one elementary step |
| Experimental | Theoretical |
| Can be 0, fractional, negative | Whole number only (1, 2, 3) |
| Applies to overall reaction | Only defined for an elementary step |

**Examiner asks:** "can this be an elementary reaction?" (2026) with a fractional order like 3/2 — **no**, because an elementary reaction's order equals its molecularity, which must be a whole number.

## Units of the rate constant — *one formula, every order*

From rate $= k[\,]^n$, so $k = \text{rate}/[\,]^n$:

$$\text{unit of } k = \text{mol}^{1-n}\,\text{L}^{n-1}\,\text{s}^{-1}$$

| Order | Unit of k |
|---|---|
| Zero | mol L⁻¹ s⁻¹ |
| First | s⁻¹ |
| Second | L mol⁻¹ s⁻¹ |

**Examiner asks:** given a rate law, state the units — or, run backwards, given the units, state the order. Both directions appear.

## Integrated rate equations — *zero and first order, plus their graphs*

#### Zero order

$$[R] = -kt + [R]_0 \qquad k = \frac{[R]_0 - [R]}{t}$$

Plot $[R]$ against $t$: straight line, **slope $= -k$**, intercept $[R]_0$.

**Example:** decomposition of gaseous ammonia on a hot platinum surface at 1130 K. At high pressure the metal surface saturates with ammonia, so adding more changes nothing — rate becomes independent of concentration:

$$\ce{2NH3(g) ->[Pt] N2(g) + 3H2(g)}, \qquad \text{rate} = k[\ce{NH3}]^0 = k$$

#### First order

$$k = \frac{2.303}{t}\log\frac{[R]_0}{[R]}$$

Plot $\log\dfrac{[R]_0}{[R]}$ against $t$: straight line through the origin, **slope $= k/2.303$**. Plot $\ln[R]$ against $t$ instead and the slope is $-k$, intercept $\ln[R]_0$.

**Examples:** hydrogenation of ethene; all natural and artificial radioactive decay; decomposition of $\ce{N2O5}$ and $\ce{N2O}$.

#### First order in the gas phase — the closed form worth memorising

Concentration is proportional to partial pressure, so the same equation runs on pressures. For $A(g) \rightarrow B(g) + C(g)$ with all coefficients 1, let $x$ be the pressure decomposed:

$$p_{\text{total}} = (p_i - x) + x + x = p_i + x \;\Rightarrow\; x = p_T - p_i$$

So the reactant's partial pressure is $p_A = p_i - x = 2p_i - p_T$, and:

$$k = \frac{2.303}{t}\log\frac{p_i}{2p_i - p_T}$$

Use this directly whenever the question gives you **initial and total** pressure. If it gives the reactant's partial pressure outright, the plain $\log(p_i/p_A)$ form is enough.

Worked · 2016 — rate constant from total pressure

$\ce{C2H5Cl(g) -> C2H4(g) + HCl(g)}$. At $t = 0$, $p_i = 0.30$ atm; at $t = 300$ s, $p_T = 0.50$ atm. ($\log 3 = 0.4771$)

$$k = \frac{2.303}{300}\log\frac{0.30}{2(0.30) - 0.50} = \frac{2.303}{300}\log\frac{0.30}{0.10}$$
 $$= \frac{2.303 \times 0.4771}{300} = 3.66\times10^{-3}\ \text{s}^{-1}$$

The unit is s⁻¹, which itself confirms first order.

> **Trap:** feeding the *total* pressure straight into the log. It must be $2p_i - p_T$, not $p_T$.

## Half-life — *and the graph question that turns on it*

Time for half the reactant to be consumed.

$$\text{First order: } t_{1/2} = \frac{0.693}{k} \qquad \text{Zero order: } t_{1/2} = \frac{[R]_0}{2k}$$

**The distinction that gets examined:** first-order half-life is **independent of initial concentration**; zero-order half-life is **directly proportional** to it.

**Examiner asks:** "predict the order from the graph" (2019) — a flat $t_{1/2}$ vs $[R]_0$ line means first order; a straight rising line means zero order.

#### Percentage-completion problems

Set $[R]_0 = 100$ and subtract the percentage completed. 75% done → $[R] = 25$; 99% done → $[R] = 1$.

Worked · 2026 — time for 3/4 decomposition

First order, $k = 2.54\times10^{-3}$ s⁻¹. Time for 3/4 of the reactant to decompose? ($\log 4 = 0.6$)

$[R]_0 = a$, so $[R] = a - \frac{3}{4}a = \frac{a}{4}$.

$$t = \frac{2.303}{k}\log\frac{a}{a/4} = \frac{2.303 \times 0.6}{2.54\times10^{-3}} = 544\ \text{s}$$

A neat consequence worth remembering: for first order, $t_{99\%} = 2 \times t_{90\%}$ — because $\log 100 = 2$ and $\log 10 = 1$.

## Pseudo first order — *two examples, one idea*

A reaction that is **bimolecular but follows first-order kinetics**, because one reactant is present in such large excess that its concentration doesn't measurably change.

**Hydrolysis of sucrose:**

$$\ce{C12H22O11 + H2O ->[H+] C6H12O6 + C6H12O6}$$

Water is the solvent, so $[\ce{H2O}]$ is effectively constant. Rate $= k[\ce{C12H22O11}]$: order 1, molecularity 2.

**Hydrolysis of an ester** in dilute acid behaves the same way.

**Examiner asks:** (2024) write the rate law, then state order *and* molecularity separately, then name the reaction type. The gap between order 1 and molecularity 2 is the whole point.

## Temperature dependence and Arrhenius — *the 5-marker's favourite*

Rate roughly **doubles for every 10 K rise** near room temperature. Quantitatively:

$$k = A\,e^{-E_a/RT}$$

$A$ = frequency factor, $E_a$ = activation energy, the minimum energy colliding molecules need.

#### The logarithmic form and its graph

$$\ln k = -\frac{E_a}{RT} + \ln A$$

Against $y = mx + c$ with $y = \ln k$ and $x = 1/T$:

- **Slope** $= -E_a/R$ (negative, so the line falls)
- **Intercept** $= \ln A$

#### Two-temperature form — the one used in numericals

$$\log\frac{k_2}{k_1} = \frac{E_a}{2.303\,R}\left[\frac{T_2 - T_1}{T_1 T_2}\right]$$

Worked · 2025 — E_a when the rate doubles over 10 K

Rate doubles from 298 K to 308 K. $2.303R = 19.15$, $\log 2 = 0.3$.

Concentrations are unchanged, so a doubled rate means a doubled $k$: $k_2/k_1 = 2$.

$$0.3 = \frac{E_a}{19.15}\left[\frac{10}{308 \times 298}\right]$$
 $$E_a = \frac{0.3 \times 19.15 \times 308 \times 298}{10} = 52729.9\ \text{J mol}^{-1} = 52.7\ \text{kJ mol}^{-1}$$

Worked · 2025 — E_a from two half-lives

First order, 50% complete in 20 min at 300 K and in 5 min at 350 K. ($\log 4 = 0.602$)

50% completion is the half-life, so $k = 0.693/t_{1/2}$:

$$\frac{k_2}{k_1} = \frac{0.693/5}{0.693/20} = 4$$
 $$0.602 = \frac{E_a}{2.303 \times 8.314}\left[\frac{50}{300\times350}\right] \Rightarrow E_a = 24205\ \text{J mol}^{-1} = 24.2\ \text{kJ mol}^{-1}$$

> **Trap:** "50% completed in 20 minutes" is a half-life in disguise. Spot that and the question collapses into two lines.

## Collision theory and catalysis — *the definitions that carry marks*

#### Activated complex and the energy profile

Colliding reactant molecules first form a short-lived **activated complex**. The energy needed to reach it is the **activation energy**. The reaction's own energy change is separate:

$$\Delta H = H_{\text{products}} - H_{\text{reactants}}$$

On a potential-energy vs reaction-coordinate plot, the barrier height is $E_a$ either way; what changes is where the products land. Products lower than reactants → $\Delta H$ negative → **exothermic**. Products higher → $\Delta H$ positive → **endothermic**.

#### Maxwell–Boltzmann distribution

Plot the fraction of molecules ($n_E/n_T$) against kinetic energy. Most molecules sit near the **most probable kinetic energy**; only a small tail — roughly 10–20% — carries energy above $E_a$, and only those can react.

**Raise the temperature by 10 K** and the curve flattens and shifts right: the fraction with energy at or above $E_a$ roughly **doubles**. That is precisely why the rate doubles for a 10 K rise.

#### Collision theory

Treats molecules as hard spheres that must collide to react.

**Collision frequency ($Z$):** number of collisions per second per unit volume of reaction mixture.

$$\text{rate} = Z_{AB}\,e^{-E_a/RT}$$

Comparing this with Arrhenius shows the frequency factor $A$ is essentially the **collision frequency**. The theory is accurate for atoms and simple molecules but deviates for complex ones — because not every collision works. Two conditions must both hold:

1. Colliding molecules have energy at least equal to the **threshold energy**.
2. They collide in the **proper orientation**, so old bonds can break and new ones form.

#### Catalysis

A catalyst increases the rate **without itself undergoing any permanent chemical change**. By **intermediate complex theory**, it forms a temporary bond with the reactant, making a transitory intermediate that decomposes into product and releases the catalyst again — which is why a small amount catalyses a large amount of reactant.

The effect is an **alternative pathway of lower activation energy**, so more molecules clear the barrier and the rate rises.

**What a catalyst does not change:** the Gibbs energy of the reaction, the equilibrium constant, or the position of equilibrium. It catalyses forward and backward reactions *to the same extent*, so equilibrium is reached **earlier** but at the same place. And since it can't change $\Delta G$, it cannot make a non-spontaneous reaction happen — only speed up one that already is.

**Examiner asks:** (2017) "effect of a catalyst on activation energy and on ΔG" — lowers $E_a$, leaves $\Delta G$ untouched. Answering only the first half loses the mark.

#### Reaction mechanism and the rate-determining step

For a multi-step reaction, the **slowest step determines the rate** — write the rate law directly from that step's reactants.

Example (2025): $\ce{2H2O2 ->[I-] 2H2O + O2}$ via a slow step $\ce{H2O2 + I- -> H2O + IO-}$ and a fast step. So rate $= k[\ce{H2O2}][\ce{I-}]$, overall order 2 — even though the balanced equation shows $\ce{2H2O2}$.

## Numerical patterns, collected — *five patterns, one model each*

A · Rate from stoichiometry — *2 marks*

*Recognise it: one species' rate is given, another is asked for.*

1. Write the full rate expression with $1/\text{coefficient}$ on every term.
2. Equate the known term to the wanted one.
3. Check whether "rate of reaction" or "rate of disappearance" is asked.

B · Order from a data table — *3 marks*

*Recognise it: a table of concentrations and initial rates.*

1. Find two rows with one concentration constant.
2. Divide the two rate laws; solve for the exponent.
3. Repeat for the other exponent, then back-substitute for $k$.

C · Integrated first-order equation — *3 marks*

*Recognise it: a percentage decomposed, or concentrations at two times.*

1. Set $[R]_0 = 100$ and subtract the percentage.
2. $k = \frac{2.303}{t}\log\frac{[R]_0}{[R]}$, rearranged for the unknown.
3. Gas phase → convert total pressure to reactant partial pressure first.

D · Half-life ↔ rate constant — *2–3 marks*

*Recognise it: "half-life", or "50% completed".*

1. Identify the order from the rate law or the units of $k$.
2. First order: $t_{1/2} = 0.693/k$. Zero order: $t_{1/2} = [R]_0/2k$.

Worked · 2026 — half-life from percentage decomposition

First order, 25% decomposed in 25 min. Find $t_{1/2}$. ($\log 4 = 0.6021$, $\log 3 = 0.4771$)

$$k = \frac{2.303}{25}\log\frac{100}{75} = \frac{2.303}{25}(0.6021 - 0.4771) = 0.0115\ \text{min}^{-1}$$
 $$t_{1/2} = \frac{0.693}{0.0115} = 60.26\ \text{min}$$

E · Activation energy from two temperatures — *5 marks*

*Recognise it: two temperatures, or "rate doubles when temperature rises by…".*

1. Get $k_2/k_1$ — from rates directly, or from $0.693/t_{1/2}$ at each temperature.
2. $\log\frac{k_2}{k_1} = \frac{E_a}{2.303R}\left[\frac{T_2-T_1}{T_1T_2}\right]$.
3. Answer in J mol⁻¹, then divide by 1000 for kJ.

## Past year questions · question types — *ranked by how often they turn up*

*From the last 10 years of boards — 25 questions, grouped by pattern.*

1 · First-order integrated rate equation — *3 marks*

*Recognise it: a percentage decomposed, or a concentration/pressure at two times.*

1. $[R]_0 = 100$, subtract the percentage.
2. Apply the 2.303 formula.
3. Convert total pressure to partial pressure if gaseous.

> **Trap:** using the percentage *decomposed* as $[R]$ instead of what remains.

2 · Activation energy (Arrhenius) — *5 marks*

*Recognise it: two temperatures, or $2.303R = 19.15$ handed to you.*

1. Get $k_2/k_1$.
2. Two-temperature Arrhenius form.
3. Convert to kJ if the answer is large.

> **Trap:** inverting $T_2 - T_1$ over $T_1T_2$, or forgetting that the half-life ratio inverts the $k$ ratio.

3 · Order from a data table — *3–5 marks*

*Recognise it: a table of initial concentrations and rates.*

1. Pair rows sharing a constant concentration.
2. Divide; solve the exponent.
3. Back-substitute for $k$ and state its units.

4 · Rate expression from stoichiometry — *2–3 marks*

*Recognise it: one species' rate given, another asked.*

1. Full expression with $1/\text{coefficient}$ terms.
2. Equate and solve.

5 · Definitions and comparisons — *2 marks*

*Recognise it: "define", "distinguish between", "write the unit of".*

1. Order vs molecularity: answer in matched pairs.
2. Half-life, collision frequency, effective collision, activation energy — book definitions.

6 · Graph interpretation — *3 marks*

*Recognise it: a plot of $\ln k$ vs $1/T$, or $t_{1/2}$ vs $[R]_0$, or $\log\frac{[R]_0}{[R]}$ vs $t$.*

1. Match the plot to its equation.
2. Read slope and intercept off $y = mx + c$.
3. State what each represents in symbols, not words alone.

## Past year questions · mark slots — *what each type is worth*

| Question type | Slot | Time |
|---|---|---|
| First-order integrated equation | 3-marker | 4 min |
| Activation energy | 5-marker (or part of one) | 6–7 min |
| Order from data table | 3-marker, sometimes a 5 | 5–6 min |
| Rate from stoichiometry | 2–3 marker | 3 min |
| Definitions / comparisons | 2-marker | 2 min |
| Graph interpretation | 3-marker | 4 min |
| Pseudo first order | 3-marker | 3 min |

*The video splits these as short-answer type I (2 marks), type II (3 marks) and long answer (5 marks) — activation energy and the multi-part data questions are where the 5-markers sit.*

## Past year questions · repeat offenders — *appeared more than once — highest probability in the chapter*

2018 Q15 · lecture PYQ

"Second order in A, first order in B" — write the differential rate equation, then how the rate changes when concentrations are tripled or doubled. Identical wording both times.

2025 Q16 · 2025 Q23(a)

Activation energy from two temperatures — once from two half-lives, once from a rate that doubles over 10 K. Same formula, two disguises.

2019 Q5 · 2022 Q17

Graph questions: $\ln k$ vs $1/T$ (intercept and slope), and $\log\frac{[R]_0}{[R]}$ vs $t$ (order and slope). Both reduce to $y = mx + c$.

2022 Q8 · 2026 Q6

Order vs molecularity — as a straight comparison, and as "can this be an elementary reaction" with a fractional order.

2024 Q21 · lecture PYQ

Sucrose hydrolysis: rate law, order 1 but molecularity 2, and the name — pseudo first order.

2019 Q9 · 2019 Q10

Half-life: predicting order from a $t_{1/2}$ vs $[R]_0$ graph, and computing $t_{1/2}$ from a first-order rate law.

2026 Q1 · 2024 Q3

Definitions: collision frequency, effective collisions, half-life period, and the units of $k$ for zero and first order.

## Past year questions · cold practice — *answers only — work them before you look*

#### Integrated rate equation

- 2017 Q11 — $\ce{N2O5}$ decomposition: 1.6×10⁻² M at $t=0$, 0.8×10⁻² M at 300 s. Show first order and find $t_{1/2}$. $k = 2.3\times10^{-3}$ s⁻¹ at both times; $t_{1/2} = 301$ s

- 2026 Q22 — $\ce{C2H5Cl}$: $p_i = 0.30$ atm, total $p = 0.50$ atm at 30 s. Find $k$. 0.0368 s⁻¹

- 2026 Q4 — $k = 2.54\times10^{-3}$ s⁻¹, time for 3/4 decomposition. 544 s

- 2024 — first order, $k = 1.25\times10^{-3}$ s⁻¹. Time for 5 g to fall to 2.5 g. 554.6 s — note this is just $t_{1/2}$ in disguise

- 2024 — show $t_{99\%} = 2\,t_{90\%}$ for first order. $\log 100 = 2$ vs $\log 10 = 1$

- 2021–22 — first order, 75% decomposed in 30 min. Find $t_{1/2}$. $k = 0.046$ min⁻¹; $t_{1/2} = 15$ min

- Lecture PYQ — zero order, $[R]_0 = 0.1$ M falls to 0.064 M, $k = 4\times10^{-3}$. Find $t$. 9 s

#### Half-life

- 2019 Q10 — rate $= 5.5\times10^{-14}[\ce{C2H4}]$. Units of $k$ and $t_{1/2}$. s⁻¹; $1.26\times10^{13}$ s

- 2026 Q24(b) — first order, 25% decomposed in 25 min. Find $t_{1/2}$. $k = 0.0115$ min⁻¹; $t_{1/2} = 60.26$ min

#### Activation energy

- 2025 Q16 — 50% complete in 20 min at 300 K, 5 min at 350 K. Find $E_a$. 24.2 kJ mol⁻¹

- 2025 Q23(a) — rate doubles from 298 K to 308 K. Find $E_a$. 52.7 kJ mol⁻¹

#### Rate and order

- 2020 — $A + 3B \to 2C$, rate of formation of C $= 2.5\times10^{-4}$. Find rate of reaction and rate of disappearance of B. $1.25\times10^{-4}$; $3.75\times10^{-4}$ mol L⁻¹ s⁻¹

- 2026 Q6 — rate $= k[A][B]^{3/2}$. Overall order, and can it be elementary? 2.5; no — elementary reactions have whole-number order

- 2025 Q18 — order with respect to A and B from a rate table where doubling B leaves the rate unchanged. Order in B is zero

#### Mechanism

- 2025 Q23(b) — $\ce{2H2O2 ->[I-] 2H2O + O2}$, slow step $\ce{H2O2 + I- -> H2O + IO-}$. Rate law and overall order. rate $= k[\ce{H2O2}][\ce{I-}]$; order 2

Built from Sourabh Raina's Chemical Kinetics one-shot and PYQ videos, cross-checked against NCERT Class XII Chemistry Chapter 3 (Rationalised 2022–23). NCERT confirms the Arrhenius form $k = Ae^{-E_a/RT}$ and the term "pseudo first order reaction".
