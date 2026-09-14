`NCERT Class XII Chemistry · Chapter 1 · Solutions`

# Solutions — Complete Notes

*15 marks on the blueprint — the heaviest chapter in the paper. Theory you know; the marks live in the numericals. Every formula below is followed by the method that actually gets used in the exam.*

## Types of solution — *nine combinations, one table*

A solution is a homogeneous mixture of two or more components. Composition and properties are uniform throughout. Two components only = **binary solution**.

The component in the largest quantity is the **solvent** — and the solvent fixes the physical state of the solution. Everything else is **solute**.

| Solvent | Solute | Example |
|---|---|---|
| Gas | Gas | Air ($\ce{O2}$ in $\ce{N2}$) |
| Liquid | Chloroform in nitrogen |  |
| Solid | Camphor in nitrogen |  |
| Liquid | Gas | $\ce{O2}$ in water; $\ce{CO2}$ in soft drinks |
| Liquid | Ethanol in water |  |
| Solid | Glucose in water |  |
| Solid | Gas | $\ce{H2}$ in palladium |
| Liquid | Amalgam (Na in Hg) |  |
| Solid | Alloys — Cu in Au |  |

**Examiner asks:** one-markers naming the solute/solvent type for a given example. Camphor-in-nitrogen and hydrogen-in-palladium are the two people forget.

## Concentration terms — *seven of them — and which one the question wants*

The whole game is reading which term the question gives you and which it wants. Get that right and the arithmetic is trivial.

#### Mass percentage (w/w)

$$\text{mass \%} = \frac{\text{mass of component}}{\text{mass of solution}} \times 100$$

"10% glucose by mass" means **10 g glucose in 100 g solution** — so 90 g water. Used for industrial chemicals.

#### Volume percentage (v/v)

$$\text{volume \%} = \frac{\text{volume of component}}{\text{volume of solution}} \times 100$$

Used when both components are liquids. 35% v/v ethylene glycol is car antifreeze — it drops water's freezing point to 255.4 K.

#### Mass by volume (w/v)

Mass of solute in 100 mL of solution. Medicine and pharmacy. **0.9% w/v NaCl = normal saline** — remember this one, it reappears in the osmosis questions.

#### Parts per million

$$\text{ppm} = \frac{\text{parts of component}}{\text{total parts}} \times 10^6$$

For trace quantities — pollutants, dissolved oxygen in seawater.

#### Mole fraction ($x$)

$$x_A = \frac{n_A}{n_A + n_B} \qquad x_A + x_B = 1$$

No units. This is the one Raoult's and Henry's laws are written in.

#### Molarity (M)

$$M = \frac{\text{moles of solute}}{\text{volume of solution in L}}$$

**Depends on temperature** — volume expands on heating, so molarity falls.

#### Molality (m)

$$m = \frac{\text{moles of solute}}{\text{mass of solvent in kg}}$$

**Independent of temperature** — mass doesn't change with T. This is why every colligative-property formula uses molality, not molarity.

> **Trap:** molarity uses *volume of solution*; molality uses *mass of solvent*. Not solution. Losing the solute mass from the denominator is the single most common arithmetic slip in this chapter.

Worked · 2014 — molality and molarity from mass %

10% by mass glucose (M = 180 g/mol) in water, density 1.2 g/mL. Find molality and molarity.

**Set up:** 10% by mass → 10 g glucose in 100 g solution → water = 90 g.

**Molality:**

$$m = \frac{10/180}{90/1000} = 0.62\ \text{mol kg}^{-1}$$

**Molarity:** need volume. From $d = m/V$: $V = 100/1.2 = 83.3$ mL $= 0.0833$ L.

$$M = \frac{10/180}{0.0833} = 0.67\ \text{mol L}^{-1}$$

**Examiner asks:** "given mass % and density, find molality and molarity" is a standing 3-marker. The density is only ever there to get you the volume.

## Solubility — *what dissolves in what, and what temperature does to it*

**Solubility** = maximum amount of solute that dissolves in a specified amount of solvent at a specified temperature.

#### Solid in liquid

**Like dissolves like.** Polar solutes (NaCl, sugar) dissolve in polar solvents (water); non-polar solutes (naphthalene, anthracene) dissolve in non-polar solvents (benzene).

