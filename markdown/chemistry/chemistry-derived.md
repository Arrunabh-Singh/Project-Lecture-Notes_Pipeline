`Class XII CBSE · Chemistry · Chapters 1–3`

# Chemistry, Derived

*Twelve derivations, one algebraic move per line, each with the reason it is allowed. Every one ends in a formula that is already on **Every Chemistry Formula** — the point of this page is that you can rebuild them when memory fails, and that you can write the proof out when the paper asks for it.*

- Derivations: 12

- Figures: 12

- Chapters: 3

- Marks covered: 42

### How to use this

Chapters 4, 5 and 6 have no derivations worth the name — their marks come from recall and reasoning, and those live on the formula sheet. Everything derivable in this paper is on this page.

Read the **setup** first and draw the figure yourself before you look at the steps. A derivation you can only follow is not one you can write.

The *italic reason* beside a step is what turns it from an assertion into a proof. In the exam, those reasons are usually where the marks are.

## `CH 3` Chemical Kinetics — *5 derivations · 13 marks*

### `D1` Integrated rate law for a zero order reaction — *2–3 marks*

> A reaction $\ce{R -> P}$ whose rate does not depend on the concentration of $\ce{R}$ at all. Start from the definition of rate, put the zero-order rate law into it, and integrate from the start of the reaction to time $t$. Write $[R]_0$ for the concentration at $t=0$ and $[R]$ for the concentration at time $t$.

**Figure.** Graph of concentration of R against time for a zero order reaction: a straight line starting at the initial concentration on the vertical axis and falling with constant slope minus k, meeting the time axis when all of R is used up.

*Zero order is the only order whose concentration–time plot is a straight line. Its slope is $-k$ and its intercept is $[R]_0$, which is how both are read off experimental data.*

1. Rate $= -\dfrac{d[R]}{dt}$  — *(definition; minus sign because $[R]$ falls)*
2. Rate $= k[R]^0 = k$  — *(zero order: anything to the power 0 is 1)*
3. $-\dfrac{d[R]}{dt} = k$
4. $d[R] = -k\,dt$  — *(separating the variables)*
5. $\displaystyle\int_{[R]_0}^{[R]} d[R] = -k\int_{0}^{t} dt$  — *(integrating between the two states)*
6. $[R] - [R]_0 = -k\,(t - 0)$
7. $[R] - [R]_0 = -kt$
8. $[R] = -kt + [R]_0$  — *(the straight line in the figure, $y = mx + c$)*
9. $kt = [R]_0 - [R]$  — *(rearranging for $k$)*
10. $k = \dfrac{[R]_0 - [R]}{t}$

**Result:** $[R] = -kt + [R]_0 \qquad k = \dfrac{[R]_0 - [R]}{t}$

*Units check: $k$ comes out as concentration ÷ time, $\ce{mol L^-1 s^-1}$ — which is exactly what C3.4 predicts for $n=0$.*

### `D2` Half-life of a zero order reaction — *2 marks*

> Half-life $t_{1/2}$ is the time at which exactly half the reactant is left. Take the integrated law from D1 and substitute that one condition.

> **Shared setup with D1.** Every half-life derivation is the integrated rate law with $[R] = [R]_0/2$ and $t = t_{1/2}$ substituted. If you can do D1 and D3, you can do D2 and D4 without learning anything new.

**Figure.** Zero order concentration against time, with the half-life marked: the concentration reaches half its initial value at a time equal to the initial concentration divided by twice k, and reaches zero at twice that time.

*Because the line is straight, the reaction finishes at exactly $2t_{1/2}$ — a zero order reaction really does run out, which no first order reaction ever does.*

1. $k = \dfrac{[R]_0 - [R]}{t}$  — *(from D1)*
2. At $t = t_{1/2}$, $[R] = \dfrac{[R]_0}{2}$  — *(definition of half-life)*
3. $k = \dfrac{[R]_0 - \tfrac{[R]_0}{2}}{t_{1/2}}$  — *(substituting both)*
4. $k = \dfrac{\tfrac{[R]_0}{2}}{t_{1/2}}$
5. $k\,t_{1/2} = \dfrac{[R]_0}{2}$
6. $t_{1/2} = \dfrac{[R]_0}{2k}$

**Result:** $t_{1/2} = \dfrac{[R]_0}{2k}$ — *directly proportional* to the initial concentration

### `D3` Integrated rate law for a first order reaction — *3 marks*

> Same reaction $\ce{R -> P}$, but now the rate is proportional to $[R]$. The integration produces a natural logarithm, which is then converted to base 10 because every exam table and graph uses $\log$.

**Figure.** Graph of log of concentration of R against time for a first order reaction: a straight line with intercept log of the initial concentration and slope minus k over 2.303.

*A first order reaction is straight only after you take the logarithm. That is the practical test: if $\log[R]$ against $t$ is a line, the reaction is first order and $k$ is $2.303\times$ the magnitude of its slope.*

1. Rate $= -\dfrac{d[R]}{dt}$  — *(definition)*
2. Rate $= k[R]^1 = k[R]$  — *(first order rate law)*
3. $-\dfrac{d[R]}{dt} = k[R]$
4. $\dfrac{d[R]}{[R]} = -k\,dt$  — *(separating the variables)*
5. $\displaystyle\int_{[R]_0}^{[R]} \dfrac{d[R]}{[R]} = -k\int_{0}^{t} dt$
6. $\ln[R] - \ln[R]_0 = -kt$  — *(integral of $1/x$ is $\ln x$)*
7. $\ln\dfrac{[R]}{[R]_0} = -kt$  — *(law of logarithms)*
8. $\ln\dfrac{[R]_0}{[R]} = kt$  — *(inverting the fraction flips the sign)*
9. $2.303\log\dfrac{[R]_0}{[R]} = kt$  — *($\ln x = 2.303\log_{10} x$)*
10. $k = \dfrac{2.303}{t}\log\dfrac{[R]_0}{[R]}$
11. Rearranged for a graph: $\log[R] = -\dfrac{k}{2.303}t + \log[R]_0$  — *(the straight line drawn above)*

**Result:** $k = \dfrac{2.303}{t}\log\dfrac{[R]_0}{[R]}$

*Units check: the log is dimensionless, so $k$ has units of $1/\text{time}$, $\ce{s^-1}$ — matching C3.4 for $n=1$. That is also why the next derivation comes out independent of concentration.*

### `D4` First order half-life, and why it ignores concentration — *2–3 marks*

> Substitute the half-life condition into D3. Watch what happens to $[R]_0$ — the whole point of this derivation is that it cancels.

**Figure.** First order decay curve: concentration falls from its initial value to one half after one half-life, to one quarter after two half-lives and one eighth after three, with the three time intervals all equal.

*Each successive halving takes the same time, no matter how little is left. That is the visual statement of the algebraic cancellation below, and it is why radioactive decay has a fixed half-life.*

1. $k = \dfrac{2.303}{t}\log\dfrac{[R]_0}{[R]}$  — *(from D3)*
2. At $t = t_{1/2}$, $[R] = \dfrac{[R]_0}{2}$  — *(definition of half-life)*
3. $k = \dfrac{2.303}{t_{1/2}}\log\dfrac{[R]_0}{[R]_0/2}$
4. $\dfrac{[R]_0}{[R]_0/2} = 2$  — *($[R]_0$ cancels — this is the whole result)*
5. $k = \dfrac{2.303}{t_{1/2}}\log 2$
6. $\log 2 = 0.301$
7. $k = \dfrac{2.303 \times 0.301}{t_{1/2}} = \dfrac{0.693}{t_{1/2}}$
8. $t_{1/2} = \dfrac{0.693}{k}$