Add solute and two opposing processes run: **dissolution** and **crystallisation**. When their rates become equal, dynamic equilibrium is reached, concentration goes constant, and the solution is **saturated**.

- **Temperature:** if dissolution is endothermic ($\Delta H > 0$), solubility rises with T. If exothermic ($\Delta H < 0$), solubility falls with T. (Le Chatelier.)
- **Pressure:** no significant effect — solids and liquids are incompressible.

#### Gas in liquid

Solubility **increases with pressure**: more gas particles per unit volume above the solution → more strike the surface → more dissolve. Solubility **decreases with temperature** (dissolution of a gas is exothermic).

**Examiner asks:** "aquatic species are more comfortable in cold water" (2019) — because oxygen's solubility falls as water warms. Straight 1–2 marker.

## Henry's law — *the gas-solubility law and its three applications*

At constant temperature, the solubility of a gas in a liquid is directly proportional to the partial pressure of that gas above the liquid. Equivalently:

$$p = K_H \, x$$

where $p$ is partial pressure of the gas, $x$ its mole fraction in solution, and $K_H$ the Henry's law constant.

**Read $K_H$ backwards:** higher $K_H$ means *lower* solubility. $K_H$ rises with temperature — which is exactly why gases get less soluble in warm water.

Worked · 2020, repeated 2026 — solubility from Henry's law

Solubility of $\ce{CO2}$ in water at 298 K under 760 mm Hg. $K_H = 1.25 \times 10^6$ mm Hg.

Solubility here means mole fraction. From $p = K_H x$:

$$x = \frac{p}{K_H} = \frac{760}{1.25 \times 10^6} = 6.08 \times 10^{-4}$$

Mole fraction has no unit.

#### The three applications

- **Carbonated drinks** — bottles sealed under high pressure to force $\ce{CO2}$ into solution.
- **Deep-sea diving / bends** — high pressure underwater dissolves $\ce{N2}$ into blood; on ascent it comes out as bubbles that block capillaries. Divers' tanks use helium-diluted air (11.7% He, 56.2% $\ce{N2}$, 32.1% $\ce{O2}$) because helium's high $K_H$ means it barely dissolves.
- **Anoxia at altitude** — low partial pressure of $\ce{O2}$ → low oxygen in blood and tissue → climbers feel weak and can't think clearly.

**Examiner asks:** "state Henry's law + calculate mole fraction" as one 2–3 marker, or the bends/anoxia reasoning as a standalone. Both are near-certain appearances.

## Raoult's law and vapour pressure — *volatile pairs, then non-volatile solutes*

#### Two volatile liquids

Partial vapour pressure of each component is proportional to its mole fraction *in the liquid*:

$$p_1 = p_1^{\circ} x_1 \qquad p_2 = p_2^{\circ} x_2$$
 $$p_{\text{total}} = p_1^{\circ} x_1 + p_2^{\circ} x_2$$

For the mole fraction in the **vapour phase**, use pressures instead of moles:

$$y_1 = \frac{p_1}{p_{\text{total}}}$$

Worked · 2023 — total vapour pressure of an ideal solution

$p_X^{\circ} = 120$ mm Hg, $p_Y^{\circ} = 160$ mm Hg, equal moles of X and Y mixed, ideal solution. Find $p_{\text{total}}$.

Equal moles → $x_X = x_Y = 0.5$.

$$p_{\text{total}} = (120)(0.5) + (160)(0.5) = 60 + 80 = 140\ \text{mm Hg}$$

#### Non-volatile solute in a volatile solvent

Only the solvent contributes to vapour pressure, so $p_{\text{solution}} = p_1^{\circ} x_1$. Adding a non-volatile solute always *lowers* vapour pressure — solute particles occupy surface area that solvent molecules would otherwise escape from.

#### Raoult's law as a special case of Henry's law

Henry's law is $p = K_H x$; Raoult's is $p = p^{\circ} x$. When the solute–solvent interaction happens to equal the solute–solute interaction, $K_H$ becomes equal to $p^{\circ}$ and the two laws coincide.

## Ideal and non-ideal solutions — *two deviations, with the examples that prove them*