**Result:** $t_{1/2} = \dfrac{0.693}{k}$ — *independent* of the initial concentration

*Step 4 is the answer to "show that the half-life of a first order reaction is independent of initial concentration". Do not skip it; it is the mark.*

### `D5` Activation energy from rate constants at two temperatures — *3 marks*

> Start from the Arrhenius equation, take logarithms to make it linear, write it once at each of two temperatures $T_1$ and $T_2$, and subtract. The frequency factor $A$ is unknown and must disappear — that is what the subtraction is for.

**Figure.** Arrhenius plot: log k against one over T is a descending straight line whose intercept is log A and whose slope is minus the activation energy divided by 2.303 R.

*$T_2 \gt T_1$, so $1/T_2$ sits to the *left* of $1/T_1$ and the higher temperature gives the higher $\log k$. Reading the axis backwards is the commonest error on this plot.*

1. $k = A\,e^{-E_a/RT}$  — *(Arrhenius equation)*
2. $\ln k = \ln A - \dfrac{E_a}{RT}$  — *(taking natural logs of both sides)*
3. $\log k = \log A - \dfrac{E_a}{2.303RT}$  — *(converting to base 10)*
4. At $T_1$: $\log k_1 = \log A - \dfrac{E_a}{2.303RT_1}$
5. At $T_2$: $\log k_2 = \log A - \dfrac{E_a}{2.303RT_2}$
6. Subtracting: $\log k_2 - \log k_1 = -\dfrac{E_a}{2.303RT_2} + \dfrac{E_a}{2.303RT_1}$  — *($\log A$ cancels — it is the same constant at both temperatures)*
7. $\log\dfrac{k_2}{k_1} = \dfrac{E_a}{2.303R}\left[\dfrac{1}{T_1} - \dfrac{1}{T_2}\right]$
8. $\dfrac{1}{T_1} - \dfrac{1}{T_2} = \dfrac{T_2 - T_1}{T_1T_2}$  — *(common denominator)*
9. $\log\dfrac{k_2}{k_1} = \dfrac{E_a}{2.303R}\left[\dfrac{T_2 - T_1}{T_1T_2}\right]$

**Result:** $\log\dfrac{k_2}{k_1} = \dfrac{E_a}{2.303R}\left[\dfrac{T_2 - T_1}{T_1T_2}\right]$

*The bracket is $\tfrac{1}{T_1} - \tfrac{1}{T_2}$, smaller temperature first. If you get a negative $E_a$, you reversed it at step 7.*

## `CH 2` Electrochemistry — *3 derivations · 14 marks*

### `D6` The Nernst equation — *3 marks*

> A galvanic cell running the reaction $\ce{aA + bB -> cC + dD}$ with $n$ electrons transferred. Two facts are combined: the thermodynamic relation between Gibbs energy and the reaction quotient, and the electrochemical relation between Gibbs energy and cell potential.

**Figure.** A galvanic cell: a zinc electrode in zinc sulphate solution on the left as the anode where oxidation occurs, a copper electrode in copper sulphate solution on the right as the cathode where reduction occurs, joined by a salt bridge that dips into both solutions and by an external circuit with a voltmeter through which electrons flow from left to right.

*The Daniell cell, $E^\circ_{\text{cell}} = 1.1\ \text{V}$. The Nernst equation says what happens to that reading when the two solutions are not at 1 M — and the sign of the correction follows from Le Chatelier, not from memory.*

1. $\Delta_r G = \Delta_r G^{\,\circ} + RT\ln Q$  — *(thermodynamics: Gibbs energy away from standard state)*
2. $\Delta_r G = -nFE_{\text{cell}}$  — *(electrical work done by the cell)*
3. $\Delta_r G^{\,\circ} = -nFE^{\,\circ}_{\text{cell}}$  — *(same relation at standard state)*
4. $-nFE_{\text{cell}} = -nFE^{\,\circ}_{\text{cell}} + RT\ln Q$  — *(substituting 2 and 3 into 1)*
5. Divide throughout by $-nF$:
6. $E_{\text{cell}} = E^{\,\circ}_{\text{cell}} - \dfrac{RT}{nF}\ln Q$
7. $E_{\text{cell}} = E^{\,\circ}_{\text{cell}} - \dfrac{2.303RT}{nF}\log Q$  — *(converting to base 10)*
8. At 298 K: $\dfrac{2.303 \times 8.314 \times 298}{96487} = 0.059$  — *(substituting $R$, $T$ and $F$)*
9. $E_{\text{cell}} = E^{\,\circ}_{\text{cell}} - \dfrac{0.059}{n}\log Q$

**Result:** $E_{\text{cell}} = E^{\,\circ}_{\text{cell}} - \dfrac{2.303RT}{nF}\log Q \;\xrightarrow{298\text{ K}}\; E^{\,\circ}_{\text{cell}} - \dfrac{0.059}{n}\log Q$

*Step 8 is worth writing out in full — being asked where the 0.059 comes from is a common follow-up, and "$2.303RT/F$ at 298 K" is the whole answer.*

### `D7` Equilibrium constant from standard cell potential — *2–3 marks*

> Take the Nernst equation and ask what it says at the one moment the cell stops working. A cell at equilibrium has no driving force, so it reads zero volts — and at that moment the reaction quotient has become the equilibrium constant.

> **Shared setup with D6.** This is the Nernst equation with one substitution. Do not learn it as a separate formula.

**Figure.** Graph of cell potential against log Q: a descending straight line of slope minus 0.059 over n, with intercept the standard cell potential at log Q equals zero, crossing the horizontal axis at log of the equilibrium constant where the cell is dead.

*The cell potential falls linearly as products build up. Where the line crosses zero, $Q$ has reached $K_c$ — the battery is flat. Reading the intercept and the zero-crossing off this one line gives both results.*

1. $E_{\text{cell}} = E^{\,\circ}_{\text{cell}} - \dfrac{0.059}{n}\log Q$  — *(from D6)*
2. At equilibrium the cell delivers no work, so $E_{\text{cell}} = 0$  — *(a dead cell)*
3. At equilibrium $Q = K_c$  — *(definition of the equilibrium constant)*
4. $0 = E^{\,\circ}_{\text{cell}} - \dfrac{0.059}{n}\log K_c$
5. $E^{\,\circ}_{\text{cell}} = \dfrac{0.059}{n}\log K_c$  — *(moving the log term across — this is why the sign is now positive)*
6. $\log K_c = \dfrac{n\,E^{\,\circ}_{\text{cell}}}{0.059}$  — *(rearranged for $K_c$)*
7. Equivalently, from $\Delta_r G^{\,\circ} = -nFE^{\,\circ}_{\text{cell}}$ and $\Delta_r G^{\,\circ} = -RT\ln K_c$:
8. $nFE^{\,\circ}_{\text{cell}} = RT\ln K_c$  — *(equating the two expressions for $\Delta_r G^\circ$)*

**Result:** $E^{\,\circ}_{\text{cell}} = \dfrac{0.059}{n}\log K_c \qquad \log K_c = \dfrac{n\,E^{\,\circ}_{\text{cell}}}{0.059}$

### `D8` Molar conductivity from conductivity — where the 1000 comes from — *2 marks*

> A conductivity cell of electrode area $A$ and separation $l$. Conductivity $\kappa$ is defined for a $1\ \text{cm}$ cube of solution; molar conductivity $\Lambda_m$ is defined for however much solution contains exactly one mole. The 1000 is nothing but a $\ce{cm^3}$-to-litre conversion, and this derivation is really a units argument.

**Figure.** A conductivity cell: two parallel electrodes of area A separated by a distance l, with the cell constant defined as l divided by A, beside a unit cube of solution of side one centimetre whose conductance is the conductivity.