#### Ideal solution

Obeys Raoult's law over the entire concentration range, and:

$$\Delta H_{\text{mix}} = 0 \qquad \Delta V_{\text{mix}} = 0$$

Happens when A–A, B–B and A–B interactions are all nearly equal. Examples: n-hexane + n-heptane, bromoethane + chloroethane, benzene + toluene.

#### Positive deviation

A–B interaction **weaker** than A–A and B–B. Molecules escape more easily → vapour pressure *higher* than Raoult predicts.

$$p_A > p_A^{\circ} x_A, \qquad \Delta H_{\text{mix}} > 0, \qquad \Delta V_{\text{mix}} > 0$$

Examples: ethanol + acetone (ethanol's own H-bonding is broken up), carbon disulphide + acetone.

#### Negative deviation

A–B interaction **stronger** than A–A and B–B. Molecules held tighter → vapour pressure *lower* than predicted.

$$p_A < p_A^{\circ} x_A, \qquad \Delta H_{\text{mix}} < 0, \qquad \Delta V_{\text{mix}} < 0$$

Examples: phenol + aniline, chloroform + acetone (they form an H-bond between them), nitric acid + water.

> **Trap:** chloroform + acetone is negative deviation because a *new* hydrogen bond forms *between* the two. Ethanol + acetone is positive because an *existing* hydrogen bond is broken. Both are asked; the reasoning direction is what earns the mark.

#### Azeotropes

Binary mixtures with the **same composition in liquid and vapour phase**, boiling at constant temperature — so they cannot be separated by fractional distillation.

- **Minimum boiling azeotrope** ← large *positive* deviation. Ethanol + water, 95% ethanol by volume.
- **Maximum boiling azeotrope** ← large *negative* deviation. Nitric acid + water, 68% $\ce{HNO3}$ by mass, boils at 393.5 K.

**Examiner asks:** "define azeotrope + which type from negative deviation, with example" — a 2–3 marker that has run repeatedly.

## Colligative properties — *four of them, four formulas, one idea*

Properties that depend on the **number** of solute particles, not their identity. That one sentence is the reason every question in this section works.

#### 1 · Relative lowering of vapour pressure

$$\frac{p_1^{\circ} - p_1}{p_1^{\circ}} = x_2 = \frac{n_2}{n_1 + n_2}$$

For a dilute solution $n_1 \gg n_2$, so this simplifies to the working form:

$$\frac{p_1^{\circ} - p_1}{p_1^{\circ}} = \frac{w_2 / M_2}{w_1 / M_1}$$

#### 2 · Elevation of boiling point

$$\Delta T_b = K_b \, m = \frac{K_b \, w_2 \times 1000}{M_2 \, w_1}$$

$K_b$ = molal elevation constant (ebullioscopic constant), units K kg mol⁻¹. For water, $K_b = 0.52$.

#### 3 · Depression of freezing point

$$\Delta T_f = K_f \, m = \frac{K_f \, w_2 \times 1000}{M_2 \, w_1}$$

$K_f$ = molal depression constant (cryoscopic constant). For water, $K_f = 1.86$, freezing point 273 K.

Both constants depend only on the solvent, and can themselves be calculated:

$$K_f = \frac{R \, M_1 T_f^2}{1000 \, \Delta H_{\text{fus}}} \qquad K_b = \frac{R \, M_1 T_b^2}{1000 \, \Delta H_{\text{vap}}}$$

#### 4 · Osmotic pressure

**Osmosis**: solvent flows through a semi-permeable membrane from pure solvent into solution. **Osmotic pressure** ($\pi$) is the extra pressure applied on the solution side that just stops that flow.

$$\pi = CRT = \frac{n_2 RT}{V} = \frac{w_2 RT}{M_2 V}$$

**Why it's preferred for macromolecules** (proteins, polymers): works at room temperature, so heat-unstable biomolecules survive; uses molarity, which is easy to measure; and its magnitude is large even for dilute solutions, which is all you get from a poorly soluble polymer.

> **Trap:** $\pi$ uses *molarity* and volume in litres. $\Delta T_b$ and $\Delta T_f$ use *molality* and solvent mass in kg. Mixing these up is the standard way to lose an otherwise-correct 3-marker.

#### Isotonic, hypertonic, hypotonic

- **Isotonic** — same osmotic pressure, no net osmosis. Blood cells are isotonic with 0.9% w/v NaCl.
- **Hypertonic** — higher concentration outside; water leaves the cell; cell **shrinks**.
- **Hypotonic** — lower concentration outside; water enters; cell **swells** and may burst.

**Reverse osmosis:** apply pressure *greater than* $\pi$ on the solution side and solvent flows backwards, out of the solution. Used to desalinate seawater, with a cellulose acetate membrane that passes water but not ions.

## Abnormal molar mass and van't Hoff factor — *when the measured mass is wrong, and by how much*

Colligative properties give a molar mass. When the solute associates or dissociates, that measured value differs from the true one — an **abnormal molar mass**.

#### Association

Molecules combine → fewer particles → colligative property falls → measured molar mass comes out **too high**. Ethanoic acid in benzene dimerises through hydrogen bonds: measured 120 g/mol against a true 60.

#### Dissociation

Electrolyte splits into ions → more particles → colligative property rises → measured molar mass comes out **too low**. KCl gives 37.25 g/mol against a true 74.5.

#### van't Hoff factor

$$i = \frac{\text{normal molar mass}}{\text{abnormal molar mass}} = \frac{\text{observed colligative property}}{\text{calculated colligative property}}$$

Equivalently, particles after dissociation/association ÷ particles before.

- **Dissociation** → $i > 1$. KCl: 2. $\ce{MgSO4}$: 2. $\ce{K2SO4}$: 3. $\ce{CaCl2}$: 3.
- **Association** → $i < 1$. Complete dimerisation gives $i = 0.5$.
- **Neither** → $i = 1$. Glucose, urea, sucrose.

Every colligative formula then carries $i$:

$$\frac{p_1^{\circ}-p_1}{p_1^{\circ}} = i\,x_2 \qquad \Delta T_b = i K_b m \qquad \Delta T_f = i K_f m \qquad \pi = \frac{i\,n_2 RT}{V}$$

#### Partial dissociation or association

$$\text{dissociation: } i = 1 + (n-1)\alpha \qquad \text{association: } i = 1 + \left(\tfrac{1}{n}-1\right)\beta$$

$\alpha$ = degree of dissociation, $\beta$ = degree of association, $n$ = particles produced or combined.

> **Trap:** a degree of dissociation cannot exceed 1. If your $\alpha$ comes out at 1.056, the intended answer is "essentially complete dissociation" — say so rather than writing an impossible number.

## Numerical patterns, collected — *every calculation type in this chapter, one model each*

Six patterns cover essentially every numerical this chapter sets. Method first, then one worked model.

A · Concentration conversion — *3 marks*

*Recognise it: gives a mass %, asks for molality/molarity, and hands you a density you'd otherwise have no use for.*

1. Take 100 g of solution. Solute mass = the percentage; solvent mass = 100 − that.
2. Moles of solute = $w_2 / M_2$.
3. Molality: divide by solvent mass in kg.
4. Molarity: get volume from $V = \text{mass}/d$, convert to litres, divide.

B · Henry's law — *2 marks*

*Recognise it: a $K_H$ value appears.*

1. $x = p / K_H$. Answer is a mole fraction, unitless. That's the whole question.

C · Total vapour pressure — *3 marks*

*Recognise it: two $p^{\circ}$ values for two volatile liquids.*

1. Find mole fractions in the liquid (equal moles → 0.5 each).
2. $p_{\text{total}} = p_1^{\circ}x_1 + p_2^{\circ}x_2$.
3. If it asks for vapour-phase composition: $y_1 = p_1/p_{\text{total}}$.

D · $\Delta T_b$ / $\Delta T_f$ → molar mass or temperature — *3 marks*

*Recognise it: a $K_b$ or $K_f$ is given. This is the most-set numerical in the chapter.*

1. Decide whether $i$ is needed — is the solute an electrolyte, or does it dimerise?
2. $\Delta T = i K \dfrac{w_2 \times 1000}{M_2 w_1}$. Rearrange for whatever's missing.
3. If asked for the actual boiling/freezing point, *add* $\Delta T_b$ to $T_b^{\circ}$ or *subtract* $\Delta T_f$ from $T_f^{\circ}$. Don't stop at $\Delta T$.

Worked · 2018 — freezing point of a glucose solution

60 g glucose ($M = 180$) in 250 g water, $K_f = 1.86$. Find the freezing point.

Glucose doesn't dissociate, so $i = 1$.

$$\Delta T_f = \frac{1.86 \times 60 \times 1000}{180 \times 250} = 2.48\ \text{K}$$
 $$T_f = 273 - 2.48 = 270.52\ \text{K}$$

E · Osmotic pressure — *3 marks*

*Recognise it: R is given, or the word isotonic appears.*

1. $\pi = \dfrac{w_2 RT}{M_2 V}$, volume in **litres**.
2. For isotonic pairs, set the two concentrations equal: $\dfrac{w_1}{M_1} = \dfrac{w_2}{M_2}$ (volumes cancel) and solve for the unknown $M$.

F · van't Hoff factor → α or β — *3–5 marks*

*Recognise it: asks for degree of dissociation/association, or "predict the nature of the solute".*

1. Get $i$ from the colligative-property equation with $i$ left in as the unknown.
2. $i > 1$ → dissociation, use $i = 1 + (n-1)\alpha$. $i < 1$ → association, use the association form.
3. Read $n$ off the actual dissociation equation — write it out, don't guess.

Worked · 2026 — degree of dissociation of fluoroacetic acid

19.5 g $\ce{FCH2COOH}$ ($M = 78$) in 500 g water gives $\Delta T_f = 1$ K. $K_f = 1.86$.

$$1 = i \times \frac{1.86 \times 19.5 \times 1000}{78 \times 500} \;\Rightarrow\; i = 1.075$$

$\ce{FCH2COOH -> FCH2COO- + H+}$, so $n = 2$:

$$1.075 = 1 + (2-1)\alpha \;\Rightarrow\; \alpha = 0.075 = 7.5\%$$

## Past year questions · question types — *ranked by how often they turn up*

*From the last 10 years of boards. 22 questions are captured below with their years; the source video states it covers 25, so treat this as the bulk of the set rather than all of it.*

1 · Colligative-property numerical — *3 marks*

*Recognise it: $K_b$, $K_f$ or R is supplied.*

1. Pick the right formula from the constant given.
2. Decide on $i$.
3. Convert to the final temperature if asked.

> **Trap:** stopping at $\Delta T$ when the question asked for the boiling or freezing point.

2 · Deviation from Raoult's law, with reason — *2–3 marks*

*Recognise it: names a specific liquid pair and asks "what type of deviation, why".*

1. Compare A–B interaction against A–A and B–B.
2. Stronger → negative, vapour pressure falls. Weaker → positive, vapour pressure rises.
3. Name the actual interaction — which H-bond forms or breaks.

> **Trap:** answering "negative deviation" without saying *which* bond forms between the two. The reason carries the mark.

3 · van't Hoff factor / degree of dissociation — *3–5 marks*

*Recognise it: asks for $i$, α, β, or "predict association or dissociation".*

1. Solve the colligative equation for $i$.
2. Compare against 1 to decide association vs dissociation.
3. Apply the matching α/β relation.

> **Trap:** using $n = 2$ automatically. $\ce{CaCl2}$ gives 3 ions, $\ce{K2SO4}$ gives 3.

4 · Henry's law statement + calculation — *2–3 marks*

*Recognise it: $K_H$ appears, often paired with "state Henry's law".*

1. State the law in mole-fraction form.
2. $x = p/K_H$.
3. If asked for applications, give carbonated drinks and the bends.

5 · Osmosis reasoning (cells, meat, isotonic) — *2–3 marks*

*Recognise it: blood cells, salting meat, or a % NaCl solution.*

1. Compare concentration inside vs outside.
2. Water moves toward the higher concentration.
3. State the consequence: shrink, swell, or preserved.

6 · Definitions and two-difference questions — *2 marks*

*Recognise it: "define…", "write two differences between…".*

1. Give the definition in the book's own words.
2. For differences, answer in pairs — ideal vs non-ideal on both $\Delta H_{\text{mix}}$ and $\Delta V_{\text{mix}}$.

## Past year questions · mark slots — *what each type is worth, and the time that buys*

| Question type | Slot | Time |
|---|---|---|
| Colligative numerical | 3-marker | 4–5 min |
| Deviation + reason | 2–3 marker | 3 min |
| van't Hoff / α | 3-marker, sometimes inside a 5 | 5 min |
| Henry's law | 2–3 marker | 3 min |
| Osmosis reasoning | 2–3 marker | 3 min |
| Definitions / differences | 2-marker | 2 min |
| Concentration conversion | 3-marker | 4 min |

*Slots marked from the question shapes in the paper — the video groups them as short-answer type I (2 marks) and type II (3 marks).*

## Past year questions · repeat offenders — *appeared more than once — highest probability in the chapter*

These are the reason the PYQ video is worth watching. Each has run at least twice.

2020 Q3 · 2026 Q1

Henry's law statement plus mole fraction of $\ce{CO2}$ at 760 mm Hg — the identical numbers reappeared six years apart.

2019 Q11(a) · lecture PYQ

Aquatic species more comfortable in cold water — gas solubility falls as temperature rises.

2019 Q11(b) · 2019 Q12

Anoxia at high altitude, and chloroform + acetone negative deviation. Both recur as reason-type one/two markers.

2018 Q10 · 2026 Q18

Freezing-point depression with a given $K_f$ — glucose in water, then fluoroacetic acid in water with a degree of dissociation on top.

2023 Q5 · lecture PYQ

Total vapour pressure of an ideal solution from two $p^{\circ}$ values and equal moles. Same 120/160 mm Hg numbers in both.

2016 Q7 · 2025 Q6

van't Hoff factor: definition, and why osmotic pressure is preferred for macromolecular molar masses.

2017 Q13 · 2020 Q2

Blood cells in 1.2% and 0.4% NaCl, and why 0.1 M KCl boils higher than 0.1 M glucose. Both test "colligative = number of particles".

## Past year questions · cold practice — *answers only — work them before you look*

One model per pattern is above. These are the same patterns with different numbers: work each one cold, then check.

#### Colligative numericals

- 2026 Q14 — 8 g non-volatile solute in 100 g diethyl ether, bp rises 35.60 → 36.86 °C, $K_b = 2.02$. Find $M_2$. 128.25 g/mol

- 2017 — 10 g $\ce{CaCl2}$ ($M=111$) in 200 g water, $K_b = 0.52$. Find $\Delta T_b$. 0.702 K (remember $i=3$)

- 2026 Q8 — 1 molal trichloroacetic acid boils at 100.18 °C, $K_b = 0.512$. Find $i$. 0.35

- 2021 Q15 — 2.56 g sulphur in 100 g $\ce{CS2}$, $\Delta T_f = 1.62$ K, $K_f = 4.9$, $M(\ce{S8}) = 256$. Find % association. $i = 0.846$; 15.4%

#### Vapour pressure

- 2026 Q19 — 61 g benzoic acid in 500 g benzene, $p^{\circ} = 51.2$ mm Hg, complete dimerisation. Find $p_s$. 50.42 mm Hg (use $i = 0.5$)

- Lecture PYQ — pure water $p^{\circ} = 32$ mm Hg at 308 K falls to 31.84 with 10 g solute in 200 g water. Find $M_2$. 180 g/mol

#### Osmotic pressure

- 2020 Q3 — 5% urea solution ($M = 60$) at 300 K, $R = 0.0821$. Find $\pi$. 20.51 atm

- 2019 Q17 — 6% glucose ($M=180$) isotonic with 2.5% of an unknown. Find the unknown's $M$. 75 g/mol

#### Freezing point, two-stage

- 2021 Q21 — 5% cane sugar ($M = 342$) freezes at 271 K. Find the freezing point of 5% glucose ($M = 180$). 269.2 K — find $K_f$ from the sugar first

Built from Sourabh Raina's Solutions one-shot and PYQ videos, cross-checked against NCERT Class XII Chemistry Chapter 1 (Rationalised 2022–23). Constants verified: water $K_b = 0.52$, $K_f = 1.86$ K kg mol⁻¹.