*Two different reference volumes: $\kappa$ is per cubic centimetre, $\Lambda_m$ is per mole. Converting between them is the entire content of the formula.*

1. $\Lambda_m = \kappa \times V$  — *($V$ = volume of solution containing exactly 1 mole of electrolyte)*
2. Let the concentration be $c$ mol per litre  — *(the unit every exam question uses)*
3. $c$ moles occupy $1\ \text{L}$, so 1 mole occupies $\dfrac{1}{c}\ \text{L}$
4. $1\ \text{L} = 1000\ \text{cm}^3$  — *(the conversion — this is the 1000)*
5. 1 mole occupies $\dfrac{1000}{c}\ \text{cm}^3$
6. $\Lambda_m = \kappa \times \dfrac{1000}{c}$
7. Units: $\ce{S cm^-1} \times \ce{cm^3 mol^-1} = \ce{S cm^2 mol^-1}$  — *(confirming the standard unit)*

**Result:** $\Lambda_m = \dfrac{\kappa \times 1000}{c}$ in $\ce{S cm^2 mol^-1}$

*In strict SI ($\kappa$ in $\ce{S m^-1}$, $c$ in $\ce{mol m^-3}$) step 4 disappears and $\Lambda_m = \kappa/c$ in $\ce{S m^2 mol^-1}$. The 1000 is a unit artefact, not physics.*

## `CH 1` Solutions — *4 derivations · 15 marks*

### `D9` Relative lowering of vapour pressure equals the solute's mole fraction — *3 marks*

> A non-volatile solute B dissolved in a volatile solvent A. Only A can evaporate, so the vapour above the solution is pure A — but there is less of it, because solute particles occupy part of the surface. Start from Raoult's law and rearrange.

**Figure.** Two beakers side by side: pure solvent on the left with many molecules escaping from its surface, and a solution on the right whose surface is partly occupied by solute particles so fewer solvent molecules escape, giving a lower vapour pressure.

*Solute particles (filled circles) take up surface sites, so fewer solvent molecules can leave. The fraction of the surface still available to solvent is $x_A$ — which is exactly what Raoult's law asserts.*

1. $p_A = x_A\,p_A^{\,\circ}$  — *(Raoult's law; the solute is non-volatile so $p_{\text{soln}} = p_A$)*
2. $p_A^{\,\circ} - p_A = p_A^{\,\circ} - x_A p_A^{\,\circ}$  — *(subtracting both sides from $p_A^\circ$)*
3. $p_A^{\,\circ} - p_A = p_A^{\,\circ}(1 - x_A)$
4. $x_A + x_B = 1$, so $1 - x_A = x_B$  — *(mole fractions sum to one)*
5. $p_A^{\,\circ} - p_A = p_A^{\,\circ}\,x_B$
6. $\dfrac{p_A^{\,\circ} - p_A}{p_A^{\,\circ}} = x_B$  — *(dividing by $p_A^\circ$ — the left side is the relative lowering)*
7. $x_B = \dfrac{n_B}{n_A + n_B}$  — *(definition of mole fraction)*
8. For a dilute solution $n_B \ll n_A$, so $n_A + n_B \approx n_A$
9. $\dfrac{p_A^{\,\circ} - p_A}{p_A^{\,\circ}} \approx \dfrac{n_B}{n_A} = \dfrac{w_B/M_B}{w_A/M_A}$
10. $\dfrac{p_A^{\,\circ} - p_A}{p_A^{\,\circ}} = \dfrac{w_B\,M_A}{M_B\,w_A}$  — *(rearranged to give molar mass)*

**Result:** $\dfrac{p_A^{\,\circ} - p_A}{p_A^{\,\circ}} = x_B \qquad M_B = \dfrac{w_B\,M_A\,p_A^{\,\circ}}{w_A\left(p_A^{\,\circ} - p_A\right)}$

*Steps 1–6 are exact. Step 8 is the only approximation, and it is only valid for a dilute solution — say so if you use it.*

### `D10` Elevation of boiling point is proportional to molality — *3 marks*

> A liquid boils when its vapour pressure equals the external pressure. A non-volatile solute lowers the vapour pressure at every temperature (D9), so the solution's curve sits below the solvent's — and has to be taken to a higher temperature before it reaches the 1 atm line.

**Figure.** Vapour pressure against temperature for pure solvent and for solution: the solution curve lies below the solvent curve everywhere, so it meets the one atmosphere line at a higher temperature, and the gap between the two crossing points is the elevation of boiling point.

*The dashed curve is the solution. It never reaches 1 atm at the solvent's boiling point, so the temperature must be raised by $\Delta T_b$ — and for a dilute solution the two curves are near enough parallel that the shift is proportional to how much vapour pressure was lost.*

1. For a dilute solution, the lowering of vapour pressure is proportional to the elevation of boiling point: $\Delta T_b \propto \left(p_A^{\,\circ} - p_A\right)$  — *(the two curves are almost straight and almost parallel over this small range)*
2. $\dfrac{p_A^{\,\circ} - p_A}{p_A^{\,\circ}} = x_B$  — *(from D9)*
3. So $\Delta T_b \propto x_B$  — *($p_A^\circ$ is a constant for a given solvent)*
4. $x_B = \dfrac{n_B}{n_A + n_B} \approx \dfrac{n_B}{n_A}$  — *(dilute solution)*
5. $\Delta T_b \propto \dfrac{n_B}{n_A}$
6. $n_A = \dfrac{w_A}{M_A}$, so $\dfrac{n_B}{n_A} = \dfrac{n_B M_A}{w_A}$
7. $M_A$ is a constant for a given solvent, so $\Delta T_b \propto \dfrac{n_B}{w_A}$
8. $\dfrac{n_B}{w_A \text{ in kg}} = m$, the molality  — *(definition of molality)*
9. $\Delta T_b \propto m$
10. $\Delta T_b = K_b\,m$  — *(introducing the proportionality constant)*
11. $m = \dfrac{w_B \times 1000}{M_B\,w_A}$  — *(molality written from masses, $w_A$ in grams)*
12. $\Delta T_b = \dfrac{K_b\,w_B \times 1000}{M_B\,w_A}$
13. $M_B = \dfrac{K_b\,w_B \times 1000}{\Delta T_b\,w_A}$

**Result:** $\Delta T_b = K_b\,m \qquad M_B = \dfrac{K_b\,w_B \times 1000}{\Delta T_b\,w_A}$

*$K_b$ is the elevation for a 1 molal solution, and depends only on the solvent — for water $0.52\ \ce{K kg mol^-1}$.*

### `D11` Depression of freezing point is proportional to molality — *3 marks*

> A solution freezes when the vapour pressure of the liquid equals that of the pure solid solvent. Adding solute lowers the liquid's vapour pressure, so the two curves now meet at a *lower* temperature. Structurally identical to D10 — only the meeting point changes.

> **Shared setup with D10.** Both start from "vapour pressure is lowered by $x_B$" and end in "proportional to molality". If you can write one, change the meeting condition and you have written the other.

**Figure.** Vapour pressure against temperature near the freezing point: the solid solvent line crosses the pure solvent curve at the normal freezing point on the right, and crosses the lower solution curve at a lower temperature on the left, the gap between the two crossings being the depression of freezing point.

*Freezing happens where the liquid curve crosses the solid curve. Lowering the liquid curve moves that crossing to the left, and the shift is $\Delta T_f$. Note the solid curve is unchanged — solute does not dissolve in the solid solvent.*

1. A solution freezes when the vapour pressure of the liquid equals that of the pure solid solvent  — *(definition of freezing point)*
2. For a dilute solution, $\Delta T_f \propto \left(p_A^{\,\circ} - p_A\right)$  — *(same near-linear argument as D10)*
3. $\dfrac{p_A^{\,\circ} - p_A}{p_A^{\,\circ}} = x_B$  — *(from D9)*
4. $\Delta T_f \propto x_B$
5. $x_B \approx \dfrac{n_B}{n_A}$  — *(dilute solution)*
6. $\Delta T_f \propto \dfrac{n_B}{w_A}$  — *($M_A$ constant for a given solvent)*
7. $\Delta T_f \propto m$  — *(definition of molality)*
8. $\Delta T_f = K_f\,m$
9. $m = \dfrac{w_B \times 1000}{M_B\,w_A}$
10. $M_B = \dfrac{K_f\,w_B \times 1000}{\Delta T_f\,w_A}$

**Result:** $\Delta T_f = K_f\,m \qquad M_B = \dfrac{K_f\,w_B \times 1000}{\Delta T_f\,w_A}$

*$K_f$ for water is $1.86\ \ce{K kg mol^-1}$ — larger than $K_b$, which is why freezing-point depression is the more sensitive method for finding a molar mass.*

### `D12` Degree of dissociation from the van't Hoff factor — *2–3 marks*

> One mole of an electrolyte $\ce{A_n}$ that breaks into $n$ particles, with a fraction $\alpha$ actually dissociating. Colligative properties count *particles*, so build the particle total after dissociation and compare it with the total before.

**Figure.** Particle count before and after dissociation: one mole of solute starts as one particle, and after a fraction alpha dissociates into n particles the total becomes one minus alpha plus n alpha, whose ratio to the original is the van't Hoff factor.

*Only the fraction $\alpha$ splits; the rest stays whole. Counting both contributions is the entire derivation — $i$ is just the ratio of the two particle totals.*

1. $\ce{A_n -> nA}$, starting from 1 mole with a fraction $\alpha$ dissociating
2. Moles of $\ce{A_n}$ left undissociated $= 1 - \alpha$
3. Moles of $\ce{A}$ produced $= n\alpha$  — *(each dissociated mole gives $n$ particles)*
4. Total moles of particles after $= (1-\alpha) + n\alpha$
5. $i = \dfrac{\text{total particles after}}{\text{total particles before}} = \dfrac{1 - \alpha + n\alpha}{1}$  — *(definition of the van't Hoff factor)*
6. $i = 1 - \alpha + n\alpha$
7. $i - 1 = \alpha(n - 1)$  — *(collecting the $\alpha$ terms)*
8. $\alpha = \dfrac{i - 1}{n - 1}$
9. For **association**, $n$ molecules combine into 1, so the total after is $1 - \alpha + \dfrac{\alpha}{n}$
10. $i = 1 - \alpha + \dfrac{\alpha}{n} = 1 - \alpha\left(1 - \dfrac{1}{n}\right)$
11. $\alpha = \dfrac{1 - i}{1 - \tfrac{1}{n}}$

**Result:** $\alpha_{\text{dissoc}} = \dfrac{i-1}{n-1} \qquad \alpha_{\text{assoc}} = \dfrac{1-i}{1-\tfrac{1}{n}}$

*Dissociation gives $i \gt 1$ and association $i \lt 1$; both formulas return a positive $\alpha$ because the numerator flips with them.*

Built from Sourabh Raina's one-shot and PYQ videos for Chapters 1–3, and cross-checked against NCERT Class XII Chemistry (Rationalised 2022–23) for constants and conventions — $F = 96487\ \ce{C mol^-1}$, $R = 8.314\ \ce{J K^-1 mol^-1}$, $K_b = 0.52$ and $K_f = 1.86\ \ce{K kg mol^-1}$ for water, and **0.059** rather than 0.0591 in the Nernst equation.

Chapters 4, 5 and 6 are not represented here because they contain no derivations — their marks come from trends, reasons and reactivity orders, all of which are on the companion page, **Every Chemistry Formula**.
