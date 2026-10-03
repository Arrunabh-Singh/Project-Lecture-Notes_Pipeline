# Class XII CBSE — Complete Notes: Physics and Chemistry

Everything built for one Class XII student at DPS Indore, in one file. It was
written from their own teacher's recorded lectures (transcribed, then
cross-checked against the board frames and the NCERT text), not from a
textbook summary, so the worked method is the point rather than the statement
of the result.

**The confirmed deadline is the chemistry half-yearly on 10 September 2026**,
70 marks, blueprint: Solutions 15 · Electrochemistry 14 · Chemical Kinetics 13
· d- and f-Block 11 · Coordination Compounds 11 · Haloalkanes 6. No physics
exam date has been given.

**Two depths, deliberately.** Chemistry chapters 1–3 are theory the student
already knows, so the length there goes into numerical method. Chapters 4–6 are
first contact: every technical term carries an **[exposure]** marker and is
defined in plain words with a concrete example before it is used again. The
physics notes are all board-grounded and flag any span the transcript could not
resolve confidently.

**Maths notation.** KaTeX throughout (`$...$` inline, `$$...$$` display), with
mhchem `\ce{...}` for chemical formulae. The older physics one-off pages at the
end use plain-text maths instead — they predate the KaTeX pipeline.

**Figures.** The source pages carry drawn SVG diagrams. A `.md` file cannot show
them, so each appears here as **Figure.** followed by the full prose description
that was written as its accessible label — a description complete enough to
redraw from.

**Size.** This file is deliberately large. Read the manifest and contents below
and seek to the section you need rather than reading it top to bottom.

## Manifest

| Section | Where it came from | What it is | Caveats |
|---|---|---|---|
| Chemistry chapters 1–6 | lecture transcripts + NCERT `lech101–105`, `lech201` | full chapter notes, exam-shaped, with past-year question sections | Ch4–6 carry `[exposure]` first-contact definitions; Ch1–3 assume the theory |
| Every Chemistry Formula | built across all six chapters | 50 entries, each with symbols, units, a recognition cue and its trap | 40 marked ● must-be-instant, 10 marked ○ |
| Chemistry, Derived | as above | 12 derivations, each ending in a formula that is on the formula sheet | figures are prose descriptions here |
| Every Physics Formula | the 57 chapter notes + NCERT `leph101–108` | 100 entries across chapters 1–9 | 78 marked ● must-be-instant, 22 marked ○; Ch9 rows come from the Ray Optics page, not from lectures |
| Physics, Derived | as above | 45 derivations, chapters 1–9, numbered PD1–PD45 | figures are prose descriptions here |
| Physics chapter notes 1–8 | 57 transcribed and verified lectures | the source of truth for every physics equation in this file | included verbatim; equations are board-grounded. **There is no Chapter 9 here** — those eighteen lectures have never been transcribed |
| Ray Optics to 9.4 | published page, no lecture source | Chapter 9 theory, four derivations, formula strip and question tiers | built for a test whose scope stopped at 9.4, so it skips lenses, prisms and instruments — those are in Physics, Derived instead |
| Alternating Current in Eight Derivations | published page | Chapter 7 in its own exam-shaped framing | eight derivations against the five (PD33–PD37) in Physics, Derived |
| Electromagnetic Waves for Six Marks | published page | Chapter 8, same shape | its five derivations include four that Physics, Derived does not carry — that book has one for Chapter 8 |

**Not included, and why.** Eight published physics chapter pages (one per
chapter, Ch1–8) exist as well. Their prose is a rendering of the same 57
chapter notes reproduced in full below, and their remaining bulk is embedded
board-frame photographs that cannot survive a Markdown export. Including them
would duplicate the largest block in this file for no added content.

## Contents

- [Part I — Chemistry](#part-i--chemistry)
    - [Chapter 1 · Solutions](#chapter-1--solutions)
    - [Chapter 2 · Electrochemistry](#chapter-2--electrochemistry)
    - [Chapter 3 · Chemical Kinetics](#chapter-3--chemical-kinetics)
    - [Chapter 4 · The d- and f-Block Elements](#chapter-4--the-d--and-f-block-elements)
    - [Chapter 5 · Coordination Compounds](#chapter-5--coordination-compounds)
    - [Chapter 6 · Haloalkanes and Haloarenes](#chapter-6--haloalkanes-and-haloarenes)
    - [Every Chemistry Formula](#every-chemistry-formula)
    - [Chemistry, Derived](#chemistry-derived)
- [Part II — Physics](#part-ii--physics)
    - [Every Physics Formula](#every-physics-formula)
    - [Physics, Derived](#physics-derived)
    - [Chapter 1 · Electric Charges and Fields — lecture notes](#chapter-1--electric-charges-and-fields--lecture-notes)
    - [Chapter 2 · Electrostatic Potential and Capacitance — lecture notes](#chapter-2--electrostatic-potential-and-capacitance--lecture-notes)
    - [Chapter 3 · Current Electricity — lecture notes](#chapter-3--current-electricity--lecture-notes)
    - [Chapter 4 · Moving Charges and Magnetism — lecture notes](#chapter-4--moving-charges-and-magnetism--lecture-notes)
    - [Chapter 5 · Magnetism and Matter — lecture notes](#chapter-5--magnetism-and-matter--lecture-notes)
    - [Chapter 6 · Electromagnetic Induction — lecture notes](#chapter-6--electromagnetic-induction--lecture-notes)
    - [Chapter 7 · Alternating Current — lecture notes](#chapter-7--alternating-current--lecture-notes)
    - [Chapter 8 · Electromagnetic Waves — lecture notes](#chapter-8--electromagnetic-waves--lecture-notes)
    - [Ray Optics to 9.4](#ray-optics-to-94)
    - [Alternating Current in Eight Derivations](#alternating-current-in-eight-derivations)
    - [Electromagnetic Waves for Six Marks](#electromagnetic-waves-for-six-marks)
- [Appendix — gaps, caveats and open questions](#appendix--gaps-caveats-and-open-questions)
    - [Chapter 9 physics was never transcribed](#chapter-9-physics-was-never-transcribed)
    - [A symbol clash still in the source](#a-symbol-clash-still-in-the-source)
    - [How much to trust the transcripts](#how-much-to-trust-the-transcripts)
    - [Open question](#open-question)

---

## Part I — Chemistry

### Chapter 1 · Solutions

`NCERT Class XII Chemistry · Chapter 1 · Solutions`

*15 marks on the blueprint — the heaviest chapter in the paper. Theory you know; the marks live in the numericals. Every formula below is followed by the method that actually gets used in the exam.*

#### Types of solution — *nine combinations, one table*

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

#### Concentration terms — *seven of them — and which one the question wants*

The whole game is reading which term the question gives you and which it wants. Get that right and the arithmetic is trivial.

###### Mass percentage (w/w)

$$\text{mass \%} = \frac{\text{mass of component}}{\text{mass of solution}} \times 100$$

"10% glucose by mass" means **10 g glucose in 100 g solution** — so 90 g water. Used for industrial chemicals.

###### Volume percentage (v/v)

$$\text{volume \%} = \frac{\text{volume of component}}{\text{volume of solution}} \times 100$$

Used when both components are liquids. 35% v/v ethylene glycol is car antifreeze — it drops water's freezing point to 255.4 K.

###### Mass by volume (w/v)

Mass of solute in 100 mL of solution. Medicine and pharmacy. **0.9% w/v NaCl = normal saline** — remember this one, it reappears in the osmosis questions.

###### Parts per million

$$\text{ppm} = \frac{\text{parts of component}}{\text{total parts}} \times 10^6$$

For trace quantities — pollutants, dissolved oxygen in seawater.

###### Mole fraction ($x$)

$$x_A = \frac{n_A}{n_A + n_B} \qquad x_A + x_B = 1$$

No units. This is the one Raoult's and Henry's laws are written in.

###### Molarity (M)

$$M = \frac{\text{moles of solute}}{\text{volume of solution in L}}$$

**Depends on temperature** — volume expands on heating, so molarity falls.

###### Molality (m)

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

#### Solubility — *what dissolves in what, and what temperature does to it*

**Solubility** = maximum amount of solute that dissolves in a specified amount of solvent at a specified temperature.

###### Solid in liquid

**Like dissolves like.** Polar solutes (NaCl, sugar) dissolve in polar solvents (water); non-polar solutes (naphthalene, anthracene) dissolve in non-polar solvents (benzene).

Add solute and two opposing processes run: **dissolution** and **crystallisation**. When their rates become equal, dynamic equilibrium is reached, concentration goes constant, and the solution is **saturated**.

- **Temperature:** if dissolution is endothermic ($\Delta H > 0$), solubility rises with T. If exothermic ($\Delta H < 0$), solubility falls with T. (Le Chatelier.)
- **Pressure:** no significant effect — solids and liquids are incompressible.

###### Gas in liquid

Solubility **increases with pressure**: more gas particles per unit volume above the solution → more strike the surface → more dissolve. Solubility **decreases with temperature** (dissolution of a gas is exothermic).

**Examiner asks:** "aquatic species are more comfortable in cold water" (2019) — because oxygen's solubility falls as water warms. Straight 1–2 marker.

#### Henry's law — *the gas-solubility law and its three applications*

At constant temperature, the solubility of a gas in a liquid is directly proportional to the partial pressure of that gas above the liquid. Equivalently:

$$p = K_H \, x$$

where $p$ is partial pressure of the gas, $x$ its mole fraction in solution, and $K_H$ the Henry's law constant.

**Read $K_H$ backwards:** higher $K_H$ means *lower* solubility. $K_H$ rises with temperature — which is exactly why gases get less soluble in warm water.

Worked · 2020, repeated 2026 — solubility from Henry's law

Solubility of $\ce{CO2}$ in water at 298 K under 760 mm Hg. $K_H = 1.25 \times 10^6$ mm Hg.

Solubility here means mole fraction. From $p = K_H x$:

$$x = \frac{p}{K_H} = \frac{760}{1.25 \times 10^6} = 6.08 \times 10^{-4}$$

Mole fraction has no unit.

###### The three applications

- **Carbonated drinks** — bottles sealed under high pressure to force $\ce{CO2}$ into solution.
- **Deep-sea diving / bends** — high pressure underwater dissolves $\ce{N2}$ into blood; on ascent it comes out as bubbles that block capillaries. Divers' tanks use helium-diluted air (11.7% He, 56.2% $\ce{N2}$, 32.1% $\ce{O2}$) because helium's high $K_H$ means it barely dissolves.
- **Anoxia at altitude** — low partial pressure of $\ce{O2}$ → low oxygen in blood and tissue → climbers feel weak and can't think clearly.

**Examiner asks:** "state Henry's law + calculate mole fraction" as one 2–3 marker, or the bends/anoxia reasoning as a standalone. Both are near-certain appearances.

#### Raoult's law and vapour pressure — *volatile pairs, then non-volatile solutes*

###### Two volatile liquids

Partial vapour pressure of each component is proportional to its mole fraction *in the liquid*:

$$p_1 = p_1^{\circ} x_1 \qquad p_2 = p_2^{\circ} x_2$$
 $$p_{\text{total}} = p_1^{\circ} x_1 + p_2^{\circ} x_2$$

For the mole fraction in the **vapour phase**, use pressures instead of moles:

$$y_1 = \frac{p_1}{p_{\text{total}}}$$

Worked · 2023 — total vapour pressure of an ideal solution

$p_X^{\circ} = 120$ mm Hg, $p_Y^{\circ} = 160$ mm Hg, equal moles of X and Y mixed, ideal solution. Find $p_{\text{total}}$.

Equal moles → $x_X = x_Y = 0.5$.

$$p_{\text{total}} = (120)(0.5) + (160)(0.5) = 60 + 80 = 140\ \text{mm Hg}$$

###### Non-volatile solute in a volatile solvent

Only the solvent contributes to vapour pressure, so $p_{\text{solution}} = p_1^{\circ} x_1$. Adding a non-volatile solute always *lowers* vapour pressure — solute particles occupy surface area that solvent molecules would otherwise escape from.

###### Raoult's law as a special case of Henry's law

Henry's law is $p = K_H x$; Raoult's is $p = p^{\circ} x$. When the solute–solvent interaction happens to equal the solute–solute interaction, $K_H$ becomes equal to $p^{\circ}$ and the two laws coincide.

#### Ideal and non-ideal solutions — *two deviations, with the examples that prove them*

###### Ideal solution

Obeys Raoult's law over the entire concentration range, and:

$$\Delta H_{\text{mix}} = 0 \qquad \Delta V_{\text{mix}} = 0$$

Happens when A–A, B–B and A–B interactions are all nearly equal. Examples: n-hexane + n-heptane, bromoethane + chloroethane, benzene + toluene.

###### Positive deviation

A–B interaction **weaker** than A–A and B–B. Molecules escape more easily → vapour pressure *higher* than Raoult predicts.

$$p_A > p_A^{\circ} x_A, \qquad \Delta H_{\text{mix}} > 0, \qquad \Delta V_{\text{mix}} > 0$$

Examples: ethanol + acetone (ethanol's own H-bonding is broken up), carbon disulphide + acetone.

###### Negative deviation

A–B interaction **stronger** than A–A and B–B. Molecules held tighter → vapour pressure *lower* than predicted.

$$p_A < p_A^{\circ} x_A, \qquad \Delta H_{\text{mix}} < 0, \qquad \Delta V_{\text{mix}} < 0$$

Examples: phenol + aniline, chloroform + acetone (they form an H-bond between them), nitric acid + water.

> **Trap:** chloroform + acetone is negative deviation because a *new* hydrogen bond forms *between* the two. Ethanol + acetone is positive because an *existing* hydrogen bond is broken. Both are asked; the reasoning direction is what earns the mark.

###### Azeotropes

Binary mixtures with the **same composition in liquid and vapour phase**, boiling at constant temperature — so they cannot be separated by fractional distillation.

- **Minimum boiling azeotrope** ← large *positive* deviation. Ethanol + water, 95% ethanol by volume.
- **Maximum boiling azeotrope** ← large *negative* deviation. Nitric acid + water, 68% $\ce{HNO3}$ by mass, boils at 393.5 K.

**Examiner asks:** "define azeotrope + which type from negative deviation, with example" — a 2–3 marker that has run repeatedly.

#### Colligative properties — *four of them, four formulas, one idea*

Properties that depend on the **number** of solute particles, not their identity. That one sentence is the reason every question in this section works.

###### 1 · Relative lowering of vapour pressure

$$\frac{p_1^{\circ} - p_1}{p_1^{\circ}} = x_2 = \frac{n_2}{n_1 + n_2}$$

For a dilute solution $n_1 \gg n_2$, so this simplifies to the working form:

$$\frac{p_1^{\circ} - p_1}{p_1^{\circ}} = \frac{w_2 / M_2}{w_1 / M_1}$$

###### 2 · Elevation of boiling point

$$\Delta T_b = K_b \, m = \frac{K_b \, w_2 \times 1000}{M_2 \, w_1}$$

$K_b$ = molal elevation constant (ebullioscopic constant), units K kg mol⁻¹. For water, $K_b = 0.52$.

###### 3 · Depression of freezing point

$$\Delta T_f = K_f \, m = \frac{K_f \, w_2 \times 1000}{M_2 \, w_1}$$

$K_f$ = molal depression constant (cryoscopic constant). For water, $K_f = 1.86$, freezing point 273 K.

Both constants depend only on the solvent, and can themselves be calculated:

$$K_f = \frac{R \, M_1 T_f^2}{1000 \, \Delta H_{\text{fus}}} \qquad K_b = \frac{R \, M_1 T_b^2}{1000 \, \Delta H_{\text{vap}}}$$

###### 4 · Osmotic pressure

**Osmosis**: solvent flows through a semi-permeable membrane from pure solvent into solution. **Osmotic pressure** ($\pi$) is the extra pressure applied on the solution side that just stops that flow.

$$\pi = CRT = \frac{n_2 RT}{V} = \frac{w_2 RT}{M_2 V}$$

**Why it's preferred for macromolecules** (proteins, polymers): works at room temperature, so heat-unstable biomolecules survive; uses molarity, which is easy to measure; and its magnitude is large even for dilute solutions, which is all you get from a poorly soluble polymer.

> **Trap:** $\pi$ uses *molarity* and volume in litres. $\Delta T_b$ and $\Delta T_f$ use *molality* and solvent mass in kg. Mixing these up is the standard way to lose an otherwise-correct 3-marker.

###### Isotonic, hypertonic, hypotonic

- **Isotonic** — same osmotic pressure, no net osmosis. Blood cells are isotonic with 0.9% w/v NaCl.
- **Hypertonic** — higher concentration outside; water leaves the cell; cell **shrinks**.
- **Hypotonic** — lower concentration outside; water enters; cell **swells** and may burst.

**Reverse osmosis:** apply pressure *greater than* $\pi$ on the solution side and solvent flows backwards, out of the solution. Used to desalinate seawater, with a cellulose acetate membrane that passes water but not ions.

#### Abnormal molar mass and van't Hoff factor — *when the measured mass is wrong, and by how much*

Colligative properties give a molar mass. When the solute associates or dissociates, that measured value differs from the true one — an **abnormal molar mass**.

###### Association

Molecules combine → fewer particles → colligative property falls → measured molar mass comes out **too high**. Ethanoic acid in benzene dimerises through hydrogen bonds: measured 120 g/mol against a true 60.

###### Dissociation

Electrolyte splits into ions → more particles → colligative property rises → measured molar mass comes out **too low**. KCl gives 37.25 g/mol against a true 74.5.

###### van't Hoff factor

$$i = \frac{\text{normal molar mass}}{\text{abnormal molar mass}} = \frac{\text{observed colligative property}}{\text{calculated colligative property}}$$

Equivalently, particles after dissociation/association ÷ particles before.

- **Dissociation** → $i > 1$. KCl: 2. $\ce{MgSO4}$: 2. $\ce{K2SO4}$: 3. $\ce{CaCl2}$: 3.
- **Association** → $i < 1$. Complete dimerisation gives $i = 0.5$.
- **Neither** → $i = 1$. Glucose, urea, sucrose.

Every colligative formula then carries $i$:

$$\frac{p_1^{\circ}-p_1}{p_1^{\circ}} = i\,x_2 \qquad \Delta T_b = i K_b m \qquad \Delta T_f = i K_f m \qquad \pi = \frac{i\,n_2 RT}{V}$$

###### Partial dissociation or association

$$\text{dissociation: } i = 1 + (n-1)\alpha \qquad \text{association: } i = 1 + \left(\tfrac{1}{n}-1\right)\beta$$

$\alpha$ = degree of dissociation, $\beta$ = degree of association, $n$ = particles produced or combined.

> **Trap:** a degree of dissociation cannot exceed 1. If your $\alpha$ comes out at 1.056, the intended answer is "essentially complete dissociation" — say so rather than writing an impossible number.

#### Numerical patterns, collected — *every calculation type in this chapter, one model each*

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

#### Past year questions · question types — *ranked by how often they turn up*

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

#### Past year questions · mark slots — *what each type is worth, and the time that buys*

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

#### Past year questions · repeat offenders — *appeared more than once — highest probability in the chapter*

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

#### Past year questions · cold practice — *answers only — work them before you look*

One model per pattern is above. These are the same patterns with different numbers: work each one cold, then check.

###### Colligative numericals

- 2026 Q14 — 8 g non-volatile solute in 100 g diethyl ether, bp rises 35.60 → 36.86 °C, $K_b = 2.02$. Find $M_2$. 128.25 g/mol

- 2017 — 10 g $\ce{CaCl2}$ ($M=111$) in 200 g water, $K_b = 0.52$. Find $\Delta T_b$. 0.702 K (remember $i=3$)

- 2026 Q8 — 1 molal trichloroacetic acid boils at 100.18 °C, $K_b = 0.512$. Find $i$. 0.35

- 2021 Q15 — 2.56 g sulphur in 100 g $\ce{CS2}$, $\Delta T_f = 1.62$ K, $K_f = 4.9$, $M(\ce{S8}) = 256$. Find % association. $i = 0.846$; 15.4%

###### Vapour pressure

- 2026 Q19 — 61 g benzoic acid in 500 g benzene, $p^{\circ} = 51.2$ mm Hg, complete dimerisation. Find $p_s$. 50.42 mm Hg (use $i = 0.5$)

- Lecture PYQ — pure water $p^{\circ} = 32$ mm Hg at 308 K falls to 31.84 with 10 g solute in 200 g water. Find $M_2$. 180 g/mol

###### Osmotic pressure

- 2020 Q3 — 5% urea solution ($M = 60$) at 300 K, $R = 0.0821$. Find $\pi$. 20.51 atm

- 2019 Q17 — 6% glucose ($M=180$) isotonic with 2.5% of an unknown. Find the unknown's $M$. 75 g/mol

###### Freezing point, two-stage

- 2021 Q21 — 5% cane sugar ($M = 342$) freezes at 271 K. Find the freezing point of 5% glucose ($M = 180$). 269.2 K — find $K_f$ from the sugar first

Built from Sourabh Raina's Solutions one-shot and PYQ videos, cross-checked against NCERT Class XII Chemistry Chapter 1 (Rationalised 2022–23). Constants verified: water $K_b = 0.52$, $K_f = 1.86$ K kg mol⁻¹.

### Chapter 2 · Electrochemistry

`NCERT Class XII Chemistry · Chapter 2 · Electrochemistry`

*14 marks — second heaviest on the blueprint. Two engines run this chapter: the Nernst equation and Faraday's laws. Nearly every numerical is one of those two wearing a different hat.*

#### The two cell types — *the distinction every question hangs off*

|  | Electrochemical (galvanic) | Electrolytic |
|---|---|---|
| Does | Chemical → electrical | Electrical → chemical |
| Reaction | Spontaneous | Non-spontaneous |
| $\Delta G$ | Negative | Positive |
| Anode | Negative | Positive |
| Cathode | Positive | Negative |

Constant across both: **oxidation at the anode, reduction at the cathode.** Only the charge signs flip.

**Examiner asks:** "two points of difference" (2020) is a standing 2-marker. Give the ΔG and the anode-sign pair — they're the two that can't be waffled.

#### Daniell cell and cell notation — *how to write a cell down, and why the salt bridge is there*

Zinc rod in 1 M $\ce{ZnSO4}$, copper rod in 1 M $\ce{CuSO4}$, joined by a salt bridge and an external wire. EMF = **1.1 V** at unit concentration.

$$\ce{Zn(s) -> Zn^2+(aq) + 2e^-} \quad \text{(anode, oxidation)}$$
 $$\ce{Cu^2+(aq) + 2e^- -> Cu(s)} \quad \text{(cathode, reduction)}$$

The zinc rod thins; the copper rod thickens.

###### Cell notation

Anode on the left, cathode on the right. Single line = phase boundary, double line = salt bridge:

$$\ce{Zn(s) | Zn^2+(aq) || Cu^2+(aq) | Cu(s)}$$

###### What the salt bridge actually does

It's a U-tube of electrolyte ($\ce{KCl}$, $\ce{KNO3}$, $\ce{NH4Cl}$) set in agar or gelatin. Without it, $\ce{Zn^2+}$ builds up in the anode compartment and $\ce{SO4^2-}$ in the cathode compartment; the charge separation stalls the cell. The bridge's ions migrate in to neutralise both halves and complete the circuit.

**Examiner asks:** "why is a salt bridge necessary" (2026) — answer with both jobs: maintains electrical neutrality *and* completes the circuit.

#### Electrode potential and SHE — *why everything is written as reduction potential*

Dip a metal in a solution of its own ions and charge separates until equilibrium. That potential difference between metal and solution is the **electrode potential**.

By IUPAC convention **every electrode potential is quoted as a reduction potential** — because you can't subtract an oxidation potential from a reduction potential meaningfully. Oxidation and reduction potentials of the same electrode are numerically equal and opposite in sign.

**Standard electrode potential ($E^{\circ}$):** ion concentration 1 M, 298 K, and 1 bar for any gas.

$$E^{\circ}_{\text{cell}} = E^{\circ}_{\text{cathode}} - E^{\circ}_{\text{anode}}$$

Also written $E_{\text{right}} - E_{\text{left}}$, since cathode sits on the right in cell notation. $E_{\text{cell}}$ for a working cell is always positive.

###### Standard hydrogen electrode

A single half-cell's absolute potential can't be measured — you need a second electrode to get a reading at all. So SHE is defined as the reference with $E^{\circ} = 0.00$ V exactly. It's a platinum foil coated with platinum black, $\ce{H2}$ at 1 bar, $\ce{H+}$ at 1 M.

Connect zinc to SHE: electrons flow zinc → SHE, so zinc is the anode, reading 0.76 V. Then $0.76 = 0 - E^{\circ}_{\ce{Zn^2+/Zn}}$, giving $E^{\circ}_{\ce{Zn^2+/Zn}} = -0.76$ V. Copper against SHE reads 0.34 V with electrons flowing the other way, giving $+0.34$ V.

#### Electrochemical series — *reading a table of E° values*

Arrange standard electrode potentials in order and the series tells you three things at a glance.

- **High $E^{\circ}$** → reduces easily → **strong oxidising agent.** Fluorine, $+2.87$ V, is the strongest.
- **Low (negative) $E^{\circ}$** → oxidises easily → **strong reducing agent.** Lithium, $-3.05$ V, is the strongest.
- **Feasibility:** the species actually being reduced must have the higher $E^{\circ}$. If a proposed reaction has it backwards, the reaction isn't feasible.

Worked · 2023 — E° of a cell

$E^{\circ}_{\ce{Ag+/Ag}} = 0.80$ V, $E^{\circ}_{\ce{Fe^2+/Fe}} = -0.44$ V. Find $E^{\circ}_{\text{cell}}$.

Higher $E^{\circ}$ becomes the cathode, so silver is cathode, iron is anode.

$$E^{\circ}_{\text{cell}} = 0.80 - (-0.44) = 1.24\ \text{V}$$

**Examiner asks:** "which of A and B liberates $\ce{H2}$ from dilute $\ce{H2SO4}$" (2026) — the one with the more negative $E^{\circ}$, because it oxidises more readily.

#### Nernst equation — *the workhorse — for when concentrations aren't 1 M*

Standard potentials assume 1 M. Change the concentration and the potential changes. Nernst gives the relation:

$$E_{\text{cell}} = E^{\circ}_{\text{cell}} - \frac{2.303\,RT}{nF}\log Q$$

At 298 K, with $R = 8.314$ and $F = 96500$, that collapses to the form you'll actually use:

$$E_{\text{cell}} = E^{\circ}_{\text{cell}} - \frac{0.0591}{n}\log \frac{[\text{products}]}{[\text{reactants}]}$$

$n$ = electrons exchanged. **Solids and pure liquids are omitted** — their concentration is constant, taken as unity.

> **Trap:** $n$ is the electrons exchanged *after balancing*, not the charge on one ion. And stoichiometric coefficients become powers inside the log. Both are where marks vanish.

Worked · 2019 — EMF with unequal concentrations

$\ce{Al | Al^3+ (0.001 M) || Ni^2+ (0.1 M) | Ni}$. $E^{\circ}_{\ce{Ni^2+/Ni}} = -0.25$ V, $E^{\circ}_{\ce{Al^3+/Al}} = -1.66$ V.

Balance: Al loses 3e⁻, Ni²⁺ gains 2e⁻ → multiply by 2 and 3 → $n = 6$.

$$E^{\circ}_{\text{cell}} = -0.25 - (-1.66) = 1.41\ \text{V}$$
 $$E_{\text{cell}} = 1.41 - \frac{0.0591}{6}\log\frac{(10^{-3})^2}{(10^{-1})^3} = 1.41 - \frac{0.0591}{6}\log(10^{-3})$$
 $$= 1.41 + \frac{0.0591 \times 3}{6} = 1.41 + 0.0295 = 1.44\ \text{V}$$

###### Nernst at equilibrium → equilibrium constant

At equilibrium $E_{\text{cell}} = 0$ and $Q = K_c$, so:

$$E^{\circ}_{\text{cell}} = \frac{0.0591}{n}\log K_c$$

**Examiner asks:** "why is $K_c$ related to $E^{\circ}_{\text{cell}}$ and not $E_{\text{cell}}$?" (2026) — because at equilibrium $E_{\text{cell}}$ is zero and generates no current, while $E^{\circ}$ stays constant.

#### Gibbs energy and cell EMF — *one equation, two exam uses*

$$\Delta_r G = -nFE_{\text{cell}} \qquad \Delta_r G^{\circ} = -nFE^{\circ}_{\text{cell}}$$

The electrical work a cell does equals the fall in Gibbs energy.

**The intensive/extensive point** the examiner likes: $E_{\text{cell}}$ is **intensive** — multiply the equation by 2 and it doesn't change. $\Delta G$ is **extensive** — it depends on $n$, so doubling the equation doubles it.

Worked · 2025 — ΔG° and log K_c

$\ce{2Cr + 3Cd^2+ -> 2Cr^3+ + 3Cd}$. $E^{\circ}_{\ce{Cd^2+/Cd}} = -0.40$ V, $E^{\circ}_{\ce{Cr^3+/Cr}} = -0.74$ V, $F = 96500$.

Cd is reduced → cathode. $E^{\circ}_{\text{cell}} = -0.40 - (-0.74) = 0.34$ V. Cr loses 3e⁻ × 2 = 6, so $n = 6$.

$$\Delta_r G^{\circ} = -6 \times 96500 \times 0.34 = -196860\ \text{J mol}^{-1} = -196.86\ \text{kJ mol}^{-1}$$

#### Conductance, conductivity, molar conductivity — *four quantities that are easy to confuse*

| Quantity | Symbol | Relation | Unit |
|---|---|---|---|
| Resistance | $R$ | $R = \rho \dfrac{l}{A}$ | Ω |
| Resistivity | $\rho$ | $\rho = R\dfrac{A}{l}$ | Ω cm |
| Conductance | $G$ | $G = 1/R$ | S (siemens) |
| Conductivity | $\kappa$ | $\kappa = 1/\rho$ | S cm⁻¹ |
| Molar conductivity | $\Lambda_m$ | $\Lambda_m = \dfrac{\kappa \times 1000}{M}$ | S cm² mol⁻¹ |

###### Cell constant

$l/A$ is fixed for a given conductivity cell, so it's called the **cell constant** $G^*$:

$$G^* = \frac{l}{A} = \kappa \times R$$

Measuring $l$ and $A$ directly is unreliable, so $G^*$ is found by filling the cell with a solution of known conductivity (usually KCl) and measuring resistance. Once known, the same cell gives $\kappa$ for any solution: $\kappa = G^*/R$.

*Resistance is measured on a Wheatstone bridge with an **AC** source (DC would electrolyse the solution and change its composition) and a purpose-built conductivity cell (a solution can't be wired into the bridge directly).*

Worked · 2024 — resistivity, conductivity, molar conductivity

0.05 M NaOH, cell constant 50 cm⁻¹, resistance $4.5 \times 10^3$ Ω.

$$\kappa = \frac{G^*}{R} = \frac{50}{4.5\times10^3} = 0.011\ \text{S cm}^{-1}$$
 $$\rho = \frac{1}{\kappa} = 90\ \Omega\,\text{cm}$$
 $$\Lambda_m = \frac{0.011 \times 1000}{0.05} = 220\ \text{S cm}^2\text{mol}^{-1}$$

###### Variation with dilution — the two go opposite ways

- **Conductivity falls** on dilution: fewer ions per cm³.
- **Molar conductivity rises** on dilution: the volume holding one mole of electrolyte increases, and interionic attraction weakens.

> **Trap:** these two moving in opposite directions is itself an exam question. Conductivity is per unit *volume*; molar conductivity is per *mole*.

###### Strong vs weak electrolyte on the graph

Plot $\Lambda_m$ against $\sqrt{c}$:

- **Strong electrolyte** — starts high, rises gently and **linearly**. Extrapolate to zero concentration to read $\Lambda_m^{\circ}$ straight off the graph.
- **Weak electrolyte** — starts low, then shoots up steeply near zero concentration, running almost **parallel to the y-axis**. Cannot be extrapolated; you must use Kohlrausch's law instead.

#### Kohlrausch's law — *and its three applications*

**Kohlrausch law of independent migration of ions:** the limiting molar conductivity of an electrolyte is the sum of the individual contributions of its cation and anion.

$$\Lambda^{\circ}_m(\ce{NaCl}) = \lambda^{\circ}_{\ce{Na+}} + \lambda^{\circ}_{\ce{Cl-}}$$
 $$\Lambda^{\circ}_m(\ce{BaCl2}) = \lambda^{\circ}_{\ce{Ba^2+}} + 2\lambda^{\circ}_{\ce{Cl-}}$$

> **Trap:** the stoichiometric multiplier. $\ce{Al2(SO4)3}$ needs $2\lambda^{\circ}_{\ce{Al^3+}} + 3\lambda^{\circ}_{\ce{SO4^2-}}$. Forgetting the 2 and 3 is the whole mistake.

###### 1 · Λ° of a weak electrolyte

Can't be read off a graph, so build it from strong electrolytes that share ions:

$$\Lambda^{\circ}(\ce{CH3COOH}) = \Lambda^{\circ}(\ce{CH3COONa}) + \Lambda^{\circ}(\ce{HCl}) - \Lambda^{\circ}(\ce{NaCl})$$

The $\ce{Na+}$ and $\ce{Cl-}$ terms cancel, leaving exactly $\lambda^{\circ}_{\ce{CH3COO-}} + \lambda^{\circ}_{\ce{H+}}$.

###### 2 · Degree of dissociation

$$\alpha = \frac{\Lambda_m}{\Lambda^{\circ}_m}$$

###### 3 · Dissociation constant

$$K_a = \frac{c\,\alpha^2}{1-\alpha}$$

Worked · 2020 — limiting ionic conductivity from Kohlrausch

$\Lambda^{\circ}(\ce{Al2(SO4)3}) = 858$, $\lambda^{\circ}_{\ce{SO4^2-}} = 160$ S cm² mol⁻¹. Find $\lambda^{\circ}_{\ce{Al^3+}}$.

$$858 = 2\lambda^{\circ}_{\ce{Al^3+}} + 3(160) \Rightarrow 2\lambda^{\circ}_{\ce{Al^3+}} = 858 - 480 = 378$$
 $$\lambda^{\circ}_{\ce{Al^3+}} = 189\ \text{S cm}^2\text{mol}^{-1}$$

#### Faraday's laws of electrolysis — *the second engine of this chapter*

###### First law

Mass deposited is proportional to the charge passed:

$$w = \frac{M \, I \, t}{n \, F}$$

$M$ = molar mass, $I$ = current in amperes, $t$ = time in **seconds**, $n$ = electrons gained per ion, $F = 96500$ C mol⁻¹.

###### Second law

Same charge through different electrolytes deposits masses in the ratio of their **equivalent weights**:

$$\frac{w_1}{w_2} = \frac{E_1}{E_2}, \qquad E = \frac{\text{atomic mass}}{n}$$

So Na (23/1), Mg (24/2 = 12), Al (27/3 = 9) deposit in the ratio 23 : 12 : 9 per faraday.

> **Trap:** time in minutes. Convert to seconds first — this single slip has cost more marks in this chapter than any conceptual error.

Worked · 2017 — mass deposited

2 A through $\ce{AgNO3}$ for 15 min. $M(\ce{Ag}) = 108$.

$t = 15 \times 60 = 900$ s. $\ce{Ag+ + e^- -> Ag}$, so $n = 1$.

$$w = \frac{108 \times 2 \times 900}{1 \times 96500} = 2.014\ \text{g}$$

###### Charge in faradays — without the formula

Often faster to reason directly. To reduce 1 mol $\ce{Zn^2+}$ you need 2 mol of electrons = **2 F** = 193000 C. To reduce 1 mol $\ce{MnO4-}$ to $\ce{Mn^2+}$, Mn goes +7 → +2, so 5 mol electrons = **5 F**.

#### Products of electrolysis — *the E° comparison, and the overpotential exception*

In aqueous solution, water competes with the dissolved ions at both electrodes. Two rules decide the winner:

- **At the cathode:** the species with the **higher** $E^{\circ}$ is reduced.
- **At the anode:** the species with the **lower** $E^{\circ}$ is oxidised.

###### Aqueous NaCl — the standard case

**Cathode:** $\ce{Na+}$ ($-2.71$ V) vs $\ce{H+}$ (0.00 V). Hydrogen wins → $\ce{H2}$ gas.

**Anode:** $\ce{Cl-}$ (1.36 V) vs water → $\ce{O2}$ (1.23 V). By the rule oxygen should win — **but it doesn't.** Oxygen evolution is kinetically slow and needs extra voltage (**overpotential**) to proceed at a useful rate, so chlorine is released instead.

Net: $\ce{NaCl(aq) + H2O -> NaOH + 1/2 H2 + 1/2 Cl2}$

> **Trap:** the overpotential exception is the entire point of this question. Answering "oxygen, because 1.23 < 1.36" is the trap being set. Name overpotential explicitly.

###### Molten vs aqueous

Molten NaCl has no water, so there's no competition: sodium at the cathode, chlorine at the anode.

###### Sulphuric acid

Dilute $\ce{H2SO4}$ → oxygen at the anode. Concentrated → peroxodisulphate, $\ce{2SO4^2- -> S2O8^2- + 2e^-}$ ($E^{\circ} = 1.96$ V).

#### Batteries and fuel cells — *four devices, and the one fact asked about each*

###### Primary — cannot be recharged

**Dry cell (Leclanché):** zinc container = anode, graphite rod surrounded by $\ce{MnO2}$ and carbon = cathode, moist $\ce{NH4Cl}$/$\ce{ZnCl2}$ paste = electrolyte. Used in transistors and clocks.

$$\text{Anode: } \ce{Zn -> Zn^2+ + 2e^-}$$
 $$\text{Cathode: } \ce{MnO2 + NH4+ + e^- -> MnO(OH) + NH3}$$

**Mercury cell:** used in hearing aids and watches. Its selling point — and the exam answer — is that **the potential stays constant through its life**, because no ions appear in the overall reaction, so no concentration changes:

$$\ce{Zn(Hg) + HgO(s) -> ZnO(s) + Hg(l)}$$

###### Secondary — rechargeable

**Lead storage battery** (automobiles, inverters): Pb anode, $\ce{PbO2}$ on a lead grid as cathode, 38% $\ce{H2SO4}$ electrolyte.

$$\ce{Pb + PbO2 + 2H2SO4 -> 2PbSO4 + 2H2O}$$

On **charging** the whole thing runs backwards: $\ce{2PbSO4 + 2H2O -> Pb + PbO2 + 2H2SO4}$.

**Nickel–cadmium:** Cd anode, $\ce{NiO2}$ cathode, KOH electrolyte. Longer life than lead storage but more expensive to make.

###### Fuel cell

Converts a fuel's chemical energy *directly* to electricity, with reactants fed in continuously. The $\ce{H2}$–$\ce{O2}$ cell powered the **Apollo programme**, and its product water was condensed into the astronauts' drinking supply.

$$\text{Anode: } \ce{H2 + 2OH^- -> 2H2O + 2e^-}$$
 $$\text{Cathode: } \ce{O2 + 2H2O + 4e^- -> 4OH^-}$$
 $$\text{Overall: } \ce{2H2 + O2 -> 2H2O}$$

**Two advantages** (the standard 2-marker): ~70% efficiency against ~40% for a thermal plant, and it's pollution-free.

#### Corrosion — *the electrochemical explanation, and two preventions*

Corrosion is chemical attack by atmospheric gases and moisture on a metal surface, giving oxides, sulphides and carbonates. Rusting is the electrochemical case:

$$\ce{2Fe + O2 + 4H+ -> 2Fe^2+ + 2H2O}, \qquad E^{\circ} = 1.67\ \text{V}$$

$\ce{Fe^2+}$ is then oxidised further by atmospheric oxygen to $\ce{Fe^3+}$, and rust is **hydrated ferric oxide**, $\ce{Fe2O3.xH2O}$.

###### Prevention

- **Barrier protection** — paint, bisphenol, or a coat of another metal (Sn, Zn) between iron and the air.
- **Sacrificial protection** — attach a *more reactive* metal (Mg, Zn). It has the more negative $E^{\circ}$, so it oxidises in preference to the iron and corrodes away while the iron survives.

**Examiner asks:** "why are magnesium blocks fixed to iron pipelines" — sacrificial anode; magnesium is more reactive, more negative $E^{\circ}$, oxidises preferentially.

#### Numerical patterns, collected — *five patterns, one model each*

A · Nernst / EMF — *3 marks*

*Recognise it: concentrations given that aren't 1 M.*

1. Write both half-reactions; balance electrons to get $n$.
2. $E^{\circ}_{\text{cell}} = E^{\circ}_{\text{cathode}} - E^{\circ}_{\text{anode}}$.
3. Apply $E = E^{\circ} - \frac{0.0591}{n}\log Q$, coefficients as powers, solids omitted.

B · ΔG° and K_c — *3 marks*

*Recognise it: F is given, or the question says "at equilibrium".*

1. Get $E^{\circ}_{\text{cell}}$ and $n$.
2. $\Delta_r G^{\circ} = -nFE^{\circ}$; divide by 1000 for kJ.
3. For $K_c$: $E^{\circ} = \frac{0.0591}{n}\log K_c$.

C · Conductivity chain — *3–5 marks*

*Recognise it: a resistance and either a cell constant or a known-κ reference solution.*

1. Cell constant: $G^* = \kappa \times R$ from the reference solution, or read it off directly.
2. $\kappa = G^*/R$ for the unknown.
3. $\Lambda_m = \kappa \times 1000 / M$.
4. If asked for α: divide by $\Lambda^{\circ}_m$ from Kohlrausch.

D · Faraday first law — *3 marks*

*Recognise it: current in amperes and a time.*

1. Time → seconds.
2. Find $n$ from the ion's charge.
3. $w = MIt/nF$, rearranged for whatever's missing.

E · Faraday second law (cells in series) — *5 marks*

*Recognise it: two electrolytic cells "connected in series".*

1. Series means identical charge through both.
2. Use the first law on the cell you have full data for, to get time.
3. Then $w_1/w_2 = E_1/E_2$ with $E = \text{atomic mass}/n$.

Worked · 2020 — two cells in series

2 A through $\ce{ZnSO4}$ (cell A) and $\ce{CuSO4}$ (cell B) in series; 2 g Cu deposited. $M(\ce{Cu}) = 63.5$, $M(\ce{Zn}) = 65$.

**Time:** $2 = \dfrac{63.5 \times 2 \times t}{2 \times 96500} \Rightarrow t = \dfrac{2 \times 96500}{63.5} = 3039$ s

**Zinc:** both gain 2 electrons, so

$$\frac{w_{\ce{Zn}}}{2} = \frac{65/2}{63.5/2} \Rightarrow w_{\ce{Zn}} = \frac{65 \times 2}{63.5} = 2.04\ \text{g}$$

#### Past year questions · question types — *ranked by how often they turn up*

*From the last 10 years of boards — 25 questions, grouped by pattern.*

1 · Nernst / EMF calculation — *3 marks*

*Recognise it: a cell notation with concentrations attached.*

1. Balance for $n$.
2. $E^{\circ}_{\text{cell}}$ from the two $E^{\circ}$ values.
3. Nernst, watching the powers in $Q$.

> **Trap:** sign error when $\log$ of a negative power comes down. $-\frac{0.0591}{n}\log10^{-3}$ becomes *plus*.

2 · Conductivity / molar conductivity chain — *3–5 marks*

*Recognise it: a resistance value in ohms.*

1. Cell constant.
2. κ, then ρ if asked.
3. $\Lambda_m$, then α if asked.

> **Trap:** forgetting the ×1000 in $\Lambda_m$, or dividing by the wrong concentration.

3 · Faraday's laws numerical — *3–5 marks*

*Recognise it: amperes, minutes, or "how many faradays".*

1. Seconds.
2. $n$ from the ion.
3. $w = MIt/nF$, or reason directly in moles of electrons.

4 · Electrolysis products with reasoning — *2–3 marks*

*Recognise it: "predict the products", with $E^{\circ}$ values supplied.*

1. Cathode: higher $E^{\circ}$ reduced.
2. Anode: lower $E^{\circ}$ oxidised.
3. Check for the overpotential exception before answering.

5 · Cell/battery definitions and comparisons — *2 marks*

*Recognise it: "define", "name the cell used in…", "two differences".*

1. Name the device.
2. Give both electrode reactions if asked.
3. For differences, answer in matched pairs.

6 · Kohlrausch application — *2–3 marks*

*Recognise it: limiting molar conductivities of ions given.*

1. Write the electrolyte as its ions with correct multipliers.
2. Sum or subtract as needed.
3. For weak electrolytes, build from three strong ones.

#### Past year questions · mark slots — *what each type is worth*

| Question type | Slot | Time |
|---|---|---|
| Nernst / EMF | 3-marker | 5 min |
| Conductivity chain | 3-marker, or part of a 5 | 5–7 min |
| Faraday's laws | 3-marker; series cells is a 5 | 4–7 min |
| Electrolysis products | 2–3 marker | 3 min |
| Definitions / cell names | 2-marker | 2 min |
| Kohlrausch | 2–3 marker | 3 min |
| ΔG° / K_c | 3-marker | 4 min |

*The video splits these as short-answer type I (2 marks), type II (3 marks), and long answer (5 marks) — the conductivity chain and series-cell problems are the ones that appear as 5-markers.*

#### Past year questions · repeat offenders — *appeared more than once — highest probability in the chapter*

2019 Q6 · 2019 Q8 · lecture PYQ

Electrolysis of aqueous NaCl, and the overpotential reason chlorine appears instead of oxygen. Runs almost every year in some form.

2020 Q16 · lecture PYQ

Two electrolytic cells in series, $\ce{ZnSO4}$ and $\ce{CuSO4}$, 2 g copper deposited — identical numbers both times.

2024 Q18 · 2026 Q22 · 2026 Q24

The conductivity → resistivity → molar conductivity chain, sometimes with degree of dissociation added. The single most reliable numerical in the chapter.

2025 Q1 · 2026 Q7(a)

Fuel cells: definition and two advantages, then the Apollo hydrogen–oxygen cell and its drinking-water by-product.

2022 Q13 · 2020 Q21 · 2026 Q22

Kohlrausch's law statement, then applied — degree of dissociation of acetic acid, limiting ionic conductivity of $\ce{Al^3+}$, Λ° of NaCl.

2020 Q3 · 2026 Q23(b)

Electrochemical vs electrolytic cell differences, and primary vs secondary battery differences. Straight recall, always available.

2017 Q5 · 2020 Q21(a)

Which cell is used where — dry cell in transistors, mercury cell in hearing aids and watches, with electrode reactions.

#### Past year questions · cold practice — *answers only — work them before you look*

###### Nernst / EMF

- 2020 Q2 — write cell notation and the Nernst equation for $\ce{Mg + 2Ag+ -> Mg^2+ + 2Ag}$. $\ce{Mg|Mg^2+||Ag+|Ag}$; $E = E^{\circ} - \frac{0.0591}{2}\log\frac{[\ce{Mg^2+}]}{[\ce{Ag+}]^2}$

- 2026 Q19 — EMF of $\ce{Sn|Sn^2+||H+|H2}$ at 298 K with concentrations given. Apply Nernst with $n=2$; $\ce{H2}$ omitted as a gas at 1 bar

###### ΔG° and K_c

- 2026 Q23 — $E^{\circ}$ for $\ce{Cu + 2Ag+ <=> Cu^2+ + 2Ag}$ at equilibrium, $K_c = 10^{15}$. $E^{\circ} = \frac{0.0591}{2}\times 15 = 0.44$ V

###### Conductivity

- Lecture PYQ — 0.05 M KCl, $l = 50$ cm, $A = 0.625$ cm², $R = 5\times10^3$ Ω. Find ρ, κ, Λ_m. 62.5 Ω cm; 0.016 S cm⁻¹; 320 S cm² mol⁻¹

- Lecture PYQ — cell gives 164 Ω with 0.02 M KCl (κ = 2.768×10⁻³), then 78.5 Ω with 0.05 M $\ce{AgNO3}$. Find κ and Λ_m of $\ce{AgNO3}$. $G^* = 0.4539$; κ = 5.78×10⁻³; Λ_m = 115.6 S cm² mol⁻¹

- 2026 Q22 — 0.1 M NaCl, κ = 1.06×10⁻² S cm⁻¹, $\lambda^{\circ}$ Na⁺ = 50.1, Cl⁻ = 76.5. Find Λ_m and α. 106 S cm² mol⁻¹; Λ° = 126.6; α = 0.837

- 2022 Q13(b) — α of acetic acid if Λ_m = 48 and Λ°_m = 400. 0.12

###### Kohlrausch

- 2021–22 — Λ° of $\ce{MgCl2}$ given $\lambda^{\circ}$ Mg²⁺ = 106, Cl⁻ = 76.3. 285.6 S cm² mol⁻¹ (remember the 2×)

###### Faraday's laws

- 2014 — 5 A through $\ce{Ni(NO3)2}$ for 20 min, $M = 58.7$. Mass of Ni? 1.825 g

- 2015 — charge to reduce 1 mol $\ce{Zn^2+}$ to Zn. 2 F = 193000 C

- 2026 Q25(b) — faradays to produce 40 g Al from molten $\ce{Al2O3}$, $M = 27$. 4.44 F

Built from Sourabh Raina's Electrochemistry one-shot and PYQ videos, cross-checked against NCERT Class XII Chemistry Chapter 2 (Rationalised 2022–23). Verified against NCERT: "Kohlrausch law of independent migration of ions"; Faraday constant 96487 C mol⁻¹ (taken as 96500 in working); Daniell cell 1.1 V at unit concentration.

### Chapter 3 · Chemical Kinetics

`NCERT Class XII Chemistry · Chapter 3 · Chemical Kinetics`

*13 marks. Almost pure numerical territory — order from data, integrated rate equations, half-life, activation energy. Four formulas do nearly all the work; the marks go to knowing which one the question is pointing at.*

#### What kinetics answers — *and what it deliberately doesn't*

Three different questions about a reaction, three different branches:

| Question | Answered by |
|---|---|
| Is it feasible? ($\Delta G < 0$) | Thermodynamics |
| How far does it go? | Chemical equilibrium ($K$) |
| How fast, and by what mechanism? | **Chemical kinetics** |

The standard illustration: thermodynamics says diamond → graphite is feasible. Kinetics explains why your ring is safe — the conversion is immeasurably slow.

#### Rate of reaction — *average, instantaneous, and the coefficient division*

Rate = change in concentration per unit time. Reactant concentration falls, so its rate carries a minus sign to keep the rate positive:

$$\text{rate} = -\frac{\Delta[R]}{\Delta t} = +\frac{\Delta[P]}{\Delta t}$$

**Average rate** uses $\Delta$ over a finite interval. **Instantaneous rate** is the slope of the tangent at one moment: $-\dfrac{d[R]}{dt}$.

###### When coefficients differ — divide by them

For $aA + bB \rightarrow cC + dD$:

$$\text{rate} = -\frac{1}{a}\frac{d[A]}{dt} = -\frac{1}{b}\frac{d[B]}{dt} = \frac{1}{c}\frac{d[C]}{dt} = \frac{1}{d}\frac{d[D]}{dt}$$

> **Trap:** "rate of reaction" and "rate of disappearance of B" are different numbers whenever B's coefficient isn't 1. Read which one is asked — this is the entire content of a 2-marker that runs most years.

Worked · 2022 — rate of reaction vs rate of disappearance

$\ce{N2 + 3H2 -> 2NH3}$, rate of formation of $\ce{NH3} = 3.6\times10^{-4}$ mol L⁻¹ s⁻¹. Find the rate of reaction and the rate of disappearance of $\ce{H2}$.

$$\text{rate} = \tfrac{1}{2}\frac{\Delta[\ce{NH3}]}{\Delta t} = \tfrac{1}{2}(3.6\times10^{-4}) = 1.8\times10^{-4}$$
 $$-\frac{\Delta[\ce{H2}]}{\Delta t} = 3 \times \text{rate} = 5.4\times10^{-4}\ \text{mol L}^{-1}\text{s}^{-1}$$

**Examiner asks:** this exact shape, with $\ce{N2}/\ce{H2}/\ce{NH3}$ or $A + 3B \to 2C$. Near-guaranteed 2–3 marker.

#### Rate law and finding the order from data — *the standard 3-marker, step by step*

The rate law is **experimental** — powers are not read off the balanced equation:

$$\text{rate} = k[A]^x[B]^y$$

$x$ and $y$ may or may not equal the stoichiometric coefficients. **Order** = $x + y$. Order can be zero, fractional, or negative; molecularity cannot.

###### Getting x and y from a data table — the method

1. Pick two experiments where **one** concentration is held constant and the other changes.
2. Write the rate law for each; divide one by the other. $k$ and the constant term cancel.
3. Read off the power that makes the ratio work.
4. Repeat with a different pair for the other exponent.
5. Substitute any single experiment back to find $k$.

> **Trap:** choosing two experiments where *both* concentrations change. Nothing cancels and the algebra becomes unsolvable. Scan the table for the constant column first.

###### Order vs molecularity — the comparison they ask for

| Order | Molecularity |
|---|---|
| Sum of powers in the experimental rate law | Number of species colliding in one elementary step |
| Experimental | Theoretical |
| Can be 0, fractional, negative | Whole number only (1, 2, 3) |
| Applies to overall reaction | Only defined for an elementary step |

**Examiner asks:** "can this be an elementary reaction?" (2026) with a fractional order like 3/2 — **no**, because an elementary reaction's order equals its molecularity, which must be a whole number.

#### Units of the rate constant — *one formula, every order*

From rate $= k[\,]^n$, so $k = \text{rate}/[\,]^n$:

$$\text{unit of } k = \text{mol}^{1-n}\,\text{L}^{n-1}\,\text{s}^{-1}$$

| Order | Unit of k |
|---|---|
| Zero | mol L⁻¹ s⁻¹ |
| First | s⁻¹ |
| Second | L mol⁻¹ s⁻¹ |

**Examiner asks:** given a rate law, state the units — or, run backwards, given the units, state the order. Both directions appear.

#### Integrated rate equations — *zero and first order, plus their graphs*

###### Zero order

$$[R] = -kt + [R]_0 \qquad k = \frac{[R]_0 - [R]}{t}$$

Plot $[R]$ against $t$: straight line, **slope $= -k$**, intercept $[R]_0$.

**Example:** decomposition of gaseous ammonia on a hot platinum surface at 1130 K. At high pressure the metal surface saturates with ammonia, so adding more changes nothing — rate becomes independent of concentration:

$$\ce{2NH3(g) ->[Pt] N2(g) + 3H2(g)}, \qquad \text{rate} = k[\ce{NH3}]^0 = k$$

###### First order

$$k = \frac{2.303}{t}\log\frac{[R]_0}{[R]}$$

Plot $\log\dfrac{[R]_0}{[R]}$ against $t$: straight line through the origin, **slope $= k/2.303$**. Plot $\ln[R]$ against $t$ instead and the slope is $-k$, intercept $\ln[R]_0$.

**Examples:** hydrogenation of ethene; all natural and artificial radioactive decay; decomposition of $\ce{N2O5}$ and $\ce{N2O}$.

###### First order in the gas phase — the closed form worth memorising

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

#### Half-life — *and the graph question that turns on it*

Time for half the reactant to be consumed.

$$\text{First order: } t_{1/2} = \frac{0.693}{k} \qquad \text{Zero order: } t_{1/2} = \frac{[R]_0}{2k}$$

**The distinction that gets examined:** first-order half-life is **independent of initial concentration**; zero-order half-life is **directly proportional** to it.

**Examiner asks:** "predict the order from the graph" (2019) — a flat $t_{1/2}$ vs $[R]_0$ line means first order; a straight rising line means zero order.

###### Percentage-completion problems

Set $[R]_0 = 100$ and subtract the percentage completed. 75% done → $[R] = 25$; 99% done → $[R] = 1$.

Worked · 2026 — time for 3/4 decomposition

First order, $k = 2.54\times10^{-3}$ s⁻¹. Time for 3/4 of the reactant to decompose? ($\log 4 = 0.6$)

$[R]_0 = a$, so $[R] = a - \frac{3}{4}a = \frac{a}{4}$.

$$t = \frac{2.303}{k}\log\frac{a}{a/4} = \frac{2.303 \times 0.6}{2.54\times10^{-3}} = 544\ \text{s}$$

A neat consequence worth remembering: for first order, $t_{99\%} = 2 \times t_{90\%}$ — because $\log 100 = 2$ and $\log 10 = 1$.

#### Pseudo first order — *two examples, one idea*

A reaction that is **bimolecular but follows first-order kinetics**, because one reactant is present in such large excess that its concentration doesn't measurably change.

**Hydrolysis of sucrose:**

$$\ce{C12H22O11 + H2O ->[H+] C6H12O6 + C6H12O6}$$

Water is the solvent, so $[\ce{H2O}]$ is effectively constant. Rate $= k[\ce{C12H22O11}]$: order 1, molecularity 2.

**Hydrolysis of an ester** in dilute acid behaves the same way.

**Examiner asks:** (2024) write the rate law, then state order *and* molecularity separately, then name the reaction type. The gap between order 1 and molecularity 2 is the whole point.

#### Temperature dependence and Arrhenius — *the 5-marker's favourite*

Rate roughly **doubles for every 10 K rise** near room temperature. Quantitatively:

$$k = A\,e^{-E_a/RT}$$

$A$ = frequency factor, $E_a$ = activation energy, the minimum energy colliding molecules need.

###### The logarithmic form and its graph

$$\ln k = -\frac{E_a}{RT} + \ln A$$

Against $y = mx + c$ with $y = \ln k$ and $x = 1/T$:

- **Slope** $= -E_a/R$ (negative, so the line falls)
- **Intercept** $= \ln A$

###### Two-temperature form — the one used in numericals

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

#### Collision theory and catalysis — *the definitions that carry marks*

###### Activated complex and the energy profile

Colliding reactant molecules first form a short-lived **activated complex**. The energy needed to reach it is the **activation energy**. The reaction's own energy change is separate:

$$\Delta H = H_{\text{products}} - H_{\text{reactants}}$$

On a potential-energy vs reaction-coordinate plot, the barrier height is $E_a$ either way; what changes is where the products land. Products lower than reactants → $\Delta H$ negative → **exothermic**. Products higher → $\Delta H$ positive → **endothermic**.

###### Maxwell–Boltzmann distribution

Plot the fraction of molecules ($n_E/n_T$) against kinetic energy. Most molecules sit near the **most probable kinetic energy**; only a small tail — roughly 10–20% — carries energy above $E_a$, and only those can react.

**Raise the temperature by 10 K** and the curve flattens and shifts right: the fraction with energy at or above $E_a$ roughly **doubles**. That is precisely why the rate doubles for a 10 K rise.

###### Collision theory

Treats molecules as hard spheres that must collide to react.

**Collision frequency ($Z$):** number of collisions per second per unit volume of reaction mixture.

$$\text{rate} = Z_{AB}\,e^{-E_a/RT}$$

Comparing this with Arrhenius shows the frequency factor $A$ is essentially the **collision frequency**. The theory is accurate for atoms and simple molecules but deviates for complex ones — because not every collision works. Two conditions must both hold:

1. Colliding molecules have energy at least equal to the **threshold energy**.
2. They collide in the **proper orientation**, so old bonds can break and new ones form.

###### Catalysis

A catalyst increases the rate **without itself undergoing any permanent chemical change**. By **intermediate complex theory**, it forms a temporary bond with the reactant, making a transitory intermediate that decomposes into product and releases the catalyst again — which is why a small amount catalyses a large amount of reactant.

The effect is an **alternative pathway of lower activation energy**, so more molecules clear the barrier and the rate rises.

**What a catalyst does not change:** the Gibbs energy of the reaction, the equilibrium constant, or the position of equilibrium. It catalyses forward and backward reactions *to the same extent*, so equilibrium is reached **earlier** but at the same place. And since it can't change $\Delta G$, it cannot make a non-spontaneous reaction happen — only speed up one that already is.

**Examiner asks:** (2017) "effect of a catalyst on activation energy and on ΔG" — lowers $E_a$, leaves $\Delta G$ untouched. Answering only the first half loses the mark.

###### Reaction mechanism and the rate-determining step

For a multi-step reaction, the **slowest step determines the rate** — write the rate law directly from that step's reactants.

Example (2025): $\ce{2H2O2 ->[I-] 2H2O + O2}$ via a slow step $\ce{H2O2 + I- -> H2O + IO-}$ and a fast step. So rate $= k[\ce{H2O2}][\ce{I-}]$, overall order 2 — even though the balanced equation shows $\ce{2H2O2}$.

#### Numerical patterns, collected — *five patterns, one model each*

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

#### Past year questions · question types — *ranked by how often they turn up*

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

#### Past year questions · mark slots — *what each type is worth*

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

#### Past year questions · repeat offenders — *appeared more than once — highest probability in the chapter*

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

#### Past year questions · cold practice — *answers only — work them before you look*

###### Integrated rate equation

- 2017 Q11 — $\ce{N2O5}$ decomposition: 1.6×10⁻² M at $t=0$, 0.8×10⁻² M at 300 s. Show first order and find $t_{1/2}$. $k = 2.3\times10^{-3}$ s⁻¹ at both times; $t_{1/2} = 301$ s

- 2026 Q22 — $\ce{C2H5Cl}$: $p_i = 0.30$ atm, total $p = 0.50$ atm at 30 s. Find $k$. 0.0368 s⁻¹

- 2026 Q4 — $k = 2.54\times10^{-3}$ s⁻¹, time for 3/4 decomposition. 544 s

- 2024 — first order, $k = 1.25\times10^{-3}$ s⁻¹. Time for 5 g to fall to 2.5 g. 554.6 s — note this is just $t_{1/2}$ in disguise

- 2024 — show $t_{99\%} = 2\,t_{90\%}$ for first order. $\log 100 = 2$ vs $\log 10 = 1$

- 2021–22 — first order, 75% decomposed in 30 min. Find $t_{1/2}$. $k = 0.046$ min⁻¹; $t_{1/2} = 15$ min

- Lecture PYQ — zero order, $[R]_0 = 0.1$ M falls to 0.064 M, $k = 4\times10^{-3}$. Find $t$. 9 s

###### Half-life

- 2019 Q10 — rate $= 5.5\times10^{-14}[\ce{C2H4}]$. Units of $k$ and $t_{1/2}$. s⁻¹; $1.26\times10^{13}$ s

- 2026 Q24(b) — first order, 25% decomposed in 25 min. Find $t_{1/2}$. $k = 0.0115$ min⁻¹; $t_{1/2} = 60.26$ min

###### Activation energy

- 2025 Q16 — 50% complete in 20 min at 300 K, 5 min at 350 K. Find $E_a$. 24.2 kJ mol⁻¹

- 2025 Q23(a) — rate doubles from 298 K to 308 K. Find $E_a$. 52.7 kJ mol⁻¹

###### Rate and order

- 2020 — $A + 3B \to 2C$, rate of formation of C $= 2.5\times10^{-4}$. Find rate of reaction and rate of disappearance of B. $1.25\times10^{-4}$; $3.75\times10^{-4}$ mol L⁻¹ s⁻¹

- 2026 Q6 — rate $= k[A][B]^{3/2}$. Overall order, and can it be elementary? 2.5; no — elementary reactions have whole-number order

- 2025 Q18 — order with respect to A and B from a rate table where doubling B leaves the rate unchanged. Order in B is zero

###### Mechanism

- 2025 Q23(b) — $\ce{2H2O2 ->[I-] 2H2O + O2}$, slow step $\ce{H2O2 + I- -> H2O + IO-}$. Rate law and overall order. rate $= k[\ce{H2O2}][\ce{I-}]$; order 2

Built from Sourabh Raina's Chemical Kinetics one-shot and PYQ videos, cross-checked against NCERT Class XII Chemistry Chapter 3 (Rationalised 2022–23). NCERT confirms the Arrhenius form $k = Ae^{-E_a/RT}$ and the term "pseudo first order reaction".

### Chapter 4 · The d- and f-Block Elements

`NCERT Class XII Chemistry · Chapter 4 · d and f Block Elements`

*11 marks, and material you haven't met before. Everything here is written from scratch — terms tagged **[exposure]** are ones you're seeing for the first time, and each gets a proper explanation before it's used. Almost every answer in this chapter traces back to one idea: **how many unpaired d electrons are there?***

#### What the d block is — *where these elements sit, and why they're called "transition"*

**[exposure]** **d-block elements** are the elements of groups 3 to 12 — the wide middle block of the periodic table, sitting between the s block on the left and the p block on the right. What defines them is that electrons are filling a **d orbital**. Each atom has an outermost shell; the shell just inside it is the **penultimate** one, and it's that shell's d orbital being filled. General configuration:

$$(n-1)d^{1-10}\,ns^{1-2}$$

So if the outermost shell is the 4th, the 3d orbital is filling. There are four such series — 3d, 4d, 5d, 6d.

**[exposure]** **Transition element** is a narrower term with a precise definition: an element with a **partially filled d orbital**, either in its atom *or* in any of its stable oxidation states. The word "transition" comes from their position, bridging the reactive metals of the s block and the non-metals of the p block. The definition matters because it excludes some d-block members — see zinc below. Transition elements share a family of properties: variable oxidation states, coloured ions, catalytic behaviour, complex formation, and hardness.

###### The four series

| Series | Orbital | Runs from | Period |
|---|---|---|---|
| First | 3d | Sc (21) → Zn (30) | 4th |
| Second | 4d | Y (39) → Cd (48) | 5th |
| Third | 5d | La (57), then Hf (72) → Hg (80) | 6th |
| Fourth | 6d | Ac (89), then Rf (104) → Cn (112) | 7th |

The gaps in the third and fourth series (58–71 and 90–103) are where the f-block elements sit — pulled out and studied separately.

###### 3d series configurations — learn these, most questions start here

All are $[\text{Ar}]\,3d^n\,4s^2$ except two exceptions:

| Sc $3d^14s^2$ | Ti $3d^24s^2$ | V $3d^34s^2$ |
|---|---|---|
| **Cr $3d^54s^1$** | Mn $3d^54s^2$ | Fe $3d^64s^2$ |
| Co $3d^74s^2$ | Ni $3d^84s^2$ | **Cu $3d^{10}4s^1$** |
| Zn $3d^{10}4s^2$ |  |  |

**Why Cr and Cu break the pattern:** a **half-filled** ($d^5$) or **completely filled** ($d^{10}$) d subshell is extra stable, so an electron shifts from 4s to 3d to reach it.

###### Why Zn, Cd, Hg are not transition elements

Their configuration is $(n-1)d^{10}ns^2$ — the d orbital is **completely filled**, in the ground state and in their common $+2$ oxidation state ($\ce{Zn^2+}$ is $3d^{10}$). No partially filled d orbital in any stable state means they fail the definition.

**Examiner asks:** the flip side — "why is Cu a transition element despite a filled d orbital in the ground state?" Because its common oxidation state $\ce{Cu^2+}$ is $3d^9$, which *is* partially filled. Same for Sc: $3d^1$ in the ground state, so it qualifies even though $\ce{Sc^3+}$ is colourless.

#### Enthalpy of atomization — *the unpaired-electron idea, introduced properly*

**[exposure]** **Enthalpy of atomization** is the energy needed to take one mole of a solid metal and pull it apart into free gaseous atoms. It exists as a measure because it tells you directly how strong the metallic bonding is — strong bonds mean the atoms resist being separated, so the value is high. Transition metals have unusually high values: unpaired d electrons participate in metallic bonding, and more unpaired electrons means a stronger bond. Chromium, with six unpaired electrons ($3d^54s^1$), sits near the top; zinc, with none ($3d^{10}4s^2$), is the lowest in the 3d series.

Two trends carry nearly all the marks:

- **Maximum in the middle of each series**, where unpaired electrons peak.
- **Second and third series > first series.** The 4d and 5d elements have poorly shielding inner electrons, so the effective nuclear charge is higher, metal–metal bonding is stronger, and atomization needs more energy.

**Examiner asks:** "zinc has the lowest enthalpy of atomization" (fully filled d, no unpaired electrons, weak metallic bond) and "why do 2nd/3rd series have greater enthalpy of atomization" (poor shielding → stronger metallic bond). Both recur.

###### Melting and boiling points follow the same logic

Highest in the middle: Cr in the 3d series, Mo in 4d, W in 5d. Mn and Tc are anomalously **low** — their $d^5s^2$ configuration is so stable that the electrons are less free to delocalise into metallic bonding.

Zn, Cd, Hg are **soft metals with low melting points** for the same reason as their low atomization enthalpy: all d electrons paired, weak metallic bond.

#### Ionization enthalpy and the exchange-energy idea — *why the trend is so irregular*

Ionization enthalpy depends on three competing things:

1. **Nuclear attraction** — higher nuclear charge holds electrons tighter, raising it.
2. **Electron repulsion (screening)** — electrons pushing each other out lowers it.
3. **Exchange energy** — see below.

**[exposure]** **Exchange energy** is a stabilising effect that appears when several electrons with **parallel spins** occupy orbitals of equal energy. Such electrons can swap positions with each other, and every possible swap releases a little energy. More possible swaps means more energy released, and losing energy means greater stability. This is the real reason $d^5$ and $d^{10}$ configurations are so stable — they maximise the number of parallel-spin exchanges. It's why chromium is $3d^54s^1$ rather than $3d^44s^2$.

###### The comparisons they set

- **$\ce{Mn+}$ has lower IE than $\ce{Cr+}$.** $\ce{Mn+}$ is $3d^54s^1$; losing one electron gives the stable $3d^5$ $\ce{Mn^2+}$, so it goes easily. $\ce{Cr+}$ is already $3d^5$; removing an electron breaks that stability.
- **$\ce{Fe^2+}$ has lower IE than $\ce{Mn^2+}$.** $\ce{Fe^2+}$ ($3d^6$) loses one to reach the stable $3d^5$; $\ce{Mn^2+}$ is already $3d^5$ and resists.
- **Second IE of Cr and Cu is high.** $\ce{Cr+}$ ($3d^5$) and $\ce{Cu+}$ ($3d^{10}$) are both stable, so the next electron is hard to remove.
- **Third IE of Mn and Zn is high** — $\ce{Mn^2+}$ ($3d^5$) and $\ce{Zn^2+}$ ($3d^{10}$) are stable.

> **Trap:** every one of these is answered by writing the configuration *before and after* the electron leaves, and pointing at whichever side is $d^5$ or $d^{10}$. Don't reason in words alone — write both configurations.

#### Variable oxidation states — *the defining property, and why P-block differs*

**[exposure]** **Variable oxidation state** means one element can lose different numbers of electrons in different compounds — iron exists as both $\ce{Fe^2+}$ and $\ce{Fe^3+}$, manganese runs from $+2$ all the way to $+7$. It happens because in transition elements the $(n-1)d$ and $ns$ orbitals are **very close in energy**. With so small a gap, electrons from both can be pulled into bonding, and the number that participates can vary. Main-group elements have no such near-degenerate pair, so their oxidation states are far more restricted.

- **Most common state is $+2$** across the 3d series (from losing the two 4s electrons) — except Sc, which is $+3$.
- **Maximum variety in the middle:** Mn shows $+2$ to $+7$, the most of any 3d element, because it has the most unpaired electrons available.
- **Fewest at the ends:** Sc and Ti have too few electrons to lose; Cu and Zn have too few vacant d orbitals to use.
- **Cu shows $+1$** ($3d^{10}$, stable) — the only 3d element with a common $+1$ state.

###### Transition vs p-block variability — a standing question

Transition metal oxidation states differ by **one** unit ($\ce{Fe^2+}$, $\ce{Fe^3+}$; V shows 2, 3, 4, 5) because both $(n-1)d$ and $ns$ contribute. P-block states differ by **two** ($\ce{Sn^2+}$, $\ce{Sn^4+}$) because there the p orbital dominates and electrons are lost in pairs.

###### Zero oxidation state in carbonyls

In $\ce{Ni(CO)4}$ and $\ce{Fe(CO)5}$ the metal is in oxidation state **zero**. CO is neutral and forms a sigma bond to the metal while accepting d-electron density back as a pi bond — so no charge is transferred overall.

#### Standard electrode potentials — *reading the E° table for this series*

Across the 3d series, $E^{\circ}(\ce{M^2+/M})$ becomes **less negative** — the tendency to form the $+2$ ion decreases — because ionization enthalpies rise as nuclear charge increases across the row.

###### Copper is the exception — positive E°

$E^{\circ}(\ce{Cu^2+/Cu}) = +0.34$ V, meaning copper prefers to stay as the solid metal. Converting $\ce{Cu(s)}$ to $\ce{Cu^2+}$ needs a high enthalpy of atomization *plus* a high sum of first and second ionization enthalpies, and the energy released on hydration doesn't compensate.

**Consequence asked directly:** copper does not displace hydrogen from acids. It lies below hydrogen in the electrochemical series with a positive reduction potential, so it can't reduce $\ce{H+}$ to $\ce{H2}$. Only oxidising acids ($\ce{HNO3}$, hot conc. $\ce{H2SO4}$) dissolve it.

###### Three more anomalies, each with the same explanation shape

- **Mn, Ni, Zn are more negative than the trend predicts.** $\ce{Mn^2+}$ is $3d^5$ (half-filled, stable); $\ce{Zn^2+}$ is $3d^{10}$ (filled, stable); $\ce{Ni^2+}$ is small so its hydration enthalpy is exceptionally large and negative.
- **$E^{\circ}(\ce{Mn^3+/Mn^2+})$ is highly positive** — $\ce{Mn^3+}$ ($3d^4$) readily gains an electron to become the stable $3d^5$. So $\ce{Mn^3+}$ is a **good oxidising agent**.
- **$E^{\circ}(\ce{Cr^3+/Cr^2+})$ is negative** — $\ce{Cr^2+}$ ($3d^4$) readily loses an electron to become $3d^3$, which is stable ($t_{2g}^3$, half-filled in the lower set). So $\ce{Cr^2+}$ is a **strong reducing agent**.

> **Trap:** $\ce{Mn^3+}$ oxidising and $\ce{Cr^2+}$ reducing are a matched pair, both answered by "which side is the stable configuration". Learn them together — the exam often asks for both in one question.

**$\ce{Cu+}$ is unstable in aqueous solution** — it disproportionates to $\ce{Cu^2+}$ and Cu, because the much more negative hydration enthalpy of the smaller $\ce{Cu^2+}$ more than compensates for the second ionization enthalpy.

#### Magnetic properties — *and the one formula you'll actually compute*

**[exposure]** **Paramagnetic** substances contain **unpaired electrons** and are weakly *attracted* into a magnetic field. **Diamagnetic** substances have all electrons paired and are weakly *repelled*. The distinction exists because an unpaired electron behaves like a tiny magnet whose field isn't cancelled by a partner. Most transition metal ions have unpaired d electrons, so most of their compounds are paramagnetic — $\ce{Mn^2+}$ ($3d^5$, five unpaired) is strongly so, while $\ce{Zn^2+}$ ($3d^{10}$) is diamagnetic.

The strength is measured as **spin-only magnetic moment**:

$$\mu = \sqrt{n(n+2)}\ \text{BM}$$

$n$ = number of unpaired electrons; BM = Bohr magneton.

| Ion | Config | n | μ (BM) |
|---|---|---|---|
| $\ce{Sc^3+}$ | $3d^0$ | 0 | 0 |
| $\ce{Ti^3+}$ | $3d^1$ | 1 | 1.73 |
| $\ce{V^3+}$ | $3d^2$ | 2 | 2.83 |
| $\ce{Cr^3+}$ | $3d^3$ | 3 | 3.87 |
| $\ce{Fe^2+}$ | $3d^6$ | 4 | 4.90 |
| $\ce{Mn^2+}$ | $3d^5$ | 5 | 5.92 |

Worked · 2020 — spin-only moment of Co²⁺

Co has $Z = 27$: $[\text{Ar}]\,3d^7\,4s^2$. Removing two electrons (the 4s pair) gives $\ce{Co^2+} = [\text{Ar}]\,3d^7$.

Filling five d orbitals with 7 electrons: two orbitals paired, three singly occupied → $n = 3$.

$$\mu = \sqrt{3(3+2)} = \sqrt{15} = 3.87\ \text{BM}$$

> **Trap:** the 4s electrons come off **first**, before any 3d electron. $\ce{Co^2+}$ is $3d^7$, not $3d^54s^2$.

#### Why transition compounds are coloured — *d–d transition, and the one exception to it*

**[exposure]** A **d–d transition** is what happens when an electron absorbs light and jumps from a lower-energy d orbital to a higher-energy one. In a complex, the five d orbitals no longer all have the same energy — they split into two sets (called $t_{2g}$ and $e_g$, covered properly in Coordination Compounds). The gap between them happens to match visible light, so the compound absorbs one colour and we see the **complementary** colour. $\ce{Cu^2+}$ ($3d^9$) has an unpaired electron available to jump, so its salts are blue; $\ce{Zn^2+}$ ($3d^{10}$) has no vacancy to jump into, so its salts are white.

**The rule:** colour requires **partially filled** d orbitals. Both $d^0$ and $d^{10}$ are colourless.

| Ion | Config | Colour |
|---|---|---|
| $\ce{Sc^3+}$, $\ce{Ti^4+}$ | $3d^0$ | Colourless |
| $\ce{Ti^3+}$ | $3d^1$ | Purple |
| $\ce{Cr^3+}$ | $3d^3$ | Green |
| $\ce{Mn^2+}$ | $3d^5$ | Pink |
| $\ce{Fe^2+}$ | $3d^6$ | Green |
| $\ce{Cu^2+}$ | $3d^9$ | Blue |
| $\ce{Zn^2+}$ | $3d^{10}$ | Colourless |

###### The exception: charge transfer

**[exposure]** **Ligand-to-metal charge transfer** is a second, different way a compound can be coloured — an electron jumps from the surrounding ligand onto the metal, rather than between two d orbitals. It matters because it explains the compounds that are intensely coloured despite having *no* d electrons at all. $\ce{KMnO4}$ is the standard case: Mn is $+7$, so $3d^0$, and no d–d transition is possible — yet it's deep purple, because charge transfers from oxygen's 2p orbital to manganese's 3d. The same explains $\ce{K2Cr2O7}$'s orange.

**Examiner asks:** "why is $\ce{KMnO4}$ coloured despite $3d^0$?" — charge transfer, not d–d. Getting this distinction right is a whole mark.

#### Catalysis, interstitial compounds, alloys — *three properties, three clean explanations*

###### Catalytic behaviour

Two reasons, and good answers give both:

1. **Variable oxidation state** lets the metal form intermediates by changing state, then revert. The classic: $\ce{Fe^3+}$ catalysing the iodide–persulphate reaction — $\ce{Fe^3+}$ oxidises $\ce{I-}$ to $\ce{I2}$ and becomes $\ce{Fe^2+}$, which is then re-oxidised by persulphate back to $\ce{Fe^3+}$.
2. **Surface adsorption** — reactants stick to the metal surface, which raises their local concentration and weakens their bonds, making reaction easier.

$\ce{V2O5}$ is asked specifically: large surface area, and it changes oxidation state easily to form an unstable intermediate, providing a lower-energy path.

###### Interstitial compounds

**[exposure]** An **interstitial compound** forms when small atoms — hydrogen, boron, carbon, nitrogen — get trapped in the gaps between metal atoms in a crystal lattice. Transition metals sit in three-dimensional lattices with spaces (**interstitial sites**) between the atoms, and small atoms slot into them without displacing anything. The result isn't a normal compound: the ratio isn't a whole number, so these are called **non-stoichiometric**. $\ce{VH_{0.56}}$ means 56 hydrogen atoms per 100 vanadium atoms; $\ce{TiH_{1.7}}$ means 170 per 100.

**Properties:** higher melting points than the pure metal, very hard (some borides approach diamond), retain metallic conductivity, and are chemically inert.

###### Alloy formation

**[exposure]** An **alloy** is a homogeneous solid solution of two or more metals — melt them together and let them solidify. It forms readily when the metals' atomic radii are within about **15%** of each other, because then one metal's atoms can simply take the other's positions in the crystal lattice. Transition metals have very similar atomic sizes, so they alloy easily. Ferrous alloys (Fe with Cr, V, W, Mo, Mn) give steel and stainless steel; brass is Cu–Zn and bronze is Cu–Sn, both pairing a transition with a non-transition metal.

**Examiner asks:** "why do transition metals form alloys" — similar atomic size, so one metal replaces the other in the lattice. Two lines, two marks.

#### Oxides and oxoanions — *the acid–base trend that gets asked every year*

The **highest oxidation number in an oxide coincides with the group number** from Sc to Mn: $\ce{Sc2O3}$ ($+3$, group 3) up to $\ce{Mn2O7}$ ($+7$, group 7). Beyond group 7 no higher oxide than $\ce{Fe2O3}$ is known.

###### The acid–base rule

| Oxidation state of metal | Oxide is | Chromium example |
|---|---|---|
| Low | Basic | $\ce{CrO}$ ($+2$) |
| Intermediate | Amphoteric | $\ce{Cr2O3}$ ($+3$) |
| High | Acidic | $\ce{CrO3}$ ($+6$) |

**Why:** in a low oxidation state the metal has d electrons available to *donate*, so it behaves as a Lewis base. In a high oxidation state the large positive charge lets it *accept* an electron pair — a Lewis acid. As oxidation state rises, metallic character falls and covalent character rises.

**Examiner asks:** "$\ce{Mn2O3}$ is basic whereas $\ce{Mn2O7}$ is acidic" (2019) — a direct application. Give the oxidation numbers ($+3$ and $+7$) and the Lewis reasoning.

###### Oxygen beats fluorine at stabilising high oxidation states

Manganese's highest fluoride is $\ce{MnF4}$ ($+4$), but its highest oxide is $\ce{Mn2O7}$ ($+7$) — even though fluorine is more electronegative. The reason: **oxygen can form multiple bonds** with the metal, fluorine only single bonds. More bonds per atom means a higher oxidation state can be supported.

#### Potassium dichromate — *preparation, the pH equilibrium, structures, oxidising action*

###### The pH interconversion — the most-asked single fact

Chromate and dichromate exist in equilibrium, and pH decides which:

$$\ce{2CrO4^2- + 2H+ <=> Cr2O7^2- + H2O}$$

- **Acidic** (high $\ce{H+}$) → equilibrium shifts right → **dichromate**, $\ce{Cr2O7^2-}$, **orange**.
- **Alkaline** → shifts left → **chromate**, $\ce{CrO4^2-}$, **yellow**.

###### Structures

**Chromate** $\ce{CrO4^2-}$: **tetrahedral**, yellow. **Dichromate** $\ce{Cr2O7^2-}$: **two tetrahedra sharing one corner** through a Cr–O–Cr bridge, bond angle **126°**, orange.

###### Oxidising action in acidic medium

$$\ce{Cr2O7^2- + 14H+ + 6e^- -> 2Cr^3+ + 7H2O}$$

Combine this reduction half with any oxidation half, matching electrons:

- $\ce{6Fe^2+ -> 6Fe^3+ + 6e^-}$ → $\ce{Cr2O7^2- + 6Fe^2+ + 14H+ -> 2Cr^3+ + 6Fe^3+ + 7H2O}$
- $\ce{I-}\to\ce{I2}$, $\ce{H2S}\to\ce{S}$, $\ce{Sn^2+}\to\ce{Sn^4+}$ all work the same way.

Potassium dichromate is used as a **primary standard** in volumetric analysis; sodium dichromate is more soluble and preferred in organic oxidations.

#### Potassium permanganate — *preparation, why it's purple, and both media*

###### Preparation — two steps

**1. Fusion.** $\ce{MnO2}$ fused with KOH in air (or with $\ce{KNO3}$ as oxidant) gives green potassium manganate:

$$\ce{2MnO2 + 4KOH + O2 -> 2K2MnO4 + 2H2O}$$

**2. Oxidation of manganate to permanganate**, either by disproportionation in acid or — commercially — by electrolytic oxidation in alkaline solution:

$$\ce{3MnO4^2- + 4H+ -> 2MnO4^- + MnO2 + 2H2O}$$

**[exposure]** That second reaction is a **disproportionation** — a reaction where *the same element* is simultaneously oxidised and reduced. It's a distinct category because normally one species oxidises while a different one reduces. Here manganese starts at $+6$ in $\ce{MnO4^2-}$ and ends up both higher ($+7$ in $\ce{MnO4^-}$) and lower ($+4$ in $\ce{MnO2}$) in the same step.

**Laboratory route:** a $\ce{Mn^2+}$ salt oxidised by peroxodisulphate: $\ce{2Mn^2+ + 5S2O8^2- + 8H2O -> 2MnO4^- + 10SO4^2- + 16H+}$.

###### Structure and colour

Both $\ce{MnO4^-}$ and $\ce{MnO4^2-}$ are **tetrahedral**. Manganate ($\ce{MnO4^2-}$, Mn is $+6$, $3d^1$) is **green and paramagnetic** — one unpaired electron. Permanganate ($\ce{MnO4^-}$, Mn is $+7$, $3d^0$) is **purple and diamagnetic**. Its colour comes from **charge transfer**, not d–d, since it has no d electrons.

Heating above 513 K decomposes it: $\ce{2KMnO4 -> K2MnO4 + MnO2 + O2}$.

###### Oxidising action — both media, both asked

**Acidic:** $\ce{MnO4^-}$ → $\ce{Mn^2+}$ (5 electrons)

$$\ce{2MnO4^- + 10I^- + 16H+ -> 2Mn^2+ + 5I2 + 8H2O}$$

**Alkaline/neutral:** $\ce{MnO4^-}$ → $\ce{MnO2}$ (3 electrons), and iodide goes to **iodate**, not iodine:

$$\ce{2MnO4^- + H2O + I^- -> 2MnO2 + 2OH^- + IO3^-}$$

> **Trap:** the products differ by medium. Acidic gives $\ce{Mn^2+}$ and $\ce{I2}$; alkaline gives $\ce{MnO2}$ and $\ce{IO3^-}$. Writing the acidic products for an alkaline question loses the whole answer.

**Examiner asks:** "why is permanganate titration not carried out in presence of HCl?" — $\ce{KMnO4}$ oxidises HCl to $\ce{Cl2}$, a side reaction giving an inaccurate end point. Use $\ce{H2SO4}$ instead.

#### Lanthanoids — *the f block, and the contraction that explains everything*

**[exposure]** The **lanthanoids** are the 14 elements following lanthanum (Ce, $Z=58$, to Lu, $Z=71$) in which the **4f orbital** progressively fills. They're pulled out of group 3 and printed as a separate row because they're so chemically alike that keeping them in the main table would be unwieldy. General configuration: $4f^{1-14}\,5d^{0-1}\,6s^2$. Their dominant oxidation state is $+3$, with a few showing $+2$ or $+4$ where that gets them closer to an empty, half-filled or full f subshell.

**[exposure]** **Lanthanoid contraction** is the steady decrease in atomic and ionic radii across the lanthanoid series, from lanthanum to lutetium, as atomic number rises. It happens because 4f electrons **shield poorly** — an f electron is diffuse and doesn't screen the outer electrons from the nucleus effectively. So each added proton pulls the whole electron cloud in a little more, and the atoms shrink steadily instead of staying the same size. The effect is small per element but accumulates over 14 elements into something chemically decisive.

###### Its three consequences — the reason it's examined so heavily

1. **Lanthanoids are hard to separate.** Similar radii → similar chemical properties → separating a mixture is difficult.
2. **4d and 5d elements have nearly identical sizes** (Zr and Hf, Nb and Ta), because the contraction cancels the expected size increase.
3. **Second and third transition series resemble each other** far more than either resembles the first.

**$\ce{Eu^2+}$ is a strong reducing agent** — $+3$ is the stable lanthanoid state, so $\ce{Eu^2+}$ readily loses an electron to reach it, reducing something else in the process.

**[exposure]** **Misch metal** is a commercially useful lanthanoid alloy — roughly **95% lanthanoid, 5% iron**, with traces of S, C, Ca and Al. It exists because separating individual lanthanoids is expensive and often unnecessary; the mixture works fine. It's used in magnesium-based alloys and to make **bullets, shells and lighter flints**, since it sparks when struck.

#### Actinoids — *and the three-way comparison with lanthanoids*

**[exposure]** The **actinoids** are the 14 elements after actinium (Th, $Z=90$, to Lr, $Z=103$) in which the **5f orbital** fills. What sets them apart from lanthanoids is that **all of them are radioactive**, and their 5f, 6d and 7s orbitals are so close in energy that electrons from all three join in bonding — giving a much wider range of oxidation states ($+3$ through $+6$ and beyond) than the lanthanoids' near-uniform $+3$. That, plus the radioactivity, is why their chemistry is described as more complicated.

**Actinoid contraction is greater than lanthanoid contraction**, because 5f electrons shield even more poorly than 4f, so effective nuclear charge rises faster and the radii shrink more sharply.

###### The three differences to write

|  | Lanthanoids | Actinoids |
|---|---|---|
| Orbital filling | 4f | 5f |
| Shielding | Poor | Even poorer → greater contraction |
| Oxidation states | Mainly $+3$; some $+2$, $+4$ | $+3$ common, but also $+4$, $+5$, $+6$ |
| Radioactivity | Only promethium | All of them |

**Examiner asks:** "three points of difference" (2020) — pick orbital, contraction magnitude, and oxidation-state range. Radioactivity is the easy fourth if you need it.

#### Numerical and equation patterns, collected — *the calculable parts of a mostly-descriptive chapter*

A · Spin-only magnetic moment — *2–3 marks*

*Recognise it: an atomic number is given, or "calculate the magnetic moment".*

1. Write the neutral atom's configuration from $Z$.
2. Remove electrons for the ion — **4s first**, then 3d.
3. Fill the five d orbitals singly before pairing; count unpaired $= n$.
4. $\mu = \sqrt{n(n+2)}$ BM.

B · Balancing a redox equation — *3–5 marks*

*Recognise it: "complete and balance", usually with $\ce{MnO4^-}$ or $\ce{Cr2O7^2-}$ in acidic medium.*

1. Write reduction and oxidation halves separately.
2. Balance the metal, then O with $\ce{H2O}$, then H with $\ce{H+}$.
3. Balance charge with electrons.
4. Scale both halves to equal electrons, add, cancel.

Worked · 2025 — permanganate and iodide in acid

**Reduction:** $\ce{MnO4^- -> Mn^2+}$. Add $\ce{4H2O}$ right, $\ce{8H+}$ left. Charge: left $-1+8 = +7$, right $+2$. Add 5 electrons left:

$$\ce{MnO4^- + 8H+ + 5e^- -> Mn^2+ + 4H2O}$$

**Oxidation:** $\ce{2I^- -> I2 + 2e^-}$

Multiply reduction by 2, oxidation by 5:

$$\ce{2MnO4^- + 10I^- + 16H+ -> 2Mn^2+ + 5I2 + 8H2O}$$

C · Oxidation number from a formula — *1–2 marks*

*Recognise it: "write the oxoanion in which the metal shows a state equal to its group number".*

1. Set the metal as $x$; oxygen is $-2$ each; sum to the overall charge.
2. For Mn (group 7): $\ce{MnO4^-}$ gives $x - 8 = -1$, so $x = +7$. For Cr (group 6): $\ce{CrO4^2-}$ or $\ce{Cr2O7^2-}$, both $+6$.

D · Identify the compound (A, B, C chains) — *5 marks*

*Recognise it: a colour-coded sequence — "black-brown solid A fused with KOH gives dark green B, which on oxidation gives dark purple C".*

1. Match colours to compounds: black-brown $\ce{MnO2}$ → dark green $\ce{K2MnO4}$ → dark purple $\ce{KMnO4}$.
2. Write each step's equation.

#### Past year questions · question types — *ranked by how often they turn up*

*From the last 10 years of boards — 25 questions, grouped by pattern. This chapter is overwhelmingly reason-based: most marks come from explaining, not calculating.*

1 · "Give reason" on configuration stability — *2–3 marks*

*Recognise it: any comparison of two ions, oxidising/reducing strength, or an E° anomaly.*

1. Write both configurations, before and after electron transfer.
2. Point at whichever is $d^5$ or $d^{10}$.
3. State the consequence in the question's own language.

> **Trap:** answering "because it's stable" without naming *which* configuration. The $3d^5$ is the mark.

2 · Balancing redox equations — *3–5 marks*

*Recognise it: "complete and balance the following".*

1. Halves separately.
2. Metal → O with water → H with $\ce{H+}$ → charge with electrons.
3. Scale, add, cancel.

3 · Lanthanoid / actinoid comparison — *3 marks*

*Recognise it: "lanthanoid contraction", "three differences", "why is actinoid chemistry more complicated".*

1. Name the orbital (4f vs 5f).
2. Poor shielding → contraction; 5f worse than 4f.
3. Add the oxidation-state range and radioactivity.

4 · Magnetic and colour properties — *2–3 marks*

*Recognise it: "which is colourless/paramagnetic and why", or a μ calculation.*

1. Get the ion's d-configuration.
2. Count unpaired electrons.
3. None → colourless and diamagnetic. Some → coloured and paramagnetic.
4. Check for the charge-transfer exception ($\ce{KMnO4}$, $\ce{K2Cr2O7}$).

5 · $\ce{KMnO4}$ / $\ce{K2Cr2O7}$ preparation and reactions — *3–5 marks*

*Recognise it: named reagent questions, or the A/B/C identification chain.*

1. Preparation equations.
2. The pH interconversion for chromate/dichromate.
3. Oxidising action — check which medium is asked.

6 · Physical-property trends — *2–3 marks*

*Recognise it: enthalpy of atomization, melting point, or a graph across the series.*

1. Count unpaired electrons.
2. More unpaired → stronger metallic bond → higher value.
3. For 2nd/3rd series, add the poor-shielding argument.

#### Past year questions · mark slots — *what each type is worth*

| Question type | Slot | Time |
|---|---|---|
| "Give reason" (configuration) | 2–3 marker | 2–3 min |
| Balancing redox equations | 3-marker; both media is a 5 | 5–7 min |
| Lanthanoid/actinoid comparison | 3-marker | 3 min |
| Magnetic moment calculation | 2–3 marker | 3 min |
| $\ce{KMnO4}$/$\ce{K2Cr2O7}$ chemistry | 3–5 marker | 5–7 min |
| Graph/trend interpretation | 3-marker | 4 min |
| Definitions (misch metal, oxoanion) | 1–2 marker | 2 min |

*The video splits these as short-answer type I (2 marks), type II (3 marks) and long answer (5 marks) — the $\ce{KMnO4}$ chemistry and multi-part "answer the following" sets are where the 5-markers sit.*

#### Past year questions · repeat offenders — *appeared more than once — highest probability in the chapter*

2017 Q3 · 2017 Q8 · 2019 Q2

"Transition metals show variable oxidation state" and "Zn, Cd, Hg are soft metals" — asked together, repeatedly, in the same two-part format.

2024 Q5 · lecture PYQ

Define lanthanoid contraction, then why actinoid contraction is greater. The single most reliable f-block question.

2025 Q4 · 2026 Q25(b)

Balance $\ce{MnO4^-}$ with $\ce{I^-}$ — once in acidic medium alone, once acidic *and* alkaline in the same question.

2022 Q15 · 2022 Q16 · lecture PYQ

Graph questions on enthalpy of atomization and E° values — lowest in 3d series (Zn), why 2nd/3rd series are higher, why Mn's E° is exceptionally negative, why Cu's is exceptionally positive.

2020 Q11 · 2026 Q22

Lanthanoids vs actinoids — three differences, then why actinoid chemistry is more complicated.

2020 Q10 · 2022 Q12 · 2020 Q6

Colour and magnetism: $\ce{Sc^3+}$ vs $\ce{Cr^3+}$, which ion is colourless, spin-only moment of $\ce{Co^2+}$. All answered by counting unpaired electrons.

2023 Q17 · 2017 Q13 · 2020 Q20

Mn's $+7$ state, transition metals as catalysts, and interstitial compound formation. Standard reason-based trio.

#### Past year questions · cold practice — *answers only — work them before you look*

###### Configuration reasoning

- 2026 Q7(a) — why is the third ionization enthalpy of Mn high? $\ce{Mn^2+}$ is $3d^5$, half-filled and stable; removing a third electron breaks it

- 2019 Q13(c) — why is $E^{\circ}(\ce{Mn^3+/Mn^2+})$ highly positive compared with $\ce{Cr^3+/Cr^2+}$? $\ce{Mn^3+}$ gains one to reach stable $3d^5$; $\ce{Cr^3+}$ is already stable $3d^3$

- 2017 Q9(a) — how does variability of oxidation state differ between transition and p-block? Transition differ by 1 unit; p-block by 2

- 2026 Q21(a) — why is Cu a transition element despite a filled d orbital? $\ce{Cu^2+}$ is $3d^9$ — partially filled in its common oxidation state

###### Magnetism and colour

- 2020 Q6 — spin-only moment of $\ce{Co^2+}$, $Z = 27$. $3d^7$, $n=3$, $\mu = 3.87$ BM

- 2022 Q12 — which of $\ce{Ti^4+}$, $\ce{Cr^3+}$, $\ce{V^3+}$ is colourless and why? $\ce{Ti^4+}$ — $3d^0$, no d–d transition possible

- 2020 Q10 — $\ce{Sc^3+}$ or $\ce{Cr^3+}$: which shows magnetic behaviour? $\ce{Cr^3+}$ ($3d^3$, paramagnetic); $\ce{Sc^3+}$ is $3d^0$, diamagnetic

- 2026 Q21(b) — $\ce{KMnO4}$ or $\ce{K2MnO4}$: which is paramagnetic? $\ce{K2MnO4}$ — Mn is $+6$, $3d^1$, one unpaired electron

###### Equations

- 2025 Q4 — balance $\ce{Cr2O7^2-}$ with $\ce{Fe^2+}$ in acid. $\ce{Cr2O7^2- + 6Fe^2+ + 14H+ -> 2Cr^3+ + 6Fe^3+ + 7H2O}$

- 2026 Q25(b) — $\ce{MnO4^-}$ with $\ce{I^-}$ in alkaline medium. $\ce{2MnO4^- + H2O + I^- -> 2MnO2 + 2OH^- + IO3^-}$

- 2026 Q25(a) — identify A, B, C: black-brown solid fused with KOH in air → dark green → electrolytic oxidation → dark purple. A = $\ce{MnO2}$, B = $\ce{K2MnO4}$, C = $\ce{KMnO4}$

- 2023 — what happens when $\ce{KMnO4}$ is heated? $\ce{2KMnO4 -> K2MnO4 + MnO2 + O2}$ at 513 K

###### f block

- 2019 Q19 — why is $\ce{Eu^2+}$ a strong reducing agent? Loses one electron to reach the stable $+3$ lanthanoid state

- 2019 Q19(b) — why is separating a lanthanoid mixture difficult? Similar radii from lanthanoid contraction → similar chemical properties

- 2019 Q14(a) — general electronic configuration of lanthanoids. $4f^{1-14}\,5d^{0-1}\,6s^2$

- 2025 Q24(a) — what is misch metal, and one use? ~95% lanthanoid + 5% Fe with traces; used in Mg alloys, bullets, shells, lighter flints

Built from Sourabh Raina's d and f Block one-shot and PYQ videos, cross-checked against NCERT Class XII Chemistry Chapter 4 (Rationalised 2022–23). First-contact material: every term marked **[exposure]** is explained from scratch before use.

### Chapter 5 · Coordination Compounds

`NCERT Class XII Chemistry · Chapter 5 · Coordination Compounds`

*11 marks, and entirely new ground. This chapter has more vocabulary than any other in the paper, so nothing here assumes you've met a term before — every one tagged **[exposure]** is defined in plain words, with a worked example, before it gets used again.*

#### What a coordination compound actually is — *start here — the whole chapter builds on this one picture*

**[exposure]** A **coordination compound** is a compound in which a central metal atom or ion is surrounded by, and bonded to, a fixed number of molecules or negative ions. Transition metals form these in huge numbers because they have small, highly charged ions and empty d orbitals ready to accept electron pairs. The bond isn't the usual "one electron each" kind — the surrounding species donates *both* electrons. A standard example is $\ce{[Co(NH3)6]^3+}$: one cobalt ion at the centre, six ammonia molecules attached around it.

They matter well beyond the exam: **chlorophyll** is a coordination compound of magnesium, **haemoglobin** of iron, and **vitamin B₁₂** of cobalt. Industrially they're used in electroplating, dyeing, medicine, metal extraction and catalysis.

###### The square bracket is the whole notation

Everything **inside** the square bracket travels together as one unit and does *not* break apart in water. Everything **outside** is a separate ion that dissociates freely.

$$\ce{[Co(NH3)6]Cl3} \rightarrow \underbrace{\ce{[Co(NH3)6]^3+}}_{\text{stays intact}} + \underbrace{\ce{3Cl^-}}_{\text{free in solution}}$$

###### Complex vs double salt — the distinction they examine

|  | Double salt | Complex |
|---|---|---|
| In water | Dissociates completely into all its ions | The bracketed part keeps its identity |
| Example | Mohr's salt $\ce{FeSO4.(NH4)2SO4.6H2O}$ | $\ce{K4[Fe(CN)6]}$ |
| What you detect | $\ce{Fe^2+}$ gives a positive test | No free $\ce{Fe^2+}$ — the complex ion survives |

Also double salts: carnallite $\ce{KCl.MgCl2.6H2O}$ and potash alum $\ce{K2SO4.Al2(SO4)3.24H2O}$. They exist only in the solid state.

**Examiner asks:** "difference between a complex and a double salt" (2019) — answer with the water behaviour and one example each.

#### Werner's theory — *the 1898 idea that made the whole subject make sense*

Alfred Werner explained a puzzle: why does $\ce{CoCl3}$ combine with different numbers of $\ce{NH3}$ to give differently coloured compounds with different behaviour? His answer was that a metal has **two kinds of valence**.

**[exposure]** **Primary valence** is the metal's ordinary oxidation number — the charge it carries. It is **ionisable**, meaning whatever satisfies it can break away in water, and it is satisfied by **negative ions**. In $\ce{[Co(NH3)6]Cl3}$ cobalt is $+3$, so its primary valence is 3, satisfied by the three chloride ions sitting outside the bracket — which is exactly why those three come free in solution.

**[exposure]** **Secondary valence** is the number of species directly bonded to the metal — what we now call the coordination number. It is **non-ionisable**, so these stay attached in water, and it's satisfied by neutral molecules or negative ions that donate a lone pair. It is **fixed for a given metal**. In $\ce{[Co(NH3)6]Cl3}$ the secondary valence is 6, satisfied by the six ammonia molecules inside the bracket. Those ligands arrange themselves in a definite shape in space — the **coordination polyhedron**.

###### How Werner proved it — the silver nitrate experiment

Add excess $\ce{AgNO3}$ to each compound. Only **free** chloride ions precipitate as AgCl, so counting the moles of AgCl tells you how many chlorides are outside the bracket:

| Formula | Colour | Moles AgCl | Actual structure |
|---|---|---|---|
| $\ce{CoCl3.6NH3}$ | Yellow | 3 | $\ce{[Co(NH3)6]Cl3}$ |
| $\ce{CoCl3.5NH3}$ | Purple | 2 | $\ce{[Co(NH3)5Cl]Cl2}$ |
| $\ce{CoCl3.4NH3}$ | Green | 1 | $\ce{[Co(NH3)4Cl2]Cl}$ |

Notice the coordination number stays **6** throughout — as ammonia leaves the bracket, chloride moves in to take its place.

#### The vocabulary — *nine terms, each with its own example*

**[exposure]** **Central atom or ion** — the metal at the middle, the one everything else attaches to. It acts as a **Lewis acid**: it's electron-deficient, so it *accepts* electron pairs. In $\ce{[Ni(H2O)4Cl2]}$ the central ion is $\ce{Ni^2+}$; in $\ce{[Fe(CN)6]^3-}$ it's $\ce{Fe^3+}$.

**[exposure]** **Ligand** — a molecule or ion attached to the central metal. It must have at least one **lone pair of electrons** to donate, which is what lets it act as a **Lewis base**. Ligands range from simple ions ($\ce{Cl^-}$, $\ce{CN^-}$) through small molecules ($\ce{H2O}$, $\ce{NH3}$) to whole proteins. The specific atom in the ligand that donates the pair is the **donor atom** — in $\ce{NH3}$ it's the nitrogen.

**[exposure]** **Coordinate bond** — the bond formed when *one* species supplies *both* electrons of the shared pair. It exists as a separate name because an ordinary covalent bond takes one electron from each partner. Once formed it's indistinguishable from a normal covalent bond; only its origin differs. Every metal–ligand bond in this chapter is one.

**[exposure]** **Coordination number** — the number of donor atoms directly bonded to the metal. Count **donor atoms, not ligands**, and count only sigma bonds. In $\ce{[Co(NH3)6]^3+}$ six ammonias give six donor atoms, so CN = 6. But in $\ce{[Co(en)3]^3+}$ there are only three ligands — each supplies *two* nitrogen donors, so CN = $3\times2 = 6$ again.

**[exposure]** **Coordination sphere** — the central metal plus its ligands, written inside the square bracket together with the overall charge. Whatever sits outside is the **counter ion**, which is the ionisable part. In $\ce{K4[Fe(CN)6]}$ the coordination sphere is $\ce{[Fe(CN)6]^4-}$ and the counter ions are four $\ce{K+}$.

**[exposure]** **Coordination polyhedron** — the shape the ligands make in space around the metal. It exists as a term because the geometry, not just the count, determines the compound's properties and isomers. Six ligands give an **octahedron** (90° angles), four give either a **tetrahedron** (109.5°) or a **square planar** arrangement (90°, all in one plane).

###### Oxidation number of the central atom

The charge the metal would carry if every ligand were removed along with its donated electron pair. Write it as a Roman numeral in brackets after the metal's name.

**Method:** set the metal as $x$, add each ligand's charge, set the sum equal to the overall charge on the bracket. For $\ce{[Cu(CN)4]^3-}$: $x + 4(-1) = -3$, so $x = +1$ → copper(I).

###### Homoleptic vs heteroleptic

**Homoleptic** — one type of ligand only, e.g. $\ce{[Co(NH3)6]^3+}$. **Heteroleptic** — more than one type, e.g. $\ce{[Co(NH3)4Cl2]+}$.

#### Types of ligand — *denticity, ambidentate, and the chelate effect*

**[exposure]** **Denticity** is simply how many donor atoms a single ligand uses to grip the metal — from Latin *dens*, tooth. The word exists because a ligand with several donor atoms behaves very differently from one with a single donor: it can clamp onto the metal at multiple points at once. A ligand with one donor site is **unidentate**, two is **didentate**, three or more is **polydentate**.

| Type | Donor sites | Examples |
|---|---|---|
| Unidentate | 1 | $\ce{Cl^-}$, $\ce{NH3}$, $\ce{H2O}$, $\ce{OH^-}$, $\ce{CN^-}$ |
| Didentate | 2 | ethane-1,2-diamine (en); oxalate $\ce{C2O4^2-}$ (ox) |
| Polydentate | 3+ | EDTA⁴⁻ — **hexadentate** |

**EDTA⁴⁻** is worth knowing precisely: it binds through **two nitrogen atoms and four oxygen atoms**, six donor sites in total.

**[exposure]** An **ambidentate ligand** is a unidentate ligand that has *more than one kind* of donor atom available, and can attach through either one — but only one at a time. It's a distinct category because it creates isomers that differ purely in which atom did the bonding. $\ce{NO2^-}$ can bind through nitrogen (called **nitrito-N**) or through oxygen (**nitrito-O**). $\ce{SCN^-}$ can bind through sulphur (**thiocyanato**) or nitrogen (**isothiocyanato**).

**[exposure]** A **chelate ligand** is a didentate or polydentate ligand that grips one metal ion at two or more points, forming a **ring** that includes the metal — the word comes from the Greek for a crab's claw. It matters because chelate complexes are markedly **more stable** than equivalent complexes made from separate unidentate ligands. In $\ce{[Pt(en)Cl2]}$, the "en" ligand bonds through both its nitrogens, closing a five-membered ring around the platinum.

**Why chelates are more stable:** replacing six separate unidentate ligands with three didentate ones releases more free particles into solution, so entropy rises; combined with a favourable enthalpy this makes $\Delta G$ more negative. More rings means more stability.

#### IUPAC nomenclature — *the rules in order, then worked examples*

###### Naming a complex — the rules

1. **Cation first, then anion** — as in any ionic compound.
2. **Ligands before the metal**, in **alphabetical order** regardless of charge.
3. **Anionic ligands end in -o**: chlorido, bromido, cyanido, hydroxido, sulphato, oxalato.
4. **Neutral ligands** keep special names: $\ce{H2O}$ = **aqua**, $\ce{NH3}$ = **ammine** (two m's), $\ce{CO}$ = **carbonyl**, $\ce{NO}$ = nitrosyl.
5. **Prefixes** di, tri, tetra for simple ligands; **bis, tris, tetrakis** when the ligand's own name already contains a prefix (then bracket the ligand).
6. Prefixes are **ignored** when alphabetising.
7. **Oxidation number** in Roman numerals, in brackets, right after the metal.
8. If the complex ion is an **anion**, the metal name ends in **-ate** (ferrate, cuprate, argentate, zincate, cobaltate).

Worked — three names built step by step

**$\ce{[Co(NH3)4(H2O)Cl]Cl2}$:** alphabetise ammine, aqua, chlorido. Four ammines → tetraammine. Charge: $x + 0 + 0 - 1 = +2$, so $x = +3$.

 → **tetraamminaquachloridocobalt(III) chloride**

**$\ce{[Cr(NH3)3Cl3]}$:** neutral overall, so $x - 3 = 0$, $x = +3$.

 → **triamminetrichloridochromium(III)**

**$\ce{[PtCl2(en)2]^2+}$:** "c" before "e", so chlorido first. "en" already contains "di", so use **bis** and bracket it. $x + 0 - 2 = +2$, $x = +4$.

 → **dichloridobis(ethane-1,2-diamine)platinum(IV)**

**$\ce{K4[Fe(CN)6]}$:** anionic complex, so iron becomes **ferrate**. $x - 6 = -4$, $x = +2$.

 → **potassium hexacyanidoferrate(II)**

###### Writing the formula from a name

1. Metal first, then ligands in **alphabetical order**.
2. Polydentate and abbreviated ligands go in **parentheses**; alphabetise abbreviations by their first letter (en → e, ox → o).
3. Whole coordination entity in **square brackets**, no spaces inside.
4. Charge as a right superscript outside the bracket, number before sign.

> **Trap:** "ammine" with two m's is $\ce{NH3}$; "amine" with one m is an organic amine like ethane-1,2-di**amine**. NCERT uses both, in these exact senses. Also: current IUPAC is **chlorido**, not chloro.

#### Isomerism — *two families, seven types — the biggest mark-earner in the chapter*

**[exposure]** **Isomers** are compounds with the same formula but a different arrangement of atoms. In coordination chemistry they split into two families: **stereoisomers**, where the connections are the same but the spatial arrangement differs, and **structural isomers**, where what is bonded to what actually differs. The distinction matters because the two families are detected in completely different ways — stereoisomers by geometry and optical activity, structural ones by simple chemical tests.

###### Stereoisomerism 1 · Geometrical (cis–trans)

Same ligands, different positions. **Cis** = identical ligands adjacent; **trans** = opposite.

- **Square planar $\ce{MX2L2}$** — shows cis and trans. Example: $\ce{[Pt(NH3)2Cl2]}$.
- **Octahedral $\ce{MX2L4}$** — shows cis and trans. Example: $\ce{[Co(NH3)4Cl2]+}$.
- **Octahedral $\ce{[CoCl2(en)2]+}$** — cis and trans.
- **Octahedral $\ce{MA3B3}$** — gives **facial (fac)** where the three identical ligands occupy one triangular face, and **meridional (mer)** where they lie around a meridian. Example: $\ce{[Co(NH3)3(NO2)3]}$.

> **Trap:** **tetrahedral complexes do not show geometrical isomerism.** In a tetrahedron every position is adjacent to every other — all angles stay 109.5° however you swap ligands, so there's no "opposite" to be trans to. This is a standing exam question.

###### Stereoisomerism 2 · Optical

**[exposure]** A complex is **optically active** when it has no plane of symmetry, so its mirror image cannot be superimposed on it — like your left and right hands. Such a molecule is **chiral**, and the two mirror-image forms are **enantiomers**: one rotates plane-polarised light to the right (**dextro, d**), the other equally to the left (**laevo, l**). It matters because two compounds identical in every other property can be told apart this way.

Most common in octahedral complexes with didentate ligands:

- $\ce{[Cr(ox)3]^3-}$ — type $\ce{M(AA)3}$, optically active.
- $\ce{[Co(en)2Cl2]+}$ — type $\ce{M(AA)2X2}$: the **cis** form is optically active, the **trans** form is not (its mirror image is superimposable).

**Examiner asks:** "draw the geometrical isomer of $\ce{[Pt(en)2Cl2]^2+}$ which is optically active" — draw the **cis** form. Trans is always the optically inactive one in these.

###### Structural isomerism — four types

| Type | What differs | Example pair |
|---|---|---|
| **Linkage** | Which atom of an ambidentate ligand bonds | $\ce{[Co(NH3)5(NO2)]^2+}$ vs $\ce{[Co(NH3)5(ONO)]^2+}$ |
| **Ionisation** | Ligand and counter ion swap places | $\ce{[Co(NH3)5SO4]Br}$ vs $\ce{[Co(NH3)5Br]SO4}$ |
| **Hydrate** | Water inside vs outside the sphere | $\ce{[Cr(H2O)6]Cl3}$ (violet) vs $\ce{[Cr(H2O)5Cl]Cl2.H2O}$ |
| **Coordination** | Ligands swap between a cationic and anionic complex | $\ce{[Co(NH3)6][Cr(CN)6]}$ vs $\ce{[Cr(NH3)6][Co(CN)6]}$ |

**The chemical test for ionisation isomers** (asked directly): add $\ce{BaCl2}$ — the isomer with free sulphate gives a white $\ce{BaSO4}$ precipitate. Add $\ce{AgNO3}$ — the isomer with free chloride gives white AgCl. Whichever ion is *outside* the bracket is the one that reacts.

#### Valence bond theory — *the hybridisation method — work every NCERT example the same way*

VBT says the metal makes empty **hybrid orbitals** of equal energy, and each ligand donates a lone pair into one of them.

| CN | Hybridisation | Geometry |
|---|---|---|
| 4 | $sp^3$ | Tetrahedral |
| 4 | $dsp^2$ | Square planar |
| 6 | $d^2sp^3$ | Octahedral (inner orbital) |
| 6 | $sp^3d^2$ | Octahedral (outer orbital) |

**[exposure]** A **strong field ligand** pushes hard enough on the metal's d electrons to force them to **pair up**, freeing inner d orbitals for bonding. A **weak field ligand** doesn't, so the electrons stay unpaired. This single distinction decides the hybridisation, the geometry, and the magnetism of every complex below. **Strong:** $\ce{CN^-}$, $\ce{CO}$, and $\ce{NH3}$ when the metal is highly charged ($\ce{Co^3+}$, $\ce{Cr^3+}$). **Weak:** $\ce{F^-}$, $\ce{Cl^-}$, $\ce{H2O}$.

###### The method — five steps, every time

1. Find the metal's oxidation number, then its d-electron count.
2. Draw the d orbitals and fill them.
3. Ask: strong ligand (pair up) or weak (leave unpaired)?
4. Count how many orbitals the ligands need, and take that many empty ones — **inner** 3d if pairing freed some, otherwise **outer** 4d.
5. Name the hybridisation, the geometry, and the magnetism.

| Complex | Metal | Ligand | Hybrid | Geometry | Magnetism |
|---|---|---|---|---|---|
| $\ce{[Co(NH3)6]^3+}$ | $\ce{Co^3+}$, $3d^6$ | Strong | $d^2sp^3$ | Octahedral | Diamagnetic |
| $\ce{[CoF6]^3-}$ | $\ce{Co^3+}$, $3d^6$ | Weak | $sp^3d^2$ | Octahedral | Paramagnetic |
| $\ce{[NiCl4]^2-}$ | $\ce{Ni^2+}$, $3d^8$ | Weak | $sp^3$ | Tetrahedral | Paramagnetic |
| $\ce{[Ni(CN)4]^2-}$ | $\ce{Ni^2+}$, $3d^8$ | Strong | $dsp^2$ | Square planar | Diamagnetic |
| $\ce{[Ni(CO)4]}$ | $\ce{Ni}$, $3d^84s^2$ | Strong | $sp^3$ | Tetrahedral | Diamagnetic |

Worked — $\ce{[Ni(CO)4]}$, the one that catches people out

CO is neutral, so nickel's oxidation state is **0** — configuration $3d^8\,4s^2$.

CO is a strong ligand: it forces pairing. The two 4s electrons move into 3d, filling it to $3d^{10}$ and leaving 4s empty.

Four CO ligands need four orbitals: one 4s + three 4p → **$sp^3$**, tetrahedral. All electrons paired → **diamagnetic**.

> **Trap:** $\ce{[NiCl4]^2-}$ and $\ce{[Ni(CN)4]^2-}$ have the same metal in the same oxidation state but *different* geometry and magnetism — purely because $\ce{Cl^-}$ is weak and $\ce{CN^-}$ is strong. This exact pair is a favourite comparison.

**[exposure]** **Inner orbital** (or **low spin**, or **spin-paired**) complexes use the metal's *inner* 3d orbitals, which only become free when a strong ligand forces pairing — so they have few or no unpaired electrons. **Outer orbital** (**high spin**, **spin-free**) complexes use the outer 4d orbitals because a weak ligand left the 3d electrons unpaired and in the way. The names are just describing which shell supplied the orbitals: $\ce{[Co(NH3)6]^3+}$ is inner/low-spin, $\ce{[CoF6]^3-}$ is outer/high-spin.

###### Magnetic moment

$$\mu = \sqrt{n(n+2)}\ \text{BM}$$

Measuring $\mu$ tells you $n$, which tells you whether the ligand was strong or weak — this is how VBT is tested experimentally.

###### Limitations of VBT — asked as a list

1. Involves many assumptions.
2. Gives no quantitative account of magnetic data.
3. Does not explain the **colour** of complexes.
4. Gives no quantitative account of stability.
5. Cannot predict whether a 4-coordinate complex will be tetrahedral or square planar.
6. Does not distinguish weak from strong ligands — it just assumes the answer.

#### Crystal field theory — *the model that finally explains colour*

**[exposure]** **Crystal field theory** treats the metal–ligand bond as purely **electrostatic attraction** — the positive metal ion pulling on negative ions or on the negative end of polar molecules. It replaced VBT's covalent picture because it can explain what VBT could not: why complexes are coloured, and why some are high spin and others low. Anionic ligands like $\ce{Cl^-}$ are treated as point negative charges; neutral ones like $\ce{H2O}$ as dipoles pointing their negative end at the metal.

**[exposure]** **Crystal field splitting** is the central idea. In a free metal ion all five d orbitals have identical energy — they are **degenerate**. If you surrounded the ion with an evenly spread sphere of negative charge, all five would rise in energy equally and stay degenerate. But real ligands arrive from *specific directions*, so some d orbitals get pushed much harder than others. The degeneracy breaks and the five orbitals split into two groups at different energies. That energy gap is what visible light interacts with — which is where colour comes from.

###### Octahedral field

Ligands approach **along the x, y and z axes**.

- $d_{x^2-y^2}$ and $d_{z^2}$ point **along** the axes → head-on repulsion → energy **raised**. These two are the **$e_g$** set.
- $d_{xy}$, $d_{yz}$, $d_{zx}$ point **between** the axes → less repulsion → energy **lowered**. These three are the **$t_{2g}$** set.

The gap is the **crystal field splitting energy**, $\Delta_o$.

###### High spin or low spin — the $\Delta_o$ vs P contest

**[exposure]** **Pairing energy (P)** is the energy cost of forcing a second electron into an orbital that already has one, against their mutual repulsion. It matters because the fourth d electron faces a genuine choice: pay P and pair up in the lower $t_{2g}$ set, or pay $\Delta_o$ and go alone into the upper $e_g$ set. Whichever costs less, wins.

- **$\Delta_o < P$** (weak field ligand): cheaper to jump up. Fourth electron enters $e_g$ → $t_{2g}^3e_g^1$ → more unpaired electrons → **high spin**.
- **$\Delta_o > P$** (strong field ligand): cheaper to pair. Fourth electron pairs in $t_{2g}$ → $t_{2g}^4$ → fewer unpaired → **low spin**.

###### Tetrahedral field

The geometry inverts: now $d_{xy}$, $d_{yz}$, $d_{zx}$ lie closer to the incoming ligands and are **raised** ($t_2$), while $d_{x^2-y^2}$ and $d_{z^2}$ are **lowered** ($e$).

The splitting is much smaller, because there are only four ligands instead of six and they don't point directly at any orbital:

$$\Delta_t = \frac{4}{9}\Delta_o$$

Since $\Delta_t$ is always smaller than P, **tetrahedral complexes are essentially always high spin.**

**Examiner asks:** "how is $\Delta_o$ related to $\Delta_t$?" (2024) — quote $\Delta_t = \frac{4}{9}\Delta_o$ and say why: fewer ligands, none pointing directly at an orbital.

###### Spectrochemical series

Ligands arranged by the size of $\Delta$ they produce, determined experimentally from light absorption. Weak field on the left, strong on the right:

$$\ce{I^- < Br^- < S^2- < SCN^- < Cl^- < F^- < OH^- < C2O4^2- < H2O < NH3 < en < CN^- < CO}$$

###### Colour, explained at last

An electron absorbs light of exactly the energy $\Delta_o$ and jumps from $t_{2g}$ to $e_g$ — a **d–d transition**. The compound transmits what it didn't absorb, so we see the **complementary** colour. A complex with $d^0$ or $d^{10}$ has no possible jump and is colourless.

**Examiner asks:** why does a complex lose its colour when the ligands are removed? Without ligands there is no crystal field, so no splitting, so no d–d transition — it turns colourless.

#### Stability and applications — *the short sections that still carry marks*

###### Stability constant

For $\ce{M + 4L <=> ML4}$, the stability (formation) constant is $K = \dfrac{[\ce{ML4}]}{[\ce{M}][\ce{L}]^4}$. Higher $K$ means a more stable complex. Stability rises with the metal's charge, with smaller metal size, and — strongly — with chelation.

###### Applications worth naming

- **Wilkinson's catalyst**, $\ce{[(Ph3P)3RhCl]}$ — catalyses the **hydrogenation of alkenes**.
- **Cisplatin**, cis-$\ce{[Pt(NH3)2Cl2]}$ — anti-cancer drug. Only the *cis* isomer works.
- **EDTA** — estimation of water hardness; treatment of lead poisoning.
- **Extraction of metals** — gold and silver via cyanide complexes.
- **Biological** — chlorophyll (Mg), haemoglobin (Fe), vitamin B₁₂ (Co).
- **Electroplating** and photography (silver thiosulphate complex).

#### Patterns, collected — *the four things you'll be asked to actually do*

A · IUPAC name ↔ formula — *2–3 marks*

*Recognise it: "write the IUPAC name" or "write the formula".*

1. Get the oxidation number first — it's needed either way.
2. Naming: ligands alphabetically, anionic ones in -o, prefixes ignored for alphabetising, Roman numeral, -ate if the complex is an anion.
3. Formula: metal first, then ligands alphabetically, abbreviations in parentheses.

B · Hybridisation, geometry, magnetism — *3 marks*

*Recognise it: an atomic number is given alongside a complex.*

1. Oxidation number → d-electron count.
2. Strong or weak ligand? Pair or don't.
3. Count the orbitals needed; inner 3d if free, else outer 4d.
4. State hybridisation, geometry, and paramagnetic/diamagnetic.

C · Identify the isomerism — *2–3 marks*

*Recognise it: "what type of isomerism is shown by…".*

1. Ambidentate ligand ($\ce{NO2^-}$, $\ce{SCN^-}$) present → **linkage**.
2. An ion could swap in/out of the bracket → **ionisation**.
3. Water present both inside and out → **hydrate**.
4. Two complex ions in one compound → **coordination**.
5. Otherwise check geometry: square planar or octahedral → **geometrical**; didentate ligands → check **optical** too.

D · Magnetic moment — *2 marks*

*Recognise it: "calculate the magnetic moment" or "predict the magnetic behaviour".*

1. d-count, then apply the ligand's field strength.
2. Count unpaired $n$.
3. $\mu = \sqrt{n(n+2)}$ BM.

#### Past year questions · question types — *ranked by how often they turn up*

*From the last 10 years of boards — 25 questions, grouped by pattern.*

1 · IUPAC naming / formula writing — *2–3 marks*

*Recognise it: a complex given with "name this" or a name given with "write the formula".*

1. Oxidation number.
2. Alphabetical ligands, correct endings.
3. -ate if anionic.

> **Trap:** "ammine" vs "amine", and forgetting **bis/tris** when the ligand name already has a prefix.

2 · Isomerism identification and drawing — *2–3 marks*

*Recognise it: "what type of isomerism", or "draw the isomer which is optically active".*

1. Scan for ambidentate ligands, swappable counter ions, or two complex ions.
2. If none, it's stereoisomerism — check cis/trans, then optical.
3. Optically active = **cis** with didentate ligands.

3 · Hybridisation and magnetic behaviour — *3 marks*

*Recognise it: atomic number supplied.*

1. Oxidation number → d count.
2. Ligand strength → pairing.
3. Hybridisation → geometry → magnetism.

> **Trap:** in $\ce{[Ni(CO)4]}$ nickel is in oxidation state **zero**, not $+2$.

4 · Crystal field theory reasoning — *3 marks*

*Recognise it: $\Delta_o$, $\Delta_t$, high/low spin, or "why is it coloured".*

1. Compare $\Delta_o$ with P.
2. $\Delta_o < P$ → high spin; $\Delta_o > P$ → low spin.
3. For colour, name the d–d transition.

5 · Definitions and comparisons — *2 marks*

*Recognise it: "define", "difference between", "what is denticity/chelate/ambidentate".*

1. Give the definition in NCERT's own words.
2. Add one concrete example — it's usually worth half the mark.

6 · Chemical tests and applications — *2–3 marks*

*Recognise it: "give a chemical test", or "write the formula and use of…".*

1. Ionisation isomers → $\ce{BaCl2}$ for sulphate, $\ce{AgNO3}$ for chloride.
2. Named catalysts: Wilkinson's for alkene hydrogenation.

#### Past year questions · mark slots — *what each type is worth*

| Question type | Slot | Time |
|---|---|---|
| IUPAC naming / formula | 2–3 marker | 3 min |
| Isomerism ID + drawing | 2–3 marker | 3–4 min |
| Hybridisation + magnetism | 3-marker | 4 min |
| CFT reasoning | 3-marker; full splitting diagram is a 5 | 4–6 min |
| Definitions / differences | 2-marker | 2 min |
| Chemical test / application | 2-marker | 2 min |
| Multi-part "answer the following" | 5-marker | 7 min |

*The video splits these as short-answer type I (2 marks), type II (3 marks) and long answer (5 marks) — the multi-part sets combining naming, isomerism and CFT are where the 5-markers sit.*

#### Past year questions · repeat offenders — *appeared more than once — highest probability in the chapter*

2026 Q1 · 2019 Q4 · 2023 Q2

IUPAC naming — including naming the **linkage isomer** of a red complex, and writing a formula from a given name. Naming appears in essentially every paper.

2017 Q14 · 2022 Q19 · 2026 Q5

"What type of isomerism is shown by…" — run across linkage, ionisation and coordination isomers in the same question format.

2025 Q13 · 2022 Q16

Hybridisation and magnetic behaviour of $\ce{[Ni(CO)4]}$ with $Z = 28$ supplied. The oxidation-state-zero trap is the point of it.

2024 Q24(a) · 2026 Q17

$\Delta_t = \frac{4}{9}\Delta_o$, and the $\Delta_o$ vs pairing-energy comparison deciding high vs low spin.

2019 Q25(a) · lecture PYQ

Difference between a complex and a double salt, with examples. Straight recall, always available.

2025 Q18 · 2022 Q23

Geometrical isomerism: which complexes show it, fac vs mer for $\ce{[Co(NH3)3Cl3]}$, and why tetrahedral complexes don't.

2025 Q22 · 2026 Q20

Wilkinson's catalyst formula and use, and why a complex becomes colourless when ligands are absent.

#### Past year questions · cold practice — *answers only — work them before you look*

###### Naming and formulae

- 2019 — write the formula for pentaamminenitrito-O-cobalt(III). $\ce{[Co(NH3)5(ONO)]^2+}$

- Lecture PYQ — IUPAC name of $\ce{[Cr(NH3)3Cl3]}$. triamminetrichloridochromium(III)

- Lecture PYQ — IUPAC name of $\ce{[Co(NH3)5(CO3)]Cl}$. pentaamminecarbonatocobalt(III) chloride

- Lecture PYQ — IUPAC name of $\ce{[Zn(OH)4]^2-}$. tetrahydroxidozincate(II) ion

###### Isomerism

- 2026 Q5 — isomerism in $\ce{[Co(NH3)5(NO2)]Cl2}$. Linkage — $\ce{NO2^-}$ is ambidentate

- 2017 Q14 — isomerism in $\ce{[Co(NH3)5Cl]SO4}$. Ionisation — sulphate and chloride can swap

- 2017 Q14 — isomerism in $\ce{[Co(NH3)6][Cr(CN)6]}$. Coordination — ligands exchange between the two spheres

- 2025 Q18 — draw the optically active geometrical isomer of $\ce{[Pt(en)2Cl2]^2+}$. The **cis** form; trans is optically inactive

- Lecture PYQ — which shows geometrical isomerism: $\ce{[Co(NH3)6]^3+}$ or $\ce{[Co(NH3)3Cl3]}$? The second — fac and mer. The first has all identical ligands

###### Bonding

- 2025 Q13 — hybridisation and magnetic behaviour of $\ce{[Ni(CO)4]}$, $Z = 28$. $sp^3$, tetrahedral, diamagnetic — Ni is in oxidation state 0

- Lecture PYQ — compare $\ce{[NiCl4]^2-}$ and $\ce{[Ni(CN)4]^2-}$. $sp^3$ tetrahedral paramagnetic vs $dsp^2$ square planar diamagnetic

- Lecture PYQ — why is $\ce{[CoF6]^3-}$ paramagnetic but $\ce{[Co(NH3)6]^3+}$ diamagnetic? $\ce{F^-}$ weak (no pairing, $sp^3d^2$); $\ce{NH3}$ strong with $\ce{Co^3+}$ (pairs, $d^2sp^3$)

###### CFT and applications

- 2024 Q24(a) — relate $\Delta_o$ and $\Delta_t$. $\Delta_t = \frac{4}{9}\Delta_o$ — fewer ligands, none pointing directly at an orbital

- 2026 Q17 — what does $\Delta_o < P$ mean for the complex? Weak field, high spin — the fourth electron goes to $e_g$ rather than pairing

- 2025 Q22 — formula and use of Wilkinson's catalyst. $\ce{[(Ph3P)3RhCl]}$; hydrogenation of alkenes

- 2026 Q6 — chemical test distinguishing $\ce{[Co(NH3)5SO4]Cl}$ from $\ce{[Co(NH3)5Cl]SO4}$. $\ce{AgNO3}$ → white AgCl for the first; $\ce{BaCl2}$ → white $\ce{BaSO4}$ for the second

Built from Sourabh Raina's Coordination Compounds one-shot and PYQ videos, cross-checked against NCERT Class XII Chemistry Chapter 5 (Rationalised 2022–23). Nomenclature verified against NCERT: **ammine** (two m's) for $\ce{NH3}$ versus **amine** for organic amines, and **chlorido** rather than chloro. First-contact material: every term marked **[exposure]** is explained from scratch before use.

### Chapter 6 · Haloalkanes and Haloarenes

`NCERT Class XII Chemistry · Chapter 6 · Haloalkanes and Haloarenes`

*6 marks, whole chapter 6.1–6.8, and your first organic chapter of the paper. Organic chemistry runs on a small set of ideas repeated everywhere — nucleophile, leaving group, carbocation, steric hindrance. Every one of them is tagged **[exposure]** and explained from scratch here, because once you have those four, most of this chapter answers itself.*

#### What these compounds are — *start here — one sentence defines the whole chapter*

**[exposure]** A **haloalkane** (also called an **alkyl halide**, written $\ce{R-X}$) is what you get when you take a hydrocarbon chain and replace one or more hydrogen atoms with a halogen — fluorine, chlorine, bromine or iodine. That's the entire definition. Ethane $\ce{CH3CH3}$ with one hydrogen swapped for chlorine becomes chloroethane $\ce{CH3CH2Cl}$. The defining structural feature: the carbon carrying the halogen is **$sp^3$ hybridised** — it has four single bonds, no double bond anywhere on it.

**[exposure]** A **haloarene** (or **aryl halide**, $\ce{Ar-X}$) is the same swap performed on an *aromatic* ring instead. Benzene with one hydrogen replaced by chlorine is chlorobenzene. The defining feature here: the carbon carrying the halogen is **$sp^2$ hybridised**, because it is part of the ring's double-bond system. This single difference — $sp^3$ versus $sp^2$ — is why haloalkanes and haloarenes behave almost oppositely, and it comes up in the exam again and again.

Throughout the chapter, $\ce{X}$ means any halogen and $\ce{R}$ means any alkyl group.

###### Why the chapter exists at all

Halogen-containing organic compounds are everywhere, natural and synthetic:

- **Chloramphenicol** — a chlorine-containing antibiotic made by soil microorganisms, used against typhoid.
- **Thyroxine** — the iodine-containing hormone your own thyroid produces. Too little iodine in the diet and you get **goitre**.
- **Chloroquine** — synthetic, used against malaria.
- **Halothane** — a synthetic anaesthetic used during surgery.
- **Fully fluorinated compounds** — every hydrogen replaced by fluorine. They dissolve and deliver oxygen to tissue, so they are being explored as **blood substitutes** in surgery.

**Examiner asks:** one-mark recall of a named compound and its use. Chloramphenicol/typhoid and thyroxine/goitre are the two that appear.

#### 6.1 Classification — *three separate cuts — count, hybridisation, and where the halogens sit*

###### By number of halogen atoms

**Mono**, **di** or **poly** halogen compounds, depending on whether they carry one, two, or more halogen atoms. $\ce{CH3Cl}$ is monohalo; $\ce{CH2Cl2}$ is dihalo; $\ce{CHCl3}$ is trihalo. The same labelling works on rings: one chlorine on benzene is a monohaloarene, two is a dihaloarene.

###### By hybridisation of the carbon holding the halogen

This is the classification that actually predicts behaviour, so learn these five names properly.

**Compounds with an $sp^3$ C–X bond:**

**[exposure]** **Alkyl halides** — the halogen sits on an ordinary $sp^3$ carbon of a chain. They are sub-classified by *what else* that carbon is attached to: if the carbon carries one other carbon it is **primary (1°)**, two others **secondary (2°)**, three others **tertiary (3°)**. This count matters more than anything else in the chapter — it decides which mechanism the compound follows and how fast. $\ce{CH3CH2Cl}$ is primary; $\ce{(CH3)2CHCl}$ is secondary; $\ce{(CH3)3CCl}$ is tertiary.

**[exposure]** An **allylic halide** has the halogen on an $sp^3$ carbon that sits *next to* a carbon–carbon double bond. The word exists because that neighbouring double bond changes everything: when the halogen leaves, the positive charge left behind can spread into the double bond by resonance, so allylic halides react far faster than ordinary ones. Example: $\ce{CH2=CH-CH2-Cl}$ — the chlorine-bearing carbon has four single bonds, the carbon beside it has the double bond.

**[exposure]** A **benzylic halide** is the same idea with a benzene ring instead of a double bond: the halogen is on an $sp^3$ carbon directly attached to an aromatic ring. $\ce{C6H5CH2Cl}$ (benzyl chloride) is the standard one. Benzylic halides are the *most* reactive of all in this respect, because the ring gives the intermediate the largest resonance stabilisation available. These too can be 1°, 2° or 3° by the same counting rule.

**Compounds with an $sp^2$ C–X bond:**

**[exposure]** A **vinylic halide** has the halogen bonded *directly to* a carbon of a carbon–carbon double bond. Not next to it — on it. $\ce{CH2=CH-Cl}$ is vinyl chloride. Because that carbon is $sp^2$, the C–X bond is shorter and stronger, and these are very unreactive towards substitution.

**[exposure]** An **aryl halide** has the halogen bonded directly to an $sp^2$ carbon of an aromatic ring — chlorobenzene. Same story as vinylic, for the same reason plus resonance.

> **Trap:** allylic/benzylic (fast) versus vinylic/aryl (slow) is decided by *one* question — is the halogen **on** the unsaturated carbon, or **next to** it? On it → $sp^2$ → unreactive. Next to it → $sp^3$ → very reactive. This exact discrimination appeared as 2017 Q5(b).

###### Dihaloalkanes: where the two halogens sit

**[exposure]** **Geminal (gem) dihalides** carry both halogens on the *same* carbon — from Latin *geminus*, twin. $\ce{CH3CHCl2}$ is one. Their common name is built from the alkylidene group: $\ce{CH3CHCl2}$ is **ethylidene chloride**.

**[exposure]** **Vicinal (vic) dihalides** carry the halogens on *adjacent* carbons — from Latin *vicinus*, neighbour. $\ce{CH2ClCH2Cl}$ is one. Their common name uses the alkylene group: **ethylene dichloride**. Vicinal dihalides matter because that's what you get when bromine adds across a double bond.

**Examiner asks:** "write the structures of all dihalogen derivatives of propane" (NCERT intext 6.3) — there are four: 1,1- and 2,2- (both geminal), 1,2- (vicinal), and 1,3-.

#### 6.2 Nomenclature — *IUPAC and common names — both are examinable*

###### IUPAC rules, in the order you apply them

1. Find the **longest carbon chain** containing the principal functional group. Count carbons only — hydrogens don't matter.
2. The halogen is a **substituent**, named as a prefix: **fluoro-, chloro-, bromo-, iodo-**.
3. If there is a **double or triple bond, it takes priority** for the lowest number, not the halogen.
4. With no multiple bond, number so the **substituent** gets the lowest locant.
5. If numbering from both ends gives the same set of numbers, give the lowest number to whichever substituent comes **first alphabetically**. Bromo beats methyl; chloro beats methyl.
6. Write substituents alphabetically in the name.

| Structure | IUPAC name | Common name |
|---|---|---|
| $\ce{CH3CH2CH2Br}$ | 1-bromopropane | *n*-propyl bromide |
| $\ce{(CH3)2CHCl}$ | 2-chloropropane | isopropyl chloride |
| $\ce{CH3CH2CHClCH3}$ | 2-chlorobutane | *sec*-butyl chloride |
| $\ce{(CH3)3CBr}$ | 2-bromo-2-methylpropane | *tert*-butyl bromide |
| $\ce{(CH3)2CHCH2Br}$ | 1-bromo-2-methylpropane | isobutyl bromide |
| $\ce{CH3CH2CH2CH2Cl}$ | 1-chlorobutane | *n*-butyl chloride |

The straight-chain compound always takes ***n*-** in the common name. A three-carbon group halogenated at the middle carbon is **isopropyl**. Four carbons branched at the end is **isobutyl**; branched at the halogen-bearing carbon is *sec*- or *tert*-butyl depending on the count.

###### Common names you're expected to know cold

| Formula | IUPAC | Common |
|---|---|---|
| $\ce{CHCl3}$ | trichloromethane | chloroform |
| $\ce{CHBr3}$ | tribromomethane | bromoform |
| $\ce{CHI3}$ | triiodomethane | iodoform |
| $\ce{CCl4}$ | tetrachloromethane | carbon tetrachloride |
| $\ce{CH2Cl2}$ | dichloromethane | methylene chloride |

###### Aromatic compounds

For haloarenes the common name and the IUPAC name are the same word — chlorobenzene is both. Three side-chain names you must recognise:

- **Benzyl** — benzene ring plus $\ce{CH2}$. So $\ce{C6H5CH2Cl}$ is benzyl chloride.
- **Benzal** — ring plus $\ce{CH}$ carrying two halogens. $\ce{C6H5CHCl2}$ is benzal dichloride.
- **Benzo-** — ring plus a carbon with no hydrogen left. $\ce{C6H5CCl3}$ is benzotrichloride.

For two substituents on a ring, positions 1,2 are **ortho (o-)**, 1,3 are **meta (m-)**, 1,4 are **para (p-)**. So 1,4-dibromobenzene is *p*-dibromobenzene. Three substituents at 1,3,5 is **sym-** (symmetrical).

**Examiner asks:** "give the IUPAC name of the following" is a standing 3-marker (2017 Q14, 2024 Q11a). Always check for a double bond before you number.

#### 6.3 Nature of the C–X bond — *short section, but it explains every reaction that follows*

Halogens are more electronegative than carbon, so the shared electron pair sits closer to the halogen. The result is a **polar bond**: the carbon carries a partial positive charge $\delta+$ and the halogen a partial negative charge $\delta-$.

$$\overset{\delta+}{\ce{C}} - \overset{\delta-}{\ce{X}}$$

That $\delta+$ carbon is the target of essentially every reaction in this chapter. Anything electron-rich will go for it.

Down the group F → Cl → Br → I, the halogen gets bigger, so the **bond length increases** and the **bond enthalpy decreases**. A longer, weaker bond breaks more easily — which is why **$\ce{R-I}$ is the most reactive alkyl halide and $\ce{R-F}$ the least** in substitution reactions. Under ordinary conditions $\ce{R-F}$ barely reacts at all.

> **Trap:** the C–Cl bond in a **haloalkane is 177 pm**, but in a **haloarene only 169 pm** — shorter, therefore stronger, therefore harder to break. That number is the physical reason haloarenes resist nucleophilic substitution, and it is worth quoting.

#### 6.4 Preparation of haloalkanes — *four routes — from alcohols, from alkanes, from alkenes, by exchange*

###### A · From alcohols

The general move: replace the $\ce{-OH}$ group with a halogen.

**(i) With halogen acids ($\ce{HX}$)**

$$\ce{R-OH + H-X -> R-X + H2O}$$

For **chloroalkanes**, use $\ce{HCl}$ with **anhydrous $\ce{ZnCl2}$** as catalyst:

$$\ce{CH3CH2OH + HCl ->[\text{anhyd. } ZnCl2] CH3CH2Cl + H2O}$$

The $\ce{ZnCl2}$ works as a **dehydrating agent**: it soaks up the water product. By Le Chatelier's principle, removing a product drives the equilibrium forward, so you get more chloroethane.

For **bromoalkanes**, heat the alcohol with $\ce{NaBr}$ (or $\ce{KBr}$) and concentrated $\ce{H2SO4}$:

$$\ce{R-OH + NaBr + H2SO4 -> R-Br + NaHSO4 + H2O}$$

**[exposure]** The $\ce{HBr}$ is generated **in situ** — Latin for "in place", meaning the reagent is made inside the reaction vessel at the moment it's needed rather than being bought and stored. Chemists do this whenever a reagent is nasty or unstable to keep around. $\ce{HBr}$ is a corrosive acid that gives off heavy fumes, so making it in the flask from $\ce{NaBr + H2SO4}$ is simply safer. You can also just use 48% concentrated $\ce{HBr}$ directly.

For **iodoalkanes**, use $\ce{NaI}$ (or $\ce{KI}$) with **95% phosphoric acid, $\ce{H3PO4}$** — *not* sulphuric acid:

$$\ce{R-OH + NaI + H3PO4 -> R-I + NaH2PO4 + H2O}$$

> **Trap — this is NCERT intext 6.2 and it appears in boards:** why not $\ce{H2SO4}$ with $\ce{KI}$? Concentrated $\ce{H2SO4}$ *would* make $\ce{HI}$, but it is also a **strong oxidising agent** and immediately oxidises that $\ce{HI}$ to $\ce{I2}$. The $\ce{HI}$ never survives to reach the alcohol. $\ce{H3PO4}$ is not an oxidising agent, so it works.

**Reactivity orders to memorise** — halogen acid: $\ce{HI > HBr > HCl}$ (because $\ce{HI}$ has the longest, weakest bond, so it ionises most easily). Alcohol: **tertiary > secondary > primary** (because these reactions go through a carbocation, and a tertiary carbocation is the most stable).

**(ii) With phosphorus halides**

$$\ce{CH3CH2OH + PCl5 -> CH3CH2Cl + POCl3 + HCl}$$

$$\ce{3CH3CH2OH + PCl3 -> 3CH3CH2Cl + H3PO3}$$

For bromides and iodides, use **red phosphorus with $\ce{Br2}$ or $\ce{I2}$**. The $\ce{PBr3}$ or $\ce{PI3}$ is generated in situ, again because these are too unstable to store:

$$\ce{3R-OH + P + 3/2 Br2 -> 3R-Br + H3PO3}$$

**(iii) With thionyl chloride — the preferred method**

$$\ce{CH3CH2OH + SOCl2 -> CH3CH2Cl + SO2 ^ + HCl ^}$$

**Examiner asks:** "why is thionyl chloride preferred for preparing alkyl chlorides from alcohols?" (2024 Q11b) — because both by-products, $\ce{SO2}$ and $\ce{HCl}$, are **gases that escape**, leaving pure alkyl chloride behind with no separation step. Say "escapable gases, hence pure product" and you have the mark.

> **Trap:** **none of these routes work on phenol.** In phenol, the oxygen's lone pair delocalises into the ring, giving the C–O bond **partial double-bond character**. It's too strong to break, so you cannot make an aryl halide from phenol this way. This is a stock 2-marker and it also shows up embedded in "major monohalo product" questions where a molecule has two $\ce{-OH}$ groups: only the non-phenolic one reacts.

###### B · From hydrocarbons — free radical halogenation

Treat an alkane with $\ce{Cl2}$ or $\ce{Br2}$ in the presence of UV light or heat, and hydrogens get replaced one at a time:

$$\ce{CH3CH2CH2CH3 + Cl2 ->[hv] CH3CH2CH2CH2Cl + CH3CH2CHClCH3 + \text{(polyhalo products)}}$$

The problem: you get a **complex mixture** of isomeric mono- and polyhalogenated products whose boiling points are so close they are almost impossible to separate. So this is **not a preferred preparative method** — but it is heavily examined for *predicting* products.

When asked for the **major** free-radical product, use the free-radical stability order: **benzylic ≈ allylic > tertiary > secondary > primary**. Benzylic and allylic radicals win because the ring or double bond stabilises them by resonance.

###### C · From alkenes

**(i) Addition of a halogen acid**

With a **symmetrical** alkene, there's no choice to make:

$$\ce{CH2=CH2 + HBr -> CH3CH2Br}$$

**[exposure]** With an **unsymmetrical** alkene the two carbons of the double bond are different, so you need a rule to say which end the halogen goes to. **Markovnikov's rule** says the **negative part of the adding molecule attaches to the carbon that carries fewer hydrogens**. The reason underneath is carbocation stability — the proton adds first, wherever it produces the more stable carbocation, and the halide then goes to that carbon. So propene plus $\ce{HBr}$ gives 2-bromopropane, not 1-bromopropane.

$$\ce{CH3CH=CH2 + HBr -> CH3CHBrCH3}$$

**Anti-Markovnikov (peroxide / Kharasch effect):** add a peroxide such as benzoyl peroxide and the rule flips — bromine goes to the carbon with *more* hydrogens.

$$\ce{CH3CH=CH2 + HBr ->[\text{peroxide}] CH3CH2CH2Br}$$

> **Trap:** the peroxide effect works with **$\ce{HBr}$ only**. It does not happen with $\ce{HCl}$ or $\ce{HI}$. If a question gives you peroxide with $\ce{HCl}$, the answer is still Markovnikov.

**(ii) Addition of a halogen**

$$\ce{CH2=CH2 + Br2 ->[CCl4] CH2BrCH2Br}$$

This gives a **vicinal dibromide**. The reddish-brown colour of the bromine solution **discharges** as the reaction proceeds — which is exactly the standard laboratory **test for unsaturation**.

###### D · Halogen exchange

**[exposure]** The **Finkelstein reaction** makes alkyl *iodides* by swapping out a chloride or bromide, using $\ce{NaI}$ in **dry acetone**. It needs a named trick because the swap is an equilibrium that wouldn't otherwise favour the product. The trick: $\ce{NaCl}$ and $\ce{NaBr}$ are **insoluble in dry acetone and precipitate out**, while $\ce{NaI}$ is soluble. Removing a product drags the equilibrium forward (Le Chatelier again).

$$\ce{R-X + NaI ->[\text{dry acetone}] R-I + NaX v} \qquad \ce{X = Cl, Br}$$

**[exposure]** The **Swarts reaction** makes alkyl *fluorides*, which the ordinary routes can't touch. Heat an alkyl chloride or bromide with a **metallic fluoride** — $\ce{AgF}$, $\ce{Hg2F2}$, $\ce{CoF2}$ or $\ce{SbF3}$:

$$\ce{CH3Br + AgF -> CH3F + AgBr}$$

**Examiner asks:** "what happens when methyl bromide is treated with silver fluoride?" (2025 Q20a) — name it as Swarts and give the equation.

#### 6.5 Preparation of haloarenes — *two routes — and one of them is a named reaction you must know*

###### A · From arenes, by electrophilic substitution

Treat benzene with $\ce{Cl2}$ or $\ce{Br2}$ in the presence of a **Lewis acid catalyst** — $\ce{FeCl3}$, $\ce{FeBr3}$ or iron filings — in the dark:

$$\ce{C6H6 + Cl2 ->[FeCl3][\text{dark}] C6H5Cl + HCl}$$

Mechanically: the Lewis acid is electron-deficient, so it pulls $\ce{Cl^-}$ off $\ce{Cl2}$, leaving $\ce{Cl+}$. That $\ce{Cl+}$ is the **electrophile** that attacks the electron-rich ring.

With **toluene**, the $\ce{-CH3}$ group is ortho/para directing, so you get a mixture of *o*- and *p*-chlorotoluene. Conveniently, these two are **easy to separate** because their melting points differ widely.

Two limits on this method:

- **Fluoro compounds can't be made this way** — fluorine is too reactive and the reaction is uncontrollable.
- **Iodination is reversible** and gives poor yield. Fix it by adding an **oxidising agent** ($\ce{HNO3}$ or $\ce{HIO4}$), which oxidises the $\ce{HI}$ by-product to $\ce{I2}$ and so pulls the equilibrium forward.

###### B · From amines — the Sandmeyer reaction

**[exposure]** A **diazonium salt** is an aromatic compound carrying the group $\ce{-N2+}$ — a nitrogen pair on its way out. It exists as an intermediate because that group is an *outstanding* leaving group: it departs as harmless $\ce{N2}$ gas, dragging the reaction forward. That makes it the standard way to put almost anything onto a benzene ring. Diazonium salts are only stable cold, which is why the next step specifies 0–5 °C.

**Step 1 — diazotisation.** Treat a primary aromatic amine (aniline) with nitrous acid, generated in situ from $\ce{NaNO2 + HCl}$, at **273–278 K (0–5 °C)**:

$$\ce{C6H5NH2 + NaNO2 + 2HCl ->[273-278 K] C6H5N2+Cl- + NaCl + 2H2O}$$

**Step 2 — Sandmeyer.** Treat the diazonium salt with a **cuprous halide**:

$$\ce{C6H5N2+Cl- ->[Cu2Cl2 / HCl] C6H5Cl + N2}$$

$$\ce{C6H5N2+Cl- ->[Cu2Br2 / HBr] C6H5Br + N2}$$

> **Trap:** for the **iodo** compound you need **no copper salt at all** — simply shaking the diazonium salt with $\ce{KI}$ does it. This exception is asked directly.

$$\ce{C6H5N2+Cl- + KI -> C6H5I + KCl + N2}$$

#### 6.6 Physical properties — *every point here is a "give the reason" question*

###### Physical state and colour

$\ce{CH3Cl}$, $\ce{CH3Br}$, $\ce{CH3CH2Cl}$ and some chlorofluoromethanes are **gases** at room temperature; higher members are liquids or solids. Pure haloalkanes are **colourless**, but bromo- and iodo- compounds develop colour on standing in light.

###### Boiling point — four separate rules

1. **$\ce{RF < RCl < RBr < RI}$.** Down the group the halogen's mass and size increase, so the **van der Waals forces** between molecules get stronger and more energy is needed to separate them.
2. **A haloalkane always boils higher than the hydrocarbon of comparable mass.** Two reasons together: the C–X bond is polar, so molecules attract each other by **dipole–dipole interaction**; and the heavy halogen raises the molecular mass, strengthening van der Waals forces.
3. **Among isomers, boiling point falls as branching rises.** Branching makes a molecule more compact and spherical, cutting the **surface area of contact** between molecules, which weakens van der Waals forces.
4. **More halogen atoms → higher boiling point**, again through mass. $\ce{CH3Cl < CH3Br < CH2Br2 < CHBr3}$.

**Worked:** Arrange in increasing boiling point: 1-chloropropane, 2-chloropropane, 1-chlorobutane.
1-chlorobutane has four carbons — highest mass, so it boils highest. The other two are isomers, so compare branching: 2-chloropropane is branched, so it boils lowest. Answer: **2-chloropropane < 1-chloropropane < 1-chlorobutane**.

###### Melting point — the para exception

The boiling points of *o*-, *m*- and *p*-dihalobenzenes are nearly identical. But the **para isomer melts much higher** than the other two, because it is more **symmetrical** and so packs more tightly into the crystal lattice. More energy is needed to break a well-packed lattice apart.

###### Density

Bromo, iodo and polychloro derivatives are **heavier than water**. Density increases with the number of carbon atoms, the number of halogen atoms, and the atomic mass of the halogen.

###### Solubility — a favourite "give the reason"

Haloalkanes are polar, yet they are **insoluble in water**. Dissolving anything in water requires breaking the strong **hydrogen bonds between water molecules** and also the dipole–dipole attractions between haloalkane molecules. The energy released when new haloalkane–water attractions form is **less** than the energy needed to break the old ones — so it doesn't happen.

They *are* soluble in organic solvents (alcohol, ether, benzene), because there the new attractions formed are about as strong as the ones broken, so the books balance.

**Examiner asks:** "why are alkyl halides, though polar, immiscible with water?" (2017 Q5a) — the two energies, in one sentence each. It is a repeat question.

#### 6.7 Reactions of haloalkanes — nucleophilic substitution — *the core of the chapter; get the two words first*

**[exposure]** A **nucleophile** is a species that is **electron-rich** — it has a lone pair or a negative charge — and goes looking for a positive centre to donate that pair to. The name means "nucleus-loving". $\ce{OH-}$, $\ce{CN-}$, $\ce{NH3}$ and $\ce{RO-}$ are all nucleophiles. In this chapter the positive centre it attacks is always the $\delta+$ carbon of the C–X bond.

**[exposure]** A **leaving group** is the species that departs, taking the bonding electron pair with it. Here it's the halide ion $\ce{X-}$. A group leaves easily when the resulting ion is stable and the bond was weak — so **$\ce{I-}$ is the best leaving group and $\ce{F-}$ the worst**, following bond strength. That single fact explains the reactivity order $\ce{RI > RBr > RCl > RF}$.

Put those together and the reaction reads: a nucleophile attacks the $\delta+$ carbon, the halide leaves, and you have a new compound. The substitution only happens if the incoming nucleophile is **stronger than the halide it displaces**.

$$\ce{Nu^- + R-X -> R-Nu + X^-}$$

###### The substitution products you must be able to write

| Reagent | Product | Class of product |
|---|---|---|
| aqueous $\ce{KOH}$ / $\ce{NaOH}$ | $\ce{R-OH}$ | alcohol |
| $\ce{NaOR}$ (sodium alkoxide) | $\ce{R-O-R}$ | ether |
| $\ce{KCN}$ | $\ce{R-CN}$ | alkyl cyanide (nitrile) |
| $\ce{AgCN}$ | $\ce{R-NC}$ | alkyl **iso**cyanide |
| $\ce{NH3}$ | $\ce{R-NH2}$ | primary amine |
| $\ce{KNO2}$ | $\ce{R-O-N=O}$ | alkyl nitrite |
| $\ce{AgNO2}$ | $\ce{R-NO2}$ | **nitro**alkane |
| $\ce{R'COOAg}$ (silver carboxylate) | $\ce{R'COOR}$ | ester |
| $\ce{LiAlH4}$ | $\ce{R-H}$ | alkane (same carbon count) |
| $\ce{R'-Li}$ (or Na) | $\ce{R-R'}$ | alkane (carbons added) |

**[exposure]** Look at the four pairs above that come in twos. An **ambident nucleophile** is a nucleophile with **two different donor atoms**, either of which can do the attacking — though only one at a time. The category exists because *which* atom attacks decides which product you get, and that in turn depends on whether the reagent is ionic or covalent. The two examples are $\ce{CN-}$ (attacks through C or N) and $\ce{NO2-}$ (attacks through N or O).

> **Trap — and one of the most-asked questions in the chapter:** $\ce{KCN}$ is **ionic**, so it dissociates and gives a free $\ce{CN-}$ ion which attacks through its **carbon** → alkyl **cyanide**. $\ce{AgCN}$ is **covalent**, so it does not dissociate; only the **nitrogen** lone pair is available → alkyl **isocyanide**. The same logic runs the $\ce{KNO2}$ / $\ce{AgNO2}$ pair: ionic gives attack through oxygen (nitrite ester), covalent gives attack through nitrogen (nitroalkane). Remember it as **"silver goes through nitrogen"**.

###### Mechanism 1 · $S_N2$ — bimolecular

**[exposure]** **$S_N2$** stands for **Substitution, Nucleophilic, bimolecular**. "Bimolecular" means **two** species are involved in the slow, rate-deciding step, so the rate depends on the concentration of *both*:

$$\text{Rate} = k\,[\ce{R-X}][\ce{Nu^-}]$$

Everything happens in **one single step**. The nucleophile attacks the carbon from the side **opposite** the halogen — it has to, because the halogen's lone pairs would repel it if it came from the front. As the new C–Nu bond forms, the old C–X bond breaks, **simultaneously**.

**[exposure]** Halfway through, the carbon is momentarily bonded to **five** things at once — the three groups it keeps, the incoming nucleophile, and the leaving halogen. That arrangement is the **transition state**. It is not an intermediate: it is a fleeting, very high-energy structure that **cannot be isolated**, existing only at the top of the energy hill. In $S_N2$ there is **no intermediate at all** — no carbocation, no free radical.

Because the nucleophile comes in from the back and the halogen leaves the front, the other three groups get pushed through, like an umbrella flipping in the wind. The result is **inversion of configuration**, called Walden inversion.

**Worked:** $\ce{(-)}$-2-bromooctane treated with $\ce{OH-}$ gives $\ce{(+)}$-octan-2-ol. The $\ce{OH}$ ends up in the position the $\ce{Br}$ did not occupy — the configuration is inverted, and the sign of optical rotation flips.

**[exposure]** **Steric hindrance** is physical crowding: bulky groups around the reaction centre get in the way of an incoming reagent and slow the reaction down. It matters here because the $S_N2$ nucleophile must physically reach the carbon. A methyl halide has only three small hydrogens in the way, so it reacts fastest. A tertiary halide has three fat $\ce{CH3}$ groups blocking the approach, so it reacts slowest.

**$S_N2$ reactivity: $\ce{CH3X}$ > primary > secondary > tertiary.**

> **Trap:** when both compounds in a pair are primary, compare **how close the branching is to the halogen**. A methyl group nearer the C–X carbon crowds it more and slows $S_N2$ further. That comparison is NCERT intext 6.7 and appears in boards.

###### Mechanism 2 · $S_N1$ — unimolecular

**[exposure]** **$S_N1$** is **Substitution, Nucleophilic, unimolecular**. "Unimolecular" means only **one** species appears in the slow step — the alkyl halide. So the rate depends only on *its* concentration; changing the nucleophile's concentration does nothing at all:

$$\text{Rate} = k\,[\ce{R-X}]$$

It runs in **two steps**, and it requires a **polar protic solvent** — polar (it has $\delta+/\delta-$ ends) and protic (it contains an O–H or N–H that can hand out protons). Water, alcohols and acetic acid all qualify.

**[exposure]** A **carbocation** is a carbon atom bearing a **full positive charge**, left behind when a leaving group departs with both bonding electrons. It has only three bonds, so it is $sp^2$ hybridised and **flat (planar)**. Being electron-deficient it is very unstable and short-lived — but its stability varies enormously, and that variation drives this whole mechanism. **Tertiary > secondary > primary > methyl**, because the surrounding alkyl groups push electron density in and cushion the positive charge. Benzylic and allylic carbocations beat all of these, because resonance spreads the charge over several atoms.

**Step 1 (slow, reversible — the rate-determining step):**

$$\ce{(CH3)3C-Br ->[\text{slow}] (CH3)3C+ + Br^-}$$

Breaking that C–Br bond costs energy. The energy comes from **solvation**: the protic solvent's $\delta+$ hydrogens crowd around the departing $\ce{Br-}$, stabilise it, and release energy in doing so. That is exactly why a polar protic solvent is required.

**Step 2 (fast):** the nucleophile attacks the carbocation.

$$\ce{(CH3)3C+ + OH^- ->[\text{fast}] (CH3)3C-OH}$$

**$S_N1$ reactivity: tertiary > secondary > primary** — the exact opposite of $S_N2$, and for a completely different reason (carbocation stability, not crowding).

> **Trap:** for allylic and benzylic halides, **both** mechanisms are fast — $S_N1$ because their carbocations are resonance-stabilised, $S_N2$ because the carbon is usually primary and uncrowded. Don't let "it's primary" push you to the wrong answer on an $S_N1$ question about benzyl chloride: benzyl chloride is the *faster* $S_N1$ substrate against cyclohexyl chloride, because the benzyl carbocation is resonance-stabilised.

###### $S_N1$ vs $S_N2$ — the comparison table

|  | $S_N1$ | $S_N2$ |
|---|---|---|
| Order of reaction | first order | second order |
| Rate depends on | $[\ce{RX}]$ only | $[\ce{RX}]$ and $[\ce{Nu}]$ |
| Steps | two | one |
| Goes through | carbocation intermediate | transition state, no intermediate |
| Stereochemistry | **racemisation** | **inversion** |
| Favoured by | 3° > 2° > 1° | 1° > 2° > 3° |
| Solvent | polar protic | polar aprotic |

**Examiner asks:** "write two differences between $S_N1$ and $S_N2$" (2021 Q21) — pick order + steps, or intermediate + stereochemistry. Two rows, two marks.

#### Optical isomerism — *the stereochemistry vocabulary — six terms, each needed for the $S_N$ answers*

**[exposure]** **Optical activity** is a property some substances have of **rotating the plane of plane-polarised light**. Ordinary light vibrates in every direction; pass it through a polariser and it vibrates in one plane only. Send that through certain liquids or solutions and the plane comes out twisted by some angle. Substances that do this are **optically active**; those that don't are optically inactive. The angle is measured with an instrument called a **polarimeter**.

A substance rotating the plane **clockwise (right)** is **dextrorotatory**, written **d** or **(+)**. One rotating it **anticlockwise (left)** is **laevorotatory**, written **l** or **(–)**.

**[exposure]** A **chiral carbon** (also called an asymmetric carbon or stereocentre) is an $sp^3$ carbon attached to **four different atoms or groups**. It is marked with an asterisk. It matters because it is the structural cause of optical activity — with four different groups the molecule has no plane of symmetry, and that asymmetry is what twists the light. In $\ce{CH3CH(Br)CH2CH3}$ the second carbon holds methyl, ethyl, bromine and hydrogen: four different things, so it is chiral.

**[exposure]** A **chiral molecule** has no plane of symmetry, and so is **non-superimposable on its mirror image** — exactly like your left and right hands, which is where the name comes from (Greek *cheir*, hand). Lay one over the other and they never match. A molecule with a chiral carbon is normally chiral, and chiral molecules are optically active.

**[exposure]** **Enantiomers** are the two mirror-image forms of a chiral molecule. They are stereoisomers — same connections, different spatial arrangement. They rotate plane-polarised light by the **same angle in opposite directions**: if one is dextro, the other is laevo. Every other physical property — melting point, boiling point, solubility, refractive index — is **identical**.

**Examiner asks:** "why are the d- and l-isomers of butan-2-ol difficult to separate by fractional distillation?" (2024 Q22) — because fractional distillation separates on boiling point, and enantiomers have **identical** boiling points. One line, full marks.

**[exposure]** A **racemic mixture** is a **1:1 (equimolar)** mixture of the two enantiomers. It is **optically inactive**, because the rotation produced by one is exactly cancelled by the other. It's written **dl** or **(±)**, as in (±)-butan-2-ol. The process of converting a single enantiomer into such a mixture is **racemisation**.

**[exposure]** Three words for what a substitution does to a chiral centre. **Retention** — the new group takes the same spatial position the old one had; the configuration is unchanged. **Inversion** — the new group takes the position *opposite*; the configuration is flipped. **Racemisation** — you get roughly 50% of each, so the product is optically inactive.

**Which mechanism gives which:**

- **$S_N2$ → inversion.** The nucleophile can only attack from the back, so there is only one possible outcome.
- **$S_N1$ → racemisation.** The carbocation intermediate is **planar**, so the nucleophile can attack from either face with equal ease. Two products form in equal amounts, they are enantiomers, and the mixture is racemic.

**Examiner asks:** "out of $S_N1$ and $S_N2$, which occurs with inversion and which with racemisation?" (2026 Q23c) — and expect to have to *explain* it: back-side attack for one, planar carbocation for the other.

#### Elimination and reactions with metals — *the other two things a haloalkane does*

###### Elimination — dehydrohalogenation

**[exposure]** **Dehydrohalogenation** means removing $\ce{H}$ and $\ce{X}$ from adjacent carbons to make a double bond. It is also called **β-elimination**, because of where the two pieces come from: the carbon bearing the halogen is the **α-carbon**, the one next to it is the **β-carbon**, and the reaction takes the halogen from α and a hydrogen from β. The reagent is **alcoholic KOH** — and the "alcoholic" is the whole point, because aqueous KOH gives substitution instead.

$$\ce{CH3CH2Br ->[\text{alc. } KOH] CH2=CH2 + KBr + H2O}$$

> **Trap — the single most reliable trick in the chapter:** **aqueous KOH → alcohol (substitution). Alcoholic KOH → alkene (elimination).** One word in the question decides the whole answer, and it is tested constantly.

**[exposure]** When a molecule has **more than one β-hydrogen**, more than one alkene can form, and **Saytzeff's rule** (NCERT spells it **Zaitsev**, "also pronounced as Saytzeff") tells you which one dominates: the **more substituted alkene** — the one whose double-bonded carbons carry the most alkyl groups — is the major product. It exists as a rule because more-substituted alkenes are more stable, and the reaction settles into the more stable product.

**Worked:** 2-bromopentane with alcoholic KOH. There are β-hydrogens on both sides, so two alkenes are possible. Removing one gives pent-1-ene, the other gives pent-2-ene. Pent-2-ene has an alkyl group on *each* double-bonded carbon, pent-1-ene has only one — so **pent-2-ene is major, 81% against 19%**.

###### Reaction with metals

**[exposure]** An **organometallic compound** is any compound containing a direct **carbon–metal bond**. They matter because the metal, being electropositive, pushes electron density onto the carbon, giving that carbon a $\delta-$ charge — the exact reverse of its usual state. A carbon that is normally attacked becomes a carbon that attacks.

**[exposure]** The **Grignard reagent**, $\ce{R-Mg-X}$ (alkyl magnesium halide), is the most important organometallic compound in the syllabus. Make it by reacting a haloalkane with **magnesium metal in dry ether**:

$$\ce{CH3CH2Br + Mg ->[\text{dry ether}] CH3CH2MgBr}$$

The C–Mg bond is covalent but **highly polar**: carbon $\delta-$, magnesium $\delta+$. That $\delta-$ carbon is so electron-rich that it grabs a proton from **any** source — water, alcohol, an amine — and turns into an alkane:

$$\ce{R-MgX + H2O -> R-H + Mg(OH)X}$$

**Examiner asks:** "why should Grignard reagents be prepared under anhydrous conditions?" (2024 Q13c) — because they react instantly with any water present to give the alkane, destroying the reagent before it can be used. Repeat question; know it verbatim.

**[exposure]** The **Wurtz reaction** joins two alkyl halides end to end using **sodium in dry ether**, producing an alkane with **double the carbon count**. It exists as a named reaction because it's the standard way to build a longer chain, and because it's the only route that *doubles* — which is what lets you work backwards from the product in exam questions.

$$\ce{2R-X + 2Na ->[\text{dry ether}] R-R + 2NaX}$$

> **Trap:** Wurtz only gives a clean product with a **symmetrical** alkane. So when a question gives you the product and asks for the starting halide, **cut the product exactly in half** and put $\ce{X}$ on the cut. 2,5-dimethylhexane cuts into two 1-bromo-2-methylpropane molecules. That reverse-engineering step is asked repeatedly (2026 Q10b).

#### Reactions of haloarenes — *why they behave backwards, and the two named ring reactions*

###### Why haloarenes resist nucleophilic substitution

This is a guaranteed question. There are four reasons; two or three earn full marks.

1. **Resonance.** The halogen's lone pair delocalises into the ring, so the C–X bond acquires **partial double-bond character**. A partial double bond is far harder to break than a single one.
2. **$sp^2$ hybridisation.** The carbon holding the halogen is $sp^2$, so it has more **s-character** and is more electronegative than an $sp^3$ carbon. It holds the bonding pair more tightly. The bond is also shorter — 169 pm against 177 pm in a haloalkane.
3. **Instability of the phenyl cation.** An $S_N1$ route would need a phenyl carbocation, which gets no resonance stabilisation and is therefore not formed.
4. **Electronic repulsion.** The ring's π-electron cloud repels an approaching nucleophile.

###### The nitro group changes everything

Put a **strongly electron-withdrawing group** such as $\ce{-NO2}$ at the **ortho or para** position and the picture flips. The nitro group pulls electron density away, weakening the C–X bond and activating the ring towards nucleophilic attack. Each extra nitro group makes it easier:

| Compound | Conditions needed |
|---|---|
| chlorobenzene | $\ce{NaOH}$, 623 K, 300 atm |
| *p*-nitrochlorobenzene | $\ce{NaOH}$, 443 K, then acidify |
| 2,4-dinitrochlorobenzene | $\ce{NaOH}$, 368 K, then acidify |
| 2,4,6-trinitrochlorobenzene | warm water alone → **picric acid** |

> **Trap:** a nitro group at the **meta** position has **no effect at all**. Resonance only pushes and pulls electron density at the ortho and para positions — meta is never in the delocalisation path. Stating this earns a mark on its own.

###### Electrophilic substitution — the halogen's split personality

Halogens are **ortho/para directing but deactivating**. Both halves of that need explaining:

- **Ortho/para directing** because the halogen's lone pair delocalises *into* the ring (**+R effect**), and resonance raises the electron density specifically at the ortho and para positions. An incoming electrophile goes where the electrons are.
- **Deactivating** because the halogen is also strongly electronegative and pulls electron density *out* along the sigma bond (**–I effect**). Overall the ring ends up poorer in electrons than plain benzene, so the reaction is slower and needs harsher conditions.

**Examiner asks:** "although chlorine shows a strong –I effect, why is it ortho/para directing?" (2026 Q25a) — answer with the two effects working in opposite directions: –I decides *how fast*, +R decides *where*.

The four standard electrophilic substitutions on chlorobenzene, all giving ortho + para with **para as the major product** (it's more symmetrical, and less crowded than ortho):

- **Halogenation** — $\ce{Cl2}$, anhydrous $\ce{FeCl3}$ → 1,2- and 1,4-dichlorobenzene.
- **Nitration** — conc. $\ce{HNO3}$ + conc. $\ce{H2SO4}$ → 1-chloro-2-nitrobenzene and 1-chloro-4-nitrobenzene.
- **Sulphonation** — conc. $\ce{H2SO4}$, heat → 2- and 4-chlorobenzenesulphonic acid.
- **Friedel–Crafts**, anhydrous $\ce{AlCl3}$ — **alkylation** with $\ce{CH3Cl}$ gives 1-chloro-2/4-methylbenzene; **acylation** with $\ce{CH3COCl}$ gives 2- and 4-chloroacetophenone.

###### Reactions with metals

**[exposure]** The **Wurtz–Fittig reaction** is the Wurtz reaction run with a **mixture** of an alkyl halide and an aryl halide, using sodium in dry ether. The alkyl group ends up attached to the ring, giving an **alkylarene**. It's the standard way to put a side chain on benzene: chlorobenzene plus $\ce{CH3Cl}$ gives **toluene**.

$$\ce{C6H5Cl + CH3Cl + 2Na ->[\text{dry ether}] C6H5CH3 + 2NaCl}$$

**[exposure]** The **Fittig reaction** is the same setup with **aryl halide alone** — so two rings couple to each other, giving **diphenyl (biphenyl)**.

$$\ce{2C6H5Cl + 2Na ->[\text{dry ether}] C6H5-C6H5 + 2NaCl}$$

> **Trap:** one reagent tells you which. **Both** halides present → Wurtz–Fittig → alkylarene. **Only** the aryl halide → Fittig → biphenyl. "How do you convert chlorobenzene to biphenyl?" (2025 Q12a) is Fittig, not Wurtz–Fittig.

#### 6.8 Polyhalogen compounds — *pure recall — uses and harmful effects, and it's free marks*

**[exposure]** A **polyhalogen compound** is simply a carbon compound carrying **more than one halogen atom**. The section exists in the syllabus not for the chemistry but for the applications and the environmental damage — so the marks here come from recall, not reasoning.

###### Dichloromethane, $\ce{CH2Cl2}$ (methylene chloride)

**Uses:** solvent, paint remover, propellant in aerosols, degreasing agent.

 **Harm:** affects the **central nervous system**. At low levels in air, impairs hearing and vision. At high levels, causes dizziness, nausea, and tingling or numbness in the fingers and toes. Direct contact burns the skin; contact with the eye burns the cornea.

###### Trichloromethane, $\ce{CHCl3}$ (chloroform)

**Uses:** solvent for fats, alkaloids and iodine; feedstock for making **Freon R-22**. It was once used as a general anaesthetic in surgery but has been replaced by ether, which is less harmful.

 **Harm:** inhaling it **depresses the central nervous system**. Breathing about 900 ppm briefly causes dizziness, fatigue and headache. Chronic exposure damages the **liver and kidneys**.

**Examiner asks:** "why is chloroform stored in dark coloured bottles?" (2026 Q24a) — because in **light and air it is slowly oxidised to phosgene, $\ce{COCl2}$**, an extremely poisonous gas. The bottles are dark **and filled to the brim**, so no air is left inside. Repeat question — memorise the equation:

$$\ce{2CHCl3 + O2 ->[\text{sunlight}] 2COCl2 + 2HCl}$$

###### Triiodomethane, $\ce{CHI3}$ (iodoform)

Formerly used as an **antiseptic**, working through the free iodine it liberates. Now replaced by other iodine formulations because of its **objectionable smell**.

###### Tetrachloromethane, $\ce{CCl4}$ (carbon tetrachloride)

**Uses:** refrigerant manufacture, aerosol propellant, feedstock for chlorofluorocarbons, solvent. Until the 1960s it was a cleaning fluid — an industrial **degreasing agent** and a household spot remover.

 **Harm:** long exposure causes **liver cancer**. Inhalation causes dizziness, light-headedness, nausea and vomiting, and can permanently damage nerve cells. Severe cases lead to stupor, coma, unconsciousness, irregular heartbeat or death. It also **depletes the ozone layer**.

###### Freons

**Freons** are the **chlorofluorocarbons (CFCs)** of methane and ethane. They are extremely stable, unreactive, non-toxic, non-corrosive and easily liquefiable — which is exactly what made them so useful and so damaging. The commonest is **Freon-12, $\ce{CCl2F2}$**, made from $\ce{CCl4}$ by the **Swarts reaction**.

**Uses:** aerosol propellant, refrigeration, air conditioning.

 **Harm:** because they are unreactive, they survive the journey up to the **stratosphere** unchanged. There they start a **chain reaction with ozone** and destroy the ozone layer.

###### DDT

**p,p'-Dichlorodiphenyltrichloroethane** — two benzene rings each carrying a chlorine at the para position, joined by a carbon bearing a $\ce{CCl3}$ group. Prepared by the **condensation of chloral with chlorobenzene in sulphuric acid**.

**Use:** the first modern insecticide — effective against the mosquitoes that spread malaria and the lice that spread typhus.

 **Harm:** many insect species **developed resistance** to it. It is highly toxic to fish. And it is chemically very stable and **fat-soluble**, so animals cannot metabolise it — it accumulates in fatty tissue and builds up along the food chain.

#### Patterns, collected — *the six things you'll actually be asked to do*

A · Predict the product — *2–3 marks*

*Recognise it: a reaction arrow with reagents written over it, and "write the major product" or "identify A and B".*

1. **Read the reagent first** — it decides everything. Aqueous KOH → alcohol. Alcoholic KOH → alkene. $\ce{Mg}$/dry ether → Grignard. $\ce{Na}$/dry ether → Wurtz. $\ce{NaI}$/acetone → Finkelstein. $\ce{AgF}$ → Swarts. $\ce{SOCl2}$ → alkyl chloride.
2. If a double bond is being attacked: Markovnikov unless "peroxide" appears, and peroxide only counts with $\ce{HBr}$.
3. If an alkene is being formed: apply Saytzeff — more substituted is major.
4. If a ring is being attacked: ortho and para, para major.

B · Which reacts faster, and why — *2–3 marks*

*Recognise it: a pair of compounds and "which undergoes faster $S_N1$/$S_N2$".*

1. Identify which mechanism the question names. They run in opposite directions.
2. **$S_N2$** → think **steric hindrance**. Fewer/smaller groups around the carbon wins. 1° > 2° > 3°.
3. **$S_N1$** → think **carbocation stability**. Tertiary, benzylic or allylic wins.
4. If the halogens differ, the **leaving group** decides: $\ce{I > Br > Cl > F}$.
5. Always give the *reason* word — "less steric hindrance" or "resonance-stabilised carbocation". The reason carries the mark, not the choice.

C · Give the reason — *1–2 marks*

*Recognise it: "account for the following" or "why is…".*

Almost every one of these reduces to one of five stock answers: **resonance / partial double bond** (haloarene unreactivity, phenol won't react, allyl beats propyl), **$sp^2$ vs $sp^3$ and s-character** (dipole moment, bond length), **energy of bonds broken vs formed** (water insolubility), **van der Waals and surface area** (boiling points), **escaping gaseous by-products** (thionyl chloride).

D · Arrange in order — *1–2 marks*

*Recognise it: three or four compounds, "increasing order of…".*

1. **Boiling point** → molecular mass first, branching second.
2. **Reactivity to $S_N1$** → carbocation stability.
3. **Reactivity to $S_N2$** → steric hindrance.
4. **Reactivity of $\ce{RX}$ generally** → C–X bond strength: $\ce{RI > RBr > RCl > RF}$.

E · Conversions — *3 marks*

*Recognise it: "how would you convert X into Y".*

1. Count the carbons on both sides. Same count → substitution or addition. Doubled → Wurtz.
2. Alkene → halide: $\ce{HX}$, checking Markovnikov versus peroxide.
3. Need an iodide → make the bromide first, then Finkelstein.
4. Halide → alkene: alcoholic KOH, then check Saytzeff.
5. Halide → alkane: $\ce{Mg}$/dry ether then water, or $\ce{LiAlH4}$ directly.

F · Work backwards from the product — *2–3 marks*

*Recognise it: the product is given and the starting material is A, or "identify the hydrocarbon".*

1. **Wurtz product** → cut the alkane in half at the middle and add $\ce{X}$.
2. **Grignard then water** → the alkane's carbon skeleton is the halide's; put $\ce{MgX}$ back where the new hydrogen went.
3. **"Only one monochlorination product"** → all the hydrogens must be equivalent → **2,2-dimethylpropane (neopentane)**.
4. **"Three isomeric products"** → pentane. **"Four"** → 2-methylbutane.

#### Past year questions · question types — *ranked by how often they turn up*

*From the last 10 years of boards — 25 questions, grouped by pattern.*

1 · Predict the product / identify A, B, C — *3–5 marks*

*Recognise it: a reaction scheme, sometimes a chain of three or four arrows.*

1. Work one arrow at a time; never skip to the end.
2. Name the reaction under each arrow before you draw anything — Finkelstein, Wurtz, Friedel–Crafts, Sandmeyer.
3. Where two products are possible, say which is major and give the rule by name (Markovnikov, Saytzeff, para-major).

> **Trap:** a molecule with two $\ce{-OH}$ groups, one on the ring and one on a side chain, treated with $\ce{SOCl2}$ or $\ce{HCl}$. Only the **side-chain** $\ce{-OH}$ reacts; the phenolic one has partial double-bond character and stays put.

2 · $S_N1$ / $S_N2$ comparison — *2–3 marks*

*Recognise it: a pair of halides, or "write the mechanism of the following".*

1. For a mechanism question, draw **both steps** of $S_N1$ and label the slow step as rate-determining, or draw the $S_N2$ transition state in square brackets.
2. For a comparison, name the deciding factor before you name the winner.

> **Trap:** $S_N2$ ordering is 1° > 2° > 3°; $S_N1$ is the exact reverse. Writing the reactivity order without checking which mechanism the question asked about is the commonest way to lose these marks.

3 · "Give the reason" / "account for the following" — *1–2 marks*

*Recognise it: a statement of fact, then "why?".*

1. Identify which of the five stock explanations applies (see Patterns, C).
2. Write it as cause → effect in one or two sentences. No padding.

4 · IUPAC naming and structure drawing — *1–3 marks*

*Recognise it: "give the IUPAC name" or "draw the structure of…".*

1. Longest chain, then check for a double bond — **it takes numbering priority over the halogen**.
2. Substituents alphabetically in the name; lowest locants where there is a tie.

> **Trap:** numbering from the halogen out of habit when a double bond is present. 4-chlorobut-1-ene, not 1-chlorobut-3-ene.

5 · Conversions — *3 marks*

*Recognise it: "how can the following conversions be carried out".*

1. Count carbons. Choose the route. Write reagents above every arrow — the reagent is what's being marked.

6 · Definitions and stereochemistry — *1–2 marks*

*Recognise it: "define the following term", or a pair of structures with "which is chiral?".*

1. For chirality: find the carbon with **four different** groups. Two identical groups anywhere on it and it is not chiral.
2. For definitions, give the definition and **one example** — the example is usually worth half the mark.

#### Past year questions · mark slots — *what each type is worth*

| Slot | What turns up there |
|---|---|
| **1 mark** | Name the type of halide (vinylic / allylic / benzylic). One-line reason questions. Assertion–reason on reactivity orders. *(inferred)* |
| **2 marks** | "Give the reason" pairs. Two differences between $S_N1$ and $S_N2$. Arrange in order of boiling point. One-step "what happens when". |
| **3 marks** | IUPAC naming (three compounds). Three-part "give reason for the following". Conversions. Identify A and B in a two-step scheme. |
| **5 marks** | Multi-part sets: a reactivity comparison plus a halide-type identification plus a polyhalogen recall, or a product-prediction set combined with definitions. |

*The video groups these as short answer type I (2 marks, Q1–10), short answer type II (3 marks, Q11–23) and long answer (5 marks, Q24–25). At 6 marks in your blueprint this chapter will most likely appear as a mix of 1- and 2-markers rather than a 5-marker — but the 5-mark sets are still the best revision, because they bundle four separate ideas into one question.*

#### Past year questions · repeat offenders — *appeared more than once — highest probability in the chapter*

2021 Q7 · 2024 Q13(b) · 2026 Q24(a)

Which of a pair reacts faster by $S_N2$, with reason. Runs across $\ce{RI}$ vs $\ce{RCl}$ (leaving group), tertiary vs primary (steric hindrance), and two primaries differing in where the branch sits. The single most repeated question shape in the chapter.

2026 Q13(a) · 2024 Q22(a)

$\ce{KCN}$ gives cyanide but $\ce{AgCN}$ gives isocyanide — the ambident nucleophile question. Ionic versus covalent is the whole answer.

2020 Q4 · 2026 Q10(a) · 2021 Q21

$S_N1$: write the mechanism, name the most reactive isomer, or give two differences from $S_N2$. Carbocation stability is the thread through all three.

2017 Q5(a) · lecture PYQ

Why alkyl halides, though polar, are immiscible with water. Energy of bonds broken versus energy released.

2023 Q8(a) · 2024 Q11(c) · lecture PYQ

Arrange in increasing order of boiling point. Appears in both a chain-length form and a halogen-count form.

2024 Q11(b) · lecture PYQ

Why thionyl chloride is preferred for making alkyl chlorides from alcohols. Escapable gaseous by-products.

2026 Q10(b) · 2020 Q18

Wurtz reaction run backwards — the product is given, find the starting halide. Cut the symmetrical alkane in half.

2024 Q13(c) · lecture PYQ

Why Grignard reagents must be prepared under anhydrous conditions. Water destroys them, giving the alkane.

2025 Q19(b) · 2026 Q25(b) · lecture PYQ

Friedel–Crafts on a haloarene, alkylation or acylation, asking for the **major** product. Always para, always because of symmetry and less crowding.

2025 Q15 · 2026 Q23(b) · 2020 Q18

Multi-step "identify A, B, C, D, E" schemes built from Grignard, Wurtz, alcoholic KOH and $\ce{HBr}$ addition. Three separate papers, near-identical shape.

#### Past year questions · cold practice — *answers only — work them before you look*

###### Reactivity and mechanism

- 2021 Q7 — which shows faster $S_N2$: *n*-propyl iodide or *n*-propyl chloride? The iodide — $\ce{I-}$ is a better leaving group because of its large size and weak C–I bond

- 2021 Q7 — faster $S_N2$: *tert*-butyl chloride or ethyl chloride? Ethyl chloride — primary, so far less steric hindrance

- 2026 Q13(b) — why is cyclohexylmethyl chloride more reactive to $S_N2$ than cyclohexyl chloride? The first is primary, the second secondary — less crowding at a primary carbon

- 2026 Q10(a) — most reactive $\ce{C4H9Br}$ isomer towards $S_N1$. 2-bromo-2-methylpropane — it forms the most stable, tertiary carbocation

- 2021 Q21 — faster $S_N1$: cyclohexylmethyl chloride or benzyl chloride? Benzyl chloride — the benzyl carbocation is resonance-stabilised by the ring

- 2026 Q24(a) — more reactive to $S_N1$: 2-bromo-2-methylbutane or 1-bromopentane? 2-bromo-2-methylbutane — tertiary carbocation beats primary

- 2025 Q20(b) — why is allyl chloride hydrolysed faster than *n*-propyl chloride? The allyl carbocation is resonance-stabilised; the propyl one is not

- 2026 Q23(c) — which of $S_N1$/$S_N2$ gives inversion, which gives racemisation? $S_N2$ inversion (back-side attack); $S_N1$ racemisation (planar carbocation, attack from either face)

###### Reason questions

- Lecture PYQ Q1 — why are haloarenes less reactive to nucleophilic substitution? Resonance gives the C–X bond partial double-bond character, and the $sp^2$ carbon holds the pair more tightly

- 2024 Q16 — why is the dipole moment of chlorobenzene lower than that of cyclohexyl chloride? The $sp^2$ carbon is more electronegative, so less charge separation; resonance also shortens the C–Cl bond

- 2020 Q9(b) — why does $\ce{-NO2}$ at ortho/para increase haloarene reactivity to nucleophilic substitution? It withdraws electron density, weakening the C–X bond and activating the ring

- 2026 Q25(a) — chlorine shows –I yet is ortho/para directing. Why? –I deactivates the whole ring, but +R resonance raises electron density specifically at ortho and para

- 2024 Q22(c) — why are d- and l-butan-2-ol hard to separate by fractional distillation? Enantiomers have identical boiling points

- 2026 Q24(a) — why is chloroform stored in dark bottles, filled to the brim? Light and air oxidise it to phosgene, $\ce{COCl2}$, a poisonous gas

###### Products and conversions

- 2023 Q3 — isopropyl alcohol + $\ce{PCl5}$, then $\ce{AgCN}$. Isopropyl chloride, then isopropyl isocyanide $\ce{(CH3)2CHNC}$

- 2023 Q3 — 1-chloropropane + alcoholic KOH, then $\ce{HBr}$. Propene, then 2-bromopropane (Markovnikov)

- 2020 Q9(a) — convert but-1-ene to 1-iodobutane. $\ce{HBr}$/peroxide → 1-bromobutane, then $\ce{NaI}$/acetone (Finkelstein)

- 2025 Q12(a) — convert chlorobenzene to biphenyl. $\ce{Na}$/dry ether — Fittig reaction

- 2025 Q12(c) — convert 2-bromobutane to but-2-ene. Alcoholic KOH; but-2-ene is major by Saytzeff

- 2025 Q20(a) — methyl bromide + $\ce{AgF}$. Methyl fluoride — Swarts reaction

- 2025 Q20(b) — 2,4,6-trinitrochlorobenzene, hydrolysed. 2,4,6-trinitrophenol, i.e. picric acid

- 2026 Q25(a) — chlorobenzene + conc. $\ce{H2SO4}$, heat: major product. 4-chlorobenzenesulphonic acid

- 2026 Q25(b) — bromobenzene + $\ce{CH3Cl}$ / anhydrous $\ce{AlCl3}$: major product. 1-bromo-4-methylbenzene (para major)

- 2025 Q19(a) — a nitro-substituted ethylbenzene heated with $\ce{Br2}$: major product. Bromination at the benzylic carbon — that free radical is resonance-stabilised

- 2026 Q25(b) — dehydrohalogenation of 1-bromo-1-methylcyclohexane. 1-methylcyclohexene — the more substituted alkene, by Saytzeff

###### Naming, structure and identification

- 2026 Q2(a) — draw 4-bromo-3-methylpent-2-ene. $\ce{CH3-CH=C(CH3)-CHBr-CH3}$

- 2024 Q11(a) — IUPAC name of a four-carbon chain with a double bond and Cl at the far end. 4-chlorobut-1-ene — the double bond takes numbering priority

- 2017 Q14 — IUPAC names of $\ce{CH3CHBrCH2CH3}$, 1,3-dibromobenzene, and a chloropropene. 2-bromobutane; 1,3-dibromobenzene; 3-chloroprop-1-ene

- 2026 Q23(a) — a hydrocarbon $\ce{C5H12}$ gives only one monochlorination product. Identify it. 2,2-dimethylpropane — all twelve hydrogens are equivalent

- 2026 Q10(b) — which $\ce{C4H9Br}$ isomer gives 2,5-dimethylhexane with $\ce{Na}$/dry ether? 1-bromo-2-methylpropane — cut the product in half

- 2026 Q24(a) — halogen present in $\ce{CH2=CH-Cl}$? Vinylic — chlorine sits directly on a doubly-bonded carbon

- 2017 Q5(b) — which of the pair is the allylic halide? The one where Cl is on an $sp^3$ carbon *next to* the double bond, not on it

- 2026 Q17(b) — which of a pair is chiral? The one whose carbon carries four *different* groups; two identical groups anywhere and it isn't

- 2026 Q24(b) — define ambident nucleophile and racemic mixture. Two donor atoms, attacks through either ($\ce{CN-}$, $\ce{NO2-}$); and a 1:1 mixture of enantiomers, optically inactive because the rotations cancel

Built from Sourabh Raina's Haloalkanes and Haloarenes one-shot and PYQ videos, cross-checked against NCERT Class XII Chemistry Chapter 6 (Rationalised 2022–23). NCERT spellings used throughout: **Zaitsev** (NCERT notes it is "also pronounced as Saytzeff"), **ambident** nucleophile, **vicinal** and **geminal** dihalides, **laevorotatory**. C–Cl bond lengths (177 pm in haloalkanes, 169 pm in haloarenes) are NCERT's. First-contact material: every term marked **[exposure]** is explained from scratch before use.

Two stretches of both transcripts were lost at automatic-transcription chunk boundaries and were recovered by re-transcribing those windows from the source audio: the $S_N2$ mechanism and ambident-nucleophile block in the lecture, and PYQ questions 12, 13, 17, 18, 22 and 23. All twenty-five PYQ questions are accounted for here.

### Every Chemistry Formula

`Class XII CBSE · Chemistry · Chapters 1–6`

*Every formula the half-yearly can ask for, each with what its symbols mean, the unit it comes out in, and the one situation that tells you to reach for it. The cue is on the outside and the formula is hidden — so read down the page and say each one before you open it.*

- Formulas: 50

- Recall rules: 18

- Must be instant: 40

- Paper: 70 marks

##### How to use this

**●** means you should be able to say it before the question finishes loading. **○** means a few seconds of thought is fine — these are the ones you derive or reconstruct rather than recall.

Work down a chapter with everything closed. Say the formula out loud, *then* tap to reveal. A formula you can only recognise is not a formula you have.

Units are not decoration. Most lost marks in Solutions and Electrochemistry are unit slips — molality is per **kilogram of solvent**, molarity per **litre of solution**, and $\kappa$ in $\ce{S cm^-1}$ with $c$ in $\ce{mol L^-1}$ is what makes the 1000 appear in molar conductivity.

##### Recognise index

*Every cue on one screen. Read the cue, say the formula, tap to check.*

1 · Solutions — 15 marks

- `C1.1` Concentration by mass, volume, or parts per million

- `C1.2` Mole fraction of a component

- `C1.3` Molarity, from mass or from moles

- `C1.4` Molality, and why it is the one used for colligative properties

- `C1.5` A gas dissolving in a liquid under pressure

- `C1.6` Vapour pressure of a mixture of two volatile liquids

- `C1.7` Vapour pressure when the solute is non-volatile

- `C1.8` Relative lowering of vapour pressure

- `C1.9` Boiling point raised by a dissolved solute

- `C1.10` Freezing point lowered by a dissolved solute

- `C1.11` Osmotic pressure across a semipermeable membrane

- `C1.12` Molar mass from any one colligative property

- `C1.13` The measured effect is bigger or smaller than predicted

- `C1.14` Degree of dissociation or association from $i$

2 · Electrochemistry — 14 marks

- `C2.1` Standard cell potential from two electrode potentials

- `C2.2` Cell potential at non-standard concentrations

- `C2.3` Nernst for a single electrode

- `C2.4` Free energy change of a cell reaction

- `C2.5` Equilibrium constant from cell potential

- `C2.6` Conductance, resistance and the cell constant

- `C2.7` Conductivity from measured resistance

- `C2.8` Molar conductivity from conductivity

- `C2.9` Limiting molar conductivity of an electrolyte from its ions

- `C2.10` Degree of dissociation of a weak electrolyte

- `C2.11` Dissociation constant of a weak acid from conductivity

- `C2.12` Mass deposited during electrolysis

- `C2.13` Moles of electrons passed

3 · Chemical Kinetics — 13 marks

- `C3.1` Rate of a reaction from a concentration change

- `C3.2` Rate written for a balanced equation with coefficients

- `C3.3` Rate law and the order of a reaction

- `C3.4` Units of the rate constant for any order

- `C3.5` Zero order — concentration against time

- `C3.6` Zero order half-life

- `C3.7` First order rate constant from concentrations

- `C3.8` First order half-life

- `C3.9` First order reaction in the gas phase, measured by total pressure

- `C3.10` Rate constant against temperature

- `C3.11` Activation energy from a straight-line plot

- `C3.12` Activation energy from two temperatures

4 · d and f Block — 11 marks

- `C4.1` Magnetic moment from unpaired electrons, and back again

- `C4.2` General electronic configuration of a block

5 · Coordination Compounds — 11 marks

- `C5.1` Oxidation number of the metal inside a complex

- `C5.2` Coordination number when a ligand grips more than once

- `C5.3` Tetrahedral splitting compared with octahedral

- `C5.4` Crystal field stabilisation energy of an octahedral complex

- `C5.5` High spin or low spin — deciding which

- `C5.6` Number of geometrical isomers of a complex

6 · Haloalkanes and Haloarenes — 6 marks

- `C6.1` Rate law that identifies the substitution mechanism

- `C6.2` Degree of unsaturation from a molecular formula

Constants — worth the same marks as the formulas

- `K` Every constant this paper can hand you, with its unit

#### `CH 1` Solutions — *14 formulas · 15 marks*

##### ● `C1.1` Concentration by mass, by volume, or in parts per million

$$\%\,w/w = \frac{w_B}{w_A + w_B}\times 100 \qquad \%\,v/v = \frac{V_B}{V_{\text{soln}}}\times 100$$
          $$\%\,w/v = \frac{w_B}{V_{\text{soln in mL}}}\times 100 \qquad \text{ppm} = \frac{w_B}{w_{\text{soln}}}\times 10^{6}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $w_B$ | mass of solute | g |
| $w_A$ | mass of solvent | g |
| $V_{\text{soln}}$ | volume of solution | mL or L |
| all four | the concentration itself | dimensionless |

**Use it when:**

> The question gives masses or volumes and no moles anywhere. ppm is for trace quantities — pollutants, dissolved gases, hardness of water.

**Trap:**

> $\%\,w/w$ divides by the mass of the **solution**, not the solvent. Adding 10 g of solute to 90 g of water gives 10%, not 11.1%.

##### ● `C1.2` Mole fraction of a component

$$x_A = \frac{n_A}{n_A + n_B} \qquad x_A + x_B = 1$$

| Symbol | Meaning | Unit |
|---|---|---|
| $x_A$ | mole fraction of the solvent | dimensionless |
| $n_A$ | moles of solvent, $= w_A/M_A$ | mol |
| $n_B$ | moles of solute | mol |

**Use it when:**

> Raoult's law or Henry's law is involved — both are written in mole fractions, never in molarity.

**Trap:**

> For water as solvent, $M_A = 18$, so $n_A$ is large and $x_B$ is tiny. Do not round $x_A$ to 1 before subtracting — you will get $x_B = 0$.

##### ● `C1.3` Molarity, from moles or straight from mass

$$M = \frac{n_B}{V_{\text{soln in L}}} = \frac{w_B \times 1000}{M_B \times V_{\text{soln in mL}}}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $M$ | molarity | mol L⁻¹ |
| $n_B$ | moles of solute | mol |
| $M_B$ | molar mass of solute | g mol⁻¹ |
| $V$ | volume of **solution** | L (or mL) |

**Use it when:**

> Volume of solution is given or asked. Also the concentration used in osmotic pressure, $\pi = CRT$.

**Trap:**

> Molarity **changes with temperature** because volume does. Molality does not. If a question mentions heating or cooling and then asks which concentration term is unaffected, the answer is molality.

##### ● `C1.4` Molality — and the unit that makes it the colligative one

$$m = \frac{n_B}{w_A \text{ in kg}} = \frac{w_B \times 1000}{M_B \times w_A \text{ in g}}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $m$ | molality | mol kg⁻¹ |
| $w_A$ | mass of **solvent** only | kg (or g) |
| $M_B$ | molar mass of solute | g mol⁻¹ |

**Use it when:**

> Anything colligative: $\Delta T_b$, $\Delta T_f$. Both are written in molality precisely because it is temperature-independent.

**Trap:**

> Per kg of **solvent**, not of solution. The 1000 in the second form converts grams of solvent to kilograms — it is not the same 1000 as in molarity, where it converts mL of solution to L.

##### ● `C1.5` A gas dissolving in a liquid under pressure

$$p = K_H \, x$$

| Symbol | Meaning | Unit |
|---|---|---|
| $p$ | partial pressure of the gas above the solution | bar (or kbar) |
| $x$ | mole fraction of the gas in solution | dimensionless |
| $K_H$ | Henry's law constant | bar (or kbar) |

**Use it when:**

> A gas is being dissolved — soda bottles, deep-sea diving and the bends, oxygen at altitude, aquatic life in warm water.

**Trap:**

> $K_H$ goes **up** with temperature, so solubility goes **down** — which is why warm water holds less dissolved oxygen. A higher $K_H$ means a *less* soluble gas.

##### ● `C1.6` Vapour pressure of a mixture of two volatile liquids

$$p_{\text{total}} = p_A^{\,\circ} x_A + p_B^{\,\circ} x_B = p_B^{\,\circ} + \left(p_A^{\,\circ} - p_B^{\,\circ}\right) x_A$$

| Symbol | Meaning | Unit |
|---|---|---|
| $p_A^{\,\circ}$ | vapour pressure of pure A | bar or mm Hg |
| $x_A$ | mole fraction of A in the **liquid** | dimensionless |
| $y_A$ | mole fraction of A in the **vapour**, $= p_A/p_{\text{total}}$ | dimensionless |

**Use it when:**

> Both components evaporate. The second form is the equation of a straight line in $x_A$ — that is the plot they ask you to sketch.

**Trap:**

> Vapour composition $y_A$ is not the same as liquid composition $x_A$. The vapour is always richer in the more volatile component.

##### ● `C1.7` Vapour pressure when the solute is non-volatile

$$p_{\text{soln}} = x_A \, p_A^{\,\circ}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $p_{\text{soln}}$ | vapour pressure of the solution | bar or mm Hg |
| $x_A$ | mole fraction of the **solvent** | dimensionless |
| $p_A^{\,\circ}$ | vapour pressure of pure solvent | bar or mm Hg |

**Use it when:**

> A solid, non-volatile solute (sugar, urea, a salt) is dissolved. Only the solvent contributes vapour.

**Trap:**

> It is $x$ of the **solvent**, not the solute. Using $x_B$ here is the single commonest slip in this chapter.

##### ● `C1.8` Relative lowering of vapour pressure

$$\frac{p_A^{\,\circ} - p_{\text{soln}}}{p_A^{\,\circ}} = x_B = \frac{n_B}{n_A + n_B} \;\approx\; \frac{w_B \, M_A}{M_B \, w_A}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $x_B$ | mole fraction of solute | dimensionless |
| $M_A$ | molar mass of solvent | g mol⁻¹ |
| $M_B$ | molar mass of solute — usually what is asked | g mol⁻¹ |

**Use it when:**

> Two vapour pressures are given (pure solvent and solution) and a molar mass is wanted.

**Trap:**

> The final approximation assumes $n_B \ll n_A$ — valid for a dilute solution only. If the question says concentrated, use the exact form.

##### ● `C1.9` Boiling point raised by a dissolved solute

$$\Delta T_b = K_b \, m \qquad \Delta T_b = T_b - T_b^{\,\circ}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Delta T_b$ | elevation of boiling point | K |
| $K_b$ | molal elevation constant (ebullioscopic constant) | K kg mol⁻¹ |
| $m$ | molality | mol kg⁻¹ |

**Use it when:**

> A boiling point shifts. For water $K_b = 0.52\ \text{K kg mol}^{-1}$.

**Trap:**

> $K_b$ is a property of the **solvent** alone — it never depends on which solute you dissolved.

##### ● `C1.10` Freezing point lowered by a dissolved solute

$$\Delta T_f = K_f \, m \qquad \Delta T_f = T_f^{\,\circ} - T_f$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Delta T_f$ | depression of freezing point | K |
| $K_f$ | molal depression constant (cryoscopic constant) | K kg mol⁻¹ |
| $m$ | molality | mol kg⁻¹ |

**Use it when:**

> A freezing point shifts — antifreeze in a radiator, salt on an icy road. For water $K_f = 1.86\ \text{K kg mol}^{-1}$.

**Trap:**

> Note the order of subtraction is reversed from $\Delta T_b$: freezing point goes **down**, so it is pure minus solution. Both $\Delta T$ values come out positive.

##### ● `C1.11` Osmotic pressure across a semipermeable membrane

$$\pi = C R T = \frac{n_B}{V} R T \qquad \pi V = n_B R T$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\pi$ | osmotic pressure | bar or atm |
| $C$ | molarity | mol L⁻¹ |
| $R$ | gas constant | 0.0821 L atm K⁻¹ mol⁻¹ |
| $T$ | absolute temperature | K |

**Use it when:**

> A membrane, a molar mass of a **protein or polymer**, or the word isotonic/hypertonic appears. This is the method of choice for large molar masses because $\pi$ is measurably large even when $\Delta T_f$ would be tiny.

**Trap:**

> Uses molarity, not molality — the only colligative property that does. Match the $R$ value to the pressure unit you want.

##### ● `C1.12` Molar mass from any one colligative property

$$M_B = \frac{K_b \, w_B \times 1000}{\Delta T_b \, w_A} \qquad M_B = \frac{K_f \, w_B \times 1000}{\Delta T_f \, w_A} \qquad M_B = \frac{w_B R T}{\pi V}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $M_B$ | molar mass of the solute | g mol⁻¹ |
| $w_B$ | mass of solute | g |
| $w_A$ | mass of solvent | g |
| $V$ | volume of solution | L |

**Use it when:**

> "Calculate the molar mass of the solute" — the standard 3-marker. All three are just C1.9–C1.11 rearranged; do not memorise them separately.

**Trap:**

> The 1000 is there because $w_A$ is in grams while molality needs kilograms. Drop it and your answer is out by exactly a factor of 1000.

##### ● `C1.13` When the measured effect is bigger or smaller than predicted

$$i = \frac{\text{observed colligative property}}{\text{calculated colligative property}} = \frac{\text{normal molar mass}}{\text{abnormal molar mass}}$$
          $$\Delta T_b = i K_b m \qquad \Delta T_f = i K_f m \qquad \pi = i C R T$$

| Symbol | Meaning | Unit |
|---|---|---|
| $i$ | van't Hoff factor | dimensionless |
| $i \gt 1$ | solute dissociates — e.g. $\ce{NaCl}$, $i \to 2$ | dimensionless |
| $i \lt 1$ | solute associates — e.g. benzoic acid in benzene, $i \to 0.5$ | dimensionless |

**Use it when:**

> The solute is ionic, or the question uses the word "abnormal", or the observed $\Delta T_f$ does not match the calculated one.

**Trap:**

> Molar mass and $i$ move **opposite** ways. Dissociation ($i \gt 1$) makes the measured molar mass come out *lower* than the true value.

##### ○ `C1.14` Degree of dissociation or association from $i$

$$\alpha_{\text{dissociation}} = \frac{i-1}{n-1} \qquad \alpha_{\text{association}} = \frac{1-i}{1-\tfrac{1}{n}}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\alpha$ | degree of dissociation or association | dimensionless |
| $n$ | number of particles one formula unit gives (or combines into) | dimensionless |
| $i$ | van't Hoff factor | dimensionless |

**Use it when:**

> $i$ has been found and the percentage dissociation is asked. For $\ce{K2SO4}$, $n = 3$; for a dimerising acid, $n = 2$.

**Trap:**

> Read $n$ off the actual dissociation equation, not the number of atoms. $\ce{K2SO4 -> 2K+ + SO4^2-}$ gives three particles, so $n=3$.

#### `CH 2` Electrochemistry — *13 formulas · 14 marks*

##### ● `C2.1` Standard cell potential from two electrode potentials

$$E^{\,\circ}_{\text{cell}} = E^{\,\circ}_{\text{cathode}} - E^{\,\circ}_{\text{anode}} = E^{\,\circ}_{\text{right}} - E^{\,\circ}_{\text{left}}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $E^{\,\circ}_{\text{cell}}$ | standard cell potential | V |
| $E^{\,\circ}$ | standard **reduction** potential of each electrode | V |

**Use it when:**

> Two half-cells and their $E^\circ$ values are given. A positive $E^\circ_{\text{cell}}$ means the reaction is spontaneous as written. Daniell cell: $1.1\ \text{V}$.

**Trap:**

> Both values in the table are **reduction** potentials — subtract, never add, and never flip the sign of the anode value and then also subtract.

##### ● `C2.2` Cell potential when concentrations are not 1 M

$$E_{\text{cell}} = E^{\,\circ}_{\text{cell}} - \frac{2.303\,RT}{nF}\log Q \;\;\xrightarrow{\;298\text{ K}\;}\;\; E_{\text{cell}} = E^{\,\circ}_{\text{cell}} - \frac{0.059}{n}\log Q$$

| Symbol | Meaning | Unit |
|---|---|---|
| $n$ | moles of electrons in the balanced cell reaction | dimensionless |
| $Q$ | reaction quotient, products over reactants | dimensionless |
| $F$ | Faraday constant | 96487 C mol⁻¹ |
| $R$ | gas constant | 8.314 J K⁻¹ mol⁻¹ |

**Use it when:**

> Any concentration is given that is not 1 M, or the question says "calculate the emf of the cell".

**Trap:**

> NCERT uses **0.059**, not 0.0591. Pure solids and liquids never appear in $Q$. Get $n$ from the balanced equation, not from the charge on one ion.

##### ○ `C2.3` Nernst equation for a single electrode

$$E_{(\ce{M^{n+}}/\ce{M})} = E^{\,\circ}_{(\ce{M^{n+}}/\ce{M})} - \frac{0.059}{n}\log\frac{1}{[\ce{M^{n+}}]}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $[\ce{M^{n+}}]$ | concentration of the metal ion | mol L⁻¹ |
| $n$ | charge on the metal ion | dimensionless |
| $E$ | electrode potential | V |

**Use it when:**

> Only one half-cell is being asked about, or a concentration cell is given where both electrodes are the same metal at different concentrations.

**Trap:**

> The solid metal is taken as unit activity, so it is the 1 in the numerator. For a concentration cell $E^\circ_{\text{cell}} = 0$ and the whole emf comes from the log term.

##### ● `C2.4` Free energy change of a cell reaction

$$\Delta_r G = -nFE_{\text{cell}} \qquad \Delta_r G^{\,\circ} = -nFE^{\,\circ}_{\text{cell}}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Delta_r G$ | Gibbs energy change of the cell reaction | J mol⁻¹ |
| $n$ | moles of electrons transferred | dimensionless |
| $F$ | Faraday constant | 96487 C mol⁻¹ |

**Use it when:**

> The question asks for $\Delta G$, for maximum work obtainable, or whether a reaction is feasible.

**Trap:**

> Answer comes out in joules, not kilojoules — divide by 1000 if the options are in kJ. The minus sign is part of the formula: a positive emf gives a negative $\Delta G$.

##### ○ `C2.5` Equilibrium constant from cell potential

$$\Delta_r G^{\,\circ} = -RT\ln K_c \qquad\Longrightarrow\qquad E^{\,\circ}_{\text{cell}} = \frac{0.059}{n}\log K_c$$

| Symbol | Meaning | Unit |
|---|---|---|
| $K_c$ | equilibrium constant of the cell reaction | dimensionless |
| $E^{\,\circ}_{\text{cell}}$ | standard cell potential | V |
| $n$ | moles of electrons | dimensionless |

**Use it when:**

> $K_c$ is asked from $E^\circ$, or vice versa. It is just the Nernst equation with $E_{\text{cell}} = 0$ and $Q = K_c$ — at equilibrium the cell is dead.

**Trap:**

> Note this is $+$, not $-$: setting $E_{\text{cell}}=0$ moves the log term across the equals sign.

##### ● `C2.6` Conductance, resistance and the cell constant

$$G = \frac{1}{R} \qquad G^{*} = \frac{l}{A} \qquad R = \rho\frac{l}{A}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $G$ | conductance | S (siemens) |
| $R$ | resistance | Ω |
| $G^{*}$ | cell constant | cm⁻¹ or m⁻¹ |
| $\rho$ | resistivity | Ω cm |

**Use it when:**

> A conductivity cell is described by its electrode area and separation, or the cell constant is given directly.

**Trap:**

> $1\ \text{S} = 1\ \Omega^{-1}$, also written mho. The cell constant has units of **inverse** length because it is length ÷ area.

##### ● `C2.7` Conductivity from a measured resistance

$$\kappa = \frac{1}{\rho} = G \times G^{*} = \frac{1}{R}\times\frac{l}{A}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\kappa$ | conductivity (specific conductance) | S cm⁻¹ or S m⁻¹ |
| $G^{*}$ | cell constant | cm⁻¹ |
| $R$ | measured resistance | Ω |

**Use it when:**

> The question gives a resistance from a conductivity cell. $\kappa$ is the conductance of a 1 cm cube of solution.

**Trap:**

> $\kappa$ **decreases** on dilution (fewer ions per unit volume) while molar conductivity **increases**. Being asked to explain that opposite behaviour is a standing 2-marker.

##### ● `C2.8` Molar conductivity from conductivity

$$\Lambda_m = \frac{\kappa}{c} = \frac{\kappa \times 1000}{c \text{ in mol L}^{-1}}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Lambda_m$ | molar conductivity | S cm² mol⁻¹ |
| $\kappa$ | conductivity | S cm⁻¹ |
| $c$ | concentration | mol L⁻¹ |

**Use it when:**

> Converting a measured $\kappa$ into the quantity you actually compare between electrolytes.

**Trap:**

> The 1000 exists only because $\kappa$ is per **cm³** while $c$ is per **litre**. In SI ($\kappa$ in S m⁻¹, $c$ in mol m⁻³) there is no 1000 and the unit is S m² mol⁻¹.

##### ● `C2.9` Limiting molar conductivity built from its ions

$$\Lambda^{\,\circ}_m = \nu_+ \lambda^{\,\circ}_+ + \nu_- \lambda^{\,\circ}_-$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Lambda^{\,\circ}_m$ | limiting molar conductivity (infinite dilution) | S cm² mol⁻¹ |
| $\lambda^{\,\circ}_\pm$ | limiting molar conductivity of each ion | S cm² mol⁻¹ |
| $\nu_\pm$ | how many of that ion one formula unit gives | dimensionless |

**Use it when:**

> $\Lambda^\circ_m$ of a **weak** electrolyte is wanted — it cannot be measured by extrapolation, so it is assembled from strong electrolytes. This is **Kohlrausch's law of independent migration of ions**.

**Trap:**

> Multiply by $\nu$. For $\ce{CaCl2}$, $\Lambda^\circ_m = \lambda^\circ_{\ce{Ca^2+}} + 2\lambda^\circ_{\ce{Cl^-}}$ — the 2 is easy to drop.

##### ● `C2.10` Degree of dissociation of a weak electrolyte

$$\alpha = \frac{\Lambda_m}{\Lambda^{\,\circ}_m}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\alpha$ | degree of dissociation | dimensionless |
| $\Lambda_m$ | molar conductivity at concentration $c$ | S cm² mol⁻¹ |
| $\Lambda^{\,\circ}_m$ | limiting molar conductivity | S cm² mol⁻¹ |

**Use it when:**

> A weak acid or base is given with both conductivity values.

**Trap:**

> Only meaningful for a **weak** electrolyte. A strong electrolyte is fully dissociated; its $\Lambda_m$ rises with dilution because ion–ion interference falls, not because more of it dissociates.

##### ○ `C2.11` Dissociation constant of a weak acid from conductivity

$$K_a = \frac{c\alpha^{2}}{1-\alpha} = \frac{c\,\Lambda_m^{2}}{\Lambda^{\,\circ}_m\left(\Lambda^{\,\circ}_m - \Lambda_m\right)}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $K_a$ | dissociation constant | mol L⁻¹ |
| $c$ | concentration of the acid | mol L⁻¹ |
| $\alpha$ | degree of dissociation | dimensionless |

**Use it when:**

> Both $\Lambda_m$ and $\Lambda^\circ_m$ are given for a weak acid and $K_a$ or $\mathrm{p}K_a$ is asked.

**Trap:**

> Do not approximate $1-\alpha \approx 1$ unless $\alpha$ is genuinely small (below about 0.05).

##### ● `C2.12` Mass deposited or liberated during electrolysis

$$Q = I t \qquad w = Z I t \qquad Z = \frac{M}{nF}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $Q$ | charge passed | C |
| $I$ | current | A |
| $t$ | time | s |
| $w$ | mass deposited | g |
| $Z$ | electrochemical equivalent | g C⁻¹ |

**Use it when:**

> A current runs for a time and a mass is asked. Faraday's first law of electrolysis.

**Trap:**

> Time must be in **seconds**. A question quoting minutes or hours is testing exactly this.

##### ● `C2.13` Moles of electrons passed, and how much substance that gives

$$n_{e^-} = \frac{Q}{F} = \frac{It}{96487} \qquad \text{moles of product} = \frac{n_{e^-}}{n}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $n_{e^-}$ | moles of electrons | mol |
| $F$ | charge on one mole of electrons | 96487 C mol⁻¹ |
| $n$ | electrons needed per ion, from the half-equation | dimensionless |

**Use it when:**

> Several cells are in series, or a gas volume at STP is asked. Faraday's second law: the same charge deposits amounts in the ratio of their equivalent masses.

**Trap:**

> Get $n$ from the half-reaction. $\ce{Cu^2+ + 2e^- -> Cu}$ needs 2 F per mole; $\ce{Al^3+}$ needs 3 F.

#### `CH 3` Chemical Kinetics — *12 formulas · 13 marks*

##### ● `C3.1` Rate of a reaction from a concentration change

$$r_{\text{av}} = -\frac{\Delta[R]}{\Delta t} = +\frac{\Delta[P]}{\Delta t} \qquad r_{\text{inst}} = -\frac{d[R]}{dt}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $[R]$ | concentration of a reactant | mol L⁻¹ |
| $t$ | time | s |
| $r$ | rate of reaction | mol L⁻¹ s⁻¹ |

**Use it when:**

> A table of concentration against time is given. Instantaneous rate is the slope of the tangent to that curve.

**Trap:**

> The minus sign exists so the rate comes out positive — reactant concentration is falling. Never report a negative rate.

##### ● `C3.2` Rate written for an equation that has coefficients

$$\ce{aA + bB -> cC + dD}$$
          $$r = -\frac{1}{a}\frac{d[A]}{dt} = -\frac{1}{b}\frac{d[B]}{dt} = +\frac{1}{c}\frac{d[C]}{dt} = +\frac{1}{d}\frac{d[D]}{dt}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $a, b, c, d$ | stoichiometric coefficients | dimensionless |
| $r$ | the one unique rate of reaction | mol L⁻¹ s⁻¹ |

**Use it when:**

> The question gives the rate of disappearance of one species and asks for another. $\ce{2N2O5 -> 4NO2 + O2}$ makes $\ce{NO2}$ four times as fast as it makes $\ce{O2}$.

**Trap:**

> You **divide** by the coefficient. Multiplying is the reflex error.

##### ● `C3.3` Rate law, and the order of a reaction

$$r = k\,[A]^{x}[B]^{y} \qquad \text{order} = x + y$$

| Symbol | Meaning | Unit |
|---|---|---|
| $k$ | rate constant | depends on order — see C3.4 |
| $x, y$ | order with respect to A and B | dimensionless |
| order | overall order | dimensionless |

**Use it when:**

> A table of initial rates against initial concentrations is given. Double one concentration, see what the rate does: unchanged → order 0, doubles → 1, quadruples → 2.

**Trap:**

> Order is found by **experiment** and can be zero or fractional. Molecularity comes from the mechanism, is a whole number, and is never zero. A **pseudo first order reaction** is second order on paper but first order in practice because one reactant is in huge excess.

##### ● `C3.4` Units of the rate constant for any order

$$[k] = \text{mol}^{\,1-n}\,\text{L}^{\,n-1}\,\text{s}^{-1}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $n = 0$ | zero order | mol L⁻¹ s⁻¹ |
| $n = 1$ | first order | s⁻¹ |
| $n = 2$ | second order | L mol⁻¹ s⁻¹ |
| $n$ | overall order | dimensionless |

**Use it when:**

> The order is asked and only the units of $k$ are given — this runs backwards perfectly, and it is a favourite one-marker.

**Trap:**

> First order $k$ has no concentration unit at all, which is why a first-order half-life does not depend on concentration.

##### ● `C3.5` Zero order — concentration against time

$$[R] = -kt + [R]_0 \qquad k = \frac{[R]_0 - [R]}{t}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $[R]_0$ | initial concentration | mol L⁻¹ |
| $[R]$ | concentration at time $t$ | mol L⁻¹ |
| $k$ | zero order rate constant | mol L⁻¹ s⁻¹ |

**Use it when:**

> The plot of $[R]$ against $t$ is a straight line of slope $-k$. Real examples: decomposition of $\ce{NH3}$ on hot platinum, of $\ce{HI}$ on gold.

**Trap:**

> Zero order means the rate is independent of concentration — usually because a catalyst surface is saturated, not because nothing is happening.

##### ● `C3.6` Zero order half-life

$$t_{1/2} = \frac{[R]_0}{2k}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $t_{1/2}$ | half-life | s |
| $[R]_0$ | initial concentration | mol L⁻¹ |
| $k$ | rate constant | mol L⁻¹ s⁻¹ |

**Use it when:**

> A zero-order reaction's half-life is asked, or the question tests that $t_{1/2} \propto [R]_0$ here.

**Trap:**

> This one **does** depend on starting concentration — the exact opposite of first order. Getting the two the wrong way round is the standing trap of this chapter.

##### ● `C3.7` First order rate constant from concentrations

$$k = \frac{2.303}{t}\log\frac{[R]_0}{[R]} \qquad \log[R] = -\frac{k}{2.303}t + \log[R]_0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $k$ | first order rate constant | s⁻¹ |
| $[R]_0$ | initial concentration | mol L⁻¹ |
| $[R]$ | concentration at time $t$ | mol L⁻¹ |

**Use it when:**

> The commonest numerical in the chapter. The second form says a plot of $\log[R]$ against $t$ is a straight line of slope $-k/2.303$.

**Trap:**

> 2.303 converts $\ln$ to $\log_{10}$. If you use $\ln$, drop the 2.303 — using both is a factor-of-2.3 error.

##### ● `C3.8` First order half-life

$$t_{1/2} = \frac{0.693}{k}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $t_{1/2}$ | half-life | s |
| $k$ | first order rate constant | s⁻¹ |
| 0.693 | $\ln 2$ | dimensionless |

**Use it when:**

> Any half-life question on a first-order reaction, including all radioactive decay.

**Trap:**

> **Independent of starting concentration.** Being asked to prove that is a standing 2-marker — see the derivations page.

##### ○ `C3.9` First order gas-phase reaction followed by total pressure

$$k = \frac{2.303}{t}\log\frac{p_i}{2p_i - p_t}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $p_i$ | initial pressure of the reactant | bar or atm |
| $p_t$ | total pressure at time $t$ | bar or atm |
| $k$ | rate constant | s⁻¹ |

**Use it when:**

> A gas decomposes into two gas molecules and the data is a table of total pressure against time — e.g. azoisopropane, or $\ce{N2O5}$ decomposition.

**Trap:**

> The $2p_i - p_t$ form holds only when one mole of gas gives two moles of gas. For a different stoichiometry, rebuild the pressure table from scratch.

##### ● `C3.10` Rate constant against temperature

$$k = A\,e^{-E_a/RT}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $A$ | frequency (pre-exponential) factor | same as $k$ |
| $E_a$ | activation energy | J mol⁻¹ |
| $R$ | gas constant | 8.314 J K⁻¹ mol⁻¹ |
| $T$ | absolute temperature | K |

**Use it when:**

> Temperature enters the question at all. The Arrhenius equation.

**Trap:**

> $e^{-E_a/RT}$ is the **fraction of molecules with energy at least $E_a$** — quoting that meaning is often the mark.

##### ○ `C3.11` Activation energy from a straight-line plot

$$\log k = \log A - \frac{E_a}{2.303\,R\,T}$$

| Symbol | Meaning | Unit |
|---|---|---|
| slope | $-E_a/2.303R$ | K |
| intercept | $\log A$ | dimensionless |
| $x$-axis | $1/T$ | K⁻¹ |

**Use it when:**

> A graph of $\log k$ against $1/T$ is given, or asked to be sketched.

**Trap:**

> The slope is **negative** and $E_a$ is positive — remember to take the magnitude when you convert slope to $E_a$.

##### ● `C3.12` Activation energy from two temperatures

$$\log\frac{k_2}{k_1} = \frac{E_a}{2.303\,R}\left[\frac{1}{T_1} - \frac{1}{T_2}\right] = \frac{E_a}{2.303\,R}\left[\frac{T_2 - T_1}{T_1 T_2}\right]$$

| Symbol | Meaning | Unit |
|---|---|---|
| $k_1, k_2$ | rate constants at $T_1$ and $T_2$ | same units |
| $E_a$ | activation energy | J mol⁻¹ |
| $T_1, T_2$ | absolute temperatures | K |

**Use it when:**

> Two rate constants at two temperatures are given. Also handles "the rate doubles when temperature rises by 10 K" — set $k_2/k_1 = 2$.

**Trap:**

> Inside the bracket it is $1/T_1 - 1/T_2$ — the **smaller** temperature first. Reversing it flips the sign of $E_a$.

#### `CH 4` d and f Block Elements — *2 formulas + rules · 11 marks*

*This chapter is mostly trends and reasons rather than calculation. Two things are computable; everything else is recall, collected in the rules table below.*

##### ● `C4.1` Magnetic moment from unpaired electrons — and back again

$$\mu = \sqrt{n(n+2)}\ \text{BM}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\mu$ | spin-only magnetic moment | BM (Bohr magneton) |
| $n$ | number of unpaired electrons | dimensionless |
| $n=1,2,3$ | gives $\mu = 1.73,\ 2.83,\ 3.87$ | BM |
| $n=4,5$ | gives $\mu = 4.90,\ 5.92$ | BM |

**Use it when:**

> Either direction: count unpaired electrons from the configuration and get $\mu$, or read $\mu$ off the question and work back to $n$. Same formula serves Chapter 5.

**Trap:**

> $n$ is unpaired electrons in the **ion**, not the atom. For a transition metal ion, remove the $4s$ electrons first, then the $3d$.

##### ○ `C4.2` General electronic configuration of each block

$$\text{d-block: } (n-1)d^{1-10}\,ns^{1-2} \qquad \text{lanthanoid: } 4f^{1-14}\,5d^{0-1}\,6s^{2} \qquad \text{actinoid: } 5f^{1-14}\,6d^{0-1}\,7s^{2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $n$ | period number | dimensionless |
| $\ce{Cr}$ | exception: $3d^5 4s^1$, half-filled is stabler | dimensionless |
| $\ce{Cu}$ | exception: $3d^{10} 4s^1$, fully-filled is stabler | dimensionless |

**Use it when:**

> Writing a configuration, or explaining why $\ce{Zn}$, $\ce{Cd}$ and $\ce{Hg}$ are not really transition metals — their $d$ subshell is full in both atom and ion.

**Trap:**

> Electrons fill $4s$ before $3d$ but are **removed from $4s$ first**. $\ce{Fe^2+}$ is $3d^6$, not $3d^4 4s^2$.

##### Rules, not formulas — recall these as facts

| Ask | Answer |
|---|---|
| Highest oxidation state in 3d series | $+7$ in $\ce{Mn}$ (as $\ce{KMnO4}$); $\ce{Cr}$ reaches $+6$ |
| Most stable oxidation state across the series | $+2$ for most, becoming more stable to the right |
| Why coloured | d–d transition of an unpaired $d$ electron; $\ce{Sc^3+}$ ($d^0$) and $\ce{Zn^2+}$ ($d^{10}$) are colourless |
| Lanthanoid contraction | Steady size decrease across 4f, from poor shielding by $f$ electrons |
| Its main consequence | Zr and Hf (also Nb/Ta) have almost identical radii and are hard to separate |
| Why alloys form readily | Similar atomic radii let one metal substitute for another in the lattice |
| Why good catalysts | Variable oxidation states and the ability to adsorb reactants on the surface |
| Most common lanthanoid oxidation state | $+3$; actinoids show far more variability |

#### `CH 5` Coordination Compounds — *6 formulas · 11 marks*

##### ● `C5.1` Oxidation number of the metal inside a complex

$$x + \sum(\text{ligand charges}) = \text{charge on the coordination sphere}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $x$ | oxidation number of the central metal | dimensionless |
| neutral | $\ce{NH3}$, $\ce{H2O}$, $\ce{CO}$, en — contribute 0 | dimensionless |
| anionic | $\ce{Cl^-}$, $\ce{CN^-}$, $\ce{OH^-}$ contribute $-1$; $\ce{C2O4^2-}$ contributes $-2$ | dimensionless |

**Use it when:**

> Always — it is the first step of every naming, VBT and CFT question. In $\ce{K4[Fe(CN)6]}$: $x + 6(-1) = -4$, so $x = +2$.

**Trap:**

> In $\ce{[Ni(CO)4]}$ the ligands are neutral and the sphere is neutral, so nickel is in oxidation state **zero**. This exact complex is the standing trap.

##### ● `C5.2` Coordination number when a ligand grips more than once

$$\text{CN} = \sum_{\text{ligands}} (\text{denticity}) = \text{number of donor atoms bonded to the metal}$$

| Symbol | Meaning | Unit |
|---|---|---|
| CN | coordination number | dimensionless |
| en | ethane-1,2-diamine — didentate, counts 2 | dimensionless |
| $\ce{C2O4^2-}$ | oxalate — didentate, counts 2 | dimensionless |
| EDTA | hexadentate, counts 6 | dimensionless |

**Use it when:**

> Working out geometry. $\ce{[Co(en)3]^3+}$ has three ligands but a coordination number of **6**.

**Trap:**

> Count **donor atoms**, not ligands. This is the difference between getting octahedral and getting the wrong geometry entirely.

##### ● `C5.3` Tetrahedral splitting compared with octahedral

$$\Delta_t = \frac{4}{9}\,\Delta_o$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Delta_o$ | octahedral crystal field splitting energy | J mol⁻¹ (or cm⁻¹) |
| $\Delta_t$ | tetrahedral splitting energy | J mol⁻¹ (or cm⁻¹) |

**Use it when:**

> Asked to relate the two, or to explain why tetrahedral complexes are essentially always high spin.

**Trap:**

> Because $\Delta_t$ is small, it is almost never bigger than the pairing energy — so **no low-spin tetrahedral complexes** in this syllabus. Also note the splitting is *inverted*: $e$ below $t_2$.

##### ○ `C5.4` Crystal field stabilisation energy of an octahedral complex

$$\text{CFSE} = \left(-0.4\,x + 0.6\,y\right)\Delta_o \qquad \text{for } t_{2g}^{\,x}\,e_g^{\,y}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $x$ | electrons in the lower $t_{2g}$ set | dimensionless |
| $y$ | electrons in the upper $e_g$ set | dimensionless |
| CFSE | crystal field stabilisation energy | J mol⁻¹ (or units of $\Delta_o$) |

**Use it when:**

> Comparing the stability of two configurations. Each $t_{2g}$ electron is stabilised by $0.4\Delta_o$; each $e_g$ electron is destabilised by $0.6\Delta_o$.

**Trap:**

> The barycentre must balance: $3\times 0.4 = 2\times 0.6$. If your two numbers do not satisfy that, you have the sets the wrong way round.

##### ● `C5.5` High spin or low spin — deciding which

$$\Delta_o \gt P \;\Rightarrow\; \text{low spin (pair up)} \qquad \Delta_o \lt P \;\Rightarrow\; \text{high spin (stay unpaired)}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Delta_o$ | crystal field splitting energy | J mol⁻¹ |
| $P$ | pairing energy | J mol⁻¹ |
| strong field | $\ce{CN^-}$, $\ce{CO}$, $\ce{NH3}$ — large $\Delta_o$, low spin | — |
| weak field | $\ce{I^-}$, $\ce{Br^-}$, $\ce{Cl^-}$, $\ce{F^-}$, $\ce{H2O}$ — small $\Delta_o$, high spin | — |

**Use it when:**

> Predicting magnetic behaviour or hybridisation. Only matters for $d^4$ to $d^7$; below and above that there is no choice to make.

**Trap:**

> Spectrochemical series, weakest to strongest: $\ce{I^- \lt Br^- \lt Cl^- \lt F^- \lt OH^- \lt H2O \lt NH3 \lt en \lt CN^- \lt CO}$.

##### ○ `C5.6` How many geometrical isomers a complex has

$$\ce{MA4B2},\ \ce{MA2B2}\text{(sq. planar)} \to 2 \quad(\text{cis, trans}) \qquad \ce{MA3B3} \to 2 \quad(\text{fac, mer})$$

| Symbol | Meaning | Unit |
|---|---|---|
| cis | identical ligands adjacent (90°) | — |
| trans | identical ligands opposite (180°) | — |
| fac | three identical ligands on one triangular face | — |
| mer | three identical ligands around a meridian | — |

**Use it when:**

> "What type of isomerism is shown by…" — check the formula shape first, then the geometry.

**Trap:**

> **Tetrahedral complexes show no geometrical isomerism** — every position is adjacent to every other, so there is no "trans". Only the **cis** form of $\ce{[M(en)2X2]}$ is optically active.

#### `CH 6` Haloalkanes and Haloarenes — *2 formulas + orders · 6 marks*

*An organic chapter, so almost everything is a reactivity order rather than an equation. The two computable things come first; the orders that actually earn the marks are collected below them.*

##### ● `C6.1` The rate law that identifies the substitution mechanism

$$S_N2:\ \ r = k\,[\ce{RX}][\ce{Nu^-}] \qquad\qquad S_N1:\ \ r = k\,[\ce{RX}]$$

| Symbol | Meaning | Unit |
|---|---|---|
| $S_N2$ | second order, one step, transition state, inversion | $k$ in L mol⁻¹ s⁻¹ |
| $S_N1$ | first order, two steps, carbocation, racemisation | $k$ in s⁻¹ |
| $[\ce{RX}]$ | concentration of the alkyl halide | mol L⁻¹ |

**Use it when:**

> Asked for two differences between the mechanisms, or told how the rate responds to changing the nucleophile's concentration.

**Trap:**

> The reactivity orders are **opposite**: $S_N2$ runs 1° > 2° > 3° (steric hindrance), $S_N1$ runs 3° > 2° > 1° (carbocation stability). Check which mechanism the question named before you answer.

##### ○ `C6.2` Degree of unsaturation from a molecular formula

$$\text{DoU} = \frac{2C + 2 + N - H - X}{2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $C, H, N$ | counts of carbon, hydrogen, nitrogen | dimensionless |
| $X$ | count of halogen atoms | dimensionless |
| DoU | rings plus π bonds | dimensionless |

**Use it when:**

> A molecular formula is given and you must decide how many isomers or what skeleton is possible. Oxygen is ignored — it does not change the count.

**Trap:**

> Halogen counts like hydrogen (subtract it). A benzene ring alone gives DoU = 4: three π bonds plus one ring.

##### The orders that earn the marks

| Comparison | Order, and the reason |
|---|---|
| Reactivity of $\ce{RX}$ to substitution | $\ce{RI \gt RBr \gt RCl \gt RF}$ — C–X bond weakens down the group |
| $S_N1$ rate | 3° > 2° > 1° — carbocation stability; benzylic and allylic beat all three |
| $S_N2$ rate | $\ce{CH3X}$ > 1° > 2° > 3° — steric hindrance |
| Alcohol + $\ce{HX}$ | 3° > 2° > 1°, and $\ce{HI \gt HBr \gt HCl}$ |
| Boiling point of isomers | Falls as branching rises — less surface contact, weaker van der Waals |
| Melting point of dihalobenzenes | para > ortho ≈ meta — para packs better in the crystal lattice |
| Free radical stability | benzylic ≈ allylic > 3° > 2° > 1° — resonance beats hyperconjugation |
| Aqueous vs alcoholic KOH | Aqueous → substitution (alcohol); alcoholic → elimination (alkene) |
| Markovnikov vs peroxide | Peroxide effect works with **$\ce{HBr}$ only** |
| Saytzeff (NCERT: Zaitsev) | The more substituted alkene is the major elimination product |

#### `CONST` Constants and conversions — *know the units too*

##### ● `K` Every constant this paper can hand you, with its unit

| Symbol | Meaning | Value and unit |
|---|---|---|
| $R$ | gas constant, energy form | 8.314 J K⁻¹ mol⁻¹ |
| $R$ | gas constant, pressure–volume form | 0.0821 L atm K⁻¹ mol⁻¹ |
| $F$ | Faraday constant | 96487 C mol⁻¹ |
| $K_b$ | ebullioscopic constant, water | 0.52 K kg mol⁻¹ |
| $K_f$ | cryoscopic constant, water | 1.86 K kg mol⁻¹ |
| $N_A$ | Avogadro constant | 6.022 × 10²³ mol⁻¹ |
| $2.303$ | converts $\ln$ to $\log_{10}$ | dimensionless |
| $0.693$ | $\ln 2$, for first-order half-life | dimensionless |
| $0.059$ | $2.303RT/F$ at 298 K, for Nernst | V |
| $T$ | 0 °C in kelvin | 273.15 K |
| STP | molar volume of an ideal gas | 22.4 L mol⁻¹ |

**Trap:**

> Match $R$ to the units you want out. Using 8.314 with pressures in atm, or 0.0821 when the answer should be in joules, is a whole-question error and not a rounding one.

Built from Sourabh Raina's one-shot and PYQ videos for Chapters 1–6, and cross-checked against NCERT Class XII Chemistry (Rationalised 2022–23). NCERT conventions used throughout: **0.059** rather than 0.0591 in the Nernst equation, $F = 96487\ \text{C mol}^{-1}$, molar conductivity in $\ce{S cm^2 mol^-1}$, and **Zaitsev** (which NCERT notes is "also pronounced as Saytzeff").

The six chapter pages carry the teaching and the past-year questions; this page is only the recall layer. Derivations for the formulas that have them live on the companion page, **Chemistry, Derived**.

### Chemistry, Derived

`Class XII CBSE · Chemistry · Chapters 1–3`

*Twelve derivations, one algebraic move per line, each with the reason it is allowed. Every one ends in a formula that is already on **Every Chemistry Formula** — the point of this page is that you can rebuild them when memory fails, and that you can write the proof out when the paper asks for it.*

- Derivations: 12

- Figures: 12

- Chapters: 3

- Marks covered: 42

##### How to use this

Chapters 4, 5 and 6 have no derivations worth the name — their marks come from recall and reasoning, and those live on the formula sheet. Everything derivable in this paper is on this page.

Read the **setup** first and draw the figure yourself before you look at the steps. A derivation you can only follow is not one you can write.

The *italic reason* beside a step is what turns it from an assertion into a proof. In the exam, those reasons are usually where the marks are.

#### `CH 3` Chemical Kinetics — *5 derivations · 13 marks*

##### `D1` Integrated rate law for a zero order reaction — *2–3 marks*

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

##### `D2` Half-life of a zero order reaction — *2 marks*

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

##### `D3` Integrated rate law for a first order reaction — *3 marks*

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

##### `D4` First order half-life, and why it ignores concentration — *2–3 marks*

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

##### `D5` Activation energy from rate constants at two temperatures — *3 marks*

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

#### `CH 2` Electrochemistry — *3 derivations · 14 marks*

##### `D6` The Nernst equation — *3 marks*

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

##### `D7` Equilibrium constant from standard cell potential — *2–3 marks*

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

##### `D8` Molar conductivity from conductivity — where the 1000 comes from — *2 marks*

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

#### `CH 1` Solutions — *4 derivations · 15 marks*

##### `D9` Relative lowering of vapour pressure equals the solute's mole fraction — *3 marks*

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

##### `D10` Elevation of boiling point is proportional to molality — *3 marks*

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

##### `D11` Depression of freezing point is proportional to molality — *3 marks*

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

##### `D12` Degree of dissociation from the van't Hoff factor — *2–3 marks*

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

## Part II — Physics

### Every Physics Formula

`Class XII CBSE · Physics · Chapters 1–9`

*Nine chapters, one hundred entries. Every one carries what its symbols mean and the SI unit it comes out in, because in physics a formula without its units is half a formula. The cue is on the outside and the formula is hidden, so you can read down a chapter and test yourself rather than just re-reading.*

- Entries: 100

- Chapters: 9

- Must be instant: 78

- Constants: 14

##### How to use this

**●** means it should arrive before you have finished reading the question. **○** means a few seconds is fine — these are the ones you reconstruct from a derivation rather than recall outright, and the companion page **Physics, Derived** shows how.

Each chapter opens with its own **recognise strip**: every cue in that chapter on one screen. Read the strip cold, name the formula, then tap the entry to check. That drill is worth more than re-reading the page.

Vector arrows are kept where the direction matters and dropped where only magnitude is asked. Where a symbol is overloaded across chapters — $L$ is length, inductance and angular momentum in three different chapters — the entry says which one it means.

#### `CH 1` Electric Charges and Fields — *13 entries*

Recognise strip — say it, then open the entry

- `P1.1` Charge is quantised, and conserved

- `P1.2` Force between two point charges

- `P1.3` The same force with a medium in the gap

- `P1.4` Force from several charges at once

- `P1.5` Field of a point charge, and what field means

- `P1.6` Charge spread along a line, over a surface, through a volume

- `P1.7` Dipole moment

- `P1.8` Field on the axis of a dipole

- `P1.9` Field on the equatorial line of a dipole

- `P1.10` Torque and energy of a dipole in a uniform field

- `P1.11` Electric flux, and Gauss's law

- `P1.12` Field of an infinite line charge and of a plane sheet

- `P1.13` Field of a charged spherical shell, inside and out

##### ● `P1.1` Charge is quantised, and conserved

$$q = \pm ne \qquad e = 1.6\times10^{-19}\ \text{C}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $q$ | charge on a body | C |
| $n$ | an integer — never a fraction | dimensionless |
| $e$ | elementary charge | 1.6 × 10⁻¹⁹ C |

**Use it when:**

> Asked how many electrons make up a given charge, or whether a stated charge is possible. $1\ \text{C}$ is about $6.25\times10^{18}$ elementary charges — which is why the coulomb is an impractically large unit.

**Trap:**

> Charge is also **conserved** and **additive**: it is a scalar, so charges add algebraically with their signs, never as vectors.

##### ● `P1.2` Force between two point charges

$$F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r^2} = k\frac{Q_1Q_2}{r^2} \qquad \vec F_{21} = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r_{12}^2}\hat r_{12}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $F$ | force between the charges | N |
| $k$ | $1/4\pi\varepsilon_0$ | 9 × 10⁹ N m² C⁻² |
| $\varepsilon_0$ | permittivity of free space | 8.854 × 10⁻¹² C² N⁻¹ m⁻² |
| $r$ | separation | m |

**Use it when:**

> Two charges, and a force. Coulomb's law. Valid only for **point charges** — separation much larger than the bodies themselves.

**Trap:**

> Unlike gravitation, this force **depends on the medium** and can be attractive or repulsive. $\vec F_{12} = -\vec F_{21}$ by Newton's third law even when the charges are unequal.

##### ○ `P1.3` The same force with a medium in the gap

$$F = \frac{1}{4\pi\varepsilon_0 K}\frac{Q_1Q_2}{r^2}, \qquad K = \varepsilon_r = \frac{\varepsilon}{\varepsilon_0}$$
          $$\text{partly filled: } F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{\left[(r-t)+\sqrt{K}\,t\right]^{2}}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $K$ | dielectric constant (relative permittivity) | dimensionless |
| $t$ | thickness of the dielectric slab | m |
| $\varepsilon$ | absolute permittivity of the medium | C² N⁻¹ m⁻² |

**Use it when:**

> The charges sit in water, oil or a slab rather than vacuum. A dielectric always **reduces** the force, since $K \gt 1$.

**Trap:**

> A slab of thickness $t$ behaves like $\sqrt{K}\,t$ of vacuum — the square root is easy to lose.

##### ● `P1.4` Force from several charges at once

$$\vec F_1 = \vec F_{12} + \vec F_{13} + \vec F_{14} + \cdots$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\vec F_{1j}$ | force on charge 1 from charge $j$ alone | N |
| $\vec F_1$ | resultant, by vector addition | N |

**Use it when:**

> Three or more charges. Principle of superposition: compute each pair as if the others were absent, then add as vectors.

**Trap:**

> Add as **vectors**, not magnitudes. For a null-point question, first decide whether the point lies between the charges (same signs) or outside, beyond the weaker one (opposite signs) — then solve.

##### ● `P1.5` Field of a point charge, and what field means

$$\vec E = \lim_{q_0\to0}\frac{\vec F}{q_0} \qquad \vec E = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\hat r \qquad \vec F = q\vec E$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\vec E$ | electric field intensity | N C⁻¹ or V m⁻¹ |
| $q_0$ | test charge, taken vanishingly small | C |
| $Q$ | source charge | C |

**Use it when:**

> Anything about field strength at a point. $E$ falls as $1/r^2$; to straighten the graph, plot $E$ against $1/r^2$.

**Trap:**

> The test charge cancels — $E$ is a property of the source and the point, not of what you probe it with. The limit exists so the probe does not disturb the field it measures.

##### ○ `P1.6` Charge spread along a line, over a surface, through a volume

$$\lambda = \frac{dq}{dl} \qquad \sigma = \frac{dq}{dS} \qquad \rho = \frac{dq}{dV}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\lambda$ | linear charge density | C m⁻¹ |
| $\sigma$ | surface charge density | C m⁻² |
| $\rho$ | volume charge density | C m⁻³ |

**Use it when:**

> The charge is continuous rather than a set of points — a charged wire, sheet or sphere. These are what turn a sum into an integral, and they feed straight into the Gauss's law applications.

**Trap:**

> On a **conductor** the charge sits entirely on the outer surface, so $\sigma$ is the relevant density even for a solid sphere.

##### ● `P1.7` Dipole moment

$$\vec p = Q \times 2\vec l$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\vec p$ | electric dipole moment | C m |
| $Q$ | magnitude of either charge | C |
| $2l$ | separation between the charges | m |

**Use it when:**

> Any dipole question. Direction is **from the negative charge to the positive one** — the opposite of the field it produces between them.

**Trap:**

> The separation is $2l$, not $l$. Losing the 2 halves every subsequent answer.

##### ● `P1.8` Field on the axis of a dipole

$$E_{\text{axial}} = \frac{1}{4\pi\varepsilon_0}\frac{2pr}{\left(r^2-l^2\right)^2} \;\xrightarrow{\;r \gg l\;}\; \frac{1}{4\pi\varepsilon_0}\frac{2p}{r^3}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $E_{\text{axial}}$ | field on the dipole's axis | N C⁻¹ |
| $r$ | distance from the dipole's centre | m |
| $p$ | dipole moment | C m |

**Use it when:**

> The point lies on the line through both charges. Direction is **parallel** to $\vec p$.

**Trap:**

> $1/r^3$, not $1/r^2$ — a dipole's field dies faster than a point charge's because the two charges nearly cancel.

##### ● `P1.9` Field on the equatorial line of a dipole

$$E_{\text{eq}} = \frac{1}{4\pi\varepsilon_0}\frac{p}{\left(r^2+l^2\right)^{3/2}} \;\xrightarrow{\;r \gg l\;}\; \frac{1}{4\pi\varepsilon_0}\frac{p}{r^3}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $E_{\text{eq}}$ | field on the perpendicular bisector | N C⁻¹ |
| $r$ | distance from the centre | m |

**Use it when:**

> The point is on the perpendicular bisector of the dipole.

**Trap:**

> Exactly **half** the axial field at the same distance, and pointing **antiparallel** to $\vec p$. Both the factor of two and the direction are asked.

##### ● `P1.10` Torque and energy of a dipole in a uniform field

$$\vec\tau = \vec p\times\vec E, \quad \tau = pE\sin\theta \qquad U = -\vec p\cdot\vec E = -pE\cos\theta$$
          $$W = pE\left(\cos\theta_1 - \cos\theta_2\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\tau$ | torque | N m |
| $U$ | potential energy of the dipole | J |
| $\theta$ | angle between $\vec p$ and $\vec E$ | rad or ° |

**Use it when:**

> A dipole is placed in a field and asked to rotate. Net **force** in a uniform field is zero — only a torque acts.

**Trap:**

> $\theta = 0$ is stable equilibrium ($U = -pE$, minimum); $\theta = 180°$ is unstable ($U = +pE$). Energy is measured from $\theta = 90°$, where $U = 0$.

##### ● `P1.11` Electric flux, and Gauss's law

$$\Phi = \vec E\cdot\vec A = EA\cos\theta \qquad \oint_S \vec E\cdot d\vec S = \frac{Q_{\text{enclosed}}}{\varepsilon_0}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Phi$ | electric flux | N m² C⁻¹ or V m |
| $\vec A$ | area vector, normal to the surface | m² |
| $Q_{\text{enc}}$ | net charge **inside** the closed surface | C |

**Use it when:**

> Symmetry lets you pick a Gaussian surface on which $E$ is constant — a sphere, a cylinder, a pillbox.

**Trap:**

> Only **enclosed** charge counts. A charge outside contributes zero net flux (what enters, leaves) — but it still contributes to $\vec E$ at every point on the surface.

##### ● `P1.12` Field of an infinite line charge and of a plane sheet

$$E_{\text{line}} = \frac{\lambda}{2\pi\varepsilon_0 r} \qquad E_{\text{sheet}} = \frac{\sigma}{2\varepsilon_0} \qquad E_{\text{conductor surface}} = \frac{\sigma}{\varepsilon_0}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\lambda$ | linear charge density | C m⁻¹ |
| $\sigma$ | surface charge density | C m⁻² |
| $r$ | perpendicular distance from the wire | m |

**Use it when:**

> A long charged wire, or a large charged plate. Both come straight out of Gauss's law.

**Trap:**

> The sheet field is **independent of distance** — and it is $\sigma/2\varepsilon_0$ for a thin sheet with field on both sides, but $\sigma/\varepsilon_0$ just outside a **conductor**, where the field exists on one side only. Confusing the two is the classic error.

##### ● `P1.13` Field of a charged spherical shell, inside and out

$$r \gt R:\ E = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2} \qquad r = R:\ E = \frac{\sigma}{\varepsilon_0} \qquad r \lt R:\ E = 0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $R$ | radius of the shell | m |
| $r$ | distance from the centre | m |
| $q$ | total charge on the shell | C |

**Use it when:**

> A hollow charged sphere or any charged conductor. Outside, it behaves exactly as if all the charge sat at the centre.

**Trap:**

> $E = 0$ inside but the **potential is not zero** — it is constant at the surface value. Zero field means no *change* in potential, not no potential.

#### `CH 2` Electrostatic Potential and Capacitance — *14 entries*

Recognise strip

- `P2.1` What potential and potential difference mean

- `P2.2` Potential from the field, and the field back from potential

- `P2.3` Potential of a point charge and of a system

- `P2.4` Potential due to a dipole at any point

- `P2.5` Potential of a charged spherical shell, inside and out

- `P2.6` Energy of a system of point charges

- `P2.7` Energy of a charge, and of a dipole, in an external field

- `P2.8` Capacitance, defined

- `P2.9` Parallel plate capacitor, with and without a dielectric

- `P2.10` A dielectric slab only partly filling the gap

- `P2.11` Spherical and cylindrical capacitors

- `P2.12` Capacitors in series and in parallel

- `P2.13` Energy stored in a capacitor, and energy density

- `P2.14` Two charged capacitors joined together

##### ● `P2.1` What potential and potential difference mean

$$V_A - V_B = \frac{W_{B\to A}}{q_0} \qquad V = \frac{W_{\infty\to P}}{q_0}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $V$ | electric potential | V (= J C⁻¹) |
| $W$ | work done by an **external** force, without acceleration | J |
| $q_0$ | test charge moved | C |

**Use it when:**

> Work, energy or volts are involved. Potential is a **scalar**, which is what makes it easier to work with than $\vec E$.

**Trap:**

> "Without acceleration" means the external force exactly balances the electric force, so no kinetic energy is gained. Convention: $V(\infty) = 0$.

##### ● `P2.2` Potential from the field, and the field back from potential

$$V = -\int_B^A \vec E\cdot d\vec l \qquad E = -\frac{dV}{dr} \qquad \oint \vec E\cdot d\vec l = 0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $E$ | field component along $r$ | V m⁻¹ |
| $dV/dr$ | potential gradient | V m⁻¹ |

**Use it when:**

> Converting between $E$ and $V$, or asked which of two points is at higher potential.

**Trap:**

> The minus sign says $\vec E$ points toward **decreasing** potential. The closed-loop integral being zero is the statement that the electrostatic field is **conservative**.

##### ● `P2.3` Potential of a point charge, and of a system

$$V = \frac{1}{4\pi\varepsilon_0}\frac{q}{r} \qquad V_P = \frac{1}{4\pi\varepsilon_0}\sum_i \frac{q_i}{r_i}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $V$ | potential at distance $r$ | V |
| $q_i$ | each charge, **with its sign** | C |
| $r_i$ | distance from each charge to the point | m |

**Use it when:**

> Potential at a point from one or several charges. Falls as $1/r$, unlike $E$'s $1/r^2$.

**Trap:**

> A **plain algebraic sum** — no vectors. Midway between $+q$ and $-q$, $V = 0$ but $\vec E \ne 0$. $V = 0$ never implies $E = 0$.

##### ○ `P2.4` Potential due to a dipole at any point

$$V = \frac{p\cos\theta}{4\pi\varepsilon_0\left(r^2 - l^2\cos^2\theta\right)} \;\xrightarrow{\;r\gg l\;}\; \frac{p\cos\theta}{4\pi\varepsilon_0 r^2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\theta$ | angle from the dipole axis | rad or ° |
| $p$ | dipole moment | C m |
| $r$ | distance from the dipole centre | m |

**Use it when:**

> A general point, not just axial or equatorial. Axial is $\theta = 0$; equatorial is $\theta = 90°$.

**Trap:**

> $V = 0$ everywhere on the **equatorial line** ($\cos 90° = 0$), even though $\vec E$ is not zero there. Potential of a dipole falls as $1/r^2$, faster than a point charge's $1/r$.

##### ● `P2.5` Potential of a charged spherical shell, inside and out

$$r \geq R:\ V = \frac{1}{4\pi\varepsilon_0}\frac{q}{r} \qquad r \lt R:\ V = V_{\text{surface}} = \frac{1}{4\pi\varepsilon_0}\frac{q}{R}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $R$ | radius of the shell | m |
| $V$ | potential | V |

**Use it when:**

> Any charged conductor. Sketching $V$ against $r$ is a standard question: flat inside, then $1/r$ outside.

**Trap:**

> **Constant** inside, not zero — even though $E = 0$ there. This pairs with P1.13 and the two are examined together.

##### ● `P2.6` Energy of a system of point charges

$$U = \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{12}} \qquad U = \frac{1}{4\pi\varepsilon_0}\left[\frac{q_1q_2}{r_{12}} + \frac{q_1q_3}{r_{13}} + \frac{q_2q_3}{r_{23}}\right]$$

| Symbol | Meaning | Unit |
|---|---|---|
| $U$ | potential energy of the assembled system | J |
| $r_{ij}$ | separation of each pair | m |

**Use it when:**

> "Work done in assembling" a set of charges. Sum over **every distinct pair**, once each.

**Trap:**

> Three charges give three pairs, not three terms of one charge each. Keep the signs — a mixed set can give negative $U$.

##### ○ `P2.7` Energy of a charge, and of a dipole, in an external field

$$U = qV(\vec r) \qquad U_{\text{dipole}} = -\vec p\cdot\vec E \qquad 1\ \text{eV} = 1.6\times10^{-19}\ \text{J}$$
          $$U_{\text{two charges in a field}} = q_1V(\vec r_1) + q_2V(\vec r_2) + \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{12}}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $V(\vec r)$ | potential of the external field at that point | V |
| $U$ | potential energy | J or eV |

**Use it when:**

> Charges are placed in a field produced by something else. The last term is the charges' mutual energy — easy to forget.

**Trap:**

> An electron-volt is an energy, not a voltage: the energy one elementary charge gains falling through 1 V.

##### ● `P2.8` Capacitance, defined

$$C = \frac{Q}{V} \qquad C_{\text{isolated sphere}} = 4\pi\varepsilon_0 R$$

| Symbol | Meaning | Unit |
|---|---|---|
| $C$ | capacitance | F (farad) |
| $Q$ | charge on either plate | C |
| $V$ | potential difference across it | V |

**Use it when:**

> Any capacitor question. $C$ depends only on geometry and the dielectric — never on $Q$ or $V$.

**Trap:**

> The farad is enormous; real capacitors are μF, nF or pF. $Q$ is the charge on **one** plate, the two being equal and opposite.

##### ● `P2.9` Parallel plate capacitor, with and without a dielectric

$$C = \frac{\varepsilon_0 A}{d} \qquad C_{\text{with dielectric}} = \frac{K\varepsilon_0 A}{d}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $A$ | area of one plate | m² |
| $d$ | plate separation | m |
| $K$ | dielectric constant | dimensionless |

**Use it when:**

> The standard capacitor. Inserting a dielectric multiplies $C$ by $K$.

**Trap:**

> What stays fixed depends on the circuit. **Battery connected** → $V$ fixed, so $Q$ rises. **Battery disconnected** → $Q$ fixed, so $V$ falls. Almost every dielectric question turns on this distinction.

##### ○ `P2.10` A dielectric slab only partly filling the gap

$$C = \frac{\varepsilon_0 A}{d - t + \dfrac{t}{K}} \qquad \text{several slabs: } C = \frac{\varepsilon_0 A}{\dfrac{t_1}{K_1}+\dfrac{t_2}{K_2}+\cdots}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $t$ | thickness of the slab | m |
| $d$ | plate separation | m |
| $K$ | dielectric constant of the slab | dimensionless |

**Use it when:**

> A slab thinner than the gap is slid in. Setting $t = d$ recovers $K\varepsilon_0A/d$; setting $K=1$ recovers $\varepsilon_0A/d$ — use those two checks.

**Trap:**

> The result does not depend on **where** in the gap the slab sits.

##### ○ `P2.11` Spherical and cylindrical capacitors

$$C_{\text{spherical}} = \frac{4\pi\varepsilon_0\,r_1r_2}{r_2-r_1} \qquad C_{\text{cylindrical}} = \frac{2\pi\varepsilon_0 L}{\ln(b/a)}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $r_1, r_2$ | inner and outer radii | m |
| $a, b$ | inner and outer cylinder radii | m |
| $L$ | length of the cylinder | m |

**Use it when:**

> Concentric shells or coaxial cylinders. Both are derived by integrating $E$ between the conductors to get $V$, then $C = Q/V$.

**Trap:**

> Here $L$ is a **length**. In Chapter 6 the same letter is self-inductance — check which chapter the question is in.

##### ● `P2.12` Capacitors in series and in parallel

$$\text{series: } \frac{1}{C_s} = \frac{1}{C_1}+\frac{1}{C_2}+\cdots \qquad \text{parallel: } C_p = C_1+C_2+\cdots$$

| Symbol | Meaning | Unit |
|---|---|---|
| series | same **charge**, voltages add | F |
| parallel | same **voltage**, charges add | F |

**Use it when:**

> A network of capacitors. Reduce it stepwise.

**Trap:**

> The rules are the **opposite way round** from resistors. Series capacitance is always smaller than the smallest one in the chain.

##### ● `P2.13` Energy stored in a capacitor, and energy density

$$U = \frac{1}{2}CV^2 = \frac{1}{2}QV = \frac{Q^2}{2C} \qquad u = \frac{1}{2}\varepsilon_0E^2$$

| Symbol | Meaning | Unit |
|---|---|---|
| $U$ | energy stored | J |
| $u$ | energy per unit volume of field | J m⁻³ |
| $E$ | field between the plates | V m⁻¹ |

**Use it when:**

> Energy, or work done in charging. Pick whichever of the three forms matches what the question gives you.

**Trap:**

> The factor of $\tfrac12$ is because $V$ rises from 0 to its final value as charge accumulates — the work is not simply $QV$.

##### ○ `P2.14` Two charged capacitors joined together

$$V_{\text{common}} = \frac{C_1V_1 + C_2V_2}{C_1+C_2} \qquad \Delta U = \frac{C_1C_2\left(V_1-V_2\right)^2}{2\left(C_1+C_2\right)}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $V_{\text{common}}$ | shared potential after connecting | V |
| $\Delta U$ | energy **lost** in the process | J |

**Use it when:**

> Two charged capacitors are connected plate to plate. Charge is conserved; energy is not.

**Trap:**

> Energy is **always lost** (the expression is a square), dissipated as heat and radiation in the connecting wires — even ideal ones. Being asked to explain that loss is common.

#### `CH 3` Current Electricity — *14 entries*

Recognise strip

- `P3.1` Current, and current density

- `P3.2` Drift velocity, and the current it produces

- `P3.3` Mobility

- `P3.4` Ohm's law, and resistance from dimensions

- `P3.5` Resistivity from what the electrons are doing

- `P3.6` Conductivity, and Ohm's law in microscopic form

- `P3.7` Resistance changing with temperature

- `P3.8` Resistors in series and parallel

- `P3.9` Emf, terminal voltage and internal resistance

- `P3.10` Cells combined in series and in parallel

- `P3.11` Electrical power and energy

- `P3.12` Kirchhoff's two rules

- `P3.13` Wheatstone bridge, and the metre bridge

- `P3.14` Potentiometer — comparing emfs and finding internal resistance

##### ● `P3.1` Current, and current density

$$I = \frac{Q}{t} = \frac{dQ}{dt} \qquad \vec J = \frac{I}{A}\hat n, \qquad I = \int_A \vec J\cdot d\vec A$$

| Symbol | Meaning | Unit |
|---|---|---|
| $I$ | current — a **scalar** | A |
| $\vec J$ | current density — a **vector** | A m⁻² |
| $A$ | cross-sectional area | m² |

**Use it when:**

> Charge flow. $1\ \text{A}$ is one coulomb per second.

**Trap:**

> Current is drawn with an arrow but is **not a vector** — it does not obey vector addition. Bending a wire does not change the current through it. Current density is the vector.

##### ● `P3.2` Drift velocity, and the current it produces

$$\vec v_d = -\frac{e\vec E}{m}\tau \qquad I = neAv_d$$

| Symbol | Meaning | Unit |
|---|---|---|
| $v_d$ | drift velocity | m s⁻¹ |
| $n$ | free electron number density | m⁻³ |
| $\tau$ | relaxation time between collisions | s |
| $e$ | electronic charge | 1.6 × 10⁻¹⁹ C |

**Use it when:**

> Linking the microscopic picture to the measured current.

**Trap:**

> Drift velocity is tiny — around $10^{-4}\ \text{m s}^{-1}$ — while random thermal speed is about $10^{5}\ \text{m s}^{-1}$. The lamp lights instantly because the **field** propagates at nearly $c$, not the electrons.

##### ○ `P3.3` Mobility

$$\mu = \frac{v_d}{E} = \frac{e\tau}{m}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\mu$ | mobility | m² V⁻¹ s⁻¹ |
| $m$ | mass of the charge carrier | kg |
| $\tau$ | relaxation time | s |

**Use it when:**

> Drift speed per unit field is asked, or comparing carriers in a semiconductor.

**Trap:**

> Defined as a positive magnitude even for electrons, which drift opposite to $\vec E$.

##### ● `P3.4` Ohm's law, and resistance from dimensions

$$V = IR \qquad R = \frac{\rho l}{A}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $R$ | resistance | Ω |
| $\rho$ | resistivity — a material property | Ω m |
| $l$ | length of the conductor | m |
| $A$ | cross-sectional area | m² |

**Use it when:**

> Almost every circuit question. Stretching a wire keeps its **volume** constant, so doubling the length quarters the area and quadruples $R$.

**Trap:**

> $R$ depends on the specimen's shape; $\rho$ does not. Ohm's law holds only for ohmic conductors at constant temperature.

##### ● `P3.5` Resistivity from what the electrons are doing

$$\rho = \frac{m}{ne^2\tau}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\rho$ | resistivity | Ω m |
| $n$ | free electron density | m⁻³ |
| $\tau$ | relaxation time | s |
| $m$ | electron mass | 9.1 × 10⁻³¹ kg |

**Use it when:**

> Explaining *why* resistance changes — the standard 3-mark derivation, and the basis of every temperature-dependence answer.

**Trap:**

> Heating a **metal** shortens $\tau$, so $\rho$ rises. Heating a **semiconductor** raises $n$ far more than it cuts $\tau$, so $\rho$ falls. Same formula, opposite behaviour.

##### ○ `P3.6` Conductivity, and Ohm's law in microscopic form

$$\sigma = \frac{1}{\rho} = \frac{ne^2\tau}{m} \qquad \vec J = \sigma\vec E$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\sigma$ | conductivity | S m⁻¹ |
| $\vec J$ | current density | A m⁻² |
| $\vec E$ | field inside the conductor | V m⁻¹ |

**Use it when:**

> Asked for Ohm's law in vector form, or to relate $J$ and $E$ without mentioning a circuit.

**Trap:**

> This $\sigma$ is conductivity. In Chapter 1 the same letter is surface charge density.

##### ● `P3.7` Resistance changing with temperature

$$R_t = R_0\left(1 + \alpha\,\Delta T\right) \qquad \alpha = \frac{R_t - R_0}{R_0\,\Delta T}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\alpha$ | temperature coefficient of resistance | K⁻¹ or °C⁻¹ |
| $R_0$ | resistance at the reference temperature | Ω |
| $\Delta T$ | temperature rise | K |

**Use it when:**

> A resistance is quoted at two temperatures.

**Trap:**

> $\alpha$ is **positive** for metals, **negative** for semiconductors and insulators, and nearly zero for alloys like nichrome and manganin — which is exactly why they are used for standard resistors.

##### ● `P3.8` Resistors in series and parallel

$$R_s = R_1+R_2+\cdots \qquad \frac{1}{R_p} = \frac{1}{R_1}+\frac{1}{R_2}+\cdots$$

| Symbol | Meaning | Unit |
|---|---|---|
| series | same **current**, voltages add | Ω |
| parallel | same **voltage**, currents add | Ω |

**Use it when:**

> Reducing any network. Two in parallel: $R_p = R_1R_2/(R_1+R_2)$.

**Trap:**

> The opposite of the capacitor rules. Parallel resistance is always **less** than the smallest resistor present.

##### ● `P3.9` Emf, terminal voltage and internal resistance

$$\mathcal{E} = V + Ir \qquad V = \mathcal{E} - Ir \qquad I = \frac{\mathcal{E}}{R+r}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\mathcal{E}$ | emf of the cell | V |
| $V$ | terminal potential difference | V |
| $r$ | internal resistance | Ω |

**Use it when:**

> A real cell is driving a circuit.

**Trap:**

> $V \lt \mathcal{E}$ while discharging, $V = \mathcal{E}$ only in open circuit, and $V \gt \mathcal{E}$ while the cell is being **charged** (current reversed).

##### ○ `P3.10` Cells combined in series and in parallel

$$\text{series: } I = \frac{N\mathcal{E}}{R+Nr} \qquad \text{parallel: } I = \frac{\mathcal{E}}{R + r/N}$$
          $$\text{two unequal cells: } \mathcal{E}_{eq} = \frac{\mathcal{E}_1r_2 + \mathcal{E}_2r_1}{r_1+r_2}, \qquad r_{eq} = \frac{r_1r_2}{r_1+r_2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $N$ | number of identical cells | dimensionless |
| $\mathcal{E}_{eq}$ | equivalent emf | V |
| $r_{eq}$ | equivalent internal resistance | Ω |

**Use it when:**

> A battery of cells. Series wins when $R \gg r$; parallel wins when $R \ll r$.

**Trap:**

> In series the internal resistances add too — which is why stacking cells does not raise the current indefinitely.

##### ● `P3.11` Electrical power and energy

$$P = VI = I^2R = \frac{V^2}{R} \qquad W = VIt \qquad 1\ \text{kWh} = 3.6\times10^{6}\ \text{J}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $P$ | power dissipated | W |
| $W$ | energy consumed | J or kWh |
| $t$ | time | s |

**Use it when:**

> Heating, power ratings, or an electricity bill.

**Trap:**

> Choose the right form. In **series** the current is shared so $P = I^2R$ applies and the largest resistor dissipates most; in **parallel** the voltage is shared so $P = V^2/R$ applies and the *smallest* resistor dissipates most.

##### ● `P3.12` Kirchhoff's two rules

$$\text{junction: } \sum I = 0 \qquad \text{loop: } \sum \Delta V = 0$$

| Symbol | Meaning | Unit |
|---|---|---|
| junction rule | conservation of **charge** | A |
| loop rule | conservation of **energy** | V |

**Use it when:**

> A network that series and parallel reduction cannot simplify. Naming which conservation law each rule expresses is usually worth a mark on its own.

**Trap:**

> Fix a sign convention before you start and keep it. Going through a resistor along the current gives $-IR$; entering a cell at its negative terminal gives $+\mathcal{E}$.

##### ● `P3.13` Wheatstone bridge, and the metre bridge

$$\frac{R_1}{R_2} = \frac{R_3}{R_4} \qquad \text{metre bridge: } X = \frac{R\,(100-l)}{l}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $X$ | unknown resistance | Ω |
| $R$ | known resistance in the other gap | Ω |
| $l$ | balancing length from the left end | cm |

**Use it when:**

> A galvanometer reads zero — the balance condition. At balance, no current flows through the galvanometer arm, so it can be removed entirely.

**Trap:**

> The bridge is most sensitive when all four resistances are comparable, which is why the balance point should sit near the middle of the wire.

##### ● `P3.14` Potentiometer — comparing emfs and finding internal resistance

$$V = Kl, \quad K = \frac{V}{L} \qquad \frac{\mathcal{E}_1}{\mathcal{E}_2} = \frac{l_1}{l_2} \qquad r = R\left(\frac{l_1 - l_2}{l_2}\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $K$ | potential gradient along the wire | V m⁻¹ or V cm⁻¹ |
| $l_1$ | balancing length with the cell open | cm |
| $l_2$ | balancing length with $R$ across the cell | cm |

**Use it when:**

> Comparing two emfs, or measuring internal resistance.

**Trap:**

> A potentiometer beats a voltmeter because at balance it draws **no current** from the cell, so it measures true emf rather than terminal voltage. Sensitivity improves with a **longer** wire — a smaller potential gradient.

#### `CH 4` Moving Charges and Magnetism — *12 entries*

Recognise strip

- `P4.1` Biot–Savart law

- `P4.2` Field at the centre of a circular loop

- `P4.3` Field on the axis of a circular loop

- `P4.4` Ampère's circuital law

- `P4.5` Field of a long straight wire

- `P4.6` Field inside a solenoid and a toroid

- `P4.7` Force on a moving charge, and the Lorentz force

- `P4.8` Radius and period of a charged particle's circular path

- `P4.9` Force on a current-carrying conductor

- `P4.10` Force between two parallel currents, and the ampere

- `P4.11` Torque on a current loop, and magnetic moment

- `P4.12` Galvanometer, and converting it to an ammeter or voltmeter

##### ● `P4.1` Biot–Savart law

$$dB = \frac{\mu_0}{4\pi}\frac{I\,dl\sin\theta}{r^2} \qquad d\vec B = \frac{\mu_0}{4\pi}\frac{I\,d\vec l\times\hat r}{r^2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $dB$ | field from one current element | T |
| $\mu_0$ | permeability of free space | 4π × 10⁻⁷ T m A⁻¹ |
| $dl$ | length of the current element | m |
| $\theta$ | angle between $d\vec l$ and $\hat r$ | rad or ° |

**Use it when:**

> Deriving the field of any current shape. The magnetic analogue of Coulomb's law.

**Trap:**

> $dB = 0$ straight ahead of the element ($\theta = 0$) and maximum sideways ($\theta = 90°$) — unlike the electric field, which is maximum along the line.

##### ● `P4.2` Field at the centre of a circular loop

$$B = \frac{\mu_0 I}{2R} \qquad \text{for } N \text{ turns: } B = \frac{\mu_0 NI}{2R}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $B$ | magnetic field at the centre | T |
| $R$ | radius of the loop | m |
| $N$ | number of turns | dimensionless |

**Use it when:**

> A circular coil and the field at its centre. For an arc subtending angle $\phi$ radians, multiply by $\phi/2\pi$.

**Trap:**

> Only for the **centre**. Off-axis needs P4.3, and $R$ is the radius, not the diameter.

##### ○ `P4.3` Field on the axis of a circular loop

$$B = \frac{\mu_0 I R^2}{2\left(R^2+x^2\right)^{3/2}} \qquad \text{for } N \text{ turns, multiply by } N$$

| Symbol | Meaning | Unit |
|---|---|---|
| $x$ | distance along the axis from the centre | m |
| $R$ | loop radius | m |

**Use it when:**

> The point is on the axis but not at the centre. Setting $x=0$ recovers P4.2 — use that as your check.

**Trap:**

> Far away ($x \gg R$) this becomes $\mu_0 \cdot 2M/4\pi x^3$ with $M = NIA$ — the loop behaves as a magnetic dipole.

##### ● `P4.4` Ampère's circuital law

$$\oint \vec B\cdot d\vec l = \mu_0 I_{\text{enclosed}}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $I_{\text{enc}}$ | current threading the closed loop | A |
| $d\vec l$ | element of the Amperian loop | m |

**Use it when:**

> Symmetry lets you choose a loop on which $B$ is constant — the magnetic counterpart of Gauss's law.

**Trap:**

> Only **enclosed** current counts, and only the component of $\vec B$ along the path contributes. In Chapter 8 this law gains a second term.

##### ● `P4.5` Field of a long straight wire

$$B = \frac{\mu_0 I}{2\pi r} \qquad \text{finite wire: } B = \frac{\mu_0 I}{4\pi r}\left(\sin\alpha_1 + \sin\alpha_2\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $r$ | perpendicular distance from the wire | m |
| $\alpha_1,\alpha_2$ | angles subtended by the wire's two ends | rad or ° |

**Use it when:**

> A straight current-carrying wire. Field lines are concentric circles; direction by the right-hand thumb rule.

**Trap:**

> $1/r$, not $1/r^2$. The infinite-wire form is the finite one with both angles at $90°$.

##### ● `P4.6` Field inside a solenoid and a toroid

$$B_{\text{solenoid}} = \mu_0 n I \qquad B_{\text{toroid}} = \mu_0 n I, \quad n = \frac{N}{2\pi r}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $n$ | turns per unit length | m⁻¹ |
| $N$ | total number of turns | dimensionless |
| $r$ | mean radius of the toroid | m |

**Use it when:**

> A long solenoid or a toroid. The field is uniform inside and essentially zero outside.

**Trap:**

> $n$ is turns per **metre**, not the total. At the **end** of a solenoid the field is half the interior value.

##### ● `P4.7` Force on a moving charge, and the Lorentz force

$$\vec F = q\left(\vec v\times\vec B\right) \qquad \vec F = q\vec E + q\left(\vec v\times\vec B\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\vec F$ | force on the charge | N |
| $\vec v$ | velocity | m s⁻¹ |
| $\vec B$ | magnetic field | T |

**Use it when:**

> A charge moves through a magnetic field. In a velocity selector the two forces balance, giving $v = E/B$.

**Trap:**

> The magnetic force is always perpendicular to $\vec v$, so it **does no work** and cannot change the particle's speed — only its direction. A charge at rest, or moving parallel to $\vec B$, feels no magnetic force at all.

##### ● `P4.8` Radius and period of a charged particle's circular path

$$r = \frac{mv}{qB} \qquad T = \frac{2\pi m}{qB} \qquad \omega = \frac{qB}{m}$$
          $$\text{pitch of the helix } p = v\cos\theta \cdot \frac{2\pi m}{qB}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $r$ | radius of the circular path | m |
| $T$ | period of revolution | s |
| $\omega$ | cyclotron angular frequency | rad s⁻¹ |

**Use it when:**

> A charge enters a field perpendicular to it. If it enters at an angle, the path is a helix and the pitch formula applies.

**Trap:**

> $T$ and $\omega$ are **independent of speed and radius** — that is the whole principle of the cyclotron.

##### ● `P4.9` Force on a current-carrying conductor

$$\vec F = I\left(\vec L\times\vec B\right), \qquad F = BIL\sin\theta$$

| Symbol | Meaning | Unit |
|---|---|---|
| $L$ | length of conductor in the field | m |
| $I$ | current | A |
| $\theta$ | angle between the conductor and $\vec B$ | rad or ° |

**Use it when:**

> A wire in a magnetic field. Direction by Fleming's left-hand rule.

**Trap:**

> Zero when the wire is **parallel** to the field, maximum when perpendicular. This is the same force as P4.7 summed over all the drifting charges.

##### ● `P4.10` Force between two parallel currents, and the ampere

$$\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi r} \qquad \text{for } I_1=I_2=1\ \text{A},\ r=1\ \text{m}: \frac{F}{L} = 2\times10^{-7}\ \text{N m}^{-1}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $F/L$ | force per unit length | N m⁻¹ |
| $r$ | separation of the wires | m |

**Use it when:**

> Two parallel wires. This relation is the **definition of the ampere** — quoting the $2\times10^{-7}$ case is the answer to "define the ampere".

**Trap:**

> Currents in the **same** direction **attract**; opposite directions repel. That is the reverse of what charges do, and it is asked.

##### ● `P4.11` Torque on a current loop, and magnetic moment

$$\vec\tau = \vec M\times\vec B, \qquad \tau = NIAB\sin\theta \qquad M = NIA$$

| Symbol | Meaning | Unit |
|---|---|---|
| $M$ | magnetic dipole moment | A m² |
| $A$ | area of the loop | m² |
| $N$ | number of turns | dimensionless |
| $\theta$ | angle between $\vec M$ and $\vec B$ | rad or ° |

**Use it when:**

> A coil in a magnetic field — the working principle of the motor and the galvanometer.

**Trap:**

> Torque is maximum when the coil's **plane** is parallel to $\vec B$ (so $\vec M$ is perpendicular to it), and zero when the plane is perpendicular. Net force is zero in a uniform field.

##### ● `P4.12` Galvanometer, and converting it to an ammeter or voltmeter

$$I = \frac{NBA}{k}\phi \qquad \text{shunt: } S = \frac{I_g G}{I - I_g} \qquad \text{series: } R = \frac{V}{I_g} - G$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\phi$ | deflection | rad or div |
| $k$ | torsional constant of the suspension | N m rad⁻¹ |
| $G$ | galvanometer resistance | Ω |
| $I_g$ | current for full-scale deflection | A |

**Use it when:**

> Sensitivity, or converting the meter. **Current sensitivity** is $NBA/k$; **voltage sensitivity** is $NBA/kG$.

**Trap:**

> Raising current sensitivity does **not** automatically raise voltage sensitivity — adding turns raises $N$ but also raises $G$. An ammeter needs a **small** shunt in parallel; a voltmeter needs a **large** resistance in series.

#### `CH 5` Magnetism and Matter — *9 entries*

Recognise strip

- `P5.1` Gauss's law for magnetism

- `P5.2` Magnetic moment of a bar magnet and of a coil

- `P5.3` Field of a bar magnet, axial and equatorial

- `P5.4` Torque, energy and work for a magnetic dipole

- `P5.5` A magnet oscillating in a field

- `P5.6` Earth's magnetic field and the angle of dip

- `P5.7` Magnetisation, magnetising field and susceptibility

- `P5.8` Permeability and its relation to susceptibility

- `P5.9` Curie's law, and the three kinds of magnetic material

##### ● `P5.1` Gauss's law for magnetism

$$\oint_S \vec B\cdot d\vec S = 0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\vec B$ | magnetic field | T |
| $d\vec S$ | element of any closed surface | m² |

**Use it when:**

> Asked why magnetic monopoles do not exist, or to contrast with the electric Gauss's law.

**Trap:**

> Always exactly zero, because magnetic field lines are **closed loops** — every line entering a surface leaves it. Cutting a magnet in half gives two magnets, never an isolated pole.

##### ● `P5.2` Magnetic moment of a bar magnet and of a coil

$$M = m \times 2l \qquad M = NIA$$

| Symbol | Meaning | Unit |
|---|---|---|
| $M$ | magnetic dipole moment | A m² or J T⁻¹ |
| $m$ | pole strength | A m |
| $2l$ | magnetic length | m |
| $N, I, A$ | turns, current, area of a coil | —, A, m² |

**Use it when:**

> Any dipole calculation. A current loop and a bar magnet are interchangeable once you know $M$.

**Trap:**

> Magnetic length is about $\tfrac{5}{6}$ of the geometric length of a bar magnet. Direction runs **S to N** inside the magnet.

##### ● `P5.3` Field of a bar magnet, axial and equatorial

$$B_{\text{axial}} = \frac{\mu_0}{4\pi}\frac{2M}{r^3} \qquad B_{\text{equatorial}} = \frac{\mu_0}{4\pi}\frac{M}{r^3}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $B$ | field at distance $r$ | T |
| $M$ | magnetic moment | A m² |
| $r$ | distance from the centre, $r \gg l$ | m |

**Use it when:**

> A short bar magnet, far from it. Identical in form to the electric dipole (P1.8, P1.9) with $\mu_0/4\pi$ replacing $1/4\pi\varepsilon_0$.

**Trap:**

> Axial is **twice** equatorial, and the two point in opposite senses. The same factor of 2 as in electrostatics.

##### ● `P5.4` Torque, energy and work for a magnetic dipole

$$\vec\tau = \vec M\times\vec B, \quad \tau = MB\sin\theta \qquad U = -\vec M\cdot\vec B$$
          $$W = MB\left(\cos\theta_1 - \cos\theta_2\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\tau$ | torque on the magnet | N m |
| $U$ | potential energy | J |
| $W$ | work to turn from $\theta_1$ to $\theta_2$ | J |

**Use it when:**

> A magnet is rotated in a field. Turning from aligned to fully reversed costs $W = 2MB$.

**Trap:**

> Structurally identical to the electric dipole (P1.10). $\theta = 0$ stable, $\theta = 180°$ unstable.

##### ○ `P5.5` A magnet oscillating in a field

$$T = 2\pi\sqrt{\frac{I}{MB}} \qquad B = \frac{4\pi^2 I}{MT^2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $T$ | period of oscillation | s |
| $I$ | moment of **inertia**, not current | kg m² |
| $M$ | magnetic moment | A m² |

**Use it when:**

> A magnet is displaced slightly and released — a vibration magnetometer. Small angles only, so that $\sin\theta \approx \theta$.

**Trap:**

> $I$ here is moment of inertia. For a bar of mass $m$ and length $L$ about its centre, $I = mL^2/12$.

##### ○ `P5.6` Earth's magnetic field and the angle of dip

$$B_H = B\cos\delta, \quad B_V = B\sin\delta \qquad \tan\delta = \frac{B_V}{B_H}, \quad B = \sqrt{B_H^2+B_V^2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $B_H$ | horizontal component | T |
| $B_V$ | vertical component | T |
| $\delta$ | angle of dip (inclination) | ° |

**Use it when:**

> Earth's field is resolved. The three elements are declination, dip and horizontal component.

**Trap:**

> $\delta = 0$ at the magnetic equator and $90°$ at the poles. At the equator the field is entirely horizontal, so a dip needle rests flat.

##### ○ `P5.7` Magnetisation, magnetising field and susceptibility

$$I = \frac{M}{V} \qquad \chi_m = \frac{I}{H} \qquad B = \mu_0\left(H + I\right) = \mu_0 H\left(1+\chi_m\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $I$ | intensity of magnetisation | A m⁻¹ |
| $H$ | magnetising field intensity | A m⁻¹ |
| $\chi_m$ | magnetic susceptibility | dimensionless |

**Use it when:**

> A material is placed in a field. $\chi_m$ is small and negative for diamagnetics, small and positive for paramagnetics, and very large for ferromagnetics.

**Trap:**

> This $I$ is magnetisation — the third meaning of the letter in this chapter, after current and moment of inertia. $H$ and $I$ share a unit; $B$ does not.

##### ○ `P5.8` Permeability and its relation to susceptibility

$$\mu = \mu_0\left(1+\chi_m\right) \qquad \mu_r = \frac{\mu}{\mu_0} = 1+\chi_m$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\mu$ | absolute permeability | T m A⁻¹ |
| $\mu_r$ | relative permeability | dimensionless |
| $\mu_0$ | permeability of free space | 4π × 10⁻⁷ T m A⁻¹ |

**Use it when:**

> Converting between susceptibility and permeability. $\mu_r \lt 1$ diamagnetic, slightly $\gt 1$ paramagnetic, $\gg 1$ ferromagnetic.

**Trap:**

> $\chi_m$ is dimensionless but $\mu$ is not — and $\mu_r$ is the one that has no unit.

##### ● `P5.9` Curie's law, and the three kinds of magnetic material

$$\chi_m = \frac{C}{T} \qquad \text{(paramagnetic; ferromagnetic above } T_C: \chi_m = \frac{C}{T-T_C})$$

| Symbol | Meaning | Unit |
|---|---|---|
| $C$ | Curie constant | K |
| $T$ | absolute temperature | K |
| $T_C$ | Curie temperature | K |

**Use it when:**

> Susceptibility against temperature. Heating randomises the aligned dipoles, so $\chi_m$ falls.

**Trap:**

> Above $T_C$ a ferromagnet becomes **paramagnetic**, not diamagnetic. Diamagnetism alone is **temperature-independent** — Curie's law does not apply to it.

#### `CH 6` Electromagnetic Induction — *9 entries*

Recognise strip

- `P6.1` Magnetic flux

- `P6.2` Faraday's law and Lenz's law

- `P6.3` Motional emf from a rod moving in a field

- `P6.4` A rod rotating about one end

- `P6.5` Charge that flows during a flux change

- `P6.6` Self-inductance, and that of a solenoid

- `P6.7` Mutual inductance of two coaxial solenoids

- `P6.8` Energy stored in an inductor, and magnetic energy density

- `P6.9` The AC generator

##### ● `P6.1` Magnetic flux

$$\Phi_B = \vec B\cdot\vec A = BA\cos\theta$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\Phi_B$ | magnetic flux | Wb (weber) |
| $A$ | area of the loop | m² |
| $\theta$ | angle between $\vec B$ and the area **normal** | rad or ° |

**Use it when:**

> Anything about induction — flux is the quantity whose change drives everything in this chapter.

**Trap:**

> $\theta$ is measured from the **normal** to the plane, not from the plane itself. A coil lying flat in a vertical field has $\theta = 0$ and maximum flux, not zero.

##### ● `P6.2` Faraday's law and Lenz's law

$$\varepsilon = -N\frac{d\Phi_B}{dt} \qquad I = \frac{\varepsilon}{R} = -\frac{N}{R}\frac{d\Phi_B}{dt}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\varepsilon$ | induced emf | V |
| $N$ | number of turns | dimensionless |
| $d\Phi_B/dt$ | rate of change of flux | Wb s⁻¹ |

**Use it when:**

> Flux changes for any reason — $B$ changing, $A$ changing, or the coil rotating.

**Trap:**

> The minus sign **is** Lenz's law: the induced current opposes the change that produced it. It is a consequence of **conservation of energy** — that is the answer when asked to justify it.

##### ● `P6.3` Motional emf from a rod moving in a field

$$\varepsilon = Blv \qquad I = \frac{Blv}{R}, \quad F = \frac{B^2l^2v}{R}, \quad P = \frac{B^2l^2v^2}{R}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $l$ | length of the rod in the field | m |
| $v$ | speed of the rod | m s⁻¹ |
| $F$ | opposing force needed to keep it moving | N |

**Use it when:**

> A conductor slides on rails. $B$, $l$ and $v$ must be mutually perpendicular.

**Trap:**

> Power applied equals power dissipated — the mechanical work done against the opposing force **is** the electrical energy produced. That equality is a favourite question.

##### ○ `P6.4` A rod rotating about one end

$$\varepsilon = \frac{1}{2}B\omega l^2$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\omega$ | angular velocity | rad s⁻¹ |
| $l$ | length of the rod | m |
| $\varepsilon$ | emf between centre and rim | V |

**Use it when:**

> A rod or disc spins in a perpendicular field.

**Trap:**

> The $\tfrac12$ comes from the average speed along the rod — the far end moves fastest, the pivot not at all. $\omega = 2\pi f$, so a rod at 50 rev/s has $\omega = 100\pi$.

##### ○ `P6.5` Charge that flows during a flux change

$$q = \frac{N\,\Delta\Phi_B}{R}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $q$ | total charge circulated | C |
| $\Delta\Phi_B$ | total change in flux | Wb |
| $R$ | total circuit resistance | Ω |

**Use it when:**

> Asked for charge rather than current — a magnet dropped through a coil, or a coil flipped over.

**Trap:**

> Independent of **how fast** the change happens. Flipping a coil through $180°$ changes flux by $2BA$, not $BA$.

##### ● `P6.6` Self-inductance, and that of a solenoid

$$N\Phi = LI \qquad \varepsilon = -L\frac{dI}{dt} \qquad L = \mu_0 n^2 A l = \frac{\mu_0 N^2 A}{l}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $L$ | self-inductance | H (henry) |
| $l$ | length of the solenoid | m |
| $n$ | turns per unit length, $N/l$ | m⁻¹ |
| $A$ | cross-sectional area | m² |

**Use it when:**

> A coil opposes a change in its own current — electrical inertia. A core of relative permeability $\mu_r$ multiplies $L$ by $\mu_r$.

**Trap:**

> Here $l$ is **length** and $L$ is **inductance** — the two are easy to collide. $L$ goes as $N^2$, so doubling the turns quadruples the inductance.

##### ○ `P6.7` Mutual inductance of two coaxial solenoids

$$\varepsilon_2 = -M\frac{dI_1}{dt} \qquad M = \frac{\mu_0 N_1 N_2 A}{l} \qquad M_{12} = M_{21}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $M$ | mutual inductance | H |
| $N_1, N_2$ | turns on each solenoid | dimensionless |
| $A$ | area of the **inner** solenoid | m² |

**Use it when:**

> Two coupled coils — the basis of the transformer.

**Trap:**

> Use the area of the **inner** coil, since that is all the flux the outer one links. $M_{12} = M_{21}$ always, however different the two coils are.

##### ● `P6.8` Energy stored in an inductor, and magnetic energy density

$$U = \frac{1}{2}LI^2 \qquad u = \frac{B^2}{2\mu_0}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $U$ | energy stored in the magnetic field | J |
| $u$ | energy per unit volume | J m⁻³ |
| $B$ | field inside the inductor | T |

**Use it when:**

> Energy in a coil. Exactly parallel to the capacitor: $\tfrac12 CV^2 \leftrightarrow \tfrac12 LI^2$, and $\tfrac12\varepsilon_0E^2 \leftrightarrow B^2/2\mu_0$.

**Trap:**

> Note $\mu_0$ is in the **denominator** for magnetic energy density, where $\varepsilon_0$ is in the numerator for electric.

##### ● `P6.9` The AC generator

$$\varepsilon = NAB\omega\sin(\omega t) = \varepsilon_0\sin(\omega t), \qquad \varepsilon_0 = NAB\omega$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\varepsilon_0$ | peak emf | V |
| $\omega$ | angular frequency of rotation, $2\pi f$ | rad s⁻¹ |
| $N, A, B$ | turns, coil area, field | —, m², T |

**Use it when:**

> A coil rotates in a uniform field. Converts mechanical energy into electrical.

**Trap:**

> Emf is **maximum** when the coil's plane is *parallel* to $\vec B$ (flux momentarily zero but changing fastest), and zero when the plane is perpendicular. The intuition runs backwards from most students' first guess.

#### `CH 7` Alternating Current — *11 entries*

Recognise strip

- `P7.1` RMS and mean values of an alternating quantity

- `P7.2` AC through a pure resistor

- `P7.3` AC through a pure inductor

- `P7.4` AC through a pure capacitor

- `P7.5` Series LCR — impedance and phase angle

- `P7.6` Resonance in a series LCR circuit

- `P7.7` Sharpness of resonance — the Q factor

- `P7.8` Average power, power factor and wattless current

- `P7.9` LC oscillations

- `P7.10` The transformer

- `P7.11` Why transformers lose energy

##### ● `P7.1` RMS and mean values of an alternating quantity

$$I_{\text{rms}} = \frac{i_0}{\sqrt2} \approx 0.707\,i_0 \qquad I_{\text{mean}} = \frac{2i_0}{\pi} \approx 0.637\,i_0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $i_0$ | peak current | A |
| $I_{\text{rms}}$ | root-mean-square (virtual) current | A |
| $I_{\text{mean}}$ | mean over a **half** cycle | A |

**Use it when:**

> Converting between peak and stated values. Mains "220 V" is the rms value, so the peak is about 311 V.

**Trap:**

> The mean over a **full** cycle is **zero** — which is exactly why rms exists. Every ammeter and voltmeter reads rms.

##### ● `P7.2` AC through a pure resistor

$$i = i_0\sin\omega t, \qquad i_0 = \frac{e_0}{R}, \qquad \phi = 0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\phi$ | phase difference between $V$ and $I$ | rad |
| $R$ | resistance | Ω |

**Use it when:**

> Only a resistor is present. Current and voltage are **in phase**.

**Trap:**

> Resistance does not depend on frequency, unlike both reactances.

##### ● `P7.3` AC through a pure inductor

$$X_L = \omega L = 2\pi f L \qquad i = i_0\sin\left(\omega t - \frac{\pi}{2}\right), \qquad i_0 = \frac{e_0}{X_L}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $X_L$ | inductive reactance | Ω |
| $L$ | inductance | H |
| $f$ | frequency | Hz |

**Use it when:**

> A coil in an AC circuit. Current **lags** voltage by $90°$.

**Trap:**

> $X_L \propto f$, so an inductor blocks high frequencies and passes DC ($f=0$, $X_L=0$) freely. It is a choke.

##### ● `P7.4` AC through a pure capacitor

$$X_C = \frac{1}{\omega C} = \frac{1}{2\pi f C} \qquad i = i_0\sin\left(\omega t + \frac{\pi}{2}\right), \qquad i_0 = \frac{e_0}{X_C}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $X_C$ | capacitive reactance | Ω |
| $C$ | capacitance | F |

**Use it when:**

> A capacitor in an AC circuit. Current **leads** voltage by $90°$.

**Trap:**

> $X_C \propto 1/f$, the opposite of the inductor: a capacitor blocks DC completely ($f=0$, $X_C \to \infty$) and passes high frequencies. Remember the order as **CIVIL** — in C, I leads V; V leads I in L.

##### ● `P7.5` Series LCR — impedance and phase angle

$$Z = \sqrt{R^2 + \left(X_L - X_C\right)^2} \qquad \tan\phi = \frac{X_L - X_C}{R} \qquad E = IZ$$

| Symbol | Meaning | Unit |
|---|---|---|
| $Z$ | impedance | Ω |
| $\phi$ | phase angle between $E$ and $I$ | rad or ° |
| $X_L, X_C$ | the two reactances | Ω |

**Use it when:**

> R, L and C in series. Found from the phasor diagram, where $V_L$ and $V_C$ are antiparallel so they subtract.

**Trap:**

> $X_L \gt X_C$ → inductive, current lags. $X_L \lt X_C$ → capacitive, current leads. Because $V_L$ and $V_C$ oppose, the voltage across one of them can **exceed the supply voltage** — which is not an error.

##### ● `P7.6` Resonance in a series LCR circuit

$$X_L = X_C \;\Rightarrow\; \omega_r = \frac{1}{\sqrt{LC}}, \qquad f_r = \frac{1}{2\pi\sqrt{LC}}$$
          $$\text{at resonance: } Z = R \text{ (minimum)}, \quad I = \frac{E}{R} \text{ (maximum)}, \quad \phi = 0$$

| Symbol | Meaning | Unit |
|---|---|---|
| $\omega_r$ | resonant angular frequency | rad s⁻¹ |
| $f_r$ | resonant frequency | Hz |

**Use it when:**

> The circuit is tuned — a radio receiver selecting a station.

**Trap:**

> At resonance the circuit is purely **resistive** and power factor is 1. Resonance only exists in a series circuit if both L and C are present — an RL or RC circuit never resonates.

##### ○ `P7.7` Sharpness of resonance — the Q factor

$$Q = \frac{\omega_r L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}} = \frac{\omega_r}{\Delta\omega}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $Q$ | quality factor | dimensionless |
| $\Delta\omega$ | bandwidth | rad s⁻¹ |
| $R$ | resistance in the circuit | Ω |

**Use it when:**

> Asked how sharply the circuit is tuned. High $Q$ means a narrow, selective peak.

**Trap:**

> $Q$ rises as $R$ **falls** — a low-resistance circuit is the sharply tuned one.

##### ● `P7.8` Average power, power factor and wattless current

$$P_{\text{avg}} = E_{\text{rms}}I_{\text{rms}}\cos\phi \qquad \text{power factor} = \cos\phi = \frac{R}{Z}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $P_{\text{avg}}$ | average power consumed | W |
| $\cos\phi$ | power factor | dimensionless |
| $Z$ | impedance | Ω |

**Use it when:**

> Power in any AC circuit. Only the resistance dissipates energy.

**Trap:**

> In a **pure** inductor or capacitor $\phi = 90°$, so $\cos\phi = 0$ and the average power is **zero** — the current is called **wattless**. Energy is stored and returned each quarter cycle, never consumed.

##### ○ `P7.9` LC oscillations

$$\frac{d^2q}{dt^2} + \frac{q}{LC} = 0 \qquad \omega = \frac{1}{\sqrt{LC}} \qquad U = \frac{q^2}{2C} + \frac{1}{2}Li^2 = \text{constant}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $q$ | charge on the capacitor | C |
| $\omega$ | angular frequency of oscillation | rad s⁻¹ |
| $U$ | total energy, constant if $R=0$ | J |

**Use it when:**

> A charged capacitor is connected across an inductor. Energy sloshes between the electric field of C and the magnetic field of L, exactly like a mass on a spring.

**Trap:**

> Undamped only in the idealised $R = 0$ case. Any real circuit has resistance, so the oscillations decay.

##### ● `P7.10` The transformer

$$\frac{\varepsilon_s}{\varepsilon_p} = \frac{N_s}{N_p} = \frac{I_p}{I_s} \qquad \text{ideal: } \varepsilon_p I_p = \varepsilon_s I_s$$

| Symbol | Meaning | Unit |
|---|---|---|
| $N_p, N_s$ | turns on primary and secondary | dimensionless |
| $\varepsilon_p, \varepsilon_s$ | primary and secondary voltages | V |
| $I_p, I_s$ | primary and secondary currents | A |

**Use it when:**

> Voltage is stepped up or down. Step-up means more secondary turns — and correspondingly **less** secondary current.

**Trap:**

> A transformer works on **AC only** — DC produces no changing flux, so no induced emf. It never creates energy: what it gains in voltage it loses in current.

##### ○ `P7.11` Why transformers lose energy

$$\eta = \frac{\text{output power}}{\text{input power}} \times 100\%$$

| Symbol | Meaning | Unit |
|---|---|---|
| flux leakage | not all primary flux links the secondary | — |
| copper loss | $I^2R$ heating in the windings | W |
| eddy currents | induced loops in the core — reduced by **laminating** it | W |
| hysteresis | repeated remagnetisation of the core | W |

**Use it when:**

> "State four energy losses in a transformer and how each is minimised" — a standing question with four recallable answers.

**Trap:**

> Each loss has its own remedy: thick copper wire for copper loss, a laminated core for eddy currents, a soft-iron core for hysteresis, and winding one coil over the other for flux leakage.

#### `CH 8` Electromagnetic Waves — *5 entries*

Recognise strip

- `P8.1` Displacement current

- `P8.2` Ampère–Maxwell law

- `P8.3` Speed of an electromagnetic wave

- `P8.4` The wave itself — fields, energy and momentum

- `P8.5` The electromagnetic spectrum, in order

##### ● `P8.1` Displacement current

$$I_d = \varepsilon_0\frac{d\Phi_E}{dt}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $I_d$ | displacement current | A |
| $\Phi_E$ | electric flux | V m |
| $\varepsilon_0$ | permittivity of free space | 8.854 × 10⁻¹² F m⁻¹ |

**Use it when:**

> A charging capacitor. It exists in the **gap between the plates**, where no charge flows, and is exactly equal to the conduction current in the wires.

**Trap:**

> It is not a flow of charge. Maxwell introduced it to fix an inconsistency in Ampère's law: two surfaces bounded by the same loop gave different answers, one passing through the wire and one through the gap.

##### ● `P8.2` Ampère–Maxwell law

$$\oint \vec B\cdot d\vec l = \mu_0\left(I_c + \varepsilon_0\frac{d\Phi_E}{dt}\right) = \mu_0\left(I_c + I_d\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $I_c$ | conduction current | A |
| $I_d$ | displacement current | A |

**Use it when:**

> Asked for the modified Ampère's law or to state Maxwell's equations. This is P4.4 with the new term added.

**Trap:**

> The consequence is the whole chapter: a changing electric field produces a magnetic field, and a changing magnetic field produces an electric field — so the two sustain each other and propagate as a wave.

##### ● `P8.3` Speed of an electromagnetic wave

$$c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = 3\times10^{8}\ \text{m s}^{-1} \qquad v = \frac{1}{\sqrt{\mu\varepsilon}} = \frac{c}{n}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $c$ | speed in vacuum | m s⁻¹ |
| $v$ | speed in a medium | m s⁻¹ |
| $n$ | refractive index of the medium | dimensionless |

**Use it when:**

> Asked why light is an electromagnetic wave — Maxwell's predicted speed matched the measured speed of light, which is what identified them.

**Trap:**

> Built from two constants measured in purely electric and magnetic experiments, with no light involved. That is what made the result so striking.

##### ● `P8.4` The wave itself — fields, energy and momentum

$$E_y = E_0\sin(\omega t - kx), \quad B_z = B_0\sin(\omega t - kx), \quad k = \frac{2\pi}{\lambda}$$
          $$c = \frac{E_0}{B_0} \qquad p = \frac{U}{c} \qquad u_{\text{avg}} = \frac{1}{2}\varepsilon_0E_0^2 = \frac{B_0^2}{2\mu_0}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $E_0, B_0$ | peak field amplitudes | V m⁻¹, T |
| $k$ | wave number | m⁻¹ |
| $p$ | momentum delivered | kg m s⁻¹ |
| $U$ | energy delivered | J |

**Use it when:**

> Given one field amplitude and asked for the other, or asked about radiation pressure.

**Trap:**

> $\vec E$, $\vec B$ and the direction of propagation are **mutually perpendicular**, in that order, and the two fields are **in phase**. Energy is shared equally between them. For a *totally reflecting* surface the momentum delivered is $2U/c$.

##### ● `P8.5` The electromagnetic spectrum, in order

$$c = f\lambda \qquad E = hf$$

| Symbol | Meaning | Unit |
|---|---|---|
| order | radio → microwave → infrared → visible → UV → X-ray → γ-ray | — |
| $\lambda$ | decreases along that order | m |
| $f$, $E$ | increase along that order | Hz, J |
| visible | about 400 nm (violet) to 700 nm (red) | nm |

**Use it when:**

> Ordering by wavelength or frequency, or naming a source and use. Radio from oscillating circuits; microwaves from klystrons, used in radar and ovens; infrared from hot bodies, used in therapy and remote controls; UV from the sun and arcs; X-rays from decelerating electrons; γ-rays from nuclei.

**Trap:**

> All travel at the **same speed** $c$ in vacuum. Only wavelength and frequency differ, and they always move in opposite directions along the list.

#### `CH 9` Ray Optics and Optical Instruments — *12 entries*

*Written from NCERT and the published **Ray Optics to 9.4** page. The lecture transcripts for this chapter are not yet processed, so the emphasis here follows the textbook rather than the teacher; it will be revisited once those are in.*

Recognise strip

- `P9.1` Mirror formula and magnification

- `P9.2` Focal length from radius of curvature

- `P9.3` Snell's law and refractive index

- `P9.4` Real depth, apparent depth and the shift

- `P9.5` Critical angle and total internal reflection

- `P9.6` Refraction at a single spherical surface

- `P9.7` Lens maker's formula

- `P9.8` Thin lens formula and magnification

- `P9.9` Power of a lens, and lenses in contact

- `P9.10` Refraction through a prism

- `P9.11` Magnifying power of a simple and compound microscope

- `P9.12` Magnifying power of a telescope

##### ● `P9.1` Mirror formula and magnification

$$\frac{1}{v} + \frac{1}{u} = \frac{1}{f} \qquad m = \frac{h'}{h} = -\frac{v}{u} = \frac{f}{f-u} = \frac{f-v}{f}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $u$ | object distance, from the pole | m |
| $v$ | image distance | m |
| $f$ | focal length | m |
| $m$ | linear magnification | dimensionless |

**Use it when:**

> Any spherical mirror. All distances are measured from the **pole** under the New Cartesian convention.

**Trap:**

> Note the **plus** sign between $1/v$ and $1/u$ — the lens formula has a minus. Negative $m$ means real and inverted; concave $f$ is negative, convex $f$ positive.

##### ● `P9.2` Focal length from radius of curvature

$$f = \frac{R}{2}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $R$ | radius of curvature | m |
| $f$ | focal length | m |

**Use it when:**

> A mirror is described by its radius rather than its focal length.

**Trap:**

> Holds for **small aperture** only, and for mirrors — not for lenses, where the lens maker's formula applies instead.

##### ● `P9.3` Snell's law and refractive index

$$\frac{\sin i}{\sin r} = {}_1n_2 = \frac{n_2}{n_1} \quad\Longleftrightarrow\quad n_1\sin i = n_2\sin r$$
          $$n = \frac{c}{v} = \frac{\lambda_{\text{air}}}{\lambda_{\text{medium}}} \qquad {}_1n_2 = \frac{1}{{}_2n_1}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $i, r$ | angles of incidence and refraction | ° |
| $n$ | refractive index | dimensionless |
| $v$ | speed of light in the medium | m s⁻¹ |

**Use it when:**

> Light crosses a boundary. Some papers write $\mu$ instead of $n$ — same quantity.

**Trap:**

> **Frequency does not change** on refraction — it is fixed by the source. Since $v = f\lambda$, it is the wavelength that shortens in the denser medium.

##### ● `P9.4` Real depth, apparent depth and the shift

$$n = \frac{\text{real depth}}{\text{apparent depth}} \qquad \text{shift } x = t\left(1 - \frac{1}{n}\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $t$ | real depth or slab thickness | m |
| $x$ | apparent shift | m |
| $n$ | refractive index of the denser medium | dimensionless |

**Use it when:**

> A coin in water, a pin under a glass slab, a pool that looks shallower than it is.

**Trap:**

> Valid for **near-normal viewing** only. The shift does not depend on where the slab sits between object and eye.

##### ● `P9.5` Critical angle and total internal reflection

$$\sin C = \frac{n_{\text{rarer}}}{n_{\text{denser}}} = \frac{1}{n} \qquad C = \sin^{-1}\left(\frac{1}{n}\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $C$ | critical angle | ° |
| $n$ | index of the denser medium w.r.t. the rarer | dimensionless |

**Use it when:**

> Optical fibres, mirages, the brilliance of diamond ($C \approx 24°$), totally reflecting prisms.

**Trap:**

> Two conditions, both required: light must travel **denser to rarer**, and $i$ must **exceed** $C$. Since $n$ is larger for violet, violet has the smallest $C$ and is totally reflected first.

##### ○ `P9.6` Refraction at a single spherical surface

$$\frac{n_2}{v} - \frac{n_1}{u} = \frac{n_2-n_1}{R}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $n_1$ | index of the medium the light starts in | dimensionless |
| $n_2$ | index of the medium it enters | dimensionless |
| $R$ | radius of curvature of the surface | m |

**Use it when:**

> One curved refracting surface. Applying it twice, once at each face, is what produces the lens maker's formula.

**Trap:**

> Distances are measured from the **pole of the surface**, and the sign convention still applies to $R$.

##### ● `P9.7` Lens maker's formula

$$\frac{1}{f} = (n-1)\left(\frac{1}{R_1} - \frac{1}{R_2}\right)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $n$ | index of the lens w.r.t. the surrounding medium | dimensionless |
| $R_1$ | radius of the first surface met | m |
| $R_2$ | radius of the second surface | m |

**Use it when:**

> Focal length from the lens's shape and material, or explaining what happens when a lens is moved into water.

**Trap:**

> It is $n$ **relative to the surroundings**. A glass lens ($n=1.5$) in water ($n=1.33$) has a much longer focal length; if the surrounding medium had the same index as the lens, $f$ would be infinite and the lens would vanish optically.

##### ● `P9.8` Thin lens formula and magnification

$$\frac{1}{v} - \frac{1}{u} = \frac{1}{f} \qquad m = \frac{h'}{h} = \frac{v}{u}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $u, v$ | object and image distances from the optical centre | m |
| $f$ | focal length — positive convex, negative concave | m |
| $m$ | magnification | dimensionless |

**Use it when:**

> Any thin lens.

**Trap:**

> **Minus** for lenses, **plus** for mirrors — and the magnification is $+v/u$ for a lens but $-v/u$ for a mirror. Both differences are exam-critical.

##### ● `P9.9` Power of a lens, and lenses in contact

$$P = \frac{1}{f\ \text{in metres}} \qquad P = P_1 + P_2 + \cdots \qquad \frac{1}{F} = \frac{1}{f_1}+\frac{1}{f_2}+\cdots$$

| Symbol | Meaning | Unit |
|---|---|---|
| $P$ | power of the lens | D (dioptre) |
| $f$ | focal length — **must be in metres** | m |
| $F$ | focal length of the combination | m |

**Use it when:**

> Spectacle prescriptions, or two lenses stuck together.

**Trap:**

> $f$ in **metres**, not centimetres — a 20 cm lens is 5 D, not 0.05 D. Converging power is positive, diverging negative.

##### ● `P9.10` Refraction through a prism

$$A + \delta = i + e \qquad r_1 + r_2 = A \qquad n = \frac{\sin\left(\dfrac{A+\delta_m}{2}\right)}{\sin\left(\dfrac{A}{2}\right)}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $A$ | angle of the prism | ° |
| $\delta$ | angle of deviation | ° |
| $\delta_m$ | minimum deviation | ° |
| $i, e$ | angles of incidence and emergence | ° |

**Use it when:**

> A prism. At minimum deviation the ray passes **symmetrically**: $i = e$ and $r_1 = r_2 = A/2$.

**Trap:**

> For a **thin** prism the formula simplifies to $\delta = (n-1)A$. The graph of $\delta$ against $i$ is a curve with a single minimum, not a straight line.

##### ● `P9.11` Magnifying power of a simple and compound microscope

$$\text{simple: } m = 1 + \frac{D}{f} \ \text{(image at }D) \qquad m = \frac{D}{f}\ \text{(image at }\infty)$$
          $$\text{compound: } m = \frac{v_o}{u_o}\left(1+\frac{D}{f_e}\right) \approx \frac{L}{f_o}\cdot\frac{D}{f_e}$$

| Symbol | Meaning | Unit |
|---|---|---|
| $D$ | least distance of distinct vision | 25 cm |
| $f_o, f_e$ | focal lengths of objective and eyepiece | m or cm |
| $L$ | tube length (separation of the lenses) | m or cm |

**Use it when:**

> A magnifier or a microscope. High magnification needs **both** focal lengths short.

**Trap:**

> Two cases for every instrument — image at $D$ (relaxed formula has the $1+$) and image at infinity (no $1+$). Read which the question wants.

##### ● `P9.12` Magnifying power of a telescope

$$m = \frac{f_o}{f_e} \ \text{(normal adjustment)}, \quad L = f_o + f_e \qquad m = \frac{f_o}{f_e}\left(1+\frac{f_e}{D}\right)\ \text{(image at }D)$$

| Symbol | Meaning | Unit |
|---|---|---|
| $f_o$ | objective focal length — **long** | m or cm |
| $f_e$ | eyepiece focal length — **short** | m or cm |
| $L$ | length of the telescope | m or cm |

**Use it when:**

> An astronomical telescope. A large objective also gathers more light, improving resolution and brightness.

**Trap:**

> Exactly the **opposite** requirement from a microscope: the telescope objective wants a **long** focal length, the microscope objective a short one. A reflecting telescope replaces the objective lens with a concave mirror, avoiding chromatic aberration entirely.

#### `CONST` Constants and conversions — *know the units too*

##### ● `K` Every constant this paper can hand you, with its unit

| Symbol | Meaning | Value and unit |
|---|---|---|
| $e$ | elementary charge | 1.6 × 10⁻¹⁹ C |
| $m_e$ | electron mass | 9.1 × 10⁻³¹ kg |
| $\varepsilon_0$ | permittivity of free space | 8.854 × 10⁻¹² F m⁻¹ |
| $1/4\pi\varepsilon_0$ | Coulomb constant | 9 × 10⁹ N m² C⁻² |
| $\mu_0$ | permeability of free space | 4π × 10⁻⁷ T m A⁻¹ |
| $\mu_0/4\pi$ | the form used in Biot–Savart | 10⁻⁷ T m A⁻¹ |
| $c$ | speed of light in vacuum | 3 × 10⁸ m s⁻¹ |
| $h$ | Planck constant | 6.63 × 10⁻³⁴ J s |
| $k_B$ | Boltzmann constant | 1.38 × 10⁻²³ J K⁻¹ |
| $\mu_B$ | Bohr magneton | 9.27 × 10⁻²⁴ A m² |
| 1 eV | electron-volt | 1.6 × 10⁻¹⁹ J |
| 1 kWh | unit of electrical energy | 3.6 × 10⁶ J |
| $D$ | least distance of distinct vision | 25 cm |
| $B_E$ | Earth's magnetic field, order of magnitude | ~10⁻⁵ T |

**Trap:**

> Watch the letters that mean different things in different chapters: $L$ is length (Ch 2, 4), self-inductance (Ch 6) and tube length (Ch 9); $I$ is current, moment of inertia (Ch 5) and magnetisation (Ch 5); $\sigma$ is surface charge density (Ch 1) and conductivity (Ch 3); $\mu$ is mobility (Ch 3) and permeability (Ch 5).

Built from the notes for Chapters 1–8 in this repository, which were themselves grounded against the lecture board frames rather than the ASR transcripts — the extracted NCERT text flattens equations during PDF conversion and is unreliable for them, so NCERT was used here only for units, constants and symbol names. Chapter 9 is written from NCERT and from the published **Ray Optics to 9.4** page, pending processing of that chapter's eighteen lecture videos.

Derivations for the entries marked ○, and for many marked ●, are on the companion page **Physics, Derived**.

### Physics, Derived

`Class XII CBSE · Physics · Chapters 1–9`

*Every derivation the paper can ask for, written one algebraic move per line with the reason each move is allowed — and every one with a real drawn figure, because in physics the diagram is usually where the marks start and where a half-remembered derivation falls apart.*

- Derivations: 45

- Figures: 45

- Chapters: 9

- Longest: 5 marks

##### How to use this

**Draw the figure first, from the setup paragraph, before you read a single step.** In every board exam the diagram carries marks of its own, and a derivation written without one rarely scores full even when the algebra is right.

The *italic reason* beside a step — *vertically opposite*, *small aperture, so N ≈ P*, *divide throughout by uvf* — is what makes it a proof rather than a list of equations. Those clauses are where examiners look.

Where two derivations share an opening, a dashed **shared setup** note says so. Those pairs are worth learning together: get one and the second costs almost nothing.

#### `CH 1` Electric Charges and Fields — *6 derivations*

##### `PD1` Electric field on the axis of a dipole — *3 marks*

> A dipole of charges $-q$ at A and $+q$ at B, separated by $2l$, with centre O. The point P lies on the axis, on the $+q$ side, at distance $r$ from O. So P is $(r-l)$ from $+q$ and $(r+l)$ from $-q$. Both fields point along the axis, so this is a scalar subtraction, not a vector sum.

**Figure.** A dipole on a horizontal axis: minus q on the left, plus q on the right, separated by 2l about the centre O. A point P lies further right on the same axis at distance r from O. The field from plus q points right and is larger; the field from minus q points left and is smaller.

*P is nearer the $+q$ charge, so $E_+$ is the larger of the two and the resultant points away from the dipole, parallel to $\vec p$.*

1. $E_{+} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{(r-l)^2}$, directed from B towards P  — *(field of a point charge, P is $(r-l)$ from $+q$)*
2. $E_{-} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{(r+l)^2}$, directed from P towards A  — *(P is $(r+l)$ from $-q$)*
3. Both lie along the same line in opposite senses, so $E = E_+ - E_-$  — *(no vector resolution needed on the axis)*
4. $E = \dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{1}{(r-l)^2} - \dfrac{1}{(r+l)^2}\right]$
5. $= \dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{(r+l)^2 - (r-l)^2}{(r^2-l^2)^2}\right]$  — *(common denominator, using $(r-l)(r+l) = r^2-l^2$)*
6. $(r+l)^2 - (r-l)^2 = 4rl$  — *(difference of two squares)*
7. $E = \dfrac{q}{4\pi\varepsilon_0}\dfrac{4rl}{(r^2-l^2)^2}$
8. $p = q \times 2l$, so $q \times 4rl = 2pr$  — *(introducing the dipole moment)*
9. $E_{\text{axial}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2pr}{(r^2-l^2)^2}$
10. For a **short** dipole, $r \gg l$, so $r^2 - l^2 \approx r^2$  — *(the standard approximation — say it explicitly)*
11. $E_{\text{axial}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2p}{r^3}$

**Result:** $E_{\text{axial}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2p}{r^{3}}$, directed **parallel** to $\vec p$

*$1/r^3$, not $1/r^2$: the two charges almost cancel, so a dipole's field dies faster than a single charge's.*

##### `PD2` Electric field on the equatorial line of a dipole — *3 marks*

> The same dipole, but P now sits on the perpendicular bisector, at distance $r$ from the centre O. Both charges are the same distance $\sqrt{r^2+l^2}$ away, so the two fields have equal magnitude — but they point in different directions, so this one *does* need resolution into components.

> **Shared setup with PD1.** Same dipole, same symbols; only the position of P changes. Draw one figure and move P, and you have both derivations.

**Figure.** A dipole on a horizontal axis with point P on the perpendicular bisector above the centre. The field from plus q points away along BP and the field from minus q points towards A along PA; their vertical components cancel and their horizontal components add, giving a resultant antiparallel to the dipole moment.

*The two fields are equal in size. Their components perpendicular to the axis cancel; the components along the axis both point from $+q$ towards $-q$, so they add — and the resultant is **antiparallel** to $\vec p$.*

1. $AP = BP = \sqrt{r^2+l^2}$  — *(P is on the perpendicular bisector)*
2. $E_{+} = E_{-} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2+l^2}$  — *(equal distances, equal magnitudes)*
3. Resolve each into a component along the axis and one perpendicular to it
4. The perpendicular components are equal and opposite, so they cancel  — *(this is why the resultant is parallel to the axis)*
5. $E = E_+\cos\theta + E_-\cos\theta = 2E_+\cos\theta$  — *(the axial components add)*
6. $\cos\theta = \dfrac{l}{\sqrt{r^2+l^2}}$  — *(from the right triangle AOP)*
7. $E = 2\cdot\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2+l^2}\cdot\dfrac{l}{\sqrt{r^2+l^2}}$
8. $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{2ql}{\left(r^2+l^2\right)^{3/2}}$
9. $p = q\times2l$, so $2ql = p$
10. $E_{\text{eq}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{p}{\left(r^2+l^2\right)^{3/2}}$
11. Short dipole, $r \gg l$: $\left(r^2+l^2\right)^{3/2} \approx r^3$
12. $E_{\text{eq}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{p}{r^3}$

**Result:** $E_{\text{eq}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{p}{r^{3}}$, directed **antiparallel** to $\vec p$ — exactly half the axial field

##### `PD3` Torque on a dipole in a uniform electric field — *2–3 marks*

> A dipole of length $2l$ placed in a uniform field $\vec E$, with its axis at angle $\theta$ to the field. Each charge feels a force $qE$ — equal in size, opposite in direction. Since the field is uniform, these forces do not translate the dipole; they form a couple.

**Figure.** A dipole tilted at angle theta in a uniform horizontal field: force qE acts rightwards on the plus charge and leftwards on the minus charge, forming a couple whose arm is 2l sine theta, the perpendicular distance between the two lines of action.

*Two equal, opposite, non-collinear forces — a couple. Its moment is one force times the perpendicular distance between their lines of action, which the geometry gives as $2l\sin\theta$.*

1. Force on $+q$ is $qE$ along $\vec E$; force on $-q$ is $qE$ opposite to $\vec E$
2. Net force $= qE - qE = 0$  — *(the field is uniform, so the dipole does not translate)*
3. The two forces are equal, opposite and **not collinear**, so they form a couple
4. Torque of a couple $=$ (one force) $\times$ (perpendicular distance between the lines of action)
5. Perpendicular distance $= 2l\sin\theta$  — *(from the right triangle in the figure)*
6. $\tau = qE \times 2l\sin\theta$
7. $p = q\times 2l$
8. $\tau = pE\sin\theta$
9. In vector form, $\vec\tau = \vec p\times\vec E$  — *(the cross product carries both the $\sin\theta$ and the direction)*

**Result:** $\vec\tau = \vec p\times\vec E, \qquad \tau = pE\sin\theta$

*Maximum at $\theta = 90°$, zero at $\theta = 0$ and $180°$. Work done rotating from $\theta_1$ to $\theta_2$ is $W = pE(\cos\theta_1 - \cos\theta_2)$, giving $U = -\vec p\cdot\vec E$ with $U=0$ taken at $90°$.*

##### `PD4` Field of an infinite straight charged wire, by Gauss's law — *3 marks*

> An infinitely long straight wire carrying uniform linear charge density $\lambda$. By symmetry the field must point radially outward and have the same magnitude everywhere at distance $r$. Choose a coaxial cylinder of radius $r$ and length $L$ as the Gaussian surface, with flat end caps.

> **Shared method with PD5 and PD6.** All three run the same four moves: pick a surface matching the symmetry, argue where the flux is zero, evaluate $\oint\vec E\cdot d\vec S$ as $E\times(\text{area})$, then set it equal to $q_{\text{enc}}/\varepsilon_0$. Only the surface changes.

**Figure.** An infinite charged wire running horizontally with a coaxial cylindrical Gaussian surface of radius r and length L around it. Field arrows point radially outward through the curved surface, and no flux passes through the two flat end caps because the field there is parallel to the surface.

*The field is everywhere perpendicular to the curved surface and everywhere parallel to the end caps — which is exactly what makes the integral collapse to a multiplication.*

1. By symmetry $\vec E$ is radial and its magnitude depends only on $r$
2. Total flux $= \Phi_{\text{curved}} + \Phi_{\text{cap 1}} + \Phi_{\text{cap 2}}$
3. On the end caps $\vec E \perp d\vec S$, so $\vec E\cdot d\vec S = 0$  — *(field is parallel to the cap, so it contributes no flux)*
4. On the curved surface $\vec E \parallel d\vec S$ and $E$ is constant
5. $\Phi = E \times (\text{curved area}) = E\left(2\pi r L\right)$
6. Charge enclosed $q_{\text{enc}} = \lambda L$  — *(only the length $L$ inside the cylinder counts)*
7. Gauss's law: $\oint\vec E\cdot d\vec S = \dfrac{q_{\text{enc}}}{\varepsilon_0}$
8. $E\left(2\pi r L\right) = \dfrac{\lambda L}{\varepsilon_0}$
9. $L$ cancels from both sides  — *(as it must — the answer cannot depend on how much wire we chose to enclose)*
10. $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$

**Result:** $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$, directed radially — outward for $\lambda \gt 0$

*$E \propto 1/r$, not $1/r^2$. Step 9 is a genuine check on your work: if $L$ survives, something is wrong.*

##### `PD5` Field of an infinite charged plane sheet, by Gauss's law — *3 marks*

> An infinite plane sheet with uniform surface charge density $\sigma$. By symmetry the field must be perpendicular to the sheet and the same on both sides. Take a cylindrical pillbox of cross-sectional area $A$ pushed through the sheet, so one flat face sits on each side.

**Figure.** An infinite charged sheet drawn vertically with a cylindrical pillbox pushed through it, one flat face of area A on each side. Field arrows point outward through both flat faces and no flux passes through the curved side, which is parallel to the field.

*Two flat faces, each of area $A$, each contributing $EA$ — which is where the factor of 2 in the flux comes from, and hence the 2 in the denominator of the answer.*

1. By symmetry $\vec E$ is perpendicular to the sheet and equal in magnitude on both sides
2. On the curved side of the pillbox, $\vec E \perp d\vec S$, so no flux passes through it
3. On each flat face $\vec E \parallel d\vec S$ and $E$ is constant
4. $\Phi = EA + EA = 2EA$  — *(both faces contribute, and they are outward on both sides)*
5. Charge enclosed $q_{\text{enc}} = \sigma A$  — *(only the patch of sheet inside the pillbox)*
6. Gauss's law: $2EA = \dfrac{\sigma A}{\varepsilon_0}$
7. $A$ cancels  — *(again, the answer cannot depend on the size of surface we chose)*
8. $E = \dfrac{\sigma}{2\varepsilon_0}$

**Result:** $E = \dfrac{\sigma}{2\varepsilon_0}$ — **independent of distance** from the sheet

*Just outside a **conductor** the answer is $\sigma/\varepsilon_0$, twice as big, because there the field exists on one side only — the other face of the pillbox is inside the metal where $E = 0$, so only one face contributes at step 4.*

##### `PD6` Field of a uniformly charged thin spherical shell — *3–5 marks*

> A thin shell of radius $R$ carrying total charge $q$ spread uniformly, so $\sigma = q/4\pi R^2$. By symmetry the field is radial and depends only on distance from the centre. Take a concentric spherical Gaussian surface of radius $r$ — once with $r \gt R$, once with $r \lt R$.

**Figure.** A charged spherical shell of radius R with two concentric dashed Gaussian spheres: one outside of radius r greater than R enclosing the whole charge, and one inside of radius r less than R enclosing no charge at all, so the field inside is zero.

*Outside, the Gaussian sphere encloses all of $q$ and the shell behaves exactly like a point charge at its centre. Inside, it encloses nothing — and Gauss's law then forces $E$ to be zero.*

1. **Case 1: outside, $r \gt R$.** Take a concentric sphere of radius $r$
2. By symmetry $E$ is constant over it and $\vec E \parallel d\vec S$ everywhere
3. $\Phi = E\left(4\pi r^2\right)$  — *(surface area of a sphere)*
4. $q_{\text{enc}} = q$  — *(the whole shell is inside)*
5. $E\left(4\pi r^2\right) = \dfrac{q}{\varepsilon_0}$
6. $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}$  — *(identical to a point charge $q$ at the centre)*
7. **Case 2: on the surface, $r = R$.** Put $r=R$ and $q = \sigma\left(4\pi R^2\right)$
8. $E = \dfrac{\sigma}{\varepsilon_0}$
9. **Case 3: inside, $r \lt R$.** Take a concentric sphere of radius $r \lt R$
10. All the charge lies on the shell, *outside* this surface, so $q_{\text{enc}} = 0$  — *(this is the whole argument)*
11. $E\left(4\pi r^2\right) = \dfrac{0}{\varepsilon_0} = 0$
12. $E = 0$ everywhere inside

**Result:** $r \gt R: E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^{2}} \qquad r = R: E = \dfrac{\sigma}{\varepsilon_0} \qquad r \lt R: E = 0$

*The field is **discontinuous** at the surface, jumping from 0 to $\sigma/\varepsilon_0$. The potential is not — it stays constant inside at the surface value, which is PD8's result.*

#### `CH 2` Electrostatic Potential and Capacitance — *7 derivations*

##### `PD7` Potential due to a point charge — *2–3 marks*

> A point charge $+q$ at O. Bring a unit positive test charge from infinity to a point P at distance $r$, along the line joining them. At an intermediate distance $x$ the field is $q/4\pi\varepsilon_0x^2$, and the external force needed is equal and opposite to the electric force, so the work done against the field is what we integrate.

**Figure.** A point charge q at O with a test charge being brought in from infinity on the right to a point P at distance r. At an intermediate distance x the small displacement dx is marked, against the outward electric field.

*The test charge moves inward while the field pushes outward, so the work is done *against* the field. The displacement $d\vec x$ and $\vec E$ are antiparallel, which is where the minus sign in $W = -\int \vec E\cdot d\vec x$ comes from.*

1. Field at distance $x$ from the charge: $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{x^2}$
2. Force on a unit positive test charge: $F = E$
3. The external agent must apply $-\vec E$ to move it without acceleration  — *(quasi-static: no kinetic energy gained)*
4. Small work done in moving through $dx$: $dW = -E\,dx$
5. $W = -\displaystyle\int_{\infty}^{r} \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{x^2}\,dx$  — *(integrating from infinity to P)*
6. $= -\dfrac{q}{4\pi\varepsilon_0}\left[-\dfrac{1}{x}\right]_{\infty}^{r}$  — *($\int x^{-2}dx = -x^{-1}$)*
7. $= \dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{1}{x}\right]_{\infty}^{r} = \dfrac{q}{4\pi\varepsilon_0}\left[\dfrac{1}{r} - \dfrac{1}{\infty}\right]$
8. $\dfrac{1}{\infty} = 0$  — *(the convention $V(\infty)=0$ enters here)*
9. $W = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r}$
10. $V = \dfrac{W}{q_0}$ with $q_0 = 1$

**Result:** $V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r}$

*Falls as $1/r$ where $E$ falls as $1/r^2$ — the integral of an inverse square is an inverse first power. For several charges just add these algebraically, signs included: potential is a scalar.*

##### `PD8` Potential of a charged spherical shell, inside and out — *3 marks*

> The shell of PD6: radius $R$, total charge $q$. Use the field results already established there and integrate them, splitting the journey at the surface when the point is inside.

> **Shared setup with PD6.** This derivation consumes PD6's three field results. Do them as a pair — the field first, then the potential — and the "$E=0$ but $V\neq0$" question answers itself.

**Figure.** Graph of potential against distance from the centre of a charged shell: constant at the surface value from the centre out to radius R, then falling as one over r beyond R, with no discontinuity at the surface.

*Flat inside, $1/r$ outside, and **continuous** at $r=R$ — unlike the field, which jumps. A flat $V$ is exactly what $E = -dV/dr = 0$ means.*

1. **Outside, $r \gt R$.** $V = -\displaystyle\int_{\infty}^{r}\vec E\cdot d\vec l$ with $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}$  — *(PD6, case 1)*
2. This is the same integral as PD7, so $V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r}$
3. **On the surface, $r=R$.** Put $r=R$: $V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{R}$
4. **Inside, $r \lt R$.** Split the path at the surface:
5. $V = -\displaystyle\int_{\infty}^{R}\vec E\cdot d\vec l \;-\; \int_{R}^{r}\vec E\cdot d\vec l$
6. The first integral is step 3, giving $\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{R}$
7. Inside the shell $E = 0$  — *(PD6, case 3)*
8. So the second integral is zero
9. $V_{\text{inside}} = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{R} = V_{\text{surface}}$

**Result:** $r \geq R:\ V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r} \qquad r \lt R:\ V = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{R}$, constant

*Steps 7–8 are the answer to "the field inside a shell is zero; is the potential zero too?" No — zero field means the potential does not *change*, so it holds its surface value.*

##### `PD9` Potential energy of a system of point charges — *2–3 marks*

> Assemble three charges $q_1, q_2, q_3$ at the corners of a triangle, bringing them in one at a time from infinity. The energy of the system is the total work done by the external agent. The trick is that each new charge must be brought in against the field of all the ones already placed.

**Figure.** Three charges at the corners of a triangle with the three pairwise separations r12, r13 and r23 marked along the sides, showing that the system energy is a sum over the three pairs.

*Three charges make exactly three pairs. Each side of the triangle contributes one term — count sides, not corners, and you cannot miscount the terms.*

1. Bring $q_1$ in first. Space is empty, so no work is done: $W_1 = 0$
2. Bring $q_2$ in. It moves in the potential of $q_1$, which at distance $r_{12}$ is $\dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1}{r_{12}}$
3. $W_2 = q_2 V_1 = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1q_2}{r_{12}}$  — *(work = charge × potential at that point)*
4. Bring $q_3$ in. It now moves in the combined potential of $q_1$ **and** $q_2$
5. $W_3 = q_3\left(V_1 + V_2\right) = \dfrac{1}{4\pi\varepsilon_0}\left[\dfrac{q_1q_3}{r_{13}} + \dfrac{q_2q_3}{r_{23}}\right]$  — *(potentials add as scalars)*
6. Total energy $U = W_1 + W_2 + W_3$
7. $U = \dfrac{1}{4\pi\varepsilon_0}\left[\dfrac{q_1q_2}{r_{12}} + \dfrac{q_1q_3}{r_{13}} + \dfrac{q_2q_3}{r_{23}}\right]$
8. In general, $U = \dfrac{1}{4\pi\varepsilon_0}\displaystyle\sum_{i \lt j}\dfrac{q_iq_j}{r_{ij}}$  — *(the restriction $i \lt j$ counts each pair exactly once)*

**Result:** $U = \dfrac{1}{4\pi\varepsilon_0}\left[\dfrac{q_1q_2}{r_{12}} + \dfrac{q_1q_3}{r_{13}} + \dfrac{q_2q_3}{r_{23}}\right]$

*The answer does not depend on the order you bring them in — a good check. Keep the signs: a mixed set of charges gives negative $U$, meaning energy is released on assembly.*

##### `PD10` Capacitance of a parallel plate capacitor — *3 marks*

> Two parallel plates of area $A$ separated by $d$, carrying $+Q$ and $-Q$, with $d$ small enough that the field between them is uniform and edge effects are ignored. Find the field, integrate it to get $V$, then divide.

**Figure.** A parallel plate capacitor: two horizontal plates of area A separated by distance d, the top carrying positive charge and the bottom negative, with uniform downward field lines between them and no field outside.

*Each plate alone gives $\sigma/2\varepsilon_0$. Between the plates the two fields point the same way and add; outside they oppose and cancel — which is why the field is confined to the gap.*

1. Surface charge density on each plate: $\sigma = \dfrac{Q}{A}$
2. Field due to the positive plate alone: $\dfrac{\sigma}{2\varepsilon_0}$  — *(PD5, infinite sheet)*
3. Field due to the negative plate alone: $\dfrac{\sigma}{2\varepsilon_0}$, in the **same** direction in the gap
4. Between the plates the two add: $E = \dfrac{\sigma}{2\varepsilon_0} + \dfrac{\sigma}{2\varepsilon_0} = \dfrac{\sigma}{\varepsilon_0}$
5. Outside, they point oppositely and cancel: $E = 0$  — *(worth stating — it justifies ignoring everything outside)*
6. $E = \dfrac{Q}{A\varepsilon_0}$
7. The field is uniform, so $V = Ed$  — *($V = -\int\vec E\cdot d\vec l$ with $E$ constant)*
8. $V = \dfrac{Qd}{A\varepsilon_0}$
9. $C = \dfrac{Q}{V} = \dfrac{Q A\varepsilon_0}{Qd}$
10. $C = \dfrac{\varepsilon_0 A}{d}$

**Result:** $C = \dfrac{\varepsilon_0 A}{d}$

*$Q$ cancels at step 9, which is the proof that capacitance is a property of the **geometry alone** — it does not depend on how much charge you put on.*

##### `PD11` Capacitance with a dielectric slab in the gap — *3 marks*

> The same capacitor, now with a slab of dielectric constant $K$ and thickness $t$ inserted, where $t \lt d$. Inside the slab the induced polarisation charges reduce the field by a factor $K$; in the remaining gap it is unchanged. The potential difference is built up piece by piece.

> **Shared setup with PD10.** Identical up to step 6 of that derivation. The only new physics is that the field inside a dielectric is $E/K$.

**Figure.** A parallel plate capacitor with a dielectric slab of thickness t occupying part of the gap of width d. The field is E in the empty parts and the smaller value E over K inside the slab.

*The slab does not change the charge, only the field within its own thickness. Since $V$ is the field integrated across the gap, a smaller field over part of the path means a smaller $V$ — and so a larger $C$.*

1. Field in the empty part of the gap: $E = \dfrac{\sigma}{\varepsilon_0} = \dfrac{Q}{A\varepsilon_0}$  — *(PD10, step 6)*
2. Field inside the dielectric: $E' = \dfrac{E}{K}$  — *(induced charges oppose the applied field, reducing it by $K$)*
3. Thickness of empty gap: $d - t$; thickness of slab: $t$
4. $V = E(d-t) + E'\,t$  — *(add the potential drop across each region)*
5. $V = E(d-t) + \dfrac{E}{K}t = E\left[(d-t) + \dfrac{t}{K}\right]$
6. $V = \dfrac{Q}{A\varepsilon_0}\left[d - t + \dfrac{t}{K}\right]$
7. $C = \dfrac{Q}{V}$
8. $C = \dfrac{\varepsilon_0 A}{d - t + \dfrac{t}{K}}$

**Result:** $C = \dfrac{\varepsilon_0 A}{d - t + \dfrac{t}{K}}$

*Two checks worth quoting: $t = d$ gives $C = K\varepsilon_0A/d$ (fully filled), and $K = 1$ gives $\varepsilon_0A/d$ (no slab). Since $K \gt 1$, the denominator shrinks and $C$ always **increases** — and the result does not depend on where in the gap the slab sits.*

##### `PD12` Energy stored in a capacitor, and energy density — *3 marks*

> Charging a capacitor means moving charge from one plate to the other against a rising potential difference. Take the capacitor at an intermediate stage, holding charge $q$ with potential $V' = q/C$, and move one more small charge $dq$ across.

**Figure.** Graph of potential difference against charge on a capacitor: a straight line through the origin of slope one over C, with the shaded triangular area beneath it representing the energy stored, equal to one half Q V.

*The shaded area under the line *is* the work done, since $dW = V'\,dq$. It is a triangle, not a rectangle — which is the whole reason for the factor of $\tfrac12$.*

1. At an intermediate stage the capacitor holds charge $q$ at potential $V' = \dfrac{q}{C}$
2. Work to move a further small charge $dq$: $dW = V'\,dq = \dfrac{q}{C}dq$
3. $W = \displaystyle\int_0^Q \dfrac{q}{C}\,dq$  — *(summing from uncharged to fully charged)*
4. $= \dfrac{1}{C}\left[\dfrac{q^2}{2}\right]_0^Q$
5. $U = \dfrac{Q^2}{2C}$
6. Using $Q = CV$: $U = \dfrac{1}{2}CV^2 = \dfrac{1}{2}QV$  — *(three equivalent forms — use whichever the question gives you)*
7. **Energy density.** Substitute $C = \dfrac{\varepsilon_0A}{d}$ and $V = Ed$:
8. $U = \dfrac{1}{2}\cdot\dfrac{\varepsilon_0A}{d}\cdot E^2d^2 = \dfrac{1}{2}\varepsilon_0E^2\left(Ad\right)$
9. $Ad$ is the volume between the plates  — *(where the field actually lives)*
10. $u = \dfrac{U}{Ad} = \dfrac{1}{2}\varepsilon_0E^2$

**Result:** $U = \dfrac{1}{2}CV^{2} = \dfrac{1}{2}QV = \dfrac{Q^{2}}{2C} \qquad u = \dfrac{1}{2}\varepsilon_0E^{2}$

*The $\tfrac12$ is not decoration: the last charge crosses at the full $V$, the first at almost nothing, and the average is $V/2$. The energy-density form says the energy is stored in the **field**, not on the plates.*

##### `PD13` Capacitors in series and in parallel — *3 marks*

> Two capacitors and a battery of voltage $V$. In **series** the same charge sits on every plate and the voltages add; in **parallel** both feel the same voltage and the charges add. Each combination follows from noting which quantity is shared.

**Figure.** Two circuit diagrams: on the left two capacitors in series across a battery carrying the same charge Q with voltages V1 and V2 adding; on the right two capacitors in parallel across a battery sharing the same voltage V with charges Q1 and Q2 adding.

*Which quantity is shared is the whole derivation. In series the charge has nowhere else to go, so it is common; in parallel both sit across the same two nodes, so the voltage is common.*

1. **Series.** The inner plates are isolated, so induction puts the same charge $Q$ on every plate
2. The voltages add: $V = V_1 + V_2$  — *(going round the loop)*
3. $V_1 = \dfrac{Q}{C_1}$, $V_2 = \dfrac{Q}{C_2}$, and $V = \dfrac{Q}{C_s}$
4. $\dfrac{Q}{C_s} = \dfrac{Q}{C_1} + \dfrac{Q}{C_2}$
5. $Q$ cancels: $\dfrac{1}{C_s} = \dfrac{1}{C_1} + \dfrac{1}{C_2}$
6. **Parallel.** Both capacitors are across the same two points, so both have voltage $V$
7. The charges add: $Q = Q_1 + Q_2$  — *(charge supplied by the battery splits between them)*
8. $Q_1 = C_1V$, $Q_2 = C_2V$, and $Q = C_pV$
9. $C_pV = C_1V + C_2V$
10. $V$ cancels: $C_p = C_1 + C_2$

**Result:** series: $\dfrac{1}{C_s} = \dfrac{1}{C_1}+\dfrac{1}{C_2}$  ·  parallel: $C_p = C_1 + C_2$

*Opposite to the resistor rules, and for a reason you can state: capacitors in series effectively increase the plate *separation*, while in parallel they increase the plate *area*.*

#### `CH 3` Current Electricity — *5 derivations*

##### `PD14` Current in terms of drift velocity — *2–3 marks*

> A conductor of cross-sectional area $A$ carrying current $I$, with $n$ free electrons per unit volume all drifting at average speed $v_d$. Count how much charge crosses a chosen cross-section in time $\Delta t$ by asking which electrons are close enough to make it.

**Figure.** A cylindrical conductor of cross-sectional area A with electrons drifting to the right. In time delta t every electron within a distance v-d delta t of the chosen cross-section crosses it, so the relevant volume is A times v-d delta t.

*Only electrons within $v_d\,\Delta t$ of the cross-section can reach it in time $\Delta t$. That slab of conductor is the entire content of the derivation.*

1. In time $\Delta t$, an electron travels a distance $v_d\,\Delta t$  — *(drift is a steady average motion)*
2. So every electron within $v_d\,\Delta t$ of the cross-section crosses it, and no others do
3. Volume of that slab $= A \times v_d\,\Delta t$
4. Number of electrons in it $= n \times A v_d\,\Delta t$  — *($n$ is the number per unit volume)*
5. Charge crossing $= \Delta Q = neAv_d\,\Delta t$
6. $I = \dfrac{\Delta Q}{\Delta t}$
7. $I = neAv_d$
8. Also $J = \dfrac{I}{A} = nev_d$  — *(current density)*

**Result:** $I = neAv_d \qquad J = nev_d$

*Drift speed is around $10^{-4}\ \ce{m s^-1}$ — slower than walking — while random thermal speed is about $10^{5}$. A lamp lights instantly because the **field** is established through the wire at nearly the speed of light, not because electrons rush along it.*

##### `PD15` Ohm's law from drift velocity, and resistivity — *3–5 marks*

> The same conductor, length $l$ and area $A$, with a potential difference $V$ across it. Between collisions each electron accelerates in the field; after each collision its drift is randomised. The average time between collisions is the relaxation time $\tau$.

> **Shared setup with PD14.** This picks up exactly where that one stops, by asking what sets $v_d$ in the first place.

**Figure.** A conductor of length l and area A with a potential difference V across it. The uniform field E equals V over l inside, and an electron zig-zags between collisions while drifting slowly against the field direction.

*The zig-zag is the fast random thermal motion; the slow, steady leftward creep superposed on it is the drift. Only the drift carries current.*

1. Field inside the conductor: $E = \dfrac{V}{l}$  — *(uniform field over length $l$)*
2. Force on an electron: $F = eE$, so acceleration $a = \dfrac{eE}{m}$
3. After a collision the drift velocity is randomised to zero on average  — *(collisions destroy the accumulated drift)*
4. So the average drift gained in time $\tau$ is $v_d = a\tau = \dfrac{eE\tau}{m}$
5. $I = neAv_d$  — *(PD14)*
6. $I = neA\cdot\dfrac{eE\tau}{m} = \dfrac{ne^2A\tau}{m}E$
7. Substituting $E = \dfrac{V}{l}$: $I = \dfrac{ne^2A\tau}{ml}V$
8. So $V = \left(\dfrac{ml}{ne^2A\tau}\right)I$ — that is, $V \propto I$  — *(everything in the bracket is constant at fixed temperature: **this is Ohm's law**)*
9. Comparing with $V = IR$: $R = \dfrac{ml}{ne^2A\tau}$
10. Comparing with $R = \dfrac{\rho l}{A}$:
11. $\rho = \dfrac{m}{ne^2\tau}$
12. And $\sigma = \dfrac{1}{\rho} = \dfrac{ne^2\tau}{m}$, giving $\vec J = \sigma\vec E$

**Result:** $\rho = \dfrac{m}{ne^{2}\tau} \qquad \sigma = \dfrac{ne^{2}\tau}{m} \qquad \vec J = \sigma\vec E$

*Step 8 is the real content: Ohm's law is not assumed, it *comes out*. And the result explains the temperature behaviour of both material classes — heating a metal shortens $\tau$ so $\rho$ rises; heating a semiconductor raises $n$ far more than it cuts $\tau$, so $\rho$ falls.*

##### `PD16` Resistors in series and in parallel — *2–3 marks*

> Two resistors and a cell of emf $V$. In **series** there is only one path, so the current is common and the voltages add. In **parallel** both are across the same two nodes, so the voltage is common and the currents add.

**Figure.** Two circuit diagrams: on the left two resistors in series carrying the same current I with voltages V1 and V2 adding; on the right two resistors in parallel across the same voltage V with currents I1 and I2 adding.

*Again the derivation is just "which quantity is shared". One path means one current; one pair of nodes means one voltage.*

1. **Series.** One path, so the same current $I$ flows through both
2. The potential drops add: $V = V_1 + V_2$  — *(Kirchhoff's loop rule)*
3. $IR_s = IR_1 + IR_2$  — *(Ohm's law on each)*
4. $I$ cancels: $R_s = R_1 + R_2$
5. **Parallel.** Both are across the same two points, so both have the same $V$
6. The current splits: $I = I_1 + I_2$  — *(Kirchhoff's junction rule — conservation of charge)*
7. $\dfrac{V}{R_p} = \dfrac{V}{R_1} + \dfrac{V}{R_2}$
8. $V$ cancels: $\dfrac{1}{R_p} = \dfrac{1}{R_1} + \dfrac{1}{R_2}$

**Result:** series: $R_s = R_1+R_2$  ·  parallel: $\dfrac{1}{R_p} = \dfrac{1}{R_1}+\dfrac{1}{R_2}$

*$R_s$ is larger than either resistor; $R_p$ is smaller than both. If your answer breaks either rule, you have used the wrong formula.*

##### `PD17` Balance condition of a Wheatstone bridge — *3 marks*

> Four resistances $P, Q, R, S$ in a quadrilateral ABCD, with a cell across the diagonal AC and a galvanometer across BD. The bridge is **balanced** when the galvanometer shows no deflection. That single condition is what makes the algebra collapse.

**Figure.** A Wheatstone bridge drawn as a diamond: resistances P and Q in the upper two arms and R and S in the lower two, a cell across the horizontal diagonal from A to C, and a galvanometer across the vertical diagonal from B to D reading zero at balance.

*At balance no current crosses BD, so B and D sit at the same potential. The bridge then behaves as two independent series pairs — P with Q, and R with S — carrying currents $I_1$ and $I_2$.*

1. At balance the galvanometer reads zero, so no current flows through BD
2. Therefore $V_B = V_D$  — *(no current through a resistanceless branch means no potential difference across it)*
3. Since no current leaves at B, the whole of $I_1$ that flows through P continues through Q
4. Likewise the whole of $I_2$ through R continues through S
5. $V_A - V_B = I_1P$ and $V_A - V_D = I_2R$
6. But $V_B = V_D$, so $I_1P = I_2R$  …(i)
7. $V_B - V_C = I_1Q$ and $V_D - V_C = I_2S$
8. Again $V_B = V_D$, so $I_1Q = I_2S$  …(ii)
9. Divide (i) by (ii): $\dfrac{I_1P}{I_1Q} = \dfrac{I_2R}{I_2S}$  — *(the unknown currents cancel — this is why we divide)*
10. $\dfrac{P}{Q} = \dfrac{R}{S}$

**Result:** $\dfrac{P}{Q} = \dfrac{R}{S}$ at balance

*In the **metre bridge**, P and Q are the two parts of a uniform wire, so their ratio is $l : (100-l)$ and the unknown becomes $X = R(100-l)/l$. The bridge is most sensitive when all four arms are comparable, so aim for a balance point near the middle of the wire.*

##### `PD18` Internal resistance of a cell, using a potentiometer — *3 marks*

> A potentiometer wire carries a steady current from a driver cell, so the potential falls uniformly along it at a rate $K$ volts per unit length. The cell under test is balanced twice: once on open circuit, and once with a known resistance $R$ across it.

**Figure.** A potentiometer: a long uniform wire AB fed by a driver cell, with the test cell and a galvanometer connected to a sliding jockey. The balance point is at length l1 with the shunt key open and at the shorter length l2 with resistance R connected across the cell.

*At balance no current is drawn from the test cell, so the potentiometer reads its true **emf** — which is exactly what a voltmeter cannot do.*

1. The potential falls uniformly along the wire at $K$ volts per unit length  — *(steady current through a uniform wire)*
2. **Key open.** No current is drawn from the test cell, so it balances against its full emf
3. $\mathcal{E} = K l_1$  …(i)
4. **Key closed**, with $R$ across the cell. Now the cell drives a current, so the balance is against its **terminal voltage**
5. $V = K l_2$  …(ii)  — *($l_2 \lt l_1$, because $V \lt \mathcal{E}$)*
6. Divide (i) by (ii): $\dfrac{\mathcal{E}}{V} = \dfrac{l_1}{l_2}$  — *($K$ cancels, so it never has to be measured*
7. For a cell delivering current through $R$: $\mathcal{E} = I(R+r)$ and $V = IR$
8. $\dfrac{\mathcal{E}}{V} = \dfrac{R+r}{R}$  — *($I$ cancels)*
9. $\dfrac{l_1}{l_2} = \dfrac{R+r}{R}$
10. $\dfrac{l_1}{l_2} - 1 = \dfrac{r}{R}$
11. $r = R\left(\dfrac{l_1 - l_2}{l_2}\right)$

**Result:** $r = R\left(\dfrac{l_1-l_2}{l_2}\right)$

*Steps 6 and 8 both work by cancelling a quantity you never measured — $K$ and $I$. The same two-balance trick with two cells gives $\mathcal{E}_1/\mathcal{E}_2 = l_1/l_2$. Sensitivity improves with a **longer** wire, because that lowers $K$.*

#### `CH 4` Moving Charges and Magnetism — *6 derivations*

##### `PD19` Field at the centre of a circular current loop — *2–3 marks*

> A circular loop of radius $R$ carrying current $I$. Take a small element $d\vec l$ anywhere on the loop. Every element is the same distance $R$ from the centre, and every element is perpendicular to the line joining it to the centre — the two facts that make this the easiest Biot–Savart application.

**Figure.** A circular current loop of radius R with a small element dl on its circumference. The radius from the element to the centre is perpendicular to the element, so the angle between them is ninety degrees, and every element contributes a field into the page at the centre.

*Every element sits at the same distance $R$ and at $90°$ to its own radius, so $\sin\theta = 1$ throughout — and every contribution points the same way, so the vector integral becomes a plain sum of magnitudes.*

1. Biot–Savart: $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl\sin\theta}{r^2}$
2. For every element, $r = R$  — *(all points of a circle are equidistant from the centre)*
3. $d\vec l$ is tangential and $\hat r$ is radial, so $\theta = 90°$ and $\sin\theta = 1$
4. $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl}{R^2}$
5. By the right-hand rule every element's contribution points the same way (along the axis)  — *(so the magnitudes simply add — no resolution needed)*
6. $B = \displaystyle\oint dB = \dfrac{\mu_0}{4\pi}\dfrac{I}{R^2}\oint dl$
7. $\displaystyle\oint dl = 2\pi R$  — *(total circumference)*
8. $B = \dfrac{\mu_0}{4\pi}\dfrac{I}{R^2}\left(2\pi R\right)$
9. $B = \dfrac{\mu_0 I}{2R}$
10. For $N$ turns, $B = \dfrac{\mu_0 NI}{2R}$

**Result:** $B = \dfrac{\mu_0 I}{2R}$, directed along the axis by the right-hand rule

*For an **arc** subtending angle $\phi$ radians at the centre, step 7 becomes $R\phi$ instead of $2\pi R$, giving $B = \mu_0 I\phi/4\pi R$. A semicircle is the $\phi = \pi$ case.*

##### `PD20` Field on the axis of a circular current loop — *3–5 marks*

> The same loop, but the field point P now sits on the axis at distance $x$ from the centre. Each element is $r = \sqrt{R^2+x^2}$ from P. Now the contributions do *not* all point the same way — they sweep round a cone — so this one needs resolution into components.

> **Shared setup with PD19.** Same loop, same element; only P moves off the centre. Putting $x=0$ in the final answer must return PD19's result, and that is your check.

**Figure.** A circular loop seen edge-on with a point P on its axis at distance x from the centre. The field contribution from an element at the top and its diametrically opposite partner at the bottom have perpendicular components that cancel and axial components that add.

*Take elements in diametrically opposite pairs. Their components perpendicular to the axis point oppositely and cancel; their axial components both point along the axis and add. Only the $\cos\theta$ part survives.*

1. Distance from any element to P: $r = \sqrt{R^2+x^2}$  — *(right triangle with legs $R$ and $x$)*
2. $d\vec l$ is perpendicular to $\hat r$ for every element, so $\sin\theta = 1$ again
3. $dB = \dfrac{\mu_0}{4\pi}\dfrac{I\,dl}{R^2+x^2}$
4. $d\vec B$ is perpendicular to $\vec r$, so it makes angle $\theta$ with the axis
5. Resolve: $dB\cos\theta$ along the axis, $dB\sin\theta$ perpendicular to it
6. For each element there is a diametrically opposite one whose perpendicular component is equal and opposite, so all perpendicular components cancel  — *(this is the key symmetry argument — state it)*
7. $B = \displaystyle\oint dB\cos\theta$
8. $\cos\theta = \dfrac{R}{\sqrt{R^2+x^2}}$  — *(from the same right triangle)*
9. $B = \dfrac{\mu_0}{4\pi}\dfrac{I}{R^2+x^2}\cdot\dfrac{R}{\sqrt{R^2+x^2}}\displaystyle\oint dl$
10. $\displaystyle\oint dl = 2\pi R$
11. $B = \dfrac{\mu_0}{4\pi}\dfrac{I\,R\,(2\pi R)}{\left(R^2+x^2\right)^{3/2}}$
12. $B = \dfrac{\mu_0 I R^2}{2\left(R^2+x^2\right)^{3/2}}$

**Result:** $B = \dfrac{\mu_0 I R^{2}}{2\left(R^{2}+x^{2}\right)^{3/2}}$, along the axis  ($\times N$ for $N$ turns)

*Check: $x = 0$ gives $\mu_0I/2R$, which is PD19. Far away, $x \gg R$, it becomes $\dfrac{\mu_0}{4\pi}\dfrac{2M}{x^3}$ with $M = IA$ — the loop is a magnetic dipole, which is the bridge into Chapter 5.*

##### `PD21` Field of a long straight wire, by Ampère's law — *2–3 marks*

> An infinitely long straight wire carrying current $I$. By symmetry the field lines are concentric circles centred on the wire, with $B$ constant on any one circle. Choose such a circle of radius $r$ as the Amperian loop.

> **Shared method with PD22.** Both are Ampère's law: choose a loop matching the symmetry, evaluate $\oint\vec B\cdot d\vec l$ as $B\times(\text{path length})$, count the enclosed current. Only the loop shape changes.

**Figure.** A long straight wire seen end-on carrying current out of the page, with a circular Amperian loop of radius r around it. The magnetic field is tangential to the circle everywhere and constant in magnitude on it.

*The circle is chosen precisely because $\vec B$ is parallel to $d\vec l$ at every point of it and constant in magnitude — the two conditions that turn the line integral into a multiplication.*

1. By symmetry, field lines are circles around the wire and $B$ has the same magnitude at every point of a given circle
2. Choose that circle, radius $r$, as the Amperian loop
3. At every point $\vec B \parallel d\vec l$, so $\vec B\cdot d\vec l = B\,dl$  — *(the angle between them is zero)*
4. $\displaystyle\oint\vec B\cdot d\vec l = B\oint dl$  — *($B$ constant, so it comes out of the integral)*
5. $\displaystyle\oint dl = 2\pi r$
6. $\displaystyle\oint\vec B\cdot d\vec l = B\left(2\pi r\right)$
7. Current enclosed $= I$
8. Ampère's law: $B\left(2\pi r\right) = \mu_0 I$
9. $B = \dfrac{\mu_0 I}{2\pi r}$

**Result:** $B = \dfrac{\mu_0 I}{2\pi r}$, tangential, sense given by the right-hand thumb rule

*$B \propto 1/r$. Note the structural echo of PD4, the electric field of a line charge — same geometry, same $1/r$, different law.*

##### `PD22` Field inside a long solenoid, by Ampère's law — *3 marks*

> A long solenoid with $n$ turns per unit length carrying current $I$. Inside it the field is uniform and along the axis; outside a long solenoid it is negligible. Take a rectangular Amperian loop with one side of length $L$ inside the solenoid and the opposite side outside it.

**Figure.** A long solenoid in cross-section with a rectangular Amperian loop. The side of length L inside the solenoid lies along the uniform axial field; the opposite side is outside where the field is zero; the two short sides are perpendicular to the field so contribute nothing.

*Three of the loop's four sides contribute nothing — one because the field is zero out there, two because they run perpendicular to it. Only the inside side of length $L$ survives.*

1. Inside a long solenoid the field is uniform and parallel to the axis; outside it is negligible
2. Take a rectangular loop with the side of length $L$ inside, parallel to the axis
3. Along that side, $\vec B\parallel d\vec l$ and $B$ is constant, contributing $BL$
4. Along the opposite side, outside the solenoid, $B = 0$, contributing nothing
5. Along the two short sides, $\vec B \perp d\vec l$, contributing nothing  — *(the dot product vanishes)*
6. $\displaystyle\oint\vec B\cdot d\vec l = BL$
7. Number of turns threaded by the loop $= nL$
8. Current enclosed $= \left(nL\right)I$  — *(each turn carries $I$ through the loop)*
9. Ampère's law: $BL = \mu_0 nLI$
10. $L$ cancels: $B = \mu_0 nI$

**Result:** $B = \mu_0 n I$ — uniform, independent of position inside

*At the **end** of a solenoid the field is half this, $\mu_0nI/2$. For a **toroid** the same argument with a circular loop gives the same formula with $n = N/2\pi r$.*

##### `PD23` Force between two parallel currents, and the definition of the ampere — *3 marks*

> Two long parallel wires, separation $r$, carrying $I_1$ and $I_2$ in the same direction. Each sits in the field of the other. Compute the field of the first at the position of the second, then the force that field exerts on a length $L$ of the second.

**Figure.** Two parallel wires carrying currents in the same direction. The field of the first wire at the position of the second points into the page, and the resulting force on the second wire points towards the first, so the wires attract.

*Wire 1's field at wire 2 points into the page; applying $\vec F = I(\vec L\times\vec B)$ to wire 2 gives a force pointing back towards wire 1. Parallel currents attract — the opposite of what like charges do.*

1. Field of wire 1 at the position of wire 2: $B_1 = \dfrac{\mu_0 I_1}{2\pi r}$  — *(PD21)*
2. Force on a length $L$ of wire 2 in that field: $F = B_1 I_2 L\sin\theta$
3. The wire is perpendicular to the field, so $\theta = 90°$ and $\sin\theta = 1$
4. $F = B_1 I_2 L = \dfrac{\mu_0 I_1}{2\pi r}I_2 L$
5. $\dfrac{F}{L} = \dfrac{\mu_0 I_1 I_2}{2\pi r}$
6. By Fleming's left-hand rule the force on wire 2 points towards wire 1, and by Newton's third law wire 1 is pulled equally towards wire 2  — *(so currents in the same direction attract)*
7. **Definition of the ampere.** Put $I_1 = I_2 = 1\ \text{A}$ and $r = 1\ \text{m}$:
8. $\dfrac{F}{L} = \dfrac{4\pi\times10^{-7}\times1\times1}{2\pi\times1}$
9. $\dfrac{F}{L} = 2\times10^{-7}\ \ce{N m^-1}$

**Result:** $\dfrac{F}{L} = \dfrac{\mu_0 I_1I_2}{2\pi r}$  ·  one ampere is the current which, in two infinitely long parallel wires 1 m apart in vacuum, produces a force of $2\times10^{-7}\ \ce{N m^-1}$

*Currents in **opposite** directions repel. Steps 7–9 are the whole answer to "define the ampere", and are worth writing out in that form.*

##### `PD24` Torque on a current loop in a magnetic field — *3 marks*

> A rectangular loop of sides $l$ and $b$, carrying current $I$, placed in a uniform field $\vec B$ with its plane making angle $\theta$ between the normal to the loop and the field. The two sides of length $l$ carry forces that form a couple; the other two produce forces along the same line that simply cancel.

**Figure.** A rectangular current loop seen edge-on in a horizontal magnetic field, tilted so that its normal makes angle theta with the field. Forces I l B act out of and into the page on the two long sides, forming a couple whose arm is b sine theta.

*Seen edge-on, the loop is a line. One long side carries force out of the page, the other into it — equal, opposite, and separated by the perpendicular distance $b\sin\theta$.*

1. Force on a current-carrying side: $F = BIl\sin\alpha$, with $\alpha$ the angle between the side and $\vec B$
2. The two sides of length $l$ are perpendicular to $\vec B$, so each feels $F = BIl$
3. These two forces are equal, opposite and not collinear — a couple
4. The other two sides feel forces along the same line, equal and opposite, which cancel and give no torque  — *(state this, or the derivation is incomplete)*
5. Perpendicular distance between the lines of action of the couple $= b\sin\theta$  — *(from the edge-on geometry)*
6. $\tau = F \times b\sin\theta = \left(BIl\right)b\sin\theta$
7. $lb = A$, the area of the loop
8. $\tau = BIA\sin\theta$
9. For $N$ turns, $\tau = NBIA\sin\theta$
10. Writing $M = NIA$: $\tau = MB\sin\theta$, or $\vec\tau = \vec M\times\vec B$

**Result:** $\vec\tau = \vec M\times\vec B, \qquad \tau = NIAB\sin\theta, \qquad M = NIA$

*Maximum when the loop's **plane** is parallel to $\vec B$ ($\theta = 90°$), zero when the plane is perpendicular. Net force is always zero in a uniform field — the loop rotates but does not drift. This is the working principle of the motor and the moving-coil galvanometer.*

#### `CH 5` Magnetism and Matter — *3 derivations*

##### `PD25` A bar magnet behaves as an equivalent solenoid — *3–5 marks*

> A solenoid of radius $a$, length $2l$, with $n$ turns per unit length carrying current $I$. Find its field at a point P on the axis, far away at distance $r$ from the centre. Treat the solenoid as a stack of circular loops, use PD20 for each, and integrate along the length.

> **Shared setup with PD20.** Each slice of the solenoid is one circular loop, so PD20's axial-field result is the integrand here.

**Figure.** A solenoid of radius a and half-length l drawn in section, with a thin slice of width dx at distance x from the centre. A point P lies on the axis far to the right at distance r from the centre, so the slice is r minus x from P.

*The shaded slice of width $dx$ holds $n\,dx$ turns and acts as one loop. Summing all such slices from $-l$ to $+l$ turns the solenoid into a single dipole.*

1. Take a slice of width $dx$ at distance $x$ from the centre; it contains $n\,dx$ turns
2. Its distance from P is $(r-x)$
3. Axial field of one loop: $dB = \dfrac{\mu_0\,I\,a^2\,(n\,dx)}{2\left(a^2 + (r-x)^2\right)^{3/2}}$  — *(PD20, with $N \to n\,dx$)*
4. P is far away, so $r \gg a$ and $r \gg x$  — *(the far-field approximation — state it)*
5. Then $a^2 + (r-x)^2 \approx r^2$
6. $dB \approx \dfrac{\mu_0\,n\,I\,a^2}{2r^3}\,dx$
7. $B = \displaystyle\int_{-l}^{+l}\dfrac{\mu_0 n I a^2}{2r^3}\,dx$
8. $B = \dfrac{\mu_0 n I a^2}{2r^3}\left(2l\right)$  — *(the integrand is now constant, so the integral is just the length $2l$)*
9. $B = \dfrac{\mu_0}{4\pi}\cdot\dfrac{2\left(n\,2l\right)I\left(\pi a^2\right)}{r^3}$  — *(regrouping to expose $N$ and $A$)*
10. Total turns $N = n(2l)$, and cross-sectional area $A = \pi a^2$, so $M = NIA$
11. $B = \dfrac{\mu_0}{4\pi}\dfrac{2M}{r^3}$

**Result:** $B = \dfrac{\mu_0}{4\pi}\dfrac{2M}{r^{3}}$ — identical to the axial field of a bar magnet of moment $M$

*This is the whole point: a solenoid's far field is indistinguishable from a bar magnet's, which is what licenses treating magnets as dipoles throughout the chapter. Compare the form with PD1 — the electric axial dipole field — and note they differ only in the constant.*

##### `PD26` A magnetic dipole oscillating in a uniform field performs SHM — *3 marks*

> A bar magnet of moment $M$ and moment of inertia $I$ suspended so it can rotate freely in a uniform field $\vec B$. Displace it by a small angle $\theta$ from the field direction and release. The restoring torque is the magnetic one; show it is proportional to $-\theta$, which is the definition of SHM.

**Figure.** A bar magnet suspended by a thread, displaced by a small angle theta from the horizontal field direction. The magnetic torque acts to restore it towards alignment, producing simple harmonic oscillation.

*The torque always acts to pull the magnet back towards alignment. For small $\theta$ it is proportional to the displacement itself — which is exactly the condition for simple harmonic motion.*

1. Torque on the magnet: $\tau = -MB\sin\theta$  — *(the minus sign says it opposes the displacement)*
2. Newton's second law for rotation: $\tau = I\alpha$, with $\alpha = \dfrac{d^2\theta}{dt^2}$
3. $I\dfrac{d^2\theta}{dt^2} = -MB\sin\theta$
4. For **small** $\theta$, $\sin\theta \approx \theta$ in radians  — *(this approximation is what makes the motion harmonic, and it must be stated)*
5. $I\dfrac{d^2\theta}{dt^2} = -MB\theta$
6. $\dfrac{d^2\theta}{dt^2} = -\dfrac{MB}{I}\theta$
7. Compare with the SHM equation $\dfrac{d^2\theta}{dt^2} = -\omega^2\theta$
8. $\omega^2 = \dfrac{MB}{I}$
9. $T = \dfrac{2\pi}{\omega} = 2\pi\sqrt{\dfrac{I}{MB}}$
10. Rearranged for the field: $B = \dfrac{4\pi^2 I}{MT^2}$

**Result:** $T = 2\pi\sqrt{\dfrac{I}{MB}} \qquad B = \dfrac{4\pi^{2}I}{MT^{2}}$

*Here $I$ is the **moment of inertia**, not current — for a bar of mass $m$ and length $L$ about its centre, $I = mL^2/12$. This is how a vibration magnetometer measures the horizontal component of the Earth's field.*

##### `PD27` Magnetic moment of an electron in a circular orbit — *2–3 marks*

> An electron of charge $e$ and mass $m$ circling a nucleus in an orbit of radius $r$ with speed $v$. A circulating charge is a current loop, so it has a magnetic moment. Relate that moment to the electron's angular momentum — the link that underlies all atomic magnetism.

**Figure.** An electron orbiting a nucleus in a circle of radius r with speed v. The electron circulates one way, so the conventional current runs the opposite way, and the resulting magnetic moment points opposite to the orbital angular momentum.

*The electron circulates one way; conventional current runs the other. That single sign flip is why the magnetic moment points opposite to the angular momentum.*

1. Period of one orbit: $T = \dfrac{2\pi r}{v}$
2. The charge $e$ passes any point once per period, so $I = \dfrac{e}{T} = \dfrac{ev}{2\pi r}$  — *(a circulating charge *is* a current)*
3. Magnetic moment of a single loop: $M = IA$
4. $A = \pi r^2$
5. $M = \dfrac{ev}{2\pi r}\times\pi r^2 = \dfrac{evr}{2}$
6. Orbital angular momentum: $L = mvr$
7. So $vr = \dfrac{L}{m}$
8. $M = \dfrac{e}{2}\cdot\dfrac{L}{m} = \dfrac{e}{2m}L$
9. The electron's charge is negative, so $\vec M$ is antiparallel to $\vec L$: $\vec M = -\dfrac{e}{2m}\vec L$
10. Bohr's quantisation gives $L = \dfrac{nh}{2\pi}$
11. $M = \dfrac{e}{2m}\cdot\dfrac{nh}{2\pi} = \dfrac{neh}{4\pi m}$
12. For $n=1$: $M = \dfrac{eh}{4\pi m} = \mu_B = 9.27\times10^{-24}\ \ce{A m^2}$

**Result:** $\vec M = -\dfrac{e}{2m}\vec L \qquad \mu_B = \dfrac{eh}{4\pi m} = 9.27\times10^{-24}\ \ce{A m^{2}}$

*The ratio $e/2m$ is the **gyromagnetic ratio**, the same for every electron orbit. $\mu_B$, the Bohr magneton, is the natural unit of atomic magnetic moment.*

#### `CH 6` Electromagnetic Induction — *5 derivations*

##### `PD28` Motional emf, and the energy balance behind it — *3–5 marks*

> A conducting rod of length $l$ slides with velocity $v$ along two parallel rails in a uniform field $\vec B$ perpendicular to the plane of the circuit, with a resistance $R$ closing the loop. As the rod moves, the enclosed area grows, so the flux grows.

**Figure.** A conducting rod sliding to the right on two horizontal rails in a magnetic field into the page, with a resistance R closing the circuit on the left. The area of the loop increases as the rod moves, and an induced current flows opposing the motion.

*Moving the rod by $dx$ sweeps out extra area $l\,dx$, and it is that growing area — not a changing $B$ — which changes the flux here.*

1. Flux through the circuit: $\Phi_B = B\,A = B\,l\,x$
2. Moving the rod by $dx$ increases the area by $l\,dx$, so $d\Phi_B = B\,l\,dx$
3. Faraday's law: $\varepsilon = -\dfrac{d\Phi_B}{dt} = -Bl\dfrac{dx}{dt}$
4. $\dfrac{dx}{dt} = v$
5. $\varepsilon = -Blv$, of magnitude $Blv$  — *(the minus sign is Lenz's law: the induced effect opposes the growth in flux)*
6. Induced current: $I = \dfrac{\varepsilon}{R} = \dfrac{Blv}{R}$
7. That current, in the same field, makes the rod feel a force $F = BIl$  — *(a current-carrying conductor in a field — PD24's starting point)*
8. $F = B\left(\dfrac{Blv}{R}\right)l = \dfrac{B^2l^2v}{R}$, directed **opposing** the motion
9. Power the agent must supply to keep $v$ constant: $P_{\text{applied}} = Fv = \dfrac{B^2l^2v^2}{R}$
10. Power dissipated in the resistance: $P = I^2R = \left(\dfrac{Blv}{R}\right)^2R = \dfrac{B^2l^2v^2}{R}$
11. The two are equal  — *(so the electrical energy came from the mechanical work — nothing was created)*

**Result:** $\varepsilon = Blv, \quad I = \dfrac{Blv}{R}, \quad F = \dfrac{B^{2}l^{2}v}{R}, \quad P_{\text{applied}} = P_{\text{dissipated}}$

*Steps 9–11 are the answer to "show that Lenz's law follows from conservation of energy". If the induced force *helped* the motion you would get free energy — which is why the minus sign must be there.*

##### `PD29` Self-inductance of a long solenoid — *2–3 marks*

> A long solenoid of length $l$, cross-sectional area $A$, with $N$ total turns ($n = N/l$ per unit length) carrying current $I$. Self-inductance is defined by $N\Phi = LI$, so find the flux linkage and divide by the current.

> **Shared setup with PD22.** The field inside is $\mu_0nI$ from that derivation; everything here is bookkeeping on top of it.

**Figure.** A solenoid of length l and cross-sectional area A with N turns carrying current I. The uniform internal field mu-zero n I threads all N turns, giving a total flux linkage N times B times A.

*The same uniform field threads every one of the $N$ turns, so the flux *linkage* is $N$ times the flux through one turn. That factor of $N$, on top of the $n$ already inside $B$, is why $L$ goes as $N^2$.*

1. Field inside the solenoid: $B = \mu_0 n I$  — *(PD22)*
2. Flux through one turn: $\Phi = BA = \mu_0 n I A$
3. The same flux threads all $N$ turns, so total flux linkage $= N\Phi$
4. $N\Phi = N\mu_0 n I A$
5. By definition $N\Phi = LI$
6. $LI = N\mu_0 n I A$
7. $I$ cancels: $L = \mu_0 n N A$  — *(as it must — inductance is a property of the coil, not of the current in it)*
8. $N = nl$
9. $L = \mu_0 n^2 A l$, equivalently $L = \dfrac{\mu_0 N^2 A}{l}$
10. With a core of relative permeability $\mu_r$, multiply by $\mu_r$

**Result:** $L = \mu_0 n^{2} A l = \dfrac{\mu_0 N^{2}A}{l}$  ($\times\mu_r$ with a core)

*Note the symbol clash: $L$ on the left is **inductance**, $l$ on the right is **length**. Doubling the turns quadruples $L$, because $N$ enters twice — once in the field, once in the linkage.*

##### `PD30` Mutual inductance of two coaxial solenoids — *3 marks*

> Two long coaxial solenoids of the same length $l$: an inner one of $N_1$ turns and area $A$, and an outer one of $N_2$ turns. Pass a current $I_1$ through the inner one and find the flux it links through the outer one.

> **Shared setup with PD29.** Same field, same flux; the only change is that the flux is now counted through a *second* coil.

**Figure.** Two coaxial solenoids of the same length: an inner one of N1 turns and area A carrying current I1, surrounded by an outer one of N2 turns. The field of the inner solenoid threads the outer coil, linking flux through it.

*Only the inner solenoid's own cross-section carries field, so it is the **inner** area $A$ that appears in the answer — not the outer coil's larger area.*

1. Field produced by the inner solenoid: $B_1 = \mu_0 n_1 I_1 = \mu_0\dfrac{N_1}{l}I_1$  — *(PD22)*
2. This field exists only inside the inner solenoid, over area $A$
3. Flux through one turn of the **outer** coil: $\Phi = B_1 A$  — *(the outer turn encloses the inner solenoid, so it links exactly this flux)*
4. Total flux linkage of the outer coil: $N_2\Phi = N_2B_1A$
5. $N_2\Phi = \mu_0\dfrac{N_1N_2A}{l}I_1$
6. By definition $N_2\Phi = M I_1$
7. $I_1$ cancels
8. $M = \dfrac{\mu_0 N_1N_2A}{l}$

**Result:** $M = \dfrac{\mu_0 N_1N_2A}{l}$, and $M_{12} = M_{21}$

*Running the argument the other way — current in the outer coil, flux through the inner — gives the same $M$, which is the reciprocity theorem. This is the principle of the transformer.*

##### `PD31` Energy stored in an inductor, and magnetic energy density — *3 marks*

> Building up a current in an inductor means working against the back emf it produces. Take the current at an intermediate value $i$, when the back emf is $L\,di/dt$, and compute the work done pushing a further $dq$ through against it.

> **Shared shape with PD12.** Exactly the capacitor argument with $L$ for $C$ and $i$ for $q$: the opposing quantity grows as you build up, so the energy carries a factor of $\tfrac12$.

**Figure.** Graph of back emf against current in an inductor: a straight line through the origin of slope L over the time constant, with the shaded triangular area beneath representing the energy stored, equal to one half L I squared.

*Same triangle as the capacitor's. The last increment of current is pushed against the full back emf, the first against almost none — so the average is half, and the energy is $\tfrac12LI^2$.*

1. Back emf when the current is $i$: $\varepsilon = -L\dfrac{di}{dt}$
2. The source must supply $+L\dfrac{di}{dt}$ to keep the current growing  — *(work is done against the back emf)*
3. Work in time $dt$: $dW = \varepsilon\,i\,dt = L\dfrac{di}{dt}\,i\,dt$
4. $dW = L\,i\,di$  — *($dt$ cancels)*
5. $W = \displaystyle\int_0^I L\,i\,di$
6. $W = L\left[\dfrac{i^2}{2}\right]_0^I$
7. $U = \dfrac{1}{2}LI^2$
8. **Energy density.** For a solenoid, $L = \mu_0n^2Al$ and $B = \mu_0nI$, so $I = \dfrac{B}{\mu_0 n}$
9. $U = \dfrac{1}{2}\left(\mu_0n^2Al\right)\left(\dfrac{B}{\mu_0n}\right)^2 = \dfrac{B^2}{2\mu_0}\left(Al\right)$
10. $Al$ is the volume inside the solenoid  — *(where the field actually is)*
11. $u = \dfrac{U}{Al} = \dfrac{B^2}{2\mu_0}$

**Result:** $U = \dfrac{1}{2}LI^{2} \qquad u = \dfrac{B^{2}}{2\mu_0}$

*Compare with PD12: $\tfrac12CV^2 \leftrightarrow \tfrac12LI^2$ and $\tfrac12\varepsilon_0E^2 \leftrightarrow B^2/2\mu_0$. Note $\mu_0$ sits in the denominator where $\varepsilon_0$ sat in the numerator.*

##### `PD32` Emf of an AC generator — *3 marks*

> A coil of $N$ turns and area $A$ rotating with angular velocity $\omega$ in a uniform field $\vec B$. The field does not change and the area does not change — what changes is the *angle*, and that alone is enough to induce an emf.

**Figure.** A rectangular coil rotating in a uniform horizontal magnetic field, with its normal at angle omega t to the field. Below, a sine curve shows the induced emf against time, peaking when the coil's plane is parallel to the field.

*Nothing about the field or the coil changes — only the orientation. The emf peaks where the flux is momentarily zero but changing fastest, which is when the coil's plane lies *along* the field.*

1. At time $t$ the normal to the coil makes angle $\theta = \omega t$ with $\vec B$
2. Flux through one turn: $\Phi = BA\cos\omega t$  — *(the angle is measured from the normal, not the plane)*
3. Flux linkage of $N$ turns: $N\Phi = NBA\cos\omega t$
4. Faraday's law: $\varepsilon = -\dfrac{d}{dt}\left(N\Phi\right)$
5. $\varepsilon = -NBA\dfrac{d}{dt}\left(\cos\omega t\right)$
6. $\dfrac{d}{dt}\cos\omega t = -\omega\sin\omega t$
7. $\varepsilon = NBA\omega\sin\omega t$
8. Writing $\varepsilon_0 = NBA\omega$: $\varepsilon = \varepsilon_0\sin\omega t$
9. Current through resistance $R$: $I = \dfrac{\varepsilon_0}{R}\sin\omega t$

**Result:** $\varepsilon = NBA\omega\sin\omega t = \varepsilon_0\sin\omega t, \qquad \varepsilon_0 = NBA\omega$

*Emf is **maximum** when $\omega t = 90°$ — the coil's plane parallel to $\vec B$, flux instantaneously zero. It is **zero** when the plane is perpendicular and the flux is maximum. That inversion is the standard trap, and it follows from $\varepsilon$ depending on the *rate of change* of flux, not the flux.*

#### `CH 7` Alternating Current — *5 derivations*

##### `PD33` RMS value of an alternating current — *3 marks*

> An alternating current $i = i_0\sin\omega t$ passes through a resistance $R$. Its average over a full cycle is zero, so the average current cannot be what a meter reads. Instead define the **rms** value as the steady DC current that would produce the same heating in the same time.

**Figure.** Two curves over one cycle: the sinusoidal current, which is negative for half the cycle and averages to zero, and the squared current, which is positive throughout and averages to half the square of the peak.

*Squaring is what rescues the average. The current itself spends half its time negative; its square never does, and its mean value is exactly half the peak squared.*

1. Heat produced by a steady current $I_{\text{rms}}$ in time $T$: $H_{DC} = I_{\text{rms}}^2RT$
2. Heat produced by the alternating current in the same time: $H_{AC} = \displaystyle\int_0^T i^2R\,dt$
3. $H_{AC} = \displaystyle\int_0^T i_0^2\sin^2(\omega t)\,R\,dt$
4. $\sin^2\omega t = \dfrac{1 - \cos 2\omega t}{2}$  — *(the identity that makes this integrable)*
5. $H_{AC} = \dfrac{i_0^2R}{2}\left[\displaystyle\int_0^T dt - \int_0^T \cos2\omega t\,dt\right]$
6. $\displaystyle\int_0^T\cos2\omega t\,dt = 0$  — *(a cosine integrated over a whole number of cycles vanishes)*
7. $H_{AC} = \dfrac{i_0^2RT}{2}$
8. Setting $H_{DC} = H_{AC}$: $I_{\text{rms}}^2RT = \dfrac{i_0^2RT}{2}$
9. $I_{\text{rms}}^2 = \dfrac{i_0^2}{2}$
10. $I_{\text{rms}} = \dfrac{i_0}{\sqrt2} \approx 0.707\,i_0$

**Result:** $I_{\text{rms}} = \dfrac{i_0}{\sqrt2} \qquad E_{\text{rms}} = \dfrac{e_0}{\sqrt2}$

*Mains "220 V" is rms, so the peak is $220\sqrt2 \approx 311\ \text{V}$. The **mean over a half cycle** is a different quantity, $2i_0/\pi \approx 0.637i_0$; over a full cycle the mean is zero.*

##### `PD34` AC through a pure inductor — reactance and phase lag — *3 marks*

> A source $e = e_0\sin\omega t$ across a pure inductance $L$ with no resistance. The inductor produces a back emf $L\,di/dt$; with no resistance to drop voltage across, the applied emf must exactly balance that back emf at every instant.

**Figure.** Voltage and current curves for a pure inductor: the current sine wave lags the voltage sine wave by a quarter of a cycle, reaching its peak ninety degrees after the voltage does.

*The current peaks a quarter cycle after the voltage does. The inductor resists *changes* in current, so the current is always playing catch-up.*

1. Applied emf: $e = e_0\sin\omega t$
2. Back emf across the inductor: $-L\dfrac{di}{dt}$
3. With no resistance, the net emf round the loop is zero: $e = L\dfrac{di}{dt}$  — *(there is nothing else to drop voltage across)*
4. $di = \dfrac{e_0}{L}\sin(\omega t)\,dt$
5. $i = \dfrac{e_0}{L}\displaystyle\int\sin\omega t\,dt = \dfrac{e_0}{L}\left(-\dfrac{\cos\omega t}{\omega}\right)$
6. $i = -\dfrac{e_0}{\omega L}\cos\omega t$
7. $-\cos\omega t = \sin\left(\omega t - \dfrac{\pi}{2}\right)$  — *(rewriting so the phase relation is visible)*
8. $i = \dfrac{e_0}{\omega L}\sin\left(\omega t - \dfrac{\pi}{2}\right)$
9. Comparing with $i = i_0\sin\left(\omega t - \phi\right)$: $i_0 = \dfrac{e_0}{\omega L}$ and $\phi = \dfrac{\pi}{2}$
10. Comparing $i_0 = e_0/\omega L$ with Ohm's law form $i_0 = e_0/X$: $X_L = \omega L$

**Result:** $X_L = \omega L = 2\pi f L$, and the current **lags** the voltage by $\dfrac{\pi}{2}$

*$X_L \propto f$, so an inductor blocks high frequencies and passes DC freely — at $f=0$, $X_L = 0$. That is why it is called a choke.*

##### `PD35` AC through a pure capacitor — reactance and phase lead — *3 marks*

> The same source across a pure capacitance $C$. Here the applied emf equals the potential difference across the plates at every instant, and the current is the rate at which charge accumulates on them.

> **Mirror of PD34.** There the voltage was a derivative of the current; here the current is a derivative of the voltage. That single swap is why the phase shift reverses.

**Figure.** Voltage and current curves for a pure capacitor: the current sine wave leads the voltage sine wave by a quarter of a cycle, reaching its peak ninety degrees before the voltage does.

*The current peaks a quarter cycle *before* the voltage. Charge has to flow onto the plates before a potential difference can appear across them, so the current runs ahead.*

1. Applied emf equals the plate potential difference: $e_0\sin\omega t = \dfrac{q}{C}$
2. $q = Ce_0\sin\omega t$
3. $i = \dfrac{dq}{dt}$  — *(current is the rate of charge accumulation)*
4. $i = Ce_0\omega\cos\omega t$
5. $\cos\omega t = \sin\left(\omega t + \dfrac{\pi}{2}\right)$
6. $i = \omega Ce_0\sin\left(\omega t + \dfrac{\pi}{2}\right)$
7. Comparing with $i = i_0\sin\left(\omega t + \phi\right)$: $i_0 = \omega Ce_0$ and $\phi = +\dfrac{\pi}{2}$
8. Writing $i_0 = \dfrac{e_0}{X_C}$: $X_C = \dfrac{1}{\omega C}$

**Result:** $X_C = \dfrac{1}{\omega C} = \dfrac{1}{2\pi f C}$, and the current **leads** the voltage by $\dfrac{\pi}{2}$

*$X_C \propto 1/f$, the opposite of the inductor: a capacitor blocks DC completely and passes high frequencies. Remember the pair as **CIVIL** — in **C**, **I** leads **V**; **V** leads **I** in **L**.*

##### `PD36` Series LCR circuit — impedance, phase angle and resonance — *5 marks*

> R, L and C in series across $e = e_0\sin\omega t$. The same current flows through all three, but each develops its voltage at a different phase — $V_R$ in phase with $I$, $V_L$ leading by $90°$, $V_C$ lagging by $90°$. So the three voltages must be added as **phasors**, not as numbers.

**Figure.** A phasor diagram for a series LCR circuit: V-R along the horizontal current direction, V-L pointing up, V-C pointing down, their difference combining with V-R by Pythagoras to give the applied voltage E at phase angle phi.

*$V_L$ and $V_C$ point in exactly opposite directions, so they subtract before combining with $V_R$ at right angles. That single geometric fact is the entire derivation.*

1. The same current $I$ flows through all three elements  — *(series)*
2. $V_R = IR$, in phase with $I$
3. $V_L = IX_L$, leading $I$ by $90°$  — *(PD34)*
4. $V_C = IX_C$, lagging $I$ by $90°$  — *(PD35)*
5. $V_L$ and $V_C$ are antiparallel, so their resultant has magnitude $\left|V_L - V_C\right|$
6. That resultant is perpendicular to $V_R$, so combine by Pythagoras:
7. $E = \sqrt{V_R^2 + \left(V_L-V_C\right)^2}$
8. $E = \sqrt{\left(IR\right)^2 + \left(IX_L - IX_C\right)^2} = I\sqrt{R^2+\left(X_L-X_C\right)^2}$
9. Comparing with $E = IZ$: $Z = \sqrt{R^2+\left(X_L-X_C\right)^2}$
10. From the same triangle, $\tan\phi = \dfrac{V_L-V_C}{V_R} = \dfrac{X_L-X_C}{R}$
11. **Resonance.** $Z$ is least when $X_L = X_C$  — *(the squared term vanishes, and it can never be negative)*
12. $\omega L = \dfrac{1}{\omega C}$, so $\omega^2 = \dfrac{1}{LC}$
13. $\omega_r = \dfrac{1}{\sqrt{LC}}$, $f_r = \dfrac{1}{2\pi\sqrt{LC}}$
14. At resonance $Z = R$ (minimum), $I = E/R$ (maximum) and $\phi = 0$

**Result:** $Z = \sqrt{R^{2}+(X_L-X_C)^{2}}, \quad \tan\phi = \dfrac{X_L-X_C}{R}, \quad \omega_r = \dfrac{1}{\sqrt{LC}}$

*$X_L \gt X_C$ makes the circuit inductive and the current lag; $X_L \lt X_C$ makes it capacitive and the current lead. Because $V_L$ and $V_C$ oppose, either can exceed the supply voltage — that is not an error.*

##### `PD37` Average power in an AC circuit, and the wattless current — *3 marks*

> A circuit in which the current lags (or leads) the voltage by $\phi$. Instantaneous power is $ei$, but that oscillates; what a meter and an electricity bill record is its average over a full cycle.

**Figure.** A phasor diagram resolving the current into two components: one along the voltage, I cosine phi, which carries all the power, and one perpendicular to it, I sine phi, the wattless component which carries none.

*Only the component of current *along* the voltage does net work over a cycle. The perpendicular component stores energy for a quarter cycle and gives it all back in the next — hence "wattless".*

1. $e = e_0\sin\omega t$ and $i = i_0\sin(\omega t - \phi)$
2. Instantaneous power: $P = ei = e_0i_0\sin\omega t\,\sin(\omega t-\phi)$
3. $\sin A\sin B = \tfrac12\left[\cos(A-B) - \cos(A+B)\right]$  — *(product-to-sum identity)*
4. $P = \dfrac{e_0i_0}{2}\left[\cos\phi - \cos(2\omega t - \phi)\right]$
5. Average over a full cycle: the second term averages to zero  — *(a cosine of $2\omega t$ over a whole number of cycles)*
6. $P_{\text{avg}} = \dfrac{e_0i_0}{2}\cos\phi$
7. $\dfrac{e_0i_0}{2} = \dfrac{e_0}{\sqrt2}\cdot\dfrac{i_0}{\sqrt2} = E_{\text{rms}}I_{\text{rms}}$  — *(PD33)*
8. $P_{\text{avg}} = E_{\text{rms}}I_{\text{rms}}\cos\phi$
9. $\cos\phi$ is the **power factor**, equal to $\dfrac{R}{Z}$  — *(from PD36's triangle)*
10. For a pure inductor or capacitor $\phi = 90°$, so $\cos\phi = 0$ and $P_{\text{avg}} = 0$

**Result:** $P_{\text{avg}} = E_{\text{rms}}I_{\text{rms}}\cos\phi, \qquad \cos\phi = \dfrac{R}{Z}$

*Step 10 is the wattless-current result: a pure reactance consumes **no average power at all**. Energy flows into it for a quarter cycle and back out in the next. At resonance $\phi = 0$ and the power factor is 1.*

#### `CH 8` Electromagnetic Waves — *1 derivation*

##### `PD38` Displacement current, and the inconsistency it repairs — *3 marks*

> A parallel plate capacitor being charged. Apply Ampère's circuital law to a loop around the connecting wire — but evaluate it over two *different* surfaces bounded by that same loop: one cutting the wire, one bulging out to pass between the plates. Ampère's law as it stands gives two different answers, which cannot both be right.

**Figure.** A charging capacitor with an Amperian loop around the connecting wire. Surface one is a flat disc cut by the wire and carrying conduction current; surface two is a bag-shaped surface bounded by the same loop that passes between the plates where no charge flows, yet the changing electric flux there supplies an equal displacement current.

*Both dashed surfaces are bounded by the *same* loop, so Ampère's law must give the same answer for both. $S_1$ is pierced by the wire; $S_2$ passes through the empty gap. Something must be flowing through $S_2$ too.*

1. Ampère's law: $\displaystyle\oint\vec B\cdot d\vec l = \mu_0 I$, where $I$ is the current crossing *any* surface bounded by the loop
2. Take $S_1$, the flat disc cut by the wire: current crossing it is $I_c$, so the law gives $\mu_0I_c$
3. Take $S_2$, bounded by the same loop but passing between the plates: **no charge crosses it at all**, so the law gives $0$
4. The same left-hand side cannot equal two different things — Ampère's law as stated is **incomplete**  — *(this contradiction is the point of the derivation)*
5. Between the plates, $E = \dfrac{\sigma}{\varepsilon_0} = \dfrac{Q}{\varepsilon_0 A}$
6. Electric flux through $S_2$: $\Phi_E = EA = \dfrac{Q}{\varepsilon_0}$
7. Differentiating: $\dfrac{d\Phi_E}{dt} = \dfrac{1}{\varepsilon_0}\dfrac{dQ}{dt}$
8. $\dfrac{dQ}{dt} = I_c$  — *(the charge arriving on the plate is carried by the conduction current)*
9. $\varepsilon_0\dfrac{d\Phi_E}{dt} = I_c$
10. Define the **displacement current** $I_d = \varepsilon_0\dfrac{d\Phi_E}{dt}$; then $I_d = I_c$, and both surfaces now agree
11. Ampère–Maxwell law: $\displaystyle\oint\vec B\cdot d\vec l = \mu_0\left(I_c + \varepsilon_0\dfrac{d\Phi_E}{dt}\right)$

**Result:** $I_d = \varepsilon_0\dfrac{d\Phi_E}{dt} \qquad \oint\vec B\cdot d\vec l = \mu_0\left(I_c + I_d\right)$

*Displacement current is not a flow of charge — it is a changing electric field acting like one. Its consequence is the whole chapter: a changing $\vec E$ makes a $\vec B$, a changing $\vec B$ makes an $\vec E$, and the pair propagates as a wave at $c = 1/\sqrt{\mu_0\varepsilon_0}$.*

#### `CH 9` Ray Optics and Optical Instruments — *7 derivations*

*Written from NCERT and from the published **Ray Optics to 9.4** page, pending processing of this chapter's eighteen lecture videos. The physics is settled; only the teacher's own emphasis is still to come.*

##### `PD39` Mirror formula for a concave mirror — *3–5 marks*

> A concave mirror with pole P, focus F and centre of curvature C. Object AB stands on the principal axis beyond C, B on the axis; a real inverted image A′B′ forms. Ray AD leaves the top of the object parallel to the axis, strikes the mirror at D and reflects through F. DN is the perpendicular from D to the axis. The aperture is small.

**Figure.** A concave mirror with object arrow AB beyond the centre of curvature and a smaller inverted real image A prime B prime between C and F. One ray runs parallel to the axis and reflects through F; a second passes through C and returns along itself. The similar triangle pairs used in the derivation are visible.

*Two pairs of similar triangles do all the work: △ABC with △A′B′C (vertically opposite at C), and △DNF with △A′B′F (vertically opposite at F). The small-aperture assumption is what lets N be treated as coincident with P.*

1. In △ABC and △A′B′C: $\angle ABC = \angle A'B'C = 90°$
2. $\angle ACB = \angle A'CB'$  — *(vertically opposite)*
3. So △ABC ~ △A′B′C
4. $\dfrac{AB}{A'B'} = \dfrac{BC}{B'C}$  …(i)
5. In △DNF and △A′B′F: $\angle DNF = \angle A'B'F = 90°$
6. $\angle DFN = \angle A'FB'$  — *(vertically opposite)*
7. So △DNF ~ △A′B′F, giving $\dfrac{DN}{A'B'} = \dfrac{NF}{B'F}$
8. $DN = AB$  — *(DN is the height of the parallel ray, equal to the object height)*
9. $\dfrac{AB}{A'B'} = \dfrac{NF}{B'F}$  …(ii)
10. From (i) and (ii): $\dfrac{BC}{B'C} = \dfrac{NF}{B'F}$
11. Small aperture, so N lies very close to P and $NF \approx PF$  — *(the one approximation — state it)*
12. $\dfrac{BC}{B'C} = \dfrac{PF}{B'F}$
13. $BC = PB - PC$, $B'C = PC - PB'$, $B'F = PB' - PF$
14. Sign convention: $PB = -u$, $PB' = -v$, $PF = -f$, $PC = -R = -2f$
15. $\dfrac{-u+2f}{-2f+v} = \dfrac{-f}{-v+f}$
16. Cross-multiplying: $(-u+2f)(-v+f) = (-f)(-2f+v)$
17. $uv - uf - 2fv + 2f^2 = 2f^2 - fv$
18. $uv - uf - 2fv = -fv$
19. $uv - uf - fv = 0$
20. $uv = uf + fv$
21. Divide throughout by $uvf$: $\dfrac{1}{f} = \dfrac{1}{v} + \dfrac{1}{u}$

**Result:** $\dfrac{1}{v} + \dfrac{1}{u} = \dfrac{1}{f}$

*Note the **plus** sign — the lens formula has a minus. Magnification follows from the ray striking the pole, where the axis is the normal: $m = h'/h = -v/u$.*

##### `PD40` Refraction at a single spherical surface — *3 marks*

> A single convex refracting surface of radius $R$ separating a medium of index $n_1$ from one of index $n_2$. A point object O on the axis gives an image at I. Take a ray OM striking the surface at M, close to the pole P so all angles are small.

> **Shared setup with PD41.** The lens maker's formula is this derivation applied twice — once at each face of the lens. Learn this one properly and the next is bookkeeping.

**Figure.** A convex refracting surface separating medium n1 on the left from n2 on the right, with centre of curvature C. A ray from the object O on the axis meets the surface at M, bends towards the normal, and converges to the image I; the angles alpha, beta and gamma are marked at O, I and C.

*The normal at M is the radius MC, so the angles $\alpha$, $\beta$ and $\gamma$ at O, I and C are what connect the ray geometry to Snell's law. All are small, so each equals its own tangent.*

1. MC is the normal at M  — *(a radius always meets a sphere at right angles)*
2. Angle of incidence $i = \alpha + \gamma$  — *(exterior angle of △OMC)*
3. Angle of refraction $r = \gamma - \beta$  — *(exterior angle of △MCI)*
4. Snell's law: $n_1\sin i = n_2\sin r$
5. All angles are small, so $\sin i \approx i$ and $\sin r \approx r$  — *(paraxial approximation)*
6. $n_1\left(\alpha+\gamma\right) = n_2\left(\gamma-\beta\right)$
7. For small angles, $\alpha \approx \tan\alpha = \dfrac{MP}{PO}$, $\beta \approx \dfrac{MP}{PI}$, $\gamma \approx \dfrac{MP}{PC}$
8. $n_1\left(\dfrac{MP}{PO} + \dfrac{MP}{PC}\right) = n_2\left(\dfrac{MP}{PC} - \dfrac{MP}{PI}\right)$
9. $MP$ cancels throughout  — *(which is why the result holds for every paraxial ray, not just this one)*
10. Sign convention: $PO = -u$, $PI = +v$, $PC = +R$
11. $n_1\left(\dfrac{1}{-u} + \dfrac{1}{R}\right) = n_2\left(\dfrac{1}{R} - \dfrac{1}{v}\right)$
12. $-\dfrac{n_1}{u} + \dfrac{n_1}{R} = \dfrac{n_2}{R} - \dfrac{n_2}{v}$
13. $\dfrac{n_2}{v} - \dfrac{n_1}{u} = \dfrac{n_2 - n_1}{R}$

**Result:** $\dfrac{n_2}{v} - \dfrac{n_1}{u} = \dfrac{n_2-n_1}{R}$

##### `PD41` Lens maker's formula, and the thin lens formula — *5 marks*

> A thin lens of material index $n$ in air, with surfaces of radii $R_1$ and $R_2$. Refraction happens twice. Treat the first surface alone: it would form an image $I_1$. Then feed that image in as the *object* for the second surface, which produces the final image I.

**Figure.** A thin biconvex lens with an object O on the left. The first surface of radius R1 would form an intermediate image I1 to the right; that image acts as the object for the second surface of radius R2, which forms the final image I.

*The intermediate image $I_1$ never actually forms — the second surface intercepts the light first. But treating it as the object for that second refraction is exactly what makes the two-step calculation work.*

1. **At the first surface** ($n_1 = 1$ air, $n_2 = n$ glass, radius $R_1$), the image is at $v_1$:
2. $\dfrac{n}{v_1} - \dfrac{1}{u} = \dfrac{n-1}{R_1}$  …(i)  — *(PD40)*
3. **At the second surface**, light goes from glass into air, so $n_1 = n$ and $n_2 = 1$, radius $R_2$
4. The object for it is $I_1$, at distance $v_1$  — *(the lens is thin, so both surfaces are effectively at the same place)*
5. $\dfrac{1}{v} - \dfrac{n}{v_1} = \dfrac{1-n}{R_2}$  …(ii)
6. Add (i) and (ii): the $\dfrac{n}{v_1}$ terms cancel  — *(this cancellation is the point of doing it in two steps)*
7. $\dfrac{1}{v} - \dfrac{1}{u} = \dfrac{n-1}{R_1} + \dfrac{1-n}{R_2}$
8. $\dfrac{1}{v} - \dfrac{1}{u} = (n-1)\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right)$
9. For an object at infinity, $u = \infty$ and $v = f$ by definition of focal length
10. $\dfrac{1}{f} = (n-1)\left(\dfrac{1}{R_1} - \dfrac{1}{R_2}\right)$  — *(the lens maker's formula)*
11. Substituting back into step 8: $\dfrac{1}{v} - \dfrac{1}{u} = \dfrac{1}{f}$

**Result:** $\dfrac{1}{f} = (n-1)\left(\dfrac{1}{R_1}-\dfrac{1}{R_2}\right) \qquad \dfrac{1}{v}-\dfrac{1}{u} = \dfrac{1}{f}$

*$n$ is the index of the lens **relative to its surroundings**. A glass lens in water has a much longer focal length; if the two indices matched, $1/f$ would be zero and the lens would disappear optically.*

##### `PD42` Two thin lenses in contact — *2–3 marks*

> Two thin lenses of focal lengths $f_1$ and $f_2$ placed in contact. The image formed by the first acts as the object for the second — the same chaining trick as PD41, one level up.

**Figure.** Two thin lenses in contact with an object on the left. The first lens alone would form an intermediate image, which then serves as the object for the second lens, giving the final image closer in.

*The intermediate image $I_1$ is the object for the second lens. Because the lenses touch, its distance is measured from the same point for both — which is what lets the terms cancel.*

1. **First lens:** $\dfrac{1}{v_1} - \dfrac{1}{u} = \dfrac{1}{f_1}$  …(i)
2. **Second lens:** its object is $I_1$ at distance $v_1$, and its image is the final one at $v$
3. $\dfrac{1}{v} - \dfrac{1}{v_1} = \dfrac{1}{f_2}$  …(ii)
4. Add (i) and (ii): the $\dfrac{1}{v_1}$ terms cancel
5. $\dfrac{1}{v} - \dfrac{1}{u} = \dfrac{1}{f_1} + \dfrac{1}{f_2}$
6. But for the equivalent single lens, $\dfrac{1}{v} - \dfrac{1}{u} = \dfrac{1}{F}$
7. $\dfrac{1}{F} = \dfrac{1}{f_1} + \dfrac{1}{f_2}$
8. Since $P = 1/f$: $P = P_1 + P_2$

**Result:** $\dfrac{1}{F} = \dfrac{1}{f_1}+\dfrac{1}{f_2} \qquad P = P_1+P_2$

*Powers simply add, which is why optometrists work in dioptres. $f$ must be in **metres** for $P$ to come out in dioptres.*

##### `PD43` Refraction through a prism, and minimum deviation — *5 marks*

> A prism of refracting angle $A$. A ray enters at angle $i$, refracts to $r_1$ inside, travels to the second face where it meets it at $r_2$, and emerges at $e$. The total deviation is $\delta$. Two quadrilateral/triangle angle sums give the whole result.

**Figure.** A triangular prism with a ray entering the left face at angle i, bending to r1 inside, meeting the right face at r2 and emerging at angle e. The prism angle A is at the apex and the total deviation delta is the angle between the incident ray produced and the emergent ray.

*The ray bends towards the normal entering the denser prism and away from it on leaving, so both bends turn it the same way — which is why the deviations add rather than cancel.*

1. In the quadrilateral formed by the two faces and the two normals, the angles at the two faces are $90°$ each
2. So the angle between the normals is $180° - A$
3. In the triangle formed by the two normals and the ray inside: $r_1 + r_2 + (180° - A) = 180°$
4. $r_1 + r_2 = A$  …(i)  — *(the first key relation)*
5. Deviation at the first face is $(i - r_1)$; at the second face $(e - r_2)$
6. Total deviation $\delta = (i - r_1) + (e - r_2)$  — *(both bends turn the ray the same way, so they add)*
7. $\delta = (i+e) - (r_1+r_2)$
8. Using (i): $\delta = i + e - A$
9. $A + \delta = i + e$  …(ii)  — *(the second key relation)*
10. **At minimum deviation** the ray passes symmetrically: $i = e$ and $r_1 = r_2 = r$
11. From (i): $2r = A$, so $r = \dfrac{A}{2}$
12. From (ii): $A + \delta_m = 2i$, so $i = \dfrac{A+\delta_m}{2}$
13. Snell's law at the first face: $n = \dfrac{\sin i}{\sin r}$
14. $n = \dfrac{\sin\left(\dfrac{A+\delta_m}{2}\right)}{\sin\left(\dfrac{A}{2}\right)}$

**Result:** $r_1+r_2 = A, \quad A+\delta = i+e, \quad n = \dfrac{\sin\!\left(\frac{A+\delta_m}{2}\right)}{\sin\!\left(\frac{A}{2}\right)}$

*For a **thin** prism all angles are small, $\sin\theta\approx\theta$, and this collapses to $\delta = (n-1)A$. The graph of $\delta$ against $i$ is a curve with one minimum, so every deviation except $\delta_m$ corresponds to two different angles of incidence.*

##### `PD44` Magnifying power of a compound microscope — *5 marks*

> Two converging lenses: an objective of short focal length $f_o$ forming a real, inverted, magnified image inside the tube, and an eyepiece of focal length $f_e$ used as a simple magnifier on that image. The total magnification is the product of the two.

**Figure.** A compound microscope: the object just outside the objective's focus forms a real inverted enlarged image inside the tube, and the eyepiece magnifies that intermediate image to give the final much larger virtual image seen by the eye.

*The objective does the first magnification and hands its real image to the eyepiece, which magnifies again. Two stages in series, so the magnifications multiply.*

1. Magnification of the objective: $m_o = \dfrac{h'}{h} = \dfrac{v_o}{u_o}$  — *(linear magnification of a lens)*
2. The eyepiece is used as a simple magnifier on that intermediate image
3. For a simple magnifier with the final image at the near point $D$: $m_e = 1 + \dfrac{D}{f_e}$
4. Total magnification $m = m_o \times m_e$  — *(two stages in series multiply)*
5. $m = \dfrac{v_o}{u_o}\left(1 + \dfrac{D}{f_e}\right)$
6. For the **relaxed eye**, the final image is at infinity and $m_e = \dfrac{D}{f_e}$
7. $m = \dfrac{v_o}{u_o}\cdot\dfrac{D}{f_e}$
8. In practice the object sits just outside $F_o$, so $u_o \approx f_o$, and the image forms near the eyepiece, so $v_o \approx L$, the tube length
9. $m \approx \dfrac{L}{f_o}\cdot\dfrac{D}{f_e}$

**Result:** $m = \dfrac{v_o}{u_o}\left(1+\dfrac{D}{f_e}\right)$  ·  relaxed eye: $m \approx \dfrac{L}{f_o}\cdot\dfrac{D}{f_e}$

*High magnification needs **both** $f_o$ and $f_e$ small — that is why microscope lenses are tiny. $D = 25\ \text{cm}$, the least distance of distinct vision.*

##### `PD45` Magnifying power of an astronomical telescope — *3–5 marks*

> A telescope viewing a distant object, so the rays arrive parallel and subtend angle $\alpha$ at the objective. The objective forms a real image at its focal plane; the eyepiece views that image, and it subtends the larger angle $\beta$ at the eye. Magnifying power is the ratio of those two angles.

**Figure.** An astronomical telescope in normal adjustment: parallel rays from a distant object arrive at angle alpha, the objective forms a real inverted image at its focal plane, and the eyepiece placed one focal length beyond sends parallel rays to the eye at the larger angle beta.

*A telescope cannot make a distant star bigger — it makes it subtend a bigger *angle*. That is why magnifying power here is a ratio of angles, not of lengths.*

1. Magnifying power $m = \dfrac{\beta}{\alpha}$  — *(angle subtended by the image at the eye ÷ angle subtended by the object)*
2. Both angles are small, so $\alpha \approx \tan\alpha$ and $\beta \approx \tan\beta$
3. The intermediate image has height $h$ at the objective's focal plane
4. $\tan\alpha = \dfrac{h}{f_o}$  — *(the object is at infinity, so its image forms at the focal plane)*
5. **Normal adjustment**: the final image is at infinity, so the intermediate image sits at the eyepiece's focus
6. $\tan\beta = \dfrac{h}{f_e}$
7. $m = \dfrac{h/f_e}{h/f_o}$
8. $h$ cancels: $m = \dfrac{f_o}{f_e}$
9. Length of the telescope $L = f_o + f_e$  — *(the two focal points coincide in normal adjustment)*
10. If instead the final image is at the near point: $m = \dfrac{f_o}{f_e}\left(1 + \dfrac{f_e}{D}\right)$

**Result:** $m = \dfrac{f_o}{f_e}$,  $L = f_o+f_e$  (normal adjustment)

*The exact **opposite** requirement from a microscope: a telescope objective wants a **long** focal length, a microscope objective a short one. A large objective also gathers more light, which is why research telescopes are big. A reflecting telescope replaces the objective lens with a concave mirror and so has no chromatic aberration at all.*

Built from the notes for Chapters 1–8 in this repository, which were grounded against the lecture board frames rather than the ASR transcripts. Chapter 9 is written from NCERT and from the published **Ray Optics to 9.4** page, pending processing of that chapter's eighteen lecture videos.

Every result here also appears, without its proof, on the companion page **Every Physics Formula**.

### Chapter 1 · Electric Charges and Fields — lecture notes

#### Introduction to Electrostatics: Frictional Electricity, the Gold Leaf Electroscope, and Basic Properties of Charge

**NCERT sections covered:** 1.2, 1.4

##### Introduction (NCERT 1.1)
Electrostatics = "electro" (charge) + "static" (at rest): the study of charges at rest. This chapter builds up in stages: frictional electricity $\to$ electric field $\to$ electric potential $\to$ applications (capacitors) -- each stage depends on the one before it (e.g. capacitors can't be understood without electric field, which can't be understood without first understanding charge itself).

##### Frictional electricity (NCERT 1.2)
Rubbing two different materials against each other transfers charge between them (the everyday "shock" felt in winter, or hair sticking to a comb, are both this phenomenon). Which material ends up positively vs. negatively charged is decided by how tightly each material's valence electrons are bound: the material whose electrons are *easier to pull away* loses electrons (becomes positive); the other gains those electrons (becomes negative).

- **Silk cloth + glass rod:** glass becomes positive, silk becomes negative.
- **Silk cloth + ebonite rod:** silk becomes positive, ebonite becomes negative.

(Silk isn't intrinsically "always negative" -- its sign depends on what it's rubbed against.)

**Naming:** Benjamin Franklin named the two kinds of charge *positive* and *negative*. An atom as a whole is electrically **neutral**: equal numbers of positive and negative charges. SI unit of charge: the **coulomb (C)**.

###### Detecting charge: the Gold Leaf Electroscope
An insulated metal knob (insulation prevents leakage and shields against stray air currents affecting the reading) connects via a wire to two thin gold leaves sealed inside a container. Touching a charged rod to the knob distributes charge onto both leaves; since like charges repel, the leaves diverge from each other. The degree of divergence indicates the strength of the charge present.

##### Basic properties of electric charge (NCERT 1.4)

###### 1. Conservation of charge (1.4.2)
Charge can neither be created nor destroyed, only **transferred** from one body to another. Total charge before and after any process (rubbing, a nuclear reaction, etc.) is unchanged.

**Example:** alpha decay $\,^{238}_{92}\text{U} \to \,^{234}_{90}\text{Th} + \,^{4}_{2}\text{He}$ conserves both mass number ($238=234+4$) and atomic/charge number ($92=90+2$).

###### 2. Additivity of charges (1.4.1)
Charges combine like ordinary signed algebraic quantities. Example: $-e,-2e,+3e,+4e$ together give a total charge
$$q = -e-2e+3e+4e = +4e$$

###### 3. Quantisation of charge (1.4.3)
The charge on any body is always an **integral multiple** of the elementary charge $e$ (the electron's charge):
$$q = \pm ne$$
Never a fraction like $e/3$ or $-2e/3$. **Quarks** are the well-known exception, carrying fractional charges ($+e/3$, $-e/3$, $\pm2e/3$) -- but they only ever exist in bound combinations whose *total* charge is again an integral multiple of $e$, so quantisation still holds for every observable free particle.

#### Electrostatic Induction, Charge Unit Conversions, and Coulomb's Law

**NCERT sections covered:** 1.4, 1.5

##### Electrostatic induction

Charging a conducting body **without physical contact**, by bringing a charged rod nearby:

1. Bring a negatively-charged rod near a grounded conducting sphere (mounted on an insulating stand). By induction, positive charge accumulates on the near side (attracted toward the rod) and negative charge on the far side (repelled free electrons).
2. Ground the sphere: the repelled negative charges flow away into the ground (an effectively infinite charge reservoir), while the positive charges stay put, held by attraction to the rod.
3. Remove the ground connection first, *then* remove the rod.
4. The remaining positive charge redistributes itself uniformly over the sphere (charges settle into the configuration of minimum potential energy) — the sphere is now charged **positively**, without ever touching a charged body to it.

(The gold leaf electroscope shows the same effect: bringing a charged rod near *without touching* still induces a charge separation that causes the leaves to diverge.)

##### Worked numerical: charge content of water
How many positive and negative (elementary) charges are in $250$ mL of water? Using $1$ mL $=1$ g, water's molar mass $18$ g/mol ($2\times1+16$), Avogadro's number $6.023\times10^{23}$ molecules/mol, and $10$ protons + $10$ electrons per H$_2$O molecule (O contributes 8, each H contributes 1):
$$\text{molecules in } 250\text{ g} = 6.023\times10^{23}\times\frac{250}{18}$$
Total positive charge count = total negative charge count = $10\times$ that number of molecules.

##### Coulomb's law (NCERT 1.5)

**Recap — Newton's law of gravitation:** $F = \dfrac{Gm_1m_2}{r^2}$ — always attractive, independent of the medium between the masses (a universal law).

**Coulomb's law:** for two **point charges** $Q_1,Q_2$ (valid only when their separation is much larger than their own physical size — the electrostatic analogue of a "point object") separated by $r$:
$$F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r^2} = k\frac{Q_1Q_2}{r^2},\qquad k=\frac{1}{4\pi\varepsilon_0}=9\times10^9~\text{N m}^2\text{C}^{-2}$$

**Compared with gravity:** both are central forces (act along the line joining the two objects) and both obey Newton's third law ($\vec F_{12}=-\vec F_{21}$) — but Coulomb's force can be attractive *or* repulsive (gravity is always attractive), and it *depends on the medium* between the charges (gravity doesn't).

###### Definition of 1 coulomb
Setting $Q_1=Q_2=1$ C, $r=1$ m: $F = 9\times10^9$ N. So **1 coulomb** is the charge that, placed 1 m from an identical charge in vacuum, repels it with a force of $9\times10^9$ N — evidently an enormous unit for practical electrostatics.

###### A note on mass and charging
Charging a body very slightly changes its mass: charging it **negatively** (adding electrons) **increases** mass; charging it **positively** (removing electrons) **decreases** mass.

###### Why the coulomb is "too big" a unit, and sub-units (NCERT 1.4)
Practical electrostatics uses smaller sub-units: $1~\text{mC}=10^{-3}$ C, $1~\mu\text{C}=10^{-6}$ C, $1~\text{nC}=10^{-9}$ C. Since charge is quantised ($Q=ne$), 1 coulomb corresponds to
$$n = \frac{1}{1.6\times10^{-19}} = \frac{10^{19}}{1.6} \approx 6.25\times10^{18}$$
elementary charges — consistent with NCERT's own statement that there are about $6\times10^{18}$ electrons in a charge of $-1$ C.

---
*Note on this lecture's transcript:* the unit-conversion / electron-count material just above is grounded entirely from a board frame near the true end of the lecture -- the transcript itself loops back and repeats the water-numerical and gravitation recap instead of transcribing it. See the flagged span below.

##### Verify these spans
- [30:29–36:24] The raw ASR transcript loops back after finishing the Coulomb's-law derivation (ending around t=1829s with F=9e9 N for the 1-coulomb definition) and re-transcribes the earlier 'how many charges in 250mL of water' numerical and Newton's-gravitation recap almost verbatim from t=1854s to the transcript's last segment at t=2182s -- a delayed-repetition artifact matching the pattern found repeatedly in this chapter's sibling chapter (Ch2). Board frames tell a different story: floor_000109.jpg (t=2160s, the last captured frame, well within this window) shows a page titled with a '5C, 1C -> very very large value' remark, unit conversions (1mC/microC/nC), and a worked calculation of how many electrons make up 1 coulomb (n=10^19/1.6) -- standard NCERT Section 1.4 content on why the coulomb is an impractically large unit -- none of which appears anywhere in the transcript. The unit-conversion and electron-count claim above is grounded entirely from that board frame.

#### Dielectric Constant, Coulomb's Law in Vector Form, and the Superposition Principle

**NCERT sections covered:** 1.5, 1.6

##### Dielectric constant

###### Force in a medium other than vacuum
$$F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r^2}\quad\text{(vacuum)} \qquad F = \frac{1}{4\pi\varepsilon}\frac{Q_1Q_2}{r^2}\quad\text{(medium, absolute permittivity }\varepsilon\text{)}$$

**Relative permittivity** $\varepsilon_r = \varepsilon/\varepsilon_0$ is preferred to quoting $\varepsilon$ directly, for the same reason density is usually quoted relative to water (density of water $=1$ g/cm$^3$, mercury $=13.6$, kerosene $=0.8$): a dimensionless ratio against a fixed, universal reference is more useful than an absolute value with units.

**Dielectric constant** $K$ is just another name for relative permittivity — there is no physical difference between the two terms:
$$\boxed{F = \frac{1}{4\pi\varepsilon_0 K}\frac{Q_1Q_2}{r^2}}, \qquad K=\varepsilon_r=\varepsilon/\varepsilon_0$$

*(Aside: in the CGS system, the Coulomb's-law constant is taken as exactly $1$, and charge is measured in electrostatic units/statcoulombs, with $1$ C $=3\times10^9$ esu. Mentioned for context; SI is used throughout this course.)*

###### Partly-dielectric, partly-vacuum gap
For two charges separated by distance $r$, with a dielectric slab of thickness $t$ (constant $K$) occupying part of the gap and the rest ($r-t$) vacuum: replace the dielectric segment with an **equivalent vacuum distance** $r_0=\sqrt{K}\,t$ (found by equating the force through the real dielectric thickness to the force through an unknown vacuum thickness), then treat the whole path as vacuum with total effective separation $(r-t)+\sqrt{K}t$:
$$F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{\left[(r-t)+\sqrt{K}\,t\right]^2}$$

##### Coulomb's law in vector form (NCERT 1.5)

For charges $Q_1$ at $\vec r_1$ and $Q_2$ at $\vec r_2$, the force on $Q_2$ due to $Q_1$:
$$\vec F_{21} = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2(\vec r_2-\vec r_1)}{|\vec r_2-\vec r_1|^3} = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r_{12}^2}\hat r_{12}$$
By Newton's third law, $\vec F_{12}=-\vec F_{21}$.

##### Principle of superposition (NCERT 1.6)

The net force on any one charge due to several others is the **vector sum** of the individual pairwise Coulomb forces, each computed independently as though only that one pair of charges existed, then combined via the triangle/parallelogram law of vector addition. For charges $Q_1,\dots,Q_5$, the force on $Q_4$:
$$\vec F_4 = \vec F_{41}+\vec F_{42}+\vec F_{43}+\vec F_{45}$$

#### Continuous Charge Distribution (Linear, Surface, Volume), and Numericals on Placing a Third Charge

**NCERT sections covered:** 1.12

##### Continuous charge distribution (NCERT 1.12)

For a continuous (non-point) charge distribution: break it into small elements, find the charge $dq$ on each, compute the small force $d\vec F$ on a test charge $q_0$ due to that element via Coulomb's law, then **integrate** over the whole distribution. (Analogy used in the lecture: once you know the cost *per* mango, you can price any quantity without asking again and again — same idea as knowing charge *per unit* length/area/volume.)

###### Linear charge density (1-D)
For a wire, or a ring (whose charge lies along its circumference — a *length*, not an area):
$$\lambda = \frac{\text{total charge}}{\text{total length}} = \frac{dq}{dl} \quad\Rightarrow\quad dq = \lambda\,dl$$
Force on $q_0$ from an element $dl$ at distance $r$: $d\vec F = \dfrac{1}{4\pi\varepsilon_0 K}\dfrac{q_0\lambda\,dl}{r^2}\hat r$, and the total force is $\vec F = \int d\vec F$ over the whole length.

###### Surface charge density (2-D)
For a charged plane sheet, or the surface of a metal solid/hollow sphere:
$$\sigma = \frac{\text{charge}}{\text{area}} = \frac{dq}{ds} \quad\Rightarrow\quad dq = \sigma\,ds$$
**Key point:** any charge given to a metal (conducting) solid sphere migrates entirely to its outer surface (area $4\pi r^2$) — so even though the sphere is a 3-D object, its charge distribution is *surface* (2-D), exactly like a hollow metal sphere.

###### Volume charge density (3-D)
For a distribution that genuinely fills a volume:
$$\rho = \frac{\text{charge}}{\text{volume}} = \frac{dq}{dV} \quad\Rightarrow\quad dq = \rho\,dV,\qquad d\vec F = \frac{1}{4\pi\varepsilon_0 K}\frac{q_0\rho\,dV}{r^2}\hat r$$

##### Numericals: placing a third charge for zero net force

###### Two same-sign charges
$Q_1$ and $Q_2$ (worked case: $Q_2=2Q_1$) separated by $r$ — find where $Q_0$, placed **between** them, feels zero net force. Setting the two force magnitudes equal (distance $x$ from $Q_1$):
$$\frac{Q_1}{x^2} = \frac{Q_2}{(r-x)^2} \;\Rightarrow\; (r-x)^2 = 2x^2 \;\Rightarrow\; r-x=\sqrt2\,x \;\Rightarrow\; \boxed{x = \frac{r}{1+\sqrt2}}$$

###### Two opposite-sign charges
$+2Q$ and $-Q$ separated by $r$. A charge $+Q_0$ placed **between** them feels both forces pushing it the *same* direction (repelled by $+2Q$, attracted toward $-Q$) — they can never cancel there. The zero-force point must lie **outside** the segment, beyond the smaller-magnitude charge ($-Q$). At distance $x$ beyond $-Q$:
$$\frac{1}{4\pi\varepsilon_0}\frac{2Q\,Q_0}{x^2} = \frac{1}{4\pi\varepsilon_0}\frac{Q\,Q_0}{(r+x)^2} \;\Rightarrow\; \boxed{x = \frac{r}{\sqrt2-1}}$$

**General technique for this type of problem:** first determine whether the null point can even exist *between* the charges (same sign → yes, between them; opposite sign → no, it's outside, on the far side of the weaker charge), *then* set up and solve the force-balance equation.

---
*Note on this lecture's transcript:* volume charge density and both worked numericals above are grounded entirely from board frames -- the transcript itself falls into a repeated loop of earlier material and never reaches any of this. See the flagged span below.

##### Verify these spans
- [14:30–32:22] This lecture's transcript is unusually badly corrupted: after the surface-charge-density/metal-sphere material (ending around t=870s), the ASR falls into a repeating loop, re-transcribing the SAME linear/surface charge density content 3-4 times over with shifted timestamps (a delayed-repetition artifact matching the pattern found across this chapter's sibling chapters), all the way to the transcript's nominal end near t=1942s. As a result the transcript never once mentions volume charge density (rho) at all, and never mentions the lecture's own second named topic -- 'numerical on placing of third charge' -- anywhere. Board frames tell the real story: floor_000050.jpg (t=980s) shows all three charge-density types (linear, surface, volume) laid out together on one page, confirming volume charge density genuinely was covered (most likely in the real, un-transcribed audio around t=870-980s); frames from t=1120s through t=1900s (floor_000057, floor_000065-66, floor_000072-74, floor_000096) show at least two distinct fully-worked numericals on where to place a third charge for zero net force -- one for two same-sign charges (null point between them), one for two opposite-sign charges (null point outside the segment) -- spanning what is likely more than half of this lecture's real running time. The volume-charge-density claim and both numerical claims above are grounded entirely from board frames, not the transcript.

#### Electric Field Intensity, Field Lines, and the Point-Charge Field Formula

**NCERT sections covered:** 1.7, 1.8

##### Electric field (NCERT 1.7)

**Concept:** the region around a charge where its effect (a force on another charge) can be felt -- directly analogous to the magnetic field around a magnet (felt by a test magnet, stronger effect closer in, negligible far away).

**Electric field intensity** $\vec E$ is the measurable version of this idea: the force per unit charge experienced by a very small ("test") positive charge $q_0$ placed at a point, in the limit $q_0\to0$ (small enough that it doesn't itself disturb the field being measured):
$$\vec E = \lim_{q_0\to0}\frac{\vec F}{q_0}$$
$\vec E$ is a **vector**, in the same direction as the force on a positive test charge. SI unit: **N/C**. Dimensional formula (from $F=ma$ and $Q=It$): $[E] = M^1L^1T^{-3}A^{-1}$.

###### Electric field due to a point charge
Combining $\vec E=\vec F/q_0$ with Coulomb's law $F=\frac{1}{4\pi\varepsilon_0}\frac{Qq_0}{r^2}$:
$$\boxed{\vec E = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\hat r}$$
The $q_0$ cancels out — **$E$ is independent of the test charge used to probe it**, a property of the source charge and the field point alone.

**Graphing $E$ vs $r$:** an inverse-square curve (a "rectangular hyperbola" shape, same family as $PV=\text{const}$ or $xy=\text{const}$). To turn it into a straight line (standard technique, same idea as plotting $V$ vs $I$ for Ohm's law to read off $R$ as the slope): plot $E$ against $1/r^2$ — since $Er^2 = Q/4\pi\varepsilon_0 = \text{const}$, this gives a straight line through the origin.

**Worked numerical:** a charge of $2$ mC at point $O$ — find $E$ at $40$ cm from it:
$$E = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2} = \frac{9\times10^9\times2\times10^{-3}}{(40\times10^{-2})^2}~\text{N/C}$$

##### Electric field lines (NCERT 1.8)

Imaginary curves such that the tangent at any point gives the direction of $\vec E$ there, and along which an isolated free positive test charge would tend to move (directly analogous to magnetic field lines, e.g. traced out by iron filings around a magnet). **Crowding** of field lines indicates a **stronger** field.

###### Characteristics
1. Field lines **start on positive charges and terminate on negative charges**.
2. Field lines **never form closed loops** — this is the key difference from magnetic field lines, which *always* form closed loops (outside a magnet N$\to$S, inside S$\to$N). A field line running from one charge to a different charge (not back to itself) is not a closed loop, even if it looks curved.

###### Patterns for common configurations
- **Isolated point charge:** lines radiate straight outward (for $+q$, terminating charge assumed at infinity) or straight inward (for $-q$, source charge assumed at infinity). A common mistake is drawing lines that curve/converge near the charge — for a true point charge they must be radially straight, never touching or crossing right at the charge.
- **Two like charges** (e.g. $+Q,+Q$ or $+2Q,+Q$): lines repel each other and bend away, never intersecting. A **null point** ($E=0$) exists between them, located **closer to the smaller-magnitude charge** — exactly at the midpoint if the charges are equal.
- **Two unlike charges** (e.g. $+Q,-Q$ or $+2Q,-Q$): lines run from positive to negative, curving toward each other — this is *not* a closed loop (each line terminates once, going from one distinct charge to the other, rather than returning to its own start). Asymmetric magnitudes get proportionally more lines drawn from the larger charge.

---
*Note on this lecture's transcript:* the quantitative point-charge field formula, the E-vs-r graph discussion, the worked numerical, and the independence-from-test-charge point are all grounded from board frames near the true end of the lecture -- the transcript loops back to earlier material there instead of covering them. See the flagged span below.

##### Verify these spans
- [39:50–46:14] The transcript's real, non-repeated narration runs continuously and coherently from t=0 to about t=2390s, thoroughly covering the definition of E, field lines, and field-line patterns for point charges and charge pairs. From t=2390s to the transcript's nominal end (t=2771s) it then loops back and re-transcribes the earlier point-charge and like-charges field-line material nearly verbatim -- the same delayed-repetition ASR artifact found elsewhere in this chapter. Unlike some other cases, board frames here show this is NOT just wasted/lost time: floor_000131.jpg (t=2600s) and floor_000138.jpg (t=2740s, the last captured frame, well within the true 2774.87s duration) show substantial genuinely new material -- the quantitative point-charge field formula E=(1/4 pi eps0)(Q/r^2) boxed 'by definition', an E-vs-r graph-linearisation discussion, a worked numerical (2 mC charge, field at 40cm), and a conceptual aside confirming E is independent of the test charge -- none of which appears anywhere in the transcript. The four point-charge-formula/numerical claims above are grounded entirely from these two board frames.

#### Null-Point Numerical, Electric Dipole, and E Due to a Dipole at Axial and Equatorial Positions

**NCERT sections covered:** 1.10

##### Worked numerical: null point between two like charges

Charges $+Q$ and $+2Q$ separated by $r=2$ m — find the null point's position measured **from $+2Q$**. Setting the null point at distance $x$ from $+Q$ (so $2-x$ from $+2Q$) and equating magnitudes:
$$\frac{Q}{x^2} = \frac{2Q}{(2-x)^2} \;\Rightarrow\; (2-x)^2 = 2x^2 \;\xrightarrow{\sqrt{\ }}\; 2-x=\sqrt2\,x \;\Rightarrow\; x = \frac{2}{1+\sqrt2}$$
Since the question asks for the distance from $+2Q$, the answer is $2-x$, **not** $x$ — read the question carefully. As expected, the null point sits closer to the smaller-magnitude charge ($+Q$).

##### Electric dipole (NCERT 1.10)

A pair of equal and opposite point charges $+Q,-Q$ separated by a small distance $2L$. **Net charge is always zero.** Strength is measured by the **dipole moment**:
$$p = Q\times 2L,\qquad \text{SI unit: coulomb-metre (C m)}$$
(Write "C m", not "m C" — the latter reads as millicoulomb.) An **ideal dipole** is the limit $Q\to\infty,\ 2L\to0$ such that $p=2QL$ stays finite and well-defined.

###### Axial (end-on) position
Point $P$ on the line through both charges, distance $r$ from the dipole's centre $O$. By superposition (valid for $\vec E$ just as for forces):
$$\vec E = \frac{2Pr}{4\pi\varepsilon_0(r^2-L^2)^2}\hat p$$
— pointing the **same** direction as $\vec p$. For $r\gg L$ ($L^2$ negligible):
$$\boxed{E_\text{axial} = \frac{2P}{4\pi\varepsilon_0 r^3}}$$
Falls off as $1/r^3$ — faster than a point charge's $1/r^2$ (visible on an $E$-vs-$r$ graph as a noticeably steeper drop).

###### Equatorial (broadside-on) position
Point $P$ on the perpendicular bisector of the dipole, distance $r$ from $O$. $E_{+Q}$ and $E_{-Q}$ have equal magnitude $\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2+L^2}$ but different directions; by symmetry their components perpendicular to the dipole axis cancel exactly, leaving only the components along the (negative) axis direction to add:
$$E_\text{eq} = 2E_{+Q}\cos\theta = \frac{2QL}{4\pi\varepsilon_0(r^2+L^2)^{3/2}},\qquad \cos\theta=\frac{L}{\sqrt{r^2+L^2}}$$
For $r\gg L$:
$$\boxed{E_\text{eq} = \frac{P}{4\pi\varepsilon_0 r^3}}$$
— exactly **half** the axial-point value at the same $r$, and pointing **antiparallel** to $\vec p$ (opposite direction from the axial-point field).

#### Torque and Potential Energy of a Dipole in a Uniform Electric Field

**NCERT sections covered:** 1.11

##### Recap: torque
$$\vec\tau = \vec R\times\vec F,\qquad |\vec\tau| = RF\sin\theta$$
Direction perpendicular to the plane of $\vec R,\vec F$, via the right-hand curl rule. Equivalently, for a **couple** (two equal and opposite forces): $\tau = F\times(\text{perpendicular distance between their lines of action})$.

##### Torque on a dipole in a uniform field (NCERT 1.11)

Dipole (charges $+Q,-Q$, length $2L$, moment $p=2QL$) at angle $\theta$ to a uniform field $\vec E$. Each charge feels an equal-magnitude force $F=EQ$, but in different directions (since $\vec E$ points from $+$ to $-$) — a couple. The perpendicular distance between the two forces' lines of action is $2L\sin\theta$, so:
$$\tau = F\times 2L\sin\theta = EQ\times2L\sin\theta = PE\sin\theta$$
In vector form:
$$\boxed{\vec\tau = \vec p\times\vec E}$$
direction perpendicular to the plane of $\vec p,\vec E$ (right-hand curl rule, fingers curling from $\vec p$ to $\vec E$).

**Extremes:** torque is **maximum** ($=PE$) at $\theta=90°$ ($\vec p\perp\vec E$); torque is **zero** at $\theta=0°$ or $180°$ ($\vec p$ parallel or antiparallel to $\vec E$) — even though forces still act on each charge individually, there's no net turning effect once aligned.

##### Potential energy of a dipole (NCERT 1.11)

Small work done rotating the dipole by $d\theta$: $dW = \tau\,d\theta = PE\sin\theta\,d\theta$ (rotational analogue of $dW=F\,dx$). Integrating from $\theta_1$ to $\theta_2$ (using $\int\sin\theta\,d\theta=-\cos\theta$):
$$W = PE\left[\cos\theta_1-\cos\theta_2\right]$$
This work is stored as potential energy. Taking $\theta_1=90°$ (where $\cos90°=0$) as the zero-PE reference:
$$\boxed{U = -PE\cos\theta = -\vec p\cdot\vec E}$$

###### Worked numerical
A dipole with charge $1~\mu\text{C}$, separated by $1$ cm, placed in $E=2\times10^6$ N/C:
- **(i)** Dipole moment: $p = Q\times2L = 10^{-6}\times10^{-2} = 10^{-8}$ C$\cdot$m
- **(ii)** Maximum torque: $\tau_\max = PE = 10^{-8}\times2\times10^6 = 2\times10^{-2}$ N$\cdot$m
- **(iii)** Work done rotating through $180°$ starting from $\theta=0$: $W = PE[\cos0°-\cos180°] = PE[1-(-1)] = 2PE$

---
*Note on this lecture's transcript:* the worked numerical above is grounded entirely from a board frame near the true end of the lecture -- the transcript repeats earlier material there and then stops well short of the lecture's actual end. See the flagged span below.

##### Verify these spans
- [25:06–34:06] Two separate transcript problems compound here. First, from roughly t=1506s the transcript re-transcribes the potential-energy derivation (theta1-to-theta2 rotation, the sin/cos integration, U=-PE cos theta) almost verbatim a second time -- a delayed-repetition artifact, not real re-teaching -- before cutting off mid-sentence at t=1883.7s. Second, and more seriously, this transcript's own timestamped coverage stops there entirely: it has NO segments at all for the final ~163 seconds of the lecture's true 2046.5s duration (a genuine truncation, not just a hidden-by-repetition gap). Board frames fill in what was lost: the last captured frame (floor_000102.jpg, t=2020s, well inside the untranscribed window) shows a 'stable eqm' heading (visible only as a two-word label -- the supporting derivation, if any, is off the top of the captured frame and not recoverable from the sampled images) followed by a fully worked numerical (dipole moment, maximum torque, and work done rotating through 180 degrees from theta=0) plus a small formula-summary box. The worked-numerical claim above is grounded entirely from that frame; the stable-equilibrium point is mentioned only as a heading seen on the board, not as a verified claim, since its derivation isn't visible in any captured frame.

#### Correction on Dipole PE, Total Force on a Dipole, Electric Flux, and Gauss's Law

**NCERT sections covered:** 1.9, 1.11, 1.13

##### Corrections and follow-ups from the previous lecture

- In the dipole PE numerical, the reference angle $\theta_1$ (where PE is taken as zero) is **$90°$**, not $0°$ — use $\cos90°=0$.
- **Total (net) force on a dipole in a uniform field is zero**: the two equal-and-opposite forces on the charges cancel exactly, so the dipole only *rotates*, it doesn't translate. In a **non-uniform** field, net force is no longer zero, so the dipole undergoes both translational *and* rotational motion.

##### Electric flux (NCERT 1.9)

**Area as a vector:** an area element $d\vec S$ has both magnitude and direction — direction given by the **outward-drawn normal** to the surface at that point (e.g. for a cube, the outward normal on each face points away from the enclosed volume).

**Electric flux** $\Phi$ is the number of field lines passing *normally* (perpendicularly) through a given area:
$$\Phi = EA\cos\theta = \vec E\cdot\vec A$$
($\theta$ = angle between $\vec E$ and the area's outward normal.) Maximum when $\vec E$ is parallel to the normal; zero when $\vec E$ lies in the plane of the surface (analogy used in the lecture: water flow through a rotating ring/bangle — maximum flow face-on, zero flow edge-on).

**General definition:** $d\Phi = \vec E\cdot d\vec S$ for a small element, $\Phi = \oint_S \vec E\cdot d\vec S$ over the whole surface. **SI unit:** N$\,$m$^2$C$^{-1}$. Flux is a **scalar** (it's a dot product).

##### Gauss's law (NCERT 1.13)

**Statement:** the total electric flux through any closed surface $S$ in vacuum equals $1/\varepsilon_0$ times the total charge enclosed:
$$\boxed{\oint_S \vec E\cdot d\vec S = \frac{Q_\text{enclosed}}{\varepsilon_0}}$$

###### Derivation for a point charge (spherical Gaussian surface)
For a point charge $Q$ at the centre of a sphere of radius $r$: $\vec E$ is radial with constant magnitude $\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}$ everywhere on the sphere, and everywhere **parallel** to $d\vec S$ ($\theta=0,\ \cos\theta=1$). So:
$$\oint_S\vec E\cdot d\vec S = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\oint_S dS = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}(4\pi r^2) = \frac{Q}{\varepsilon_0}$$
The $r^2$ cancels — the result is **independent of the sphere's radius**. Though proved here only for a sphere, $\Phi=Q/\varepsilon_0$ holds for a closed surface of **any** shape enclosing the same charge $Q$.

###### Flux example: closed cylinder in a uniform field
For a uniform field passing straight through a closed cylinder aligned with the field (entering one flat end, exiting the other, none crossing the curved side): the **total** flux through the closed surface is **zero** — outward flux at the exit face exactly cancels inward flux at the entry face.

---
*Note on this lecture's transcript:* the Gauss's-law derivation and the cylinder example above are grounded entirely from board frames -- the transcript repeats earlier flux-definition material there instead. See the flagged span below.

##### Verify these spans
- [30:04–32:02] The transcript re-transcribes the earlier flux-definition material (Phi=EA cos theta, roughly matching t=903-1030s) a second time from about t=1834s to its last segment at t=1918-1947s -- a delayed-repetition artifact, not new content. Board frames tell a different story for this same window: floor_000091.jpg and floor_000095.jpg (both around t=1800-1880s, within this window) show the actual mathematical PROOF of Gauss's law for a point charge using a spherical Gaussian surface (E radial and parallel to dS everywhere, integral reduces via the sphere's surface area 4 pi r^2 to Phi=Q/eps0), generalised to an arbitrary closed surface shape, plus a flux-through-a-closed-cylinder example (net flux zero). None of this derivation or example appears in the transcript, which only ever states Gauss's law verbally without deriving it. The two claims above (the spherical-surface derivation and the cylinder example) are grounded entirely from these board frames.

#### Applications of Gauss's Law: Cube Flux Numericals, Infinite Wire, Infinite Sheet, Charged Spherical Shell

**NCERT sections covered:** 1.13, 1.14

##### Gauss's law: flux numericals with a cube

**Charge near one face:** a point charge $10$ cm from the centre of one face of a cube — flux through the whole (closed) cube is $q/\varepsilon_0$; since a cube has 6 identical faces, flux through just that one face is $\dfrac{1}{6}\dfrac{q}{\varepsilon_0}$.

**Charge at special points of a cube:**
- **Body centre:** charge fully enclosed by one cube $\Rightarrow$ flux $=q/\varepsilon_0$.
- **Face centre:** charge sits on the boundary shared with one neighbouring cube $\Rightarrow$ effective enclosed charge $q/2$, flux $=\dfrac{q}{2\varepsilon_0}$.
- **Edge centre:** charge shared among the $8$ cubes meeting at that edge $\Rightarrow$ effective enclosed charge $q/8$, flux $=\dfrac{q}{8\varepsilon_0}$.

##### Applications of Gauss's law (NCERT 1.14)

Gauss's law gives a shortcut to find $E$ for highly symmetric continuous charge distributions: choose a Gaussian surface matching the symmetry, so $E$ can be pulled outside the flux integral.

###### Field due to an infinitely long charged wire (1.14.1)
Linear charge density $\lambda$, field point at perpendicular distance $r$. Gaussian surface: a coaxial cylinder of radius $r$, length $L$. By symmetry $E$ is radial and constant on the curved surface (parallel to its area vector, $\theta=0$), and perpendicular to the two flat end-caps ($\theta=90°$, zero contribution):
$$E(2\pi rL) = \frac{\lambda L}{\varepsilon_0} \;\Rightarrow\; \boxed{E = \frac{\lambda}{2\pi\varepsilon_0 r}}$$
($L$ cancels.) Inversely proportional to $r$ — same rectangular-hyperbola-shaped $E$-vs-$r$ graph family as the point charge and the dipole.

###### Field due to an infinite plane sheet (1.14.2)
Surface charge density $\sigma$; field is perpendicular to the sheet, equal magnitude both sides. Gaussian surface: a thin "pillbox" cylinder straddling the sheet, flat circular end-caps of area $A$ parallel to the sheet. $E$ parallel to both end-caps ($\theta=0$, contributing $EA$ each) and perpendicular to the curved side (zero):
$$2EA = \frac{\sigma A}{\varepsilon_0} \;\Rightarrow\; \boxed{E = \frac{\sigma}{2\varepsilon_0}}$$
($A$ cancels.) **Independent of distance** from the sheet — a flat horizontal line on an $E$-vs-$r$ graph.

###### Field due to a uniformly charged thin spherical shell (1.14.3)
Total charge $q$, radius $R$.
- **Outside / on the surface** ($r\geq R$, Gaussian sphere concentric with the shell): the whole charge behaves as if concentrated at the centre, exactly like a point charge:
$$E = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\ (r>R), \qquad E = \frac{1}{4\pi\varepsilon_0}\frac{q}{R^2}\ (r=R)$$
- **Inside** ($r<R$): a Gaussian sphere strictly inside the shell encloses **zero** charge (all the shell's charge sits on its outer surface). Since the flux integral's surface-area factor $4\pi r^2$ is never zero for $r>0$, this forces:
$$\boxed{E = 0 \text{ everywhere strictly inside a uniformly charged shell}}$$

---
*Note on this lecture's transcript:* both the outside/surface and inside results for the charged spherical shell above are grounded entirely from board frames near the true end of this (very long, 48-minute) lecture -- the transcript itself stops right at the sentence introducing this final application, with no further segments. See the flagged span below.

##### Verify these spans
- [46:20–47:38] This is a straightforward truncation rather than a repetition/substitution artifact: the transcript's own last segment is the single sentence 'So, what we do is we consider a thin spherical shell, let us suppose we consider this as a thin spherical shell,' right at the very start of the third application (field due to a charged spherical shell), and no further segments follow even though this was clearly meant to be a full derivation (matching this very long, 48-minute lecture's own title, 'application of gauss th'). Board frames fill the gap completely: floor_000134.jpg and floor_000138.jpg (both well within the true 2858s duration, after the transcript's own cutoff) show the full three-case derivation -- outside/on the surface (Gauss's law with a Gaussian sphere of radius r>=R, giving the point-charge-like result), and inside (Gaussian sphere r<R encloses zero charge, forcing E=0) -- reaching clean, boxed final results in each case. Both spherical-shell claims above are grounded entirely from these two board frames.

### Chapter 2 · Electrostatic Potential and Capacitance — lecture notes

#### Electric Potential: Definition, Relation to Field, Potential Due to a Point Charge and a System of Charges

**NCERT sections covered:** 2.2, 2.3, 2.5

##### Electric potential

###### Definition (NCERT 2.2)
Building on electric field intensity (force-based, from the previous chapter), this lecture switches to a work-based description.

**Electric potential difference:**
$$V_A - V_B = \frac{W_{B \to A}}{q_0}$$
the work done by an *external* force per unit charge in moving a test charge from $B$ to $A$, **without acceleration** -- meaning the external force exactly balances the electric force at every point along the path, so the process is quasi-static and no kinetic energy is gained or lost.

**Unit:** $1~\text{volt} = 1~\text{joule/coulomb}$.

**Electric potential at a point** (not just a difference) is the special case where the charge is brought from infinity, with the convention $V(\infty) = 0$:
$$V = \frac{W_{\infty \to P}}{q_0}$$

**Physical significance:** a positive charge moves from high to low potential; a negative charge moves from low to high potential -- the electrical analogue of water flowing from high to low level, or heat flowing from hot to cold.

###### Potential as a line integral of the field
$$V = -\int_B^A \vec{E}\cdot d\vec{l}$$
Derived from $dW = -q_0\vec{E}\cdot d\vec{l}$ (external force is equal and opposite to the electric force) and $V = W/q_0$. Called out in the lecture as a must-know result ("your 2 AM formula").

**Corollary -- the electrostatic field is conservative:**
$$\oint \vec{E}\cdot d\vec{l} = 0$$
Any closed-loop line integral of $\vec E$ vanishes, since the potential difference between two points doesn't depend on the path taken between them.

###### Potential due to a point charge (NCERT 2.3)
$$V(r) = \frac{1}{4\pi\varepsilon_0}\frac{q}{r}$$
Falls off as $1/r$ (compare to $E \propto 1/r^2$).

###### Potential due to a system of charges (NCERT 2.5)
Potential obeys superposition -- being a **scalar**, it's a plain sum (no vector addition needed, unlike $\vec E$):
$$V_P = \frac{1}{4\pi\varepsilon_0}\sum_i \frac{q_i}{r_i}$$
with each $q_i$ carrying its own sign.

**Worked example:** at the point $P$ midway between a $+q$ and a $-q$ charge (equidistant, distance $r$ from each):
$$V_P = \frac{1}{4\pi\varepsilon_0}\frac{q}{r} - \frac{1}{4\pi\varepsilon_0}\frac{q}{r} = 0$$
even though $\vec E \ne 0$ at that point. This is the key conceptual takeaway of the section: **potential and field are not simply proportional point-by-point** -- $V=0$ at a point says nothing about whether $E=0$ there, and vice versa.

---
*Note on this lecture's transcript:* the segment covering the point-charge and system-of-charges derivations (roughly the last 2 minutes of the lecture) is not reliable in the ASR transcript -- see the flagged span below. Those claims above are grounded directly in the board frames instead.

##### Verify these spans
- [37:15–39:15] Transcript is unreliable here: instead of transcribing the real content actually on the board in this window (potential due to a point charge, then due to a system of charges -- confirmed from frames at t=2140-2320s), the ASR output regresses to repeating the 'significance of potential / high-to-low potential' material from around t=1200s almost verbatim. This looks like a distinct ASR failure mode (content substitution rather than truncation or tail fabrication) -- the claims for this section are grounded entirely in the board frames, not the transcript.

#### Potential Due to an Electric Dipole, and Potential Energy of a System of Charges

**NCERT sections covered:** 2.4

##### Potential due to an electric dipole (NCERT 2.4)

Unlike the earlier electric-field-intensity treatment (which used axial and equatorial special points), here a **general point** $P$ at polar coordinates $(r,\theta)$ from the dipole's center is considered directly.

By superposition (potential is a scalar, so this is simple addition, not vector addition like $\vec E$):
$$V = V_{+q} + V_{-q} = \frac{1}{4\pi\varepsilon_0}\frac{q}{R_1} - \frac{1}{4\pi\varepsilon_0}\frac{q}{R_2}$$

Using the standard far-field approximation (dropping perpendiculars from each charge to the line $OP$, giving $PN \approx AP$ and $ON = L\cos\theta$):

$$V = \frac{P\cos\theta}{4\pi\varepsilon_0\left(r^2 - l^2\cos^2\theta\right)}$$

For $r \gg l$ (the point far from the dipole compared to its size), this simplifies to:
$$\boxed{V = \frac{P\cos\theta}{4\pi\varepsilon_0 r^2}}$$

Two things worth noting against the point-charge result $V \propto 1/r$: dipole potential falls off **faster** ($1/r^2$), and it's **direction-dependent** through $\cos\theta$ — a point charge's potential has no such angular dependence.

###### Special cases
- **Axial** ($\theta = 0$): $V = \dfrac{P}{4\pi\varepsilon_0 r^2}$ (maximum)
- **Equatorial / "broadside"** ($\theta = 90°$): $V = 0$ exactly, since $\cos 90° = 0$ — consistent with the direct superposition argument from the previous lecture (equidistant $+q$ and $-q$ cancel).

###### Worked example
$q = 100\times10^{-9}$ C, separation $2L = 2\times10^{-3}$ m (so $P = 2QL = 2\times10^{-10}$ C·m), evaluated at $r=0.5$ m:
- Axial position: $V = 7.2$ V
- Broadside (equatorial) position: $V = 0$

##### Potential energy of a system of point charges

Defined as the total work needed to assemble the charge configuration by bringing each charge in from infinity, one at a time, against the field of the charges already in place.

**Two charges:** bringing $q_1$ in first costs nothing (no field exists yet); bringing $q_2$ to a distance $r$ from $q_1$ costs work equal to (potential due to $q_1$) $\times\, q_2$:
$$U = \frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r}$$

**Three charges:** sum over every pair, in the order each charge is brought in:
$$U = \frac{1}{4\pi\varepsilon_0}\left[\frac{q_1q_2}{r_{12}} + \frac{q_1q_3}{r_{13}} + \frac{q_2q_3}{r_{23}}\right]$$

**General result, $n$ charges:** every pair contributes exactly once:
$$U = \frac{1}{2}\cdot\frac{1}{4\pi\varepsilon_0}\sum_{i=1}^n\sum_{\substack{j=1\\j\ne i}}^n \frac{q_iq_j}{r_{ij}} \;=\; \frac{1}{4\pi\varepsilon_0}\sum_{i<j} \frac{q_iq_j}{r_{ij}}$$
(the two forms are equivalent -- the first double-counts every pair once from each side and divides by 2; the second restricts to $j>i$ so each pair is counted exactly once directly.)

###### Worked example
Equilateral triangle of side $a = 0.1$ m, with $q_1=q$, $q_2=2q$, $q_3=-2q$ and $q=10^{-6}$ C:
$$U = \frac{1}{4\pi\varepsilon_0}\frac{q^2}{a}\Big[(1)(2) + (1)(-2) + (2)(-2)\Big]$$
evaluated by the lecture to a negative total (a bound, energy-releasing configuration) — worth re-deriving by hand to check the arithmetic rather than trusting the board's final numeric answer verbatim.

#### Potential Energy in an External Field, and Potential Due to a Charged Sphere

**NCERT sections covered:** 2.5, 2.8

##### Potential energy in an external field (NCERT 2.8)

Distinct from Section 2.7 (potential energy of a system of charges due to *their own* mutual field): here the field $E$ (and potential $V$) is produced by **external sources**, not by the charge(s) whose energy we're computing.

###### Potential energy of a single charge (NCERT 2.8.1)
Work done in bringing charge $q$ from infinity to a point at position $\vec r$, against the external potential $V(\vec r)$:
$$\boxed{PE = qV(\vec r)}$$

**Electron-volt:** if a charge of magnitude $e = 1.6\times10^{-19}$ C is accelerated through a potential difference of 1 V, it gains energy $1.6\times10^{-19}$ J -- this quantity of energy is defined as **1 electron-volt**:
$$1~\text{eV} = 1.6\times10^{-19}~\text{J}$$
(A unit of *energy*, built from the volt but not itself a unit of potential.)

###### Potential energy of a system of two charges (NCERT 2.8.2)
Assemble $q_1$ then $q_2$ into the external field region, positions $\vec r_1,\vec r_2$:
- Bringing $q_1$ to $\vec r_1$ costs $q_1V(\vec r_1)$ (work against the external field alone).
- Bringing $q_2$ to $\vec r_2$ costs work against **both** the external field *and* the field now due to $q_1$:
$$W_{q_2} = q_2V(\vec r_2) + \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{12}}$$

Total potential energy of the assembled system:
$$\boxed{PE = q_1V(\vec r_1) + q_2V(\vec r_2) + \frac{1}{4\pi\varepsilon_0}\frac{q_1q_2}{r_{12}}}$$

*(For reference, the board also carries the dipole-in-external-field result derived from this same equation: $PE = -\vec p\cdot\vec E$ -- covered in more depth in a separate lecture on dipole potential energy.)*

##### Electric potential due to a uniformly charged sphere (NCERT 2.5)

###### On the surface
Outside a uniformly charged sphere (charge $q$, radius $R$), the field is identical to that of a point charge $q$ at the centre: $E = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}$. Integrating from infinity in to the surface:
$$V = -\int_\infty^R \vec E\cdot d\vec l = \frac{1}{4\pi\varepsilon_0}\frac{q}{R}$$
Same value a point charge $q$ at the centre would produce at distance $R$.

###### Inside the sphere
Split the line integral at the surface -- from infinity to $R$ (as above), plus from $R$ inward to the field point:
$$V = -\int_\infty^R \vec E\cdot d\vec l \;+\; \left(-\int_R^{r} \vec E\cdot d\vec l\right)$$
The second term vanishes because $E = 0$ everywhere inside a charged conducting sphere. So:
$$\boxed{V_\text{inside} = V_\text{surface} = \frac{1}{4\pi\varepsilon_0}\frac{q}{R}}$$

**Key takeaway:** potential inside the sphere is *constant*, equal to the surface value -- even though the field itself is zero throughout the interior. (Zero field means no *change* in potential, not zero potential; this is the same field/potential distinction flagged in the very first lecture of this chapter.)

---
*Note on this lecture's transcript:* the final ~340 seconds, covering the sphere derivation above, are not reliably transcribed -- see the flagged span below. Those two claims are grounded directly in the board frames instead.

##### Verify these spans
- [17:40–23:20] Board frames (floor_000054 at t=1060s: blank new page; floor_000055 at t=1080s: 'Electric potential on surface of sphere' heading just begun; floor_000063 at t=1240s and floor_000067 at t=1320s: the full surface-and-inside-sphere derivation, reaching a concluding statement) show this final ~340s of the lecture is spent on the sphere-potential derivation named in the lecture's own title. The ASR transcript never once mentions a sphere, surface, or conductor anywhere in its 38 segments -- instead its last ~30 segments (from roughly 790s to the claimed end at 1421s) continue elaborating the two-charges-in-external-field material, well past where the board shows that topic was finished (page 1, visible complete by ~t=520s) and a new page begun. This reads as sustained content substitution: real audio about the sphere derivation went untranscribed, replaced by an extended rehash of already-covered material. Automated coverage checks (duration-fabrication and repetition-loop detectors) did not catch it, since the substituted text is paraphrased rather than verbatim-repeated and its final timestamp (1421.1s) is close to the true 1400.47s duration. The two sphere claims above are grounded entirely in the board frames, not the transcript.

#### Equipotential Surfaces, and an Introduction to Dielectric Polarisation

**NCERT sections covered:** 2.6, 2.10

##### Equipotential surfaces (NCERT 2.6)

###### Definition
A surface drawn in an electric field such that the electric potential is the same at every point of it. For points $A,B,C,D$ all on one such surface around a charge $q$:
$$V_A = V_B = V_C = V_D$$

###### E is always perpendicular to an equipotential surface
If $\vec E$ had any component *along* the surface, moving a test charge in that direction would require work -- but work done between any two points of an equipotential surface is zero (no potential difference between them, by definition). So $\vec E$ can have no tangential component: it must be purely normal to the surface everywhere.

**Corollary:** the surface of a conductor in electrostatic equilibrium is itself an equipotential surface (no tangential $E$ on/inside a conductor at equilibrium).

###### Reading direction and relative magnitude of V from E = -dV/dr
$$\vec E = -\frac{dV}{dr}$$
The **negative sign** means $\vec E$ points in the direction of *decreasing* potential -- not increasing. This gives a fast way to answer "which of two points is at higher potential / which way does $E$ point" questions: follow the field lines from high potential to low potential (for $-q$: field lines point *into* the charge, so potential increases as you move away from it; for $+q$: field lines point *away*, so potential decreases as you move away).

###### Spacing between equipotential surfaces
For a **fixed** potential difference $dV$ between successive equipotential surfaces, the spacing $dr$ between them is set by $E = -dV/dr$, i.e. $dr \propto 1/E$:
- Where the field is **stronger**, equipotential surfaces are drawn **closer together**.
- Where the field is **weaker**, they are drawn **farther apart**.

This is the visual companion to field-line density: both crowd together where $E$ is large.

###### Equipotential surfaces for a uniform field
For a uniform $\vec E$ (e.g. between parallel plates), equipotential surfaces are **planes perpendicular to $\vec E$**, equally spaced (since $E$ doesn't vary, equal $dV$ steps mean equal $dr$ steps throughout).

##### Electric polarisation -- introduction (NCERT 2.10)

**Free charges** exist in conductors (metals) and are free to move through the material. **Bound charges** are the electrons and ions bound within the atoms/molecules of an insulator -- they cannot move freely through the material. Insulators are also called **dielectrics**.

**Electric polarisation:** when a dielectric is placed in an external electric field, each molecule's positive and negative charge get displaced relative to each other (a simplified picture of an induced dipole forming), even though no charge actually leaves the material. This relative displacement, summed across the dielectric, is what's meant by polarisation.

---
*Note on this lecture's transcript:* the transcript stops right at the introduction of polarisation -- board pages visible later in this same recording carry more advanced dielectric material (polar/non-polar molecule classification, a quantitative polarisation formula) that the transcript's own narration never reaches, and at least one other visible page (an "electrostatic shielding" page) doesn't belong to this lecture's spoken content at all. See the flagged span below -- only the qualitative polarisation definition above, independently confirmed by the transcript's own words, is treated as covered by this lecture.

##### Verify these spans
- [34:00–45:40] Board frames in this window (e.g. floor_000103 at t=2040s: polar vs non-polar molecule classification with examples H2O/HCl/CO, induced-charge diagram; floor_000138 at t=2740s: polarisation vector P = q_i.t/(A.t) = q_i/A with SI unit C/m^2, and 'susceptibility of a dielectric') show substantially more advanced dielectric material than the transcript's own narrated content ever reaches -- the transcript's last 51st segment (2900.5-2955.6s) is still at the introductory 'one molecule gets displaced, simplified model' stage. Two other frames sampled in this same document (floor_000066 at t=1300s and floor_000074 at t=1460s) show an unrelated 'electrostatic shielding / Faraday's cage' page that has no correspondence anywhere in this lecture's transcript at all, confirming this recording's slide document contains material from other classes that the teacher scrolls past or pre-writes without narrating in this particular video. For that reason the polar/non-polar classification and the P=q_i/A formula are NOT included as grounded claims above -- only the qualitative polarisation definition that the transcript itself independently states is included.

#### Capacitors and Capacitance: Basics, Isolated Sphere, Spherical Capacitor, Cylindrical Capacitor

**NCERT sections covered:** 2.11

##### Capacitors and capacitance (NCERT 2.11)

###### Capacitance of a conductor
As charge $Q$ on a conductor increases, its potential $V$ rises proportionally: $Q \propto V$, so
$$Q = CV$$
where $C$, the **capacitance**, is a constant depending only on the conductor's geometry (independent of $Q$ and $V$ themselves). On a $Q$–$V$ graph this is a straight line through the origin; its slope gives $C$.

**Unit:** $1~\text{farad} = 1~\text{coulomb/volt}$ (named for Faraday). **Worked example:** $Q = 10~\mu\text{C}$ raising the potential by $2.5$ V gives $C = Q/V = 4\times10^{-6}$ F.

###### Why two plates, not one
A single charged plate's potential rises so much (for a modest amount of charge) that the surrounding air can ionise and charge starts leaking away. Bringing a second, **grounded** plate close by induces opposite charge on it, which sharply lowers the first plate's potential for the *same* stored charge — allowing far more charge to be stored before breakdown. A **capacitor** is this pair of two neighbouring conductors carrying equal and opposite charge. Common shapes: parallel-plate, spherical, and cylindrical (coaxial) capacitors.

###### What capacitance depends on
$C$ does **not** depend on $Q$ or $V$ individually (only their ratio) — it depends purely on **geometry**: plate area (directly proportional), separation $d$ (inversely proportional), and the medium between the plates (increases with dielectric constant $K$). For a parallel plate capacitor, $C = K\varepsilon_0 A/d$ (stated here; derived from first principles in a later lecture).

###### Capacitance of an isolated spherical conductor
A single charged sphere (charge $Q$, radius $R$), with the "other plate" taken at infinity:
$$V = V_A - V_B = \frac{Q}{4\pi\varepsilon_0 R} - 0 \quad\Rightarrow\quad C = \frac{Q}{V} = 4\pi\varepsilon_0 R \;\;(\text{or } 4\pi\varepsilon_0 KR \text{ with a dielectric of constant } K)$$
So $C \propto R$. **Worked example:** modelling Earth as a spherical conductor of radius $6400$ km gives $C_\text{Earth} \approx 711~\mu\text{F}$.

###### Capacitance of a spherical capacitor
Two concentric spherical conductors: inner sphere charge $+Q$ at radius $r_1$, outer shell $-Q$ (grounded) at radius $r_2$. Using a Gaussian surface at radius $r$ between them ($E = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}$ in that region only):
$$V = -\int_{r_1}^{r_2}\vec E\cdot d\vec r = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{r_1}-\frac{1}{r_2}\right) = \frac{Q}{4\pi\varepsilon_0}\frac{r_2-r_1}{r_1 r_2}$$
$$\boxed{C = \frac{Q}{V} = \frac{4\pi\varepsilon_0\, r_1 r_2}{r_2-r_1}}$$

###### Capacitance of a cylindrical capacitor
Two coaxial cylinders of length $L$: inner radius $a$ carrying linear charge density $+\lambda$, outer radius $b$ carrying $-\lambda$ (grounded). Between them, Gauss's law gives $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$:
$$V = -\int_b^a \vec E\cdot d\vec r = \frac{\lambda}{2\pi\varepsilon_0}\ln\!\left(\frac{b}{a}\right)$$
With $\lambda = Q/L$:
$$\boxed{C = \frac{Q}{V} = \frac{2\pi\varepsilon_0 L}{\ln(b/a)}}$$

---
*Note on this lecture's transcript:* the two derivations above (spherical capacitor, cylindrical capacitor) are grounded entirely in board frames -- the transcript itself does not contain them at all; see the flagged span below for what happened instead. Also note: NCERT's core text (Section 2.11) covers capacitance of a single (isolated) conductor and states the general definition, but does not itself carry closed-form spherical/cylindrical capacitor derivations -- these two results are standard board/exam extensions beyond the strict textbook section, not verified against an NCERT-stated formula, though they follow directly from the same first principles ($V=-\int\vec E\cdot d\vec l$, Gauss's law) taught earlier in the chapter.

##### Verify these spans
- [17:40–32:06] This is the most severe transcript failure found in this chapter so far. Board frames show the isolated-sphere derivation is essentially complete by t=1060s (floor_000054); by t=1220s (floor_000062) the board has already moved on to a NEW page titled 'capacitance of a spherical capacitor' with a two-conductor Gaussian-surface diagram; by t=1440s (floor_000073) that derivation is fully worked out to a boxed capacitance formula; by t=1700s (floor_000086) a further new page 'capacitance of a cylindrical capacitor' has begun; and by t=1900s (floor_000096, just 26s before the lecture's true end) that derivation too is complete with a boxed final formula -- exactly the two topics ('spherical, cylindrical') named in this lecture's own filename. The ASR transcript, however, does not follow any of this: from roughly t=1092s to t=1866s it transcribes the SAME 'isolated spherical conductor' derivation (including the identical Earth/711-microfarad example, down to near-identical sentence wording) TWICE in a row, then cuts off mid-sentence at t=1925s ('And say this is the second sphere, okay, surrounding it') just as it appears to begin the topic the board had already finished twenty minutes of board-time earlier. Automated coverage checks did not flag this: the repeated block is not adjacent-duplicate text (a few short transitional segments separate the two copies) so the repetition-loop detector missed it, and the final timestamp lands within the true duration so the duration-fabrication check also passed. The two capacitor-formula claims above (spherical and cylindrical) are grounded entirely from board frames, with no transcript corroboration at all.

#### Capacitance of a Parallel Plate Capacitor: No Dielectric, Fully Filled, Partially Filled

**NCERT sections covered:** 2.12, 2.13

##### Capacitance of a parallel plate capacitor (NCERT 2.12, 2.13)

###### Without dielectric (medium = air/vacuum)
Plates of area $A$, separation $D$. Field between the plates: $E = \dfrac{\sigma}{\varepsilon_0} = \dfrac{Q}{A\varepsilon_0}$. Since $Q=CV$ and (for a uniform field) $V = ED$:
$$V = \frac{QD}{A\varepsilon_0} \quad\Rightarrow\quad \boxed{C = \frac{A\varepsilon_0}{D}}$$

###### With dielectric completely filling the gap (dielectric constant $K$)
Inside the dielectric the field is reduced by a factor of $K$: $E = \dfrac{\sigma}{K\varepsilon_0} = \dfrac{Q}{AK\varepsilon_0}$. The same route as above gives:
$$\boxed{C = \frac{KA\varepsilon_0}{D}}$$
Capacitance increases by a factor of $K$ compared to the no-dielectric case. (Real capacitors are commonly built this way -- e.g. paper capacitors, electrolytic capacitors -- using a dielectric layer between the plates.)

###### With a dielectric slab partially filling the gap
Slab of thickness $t < D$ and dielectric constant $K$ inserted between the plates (remaining $D-t$ is air). The field is $\sigma/\varepsilon_0$ across the air gap and $\sigma/(K\varepsilon_0)$ across the slab; adding the two potential-drop contributions:
$$V = \frac{Q}{A\varepsilon_0}\left[(D-t) + \frac{t}{K}\right] \quad\Rightarrow\quad \boxed{C = \frac{A\varepsilon_0}{D-t+\dfrac{t}{K}}}$$

**General shortcut** for any number of stacked layers (dielectric slabs and/or air gaps) between the plates:
$$C = \frac{A\varepsilon_0}{\dfrac{t_1}{K_1}+\dfrac{t_2}{K_2}+\cdots}$$
where each $t_i$ is a layer's thickness and $K_i$ its dielectric constant (air is just a layer with $K=1$). The single-slab case above is the special case $t_1=t,\,K_1=K$ and $t_2=D-t,\,K_2=1$.

###### Consistency checks
- Setting $t=D$ (slab fills the entire gap) in the partially-filled formula reduces it to $C = KA\varepsilon_0/D$ -- matching the fully-filled result, as it must.
- If the inserted slab is a **metal** rather than a dielectric, that's the limit $K\to\infty$: $C \to \infty$.

---
*Note on this lecture's transcript:* the two consistency-check results above are grounded from a board frame near the true end of the audio; the transcript itself doesn't reach them. See the flagged span below.

##### Verify these spans
- [11:00–13:22] Board frame floor_000034.jpg (t=660s, comfortably within the true 802.67s duration) shows two consistency checks worked out after the main partially-filled-dielectric formula: substituting t=D to recover the fully-filled result, and the K->infinity (metal slab) limit giving C->infinity. Neither appears anywhere in the transcript's 37 segments, which end (at a coherent, naturally-concluding sentence) on the T1/K1+T2/K2 shortcut applied to this lecture's specific numbers. This is a much smaller gap than the severe substitution found in the previous lecture (14 ch2 capacitors) -- most likely a short board-only aside that went untranscribed near the true end of the audio, rather than sustained content substitution. The metal-slab/K-to-infinity claim above is grounded from the board frame only.

#### Force Between Capacitor Plates, Energy Stored, Energy Density, and Combination of Capacitors

**NCERT sections covered:** 2.14, 2.15

##### Force between the plates of a capacitor (NCERT 2.14 context)

The force on plate 1 is due to the field produced by plate 2 *alone* (a plate cannot exert a net force on its own charge), so the relevant field is $E = \sigma/2\varepsilon_0$, not the full inter-plate field $\sigma/\varepsilon_0$:
$$F = \left(\frac{\sigma}{2\varepsilon_0}\right)q = \frac{q^2}{2A\varepsilon_0}$$
The plates attract each other with this force.

##### Energy stored in a capacitor (NCERT 2.15)

Charging a capacitor means moving successive small charges $dQ$ onto it against the potential $V=Q/C$ already built up. Total work done charging from $0$ to final charge $q$:
$$U = \int_0^q \frac{Q}{C}\,dQ = \frac{q^2}{2C} = \frac{1}{2}CV^2 = \frac{1}{2}qV$$

**Subtlety worth remembering for exams:** the battery does total work $QV$, but only **half** of that, $\frac{1}{2}QV$, ends up stored as the capacitor's potential energy. The other half is dissipated as heat in the connecting wires during charging -- both statements are correct simultaneously, they're just different quantities.

###### Energy density
Starting from $U = \frac{1}{2}Q^2/C$ with $C = K\varepsilon_0 A/d$ and $Q = K\varepsilon_0 E A$ (from $\sigma = Q/A = K\varepsilon_0 E$), and using $\text{volume} = Ad$:
$$\boxed{u = \frac{U}{Ad} = \frac{1}{2}K\varepsilon_0 E^2}$$
the electrostatic energy stored per unit volume of the field region (NCERT states the vacuum case $u=\frac12\varepsilon_0E^2$; this is the direct generalisation for a linear dielectric medium of constant $K$, using the field actually present inside it).

##### Combination of capacitors (NCERT 2.14)

###### Series (2.14.1)
Every capacitor in series carries the **same charge** $Q$ (by induction at each junction — the series analogue of current, not voltage, being shared in series resistors), while voltages **add**:
$$V = V_1+V_2+V_3 = \frac{Q}{C_1}+\frac{Q}{C_2}+\frac{Q}{C_3} \quad\Rightarrow\quad \boxed{\frac{1}{C_\text{eff}} = \frac{1}{C_1}+\frac{1}{C_2}+\frac{1}{C_3}}$$
Structurally the *opposite* of series resistors, where $R_\text{eff}=R_1+R_2+R_3$ directly.

###### Parallel (2.14.2)
Every capacitor sees the **same voltage** $V$; capacitances simply add:
$$\boxed{C_\text{eff} = C' + C''}$$

###### Balanced Wheatstone-bridge network of capacitors
For a bridge arrangement of five capacitors $C_1,\dots,C_5$ ($C_5$ bridging the two midpoints), if
$$\frac{C_1}{C_2} = \frac{C_3}{C_4}$$
the bridge is **balanced** and $C_5$ carries no charge — it can simply be removed from the circuit, leaving a plain series–parallel reduction of $C_1$–$C_4$.

---
*Note on this lecture's transcript:* the raw ASR transcript repeats the energy-density derivation (the "$\frac12K\varepsilon_0E^2$" section, roughly t=934s onward) two-to-three times in a row with different timestamps before moving on -- a delayed-repetition artifact, not a sign the teacher re-taught it live (a single board frame, floor_000038.jpg, shows the derivation written out exactly once). The physics content above reflects that single, real derivation; the duplicate text was not used for anything beyond confirming the same content twice.

#### Redistribution of Charges, Dielectric Strength, and Kirchhoff's Laws for Capacitor Networks

**NCERT sections covered:** 2.11

##### Redistribution of charges (NCERT 2.11, cf. Example 2.10)

Two capacitors, separately charged ($Q_1=C_1V_1$, $Q_2=C_2V_2$), connected together (positive plate to positive plate): once connected, charge redistributes until both reach the **same potential** $V$. This makes them effectively **parallel** (same $V$, different $Q_1', Q_2'$), even though the connection can visually resemble a series arrangement.

By charge conservation, $Q_1+Q_2 = Q_1'+Q_2'$, and the common potential is:
$$V = \frac{Q_1+Q_2}{C_1+C_2} = \frac{C_1V_1+C_2V_2}{C_1+C_2}$$

###### Energy loss on redistribution
Even though charge is conserved, energy is **not**. Using $U=\frac12CV^2$ for the initial (separate) and final (common-potential) states and simplifying:
$$\Delta U = U_i - U_f = \frac{1}{2}\frac{C_1C_2}{C_1+C_2}(V_1-V_2)^2$$
This is always $\geq 0$ (a squared quantity), so $U_i \geq U_f$ whenever $V_1\neq V_2$ — the "lost" energy is dissipated as heat in the connecting wires during the transient redistribution. Nothing about this process is free.

**Worked numerical** (matching the structure of NCERT Example 2.10): a $10~\mu\text{F}$ capacitor charged by $30$ V DC is connected to an uncharged $50~\mu\text{F}$ capacitor — find the common potential, the initial and final energies, and account for the difference.

###### Worked example: which way do charges flow?
Two spheres — radius $r$ with charge $+q$, radius $R$ with charge $+Q$ — connected by a wire. Using potential-inside-a-sphere-equals-potential-on-surface (from an earlier lecture):
$$V_A - V_B = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{r}-\frac{1}{R}\right)$$
Since $r<R$, this is positive, so $V_A > V_B$: charges flow from the **smaller** sphere to the **larger** one. The general rule is charges flow from **higher to lower potential**, not simply from "more charge" to "less charge" — the two are not the same thing.

##### Dielectric strength (NCERT 2.11)

Distinct from dielectric constant $K$ (dimensionless): the **dielectric strength** of a material is the maximum electric field it can withstand without breakdown of its insulating property. Vacuum's dielectric strength is infinite (nothing there to ionise); air's is about $3\times10^6$ V/m. Beyond this field, bound charges get torn free and the material starts conducting, letting stored charge leak away — this is why a capacitor's practical charge-storage limit is set by breakdown, not just by $C=Q/V$ alone.

##### Kirchhoff's laws for capacitor networks

1. **Charge conservation in an isolated system:** the net charge is constant, $\sum Q = 0$ for any change.
2. **Loop rule:** around any closed loop in a capacitor network, $\sum V + \sum \dfrac{Q}{C} = 0$ — the capacitor-network analogue of Kirchhoff's voltage law used for resistor circuits (covered in the Current Electricity chapter).

---
*Note on this lecture's transcript:* the Kirchhoff's-laws section above is grounded entirely from a board frame -- the transcript's own narration never reaches it, instead getting stuck repeating a dielectric-strength worked example and ending on an unresolved question. See the flagged span below.

##### Verify these spans
- [38:00–43:10] Board frames show a page titled 'Kirchhoff's laws in capacitors' beginning to be written at t=2120s (floor_000107, page still blank) and fully complete with both stated laws and a worked circuit by t=2240s (floor_000113) -- comfortably within this lecture's own duration and matching the third topic named in its filename. The transcript, however, never once mentions Kirchhoff -- its own narration is still mid-way through the dielectric-strength discussion (vacuum/air breakdown fields, a paper-capacitor breakdown example, and a 'can you charge a 1m-radius sphere with 1 coulomb?' worked question) right up to its last segment at t=2603s, with the paper-breakdown example itself repeated near-verbatim twice (t=2378-2467s and again t=2499-2581s) before the transcript ends without ever resolving the sphere-charging question. This matches the same delayed-repetition-then-substitution pattern found in other lectures in this chapter. The Kirchhoff's-laws claim above is grounded entirely from the board frame; the dielectric-strength claim above uses only the transcript's first (non-duplicated) pass through that material.

### Chapter 3 · Current Electricity — lecture notes

#### Electric Current, Current Density, Drift Velocity and Mobility

**NCERT sections covered:** 3.2, 3.3, 3.4, 3.5, 3.5.1

##### Electric current (NCERT 3.2)

Current is defined as the rate of flow of charge through a cross-sectional area:
$$I = \frac{Q}{t}, \qquad I = \frac{dQ}{dt}\ \text{(instantaneous form)}$$
SI unit: the **ampere** (A), with $1\text{ A} = 1\text{ C}/1\text{ s}$ -- a current of 1 A means 1 coulomb crosses the cross-section every second.

**Current is a scalar**, not a vector, even though it is conventionally drawn with an arrow: it does not obey the law of vector addition. The teacher's example -- current through a wire is the same value $I$ whether the wire runs straight or is bent/curled -- matches NCERT's own point (a curved path would need vector resolution into components if current were a vector, but the measured current is identical regardless of the wire's shape).

##### Current density (NCERT 3.4)

Current density $\vec{J}$ is current per unit area, a **vector** directed along the flow of current:
$$J = \frac{I}{A}$$
If the cross-section is tilted at angle $\theta$ to the current direction, the effective area is $A\cos\theta$, so
$$J = \frac{I}{A\cos\theta}$$
For a conductor whose cross-section changes along its length (same $I$ everywhere by charge conservation, but $A$ -- and hence $J$ -- varies), current density in general varies point to point. Since $\vec{J}$ and $\vec{A}$ are both vectors, the relation is written as a dot product, and in integral form (for $J$ non-uniform over the area):
$$I = \vec{J}\cdot\vec{A}, \qquad I = \int_A \vec{J}\cdot d\vec{A}$$
Unit of current density: $\text{A/m}^2$.

##### Random thermal motion of free electrons (NCERT 3.5, cf. Example 3.1(b))

In a conductor with no applied field, free electrons move randomly, colliding with fixed ions. Each electron's thermal speed follows from kinetic theory:
$$\frac{1}{2}mv^2 = \frac{3}{2}k_BT \implies v = \sqrt{\frac{3k_BT}{m}}$$
At room temperature this comes out to about $10^5\ \text{m/s}$ -- very fast, but because the $N$ free electrons' velocities $u_1, u_2, \ldots, u_N$ are randomly oriented, their vector average is zero:
$$\text{average velocity} = \frac{\vec{u}_1+\vec{u}_2+\cdots+\vec{u}_N}{N} = 0$$
So despite the huge thermal speed, there is **no net current** without an applied field.

##### Drift velocity (NCERT 3.5, eq. 3.14-3.17)

Switching on an electric field $\vec{E}$ exerts a force on each (negatively charged) electron:
$$\vec{F} = -e\vec{E} \quad(\text{opposite to } \vec{E}), \qquad \vec{a} = \frac{\vec{F}}{m} = -\frac{e\vec{E}}{m}$$
Current direction is conventionally opposite to the direction electrons actually drift. Averaging the velocity gained since each electron's *last collision*, over the average time between collisions (the **relaxation time** $\tau$), gives the drift velocity:
$$\vec{v}_d = \vec{a}\tau = -\frac{e\vec{E}}{m}\tau$$
Plugging in typical numbers gives $v_d \approx 1\ \text{mm/s}$ -- consistent with NCERT's Example 3.1(a) result of $\approx 1.1\ \text{mm/s}$ for a copper wire -- i.e. roughly $10^{-8}$ times the thermal speed, even though it's this tiny drift, not the large thermal motion, that constitutes the current.

##### Mobility (NCERT 3.5.1)

Mobility $\mu$ (a scalar) is the magnitude of drift velocity per unit electric field:
$$\mu = \frac{v_d}{E}$$
Substituting $v_d = eE\tau/m$:
$$\boxed{\mu = \frac{e\tau}{m}}$$
Mobility is **independent of $E$** -- it depends only on the electron's charge, mass, and the relaxation time $\tau$. Since $\tau$ decreases as temperature rises (more frequent collisions), $\mu$ also decreases with rising temperature. Combining with the earlier current-density relation gives current density directly in terms of mobility:
$$\vec{J} = -ne\vec{v}_d = ne\mu\vec{E}$$

---
*Note on this lecture's transcript:* coverage checks pass cleanly (ratio 1.02, no adjacent-repetition, and the non-adjacent duplicate scan found zero flagged pairs across all 65 segments) -- this lecture does **not** show the delayed-repetition ASR artifact found in some other lectures in this chapter. However, the transcript's own narration runs out about 12 seconds before the video's true end, right as the teacher begins the formal N-electron derivation of drift velocity. The quantitative drift-velocity result ($v_d=a\tau$, $v_d\approx1$ mm/s) and the entire mobility section above (definition, boxed formula, temperature dependence, and the final $J=ne\mu E$ relation) are grounded entirely from board frames, not narration -- the board runs ahead of the spoken explanation for this last stretch. See the flagged span below for exactly which frames and why this reads as "recording ran out," not a fabrication/repetition artifact.

##### Verify these spans
- [30:51–31:03] The transcript's final segment (starting 1851s, 'let us suppose there are n electrons...') cuts off mid-sentence right as the teacher begins the formal N-electron derivation of drift velocity (NCERT eq. 3.16-3.17) -- the transcript never verbally states vd = a*tau = -eE*tau/m, the ~1 mm/s numeric estimate, the mobility definition, mu = e*tau/m, or J = n*e*mu*E. This is NOT the delayed-repetition ASR artifact found elsewhere in this chapter: the non-adjacent duplicate scan found 0 flagged pairs across all 65 segments, coverage passes cleanly (ratio 1.02), and every segment from 1396s onward is distinct, coherent, natural classroom speech (direction-of-current, then F=-eE, then Newton's-second-law acceleration) with no verbatim or near-verbatim repeats -- it reads like real audio that simply runs out at the video's true duration, not fabrication or a re-transcription loop. Board frames, however, show this exact content already written well before the transcript catches up: floor_000063 (1240s) has the boxed vd = -eE*tau/m and vd~1mm/s, and floor_000085 (1680s) through floor_000093 (1840s) show a clean incremental build of the mobility section (heading -> ratio definition -> mu=vd/E -> mu=e*tau/m boxed -> mu independent of E, temperature dependence -> J=neuE) -- a genuine progression, not an out-of-place page, and a direct continuation of the derivation the transcript was mid-way through narrating. The teacher appears to have written ahead of his own narration for this final stretch; all claims above with transcript_span=None are grounded from these frames alone.

#### Resistance, Resistivity, Conductivity and Ohmic vs Non-Ohmic Conductors

**NCERT sections covered:** 3.4, 3.5, 3.6, 3.8

##### Ohm's law -- macroscopic form (NCERT 3.4)

If a conductor's temperature is constant, potential difference is directly proportional to current:
$$V \propto I \implies V = IR$$
where $R$ is the resistance (unit: ohm, $\Omega$; $1\ \Omega = 1\text{ V}/1\text{ A}$). A $V$-vs-$I$ plot is a straight line through the origin with slope $R$ (matching $y=mx$); an $I$-vs-$V$ plot instead has slope $1/R$ -- worth checking which axis is which before reading off a slope as $R$ or $1/R$.

Physically, resistance is the **hindrance offered to current flow**: microscopically, drifting electrons collide with the fixed positive ions of the lattice. Raising the temperature makes the ions vibrate with larger amplitude, increasing collision frequency and hence resistance.

##### Resistivity (NCERT 3.4)

Resistance depends on the conductor's geometry: $R\propto l$ (longer wire, more collisions to traverse) and $R\propto 1/A$ (larger cross-section, more parallel paths, less resistance). Combining:
$$R = \frac{\rho l}{A}$$
where $\rho$, the **resistivity**, depends only on the material's nature and temperature -- crucially, **not** on the wire's dimensions. The teacher's analogy: the density of water is the same whether you take a drop, a glass, or a bucket of it -- resistivity of copper is the same whether the copper wire is thin, thick, long, or shaped as a sheet.

**Resistance vs. resistivity:**

| | depends on dimensions (l, A)? | depends on material & temperature? | SI unit |
|---|---|---|---|
| Resistance $R$ | yes | yes | $\Omega$ |
| Resistivity $\rho$ | no | yes | $\Omega\cdot\text{m}$ |

##### Deriving $\rho = m/(ne^2\tau)$ (NCERT 3.5, eq. 3.23)

Starting from the drift-velocity relation $I = nev_dA$ (from the previous lecture) with $v_d = eE\tau/m$ and $E=V/l$:
$$I = neA\cdot\frac{eE\tau}{m} = \frac{ne^2A\tau}{m}\cdot\frac{V}{l}$$
Rearranging for $V$ and comparing with both $V=IR$ and $R=\rho l/A$:
$$R = \frac{m}{ne^2\tau}\cdot\frac{l}{A} \implies \boxed{\rho = \frac{m}{ne^2\tau}}$$
where $n$ is the free-electron (charge) density, $\tau$ the average relaxation time, $e$ the electron's charge and $m$ its mass.

**Temperature dependence (metals):** as $T$ increases, $\tau$ decreases (more frequent collisions), so $\rho$ increases with temperature. Since $\rho\propto 1/n$, a material with higher free-electron density (e.g. copper) has lower resistivity than one with lower density (e.g. an alloy or iron); silver has the least resistivity of common conductors, though copper/aluminium are used for practical wiring.

##### Conductance and conductivity

**Conductance** $g = 1/R = I/V$, unit mho -- this specific term is not part of the NCERT chapter text but is a standard reciprocal-of-resistance quantity introduced as useful vocabulary.

**Conductivity** (NCERT-covered, eq. 3.23), the reciprocal of resistivity:
$$\sigma = \frac{1}{\rho} = \frac{ne^2\tau}{m}$$

##### Macroscopic vs. microscopic Ohm's law (NCERT eq. 3.3, 3.13)

$V=IR$ relates external, circuit-level quantities (voltage, current, resistance) -- the teacher calls this the **macroscopic form**. There is also a **microscopic form** relating quantities internal to the conductor:
$$\vec{J} = \sigma\vec{E}$$
**Derivation:** from $I=nev_dA$, dividing both sides by $A$ gives $J = nev_d$; substituting $v_d = eE\tau/m$:
$$J = ne\cdot\frac{eE\tau}{m} = \frac{ne^2\tau}{m}E = \sigma E$$

##### Ohmic and non-ohmic conductors (NCERT 3.6, "Limitations of Ohm's Law")

Conductors whose $V$-$I$ graph is **linear** (they obey Ohm's law) are **ohmic conductors**. Conductors that do **not** obey Ohm's law are **non-ohmic**, in (at least) three distinct ways:

1. **$V$-$I$ graph is non-linear** -- e.g. metals at high currents.
2. **The relation between $V$ and $I$ depends on the sign of $V$** -- e.g. a junction diode (reversing $V$ does not simply reverse $I$).
3. **The $V$-$I$ relation is non-unique** -- for the same voltage $V$, the current may take two or more values -- e.g. a thyristor (an S-shaped curve with a folded-back region).

This matches NCERT's three limitations (a)-(c) closely, though the board's example for case 3 is a **thyristor** rather than NCERT's GaAs -- both are valid real devices with a non-unique $V$-$I$ curve, just a different illustrative choice.

---
*Note on this lecture's transcript:* the non-adjacent duplicate scan flagged 9 pairs, but every one turned out to be a short, genuinely-reused stock phrase or formula recited at two different points of one continuous, non-repeating derivation (e.g. stating a formula as a derivation's goal, then again once it's actually reached) -- not the delayed re-transcription artifact found elsewhere in this chapter. The one real gap: the transcript's spoken narration essentially stops at the *announcement* of "ohmic and non-ohmic conductors" (its last real content, ending right at the video's true duration), while the board already shows the complete, worked-through NCERT 3.6 content well before that announcement timestamp. The whole ohmic/non-ohmic section above is grounded from board frames alone -- see the flagged span below for the frame-by-frame detail.

##### Verify these spans
- [31:25–31:37] The transcript's last two segments (1885-1899s) only ANNOUNCE the topic -- 'when we talk of conductors, there are two types...ohmic...and non-ohmic...here we are going to talk about ohmic and non-ohmic conductors' -- and then the transcript ends (its very last segment's start, 1901s, is already past the true video duration of 1897.5s, inside only the small fixed rounding grace, so essentially nothing more was narrated). The actual ohmic/non-ohmic content -- the definitions and all three NCERT 3.6 sub-cases (i-iii), matching (a)-(c) almost exactly, down to worked diagrams for each -- is fully present on the board, built up progressively across frames floor_000079 (1560s, heading + J=sigma*E just finished) through floor_000089 (1760s, both definitions + case (i) with the metals-at-high-current graph), floor_000091 (1800s, case (ii), junction diode), and floor_000093-floor_000095 (1840-1880s, case (iii) built up step by step with the thyristor S-curve). This board sequence runs from 1560s to 1880s -- i.e. it was mostly already written well BEFORE the transcript's narration even announces starting the topic at ~1885-1901s. That is the reverse of lecture 1's pattern (board slightly ahead of speech near the very end) and large enough (over 300s) that it may reflect ASR timestamp drift accumulating over this single-shot ~32-minute transcription rather than the teacher truly writing 5+ minutes silently ahead of his own explanation. Either way, the automated non-adjacent duplicate scan found no repeated block here (all 9 flagged pairs earlier in this transcript are short, genuinely reused stock phrases/formulas within one continuous derivation, not a re-transcription loop), so this reads as a timestamp/coverage mismatch rather than fabrication. The final ohmic/non-ohmic claim above is grounded entirely from these board frames.

#### Joule's Law, Electric Power, Bulb Ratings, kWh, and Temperature Coefficient of Resistance

**NCERT sections covered:** 3.8, 3.9

##### Joule's law of heating (NCERT 3.9)

Current through a resistor converts electrical energy into heat. For charge $dQ$ moved across potential difference $V$ in time $dt$: $dW = V\,dQ = VI\,dt$. Total work (constant $V,I$) over time $t$:
$$W = \int VI\,dt = VIt$$
Using $V=IR$, this heat can also be written:
$$W = I^2Rt = \frac{V^2}{R}t$$

##### Electric power (NCERT 3.9)

$$P = \frac{W}{t} = VI = I^2R = \frac{V^2}{R}$$
SI unit: **watt** (W) $=$ J/s.

###### Bulb rating numerical
A bulb rated $220$ V, (worked example: $20$ W) consumes that many joules per second at $220$ V.
- **Max permissible current:** $I = P/V$ (e.g. $20/220 = 1/11$ A)
- **Filament resistance:** from $P=V^2/R$, $R = V^2/P$ (e.g. $220\times220/20\ \Omega$)

###### Kilowatt-hour
Electricity bills measure energy in **kilowatt-hours (kWh)**, not joules: energy $=$ power (kW) $\times$ time (h). $1$ kWh is the energy an appliance rated $1$ kW consumes running for $1$ hour:
$$1~\text{kWh} = 1000~\text{W}\times3600~\text{s} = 3.6\times10^6~\text{J}$$

##### Temperature coefficient of resistance (NCERT 3.8)

$$\Delta R \propto R\,\Delta T \;\Rightarrow\; \alpha = \frac{\Delta R}{R\,\Delta T} = \frac{R_t-R_0}{R_0\,\Delta T} \;\Rightarrow\; \boxed{R_t = R_0(1+\alpha\,\Delta T)}$$
The same relation holds for resistivity $\rho$: $\rho_t=\rho_0(1+\alpha\,\Delta T)$. (This mirrors the general pattern for thermal expansion coefficients: $\alpha=\Delta L/L_0\Delta T$, $\beta=\Delta A/A_0\Delta T$, $\gamma=\Delta V/V_0\Delta T$, with $\alpha:\beta:\gamma=1:2:3$.)

###### By material class
- **Metals:** $\alpha$ positive, comparatively large — resistivity **rises** with temperature.
- **Semiconductors:** $\alpha$ **negative** — resistivity **falls** as temperature rises (more charge carriers become available at higher $T$).
- **Alloys** (manganin, constantan, nichrome): $\alpha$ very small — resistance is nearly temperature-independent, which is exactly why these are the materials chosen for precision resistors and heating elements.

---
*Note on this lecture's transcript:* the entire temperature-coefficient section above is grounded from board frames -- the transcript itself never reaches it in words, instead getting sidetracked into a kWh digression and stopping there. See the flagged span below. "Carbon resistor" (also named in this lecture's filename) was not found in either the transcript or the sampled frames and is not covered in this note.

##### Verify these spans
- [27:44–35:29] The transcript's real narration (43 segments, no detected repetition) runs through a coherent introduction to 'different types of resistors' (t=1530-1664s: 'standard coil resistors...') before pivoting to a kilowatt-hour digression ('before understanding [resistor types], I just missed out one more thing...') that then runs to the transcript's last segment, ending mid-explanation of the kWh-to-joules conversion. The transcript never returns to resistor types, and never mentions temperature coefficient of resistance in words at all. Board frames tell a fuller story: floor_000071.jpg through floor_000095.jpg (spanning roughly t=1400-1880s, overlapping and extending past the transcript's own covered range) show a complete, thorough 'temperature coefficient of resistance' derivation plus a three-way comparison of metals, semiconductors, and alloys -- none of it narrated in the available transcript. All temperature-coefficient claims above are grounded entirely from these frames. Separately, 'carbon resistor' -- named in this lecture's own filename alongside temperature coefficient -- was NOT found in either the transcript or any of the 32 sampled board frames; rather than guess at its content, it is omitted from this note entirely.

#### Internal Resistance, EMF, Terminal PD, and Combination of Cells

**NCERT sections covered:** 3.10, 3.11

##### Internal resistance (NCERT 3.10)

A cell's electrolyte hinders current flow just like an external resistor. Internal resistance $r$ depends on the electrolyte's nature, temperature, and concentration; it is directly proportional to electrode separation $l$ and inversely proportional to immersed electrode area $A$:
$$r = \frac{cl}{A}\quad\text{(at a given temperature)}$$
$r$ **decreases** with increasing temperature, and **increases** as a cell ages with use.

##### EMF and terminal potential difference (NCERT 3.10)

**EMF** ($\mathcal E$): despite the name, has nothing to do with force — unit is the **volt**, not newton (a historical misnomer). Defined as work done per unit charge; equals the potential difference across a cell's terminals when **no current is drawn** (open circuit).

**Terminal PD** ($V$): once current flows through an external resistor $R$ (closed circuit), the measured PD across the cell's terminals:
$$\mathcal E = V + Ir \quad\Leftrightarrow\quad V = \mathcal E - Ir$$
During **discharging** (normal use), $\mathcal E > V$. Rearranged forms: $I = \dfrac{\mathcal E}{R+r}$, and $r = \dfrac{\mathcal E - V}{V}R$ (this last form is reused later for the potentiometer method of measuring internal resistance).

**During charging**, current direction through the cell reverses: $V = \mathcal E + Ir$, so $V > \mathcal E$.

##### Combination of cells (NCERT 3.11)

**Sign-convention / potential-walk method:** pick a current direction; a potential *drop* in the direction of current is negative, a *rise* is positive. Walking from one circuit point to another, sum each EMF and $Ir$ term with its sign — e.g. $V_A - V_B = \mathcal E_1 - ir_1$ for one branch. (This same method is reused later for potentiometer problems.)

###### Cells in parallel
Two cells $(\mathcal E_1,r_1)$ and $(\mathcal E_2,r_2)$ between the same points $A,B$, supplying $I_1=\dfrac{\mathcal E_1-V}{r_1}$, $I_2=\dfrac{\mathcal E_2-V}{r_2}$, with $I=I_1+I_2$. Solving for $V$ in terms of total current $I$ gives an equivalent single cell:
$$\mathcal E_{eq} = \frac{\mathcal E_1 r_2+\mathcal E_2 r_1}{r_1+r_2}, \qquad \frac{1}{r_{eq}} = \frac{1}{r_1}+\frac{1}{r_2}\quad(\text{i.e. } r_{eq}=\frac{r_1 r_2}{r_1+r_2})$$
$$V = \mathcal E_{eq} - I\,r_{eq}$$
Internal resistances combine exactly like the reciprocal (parallel) rule for resistors; the equivalent EMF is a resistance-weighted combination of the two.

---
*Note on this lecture's transcript:* the cells-in-parallel derivation above is grounded entirely from a board frame near the true end of the lecture -- the transcript's own narration stops mid-way through setting up the series case. See the flagged span below.

##### Verify these spans
- [23:41–33:10] The transcript's real (non-repeated) narration introduces 'combination of cells' and demonstrates the sign-convention potential-walk method for a series-like arrangement (deriving VA-VB=E1-ir1 and VB-VC=E2-ir2 for two cells), then cuts off exactly at the true end of the recording, right as a new worked-numerical circuit is being set up. Board frames extend past this: floor_000088.jpg through floor_000097.jpg (t=1740-1920s, within the true duration) show a full 'cells in parallel' page already in progress and then complete, deriving the equivalent EMF and equivalent internal resistance for two cells in parallel -- none of it narrated in the available transcript. The cells-in-parallel claim above is grounded entirely from the final frame. The corresponding final compact formula for cells in SERIES (which would logically precede the parallel case, analogous to E_eq=E1+E2, r_eq=r1+r2 for aligned cells) was not found written out on any sampled frame either, so it is intentionally left out of this note rather than assumed from the general pattern.

#### N Identical Cells, Kirchhoff's Rules, Wheatstone Bridge, and Resistors in Series/Parallel

**NCERT sections covered:** 3.11, 3.12, 3.13

##### N identical cells in series and parallel (NCERT 3.11)

###### In series (with external resistance $R$)
$$I = \frac{N\mathcal E}{R+Nr}$$
- $R\gg Nr$: $I \approx N\mathcal E/R = N\times$(current from one cell) — worth connecting in series.
- $R\ll Nr$: $I\approx \mathcal E/r$, same as a single cell — no benefit.

**Conclusion:** connect cells in series only when external resistance is much greater than total internal resistance.

###### In parallel (with external resistance $R$)
Net EMF $=\mathcal E$ (all cells share the same EMF between the junction points), net internal resistance $=r/N$:
$$I = \frac{\mathcal E}{R+r/N}$$
- $R\gg r/N$: $I\approx\mathcal E/R$, same as a single cell — no benefit.
- $R\ll r/N$: $I\approx N\mathcal E/r = N\times$(current from one cell) — worth connecting in parallel.

**Conclusion:** connect cells in parallel only when external resistance is much smaller than internal resistance.

##### Kirchhoff's rules (NCERT 3.12)

**First law (junction rule):** $\sum I = 0$ at any junction — current in equals current out. Assume a direction for each unknown current before solving; a wrong guess simply comes out negative in the answer.

**Second law (loop rule):** around any closed loop, $\sum(\text{EMFs and }IR\text{ drops}) = 0$ (conservation of energy). **Sign convention:** a potential *drop* in the direction you're tracing (same as assumed current, or through a cell $+\to-$) is negative; a *rise* is positive. Pick one convention and use it consistently for the whole problem — mixing conventions mid-solution gives wrong answers.

**Solving a circuit:** assign unknown currents using the junction rule (reduces the count of unknowns needed), then write loop equations for enough independent loops to match the number of remaining unknowns, and solve simultaneously.

##### Wheatstone bridge (NCERT 3.13)

Four resistors $R_1,R_2,R_3,R_4$ in a diamond/bridge arrangement, galvanometer (resistance $G$) across the diagonal. **Balance condition:**
$$\boxed{\frac{R_1}{R_2} = \frac{R_3}{R_4}}$$
When balanced, the galvanometer's two ends are at equal potential, so **no current flows through it** ($I_G=0$) — provable by applying the loop rule to two loops of the bridge and setting $I_G=0$.

**Practical use:** in a balanced bridge, the galvanometer-arm resistor can simply be dropped from the circuit for equivalent-resistance calculations, leaving a simpler series-parallel network.

##### Resistors in series and parallel: worked simplifications

- Two resistors in parallel: $R_{eff} = \dfrac{R_1R_2}{R_1+R_2}$ (only valid for exactly two).
- For symmetric networks, first check whether multiple labelled points are actually the *same* electrical node (connected by plain, zero-resistance wire) — relabelling them can reveal resistors are secretly all in parallel between the same two effective points. Example: three $1\,\Omega$ resistors that turn out to all sit between the same two nodes $A,B$ give $R_{eff}=1/3\,\Omega$ by the reciprocal rule.

---
*Note on this lecture's transcript:* the final worked example (a 5-resistor bridge-shaped network) is left unsolved -- the recording ends with it redrawn in equivalent bridge form, before a numeric answer is reached in either the transcript or the board frames. See the flagged span below.

##### Verify these spans
- [47:35–48:09] This is a clean truncation at the natural end of the recording rather than a repetition or substitution artifact: the transcript's last segment ends mid-sentence while labelling a new 5-resistor (R1-R5) network for one final effective-resistance example, and the last board frame (floor_000144.jpg, at the true end of the recording) shows that same network redrawn in its equivalent Wheatstone-bridge diamond shape, ready for balance-condition analysis -- but the lecture simply ends there, with no numeric answer worked out in either the transcript or any captured frame. This final example is therefore left unsolved in this note rather than guessed at.

#### Resistance of a Cube Network, and the Metre Bridge

**NCERT sections covered:** 3.13

##### Resistance of a cube network (worked numerical)

A cube with an identical resistor $R$ on each of its 12 edges — find the effective resistance between two opposite corners along a **body diagonal** ($X$ and $Y$).

**Symmetry argument:** current $I$ entering at $X$ splits equally into three paths of $I/3$ (three edges meet at $X$). At each of the next three vertices, $I/3$ splits further into $I/6+I/6$ (two edges lead onward toward $Y$'s neighbourhood). The six $I/6$ branches recombine in pairs back into three $I/3$ branches, converging at $Y$.

**Applying Kirchhoff's loop rule** along one $X\to Y$ path (edges carrying $I/3$, then $I/6$, then $I/3$, each of resistance $R$), back through the battery (EMF $\mathcal E$):
$$\mathcal E = IR\left(\frac13+\frac16+\frac13\right) = IR\cdot\frac{2+1+2}{6} = \frac56 IR$$
Using $I=\mathcal E/R_\text{eff}$:
$$\boxed{R_\text{eff} = \frac{5}{6}R}$$
— the classic result for a cube's body-diagonal resistance when every edge carries the same $R$.

##### The metre bridge (NCERT 3.13, application of the Wheatstone bridge)

A practical device based on the Wheatstone bridge, used to find an **unknown resistance** $X$.

**Method:** take a known resistance $R$ from a resistance box; connect $R$ and $X$ as the two "gap" resistors of the bridge. The other two bridge arms are formed by a $100$ cm resistance wire $AB$ (typically nichrome) stretched over a metre scale. Tap a jockey along the wire until the galvanometer shows **zero deflection** (the null/balance point) at position $C$, splitting the wire into length $l$ (from $A$) and $100-l$ (from $C$ to $B$).

**Balance condition:** the two wire segments act as resistances $R'=\rho l/A$ and $R''=\rho(100-l)/A$ ($\rho$ = wire resistivity, $A$ = cross-sectional area), forming a bridge with $R$ and $X$. The resistivity/area factors cancel in the balance ratio, giving:
$$\boxed{X = \frac{R(100-l)}{l}}$$

**Practical note:** for the best accuracy, the null point $l$ should fall near the **centre** of the wire (around $50$ cm).

---
*Note on this lecture's transcript:* the entire metre bridge section above is grounded from board frames -- the transcript's own 20 segments describe only the cube-resistance problem, with no mention of the metre bridge anywhere. See the flagged span below.

##### Verify these spans
- [00:00–17:42] This is an unusually total content-omission failure: the transcript's 20 segments, spanning essentially the entire lecture from t=0 to its stated end, describe ONLY the resistance-of-a-cube numerical -- the metre bridge, the lecture's own second named topic, is never mentioned even once in the transcript. Board frames tell a completely different story: floor_000041.jpg (t=800s) already shows the full metre-bridge setup (heading, method description, and circuit diagram) essentially complete, and floor_000052.jpg (t=1020s, near the true end) shows the full derivation through to the boxed final formula X=R(100-l)/l, plus a practical note about keeping the null point near the wire's centre for accuracy. Since the transcript's own timestamps leave no visible gap for this material (it reads as one continuous narration of the cube problem throughout), this looks like the ASR silently failing to transcribe an entire audio segment covering a real second topic, rather than a duration-truncation or delayed-repetition case seen elsewhere in this project. All metre-bridge claims above are grounded entirely from the two board frames.

#### The Potentiometer: Principle, Sensitivity, and Comparing EMFs

##### Why a potentiometer, not a voltmeter, for measuring EMF

EMF is defined as the potential difference across a cell's terminals when **no current** is drawn. A real voltmeter has finite (not infinite) resistance, so it always draws a small current, meaning its reading is never *exactly* EMF. A potentiometer, based on the **null-deflection method**, draws no current from the cell at its balance point — so it measures true EMF exactly.

##### Principle of the potentiometer

For a wire of uniform cross-sectional area carrying a **steady current**, the fall of potential across any portion is directly proportional to that portion's length. Since $V=IR=I\rho L/A$ and $I,\rho,A$ are all constant:
$$V = KL, \qquad K = \frac{V}{L} = \text{potential gradient (fall of potential per unit length)}$$
(Analogous to other length-based rate quantities, e.g. temperature gradient $dT/dx$.)

##### Sensitivity

The smallest potential difference the potentiometer can detect. Smaller $K$ (potential gradient) $\Rightarrow$ finer resolution $\Rightarrow$ **higher** sensitivity (e.g. $0.1$ V/cm is more sensitive than $1$ V/cm). Increase sensitivity by:
1. **Increasing** the total wire length, or
2. **Decreasing** the potential difference (equivalently, current) across the wire — in practice, by adding a series rheostat in the main circuit.

##### Apparatus

A long uniform wire (e.g. $4$ m) from $A$ to $B$, connected in the main circuit to a driver battery, key, and optional rheostat. The two cells being compared connect via a **commutator** (three-way switch, only one cell in the galvanometer branch at a time), with a protective resistance in series with the galvanometer, and a **jockey** to tap along the wire and find the null point.

##### Use 1: comparing EMFs of two cells

Connect $\mathcal E_1$ to the galvanometer branch ($\mathcal E_2$ left open); tap the jockey to find the null point (zero galvanometer deflection $\Rightarrow$ zero current drawn from $\mathcal E_1$) at length $L_1$: $\mathcal E_1 = KL_1$. Repeat with $\mathcal E_2$ to get $\mathcal E_2=KL_2$. Then:
$$\boxed{\frac{\mathcal E_1}{\mathcal E_2} = \frac{L_1}{L_2}}$$

**Precaution:** the positive terminal of each cell must connect to the *same* positive terminal of the main circuit — wrong polarity means the potentials add instead of oppose, and no null point will ever be found.

##### Use 2: internal resistance of a cell (setup only)

A board heading and circuit diagram show a second use beginning: finding a cell's internal resistance using the potentiometer, with a resistance box added in the cell-and-galvanometer branch, alongside a reminder of $r=\dfrac{(\mathcal E-V)}{V}R$ (a formula derived in an earlier lecture of this chapter specifically for this purpose). Only the setup is confirmed here — see the flagged span below for why the worked derivation isn't included.

---
**A note on syllabus status:** the Potentiometer topic covered in this lecture does not appear anywhere in the current (rationalised) NCERT Class 12 Physics textbook's Current Electricity chapter -- it was one of the topics removed in the CBSE 2022-23 rationalisation. It may still be relevant depending on your specific school's or exam's syllabus, but it is not in the current official NCERT text, so no NCERT section number is cited for any claim in this note.

##### Verify these spans
- [32:08–34:07] The transcript's real narration (247 unique segments) runs coherently through the potentiometer's principle, sensitivity, apparatus, and the EMF-comparison use, ending naturally on the positive-terminal precaution at t=1928.7s -- about 119 seconds before the recording's true end. The last captured board frame (floor_000096.jpg, t=1900s) shows a second use of the potentiometer just beginning: 'Find internal resistance of cell using potentiometer', with a circuit diagram (resistance box, galvanometer) and a reminder of the r=[(E-V)/V]R formula derived in an earlier lecture -- but only the heading and circuit setup are visible, with no further frames available to confirm a worked derivation. This second use is included above only as what is directly visible (the setup), not as a completed derivation, since neither the transcript nor any later frame confirms how far it was carried.

### Chapter 4 · Moving Charges and Magnetism — lecture notes

#### Oersted's Experiment, Biot-Savart Law, and Field at the Centre of a Coil

**NCERT sections covered:** 4.1, 4.4, 4.5

##### Historical introduction (NCERT 4.1)
Magnetism was first known through **lodestone**, a naturally magnetised form of magnetite (an iron ore, $\text{Fe}_3\text{O}_4$), which attracts small pieces of iron. The realisation that electricity and magnetism are connected -- that electricity can produce a magnetic field and a magnetic field can (in turn) produce an electric field -- gave rise to the unified subject of **electromagnetism**, associated with Faraday and Maxwell. A moving charge, or equivalently a **current element** $I\,d\vec l$ (a small length $d\vec l$ of current-carrying wire), is a source of magnetic field.

###### Oersted's experiment
A compass needle placed near a current-carrying wire deflects when current flows, showing that a current-carrying wire produces a magnetic field around it -- the first experimental link between electricity and magnetism.

**Teacher's 'SNOW' deflection rule** (a memory device, not itself an NCERT term): if current flows from **S**outh to **N**orth and the wire is **O**ver the needle, the needle's north pole deflects toward **W**est. Reversing the current direction (N to S) flips the deflection to East; placing the wire below the needle instead of above it also flips the result. Physically this is just a special case of the general right-hand rule for the circular field around a straight wire, applied to the fixed N-S rest orientation of a compass needle.

##### Magnetic field lines
Compared with electric field lines (Chapter 1):
- **Magnetic field lines always close on themselves** (outside a bar magnet they run N $\to$ S; inside the magnet, S $\to$ N) -- there is no starting or ending point.
- **Electric field lines never form closed loops** -- they start on positive charge and terminate on negative charge. This is the key structural difference between the two, and NCERT states it explicitly (Sec. 4.4, and again in the chapter summary).
- Field lines of either kind **never intersect**: at a crossing point the tangent (which gives the field direction) would have to point in two directions at once, which is impossible.
- **Parallel, equally spaced lines** indicate a **uniform** field; **crowded** lines indicate a stronger field magnitude.

##### Biot-Savart law (NCERT 4.4)
For a current element $I\,d\vec l$ carrying current $I$, the magnetic field $d\vec B$ it produces at a point $P$, a distance $r$ away, obeys:

1. $dB \propto I\,dl$
2. $dB \propto \sin\theta$, where $\theta$ is the angle between the current element and the line joining the element to $P$
3. $dB \propto \dfrac{1}{r^2}$

Combining these (in exact analogy with Coulomb's law, replacing $\frac{1}{4\pi\varepsilon_0}$ with $\frac{\mu_0}{4\pi}$):
$$dB = \frac{\mu_0}{4\pi}\,\frac{I\,dl\sin\theta}{r^2}$$

In vector form, since the $\sin\theta$ dependence signals a cross product:
$$d\vec B = \frac{\mu_0}{4\pi}\,\frac{I\,d\vec l \times \hat r}{r^2} = \frac{\mu_0}{4\pi}\,\frac{I\,d\vec l \times \vec r}{r^3}$$

###### Finding the direction of $d\vec B$
Three equivalent right-hand rules were used on the board:
1. **Right-hand palm rule:** point the thumb along the current, the centre finger toward $P$; the palm then faces the direction the field emerges from (out of the page $\odot$, or into the page $\otimes$).
2. **Right-hand thumb rule (for a straight wire):** hold the wire with the thumb pointing along the current; the curled fingers give the sense of circulation of $\vec B$ around the wire.
3. **Right-hand screw rule:** $\vec B$ is perpendicular to the plane containing $d\vec l$ and $\hat r$, in the sense obtained by imagining the rotation carrying $d\vec l$ toward $\hat r$ -- this is the exact rule NCERT itself gives as a footnote to the Biot-Savart law. This rule, and the label "$\mu_0$ = permeability of free space", appear worked out on the board but are **not narrated in the transcript at all** -- see the flagged span below.

**Worked example** (from the board): for a vertical wire carrying current downward, with $P$ to its side, the palm-rule construction (thumb down, centre finger toward $P$) gives a palm facing outward, so $\vec B$ at $P$ points out of the page.

##### Magnetic field at the centre of a current-carrying circular coil (NCERT 4.5, special case)
For a circular coil of radius $R$ carrying current $I$, every current element $I\,dl$ on the coil is at the same perpendicular distance $R$ from the centre, with $\theta = 90^\circ$ (so $\sin\theta = 1$). By the Biot-Savart law,
$$dB = \frac{\mu_0}{4\pi}\frac{I\,dl}{R^2}$$
Integrating around the full circumference ($\oint dl = 2\pi R$):
$$B = \oint dB = \frac{\mu_0}{4\pi}\frac{I}{R^2}(2\pi R)$$
$$\boxed{B = \frac{\mu_0 I}{2R}}$$
This matches NCERT's own derivation in Sec. 4.5, which reaches the same field-at-the-centre result as the $x=0$ special case of the more general on-axis formula $B = \dfrac{\mu_0 I R^2}{2(x^2+R^2)^{3/2}}$ (the general axis formula itself is developed in the next lecture). The board also sketches the closed-loop field-line pattern threading through a current-carrying loop, consistent with NCERT Fig. 4.10.

##### Verify these spans
- [36:50–37:17] Board frames (floor_000068 at 1340s, floor_000077 at 1520s) show a third direction rule -- the 'right-hand screw rule', with a diagram and the label 'mu0 = permeability of free space' -- fully written out on the same page as rules 1 and 2. The transcript, however, never narrates this rule or these words at all ('screw' and 'permeability' have zero hits across the full 141-segment transcript): after finishing rule 2 (right-hand thumb rule, ending ~2210s) it jumps directly to a worked direction example at 2237s and then on to the coil derivation. Automated coverage and repetition checks both pass cleanly here (no duplicated block, no duration overshoot) -- this is a case of the ASR silently skipping real board content rather than looping, not a duration or repetition failure. The screw-rule claim above is grounded from the board frames alone.

#### Magnetic Field on the Axis of a Coil, and Ampere's Circuital Law

**NCERT sections covered:** 4.5, 4.6

##### Magnetic field on the axis of a circular current loop (NCERT 4.5)
Building on the previous lecture's centre-of-coil result, this lecture derives the field at a general point $P$ on the **axis** of a circular loop of radius $R$ carrying current $I$, at distance $x$ from the centre $O$.

**Setup.** A current element $I\,d\vec l$ at point $A$ on the loop is at distance $r$ from $P$. Since the loop lies in a plane through $O$ perpendicular to the axis, $d\vec l$ and the displacement vector $\vec r$ (from the element to $P$) are (very nearly) perpendicular, so $\sin\theta \approx 1$ and the Biot-Savart law gives
$$dB = \frac{\mu_0}{4\pi}\frac{I\,dl}{r^2}$$
$d\vec B$ is perpendicular to the plane containing $d\vec l$ and $\vec r$, and can be resolved into a component $dB\sin\alpha$ along the axis and $dB\cos\alpha$ perpendicular to it, where $\alpha$ is the angle between $\vec r$ and the axis.

**Symmetry argument.** For every element, the diametrically opposite element (same distance $r$, same $\alpha$) produces a field whose perpendicular component is equal and opposite -- so all perpendicular ($\cos\alpha$) components cancel around the full loop, while the axial ($\sin\alpha$) components all add. Hence the net field lies entirely along the axis:
$$B = \oint dB\sin\alpha$$

**Completing the integral.** Using $\sin\alpha = R/r$ and $r=(R^2+x^2)^{1/2}$ (Pythagoras), and $\oint dl = 2\pi R$:
$$B = \frac{\mu_0}{4\pi}\frac{I}{r^2}\cdot\frac{R}{r}\cdot 2\pi R = \frac{\mu_0}{4\pi}\frac{I\,(2\pi R)\,R}{(R^2+x^2)^{3/2}}$$
$$\boxed{B = \frac{\mu_0\, I\, R^2}{2\,(R^2+x^2)^{3/2}}}$$
Setting $x=0$ recovers $B=\dfrac{\mu_0 I}{2R}$, matching the direct centre-of-coil derivation from the previous lecture -- exactly the check NCERT itself makes in Sec. 4.5.

##### Ampere's Circuital Law and its first application (NCERT 4.6)
*(This entire section is grounded from board frames only -- the transcript does not narrate it. See the flagged span below for why, and the strong corroborating evidence from the very next lecture.)*

**Statement.** The line integral of the magnetic field along the boundary of any closed path (an "Amperian loop") equals $\mu_0$ times the net current enclosed by that path:
$$\oint \vec B \cdot d\vec l = \mu_0 I_e$$

**Application: infinitely long straight current-carrying wire.** Take a circular Amperian loop of radius $r$ centred on the wire. By symmetry $B$ is constant in magnitude on the loop and everywhere tangential to it (parallel to $d\vec l$, so $\vec B\cdot d\vec l = B\,dl$):
$$\oint \vec B\cdot d\vec l = B\oint dl = B(2\pi r) = \mu_0 I \quad\Rightarrow\quad \boxed{B = \frac{\mu_0 I}{2\pi r}}$$
This is the same result NCERT reaches via Ampere's law in Sec. 4.6 (Eq. 4.14).

**Finite-wire generalisation.** For a straight wire of finite length, with $P$ at perpendicular distance $r$ and the two ends subtending angles $\alpha_1,\alpha_2$ at $P$:
$$B = \frac{\mu_0 I}{4\pi r}\left(\sin\alpha_1 + \sin\alpha_2\right)$$
As the wire becomes infinite, $\alpha_1,\alpha_2 \to 90^\circ$, so $\sin\alpha_1+\sin\alpha_2\to 2$ and the formula correctly reduces to $B=\dfrac{\mu_0 I}{2\pi r}$ -- the board explicitly checks this consistency between the Biot-Savart (finite-wire) and Ampere's-law (infinite-wire) results.

##### Verify these spans
- [15:40–23:29] This lecture's filename promises both 'B at axis of coil' AND 'Ampere circuital law', but the transcript (85 segments, clean coverage ratio 1.012, zero flagged near-duplicate pairs from the delayed-repetition scan) never once mentions Ampere, 'circuital', or an enclosed/boundary current -- every single segment, right up to the last one ending at 1426.7s, narrates only the on-axis-of-a-coil derivation (culminating in the x=0 sanity check against the earlier centre-of-coil result). Board frames tell a different story: by t=940s (floor_000048) the page has already turned to a heading 'Ampere circuital law:'; by t=1040s (floor_000053) the full boxed statement (closed-loop integral of B.dl = mu0*I_e) is written; and by t=1240-1380s (floor_000063/67/70, still comfortably inside the true 1409.8s duration) a complete first application -- straight-wire Amperian loop giving B=mu0*I/(2*pi*r), plus the finite-wire generalisation B=(mu0*I/4*pi*r)(sin a1+sin a2) checked against the infinite-wire limit -- is fully worked out with diagrams. This is corroborated independently by the very next lecture in this chapter (file 1xP2VppJSiqby6nk4Gys--lX5GeM1TGNg, 'Solenoid and toroid'), whose transcript opens mid-thought with 'let us try to see the SECOND application of your ampere circuital law that is magnetic field due to a solenoid' -- confirming a first application (straight wire, via Ampere's law) really was taught, immediately before that. So the real audio almost certainly does contain the Ampere's-law statement and straight-wire derivation somewhere in this lecture's second half; the ASR simply never transcribes it, instead only ever narrating the coil-axis algebra, all the way to the true duration boundary. Neither the coverage check nor the adjacent/delayed-duplicate detectors catch this, because nothing is fabricated or repeated -- real content is silently missing rather than replaced by a copy. All three Ampere's-law claims above are grounded from board frames (and the lecture-3 cross-reference) alone, with no transcript span.

#### Magnetic Field Due to a Solenoid and a Toroid, and Inside/Outside a Current-Carrying Conductor

**NCERT sections covered:** 4.6, 4.7

##### The solenoid (NCERT 4.7)

A long wire wound as a closely-packed helix. If closely wound (no gaps) and long, individual turns' fields add up along the axis to give a **uniform field inside**. Applying Ampere's circuital law with a rectangular Amperian loop (one side of length $l$ inside the solenoid parallel to the axis, the opposite side far outside where $B\approx0$, the two connecting sides perpendicular to $\vec B$ so $\vec B\cdot d\vec l=0$ there):
$$Bl = \mu_0(nl)I \quad\Rightarrow\quad \boxed{B = \mu_0 n I}$$
where $n$ = turns per unit length.

**Determining polarity from winding:** viewed end-on, current flowing **clockwise** at a face $\Rightarrow$ that face is a **south** pole (field lines converge/enter); **anticlockwise** $\Rightarrow$ **north** pole (field lines emerge) — consistent with field lines running south-to-north inside the solenoid.

##### The toroid (application of Ampere's law, NCERT 4.6)

An **endless solenoid**: a solenoid bent into a closed ring. Current enters at one point on the cross-section and exits diametrically opposite, alternating dots/crosses around the ring; field lines inside the core form **concentric circles**.

**Three regions:**
1. **Empty space enclosed by the ring** (the "hole"): no current enclosed $\Rightarrow B=0$.
2. **Outside the toroid entirely:** $B=0$.
3. **Inside the toroid's wound core** — the only region with field:
$$B = \mu_0 n I, \qquad n = \frac{N}{2\pi R_\text{avg}}$$
(same form as a straight solenoid, using the average of the toroid's inner and outer radii for $R_\text{avg}$).

##### Field inside/outside a long straight current-carrying conductor (Ampere's law application)

A cylindrical conductor of radius $a$ carries current $I$, uniformly distributed over its cross-section. Using a circular Amperian loop of radius $r$:

- **Outside** ($r>a$): full current $I$ enclosed: $B(2\pi r)=\mu_0 I \Rightarrow \boxed{B=\dfrac{\mu_0 I}{2\pi r}}$ — same as a thin wire, $\propto 1/r$.
- **Inside** ($r<a$): only the enclosed fraction of current counts (uniform current density): $I_\text{enc} = I\dfrac{r^2}{a^2}$, giving $B(2\pi r) = \mu_0 I\dfrac{r^2}{a^2} \Rightarrow \boxed{B = \dfrac{\mu_0 I r}{2\pi a^2}}$ — $\propto r$.
- **At the surface** ($r=a$): both expressions agree, $B=\dfrac{\mu_0 I}{2\pi a}$, the **maximum** value.

$B$-vs-$r$ graph: a straight line rising from the centre to the surface, then a $1/r$ curve falling off outside.

#### Force on a Moving Charge in a Magnetic Field, the Lorentz Force, the Velocity Selector, and Helical Motion

**NCERT sections covered:** 4.2, 4.3

##### Force on a moving charge in a magnetic field (NCERT 4.2)

$$\vec F = Q(\vec v\times\vec B)$$
- **Maximum** at $\theta=90°$ (angle between $v$ and $B$): $F_\max = BQv$.
- **Zero** at $\theta=0°$ or $180°$ (velocity parallel/antiparallel to $B$) — and also zero if $v=0$ (a stationary charge feels no magnetic force).
- **Direction:** perpendicular to the plane of $\vec v$ and $\vec B$, via the right-hand curl rule (curl fingers from $\vec v$ to $\vec B$, thumb gives $\vec F$).

###### The Lorentz force
When a charge moves through both an electric field $\vec E$ and a magnetic field $\vec B$ simultaneously, the electric force $Q\vec E$ and magnetic force $Q(\vec v\times\vec B)$ combine as a vector sum:
$$\boxed{\vec F = Q\vec E + Q(\vec v\times\vec B)}$$

###### Velocity selector (setup)
Uses **crossed** electric and magnetic fields ($\vec E\perp\vec B$). A charge $+q$ moving with velocity $v$ (say along the $x$-axis) experiences both an electric force and a magnetic force simultaneously, generally in different directions — the basis of a device that only lets through particles of one specific speed (where the two forces exactly balance).

##### Helical motion (NCERT 4.3)

For velocity $\vec v$ at angle $\theta$ to $\vec B$, decompose it:
- $v\cos\theta$, **parallel** to $\vec B$ — unaffected by the magnetic force, giving uniform straight-line motion along $\vec B$.
- $v\sin\theta$, **perpendicular** to $\vec B$ — causes circular motion (same $\vec v\times\vec B$ analysis as for purely perpendicular velocity).

The combination of straight-line motion along $\vec B$ and circular motion around it traces a **helix**. The distance moved along $\vec B$ in one full rotation is the **pitch**:
$$p = v_\parallel T = v\cos\theta\cdot\frac{2\pi m}{Bq}$$
The radius of the helix equals the radius of its circular component of motion.

##### Verify these spans
- [26:40–30:06] The transcript's real narration continues describing the velocity-selector's cross-product setup (unit vectors i, j, k) right up to its last segment at t=1827s (just past the true 1806.9s duration), never once using the word 'helix' or describing helical motion -- despite it being the second topic explicitly named in this lecture's own filename ('force on charge, helix'). Board frames tell a different story: floor_000081.jpg (t=1600s) already shows the helix topic's introduction (decomposing v into components parallel and perpendicular to B), and floor_000090.jpg (t=1780s, essentially at the true end) shows the complete derivation through to the pitch formula and the radius-of-helix statement, plus a one-line preview of 'cyclotron' (the next lecture's topic in this same chapter). The helical-motion claim above is grounded entirely from these two frames; the velocity selector's final balancing condition (which would follow directly as qE=qvB, i.e. v=E/B, from the setup that IS confirmed in the transcript) is not separately asserted here since neither the transcript nor a frame explicitly states that concluding line.

#### The Cyclotron

**NCERT sections covered:** 4.3

##### The cyclotron (NCERT 4.3)

A device (developed by Lawrence) that accelerates **positively charged particles** (proton, deuteron, alpha particle) to high energies using repeated passes through a comparatively small oscillating electric field, combined with a strong magnetic field.

###### Construction
Two hollow, evacuated D-shaped metal chambers ("Dees", $D_1,D_2$) separated by a small gap, connected to a high-frequency oscillator (providing the oscillating field across the gap), placed in a strong magnetic field perpendicular to the Dees' plane.

###### Working
A positive charge injected near the centre accelerates across the gap into one Dee, traces a **semicircular path** inside it (magnetic force only — no field inside a hollow conducting Dee), returns to the gap just as the oscillator's polarity reverses, gets accelerated again, and traces a **larger** semicircle in the next Dee (higher speed now). This repeats — spiralling outward — until the particle exits through a window with high velocity and strikes a target.

###### Mathematics
Inside a Dee, the magnetic force supplies centripetal force:
$$Bqv = \frac{mv^2}{r} \;\Rightarrow\; r = \frac{mv}{Bq}$$
Using $v=r\omega$:
$$\boxed{\omega = \frac{Bq}{m}}, \qquad T = \frac{2\pi m}{Bq}$$
$\omega$ (and $T$) are **independent of radius** $r$ — as the radius grows with each pass, speed grows proportionally, keeping each semicircle's transit time constant. This is exactly why the oscillator, tuned to this fixed period, stays synchronized with the particle across every pass.

###### Why not electrons?
An electron's tiny rest mass means it reaches relativistic speeds almost immediately, so its **relativistic mass** $m=m_0/\sqrt{1-v^2/c^2}$ grows with speed rather than staying constant. Since $T=2\pi m/(Bq)$ depends on mass, a growing mass breaks the match with the fixed-frequency oscillator — the electron drifts **out of phase** and stops being properly accelerated. Heavier particles (protons, deuterons, alpha particles) are far less affected by this at cyclotron energies, so cyclotrons work well for them but not for electrons.

#### Numerical: Identifying Proton, Alpha Particle, and Electron by Radius in a Magnetic Field

**NCERT sections covered:** 4.3

##### Worked numerical: identifying particles by radius in a magnetic field

Three particles -- a **proton**, an **alpha particle**, and an **electron** -- all moving with the same velocity $v$, enter a uniform magnetic field $B$ and trace three visibly different curved paths. Identify which is which.

**Step 1 -- sign of charge:** proton and alpha particle are both positive; the electron is negative, so it curves the *opposite* way from the other two. This immediately identifies the electron.

**Step 2 -- radius comparison for the two positive particles:**
$$r = \frac{mv}{Bq} = \frac{v}{B(q/m)} \quad\Rightarrow\quad r \propto \frac{1}{q/m}$$
- **Proton** ($^1_1\text{H}$): charge $+e$, mass $m$ $\Rightarrow q/m = e/m$
- **Alpha particle** ($^4_2\text{He}$, a helium nucleus): charge $+2e$, mass $4m$ $\Rightarrow q/m = 2e/4m = e/2m$

Since $e/m > e/2m$, the proton has the larger charge-to-mass ratio, hence the **smaller** radius: $r_\text{proton} < r_\text{alpha particle}$. The particle tracing the smaller-radius curve is the proton; the larger-radius one is the alpha particle.

###### Reading charge and mass from isotope notation
For $^A_Z X$: the subscript $Z$ (atomic number) gives charge $+Ze$; the superscript $A$ (mass number) gives mass $\approx Am$ (one nucleon mass each). Example: deuteron ($^2_1\text{H}$) and tritium ($^3_1\text{H}$) share the same charge $+e$ (both hydrogen, $Z=1$) but different masses ($2m$ and $3m$, from their different mass numbers).

---
*Note: this recording continues past this numerical into the start of the next topic (force on a current-carrying conductor in an external magnetic field) — that derivation is covered fully in the following lecture's own note, not duplicated here.*

#### Force on a Current-Carrying Conductor, Fleming's Left-Hand Rule, Force Between Parallel Wires, and the Ampere

**NCERT sections covered:** 4.2, 4.8

##### Force on a current-carrying conductor (NCERT 4.2)

Each conduction electron (drift velocity $v_d$) feels $\vec f = (-e)(\vec v_d\times\vec B)$. With electron density $n$, a conductor of length $L$, area $A$ has $nAL$ electrons, total charge $-enAL$:
$$\vec F = (-enAL)(\vec v_d\times\vec B)$$
Using $I=neAv_d$ (and that $\vec v_d$ points opposite to conventional current), the signs resolve to:
$$\boxed{\vec F = I(\vec L\times\vec B)}$$
where $\vec L$ points along the current, magnitude = conductor length.

###### Fleming's left-hand rule
Hold thumb, first (index), and centre (middle) fingers of the **left** hand mutually perpendicular: centre finger = current direction, first finger = field direction, **thumb = force direction**. (Equivalently, evaluate $I\vec L\times\vec B$ directly with unit vectors.)

##### Force between two parallel current-carrying wires (NCERT 4.8)

Two infinitely long, straight, parallel wires, currents $I_1,I_2$, separated by $r$. Field due to wire 1 at wire 2's location: $B_1 = \dfrac{\mu_0 I_1}{2\pi r}$. Force on wire 2 (length $L$) in this field: $F_2 = I_2LB_1$ (angle $90°$), giving **force per unit length**:
$$\boxed{\frac{F}{L} = \frac{\mu_0 I_1 I_2}{2\pi r}}$$
(By symmetry, the same expression gives the force per unit length on wire 1 due to wire 2.)

**Direction:** currents in the **same** direction $\Rightarrow$ wires **attract**; currents in **opposite** directions $\Rightarrow$ wires **repel**.

###### Definition of the ampere
Setting $I_1=I_2=1$ A and $r=1$ m in the force-per-unit-length formula, with $\mu_0=4\pi\times10^{-7}$ T·m/A:
$$\frac{F}{L} = \frac{\mu_0}{2\pi}(1)(1) = 2\times10^{-7}~\text{N/m}$$
**One ampere** is the constant current which, if maintained in each of two infinitely long, straight, parallel conductors of negligible cross-section placed 1 metre apart in vacuum, would produce a force of exactly $2\times10^{-7}$ newton per metre of length between them.

##### Verify these spans
- [26:20–26:39] The transcript's real narration ends mid-sentence right after stating the force-per-unit-length formula and beginning to plug in numbers ('this value will be 2x10^-7 ne[wton]...'), cutting off just short of formally stating the definition of 1 ampere -- the lecture's own second named topic. No board frame is available past t=1300s to confirm the exact wording used for this definition. Since the numerical ingredients (mu0/(2 pi) = 2x10^-7 N/A^2, from mu0=4*pi*10^-7) are already given directly in the transcript's own final segments, the definition of 1 ampere is stated in this note as the direct, unavoidable algebraic completion of what the transcript itself already establishes -- setting I1=I2=1 A and r=1 m in the just-derived formula -- rather than as independently confirmed content.

#### Torque on a Current-Carrying Loop in a Uniform Magnetic Field

**NCERT sections covered:** 4.9

##### Torque on a current-carrying loop (NCERT 4.9)

###### Special case: B in the plane of the loop (normal $\perp B$)
Rectangular loop (sides $PQ=RS=l$, $QR=SP=b$, current $I$), $\vec B$ lying in the loop's plane. Forces on the two sides parallel to $B$ (SR, QP) are zero ($I\vec L\times\vec B=0$ there). Forces on the two sides perpendicular to $B$ (PS, RQ) are each $ILB$, equal and opposite but acting along **different** lines — a couple.

$$\tau = (\text{force})\times(\text{perpendicular distance between lines of action}) = (ILB)(b) = I(lb)B = \boxed{IAB}$$
where $A=lb$ is the loop's area. Direction: perpendicular to the plane of $\vec A$ and $\vec B$ (right-hand cross-product rule).

*Mnemonic used in the lecture:* force $=I\vec L\times\vec B$ ("I love Bhopal"), torque $=I\vec A\times\vec B$ ("I admire Bhopal").

###### General case: normal at angle $\theta$ to $B$
Now the loop's normal makes angle $\theta$ (not $90°$) with $\vec B$. Forces on the sides perpendicular to the *original* orientation (QR, SP) turn out equal, opposite, and **collinear** — their resultant is zero. Forces on the other pair (PQ, RS) are equal, opposite, but **not collinear** — these constitute the torque:
$$\tau = (ILB\sin\theta)\times b = IAB\sin\theta$$
$$\boxed{\vec\tau = I(\vec A\times\vec B)}, \qquad |\tau| = IAB\sin\theta$$
The special case above ($\theta=90°$, $\sin\theta=1$, $\tau=IAB$) is the **maximum-torque** special case of this general result.

##### Verify these spans
- [25:26–25:29] The transcript's last segment ends right as the general-case torque setup is completed ('force on PQ and RS... will constitute torque') but before the final formula is spoken. A board frame just past this point (floor_000072.jpg, t=1420s) shows the completed derivation and the boxed general result torque=I*A*B*sin(theta) (vector form tau=I(A x B)), so the final general-torque claim above is grounded from that frame rather than the transcript's own words, though it is the direct, expected algebraic completion of what the transcript does establish.

### Chapter 5 · Magnetism and Matter — lecture notes

#### Magnetism Intro: Gauss's Law, Electrostatic Analogy, and Bar Magnet as Equivalent Solenoid

**NCERT sections covered:** 5.1, 5.2.2, 5.2.3, 5.2.4, 5.3

##### Introduction: monopoles and Gauss's law in magnetism (NCERT 5.1, 5.3)
Lodestone (natural magnetite) is introduced as a naturally occurring magnet, and the earth itself is described as behaving like a giant magnet (a freely suspended bar magnet always settles north-south). A key qualitative fact is developed by repeatedly breaking a bar magnet: **magnetic monopoles do not exist** -- however small a piece you cut, it still has both an N and an S pole.

This directly motivates **Gauss's law in magnetism**: since field lines leaving the N pole always curve around and re-enter at S (closed loops, unlike electric field lines which start/end on isolated charges), the net magnetic flux through *any* closed surface is zero:
$$\oint \vec B\cdot d\vec S = 0$$
This is explicitly contrasted with Gauss's law in electrostatics, $\oint \vec E\cdot d\vec S = q/\varepsilon_0$, which is nonzero in general because isolated electric charge does exist.

##### Bar magnet vs. solenoid: similarities and differences
Before deriving the equivalence formally, the lecture recaps general field-line properties (closed loops, tangent gives direction, never intersect, density $\propto$ strength) and lists concrete differences/similarities between a bar magnet and a current-carrying solenoid:

- **Differences:** a bar magnet's field strength is fixed once magnetised and its poles cannot be swapped; a solenoid's field $B=\mu_0 nI$ can be tuned via turns-per-length $n$ or current $I$, and its poles reverse if the current direction reverses.
- **Similarities:** both align north-south when freely suspended, both attract small iron pieces, and both have field lines and two poles.

These similarities are the motivation for treating a bar magnet as an "equivalent solenoid" -- the main derivation of this lecture.

##### The electrostatic analogy (NCERT 5.2.3, 5.2.4)
A large stretch of the lecture builds up magnetism's dipole formulas entirely by comparison with the already-known electric dipole formulas, introducing a hypothetical **pole strength** $m$ (analogous to charge $q$) purely as a bookkeeping device -- flagged explicitly as *not* physically real, since isolated poles don't exist.

| Electrostatics | Magnetism |
|---|---|
| Charges $q_1,q_2$ | Pole strengths $m_N,\,m_S$ (hypothetical) |
| $F=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q_1q_2}{r^2}$ | $F=\dfrac{\mu_0}{4\pi}\dfrac{m_1m_2}{r^2}$ |
| $\vec p = q(2\vec l)$, points $-q\to+q$ | $\vec M = m(2\vec l)$, points S$\to$N |
| $\vec\tau=\vec p\times\vec E$ | $\vec\tau=\vec M\times\vec B$ |
| $U=-\vec p\cdot\vec E$ | $U=-\vec M\cdot\vec B$ |
| $E=F/q$ | $B=F/m$ |
| $E=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}$ | $B=\dfrac{\mu_0}{4\pi}\dfrac{m}{r^2}$ |
| $E_\text{axial}=\dfrac{2p}{4\pi\varepsilon_0 r^3}$ | $B_\text{axial}=\dfrac{\mu_0}{4\pi}\dfrac{2M}{r^3}$ |
| $E_\text{equatorial}=\dfrac{-p}{4\pi\varepsilon_0 r^3}$ | $B_\text{equatorial}=-\dfrac{\mu_0}{4\pi}\dfrac{M}{r^3}$ |

The magnetic dipole moment magnitude is pinned down independently by comparing two expressions for the torque on a current loop of $N$ turns, area $A$, in field $B$: $\tau=NIAB\sin\theta$ (from $\tau=I\vec A\times\vec B$, done in the previous chapter) against $\tau=MB\sin\theta$ (the magnetic analogue of $\tau=pE\sin\theta$), giving
$$M = NIA$$
and from $M=m(2l)$ with $[M]=\text{A m}^2$, the SI unit of pole strength $m$ works out to $\text{A m}$.

*Brief aside (not fully worked):* the lecture briefly poses cutting a bar magnet either along its axis or perpendicular to its axis through the centre, noting in both cases you get two smaller magnets, each still with an N and S pole -- reinforcing the "no monopoles" theme -- but does not carry the numerical through to compute the resulting pole strengths/moments.

##### Derivation: bar magnet as an equivalent solenoid (NCERT 5.2.2)
**Goal:** prove that at a large axial distance $r$, the magnetic field of a current-carrying solenoid equals the known axial field of a bar magnet, $B=\dfrac{\mu_0}{4\pi}\dfrac{2m}{r^3}$ -- i.e. a solenoid *is* equivalent to a bar magnet of moment $M=NIA$.

**Prerequisite** (recalled from the previous chapter): the on-axis field of a single circular current loop of radius $a$ at distance $x$ from its centre is $B=\dfrac{\mu_0 I a^2}{2(a^2+x^2)^{3/2}}$, which reduces to $B=\dfrac{\mu_0 I}{2a}$ at the centre ($x=0$).

**Setup:** a solenoid of radius $a$, total length $2l$, turns per unit length $n$, axis along $x$ with origin $O$ at the centre. Field point $P$ lies on the axis at distance $r$ from $O$ ($r\gg l$, $r\gg a$). Consider a thin slice of width $dx$ at position $x$ from centre, carrying $n\,dx$ turns; its distance from $P$ is $(r-x)$, so treating it as a single loop of $n\,dx$ turns:
$$dB = \frac{\mu_0\, I\, a^2\, n\, dx}{2\big(a^2+(r-x)^2\big)^{3/2}}$$

**Far-field approximation:** since $r\gg x$ and $r\gg a$, the denominator simplifies to just $r^3$:
$$dB \approx \frac{\mu_0\, n\, I\, a^2}{2 r^3}\,dx$$

**Integrate** over the whole solenoid, $x=-l$ to $x=+l$:
$$B=\int_{-l}^{l} dB = \frac{\mu_0\, n\, I\, a^2}{2r^3}(2l)$$

**Substitute** $n = N/(2l)$ (so the $2l$'s cancel) and multiply/divide by $\pi$ to turn $Ia^2$ into $I(\pi a^2) = I\!\cdot\!(\text{loop area})$, i.e. the magnetic moment $M=NIA=NI\pi a^2$:
$$\boxed{B = \frac{\mu_0}{4\pi}\frac{2M}{r^3}}$$

This is exactly the bar-magnet axial field formula the derivation set out to reproduce (matching NCERT Eq. 5.1) -- so at large axial distances, a current-carrying solenoid of moment $M=NIA$ behaves identically to a bar magnet of the same moment, completing the proof.

---
*Note on this lecture:* the transcript and board frames agree closely throughout -- the derivation completes on the board (boxed final result, `floor_000097.jpg`) right at the very end of the lecture's true duration, matching the transcript's own conclusion at essentially the same point. No delayed-repetition or missing-topic issue was found in this lecture; the automated non-adjacent-duplicate scan flagged only two short, low-length phrase pairs (natural verbal repetition of brief labelling statements), not a genuine content loop.

#### A Dipole in a Uniform Magnetic Field Performs SHM

**NCERT sections covered:** 5.2.3

##### Recap: the spring-mass SHM condition (Class 11 link)
Before proving the magnetic result, the lecture re-derives the spring-mass SHM condition as a template: a spring stretched by $x$ has restoring force $F=-kx$, so $ma=-kx \Rightarrow a=-\dfrac{k}{m}x=-\omega^2x$. Since acceleration is proportional to $-(\text{displacement})$, this is simple harmonic motion, obeying the general equation
$$\frac{d^2x}{dt^2}+\omega^2 x = 0$$
The same logic carries over to *angular* quantities: replacing $x\to\theta$ and $a\to\alpha$ (angular acceleration), if $\alpha\propto-\theta$ then $\dfrac{d^2\theta}{dt^2}+\omega^2\theta=0$ and the angular motion is SHM too. This angular version is what the main derivation below needs.

##### Derivation: a dipole in a uniform field performs SHM (NCERT 5.2.3)
A magnetic dipole (a short bar magnet, moment $\vec M$) is placed in a uniform field $\vec B$, making angle $\theta$ with it. It experiences a **deflecting torque**
$$\vec\tau = \vec M\times \vec B, \qquad \tau = MB\sin\theta$$
By the rotational analogue of Newton's second law ($F=ma \to \tau=I\alpha$, with moment of inertia $I$ in place of mass and angular acceleration $\alpha$ in place of linear acceleration):
$$I\alpha = -MB\sin\theta$$
The minus sign is because the **restoring** torque set up by the field acts opposite to the deflecting displacement -- exactly like $F=-kx$ in the spring case.

For small angular displacement, $\sin\theta\approx\theta$, so
$$I\alpha = -MB\theta \quad\Rightarrow\quad \alpha = -\frac{MB}{I}\theta$$
Since $\alpha\propto-\theta$, this **is** SHM, with
$$\omega^2 = \frac{MB}{I}, \qquad T = 2\pi\sqrt{\frac{I}{MB}} \quad\left(\text{equivalently } B=\frac{4\pi^2 I}{MT^2}\right)$$
This last rearranged form is useful whenever a problem gives the period of oscillation and asks for the unknown field or moment.

##### Worked numerical 1: field from an oscillating magnetic needle
A magnetic needle has moment $M=6.7\times10^{-2}$ A m$^2$ and moment of inertia $I=7.5\times10^{-6}$ kg m$^2$, and completes 10 oscillations in 6.7 s.

**Time period:** $T = \dfrac{6.7}{10} = 0.67$ s.

**Field:** using $B=\dfrac{4\pi^2 I}{MT^2}$,
$$B \approx 0.01~\text{T}$$

##### Worked numerical 2: bar magnet vs. equal-moment solenoid (3 parts)
A short bar magnet, axis at $30^\circ$ to an external field $B=800$ G, experiences torque $\tau=0.016$ N m. First convert the field to SI: $1$ T $=10^4$ G, so $B = 800\times10^{-4}~\text{T} = 0.08$ T.

**(i) Find $M$:** from $\tau = MB\sin\theta$,
$$M = \frac{\tau}{B\sin\theta} = \frac{0.016}{0.08\times\sin30^\circ} = 0.4~\text{A m}^2$$

**(ii) Work done moving the magnet from its most stable to its most unstable position.** Most stable is $\vec M\parallel\vec B$ ($\theta_1=0^\circ$); most unstable is $\vec M$ antiparallel to $\vec B$ ($\theta_2=180^\circ$). Work done against the restoring torque:
$$W = \int_{\theta_1}^{\theta_2}\tau\,d\theta = \int_{\theta_1}^{\theta_2}MB\sin\theta\,d\theta = MB\big[\cos\theta_1-\cos\theta_2\big] = MB\big(1-(-1)\big) = 2MB = 0.064~\text{J}$$

**(iii) Same magnet replaced by a solenoid of the same moment $M$**, with cross-sectional area $A=2\times10^{-4}$ m$^2$ and $N=1000$ turns. From $M=NIA$:
$$I = \frac{M}{NA} = \frac{0.4}{1000\times2\times10^{-4}} = 2~\text{A}$$

---
*Note on this lecture:* part (i) of numerical 2 is confirmed in both transcript and board frames, but the transcript audio track trails off mid-sentence right as parts (ii) and (iii) begin, well before reaching either result -- see the flagged span below. Both results were recovered directly from later board frames (`floor_000048.jpg`, `floor_000053.jpg`) that exist in the frames folder on disk but were dropped from the coverage-floor sampler's deduped `index.json` list (likely misjudged as near-duplicates of the preceding frame by the perceptual-hash dedupe step, since the board changes only incrementally as new lines are added below existing text) -- worth flagging upstream, since it means `index.json` alone is not a reliable guide to what content exists in a lecture's frame folder.

##### Verify these spans
- [14:48–17:33] The transcript trails off mid-sentence at its last segment ('unstable position means unstable position means', ending 1060s) right as the teacher is setting up part (ii) of the second numerical (most-stable-to-most-unstable work done) -- it never reaches the computation of W, nor part (iii) (replacing the bar magnet with a solenoid to find the current). This does not look like the delayed-repeat fabrication loop (no earlier block is re-transcribed) -- it reads like the ASR response simply ran out/was cut short near the true end of the audio. The board-frame coverage-floor sampler's deduped index (index.json) also stops at t=880s (floor_000045), but the raw frames directory retains later, non-deduped frames (floor_000046 through floor_000053) that a direct check confirms DO carry new content -- floor_000048.jpg shows part (ii)'s full work-done derivation (W=2MB=0.064 J) and floor_000053.jpg shows part (iii)'s solenoid current result (I=2 A) freshly added beside it. Both of the two claims above for parts (ii) and (iii) are grounded from these board-only frames, with no transcript corroboration -- the physics is standard and consistent with the board's own part (i) answer and the given N, A, so treated as reliable, but flagged here since it could not be cross-checked against narration.

#### The Earth's Magnetism: Dynamo Effect, Magnetic Axis, and Elements of the Field

##### A note on syllabus scope
**This entire lecture covers material that has been removed from the current (rationalised, 2022-23 onward) NCERT Class 12 Physics syllabus.** The current NCERT Chapter 5 raw text jumps directly from Section 5.3 (Magnetism and Gauss's Law) to Section 5.4 (Magnetisation and Magnetic Intensity), with no "Earth's Magnetism" section at all -- in the pre-rationalisation NCERT this was Section 5.4, covering exactly the dynamo-effect theory, magnetic vs. geographic axis, and the three elements (declination, dip, horizontal component) taught in this lecture. Every claim below is therefore given `ncert_section=None` rather than forced onto a current-syllabus number; nothing here should be treated as CBSE-examinable under the present syllabus, though it remains standard, correct physics and is commonly retained in classroom teaching for conceptual completeness (and because some boards/older question banks still reference it).

##### Why the earth behaves as a magnet: the dynamo effect
Two historical explanations are contrasted. A "huge bar magnet buried inside the earth" is ruled out, since the core's temperature is far above any material's Curie point -- a permanent magnet simply could not survive there. The accepted picture instead is the **dynamo effect**: the earth's core contains molten iron and nickel existing as mobile ions; their large-scale motion constitutes electric currents, and a moving charge always produces a magnetic field -- this circulating current system is the real source of the earth's magnetism.

##### Magnetic axis vs. geographic axis
Treating the earth as though it contains an internal short bar magnet, its **magnetic axis** (through the magnetic N/S poles) is tilted at **11.3°** to the **geographic axis** (the earth's rotation axis, through the true/geographic N/S poles). Since a freely suspended compass needle's own north pole always swings toward geographic north (opposite poles attract), the pole of the earth's "internal magnet" lying near geographic north must, strictly, be a south pole -- but by long-standing convention it is still labelled the earth's "magnetic north pole."

**Field-line direction examples:** with field lines running (loosely) from geographic south to geographic north outside the earth,
- at a place near the geographic south (e.g. **Australia**), field lines appear to emerge **out of** the ground;
- at a place near the geographic north (e.g. **Britain**), field lines appear to go **into** the ground.

##### Geographic vs. magnetic: axis, equator, meridian
| Geographic | Magnetic |
|---|---|
| **Axis:** line through geographic N & S poles (earth's rotation axis) | **Axis:** line through magnetic N & S poles |
| **Equator:** great circle perpendicular to the geographic axis | **Equator:** great circle perpendicular to the magnetic axis |
| **Meridian:** vertical plane containing the geographic axis at a place | **Meridian:** vertical plane containing the magnetic axis at a place |

At any given place, the geographic meridian and magnetic meridian planes generally differ by some angle -- which is precisely the first "element" of earth's magnetic field, below.

##### The three elements of earth's magnetic field
These three quantities together completely specify the earth's magnetic field (magnitude and direction) at any place:

**1. Angle of declination ($\alpha$):** the angle at a place between the magnetic meridian and the geographic meridian. Knowing $\alpha$ tells you exactly where the magnetic meridian lies relative to true north.

**2. Angle of dip / magnetic inclination ($\delta$):** the angle at a place, measured within the magnetic meridian plane, between the earth's total field $\vec B$ and the horizontal. It is measured using a **dip circle**.

**3. Horizontal component ($B_H$):** the component of the earth's total field lying in the horizontal plane (within the magnetic meridian). Resolving $\vec B$ using the dip angle $\delta$:
$$B_H = B\cos\delta, \qquad B_V = B\sin\delta, \qquad B=\sqrt{B_V^2+B_H^2}, \qquad \tan\delta=\frac{B_V}{B_H}$$

**Special cases:**
- **At the magnetic equator:** $\delta=0^\circ$, so $B_V=0$ and $B=B_H$ -- the field is entirely horizontal.
- **At the magnetic poles:** $\delta=90^\circ$, so $B_H=B\cos 90^\circ=0$ and $B_V=B$ -- the field is entirely vertical. A compass needle, which normally settles by rotating in the horizontal plane to align with $B_H$, has no horizontal field to align with at the poles and so points in an arbitrary horizontal direction there.

---
*Note on this lecture:* the transcript covers the dynamo effect, the magnetic-vs-geographic axis/equator/meridian geometry, and element 1 (declination) cleanly and in full, matching the board closely throughout. However, the transcript's audio track runs out right as element 2 (angle of dip) is first named, and never reaches its definition or element 3 (horizontal component) at all -- see the flagged span below. Both were recovered from later board frames that exist in the frames folder on disk but, as in lecture 2 of this chapter, were dropped from the coverage-floor sampler's deduped `index.json` (last indexed frame stops at t=1200s, 177s before the lecture's true end at 1377.1s) -- the same upstream dedupe-drops-real-tail-content issue found there.

##### Verify these spans
- [22:49–22:57] The transcript's last segment (index 92, 1369.5-1405.7s) only NAMES 'angle of dip, also known as magnetic inclination' and then stops entirely -- it never defines the term, never introduces the horizontal component (the 3rd of the '3 elements' the teacher explicitly enumerates at segment 78), and never derives the B_H/B_V/tan(delta) relations or the equator/pole special cases. This does not look like the delayed-repeat fabrication loop (nothing upstream is re-transcribed) -- it reads as the ASR response simply running out near the true end of the audio, similar to lecture 2 in this chapter. The coverage-floor sampler's deduped index.json also stops at t=1200s (floor_000061), but as in lecture 2, the raw frames folder retains later non-deduped frames (up to floor_000069, confirmed to exist and checked directly) that show the angle-of-dip definition fully written out plus the entire horizontal-component derivation with all four equations and both special-case results -- this is a real, temporally progressive board build-up (declination alone at t~860s and t~1140s, dip's definition text complete by the 65th raw frame, horizontal-component equations and special cases added afterward at the 66th-69th raw frames), not an isolated out-of-place frame. Both element-2 and element-3 claims above are grounded from these board-only frames, with no transcript corroboration at all -- flagged here since narration could not confirm them, though the content is standard and consistent with the board's own stated 3-element structure.

#### Earth's Magnetism Numericals, Null Point Problems, and the Atom as a Magnetic Dipole

##### Earth's magnetism: worked numericals

**Not present in the current rationalised NCERT syllabus** for this chapter -- checking the extracted textbook text (`data/ncert/raw/leph105.txt`), Chapter 5 "Magnetism and Matter" runs 5.1 Introduction, 5.2 The Bar Magnet, 5.3 Magnetism and Gauss's Law, 5.4 Magnetisation and Magnetic Intensity, 5.5 Magnetic Properties of Materials -- there is no Earth's-magnetism section at all (the pre-rationalisation NCERT's Earth's magnetism sub-chapter, including angle of dip/declination and null-point problems, was removed). This content is covered here as extra material the teacher chose to include, not because it is examinable under the current syllabus.

Using $B_H = B\cos\delta$ and $B_V=B\sin\delta$ ($\delta$ = angle of dip):
- Given $B_H$ and $\delta$: $B = B_H/\cos\delta$ (e.g. $B_H=0.35$ gauss, $\delta=22°$ $\Rightarrow B=0.35/0.92$).
- Given $B_H, B_V$: $\tan\delta = B_V/B_H$, then solve for $B$.
- **Full 3-D direction of $\vec B$:** first locate the *magnetic meridian* using the angle of **declination** (between geographic and magnetic meridian), then specify the angle within that vertical plane using the angle of **dip**.

##### Null point problems

A null point is where a bar magnet's field exactly cancels Earth's horizontal field $B_H$. Its location depends on the magnet's orientation:
- **North pole toward geographic south:** null points lie on the magnet's **axial** line. $\left(\dfrac{\mu_0}{4\pi}\dfrac{2M}{d^3}=B_H\right)$
- **North pole toward geographic north:** null points lie on the **equatorial** line instead. $\left(\dfrac{\mu_0}{4\pi}\dfrac{M}{d^3}=B_H\right)$

Worked examples solve for the null-point distance (e.g. $14$ cm axial, $11.1$ cm equatorial in two separate problems), including a variant asking for the *new* null-point location after the magnet is turned $180°$ (which swaps axial $\leftrightarrow$ equatorial per the rule above).

##### The atom as a magnetic dipole

**Also not present in the current rationalised NCERT syllabus** for this chapter (no section derives an atomic/orbital magnetic moment or the Bohr magneton) -- again extra material beyond the current textbook, included here for completeness since it was taught.

Every atom behaves as a tiny magnet: an orbiting electron is a tiny current loop (**orbital** magnetic moment); electron spin contributes a **spin** magnetic moment too (about double the orbital contribution for the same angular momentum, per this lecture). **Direction:** curl the right hand's fingers in the direction of *conventional current* (opposite the electron's actual motion) — thumb gives the direction of $\vec M$, pointing from the loop's south to north face.

###### Orbital magnetic moment derivation
Electron (charge $e$, angular speed $\omega$) in a circular orbit radius $r$: equivalent current $I=e/T=e\omega/2\pi$, loop area $A=\pi r^2$:
$$M = IA = \frac{e\omega}{2\pi}\cdot\pi r^2 = \frac{1}{2}e\omega r^2$$

###### Connecting to Bohr's theory
Angular momentum is quantised: $mvr = \dfrac{nh}{2\pi}$. Using $v=r\omega$: $mr^2\omega = \dfrac{nh}{2\pi}$. Substituting:
$$M = \frac{neh}{4\pi m}$$
For $n=1$ (ground state), this defines the **Bohr magneton**:
$$\boxed{M = \frac{eh}{4\pi m} = \mu_B = 9.27\times10^{-24}~\text{A}\cdot\text{m}^2}$$

###### Alternative form via angular momentum
Since $L = \vec r\times\vec p = mvr = mr^2\omega$, the same result rewrites as:
$$\boxed{M = \frac{e}{2m}L}, \qquad \vec M = -\frac{e}{2m}\vec L~\text{(electron's negative charge flips the direction)}$$
$e/2m$ is the **gyromagnetic ratio** — magnetic moment is directly proportional to angular momentum.

##### Verify these spans
- [36:40–39:38] The transcript's real narration follows the Bohr-quantisation derivation closely and reaches M = (1/2)e * (nh/2*pi*m) as its very last segment, essentially arriving at the Bohr magneton result but never simplifying it to the named 'Bohr magneton' with its numerical value, and never mentioning the alternative angular-momentum form M=(e/2m)L or the gyromagnetic ratio at all. A board frame (floor_000116.jpg, t=2300s, within the transcript's own covered time range) shows both of these already written out: the boxed 'for n=1, M=eh/4*pi*m=mu_B=Bohr magneton' with its value 9.27e-24 A.m^2, and a separate derivation via L=r x p leading to M=(e/2m)L (vector form with a minus sign for the electron) plus a right-hand-rule statement for the direction of M. The Bohr-magneton-value and angular-momentum-form claims above are grounded from this frame rather than the transcript's own words.

#### Magnetizing Intensity, Intensity of Magnetization, Permeability, and Susceptibility

**NCERT sections covered:** 5.4

##### Magnetizing intensity, intensity of magnetization, and permeability (NCERT 5.4)

**Magnetizing intensity $H$:** from the solenoid result $B_0=\mu_0 nI$, the quantity $nI$ (turns/length $\times$ current), independent of any material, is called $H$. So $B_0=\mu_0 H$ for an air/vacuum core, or generally $B=\mu H$ with a material core. SI unit: A/m.

**Intensity of magnetization $I$ (or $M$):** a vector, defined as magnetic moment per unit volume of a material placed in the magnetizing field — the material's atomic dipoles align with the field:
$$I = \frac{m}{V}$$
Same SI unit as $H$ (A/m), despite representing a different physical quantity (external coil/current setup vs. the material's own response).

**Magnetic permeability $\mu$:** quantifies how readily a magnetic field can penetrate a material (e.g. an iron bar between magnet poles draws field lines through it far more than air would). $\mu = B/H$. SI units: T$\cdot$m$\cdot$A$^{-1}$ (equivalently Wb$\cdot$m$^{-1}\cdot$A$^{-1}$).

###### Relation between permeability and susceptibility
Total field $B = B_0+B_m = \mu_0 H + \mu_0 I$ (the material's own contribution $B_m=\mu_0 I$ adds to the bare $\mu_0 H$). **Magnetic susceptibility** $\chi_m = I/H$, so $I=\chi_m H$:
$$B = \mu_0 H(1+\chi_m)$$
Comparing with $B=\mu H$:
$$\boxed{\mu = \mu_0(1+\chi_m)}, \qquad \mu_r = \frac{\mu}{\mu_0} = 1+\chi_m$$

###### Worked numericals
- **Rowland ring:** mean radius $15$ cm, $3500$ turns on a ferromagnetic core ($\mu_r=800$), current $1.2$ A. $n=N/2\pi r$, $B=\mu_0\mu_r nI = 4.48$ T.
- **Steel magnet:** $M=2.5$ A$\cdot$m$^2$, mass $6.6$ g, density $7.9\times10^3$ kg/m$^3$. Find $I$: get volume from mass/density, then $I=M/V$.
- **Iron rod:** cross-section $0.2$ cm$^2$, $H=1200$ A/m, $\chi_m=599$. Find $\mu$ and flux $\phi$: $\mu_r=1+\chi_m=600$, $\mu=\mu_0(1+\chi_m)=7.536\times10^{-4}$ T$\cdot$m$\cdot$A$^{-1}$; then $\phi=BA$ with $B=\mu H$.

---
*Note on this lecture's transcript:* the susceptibility relation and all three worked numericals above are grounded entirely from board frames -- the transcript itself never mentions susceptibility at all, instead getting stuck repeating the permeability and magnetization definitions several times over. See the flagged span below.

##### Verify these spans
- [07:32–23:52] This is one of the most severely corrupted transcripts found in this project: after cleanly covering magnetizing intensity H and intensity of magnetization I, the transcript's narration of 'magnetic permeability' repeats itself at least four to five times over (near-identical short phrases like 'to which magnetic field can penetrate a material' and 'mu is equal to B upon H' recur at t=452s, 623s, 814s, 997s, and 1129s), then the 'intensity of magnetization' definition is re-transcribed a second time (t=1160-1420s) nearly verbatim from its first pass (t=194-445s) -- all classic delayed-repetition artifacts. Crucially, the transcript NEVER once mentions magnetic susceptibility, despite board frames showing it is thoroughly covered: floor_000047.jpg (t=920s) shows the full permeability-susceptibility relation derivation (chi_m=I/H, mu=mu0(1+chi_m)); floor_000050.jpg through floor_000060.jpg (t=980-1180s) show a complete Rowland-ring numerical; and floor_000060.jpg through floor_000069.jpg (t=1180-1360s) show a magnet intensity-of-magnetization numerical and an iron-rod susceptibility numerical, both fully worked. Roughly the back half of this lecture (everything from the susceptibility relation onward) is grounded entirely from these frames.

#### Diamagnetic and Paramagnetic Substances, and Curie's Law

**NCERT sections covered:** 5.5

##### Diamagnetic, paramagnetic, and (introduced) ferromagnetic substances (NCERT 5.5)

###### Diamagnetic substances
When placed in an external magnetic field, diamagnetic substances get feebly magnetized in the direction **opposite** to the magnetizing field (repelled by a magnet). Examples: Bi, Cu, Sb, Pb, Au, Ag, H$_2$O.

**Explanation:** each atom acts as a magnetic dipole (orbiting electrons contribute dipole moments). In a diamagnetic substance the electrons are *paired* — one clockwise, one anticlockwise — so their dipole moments cancel: $M_\text{net}=0$ with no field. When a field $\vec B$ is applied, the perturbed electron motion gives each atom a net dipole moment **opposite** to $\vec B$.

**Properties:**
1. They move from the **stronger** to the **weaker** part of an external field.
2. When placed in a field, they **expel field lines**: $B<B_0 \Rightarrow \mu<\mu_0 \Rightarrow \mu_r<1$. **Superconductors** are the most extreme (exotic) diamagnets — no field lines pass through at all, $\mu_r=0 \Rightarrow \chi_m=-1$ (from $\mu_r=1+\chi_m$).
3. They are **independent of temperature** — since each diamagnetic molecule is not itself a magnetic dipole, random thermal motion doesn't affect the (induced) magnetization.
4. Freely suspended in a uniform field, they align with their **longest axis perpendicular to $B$** (the minimum-energy orientation, since the material "wants" to expel field lines).

###### Paramagnetic substances
When placed in an external field, paramagnetic substances get feebly magnetized in the **same** direction as $B$ (feebly attracted). Examples: Al, Cr, Li, Mg, Na, K.

**Explanation:** unlike diamagnetic substances, paramagnetic atoms have *unpaired* electrons, so each atom already has a permanent magnetic dipole moment. With no field, thermal motion randomises these — $M_\text{net}=0$. In a field $\vec B$, the dipoles align with $\vec B$, giving $M_\text{net}\ne0$.

**Properties** (opposite of the diamagnetic case):
1. They move from the **weaker** to the **stronger** part of an external field.
2. Field lines **prefer to pass through** them (rather than being expelled).

###### Curie's law
$$I \propto B, \qquad I\propto\frac{1}{T} \quad\Rightarrow\quad I\propto\frac{B}{T}$$
Using $B=\mu H$: $I\propto H/T$, so $I/H \propto 1/T$. Since susceptibility $\chi_m = I/H$:
$$\boxed{\chi_m = \frac{C}{T}}$$
where $C$ is the **Curie constant** — magnetic susceptibility of a paramagnetic material is inversely proportional to absolute temperature.

**Graphs:** $1/\chi_m$ vs. $T$ is a straight line through the origin (slope $1/C$); $I$ vs. $H$ at fixed $T$ is also a straight line through the origin.

---
*Note on this lecture's transcript:* two whole properties sections — diamagnetic property 3 (temperature-independence) and paramagnetic properties 1–2 (weaker→stronger field, field lines preferring to pass through) — are visible on the board but never spoken in the transcript at all, a total-omission gap rather than a timestamp gap. A third graph (I vs. H/T, showing **saturation magnetization** — the real departure from Curie's law at high field/low temperature) is drawn on the board just past where the transcript's own narration stops. All three are grounded from frames alone; see the flagged spans below.

##### Verify these spans
- [18:44–20:00] A third property of diamagnetic substances -- 'they are independent of temperature, since (unlike a paramagnetic atom) each diamagnetic molecule is not a magnetic dipole in itself, so random thermal motion of molecules does not affect their magnetization' -- appears clearly on the board (floor_000059.jpg, t=1160s, squarely inside the transcript's own covered timespan 1105-1234s) but is never spoken in the transcript at all: the transcript jumps from discussing superconductors/chi_m=-1 (ending ~1124-1136s) directly to property 4 (alignment perpendicular to B, starting ~1200s) with no trace of this temperature-independence property in between. This claim is grounded entirely from the frame.
- [28:10–30:25] Two properties of paramagnetic substances, directly parallel to (and the opposite of) the diamagnetic properties covered earlier in this same lecture -- (1) they move from the WEAKER to the STRONGER part of an external magnetic field, and (2) field lines prefer to pass through them (rather than being expelled) -- appear clearly on the board (floor_000087.jpg, t=1720s, inside the transcript's covered span 1690-1825s) but are never spoken: the transcript goes directly from 'M net will not be equal to zero' to 'individual atoms of a paramagnetic substance possess permanent magnetic dipole moment... thus M net is equal to zero... curie's law', skipping this properties section entirely.
- [35:47–37:45] The transcript's own narration, in its final segments, describes only two graphs following from Curie's law: 1/chi_m vs T, and I vs H (both straight lines through the origin). A later board frame (floor_000110.jpg, t=2180s, still within the transcript's nominal duration) shows a THIRD graph drawn after the first two: I vs H/T, which rises and then flattens out, explicitly labelled 'saturation magnetization' -- this shows that at sufficiently high field / low temperature, a real paramagnetic material's magnetization saturates rather than continuing to grow linearly as Curie's law (I proportional to H/T) would predict. The transcript's final segment (ending 2301s, itself slightly past the video's measured duration) never reaches this third graph or the word 'saturation' at all, so this content is grounded entirely from the frame and is not independently confirmed by the transcript's own words.

#### Ferromagnetic Substances and Domain Theory

**NCERT sections covered:** 5.5

##### Ferromagnetic substances and domain theory (NCERT 5.5)

**Ferromagnetic substances** get **strongly** magnetized in the direction of an external field (contrast: paramagnetic substances are only feebly magnetized). Examples: iron, cobalt, nickel, and the alloy **Alnico** (Al, Ni, Co, Fe, and some Cu).

###### Domain theory
Each atom has a magnetic dipole moment (as in a paramagnetic substance), but here neighbouring atomic dipoles **interact strongly** and spontaneously align in a common direction over a macroscopic volume called a **domain**. Each domain has its own net dipole moment, but domain directions vary randomly across the sample, so the substance's overall $M_\text{net}=0$ when $B=0$. (This is the key structural difference from paramagnetic substances, which don't form domains at all — there, each individual *atom* is independently randomly oriented.)

When placed in an external field $\vec B$: the domains themselves **orient toward $\vec B$ and grow** — domain boundaries shift so smaller domains merge into bigger ones, approaching one giant domain aligned with $B$. With the domains now aligned, $M_\text{net}\ne0$: the substance behaves as a magnet.

###### Worked numerical (Curie's law, paramagnetic salt)
*(NCERT exercise, pre-rationalisation numbering 5.13)*

A paramagnetic salt has $2\times10^{24}$ dipoles, each of moment $1.5\times10^{-23}$ J/T. Placed in $B_1=0.64$ T, cooled to $T_1=4.2$ K, it reaches $15\%$ magnetic saturation. Find the total dipole moment at $B_2=0.98$ T, $T_2=2.8$ K (assume Curie's law).

- Fully-saturated total moment: $(2\times10^{24})(1.5\times10^{-23}) = 30$ J/T
- At $15\%$ saturation: $M_1 = 0.15\times30 = 4.5$ J/T
- By Curie's law ($M\propto B/T$): $M_2 = M_1\times\dfrac{B_2}{B_1}\times\dfrac{T_1}{T_2}$

---
*Note on this lecture's transcript:* the domain-theory explanation above is transcribed correctly on its first pass, but the ASR then re-transcribes the *same* explanation nearly verbatim four more times back-to-back, filling almost the entire second half of the lecture. Board frames show that, during this same stretch, the teacher had actually moved on to the worked Curie's-law numerical above — none of which made it into the transcript's own words. The numerical is grounded entirely from frames; see the flagged span below.

##### Verify these spans
- [06:41–25:51] This transcript has a severe, repeated delayed-repetition problem: the same ~230-word domain-theory explanation ('this domain theory... individual atoms possess dipole moment... they interact... align... called domain... each domain has net M but it varies domain to domain... M net of whole substance is zero... place in external field... domains orient... grow... form giant domain...') is transcribed essentially verbatim FIVE separate times, at approximately t=91-399s (first, genuine pass, matching the board diagrams in floor_000019.jpg), then re-transcribed nearly word-for-word again at t=625-916s, t=918-1143s, t=1129-1371s (this one partially overlapping/out-of-order with the previous), and t=1396-1560s. Only the first pass reflects new content; the other four are ASR hallucinated repeats that silently displaced whatever the teacher actually said during those stretches. Board frames confirm real new content WAS being taught during this displaced time: from floor_000061.jpg (t=1200s) onward, the board shows a full worked Curie's-law numerical (a paramagnetic-salt problem, apparently NCERT exercise 5.13 in the pre-rationalisation numbering) being written and solved, continuing through the last available frame (floor_000074.jpg, t=1460s) -- none of which appears anywhere in the transcript's own words. The numerical is grounded entirely from these frames; the method for the final step (M2 via Curie's law ratio) is the direct, expected completion of the givens shown, but the frames do not show a final computed value for M2, so none is stated here.

#### Hysteresis Curve: Retentivity, Coercivity, and Soft Iron vs. Steel

**NCERT sections covered:** 5.5

##### The hysteresis curve (NCERT 5.5)

A solenoid carries current $I$ with an iron rod (magnetizing material) inside. The **hysteresis curve** plots $B$ (total field inside the material — related to how many of its dipoles are aligned) against $H$ (related to the coil current).

**Tracing the loop:**
- **O:** initially $B=0$, $H=0$ (no current).
- **O$\to$A:** current increased $\Rightarrow$ $H$ increases $\Rightarrow$ $B$ increases (domains align with $B$). At **A**, $B$ stops increasing however much $H$ increases further — this is the **saturation point** (all domains now aligned).
- **A$\to$B:** current (and $H$) decreased back toward zero — but $B$ does *not* retrace the same path. When $H=0$, $B$ is still non-zero: $OB$ is the **retentivity** (residual magnetism) — the material stays magnetized after the current is switched off.
- **B$\to$C:** to bring $B$ back to zero, the current must be **reversed** and increased. Where $B=0$ (with $H\ne0$, reversed) is point $C$: $OC$ is the **coercivity** — the reverse field needed to fully demagnetize. Larger coercivity $\Rightarrow$ harder to demagnetize.
- **C$\to$D$\to$...$\to$A:** increasing the reversed current further reaches negative saturation at $D$; repeating the same steps in the forward direction (through $E$, $F$) closes the loop back at $A$.

**Hysteresis:** the phenomenon of $B$ *lagging behind* $H$ when a magnetic specimen is taken through a cycle of magnetisation. The closed $B$–$H$ curve traced is the **hysteresis loop**.

**Area of the loop** = energy dissipated per unit volume, per cycle (the substance heats up) — the bigger the loop, the greater the dissipation.

##### Soft iron vs. steel

Comparing their hysteresis loops (steel's is visibly wider):
1. Retentivity: **steel < soft iron**
2. Coercivity: **steel > soft iron** $\Rightarrow$ steel is used for **permanent magnets** (harder to demagnetize)
3. Loop area: **steel > soft iron** $\Rightarrow$ hysteresis loss in soft iron is **less** $\Rightarrow$ soft iron is used in **electromagnets** (repeatedly (de)magnetized, so low loss matters)

###### Making a permanent magnet
1. Hold an iron/steel rod in the N–S direction and hammer it repeatedly.
2. Hold a steel rod and stroke it repeatedly (many times), always in the same sense, with one end of a bar magnet.

---
*Note on this lecture's transcript:* the loop-construction explanation (saturation, retentivity, coercivity) is transcribed correctly once, then repeated nearly verbatim a second time -- inflating the transcript's own timestamps past the video's true duration. The final soft-iron-vs-steel comparison and the two permanent-magnet methods are visible in full on the board but never make it into the transcript's own words at all (it cuts off announcing the topic). Both are grounded entirely from frames; see the flagged spans below.

##### Verify these spans
- [03:53–17:40] The full explanation of the hysteresis curve's construction (saturation at A, decreasing H giving retentivity at B, reversing current to reach coercivity at C, the fourth/fifth steps) is transcribed once correctly (~t=233-660s) and then transcribed a SECOND time nearly verbatim (~t=692-1015s) -- the same delayed-repetition pattern found repeatedly in this chapter's lectures. This inflated the transcript's own self-reported timestamps: its last segment claims to end at 1724.84s even though the video's true duration is only 1661.0s, confirming the internal duplication pushed later timestamps out of sync with real video time. Content-wise nothing appears lost here (the two passes say the same thing), but the timestamps attached to claims in the back half of this note should be read as approximate.
- [26:46–27:41] The transcript's own words announce the final topic twice ('Now we have hysteresis curve for soft iron and steel', repeated) and then cut off mid-sentence while just starting to draw a B-H curve ('I have a curve something like this... A curve main aise draw kar rahi hoon'), giving the impression the lecture ends before this comparison is actually taught. However, a board frame (floor_000067.jpg) -- whose own true video timestamp (t=1320s) falls chronologically BEFORE this final transcript segment's self-reported (drifted, see the span above) timestamp -- shows the soft-iron-vs-steel comparison already fully written out: three comparison properties (retentivity, coercivity, loop area/hysteresis loss) plus two practical methods for making a permanent magnet. This confirms the teacher did complete this topic on the board within the true 1661s runtime; the transcript simply never captured the spoken explanation of it. All of the soft-iron/steel and permanent-magnet content in this note is grounded entirely from that frame, not from the transcript's own words.

### Chapter 6 · Electromagnetic Induction — lecture notes

#### Faraday and Henry's Experiments, Magnetic Flux, Faraday's Law

**NCERT sections covered:** 6.1, 6.2, 6.3, 6.4

##### Motivation and setup (NCERT 6.1)
Oersted and Ampere had already shown that a moving charge (current) produces a magnetic field. Faraday and Henry's ~1830 experiments asked the converse question: can a magnetic field produce a current? The chapter's answer is yes -- **electromagnetic induction**.

##### Magnetic flux (NCERT 6.3)
For a plane area $A$ sitting in a uniform field $\vec B$, with the area's normal at angle $\theta$ to $\vec B$:
$$\Phi_B = \vec A \cdot \vec B = BA\cos\theta$$
$\Phi_B$ is a **scalar**. SI unit: **weber** (Wb); since $\Phi_B = BA$, $\text{Wb} = \text{T}\cdot\text{m}^2$.

**Dimensional formula (board derivation, exam-technique aside, not itself an NCERT-numbered result):** using $B = \tau/(IA)$ from $\tau = MB\sin\theta$ (with $M=IA$), and $\tau$ in N·m:
$$[\Phi_B] = [M][A] = \left[\frac{N\cdot m}{A\cdot m^2}\right][m^2] = [M^1 L^2 T^{-2} A^{-1}]$$
(A short board loop repeats this sub-derivation once before continuing -- see flagged span below; it doesn't affect the final result.)

**Magnetic flux density:** $B = \Phi_B/A$, so $B$ can equivalently be expressed in Wb/m$^2$ as well as tesla.

##### Faraday and Henry's experiments (NCERT 6.2)
Three experiments, each showing current is induced in a coil connected to a galvanometer (no battery in the coil circuit itself):

**Experiment 1.** A bar magnet is moved towards, then away from, a coil $C$ wired to a galvanometer $G$. A deflection appears only *while the magnet is moving* -- faster motion gives a larger deflection -- and the deflection reverses direction when the motion (or the facing pole) reverses. A stationary magnet, however close, gives zero deflection.

**Experiment 2.** The bar magnet is replaced by a second coil $C_2$ carrying a steady current from a battery (so $C_2$ itself has a magnetic field and plays the magnet's role). Moving $C_2$ towards/away from $C_1$ (or vice versa) reproduces exactly the same deflection behaviour as Experiment 1. This shows relative motion between the flux source and the coil is what matters, not that the source specifically be a permanent magnet.

**Experiment 3.** Both coils are now held **stationary**. $C_1$ is wired to a battery through a key $K$; $C_2$ to the galvanometer. Closing the key produces a brief deflection that decays to zero once the current in $C_1$ becomes steady; opening the key produces a brief deflection in the *opposite* direction. Inserting an iron rod through the coils strengthens the effect (it strengthens the coupling field).

**What ties the three together:** in every case, current is induced only when the magnetic flux linked with the coil is *changing* -- via relative motion in Experiments 1-2, or via the current (and hence field) switching on/off/settling in Experiment 3. A coil sitting in any steady flux, however large, shows no induced current.

##### Faraday's Law of electromagnetic induction (NCERT 6.4)
*(Grounded from board frames -- see the flagged span below for what the transcript does instead over this stretch.)*

**First law (qualitative):** whenever the magnetic flux linked with a coil changes, an emf is induced in it.

**Second law (quantitative), as boarded:** the induced emf's magnitude is directly proportional to the rate of change of flux linkage:
$$|\varepsilon| = N\frac{d\Phi_B}{dt} \approx N\frac{\Delta\Phi_B}{\Delta t}, \qquad I = \frac{\varepsilon}{R} = \frac{N}{R}\frac{d\Phi_B}{dt}$$
This lecture boards the **magnitude-only** form -- NCERT's Eq. 6.4 carries a minus sign, $\varepsilon = -N\,d\Phi_B/dt$, whose direction is Lenz's law; that sign/direction is explicitly deferred to the next lecture ("#2 Lenz law and motional emf"), so treat this as the teacher intentionally splitting magnitude from direction across two lectures rather than a factual gap.

**Worked example 1 (board only):** flux through a 500-turn coil falls from $0.8$ Wb to $0$ in $0.02$ s.
$$|\varepsilon| = N\frac{d\Phi}{dt} = 500\times\frac{0-0.8}{0.02} = 20{,}000~\text{V} = 20~\text{kV}$$

**Worked example 2 (board only, unfinished at the recording's end):** a 100-turn coil of area $0.1~\text{m}^2$ sits in a field growing from $0$ to $4\times10^{-3}$ Wb/m$^2$ over $4$ s, after which the coil is reversed through $180°$.
$$\Phi_1 = BA\cos 0° = BA, \qquad \Phi_2 = BA\cos 180° = -BA, \qquad \Delta\Phi = \Phi_2-\Phi_1 = -2BA$$
The board was mid-substitution ($|\varepsilon| = 2BA/t = 2\times(4\times10^{-3})/\ldots$) when the frame set ends, so the final numeric answer isn't recoverable from the available material.

---
*Note on this lecture's transcript:* the ASR transcript covers Experiments 1-3 and the flux/dimensional-analysis material solidly, corroborated closely by the board. But it never reaches Faraday's Law by name, never states the quantitative $N\,d\Phi/dt$ form, and never transcribes either worked numerical -- even though all of that is written on the board well inside the verified 1386.6s duration, and is exactly the "...and law" this lecture's own filename promises. See the flagged span below for the full timeline and why the automated coverage/repetition checks didn't catch it.

##### Verify these spans
- [04:43–05:46] Minor delayed-duplicate: the flagged pair-scan catches segments 22-26 (283.9-312.8s, 'torque is MB sin(theta)... B = tau/M... M=IA...') repeated almost verbatim as segments 27-32 (313.3-346.7s), separated by no true new content in between. Unlike the severe cases found elsewhere in this chapter, this one does NOT swallow any missing material -- the dimensional derivation resumes correctly right after (segment 33, 'so this will cancel out') and completes normally by t=433.8s, matching the board (floor_000018-000019). Left un-grounded rather than double-counted as a claim.
- [18:00–23:06] The lecture's own promised final topic ('...and law') -- Faraday's Second Law in quantitative form and both worked numericals -- is missing from the ASR transcript entirely, despite being fully present on the board and on schedule well within the verified duration (1386.6s). Board timeline: floor_000055 (t=1080s) is the first frame showing a 'Faraday's law of em induction' heading with the qualitative first law; floor_000057 (t=1120s) shows the complete quantitative second law (|eps|=N dPhi/dt, I=eps/R) on a fresh page; floor_000059 (t=1160s) already has the first worked numerical's question written ('coil of 500 turns varies...'); floor_000063/000065 (t=1240-1280s) show it fully solved (20 kV); floor_000067/000069 (t=1320-1360s) show a second numerical (100 turns, 0.1 m^2, field reversed through 180 degrees) set up and half-solved, right where the frame set ends (only 26.6s of true runtime remains after the last extracted frame). The transcript, however, over this same interval (segments 75-92, t=998.4-1400.9s) stays on a qualitative re-explanation of experiments 1-3 and 'change in flux causes current' (itself somewhat repetitive across segments 83-91, though not an exact loop) and never once contains the words 'law', 'emf', 'proportional', '500', or 'turns'. Automated checks do not catch this: coverage_ratio is 1.010 (comfortably 'passed'), and check_coverage/sanitize_segments report repetition_detected=False, because the transcript's final ~400s is a paraphrase of earlier ground rather than a verbatim repeat of adjacent segments. The second-law equation, both worked numericals, and the phrase 'Faraday's law' itself are grounded from board frames alone in this note.

#### Lenz's Law and Motional EMF

**NCERT sections covered:** 6.4, 6.5, 6.6

##### Recap: Faraday's law gives magnitude only (NCERT 6.4)
$$|\varepsilon| = N\frac{d\Phi_B}{dt}$$
This tells you *how much* emf is induced, but not its *direction* -- for that, we need **Lenz's law**.

##### Lenz's Law (NCERT 6.5)
**Statement:** the direction of an induced emf (and the current it drives) is always such that it **opposes the cause that produces it**.

**Why -- derived from energy conservation, not asserted:** bring the north pole of a magnet towards a coil.
- *Suppose* the coil's near face became a **south** pole. South attracts north, so the coil would pull the magnet in on its own, with **no work done by you** -- yet a current (energy) would appear. That is a free lunch, forbidden by conservation of energy.
- So the near face **must** become **north** instead. You now have to do mechanical work pushing the magnet in *against* this repulsion -- and it is exactly that mechanical work which converts into the induced electrical energy.

Run the same argument with the magnet being *withdrawn*: the near face must become attractive (opposite pole), so you do work pulling it away against attraction -- which is also why the induced current reverses direction between approach and withdrawal (matching Experiment 1 from Lecture 1). **Lenz's law is thus a restatement of conservation of energy**, and the minus sign in $\varepsilon = -N\,d\Phi_B/dt$ (restored explicitly later this lecture) is its mathematical signature.

###### Worked Lenz's-law problems (direction-finding practice)
The board works through several loop-crossing-a-field-boundary problems using the right-hand rule (curl fingers along the trial current, thumb gives the field that current would create; the real current must be whichever direction makes that field **oppose** the actual flux change):
- A triangular loop $ABC$ dragged through a field region into the page: **anti-clockwise** while entering (opposing increasing flux), **no current** while fully inside and flux is momentarily steady, **clockwise** while leaving (opposing decreasing flux).
- The same technique repeated for circular and square loops crossing a field boundary.
- A straight current-carrying wire next to a small coil: coil current is clockwise when the wire's current (and hence its field) is increasing.
- A coil approaching a bar magnet's field region, solved by the pole-facing method.

*(These worked examples are grounded from board frames -- see the flagged spans below for why the transcript is not a reliable source for this material.)*

##### Motional EMF (NCERT 6.6)
**Setup:** since $\Phi_B = BA\cos\theta$, emf can be induced by changing $B$, changing $A$, or changing $\theta$. Changing $B$ is the Faraday/Lenz case just covered; changing the **area** is new and gives **motional emf**.

**Derivation (flux rule).** A conducting rod $ab$ of length $l$ slides with velocity $v$ along rails, in a uniform field $B$ into the page. In time $dt$ it sweeps extra area $dA = l\,dx$:
$$d\Phi_B = B\,dA = B\,l\,dx \quad\Rightarrow\quad \varepsilon = -\frac{d\Phi_B}{dt} = -Bl\frac{dx}{dt} = -Blv$$
Because the emf here comes from the conductor's own **motion** (not a changing $B$), this is called **motional emf**:
$$\boxed{\varepsilon = -Blv} \qquad (B, l, v \text{ mutually perpendicular})$$

**Direction -- Fleming's Right Hand Rule (FRHR):** thumb = direction of motion ($v$), forefinger = magnetic field ($B$), centre finger = induced current.

**Special and general cases:**
- If $v \parallel B$: **no emf is induced** (the rod's motion has no component driving charges along its length relative to the field).
- If the rod and its velocity are both inclined at angle $\theta$ to $B$ (the fully general case): $\varepsilon = Blv\sin\theta$.

---
*Note on this lecture's transcript:* the opening recap and the Lenz's-law energy-conservation argument (roughly the first 950 seconds of real content) are well corroborated by both transcript and board frames. Past that point, the transcript becomes unreliable -- a large block of earlier material gets re-transcribed a second and even a third time with fabricated later timestamps, silently standing in for the real audio. As a direct result, **every worked Lenz's-law practice problem past the ABC-loop case, the explicit $\varepsilon=-N\,d\Phi_B/dt$ recombination, and this lecture's entire motional-emf derivation (its own named second topic) are grounded from board frames alone.** See the flagged spans below for the full timeline and why the automated coverage/repetition checks did not catch it.

##### Verify these spans
- [10:46–35:34] Severe delayed-duplication, worse than a single repeat: the same block of content (magnet-withdrawal Lenz argument through the ABC-loop right-hand-rule problem, corresponding to real segments ~44-100) appears to have been re-transcribed by the model a SECOND time as segments 101-132 (timestamps 1632.2-1888.8s) and a THIRD time as segments 133-167 (timestamps 1888.8-2134.8s, i.e. running to and past the true 2129.8s end) -- e.g. segment 71@1070s / 143@1966s / 159@2072s are a near-verbatim ratio=1.00 triple, as are several dozen other pairs the delayed-duplicate scan flagged (54 pairs total, ratios 0.71-1.00). check_coverage()/sanitize_segments() do not catch this: duration coverage is ~100% and repetition_detected is False, because none of the duplicate segments are ADJACENT to their earlier twin -- each recurrence is separated by many segments, exactly the blind spot this scan exists for.
- [15:50–35:29] Consequence of the above: essentially everything the board shows from floor_000049 (t=960s) onward is missing from the ASR transcript, which spends that entire real-time window re-outputting earlier material under fabricated later timestamps instead. No transcript segment anywhere in this 168-segment transcript contains the words 'motional', 'Blv', 'Fleming', or 'Lorentz' -- despite 'motional emf' being this lecture's own named second topic, and despite a complete board derivation of it existing on schedule, well inside the verified 2129.8s duration. Board timeline used to ground this note: floor_000049 (960s) circle/square/triangle Lenz practice problems; floor_000059 (1160s) current-carrying-wire-and-coil problem; floor_000063/65 (1240-1280s) coil-approaching-magnet problem; floor_000071/73 (1400-1440s) Faraday+Lenz recombined WITH the minus sign, then 'ways to induce emf'; floor_000077-87 (1520-1720s) the full motional-emf flux-rule derivation to eps=-Blv; floor_000089/91 (1760-1800s) Fleming's Right Hand Rule; floor_000095-106 (1880-2100s, the last extracted frame) the v-parallel-to-B null case and the general eps=Blv*sin(theta) case, which is where the board's own content ends, matching the lecture's true runtime closely. Every claim in this note past 'the ABC-loop problem' is grounded from board frames alone for exactly this reason.

#### Motional EMF: Polarity, Numericals, Rotating Rod, and Energy Consideration

**NCERT sections covered:** 6.6

##### Motional EMF: polarity, and worked numericals (NCERT 6.6)

**Finding polarity:** for a rod moving with velocity $v$ through field $B$, using $\vec F=q\vec v\times\vec B$ on the rod's free charges, positive charge accumulates at one end and negative at the other, until the resulting internal electric field balances the magnetic force ($F_E=F_M$ at equilibrium). The rod then behaves like a fictitious battery — no battery is actually present, only charge separation.

###### Worked numerical: jet plane in Earth's field
A jet, wingspan $l=25$ m, flies west at $v=1800$ km/hr. Only Earth's **horizontal** field component $B_H$ matters (the vertical component $B_V$ is parallel to $l$, so contributes nothing — $v$, $l$, $B$ must all be mutually perpendicular). With $B=5\times10^{-4}$ T, dip angle $\delta=30°$:
$$B_H = B\cos\delta = 5\times10^{-4}\times\frac{\sqrt3}{2}$$
$$\varepsilon = B_H\, l\, v \qquad (v \text{ in m/s, via} \times 5/18)$$
Polarity found the same way as above via $\vec F=q\vec v\times\vec B$.

##### EMF from a rotating conductor

A rod of length $l$, hinged at the centre and free at the other end, rotates with angular velocity $\omega$ in a uniform field $B$ parallel to the rotation axis:
$$\boxed{\varepsilon = \frac{1}{2}B\omega l^2}$$

**Worked numerical:** rod length $1$ m, rotated at $50$ rev/s, hinged at the centre of a ring of radius $1$ m, $B=1$ T parallel to the axis. $\omega=2\pi\nu=2\pi(50)$ rad/s:
$$\varepsilon = \frac{1}{2}(1)(2\pi\times50)(1)^2 = 50\pi~\text{V}$$

**Second numerical (setup):** a wheel with $10$ metallic spokes, each $0.5$ m long, rotated at $120$ rev/min in a plane normal to Earth's horizontal field $H_E=0.4$ gauss.

##### Energy consideration in motional EMF (NCERT 6.6)

Conducting rod $ab$ (length $l$) slides with velocity $v$ on rails, closed through resistance $R$, in field $B$:
$$\varepsilon = Blv, \qquad i = \frac{Blv}{R}$$
Magnetic force on the current-carrying rod, opposing $v$ (Lenz's law / Fleming's left-hand rule):
$$F_m = BIl = \frac{B^2l^2v}{R}$$
To keep the rod moving at **constant velocity**, an equal and opposite applied force $F=B^2l^2v/R$ is needed. Rate of work done by this applied force:
$$P_\text{applied} = Fv = \frac{B^2l^2v^2}{R}$$
Rate of electrical energy dissipated in the circuit:
$$P_\text{dissipated} = I^2R = \left(\frac{Blv}{R}\right)^2 R = \frac{B^2l^2v^2}{R}$$
$$\boxed{P_\text{applied} = P_\text{dissipated}}$$
confirming energy conservation: mechanical work done pushing the rod converts exactly into dissipated electrical energy.

---
*Note on this lecture's transcript:* the jet-plane numerical is transcribed correctly once, then repeated nearly verbatim a second time, which drifted the transcript's own self-reported timestamps well behind real video time. As a result, three major topics that the board confirms were fully taught within the true ~1958s runtime — the completed rotating-rod derivation and its two numericals, and the entire "energy consideration" topic (this lecture's own second named topic) — never appear in the transcript's own words at all. All are grounded entirely from frames; see the flagged spans below.

##### Verify these spans
- [10:54–29:35] The jet-plane numerical (motional EMF, Earth's field) is transcribed correctly once (~t=654-1226s), but the ASR then re-transcribes essentially the same explanation nearly verbatim a second time (~t=1226-1775s) -- the same delayed-repetition pattern found repeatedly in this chapter's and Ch5's lectures. Board frames show that by real video time t=1260s the class has already finished this numerical AND completed the rotating-rod EMF derivation (epsilon=(1/2)*B*omega*l^2) plus solved a full worked numerical on it (metallic rod, 50 rev/s, giving 50*pi V) and started a second one (wheel with 10 spokes) -- meaning the transcript's self-reported timestamps for its second half are significantly drifted later than real video time due to this internal duplication. The rotating-rod claims above are grounded from frames rather than the transcript's own words, since the transcript (in its own, drifted timeline) only reaches the point of setting up the rotating-conductor problem before cutting off.
- [29:35–32:38] The transcript's own words never get past setting up the rotating-rod problem (its last segment describes the rod and asks for the EMF between a and b, without deriving or solving it). Board frames, however, show that -- likely well within the true 1958s runtime, given the timestamp drift documented above -- the class not only completes the rotating-rod derivation and two numericals but goes on to a full 'Energy consideration in motional EMF' derivation (floor_000079.jpg, floor_000096.jpg): the magnetic braking force on the rod, the applied force needed to sustain constant velocity, and the equality of applied mechanical power and dissipated electrical power. This entire topic -- named directly in this lecture's own filename ('numericals, energy consideration') -- is completely absent from the transcript's own words and is grounded here entirely from frames.

#### Flux/EMF Graph Numerical, Induced Charge, Induced Electric Field, Eddy Currents

**NCERT sections covered:** 6.4, 6.5, 6.6, 6.8

##### Worked numerical: flux, EMF, force, and power vs. distance (NCERT 6.4)

Classic NCERT-style problem: the arm PQ of a rectangular conductor is moved from $x=0$ outwards. A uniform field $B$ is perpendicular to the plane, present for $0\le x\le b$ and zero for $x>b$; only PQ (length $l$) has resistance $r$. PQ is pulled from $x=0$ to $x=2b$, then back to $x=0$, at constant speed $v$.

| Quantity | $0\le x<b$ | $b\le x<2b$ |
|---|---|---|
| Flux $\phi$ | $Blx$ (linear) | $Blb$ (constant) |
| EMF $\varepsilon=-d\phi/dt$ | $-Blv$ | $0$ |
| Force to pull PQ | $F=I l B=\dfrac{B^2l^2v}{r}$ | $0$ |
| Power dissipated | $P=I^2r=\dfrac{B^2l^2v^2}{r}$ | $0$ |

(Same pattern retraces, sign-flipped, on the return trip from $2b$ back to $0$.)

##### Induced charge is independent of time (NCERT 6.4)

From $\varepsilon=-N\dfrac{d\phi}{dt}$ and $I=\varepsilon/R$: charge in a small interval $dt$ is $dq = I\,dt = \dfrac{N}{R}d\phi$. Over a finite interval:
$$\boxed{q = \frac{N}{R}\,\Delta\phi}$$
The time interval cancels out completely — induced charge depends only on $N$, $R$, and the *total* flux change, never on how fast it happens.

##### Induced electric field (NCERT 6.4)

Unlike an **electrostatic** field (conservative: $\oint\vec E\cdot d\vec l=0$), an **induced** electric field arises from a time-varying $B$ and is **non-conservative**: $\oint\vec E\cdot d\vec l = -\dfrac{d\phi}{dt} \ne 0$.

##### Eddy (Foucault) currents (NCERT 6.5)

**Definition:** induced circulating currents produced *within* a metal itself, due to a change in flux linked with the metal; direction given by Lenz's law.

- **Damping example:** a metal plate oscillating in/out of a field comes to rest quickly — eddy currents oppose the motion. Slotting the plate lengthens the current path (more resistance, less current), reducing damping.
- **Jumping ring/disc:** an AC-driven coil induces eddy currents in a nearby disc; by Lenz's law the induced pole repels the coil's pole, making the disc jump.
- **Falling magnet in a tube:** dropping a magnet through a copper tube vs. a plastic tube of the same length — eddy currents in the copper brake the fall ($a<g$), while the plastic tube (non-conductive, no eddy currents) lets it fall freely ($a=g$).
- **Disadvantages:** energy loss as heat; unwanted damping.
- **Applications:** induction furnaces, speedometers, dead-beat galvanometers, electric braking (e.g. trains).

##### Third way to induce EMF: changing coil orientation (NCERT 6.8, intro to AC generator)

$$\phi = AB\cos\theta$$
where $\theta$ is the angle between the coil's area vector $\hat n$ and $\vec B$. With $\theta=\omega t$:
$$\phi = AB\cos(\omega t), \qquad \varepsilon = -\frac{d\phi}{dt} = AB\omega\sin(\omega t)$$
For an $N$-turn coil: $\varepsilon = NAB\omega\sin(\omega t)$ — the sinusoidal EMF of an **AC generator**.

---
*Note on this lecture's transcript:* the numerical's force and power parts (announced at the start but never narrated), the conclusion of the falling-magnet demonstration (cut off mid-sentence), and the final step of the AC-generator derivation are all grounded from board frames rather than the transcript's own words. See the flagged spans below.

##### Verify these spans
- [00:45–10:05] At the very start of this numerical (t=29s), the transcript explicitly announces that FOUR quantities will be found: flux, EMF, force, and power. The transcript's actual narration, however, only ever works through flux and EMF (with their graphs) before moving on (at t=605s) to a completely different topic (proving induced charge is independent of time interval) -- the force and power parts are never spoken at all. A board frame (floor_000030.jpg, t=580s -- chronologically before even the transcript's own EMF-graph discussion concludes) shows the complete solution already written for all four parts, including force (F=B^2l^2v/r) and power (P=B^2l^2v^2/r) with their own graphs vs. x. The force and power claims above are grounded entirely from this frame, not the transcript's own words.
- [29:40–30:07] The transcript describes a falling-magnet demonstration (dropping a magnet through a copper pipe vs. a plastic pipe of the same length, to see which one it exits first) but cuts off mid-sentence ('when it is coming down...') right as it should explain the actual physical conclusion, then abruptly jumps to a new topic ('advantages and disadvantages of eddy currents') with an out-of-order timestamp (the next segment's reported start, 1800s, is earlier than the cut-off segment's own start of 1801s) -- suggesting a dropped/skipped segment rather than a natural transition. A board frame (floor_000092.jpg) shows the resolution: the copper-tube magnet falls with a<g (eddy-current braking) while the plastic-tube magnet falls with a=g (free fall, no eddy currents possible in a non-conductor). This conclusion is grounded entirely from the frame.
- [34:33–36:28] The transcript's own words, in their final segments, introduce flux=AB*cos(theta) and identify theta as the angle between the area vector and B, but never reach the point of substituting theta=omega*t or taking the derivative to get the sinusoidal EMF form. A board frame (floor_000105.jpg) shows this next step already written (phi=AB cos(omega t), epsilon=-dphi/dt, with the derivative rule for cos(omega t) noted alongside) -- the direct, expected continuation of what the transcript itself sets up. The final AC-generator EMF formula claim above is grounded from this frame rather than the transcript's own words.

#### Self Induction (Inertia of Electricity) and Self Inductance

**NCERT sections covered:** 6.7

##### Self induction: inertia of electricity (NCERT 6.7)

When a coil is switched on, current takes time to rise to its maximum value rather than jumping instantly: the changing current produces changing flux through the coil itself, inducing a **back EMF** (by Lenz's law) that opposes the current's growth. At switch-off, the coil similarly opposes the current's decay. This resistance to *any change* in its own current — analogous to mechanical inertia — is why self-induction is called the **inertia of electricity**.

**Definition:** self-induction is the property of a coil by virtue of which it opposes the growth or decay of current flowing through it.

###### Conceptual example
Battery + key feed two parallel branches: inductor $L$ + bulb $B_1$, and resistor $R$ + bulb $B_2$.
- **On switch-close:** $L$ opposes current growth, $R$ doesn't $\Rightarrow$ $B_2$ glows **immediately**; $B_1$ brightens gradually.
- **On switch-open** (after both are steady): $L$ opposes the current's decrease $\Rightarrow$ $B_1$ glows **for longer**.

###### Sparking and non-inductive winding
Rapid voltage change at switching ($0\to230$ V or back) induces a large EMF, ionizing the air gap at switch contacts $\Rightarrow$ a spark (why circuits should never be switched near a gas leak). Modern switches add a small resistor between contacts to reduce this. Household AC wires are **twisted** together so current in adjacent opposite-direction sections is equal and opposite, cancelling the magnetic field — a **non-inductive coil**, minimizing self-induction.

##### Self-inductance $L$

Flux linked with a coil is proportional to current: $\phi \propto i \Rightarrow \phi = Li$, where $L$ is the **coefficient of self-induction** (self-inductance).

**Three equivalent definitions:**
1. Setting $i=1$ A: $L=\phi$ — flux linked with the coil per unit current.
2. From $e=-d\phi/dt = -d(Li)/dt$: $\boxed{e = -L\dfrac{di}{dt}}$
3. Setting $di/dt=1$ A/s: $L=e$ — the EMF induced per unit rate of change of current.

**Units:** $L=\phi/I \Rightarrow$ Wb/A $=$ **Henry (H)**; also $L=e/(di/dt)\Rightarrow$ V$\cdot$A$^{-1}\cdot$s. $1\text{ H} = 1\text{ V}\cdot\text{A}^{-1}\cdot\text{s} = 1\text{ Wb}\cdot\text{A}^{-1}$.
**Dimensional formula:** $[L] = [ML^2T^{-2}A^{-2}]$

---
*Note on this lecture's transcript:* this is one of the cleanest transcripts found in this chapter. The only gap is at the very end — the video cuts off just as a third phrasing of $L$'s definition is announced; that phrasing and the units/dimensional formula are grounded from a board frame just past the transcript's own last words.

##### Verify these spans
- [24:14–24:14] The transcript's very last words are 'So, now let's try to define L' -- suggesting a third phrasing of the definition is about to be given, right as the video ends. A board frame (floor_000069.jpg) shows this third definition already written out (L=e when di/dt=1), along with the units of L (Wb/A = Henry; V.A^-1.s) and its dimensional formula [ML^2T^-2A^-2]. Since the transcript itself never speaks these words, the third-definition and units/dimensions claims above are grounded from the frame -- the direct, expected continuation of what the transcript's own final sentence announces.

#### Inductor, Self Inductance of a Solenoid, Energy Stored, and Intro to Mutual Induction

**NCERT sections covered:** 6.7

##### Ideal resistor vs. ideal inductor; self-inductance of a solenoid (NCERT 6.7)

An **ideal resistor** has zero self-inductance; an **ideal inductor** has zero resistance and high self-inductance. An inductor is a tightly wound coil of insulated wire. (Real components are never perfectly ideal.)

###### Self-inductance of a solenoid
Solenoid: length $L$, $n$ turns per unit length ($N=nL$ total turns), area $A$, current $I$. Using $B=\mu_0 nI$ (Ampere's law) and flux per turn $\phi=BA$:
$$\phi_\text{total} = N\phi = N A B = (nL)(A)(\mu_0 nI) = \mu_0 n^2 A L\, I$$
Since $\phi_\text{total}=LI$:
$$\boxed{L = \mu_0 n^2 A L}$$
With a magnetic core of relative permeability $\mu_r$: $L=\mu_0\mu_r n^2 A L$ (bigger $L$ opposes current more strongly).

##### Energy stored in an inductor

Charging current against the back EMF does work: $dW = E\,dq$. With $E=L\,dI/dt$ and $dq=I\,dt$: $dW = LI\,dI$. Integrating from $0$ to $I$:
$$\boxed{U_M = \frac{1}{2}LI^2 = \frac{1}{2}\phi I}$$

###### Energy density (energy per unit volume)
$$u = \frac{U_M}{\text{Volume}} = \frac{\frac12 LI^2}{AL}$$
Substituting $\phi=NAB$, $L=\phi/I$, and $B=\mu_0 nI$ (so $nI=B/\mu_0$), this simplifies to the standard result:
$$\boxed{u = \frac{B^2}{2\mu_0}}$$

##### Mutual induction (intro)

**Phenomenon:** inducing a current in a nearby coil (secondary, $S$) due to a changing current in another coil (primary, $P$). Coefficient of mutual induction:
$$\phi_S \propto I_P$$

**Demo:** AC-driven primary coil $A$; secondary coil $B$ with a bulb lights up due to mutual induction. Moving $B$ further from $A$ dims the bulb — flux linking $B$ decreases with separation.

---
*Note on this lecture's transcript:* the derivation of energy density is cut off mid-algebra right at the transcript's own final words, and the introduction to mutual induction (this lecture's own third named topic) never appears in the transcript at all. Both are completed/grounded from a board frame; see the flagged span below.

##### Verify these spans
- [20:12–22:12] The transcript's own words are still working through the algebra of the energy-per-unit-volume derivation right up to its very last segment ('I want my answer... I want basically B, I don't want to eliminate B because at the back of the mind I want to prove that this energy per unit volume...'), cutting off before ever stating the final result or reaching mutual induction at all. However, a board frame (floor_000061.jpg) -- whose true video timestamp (t=1200s) falls BEFORE the transcript's own self-reported final segment (which claims to start at t=1336s, already past the video's true 1332.03s duration) -- shows mutual induction already introduced in full: its definition, the coefficient of mutual induction (phi_S proportional to I_P), and a primary/secondary coil demonstration with a bulb. This confirms the transcript's own timestamps drifted later than real video time by the end of the lecture. The final energy-density result (u=B^2/2*mu0) is the direct, expected algebraic completion of the transcript's own work and is standard NCERT content; the mutual-induction claims are grounded entirely from the frame, not the transcript's own words.

#### Mutual Inductance of Two Coaxial Solenoids, Worked Numerical, and the AC Generator

**NCERT sections covered:** 6.7, 6.8

##### Mutual inductance of two coaxial solenoids (NCERT 6.7)

Two long coaxial solenoids $S_1$ (inner, $n_1$ turns/length, $N_1$ turns, area $A_1$) and $S_2$ (outer, $n_2$, $N_2$, $A_2$), both length $l$. Current $I$ in $S_1$ creates:
$$B_1 = \mu_0 n_1 I = \mu_0\frac{N_1}{l}I$$
Flux linked with $S_2$ (using $A_1$, the area where $B_1$ actually exists):
$$\phi_2 = N_2 B_1 A_1 = \mu_0\frac{N_1 N_2 A_1}{l}I \quad\Rightarrow\quad \boxed{M_{21} = \frac{\mu_0 N_1 N_2 A_1}{l}}$$

**Reciprocity:** a symmetric argument (current in $S_2$ instead, using whichever cross-section is common/smaller) gives $M_{12}=M_{21}$ — the mutual inductance is the same either way.

###### Worked numerical (classic two-loop problem)
A circular loop of radius $0.3$ cm lies parallel to a much bigger circular loop of radius $20$ cm, centres $15$ cm apart. (a) Flux linking the bigger loop for $I=0.2$ A in the smaller loop? (b) Mutual inductance?

**Method:** treat the small loop as a point dipole; use the big loop's on-axis field $B=\dfrac{\mu_0}{2}\dfrac{I a_2^2}{(a_2^2+x^2)^{3/2}}$ at the small loop's location, then $\phi = \pi a_1^2 B$ (uniform over the tiny loop's area); $M=\phi/I$.

##### The AC generator (NCERT 6.8)

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

##### Verify these spans
- [05:03–37:19] This is the most severe delayed-repetition failure found anywhere in this project: after correctly deriving M21 (t=3-303s), the transcript gets stuck setting up the M12=M21 proof ('to calculate M12, consider current flowing through S2... magnetic field generates only in area A2... M12 due to 2... n1 n2 mu0 a2 upon l') and re-transcribes this SAME ~230-second block at least SEVEN times back-to-back, continuing almost verbatim all the way to the transcript's very last word ('flowing', at t=2242.975s, cut off mid-sentence). Essentially the entire remaining 86% of this lecture's real content -- completion of the M12=M21 proof, the worked mutual-inductance numerical (the lecture's own second named topic), and the ENTIRE AC generator topic (construction, working, and the full sinusoidal-EMF derivation -- the lecture's own third named topic) -- is completely absent from the transcript's own words. Board frames confirm all of this content was genuinely taught and written out in full within the true 2239.5s runtime (the numerical at real t~1180s, the complete AC generator section by real t~2220s, near the very end of the video). Every claim in this note beyond the initial M21 derivation is grounded entirely from frames, not the transcript's own words.

### Chapter 7 · Alternating Current — lecture notes

#### Mean (Average) and RMS Value of Alternating Current

**NCERT sections covered:** 7.1, 7.2

##### Introduction to AC

Alternating current varies continuously in magnitude and periodically reverses direction, written as $i = i_0\sin(\omega t)$ (or equivalently $i_0\cos\omega t$, since both sine and cosine are periodic -- the lecture notes both forms are used interchangeably depending on where $t=0$ is taken). Time period $T$ is the time for one cycle; frequency $f = 1/T = \omega/2\pi$.

Domestic AC supply in India is 50 Hz. Since current crosses zero twice per cycle, at 50 Hz a bulb driven by mains current is effectively "off" 100 times a second -- invisible to the eye because of persistence of vision. The lecture notes that at deliberately low frequencies (e.g. a hand-cranked classroom generator) this flicker becomes visible as the bulb visibly switching on and off.

Alternating EMF follows the same form: $e = e_0\sin(\omega t)$ or $e_0\cos(\omega t)$.

##### Mean (average) value of AC

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

##### RMS (root mean square) value of AC

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

##### Worked numericals (board-only)

The board (visible from roughly 1780s to the end of the lecture) works through six short problems applying the $i_0=\sqrt2\, I_{rms}$ / $I_{rms}=0.707\,i_0$ relations. These do not have matching spoken narration in the available transcript (see uncertain span below) but are clearly legible on the board:

1. $E_{rms}=220\text{ V}$ (household mains) $\Rightarrow E_0=\sqrt2\times220\approx311\text{ V}$ -- matches NCERT's own worked household-voltage figure exactly.
2. $I_{rms}=10\text{ A}\Rightarrow I_0=\sqrt2\times10\approx14.14\text{ A}$.
3. $i=6\sin(314t)\text{ A}$ (i.e. $\omega=314\text{ rad/s}\approx2\pi\times50\text{ Hz}$) $\Rightarrow I_0=6\text{ A}$, $I_{rms}=0.707\times6\approx4.24\text{ A}$.
4. Given rms voltage during a half cycle, find peak voltage and mean value -- set up the same way as above ($E_0=\sqrt2\,E_{rms}$, $E_m=0.637E_0$).
5. Time for current starting from zero to reach its peak value: $t=T/4$ (one quarter cycle), read directly off the sine waveform.
6. RMS value of a **square wave** alternating between $+2$ A and $-2$ A: since the sinusoidal formula $i_0/\sqrt2$ does not apply to a non-sinusoidal waveform, the board instead applies the defining recipe directly -- square the current, average the squares, take the square root: $I_{rms}=\sqrt{\dfrac{I_0^2+I_0^2+I_0^2}{3}}=2\text{ A}$. This is a good check that the student understands "root-mean-square" as a procedure, not just a formula tied to sine waves.

##### Verify these spans
- [29:39–32:49] Delayed-repetition ASR artifact: segment starting 1779.5s ('Now, see here, in this case, let's try to understand this definition first...') is repeated almost verbatim at 1944.3s, with segments 65-66 in between (1845.9-1944.3s) re-covering the same 'same amount of heat in a given resistance' phrasing already said at 1720.7s. Net effect is only a short (~165s) block of redundant/looped narration around the RMS heat-definition setup, not a loss of new content -- board frames (floor_000064 at 1260s onward) show the derivation already fully written and progressing steadily, so nothing appears to have been dropped.
- [37:15–38:25] Transcript ends mid-sentence ('Now for AC what you can do is heat produced by AC circuit in time T') without ever verbally stating the final RMS-current derivation or its conclusion I_rms = i0/√2. The segment's declared end (2305.8s) also overshoots the reported lecture duration (2261.8s) by ~44s, suggesting either truncation or an imprecise end-timestamp for the final utterance. However, board frames from ~1580s onward (floor_000080, floor_000083) already show this exact derivation completed and boxed (I_rms = i0/√2 = 0.707 i0, E_rms = 0.707 e0), and frames from 1780s-2240s show it being applied confidently across six solved numericals ending with a non-sinusoidal square-wave example -- so the material was clearly taught in this lecture even though the ASR did not capture the teacher saying the final conclusion aloud. Grounded from frames per the workflow's guidance for this exact failure pattern.
- [25:19–26:10] Segments 56-57 consist of the short phrase 'So, mean or average value of AC is that direction' repeated verbatim ~38 times in a row (a stutter/loop artifact within the ASR output itself, distinct from the delayed-repetition pattern above). Segment durations (21-30s) are plausible for real elapsed time, and the derivation resumes cleanly on both sides (Im=2i0/pi immediately before, 0.637i0 immediately after), so this looks like a local ASR glitch rather than missing content -- flagging for awareness, not treated as a content gap.

#### AC Circuits with Only R and Only L (Phasors, Resistor, Pure Inductor)

**NCERT sections covered:** 7.2, 7.3, 7.4

##### Phasors

A phasor is a vector that rotates about the origin with angular speed $\omega$. Its vertical (projected) component at any instant gives the instantaneous value of the quantity it represents. Both current and voltage in an AC circuit are represented as phasors -- $i_0$ and $e_0$ are the phasor lengths (amplitudes), and the projection onto the vertical axis traces out $i_0\sin\omega t$ or $e_0\sin\omega t$ as the phasor sweeps around.

##### AC circuit with only a resistor

For an ideal resistor $R$ on source $e=e_0\sin\omega t$, Kirchhoff's law gives directly
$$e_0\sin\omega t = iR \quad\Rightarrow\quad i = i_0\sin\omega t,\quad i_0=\frac{e_0}{R}$$
Current and voltage are **in phase** -- same $\sin\omega t$ dependence, zero phase difference. On a phasor diagram the $E_0$ and $I_0$ phasors point along the same line; on a $y$-$t$ graph the two sinusoids rise and fall together.

**Aside -- why AC needs its own ammeter design.** A DC ammeter placed in an AC circuit reads the *mean* current, which is zero over a full cycle, so it shows a zero reading. Purpose-built AC ammeters instead exploit the **heating effect** of current ($H\propto i^2Rt$): since $i^2$ is never negative, this gives a genuine non-zero reading, but because the response is proportional to $i^2$ rather than $i$, the scale spacing on an AC ammeter is unequal -- markings spread further apart at higher readings -- rather than the evenly-spaced scale on a DC ammeter.

##### AC circuit with only (pure) inductance

For an ideal inductor $L$ (no resistance) on the same source, the induced EMF is $e=-L\,di/dt$, so by Kirchhoff's law
$$e = L\frac{di}{dt} \quad\Rightarrow\quad di = \frac{1}{L}e\,dt \quad\Rightarrow\quad i = \frac{1}{L}\int e_0\sin(\omega t)\,dt = \frac{e_0}{\omega L}\big[-\cos\omega t\big]$$
Rewriting $-\cos\omega t$ as $\sin(\omega t - \pi/2)$ (worked out on the board via $\sin(\pi/2-\omega t)=\cos\omega t$, then reversing sign) gives the standard form
$$i = \frac{e_0}{\omega L}\sin\left(\omega t - \frac{\pi}{2}\right) = i_0\sin\left(\omega t-\frac{\pi}{2}\right),\qquad i_0=\frac{e_0}{\omega L}$$
Defining **inductive reactance** $X_L=\omega L$ (unit ohm, playing the same role $R$ plays for a resistor), this is $i_0=e_0/X_L$.

**Phase relationship.** Current **lags** voltage by $\pi/2$ (a quarter cycle) in a pure inductor -- when the voltage is at its peak, current is zero, and when voltage is zero, current is at its peak. This is the opposite of the resistor case and is drawn on the board both as an $e,i$-vs-$t$ graph and as a phasor diagram with the $I_0$ phasor sitting $90°$ behind $E_0$.

##### Worked numericals (board)

1. **Pure resistance, R = 10 Ω, 230 V–50 Hz supply.** $I_{rms}=V_{rms}/R=230/10=23\text{ A}$. With $\omega=2\pi(50)=100\pi\text{ rad/s}$: $e=230\sqrt2\sin(100\pi t)$, $i=23\sqrt2\sin(100\pi t)$ -- same phase, as expected for a resistor.
2. **Pure inductive coil, I_rms = 10 A from the same 230 V–50 Hz supply, find X_L and L.** $X_L=V_{rms}/I_{rms}=230/10=23\ \Omega$, so $L=X_L/\omega=23/(2\pi\times50)\approx0.073\text{ H}$. Current equation written with the lag explicit: $i=10\sqrt2\sin(100\pi t-\pi/2)$.
3. **A third coil problem** ($L=1.4$ H, $f=50$ Hz, a given peak current, asking for pd across the coil and its rms value) appears on the last sampled board frames but the intermediate arithmetic could not be reliably read off the image -- see the uncertain span below. Only the problem's existence and setup are recorded here, not a solved answer.

##### Verify these spans
- [25:55–27:13] CONFIRMED delayed-repetition ASR corruption, and this one produces a physically WRONG statement, not just redundant text. Segments here ('equation one and two implies... E and I are in phase... E0 upon r is I0') are a near-verbatim duplicate (similarity ratio 0.82-0.99) of segments 23-25 from the RESISTOR section (491-535s) -- but they have been grafted onto the tail of the INDUCTOR derivation, where the just-completed board work (i = i0 sin(wt - pi/2), see floor_000047) unambiguously shows current LAGGING voltage by pi/2, not 'in phase'. This claim is NOT used anywhere in this note. Board frames covering this exact video-time window (floor_000077 at 1520s through floor_000089 at 1760s) show the real content that was almost certainly on the audio here: two fully worked numericals (pure-R circuit: R=10 ohm, 230V-50Hz -> Irms=23A; pure-inductive-coil circuit: Irms=10A, 230V-50Hz -> XL=23 ohm, L=0.073H) that have NO transcript representation at all -- neither these substituted segments nor any segment before/after mentions numeric values 10, 23, 230, or 0.073. Both numericals are grounded from frames only in this note (see the two worked-example claims above).
- [31:00–32:26] A third worked numerical appears on the last two sampled board frames (floor_000094, floor_000097, both past the last indexed frame at 1860s and un-timestamped beyond that): a pure inductive coil with L=1.4 H, f=50 Hz and a given I0, asking for the pd across the coil and its rms value. The intermediate working shown (e0 = I0(wL) = 10 x 2*pi*50 x 1.4) does not cleanly match the I0 value legible elsewhere on the same frame (I0=2A), so the arithmetic could not be confidently reconciled from the image alone -- possibly a board transcription-of-handwriting misread on my part, possibly the teacher's own slip, possibly a leftover value from the previous problem. No transcript coverage exists for this region at all (last transcript segment ends at 1941.4-1980.4s describing the general inductor phasor diagram, not this specific numerical) to cross-check against. Left out of the grounded claims above rather than asserting an unverified number; the problem's existence and setup (not its solved answer) is the only thing confidently established here.
- [10:12–13:29] Segments 28-35 repeat an identical short description of the resistor phase diagram ('this is the phase diagram... they are in the same phase... now if I draw a phase diagram...') four times in a row. Unlike the corruption above, this looks like genuine repeated in-class narration rather than a content-hiding artifact: the board (floor_000030 at 580s) already shows the complete resistor phasor diagram and waveform sketch fully drawn, consistent with the teacher recapping the same simple diagram while students copy it down. Flagged for awareness only; no claim in this note depends on distinguishing the four repeats from each other.

#### AC Circuits: Pure Capacitor, Power in L/C, LR Circuit, RC Circuit, Numericals

**NCERT sections covered:** 7.5, 7.6, 7.7

##### AC circuit with a pure capacitor (NCERT 7.5)

With $E=E_0\sin(\omega t)$: $q=CE_0\sin(\omega t)$, $i=dq/dt=\omega C E_0\cos(\omega t) = E_0\omega C\sin(\omega t+\pi/2)$.

**Current leads EMF by $\pi/2$** (opposite the inductor case). Writing $i=I_0\sin(\omega t+\pi/2)$ with $I_0=E_0/X_C$:
$$\boxed{X_C = \frac{1}{\omega C}} \quad\text{(capacitive reactance, unit: ohm)}$$

$X_C f = \dfrac{1}{2\pi C}=$ const $\Rightarrow$ $X_C$ vs. $f$ is a rectangular hyperbola. At $f=0$ (DC), $X_C\to\infty$ — **a capacitor blocks DC**.

**Worked numerical:** $318\,\mu$F, $230$ V, $50$ Hz. $X_C\approx10\,\Omega$; $I_\text{rms}=E_\text{rms}/X_C=230/10=23$ A; $i=I_0\sin(\omega t+\pi/2)$, $E_0=\sqrt2\,E_\text{rms}$.

##### Average power in pure L or C: zero (wattless current) (NCERT 7.7)

For a pure inductor, $P=EI=E_0I_0\sin(\omega t)\sin(\omega t-\pi/2) = -\tfrac12 E_0I_0\sin(2\omega t)$ — averages to **zero** over a full cycle. Current still flows despite zero power dissipation: this is **wattless current**. (Same result, opposite sign, for a pure capacitor.)

**Practical use:** to reduce AC current with (ideally) no power loss, prefer an inductor over a resistor — old tube lights used a **choke coil** for exactly this reason.

##### LR circuit (extends NCERT 7.6's phasor method)

$V_R$ and $V_L$ add as **phasors**, not algebraically (they're $90°$ out of phase — $V_L$ leads $V_R$):
$$E = \sqrt{V_R^2+V_L^2} = I\sqrt{R^2+X_L^2} = IZ, \qquad Z=\sqrt{R^2+X_L^2}~\text{(impedance)}$$
$$\phi = \tan^{-1}\frac{X_L}{R}, \qquad E = E_0\sin(\omega t+\phi)$$

**Worked numerical:** coil $L=0.5$ H, $R=100\,\Omega$, on $240$ V, $50$ Hz AC. $Z_L=\sqrt{R^2+(\omega L)^2}$; max current $I_0=E_0/Z_L\approx1.82$ A; phase angle $\phi=\tan^{-1}(\omega L/R)\approx57.5°$; **time lag** $=\phi/\omega\approx3.19\times10^{-3}$ s (current peaks this long after voltage peaks).

##### RC circuit (extends NCERT 7.6's phasor method)

By analogous phasor reasoning (now $I$ leads $\varepsilon$, since current leads voltage across $C$):
$$\varepsilon = \sqrt{V_R^2+V_C^2} = I\sqrt{R^2+X_C^2} = IZ_C, \qquad Z_C=\sqrt{R^2+\frac{1}{\omega^2C^2}}$$
$$\tan\phi = \frac{X_C}{R}=\frac{1}{\omega CR}, \qquad \phi = \tan^{-1}\left(\frac{1}{\omega CR}\right)$$

**Worked numerical (setup + method):** circuit on $20$ V, $50$ Hz takes $10$ A, current leading voltage by $T/12$. $\phi = 360°/12=30°$; $R=Z_C\cos\phi$ (with $Z_C=E_\text{rms}/I_\text{rms}$); $X_C$ and hence $C$ follow similarly.

**Second numerical (unfinished in available material):** a $100$ V, $60$ W lamp operated on $220$ V, $50$ Hz mains — find $R$, $X_C$, and $C$ (a lamp-in-series-with-capacitor circuit, used to drop voltage without wasting power in a resistor).

---
*Note on this lecture's transcript:* the LR-circuit derivation repeats nearly verbatim six times back-to-back, consuming roughly 1000 seconds and drifting the transcript's own timestamps for everything after it. As a result, the entire RC-circuit derivation and its own worked numerical are completely absent from the transcript's words and are grounded here from a board frame; the final lamp-and-capacitor numerical is left unsolved since neither the transcript nor the available frames capture its resolution.

##### Verify these spans
- [18:41–37:09] The LR-circuit phasor derivation (from setting up the vector-addition argument through the full phasor diagram and phase-angle formula) is transcribed correctly once, then re-transcribed nearly verbatim FIVE more times back-to-back (roughly repeating every ~150-230s from t~1262s through t~2229s) -- another instance of the severe delayed-repetition pattern found throughout this project. This consumed roughly 1000 seconds of transcript time narrating what is a single, short derivation, and appears to have drifted the transcript's own internal timestamps for everything that follows.
- [43:48–46:03] After the LR-circuit numerical, the transcript's own words move directly into setting up a second numerical (a 100V, 60W lamp operated on 220V, 50Hz mains, asked to find resistance, capacitive reactance, and capacitance) but cut off mid-question at 'and capacitance of' -- never reaching the RC-circuit derivation or its own worked numerical at all. However, a board frame (floor_000134.jpg, true video timestamp t=2660s) shows a complete RC-circuit phasor derivation AND a distinct worked numerical (a 20V/50Hz/10A circuit with current leading by T/12) already substantially solved. Since this content cannot fit within the transcript's own (drifted) timeline after the LR numerical, this confirms the earlier repetition pushed the transcript's self-reported timestamps for its final third well behind real video time. The RC-circuit derivation and this second numerical are grounded entirely from the frame; the lamp-and-capacitor numerical remains only partially stated (never solved) in the available material, so no answer is given for it here.

#### LCR Series Circuit, Resonance, Q Factor, and LC Oscillations

**NCERT sections covered:** 7.7, 7.8, 7.9

##### LCR series circuit (NCERT 7.7)

$V_R=IR$ (in phase with $I$), $V_L=IX_L$ (leads $I$ by $90°$), $V_C=IX_C$ (lags $I$ by $90°$). Since $V_L$, $V_C$ are $180°$ apart, their resultant is $V_L-V_C$ (say $V_L>V_C$), perpendicular to $V_R$:
$$E = \sqrt{V_R^2+(V_L-V_C)^2} = I\sqrt{R^2+(X_L-X_C)^2} = IZ$$
$$Z=\sqrt{R^2+(X_L-X_C)^2}~\text{(impedance)}, \qquad \tan\phi=\frac{X_L-X_C}{R}$$

##### Resonance (NCERT 7.8)

When $X_L=X_C$ ($\omega L = 1/\omega C$): **resonance**. Here $Z=R$ (minimum), $\phi=0$ (purely resistive behavior), and current is **maximum**, $I_\text{max}=E/R$.
$$\boxed{\omega_r = \frac{1}{\sqrt{LC}}}$$

**Resonance curve** ($I_0$ vs. $\omega$): peaks at $\omega_r$. Smaller $R$ $\Rightarrow$ sharper peak $\Rightarrow$ more **selective** — exactly the property used to tune a radio/TV to one station among many overlapping frequencies.

###### Quality factor (Q)
$$Q = \frac{V_L\text{ (or }V_C\text{) at resonance}}{V_R\text{ at resonance}} = \frac{\omega_r L}{R} = \frac{1}{R}\sqrt{\frac{L}{C}}$$
High $Q$ needs large $L$, small $R,C$.

**Half-power points** $\omega_1,\omega_2$: where $I=I_0/\sqrt2$. **Bandwidth** $BW=\omega_2-\omega_1$ (smaller for sharper curves). Second definition:
$$Q = \frac{\omega_r}{BW}$$

##### LC oscillations (NCERT 7.9)

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

##### Verify these spans
- [37:16–40:00] There is a genuine ~164-second gap in the transcript with no segments at all (jumping directly from the definition of LC oscillations, ending mid-sentence around t=2236s, to a segment at t=2400s that is itself mid-sentence: 'c and Um is equal to zero'). This is where the initial circuit setup (capacitor charged, connected via switch to the inductor) and the first two energy states (t=0: U_E max, U_M=0; t=T/4: U_E=0, U_M max) must have been explained, based on both the surrounding context and a board frame (floor_000123.jpg) that shows exactly this content -- the t=0 and t=T/4 circuit diagrams with their energy formulas. The initial-setup claim above is grounded from this frame rather than the transcript's own words, since no transcript segments exist for this stretch.

#### Power in AC Circuits, Power Factor, Wattless Current, and the Transformer

**NCERT sections covered:** 7.7, 7.8

##### Average power in an AC circuit (NCERT 7.7)

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

##### Wattless current (general case)

Resolving $I_\text{rms}$ relative to $E_\text{rms}$ (angle $\phi$): the parallel component $I_\text{rms}\cos\phi$ delivers real power ($P_\text{avg}=E_\text{rms}I_\text{rms}\cos\phi$); the perpendicular component $I_\text{rms}\sin\phi$ delivers **zero** power (angle $90°$ to $E_\text{rms}$). This perpendicular component is the **wattless current** — current that flows without consuming power over a cycle.

##### The transformer (NCERT 7.8)

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

##### Verify these spans
- [24:20–28:18] The transcript's own words never get past explaining the transformer's construction (soft iron core, lamination to reduce eddy currents, coil winding) -- its last available segment ends mid-explanation of lamination/eddy currents. However, board frames confirm that, within the true video duration, the lecture goes on to derive the transformer's key working equations (epsilon_s/epsilon_p=Ns/Np=Ip/Is, step-up vs. step-down) and lists all four types of energy losses in a real transformer (flux leakage, winding resistance, eddy currents, hysteresis losses) -- none of which appear in the transcript's own words at all. Both the working-equations claim and the energy-losses claim above are grounded entirely from frames.

### Chapter 8 · Electromagnetic Waves — lecture notes

#### Displacement Current and Maxwell's Equations

**NCERT sections covered:** 8.1, 8.2

##### The problem with Ampere's circuital law (NCERT 8.2)

Ampere's circuital law states $\oint \vec{B}\cdot d\vec{l} = \mu_0 I$, where $I$ is the current
enclosed by the Amperian loop.

Consider a capacitor being charged by a time-varying current $i(t)$. Draw a loop around one of
the connecting wires, and consider two different surfaces bounded by that same loop:

- **$C_1$**: a small "pot"-shaped surface that stays outside the capacitor gap -- the wire's
  conduction current $I$ pierces it, so Ampere's law gives $\oint \vec{B}\cdot d\vec{l} = \mu_0 I$.
- **$C_2$**: a larger surface bulging through *between* the plates -- no conduction current
  crosses it (charge does not jump the gap), so Ampere's law gives $\oint \vec{B}\cdot d\vec{l} = 0$.

Both surfaces share the same boundary loop, so $\vec{B}$ integrated around that loop cannot
have two different values -- Ampere's law as stated is inconsistent. The lecture also frames
this as an apparent violation of Kirchhoff's junction rule: current $I$ flows in at a point $P$
just before one plate, seems to vanish across the gap, and reappears at a point $Q$ past the
other plate.

##### Maxwell's resolution: displacement current (NCERT 8.2)

Maxwell's fix: there must be a second current term active precisely in the gap where the
conduction current is zero. Between the plates, the electric flux is

$$\Phi_E = \vec E \cdot \vec A = \frac{\sigma}{\varepsilon_0}A = \frac{Q}{\varepsilon_0}$$

using the field between capacitor plates $E = \sigma/\varepsilon_0 = Q/(A\varepsilon_0)$.
Differentiating with respect to time,

$$\varepsilon_0\frac{d\Phi_E}{dt} = \frac{dQ}{dt}$$

and since $dQ/dt$ is a current by definition, Maxwell named this the **displacement current**,

$$I_d = \varepsilon_0 \frac{d\Phi_E}{dt}$$

Outside the plates only conduction current flows ($I_d = 0$); inside the gap only displacement
current flows ($I_c = 0$); together they form one continuous total current $I = I_c + I_d$ that
never actually breaks at the gap -- resolving the Kirchhoff-rule paradox as well. This gives the
corrected, general form of Ampere's law (the Ampere-Maxwell law):

$$\oint \vec B \cdot d\vec l = \mu_0\left(I_c + \varepsilon_0\frac{d\Phi_E}{dt}\right)$$

##### Maxwell's four equations (NCERT 8.2, boxed summary)

The board closes the lecture by collecting the complete set of Maxwell's equations in vacuum:

1. **Gauss's law of electrostatics:** $\oint \vec E \cdot d\vec A = Q/\varepsilon_0$
2. **Gauss's law of magnetostatics:** $\oint \vec B \cdot d\vec A = 0$
3. **Faraday's law of EMI:** $\oint \vec E \cdot d\vec l = -\dfrac{d\Phi_B}{dt}$ (i.e. $\varepsilon = -d\phi/dt$)
4. **Modified (Ampere-Maxwell) circuital law:** $\oint \vec B \cdot d\vec l = \mu_0\left(I_c + \varepsilon_0\dfrac{d\Phi_E}{dt}\right)$

This is exactly NCERT's boxed list in section 8.2, same four laws, same order.

##### A note on this lecture's transcript

The automated coverage check reports 107% coverage and passes cleanly, but that is misleading
here -- see the uncertain span below. The ASR transcript's real content stalls mid-derivation
(still building $\Phi_E = E\cdot A$) and its last captured sentence cuts off mid-word. It never
narrates the differentiation step, the $I=I_c+I_d$ statement, or Maxwell's four equations by
name at all, even though the board frames show all of this written out, in a natural progressive
build on the same page, well within the lecture's verified 980.19s duration. The final three
claims above (differentiation/$I_d$, and Maxwell's four equations) are therefore grounded from
board frames only.

##### Verify these spans
- [13:50–16:20] The transcript's own final segment is timestamped 968.0-1056.0s, which overshoots the video's verified true duration (980.19s) by ~76s -- exactly the 'coverage looks clean but isn't' trap: check_coverage() reports 107% coverage and passes, yet the segment's text cuts off mid-word ('...electric field direction is this is the direction o'), and the delayed-duplicate scanner found no repeated block (0 flagged pairs), so this is neither of the two previously-catalogued failure modes cleanly -- it looks like a silent truncation whose tail segment was also given a stretched/overshot timestamp. Either way, the transcript's real captured content stalls partway through the displacement-current derivation (still building Phi_E = E.A) and never reaches the differentiation step (I_d = eps0 dPhi_E/dt), the I=Ic+Id statement, or any mention of 'Maxwell's equations' / 'Gauss's law' / 'Faraday's law' by name. The board frames, however, show this content completed and written out in full: floor_000030 (sampled at video t=580s -- notably BEFORE the transcript's own claimed timestamp for the Phi_E=E.A discussion, another sign the transcript's internal timestamps are not reliable in this stretch) already has the differentiation and I=Ic+Id; floor_000043 (t=840s) has Maxwell's equations 1-2 being written; floor_000049 (t=960s, near the true end) has all four complete. These three frames sit on the same continuously-built board page as the earlier, transcript-confirmed derivation (visible progression, not a jump to an unrelated page), which is why they are trusted as belonging to this lecture despite having no matching transcript span -- grounded from board frames alone, per claims 7 and 8 above.

#### Displacement Current, Maxwell's Equations, and the E-B Symmetry

**NCERT sections covered:** 8.1, 8.2

##### Relationship to the other Displacement-Current lecture in this chapter

This lecture (`Displacement and maxwell Eqns..mkv`, 1063.3s) covers essentially the same
material as the shorter `#1Displacement current and Maxwell Eqns.mp4` (980.19s, see
`01-displacement-current-and-maxwells-equations.md`) -- same opening line almost verbatim, the
identical pot/tiffin-box two-surface argument, the identical Kirchhoff-paradox framing, and (from
the board) what looks like literally the same handwritten page for the first half of the
derivation. It is **not** a duplicate file (different sha256, different duration, different
Gemini cache key -- see the chapter's file-list note), and it is meaningfully more complete: it
continues past the point where lecture 01's transcript stalls, explicitly *narrating* (not just
writing on the board) all four of Maxwell's equations one at a time by name and formula, and
closes with a spoken resolution of the apparent Kirchhoff violation and a short discussion of the
symmetry between Faraday's law and the displacement-current result that lecture 01 does not have
in its transcript at all. It also continues slightly further, into a one-line preview of "light is
an EM wave" that bridges into the chapter's next topic. Whether this is an independent retake or
an extended second pass over the same board is not determinable from the available material, but
for note-taking purposes this version supersedes lecture 01 in coverage -- if a student only had
time for one of the two, this is the more complete one.

##### The problem with Ampere's circuital law (NCERT 8.2)

Ampere's circuital law states $\oint \vec B \cdot d\vec l = \mu_0 I$. For a capacitor being
charged by a time-varying current $i(t)$, two different surfaces bounded by the same loop give
different answers: a small surface $C_1$ that the wire's conduction current pierces gives
$\oint \vec B\cdot d\vec l = \mu_0 I$, while a larger surface $C_2$ bulging through the capacitor
gap (where no conduction current crosses) gives $\oint \vec B \cdot d\vec l = 0$. Same loop, same
law, two different results -- and the same picture looks like it violates Kirchhoff's junction
rule too, since current flowing in at a point $P$ seems to vanish across the gap and reappear at
a point $Q$ on the other plate.

##### Displacement current and the modified Ampere-Maxwell law (NCERT 8.2)

Between the plates, $\Phi_E = \vec E\cdot\vec A = Q/\varepsilon_0$. As the current varies, the
charge on the plates -- and hence $\Phi_E$ -- changes with time. Outside the plates only
conduction current flows; inside the gap only **displacement current**,

$$I_d = \varepsilon_0\frac{d\Phi_E}{dt}$$

flows, with $I_c = I_d$. This gives the corrected, general Ampere-Maxwell law:

$$\oint \vec B \cdot d\vec l = \mu_0 I_c + \mu_0\varepsilon_0\frac{d\Phi_E}{dt} = \mu_0(I_c + I_d)$$

With displacement current in the picture, Kirchhoff's rule is no longer violated -- current just
outside $P$ is conduction current, current in the gap is displacement current, and the two are
equal, so the total current is continuous through the whole loop after all.

###### A symmetry worth noting
The lecture pauses here to connect this back to electromagnetic induction (Ch. 7): a
time-varying **magnetic** field generates an **electric** field (Faraday's law). The
displacement-current result just derived shows the converse also holds -- a time-varying
**electric** field generates a **magnetic** field. The two effects are symmetric/interchangeable,
which is part of why light (an oscillating $E$ and $B$ sustaining each other) can propagate
without a medium.

##### Maxwell's four equations (NCERT 8.2, boxed summary)

1. **Gauss's law of electrostatics:** $\oint \vec E\cdot d\vec s = Q/\varepsilon_0$
2. **Gauss's law of magnetostatics:** $\oint \vec B\cdot d\vec s = 0$
3. **Faraday's law of EMI:** $\text{emf} = -d\Phi/dt$, i.e. $\oint \vec E\cdot d\vec l = -d\Phi_B/dt$
4. **Modified Ampere-Maxwell law:** $\oint \vec B\cdot d\vec l = \mu_0\left(I_c + \varepsilon_0\dfrac{d\Phi_E}{dt}\right)$

Matches NCERT's boxed list in 8.2 exactly, same four laws and order. The board's final line for
this lecture -- "light is EM waves $\Rightarrow$ it consists of electric field and magnetic field
intensities" -- previews the chapter's next topic (NCERT 8.1's remark that Maxwell's predicted EM
wave speed matching light's speed is what identifies light itself as an electromagnetic wave).

##### A note on this lecture's transcript

Coverage checks report 103.5% and pass cleanly, but (as with lecture 01) that is misleading --
the transcript's real content cuts off mid-sentence while defining EMF, before the fourth
equation is explicitly re-stated in the summary and before the "light is EM waves" note. Both are
grounded from board frames only -- see the uncertain span below. Unlike lecture 01, though, this
transcript *does* narrate all four equations by name and formula, and derives displacement
current with a fully spoken formula, before that late cutoff -- so the gap here is much smaller
and confined to the closing recap.

##### Verify these spans
- [16:40–17:43] check_coverage() reports 103.5% coverage and passes cleanly (the last segment is timestamped 1036.5-1101.1s, overshooting the video's verified true duration of 1063.3s by ~38s) -- the same 'clean-looking but misleading' pattern seen in the companion lecture 01. The delayed-duplicate scanner found no repeated block here either (only one short flagged pair, segments 27 vs 30 at ratio 0.73, which is just the teacher naturally repeating the short phrase 'modified ampere circuited law' a few sentences apart, not a real loop). The transcript's actual content, however, cuts off mid-sentence while defining EMF from Faraday's law ('...we can also write EMF as...'). Two things past that cutoff are grounded from board frames only: the explicit restatement of Maxwell's 4th equation in the summary list (already independently derived and narrated earlier in the lecture, at ~610-655s, so this is a recap gap, not a missing-content gap), and the 'light is EM waves' bridging note, which is not spoken anywhere in the available transcript at all. Frame floor_000052 (t=1020s), close to the true end of the video, is a direct continuation of the same board page built up continuously from floor_000041 onward, so it is trusted as belonging to this lecture.

#### Hertz's Experiment

##### Hertz's experiment

*Not covered in the current NCERT textbook* -- included here as background on how electromagnetic waves were first produced and detected experimentally, since most EM waves (radio, TV, UV, X-rays, etc.) are invisible to the eye.

**Core idea:** an oscillating charge is an accelerated charge, and an accelerated charge radiates electromagnetic energy.

###### Apparatus
Two metal plates (copper or zinc), $60$ cm apart, connected via metal spheres $S_1$, $S_2$ with an air gap between them, fed by a high-voltage induction coil (several thousand volts).

###### Working
The very high potential difference ionizes the air gap between $S_1$ and $S_2$, making it briefly conducting — producing a spark, and hence an **oscillating current**. This oscillating current produces an oscillating magnetic field, which induces a large oscillating EMF at a separate detector (points $C$, $D$ on a nearby ring), itself large enough to produce a second spark there — with no direct wire connecting the two. This demonstrates that electromagnetic energy was **radiated through space** from $S_1$–$S_2$ and picked up at the detector.

###### Frequency
The two metal plates act as a capacitor ($C$); the connecting wires contribute a small inductance ($L$). The oscillator's frequency (and hence the radiated EM wave's frequency) is:
$$\nu = \frac{1}{2\pi\sqrt{LC}}$$

###### Detector orientation
The detector ring must be oriented so the oscillating magnetic field is **perpendicular to the plane of the ring** — this is what produces the large induced EMF (and visible spark) at $C$–$D$.

---
*Note on this lecture's transcript:* the explanation of why the detector sparks is transcribed once correctly, then repeated nearly verbatim a second time (~95s of this 682s lecture). The transcript's own final sentence is also cut off mid-word; its completion is grounded from a board frame.

##### Verify these spans
- [04:43–08:55] The explanation of why sparking occurs at the detector (oscillating current -> oscillating magnetic field -> large induced EMF between C and D -> detector spark, demonstrating radiated EM energy) is transcribed once (~t=283-378s) and then re-transcribed nearly verbatim a second time (~t=444-535s) -- a shorter instance of the delayed-repetition pattern found throughout this project. No content appears to have been lost here (the two passes say the same thing), but roughly 95 of this short lecture's 682 seconds are duplicated explanation rather than new material.
- [11:10–11:22] The transcript's own final segment cuts off mid-sentence ('...such that the magnetic field produced by oscillating current'). A board frame (floor_000030.jpg) shows the completed sentence: the detector ring is held such that the oscillating magnetic field is perpendicular to the plane of the ring, which is what produces the large induced EMF across C and D. The detector-orientation claim above completes this from the frame.

#### Sources, Properties, and Equation of Electromagnetic Waves

**NCERT sections covered:** 8.3, 8.4

##### Sources of electromagnetic waves (NCERT 8.3)

A stationary charge produces only an electric field; a charge moving at constant velocity produces a time-independent magnetic field. An **accelerated** charge (non-uniform velocity) is a source of EM waves — its E and B fields vary with time. An oscillating LC circuit is one way to produce EM waves (the capacitor's charge varies with time, i.e. is being accelerated).

##### Properties of electromagnetic waves (NCERT 8.3)

1. **Transverse** in nature.
2. Frequency of the EM wave = frequency of its source.
3. Energy of the wave comes **at the expense of the source's energy**.
4. Travel through vacuum at the **speed of light**, $c$.
5. **Electrically neutral** — not made of charged particles, so NOT deflected by electric or magnetic fields.
6. Show ordinary wave phenomena: reflection, refraction, interference, diffraction, polarization.

##### Field relations and energy (NCERT 8.4)

$$c = \frac{E_0}{B_0}$$
In a medium: $v = \dfrac{1}{\sqrt{\mu\varepsilon}}$; in vacuum, $c=\dfrac{1}{\sqrt{\mu_0\varepsilon_0}}$.

**Equal energy density:** $U_E = U_M$ everywhere in an EM wave. Total energy density $U=U_E+U_M$ (expressible via $\varepsilon_0 E^2$).

##### Momentum and radiation pressure

EM waves carry momentum as well as energy, so they exert **radiation pressure**. If total energy $U$ is transferred to a surface (fully absorbed) in time $t$:
$$p = \frac{U}{c}$$

**Example:** sunlight on your hand — you feel the energy (warmth), but the momentum transferred is imperceptibly small (since $c$ is so large).

**Importance:** carrying energy from one place to another — radio/TV signals, and light carrying energy from the Sun to the Earth.

**Historical note:** the best modern electronic oscillator circuits reach only $\sim10^{11}$ Hz, far below visible light's frequency — so light's electromagnetic nature couldn't be demonstrated the same way Hertz demonstrated radio waves.

##### Equation of an electromagnetic wave (NCERT 8.3)

$E$, $B$, and the direction of propagation are mutually perpendicular. For propagation along $x$, $E$ along $y$, $B$ along $z$:
$$E_y = E_0\sin(\omega t - kx), \qquad B_z = B_0\sin(\omega t - kx), \qquad k=\frac{2\pi}{\lambda}$$
Direction of propagation given by $\hat E\times\hat B$ (e.g. $\hat\jmath\times\hat k=\hat\imath$).

---
*Note on this lecture's transcript:* properties, field-magnitude ratio, energy density, and momentum/radiation-pressure are all transcribed cleanly. However, the "equation of EM waves" half of this lecture's own title — the explicit sinusoidal $E_y$/$B_z$ component equations and the propagation-direction rule — never appears anywhere in the transcript at all, despite being clearly present on the board near the end of the true video. Grounded entirely from frames; see the flagged span below.

##### Verify these spans
- [27:40–30:18] Board frames (floor_000084.jpg, floor_000088.jpg, both within the video's true 1818.37s duration) show a substantial 'Propagation of EM waves' section -- explicit sinusoidal component equations for E and B (Ey=E0*sin(omega*t-kx), Bz=B0*sin(omega*t-kx)), the propagation constant k=2*pi/lambda, and the cross-product rule for the direction of propagation -- that never appears anywhere in the available transcript at all, despite the lecture's own title explicitly naming 'equation of EM waves' as a topic (the transcript covers only the qualitative 'properties' half of the title). Given the frames' timestamps are near the very end of the true video duration while the transcript's own final words are on a different topic (comparing oscillator vs. visible-light frequency), this content was most likely taught near the end of the lecture but never captured by the ASR at all -- a total omission rather than a timestamp-drift artifact, since no transcript segments reference it anywhere. This whole claim is grounded entirely from the frames.

#### Electromagnetic Spectrum: Production and Uses of EM Waves

**NCERT sections covered:** 8.5

##### The electromagnetic spectrum (NCERT 8.5)

Ordered by wavelength around the visible range ($\approx400$–$700$ nm):

| Band | Wavelength range |
|---|---|
| Radio waves | $0.3$ m – $10^5$ m |
| Microwaves | $1$ mm – $0.3$ m |
| Infrared | $700$ nm – $1$ mm |
| **Visible** | $400$ nm – $700$ nm |
| UV | $10$ nm – $400$ nm |
| X-rays | $1$ Å – $100$ Å |
| Gamma rays | $10^{-3}$ Å – $1$ Å |

No sharp boundaries — adjacent bands overlap, and cited boundary values vary slightly by source. Moving from visible toward shorter wavelength, frequency increases; toward longer wavelength, frequency decreases. (Common exam question: arrange given radiation types in ascending/descending order of frequency.)

###### Production and uses, band by band

**Radio waves** — produced by accelerated charges in a conducting wire. Radio/TV communication: AM band $500$–$1710$ kHz, TV $\approx54$–$890$ MHz, FM band $88$–$108$ MHz; mobile phones use even higher (ultra-high) frequencies.

**Microwaves** — produced by klystrons/magnetrons. Used in **radar** (short wavelength $\Rightarrow$ high energy, good directionality, minimal diffraction, straight-line travel) and **microwave ovens** (frequency tuned to water molecules' resonant frequency for efficient energy transfer, heating food).

**Infrared** — produced by hot bodies/molecules; also called *heat waves* (water molecules readily absorb IR, raising thermal motion). Used in physiotherapy lamps, remote controls. Also explains the **greenhouse effect**: incoming solar UV/energy is absorbed and re-radiated as IR, which greenhouse gases (CH$_4$, H$_2$O, CO$_2$) trap in the atmosphere, warming the surface (analogous to a closed car heating in sunlight).

**Visible light** — produced by lamps, ionized gases. Lets us see objects (light emitted/reflected carries information about the world); also used to study molecular structure and electron arrangement.

**UV rays** — produced by special lamps and very hot bodies (the Sun). Used in LASIK eye surgery, water purification (killing germs), detecting forged documents/fingerprints. **Caution:** ozone-layer depletion by CFCs is a concern, since ozone normally filters harmful UV.

**X-rays** — produced by high-energy electrons bombarding a heavy metal target (Coolidge tube). Used diagnostically in medicine, in cancer treatment, and in scientific research (revealing molecular structure) — exposure kept brief since prolonged exposure harms healthy cells.

**Gamma rays** — wavelength $<10^{-3}$ nm, the highest-energy band; produced in nuclear reactions/emitted by radioactive nuclei. Used in medicine to destroy cancer cells, to study atomic nuclei, and (due to their high energy) to induce nuclear reactions.

---
*Note on this lecture's transcript:* this is an exceptionally clean and thorough transcript, covering radio through X-rays in full detail. The one gap is the gamma-rays uses section — the lecture opens by promising to cover production *and* uses for every band, and a board frame confirms the gamma-rays uses were written out (alongside X-rays) within the true video duration, but the transcript's own words never reach this content. Grounded from that frame; see the flagged span below.

*This lecture exists as two byte-identical duplicate files in the source library (confirmed via matching SHA-256 hashes); only one copy was transcribed and noted.*

##### Verify these spans
- [36:40–39:10] The transcript's own words, right up through their final available segment, cover only the wavelength range, production method, and uses of X-rays -- despite the lecture opening (t=5s) explicitly promising to cover production and uses for ALL bands including gamma rays, and despite gamma rays being introduced (briefly, as produced by nuclear reactions) at the very start. A board frame (floor_000116.jpg), whose true video timestamp (t=2300s) falls before the video's true 2350.27s duration, shows a full 'gamma rays' section already written alongside the X-rays section: wavelength <10^-3 nm, produced in nuclear reactions / emitted by radioactive nuclei, and used in medicine to destroy cancer cells, to study atomic nuclei, and to produce nuclear reactions. None of this gamma-ray-uses content appears in the transcript's own words at all -- it is grounded entirely from this frame.

### Ray Optics to 9.4

*Chapter 9 · Ray Optics — 9 marks. Source: published page `b7ff23a3-c455-4f36-a2ff-f2896f06c23b`. Maths on this page is plain text, not KaTeX — it predates the KaTeX pipeline. The eighteen Ray Optics lectures have never been transcribed, so this page and the Chapter 9 sections of **Physics, Derived** and **Every Physics Formula** were written from NCERT rather than from class.*

> **Scope.** Ends at Section 9.4. Total internal reflection and its applications are the last thing on the paper — lenses, prisms, dispersion and optical instruments are all off it.

#### 01 · Theory

##### 1 · Spherical mirrors — the words and the sign convention

A spherical mirror is a slice cut from a hollow sphere, silvered on one side. Silver the bulging side and the reflecting face is hollow — **concave**. Silver the hollow side and the reflecting face bulges out — **convex**.

- **Pole (P)** — the centre of the reflecting surface.
- **Centre of curvature (C)** — the centre of the sphere the mirror was cut from.
- **Radius of curvature (R)** — the distance PC.
- **Principal axis** — the line PC.
- **Principal focus (F)** — where rays parallel to the axis meet after reflection (concave), or appear to come from (convex).
- **Focal length (f)** — the distance PF, and for a small aperture `f = R/2`.

Both laws of reflection hold at every point: the angle of incidence equals the angle of reflection, and incident ray, reflected ray and normal lie in one plane. The normal at any point of a spherical mirror is the radius drawn to that point. Reflection changes neither wavelength nor frequency.

**New Cartesian sign convention** — write this out before every numerical:

- All distances are measured from the pole P.
- Distances measured along the incident light are **positive**; against it, **negative**. A real object is always on the incoming side, so `u` is negative.
- Heights above the principal axis are positive, below it negative.
- Consequence: concave mirror `f` negative, convex mirror `f` positive.

##### 2 · Refraction, Snell's law, refractive index

Light entering a new transparent medium changes speed, and if it meets the surface obliquely it changes direction too. That bending is refraction.

- Incident ray, refracted ray and normal lie in one plane.
- **Snell's law:** `sin i / sin r` is a constant for a given pair of media and a given wavelength. That constant is `₁n₂ = n₂/n₁`, the refractive index of medium 2 with respect to medium 1.

The **absolute refractive index** of a medium is `n = c/v` — speed of light in vacuum divided by speed in the medium. Since frequency is fixed by the source and does not change on crossing a boundary, `v = νλ` forces the wavelength to shrink in the denser medium, so `n = λ_air / λ_medium` as well.

Denser to rarer, the ray bends *away* from the normal; rarer to denser, *towards* it. Reversing the light gives `₂n₁ = 1/₁n₂`, and going round a chain of media brings you back to 1: `ₐn_w × _wn_g × _gn_a = 1`. Light passing through a parallel-sided slab emerges parallel to its original direction, only shifted sideways.

*Some questions write μ instead of n. Same quantity.*

##### 3 · Total internal reflection

Send light from a denser medium towards a rarer one and it bends away from the normal, so the refracted ray leans further from the normal than the incident ray does. Push the angle of incidence up and the refracted ray eventually grazes along the surface at 90°. The angle of incidence that does this is the **critical angle C**.

**Definition to write:** the critical angle for a pair of media is the angle of incidence in the denser medium for which the angle of refraction in the rarer medium is 90°.

Beyond C there is no angle of refraction left to have, so no light crosses the boundary at all — the surface behaves as a perfect mirror and every bit of the light is reflected back into the denser medium. That is **total internal reflection**.

**The two conditions** (state both, always):

- Light must travel from the denser medium towards the rarer one.
- The angle of incidence in the denser medium must exceed the critical angle for that pair.

It is genuinely total — unlike an ordinary silvered mirror there is no absorbed fraction, so no energy is lost.

##### 4 · Where total internal reflection is used

- **Optical fibre** — a thin core of glass or quartz (n ≈ 1.7) clad in a coating of lower index (n ≈ 1.5). Light entering one end at a small angle to the axis strikes the core–cladding wall well above the critical angle, is totally reflected, strikes the far wall, is totally reflected again, and so zig-zags the whole length of the fibre without leaking out. Used to carry telephone and internet signals over long distances, and in endoscopy.
- **Mirage** — on a hot road the air near the surface is hot and rarer, the air above cooler and denser. Light from the sky travelling downwards passes from denser to rarer layers, bending away from the vertical at each layer until it exceeds the critical angle and turns back upwards. The eye traces it back to the ground and sees an inverted patch of sky, read as water.
- **Brilliance of diamond** — diamond's critical angle is only about 24°, so light entering a cut stone strikes face after face above that angle and is trapped through many total reflections before finding a face it can leave by, emerging concentrated.
- **Totally reflecting prisms** — a right-angled isosceles glass prism has a critical angle near 42°, so light striking the hypotenuse at 45° is totally reflected. Used to turn a beam through 90°, through 180°, or to invert an image in binoculars and periscopes.
- **Air bubble in water** shines for the same reason — light going from water into the rarer air of the bubble is totally reflected.

##### 5 · Image formation by spherical mirrors

Two of these three rays fix the image: a ray parallel to the axis reflects through F; a ray through F reflects parallel to the axis; a ray through C returns along itself.

| Mirror & object at | Image position | Nature | Size |
|---|---|---|---|
| Concave — infinity | At F | Real, inverted | Point-sized |
| Concave — beyond C | Between F and C | Real, inverted | Diminished |
| Concave — at C | At C | Real, inverted | Same size |
| Concave — between C and F | Beyond C | Real, inverted | Enlarged |
| Concave — at F | At infinity | Real, inverted | Highly enlarged |
| Concave — between F and P | Behind the mirror | Virtual, erect | Enlarged |
| Convex — anywhere | Between P and F, behind | Virtual, erect | Diminished |

A convex mirror gives a virtual erect diminished image wherever the object is put, which is why it is the driver's side mirror — a wide field of view, at the cost of making everything look further away. A concave mirror is the shaving mirror and the dentist's mirror, used inside its focus where the image is virtual, erect and magnified.

*Covering the lower half of a mirror does not cut the image in half. The rays from every point still reach the top half, so the whole image is still formed — only fewer rays arrive, so it is fainter.*

#### 02 · Derivations

##### D1 · Mirror formula, concave mirror

> Concave mirror with pole P, focus F, centre of curvature C. Object AB stands on the principal axis beyond C, B on the axis. A real inverted image A′B′ is formed. A ray AD from the top of the object runs parallel to the axis, strikes the mirror at D and reflects through F. DN is the perpendicular dropped from D onto the principal axis. Aperture is small.

1. In △ABC and △A′B′C: ∠ABC = ∠A′B′C = 90°
2. ∠ACB = ∠A′CB′ — *(vertically opposite)*
3. △ABC ~ △A′B′C
4. AB / A′B′ = BC / B′C …(i)
5. In △DNF and △A′B′F: ∠DNF = ∠A′B′F = 90°
6. ∠DFN = ∠A′FB′ — *(vertically opposite)*
7. △DNF ~ △A′B′F
8. DN / A′B′ = NF / B′F
9. DN = AB — *(DN is the height of the parallel ray = height of object)*
10. AB / A′B′ = NF / B′F …(ii)
11. From (i) and (ii): BC / B′C = NF / B′F
12. Aperture small ⇒ N lies very close to P ⇒ NF = PF
13. BC / B′C = PF / B′F
14. BC = PB − PC, B′C = PC − PB′, B′F = PB′ − PF
15. (PB − PC) / (PC − PB′) = PF / (PB′ − PF)
16. Sign convention: PB = −u, PB′ = −v, PF = −f, PC = −R = −2f
17. (−u + 2f) / (−2f + v) = (−f) / (−v + f)
18. (−u + 2f)(−v + f) = (−f)(−2f + v) — *(cross-multiplying)*
19. uv − uf − 2fv + 2f² = 2f² − fv
20. uv − uf − 2fv = −fv
21. uv − uf − 2fv + fv = 0
22. uv − uf − fv = 0
23. uv = uf + fv
24. uv / uvf = uf / uvf + fv / uvf — *(divide throughout by uvf)*
25. 1/f = 1/v + 1/u

**Result:** 1/v + 1/u = 1/f

**Diagram:** concave mirror on the right, axis horizontal, C and F marked with C further from P. Object arrow AB beyond C pointing up; image arrow A′B′ between C and F pointing down. Show ray AD parallel to the axis reflecting through F, and the second ray from A through C returning on itself. Mark u, v, f from P.

##### D2 · Magnification for a spherical mirror

> Same concave mirror, same object AB of height h giving a real inverted image A′B′ of height h′. Take the ray that leaves the top of the object A and strikes the mirror exactly at the pole P. At P the principal axis is the normal, so this ray reflects to A′ with the angle of reflection equal to the angle of incidence.

1. Linear magnification m = h′ / h — *(height of image ÷ height of object, both signed)*
2. Ray AP strikes the pole at angle i to the axis; reflected ray PA′ leaves at angle r
3. i = r — *(law of reflection; axis is the normal at P)*
4. In right △ABP: tan i = AB / BP = h / |u|
5. In right △A′B′P: tan r = A′B′ / B′P = |h′| / |v|
6. i = r ⇒ tan i = tan r
7. h / |u| = |h′| / |v|
8. |h′| / h = |v| / |u| …(i)
9. Sign convention: u < 0, v < 0, h > 0, h′ < 0 — *(real image, inverted)*
10. |u| = −u, |v| = −v, |h′| = −h′
11. Substituting in (i): (−h′) / h = (−v) / (−u)
12. (−h′) / h = v / u
13. h′ / h = −v / u
14. m = −v / u
15. From D1: 1/v = 1/f − 1/u = (u − f) / uf
16. v = uf / (u − f)
17. m = −v/u = −[uf / (u − f)] / u = −f / (u − f)
18. m = f / (f − u)
19. From D1 again: 1/u = 1/f − 1/v = (v − f) / vf
20. u = vf / (v − f)
21. m = −v/u = −v(v − f) / vf = −(v − f) / f
22. m = (f − v) / f

**Result:** m = h′/h = −v/u = f/(f − u) = (f − v)/f

**Diagram:** the same figure as D1, with the extra ray drawn from A to the pole P and reflected down to A′, and the equal angles i and r marked on either side of the axis at P.

*Reading m: negative m means a real inverted image; positive m means a virtual erect one. |m| > 1 enlarged, |m| < 1 diminished.*

##### D3 · Real depth and apparent depth at a plane surface

> An object O lies at a depth t below the flat surface of a denser medium of refractive index n (water in a tank, or a pin under a glass slab), viewed from air almost vertically above. A ray OM leaves O along the normal and passes straight out at M. A second ray OP leaves at a small angle of incidence i, meets the surface at P and refracts away from the normal into air at angle r. Extended backwards, the two emergent rays meet at I.

1. I is the virtual image of O, so real depth = OM = t and apparent depth = IM
2. In right △OMP: tan i = MP / OM
3. In right △IMP: tan r = MP / IM
4. Snell's law, denser → air: sin r / sin i = n
5. Viewed nearly vertically, P lies close to M, so i and r are small
6. sin i ≈ tan i and sin r ≈ tan r — *(small-angle approximation)*
7. n = tan r / tan i
8. n = (MP / IM) ÷ (MP / OM)
9. n = (MP / IM) × (OM / MP)
10. n = OM / IM
11. n = real depth / apparent depth
12. Apparent depth IM = OM / n = t / n
13. Apparent shift x = OM − IM = t − t/n
14. x = t (1 − 1/n)

**Result:** n = real depth / apparent depth · x = t (1 − 1/n)

**Diagram:** horizontal water line; O at depth t below M; the normal ray OM straight up; a slanted ray OP refracting away from the normal at P; both emergent rays dashed backwards to meet at I, which sits above O. Mark t, the apparent depth, and the shift x.

*Because n depends on the medium only, the shift does not depend on where the slab sits between the object and the eye.*

##### D4 · Critical angle and total internal reflection

> A ray travels inside a denser medium of refractive index n_d and meets a plane boundary with a rarer medium of refractive index n_r, at angle of incidence i. Steps 1–2 are the same Snell's-law starting point as D3 — the difference is that there the small angle was tracked, here the largest one is.

> **Shared setup:** D3 and D4 both begin from Snell's law applied once at a plane surface. If you can set up one, you can set up the other.

1. Snell's law at the boundary: n_d sin i = n_r sin r
2. sin r = (n_d / n_r) sin i
3. n_d > n_r ⇒ n_d/n_r > 1 ⇒ sin r > sin i ⇒ r > i — *(bends away from the normal)*
4. As i increases, r increases faster and reaches 90° first
5. The value of i for which r = 90° is defined as the critical angle C
6. Put i = C, r = 90° in step 1: n_d sin C = n_r sin 90°
7. sin 90° = 1
8. n_d sin C = n_r
9. sin C = n_r / n_d
10. If the rarer medium is air: n_r = 1 and n_d = n
11. sin C = 1 / n
12. C = sin⁻¹ (1 / n)
13. Now take i > C. From step 2: sin r = (n_d/n_r) sin i
14. sin i > sin C ⇒ (n_d/n_r) sin i > (n_d/n_r) sin C
15. (n_d/n_r) sin C = 1 — *(from step 9)*
16. sin r > 1
17. No angle r satisfies sin r > 1, so no refracted ray can exist
18. All the incident energy returns into the denser medium — total internal reflection

**Result:** sin C = n_r/n_d = 1/n · C = sin⁻¹(1/n), and TIR for i > C

**Diagram:** one horizontal boundary, denser medium below. Draw three rays from the same point O on the surface: i < C refracting into the rarer medium; i = C with the refracted ray grazing along the boundary at 90°; i > C reflecting back into the denser medium with the reflected angle equal to i.

*n is larger for violet than for red, so C is smallest for violet — violet is totally reflected before red is.*

#### 03 · Formula strip

*● must be instant · ○ a few seconds is fine*

##### ● Focal length of a spherical mirror in terms of its radius of curvature

`f = R / 2` — f = focal length, R = radius of curvature. Both in metre (m). Holds for small aperture, concave and convex alike.

##### ● Mirror formula

`1/v + 1/u = 1/f` — u = object distance, v = image distance, f = focal length, all measured from the pole and all in metre (m). Signed by the New Cartesian convention.

##### ● Linear magnification of a mirror, in terms of u and v

`m = h′/h = −v/u` — h′ = image height, h = object height (both m). m is a pure number, no unit. Negative m = real and inverted.

##### ○ Magnification of a mirror written with f instead of a height

`m = f/(f − u) = (f − v)/f` — same m, no unit. Use whichever of u or v the question gives you.

##### ● Snell's law, in ratio form and in the n-on-both-sides form

`sin i / sin r = ₁n₂ = n₂/n₁ ⟺ n₁ sin i = n₂ sin r` — i = angle of incidence, r = angle of refraction (degree). n₁, n₂ = absolute refractive indices, no unit.

##### ● Absolute refractive index in terms of speed

`n = c / v` — c = speed of light in vacuum = 3 × 10⁸ m s⁻¹, v = speed in the medium (m s⁻¹). n has no unit and is never less than 1.

##### ○ Refractive index in terms of wavelength — and what stays fixed

`n = λ_air / λ_medium` — λ in metre (m). Frequency ν (hertz, Hz) is unchanged on refraction; the wavelength shortens in the denser medium.

##### ○ Principle of reversibility, as an equation

`₁n₂ = 1 / ₂n₁` — both sides dimensionless. Swapping the two media inverts the refractive index.

##### ○ Chain rule for three media in succession

`ₐn_w × _wn_g × _gn_a = 1` — air → water → glass → air. Also gives `_wn_g = ₐn_g / ₐn_w`. Dimensionless.

##### ● Refractive index from real and apparent depth

`n = real depth / apparent depth` — both depths in metre (m); n dimensionless. Applies for near-normal viewing only.

##### ● Apparent shift produced by a slab of thickness t

`x = t (1 − 1/n)` — t = real thickness or depth, x = shift, both in metre (m). Independent of where the slab is placed.

##### ● Critical angle for a denser medium against air

`sin C = 1/n ⇒ C = sin⁻¹(1/n)` — C in degree. n = refractive index of the denser medium w.r.t. air, dimensionless.

##### ○ Critical angle for any two media

`sin C = n_r / n_d` — n_r = rarer medium, n_d = denser medium, both dimensionless. Reduces to 1/n when the rarer medium is air.

##### ○ Radius of the circle of light escaping from a source at depth H

`r = H tan C = H / √(n² − 1)` — H = depth of the source, r = radius of the bright circle at the surface, both in metre (m). Area escaping = πr².

##### ○ Speed of light inside a medium of index n

`v = c / n` — v in m s⁻¹. Combine with n = real/apparent depth to get v straight from a depth measurement.

#### 04 · Questions to attempt

*Question numbers only, from Xam Idea Chapter 9 and the NCERT questions reprinted inside it. Section names are Xam Idea's own.*

##### Tier 1 — must do

*15 questions · these are the 3-mark and 5-mark slots*

| Question | Page | Why |
|---|---|---|
| Long Answer Q1 | p. 344 | The 5-marker |
| Practice Q40 | p. 362 | Same derivation |
| Short Answer Q1 | p. 331 | Full TIR set |
| Short Answer Q2 (a) | p. 331 | Reasoning from formula |
| Short Answer Q7 | p. 334 | Optical fibre, guaranteed |
| Short Answer Q10 | p. 335 | Two sign cases |
| Short Answer Q11 | p. 336 | Two-equation chain |
| Very Short Ans Q19 | p. 324 | Proves f = R/2 |
| Very Short Ans Q4 | p. 319 | Definition plus geometry |
| Very Short Ans Q2 | p. 318 | Two mirror equations |
| NCERT Q15 | p. 298 | All mirror cases |
| NCERT Q17 | p. 299 | Fibre, full numerical |
| NCERT Q5 | p. 294 | Critical-angle cone |
| NCERT Q3 | p. 293 | Real versus apparent |
| Practice Q5 | p. 359 | Conditions plus graph |

##### Tier 2 — if time

*extra pattern coverage, mostly 1 and 2 marks*

| Question | Page | Why |
|---|---|---|
| MCQ 2, 13, 14, 15 | p. 307–308 | TIR one-markers |
| MCQ 7, 12 | p. 308 | Index from depth, speed |
| MCQ 9, 10 | p. 308 | Mirror one-markers |
| Case-based Q4 (i)–(iv) | p. 313 | Whole TIR case study |
| Case-based Q2 (i) | p. 312 | The R/H result |
| NCERT Q1, Q2 | p. 293 | Plain mirror drills |
| NCERT Q4, Q16 | p. 293, 299 | Snell chain, slab shift |
| NCERT Q30 | p. 306 | Mirror turns, ray turns 2θ |
| Very Short Ans Q12 | p. 322 | Snell in a sphere |
| Practice Q12, Q26 | p. 360, 361 | Half-mirror reasoning |
| Practice Q14, Q22, Q24, Q33 | p. 360–361 | Mirror numericals |
| Practice Q25 | p. 361 | Why convex is virtual |
| Practice Q6, Q31 | p. 359, 361 | Index, speed, wavelength |

##### Tier 3 — skip unless revising

*out of scope, or right physics in a banned frame*

**Off the syllabus entirely — do not open:** NCERT `Q6–Q14, Q18–Q29, Q31`. MCQ `3, 4, 5, 6, 8, 11, 16–27`. Very Short Answer `Q1, Q3, Q5–Q10, Q13–Q18, Q20–Q34, Q36`. Short Answer `Q2(b), Q3, Q4, Q5, Q6, Q8, Q9, Q12, Q13`. Long Answer `Q2–Q12` — every one of them is a lens, prism or instrument derivation. Case-based `Q1, Q3`. Practice `1(ii)–(v), 2, 3, 4, 8, 9, 10, 11, 13, 15, 17–21, 23, 27–30, 32, 34, 36–39`.

**Correct TIR physics wearing a prism, so the setup is unexaminable:** NCERT `Q21`, Very Short Answer `Q35, Q37`, Practice `Q7, Q16, Q35`. Read them only if you have finished Tiers 1 and 2 and want more critical-angle practice.

##### The five numerical types this chapter can ask

1. **Find the image of an object in a spherical mirror** — `1/v + 1/u = 1/f` (then m = −v/u)
2. **Object or mirror moved, or two positions giving the same magnification** — `m = −v/u`, with f = R/2 fixed
3. **Depth of a coin, pin or needle seen through water or a slab** — `n = real depth / apparent depth` (shift x = t(1 − 1/n))
4. **Onset of total internal reflection — fibre, tank, diamond, bubble** — `sin C = 1/n`
5. **Bending, speed or wavelength across one interface or a stack** — `n₁ sin i = n₂ sin r`, with n = c/v = λ_air/λ_medium

### Alternating Current in Eight Derivations

*Chapter 7 · Alternating Current — inside the 16-mark unit shared with EMI. Source: published page `1e4833b5-4f5c-490c-8b6f-b9bf9a3e972c`. Plain-text maths, not KaTeX. Its eight derivations against the five (PD33–PD37) in **Physics, Derived**; this page also carries the theory, formula strip and question tiers.*

> **Scope.** No scope cut. Eight derivations, and this is the chapter most likely to supply a five-mark question on the paper.

#### 01 · Theory

##### 1 · Alternating current, mean value, rms value

An alternating current reverses direction periodically and varies in magnitude continuously, written `i = i₀ sin ωt` with a matching voltage `v = v₀ sin ωt`. Here `i₀` is the peak value or current amplitude, `ω = 2πν` the angular frequency.

Averaged over a **complete** cycle the current is zero — the negative half exactly cancels the positive half. That is why a moving-coil ammeter reads nothing on ac. Over **half** a cycle the average is not zero:

- Mean over half a cycle: `i_mean = 2i₀/π = 0.637 i₀`

Because the average is useless, ac is described by its **root mean square** value — the steady direct current that would produce the same heating in the same resistance over the same time. Since heating goes as `i²`, and the mean of `sin²ωt` over a cycle is `½`:

- `I_rms = i₀/√2 = 0.707 i₀` and `V_rms = v₀/√2 = 0.707 v₀`

Every ac meter reads rms, and every stated supply voltage — the 220 V mains — is an rms value. Its peak is 220√2 ≈ 311 V.

##### 2 · Reactance, impedance, power factor

- **Reactance** is the opposition offered by an inductor or a capacitor alone. Inductive reactance `X_L = ωL`, capacitive reactance `X_C = 1/ωC`. Both in ohm.
- **Impedance Z** is the total opposition of a circuit containing resistance and reactance together, `Z = V_rms/I_rms`, in ohm.
- **Phase angle φ** is the angle by which the current leads or lags the applied voltage.
- **Power factor** is `cos φ = R/Z`, a pure number between 0 and 1. It is the fraction of the apparent power `V_rms I_rms` that is actually consumed.

Reactance differs from resistance in one crucial way: a resistor dissipates energy, a pure reactance does not. Over one cycle an inductor returns to the source exactly the energy it took, and so does a capacitor. That is why a purely reactive circuit consumes zero power however large the current.

##### 3 · The three single elements side by side

| Element | Opposition | Phase of current | Against frequency | Power |
|---|---|---|---|---|
| Resistor R | R, constant | In phase with V | Independent of ν | V_rms I_rms |
| Inductor L | X_L = ωL | Lags V by π/2 | Straight line through origin | Zero |
| Capacitor C | X_C = 1/ωC | Leads V by π/2 | Rectangular hyperbola | Zero |

A memory hook the examiner expects you to use correctly: **CIVIL** — in a **C**apacitor **I** comes before **V**; **V** comes before **I** in an inductor **L**.

Two consequences worth knowing as one-liners: a capacitor blocks dc (at `ν = 0`, `X_C = ∞`) but passes ac; an inductor passes dc freely (at `ν = 0`, `X_L = 0`) but chokes ac, which is what a choke coil is for.

##### 4 · Resonance and sharpness

In a series LCR circuit `X_L` rises with frequency and `X_C` falls, so at one frequency they are equal and cancel. There the impedance collapses to its smallest possible value, `Z = R`, the current reaches its largest possible value `v₀/R`, and voltage and current come into phase. That is **resonance**, at `ω₀ = 1/√(LC)`.

Resonance only exists if both L and C are present — with one of them missing there is nothing to cancel.

**Sharpness** is how quickly the current falls away on either side of `ω₀`. It is measured by the quality factor

- `Q = ω₀L/R = (1/R)√(L/C) = ω₀/(ω₂ − ω₁)`, where ω₁ and ω₂ are the half-power frequencies at which the current has dropped to `1/√2` of its peak.

Smaller R means larger Q, a taller and narrower peak, and a circuit that responds to a narrower band of frequencies — which is exactly what tuning a radio to one station requires.

##### 5 · Transformer, and why transmission uses high voltage

A transformer changes an alternating voltage up or down. It works on **mutual induction**: alternating current in the primary sets up a changing flux in a shared soft-iron core, and that changing flux induces an alternating emf of the same frequency in the secondary. It cannot work on dc, because a steady current makes no changing flux.

The transmission argument, which is asked directly:

- A power station must deliver a fixed power `P = VI` down a line of resistance R.
- The heat wasted in the line is `I²R`.
- For a fixed P, stepping the voltage up divides the current by the same factor.
- Since the loss goes as `I²`, ten times the voltage means a hundredth of the loss.
- So a step-up transformer at the generating end raises the voltage for the journey, and step-down transformers at the consumer end bring it back to 220 V.

*A step-up transformer does not create energy. Raising the voltage lowers the current by the same factor, so `V_P I_P = V_S I_S` still holds.*

#### 02 · Derivations

##### D1 · AC through a pure resistor

> A source of alternating voltage `v = v₀ sin ωt` is connected across a pure resistance R, with no inductance or capacitance in the circuit.

1. v = v₀ sin ωt
2. Kirchhoff's loop rule: v − iR = 0
3. i = v / R
4. i = (v₀ sin ωt) / R
5. i = (v₀/R) sin ωt
6. Compare with i = i₀ sin(ωt + φ)
7. i₀ = v₀ / R and φ = 0
8. φ = 0 ⇒ current and voltage are in phase
9. i² = i₀² sin²ωt
10. Mean of sin²ωt over one full cycle = 1/2
11. Mean of i² = i₀² / 2
12. I_rms = √(i₀²/2) = i₀/√2 = 0.707 i₀
13. Likewise V_rms = v₀/√2
14. Dividing: V_rms / I_rms = (v₀/√2) / (i₀/√2) = v₀/i₀ = R
15. Instantaneous power p = vi = (v₀ sin ωt)(i₀ sin ωt)
16. p = v₀ i₀ sin²ωt
17. Average over a cycle: P = v₀ i₀ × (1/2)
18. P = (v₀/√2)(i₀/√2)
19. P = V_rms I_rms

**Result:** i = (v₀/R) sin ωt, φ = 0 · I_rms = i₀/√2 · P = V_rms I_rms

**Graph and phasor:** v and i are sine curves that cross zero together and peak together. On the phasor diagram V₀ and i₀ lie along the same line, angle between them zero.

##### D2 · AC through a pure inductor — X_L = ωL

> The same source `v = v₀ sin ωt` across a coil of pure self-inductance L with negligible resistance.

1. v = v₀ sin ωt
2. Induced back emf in the coil: ε = −L di/dt
3. Kirchhoff's loop rule: v + ε = 0
4. v − L (di/dt) = 0
5. L (di/dt) = v₀ sin ωt
6. di/dt = (v₀/L) sin ωt
7. di = (v₀/L) sin ωt dt
8. ∫di = (v₀/L) ∫ sin ωt dt
9. i = (v₀/L) (−cos ωt / ω) + constant
10. The source has no steady component, so the constant of integration = 0
11. i = −(v₀/ωL) cos ωt
12. −cos ωt = sin(ωt − π/2)
13. i = (v₀/ωL) sin(ωt − π/2)
14. Compare with i = i₀ sin(ωt − π/2): i₀ = v₀ / (ωL)
15. Compare with i₀ = v₀ / X_L
16. X_L = ωL = 2πνL
17. Phase of current = ωt − π/2; phase of voltage = ωt
18. Current phase is behind voltage phase by π/2

**Result:** X_L = ωL = 2πνL · i = i₀ sin(ωt − π/2) · current lags V by π/2

**Graph and phasor:** X_L against ν is a straight line through the origin. On the phasor diagram V₀ points up and i₀ is 90° clockwise behind it. On the v–i time graph the current curve peaks a quarter cycle after the voltage curve.

##### D3 · AC through a pure capacitor — X_C = 1/ωC

> The same source `v = v₀ sin ωt` across a capacitor of capacitance C.

> **Shared setup:** this is derivation 2 with one substitution. Step 1 is identical, steps 12–18 of D2 map one-to-one onto steps 8–13 here, and the boxed result has the same shape. The only real difference: the inductor needs an *integration* and the capacitor a *differentiation*, and that flips the sign of the π/2.

1. v = v₀ sin ωt
2. Charge on the capacitor at any instant: q = Cv
3. q = C v₀ sin ωt
4. i = dq/dt
5. i = d/dt (C v₀ sin ωt)
6. i = C v₀ ω cos ωt
7. i = [v₀ / (1/ωC)] cos ωt
8. cos ωt = sin(ωt + π/2)
9. i = [v₀ / (1/ωC)] sin(ωt + π/2)
10. Compare with i = i₀ sin(ωt + π/2): i₀ = v₀ / (1/ωC)
11. Compare with i₀ = v₀ / X_C
12. X_C = 1/ωC = 1/(2πνC)
13. Current phase (ωt + π/2) is ahead of voltage phase (ωt) by π/2

**Result:** X_C = 1/ωC = 1/(2πνC) · i = i₀ sin(ωt + π/2) · current leads V by π/2

**Graph and phasor:** X_C against ν is a rectangular hyperbola, falling steeply and never touching either axis. On the phasor diagram i₀ is 90° ahead of V₀. At ν = 0 the reactance is infinite, which is the statement that a capacitor blocks dc.

##### D4 · Series LCR circuit by phasor diagram

> R, L and C in series across `v = v₀ sin ωt`. Being in series, the same instantaneous current flows through all three, so the current is taken as the reference phasor.

1. Same current I through R, L and C
2. Draw the current phasor I along the reference axis
3. V_R = I R, in phase with I — drawn along I
4. V_L = I X_L, leading I by π/2 — drawn 90° ahead
5. V_C = I X_C, lagging I by π/2 — drawn 90° behind
6. V_L and V_C are opposite in direction, so they partly cancel
7. Their resultant has magnitude (V_L − V_C), along V_L when V_L > V_C
8. V_R and (V_L − V_C) are perpendicular
9. The applied voltage V is the resultant of these two perpendicular phasors
10. V² = V_R² + (V_L − V_C)²
11. V = √(V_R² + (V_L − V_C)²)
12. Substituting V_R = IR, V_L = IX_L, V_C = IX_C:
13. V = √((IR)² + (IX_L − IX_C)²)
14. V = √(I²[R² + (X_L − X_C)²])
15. V = I √(R² + (X_L − X_C)²)
16. Impedance is defined as Z = V / I
17. Z = √(R² + (X_L − X_C)²)
18. Substituting X_L = ωL and X_C = 1/ωC:
19. Z = √(R² + (ωL − 1/ωC)²)
20. From the phasor triangle, tan φ = (V_L − V_C) / V_R
21. tan φ = (I X_L − I X_C) / (I R)
22. tan φ = (X_L − X_C) / R
23. φ = tan⁻¹[(X_L − X_C) / R]
24. Peak current i₀ = v₀ / Z
25. i = [v₀ / √(R² + (ωL − 1/ωC)²)] sin(ωt − φ)

**Result:** Z = √(R² + (X_L − X_C)²) · tan φ = (X_L − X_C)/R

**Phasor diagram:** current along the horizontal reference axis; V_R along it; V_L straight up; V_C straight down; (V_L − V_C) as the surviving vertical; the hypotenuse from the origin is V, and the angle it makes with V_R is φ.

*X_L > X_C: φ positive, circuit is inductive, current lags. X_C > X_L: φ negative, circuit is capacitive, current leads. X_L = X_C: φ = 0, resonance.*

##### D5 · Resonance in a series LCR circuit

> The circuit of derivation 4, with R, L and C fixed and the frequency ω of the source varied. Starts from the boxed result of D4, so quote that line first in the exam.

1. From D4: Z = √(R² + (ωL − 1/ωC)²)
2. i₀ = v₀ / Z
3. v₀ is fixed, so i₀ is maximum when Z is minimum
4. R is fixed; the only term that changes with ω is (ωL − 1/ωC)²
5. (ωL − 1/ωC)² ≥ 0 for every ω, and its least value is 0
6. Z is minimum when ωL − 1/ωC = 0
7. ωL = 1/ωC
8. ω²LC = 1
9. ω² = 1/(LC)
10. ω₀ = 1/√(LC)
11. ν₀ = ω₀/2π = 1/(2π√(LC))
12. At ω = ω₀: X_L = X_C, so X_L − X_C = 0
13. Z_min = √(R² + 0) = R
14. i₀(max) = v₀ / R
15. From D4: tan φ = (X_L − X_C)/R = 0/R = 0
16. φ = 0 ⇒ current and applied voltage are in phase
17. The circuit behaves as though only R were present

**Result:** ω₀ = 1/√(LC), ν₀ = 1/(2π√(LC)) · Z = R · i₀(max) = v₀/R

**Graph:** i₀ against ν rises to a peak at ν₀ and falls away on both sides. Draw two curves for two values of R: the smaller R gives the taller, sharper peak. Mark the half-power frequencies ν₁ and ν₂ where the current is i₀(max)/√2, and label the width (ν₂ − ν₁).

*Sharpness is measured by `Q = ω₀L/R = (1/R)√(L/C) = ω₀/(ω₂ − ω₁)`. Resonance is impossible unless both L and C are present.*

##### D6 · Average power in an AC circuit, and wattless current

> A voltage `v = v₀ sin ωt` drives a current `i = i₀ sin(ωt − φ)` through any ac circuit, φ being the phase difference between them.

1. Instantaneous power p = v i
2. p = v₀ sin ωt · i₀ sin(ωt − φ)
3. p = v₀ i₀ sin ωt sin(ωt − φ)
4. p = (v₀ i₀ / 2) · 2 sin ωt sin(ωt − φ)
5. Identity: 2 sin A sin B = cos(A − B) − cos(A + B)
6. Here A = ωt and B = ωt − φ
7. A − B = φ and A + B = 2ωt − φ
8. 2 sin ωt sin(ωt − φ) = cos φ − cos(2ωt − φ)
9. p = (v₀ i₀ / 2)[cos φ − cos(2ωt − φ)]
10. Average over one complete cycle: P = (v₀ i₀ / 2)[cos φ − ⟨cos(2ωt − φ)⟩]
11. ⟨cos(2ωt − φ)⟩ over one complete cycle = 0
12. P = (v₀ i₀ / 2) cos φ
13. P = (v₀/√2)(i₀/√2) cos φ
14. P = V_rms I_rms cos φ
15. Purely resistive: φ = 0, cos φ = 1, P = V_rms I_rms — maximum
16. Purely inductive or purely capacitive: φ = π/2, cos φ = 0
17. P = V_rms I_rms × 0 = 0
18. Current flows but no power is consumed — the current is wattless
19. Wattless component of the current = I_rms sin φ

**Result:** P = V_rms I_rms cos φ · cos φ = R/Z is the power factor

**Graph:** plot v, i and p on one set of axes. The power curve oscillates at twice the frequency of v and i; when φ = π/2 it spends equal time above and below the axis, so its average is zero.

*Note that P = 0 for a pure reactance is not because the resistance is zero, but because voltage and current are 90° out of phase.*

##### D7 · Transformer — turns ratio, and the four losses

> Two coils, N_P turns in the primary and N_S in the secondary, wound on a common laminated soft-iron core. Assume no flux leakage, so the same flux φ links every turn of both coils, and negligible primary resistance.

1. Flux through each turn of either coil = φ
2. Faraday's law for the primary: ε_P = −N_P (dφ/dt)
3. Faraday's law for the secondary: ε_S = −N_S (dφ/dt)
4. Divide the second by the first: ε_S / ε_P = [−N_S (dφ/dt)] / [−N_P (dφ/dt)]
5. ε_S / ε_P = N_S / N_P
6. Primary resistance negligible ⇒ ε_P = V_P
7. Secondary on open circuit ⇒ ε_S = V_S
8. V_S / V_P = N_S / N_P = r — *(r = turns ratio)*
9. For an ideal transformer, output power = input power
10. V_S I_S = V_P I_P
11. I_P / I_S = V_S / V_P
12. I_P / I_S = N_S / N_P = r
13. I_S / I_P = N_P / N_S = 1/r

**Result:** V_S/V_P = N_S/N_P = I_P/I_S

*`N_S > N_P` is a step-up transformer: voltage rises, current falls. `N_S < N_P` is a step-down: voltage falls, current rises. Efficiency = (V_S I_S / V_P I_P) × 100%.*

###### The four energy losses, and the fix for each

| Loss | What is happening | The fix |
|---|---|---|
| Copper loss | Joule heating i²R in the primary and secondary windings | Use thick copper wire of low resistance |
| Iron loss (eddy currents) | The changing flux induces circulating currents in the solid iron core, which heat it | Laminate the core — thin sheets, insulated from one another, so the eddy loops are broken |
| Flux leakage | Not all the flux made by the primary reaches the secondary | Wind the two coils one over the other on the same core |
| Hysteresis loss | The core is magnetised and demagnetised every cycle and energy is dissipated each time round the loop | Use a soft magnetic material — soft iron or silicon steel — with a thin hysteresis loop |

*Xam Idea adds a fifth, humming loss — energy lost as sound when the core vibrates. Give the four above unless the question asks for five.*

##### D8 · AC generator — the emf equation

> A coil of N turns, each of area A, rotates with constant angular speed ω about an axis perpendicular to a uniform magnetic field B. At `t = 0` the plane of the coil is perpendicular to the field, so the area vector is along B.

1. Angle between B and the area vector at time t: θ = ωt
2. Flux through one turn: φ = B A cos θ
3. φ = B A cos ωt
4. Flux linkage through N turns: Nφ = N B A cos ωt
5. Faraday's law: ε = −d(Nφ)/dt
6. ε = −d/dt (N B A cos ωt)
7. N, B and A are constants: ε = −N B A · d/dt (cos ωt)
8. d/dt (cos ωt) = −ω sin ωt
9. ε = −N B A (−ω sin ωt)
10. ε = N B A ω sin ωt
11. sin ωt has maximum magnitude 1
12. Peak emf ε₀ = N B A ω
13. ε = ε₀ sin ωt
14. With ω = 2πν: ε = ε₀ sin 2πνt

**Result:** ε = NBAω sin ωt = ε₀ sin ωt, with ε₀ = NBAω

**Graph:** ε against t is a sine curve, one complete cycle per revolution of the coil, zero when the coil plane is perpendicular to B and peak when the plane is parallel to B.

*Four parts to name in the diagram: field magnet, armature coil, slip rings, carbon brushes. The output can be raised by increasing N, increasing B, increasing A, or spinning faster. A moving-coil galvanometer cannot read this current, because its average over a cycle is zero.*

#### 03 · Formula strip

*● must be instant · ○ a few seconds is fine*

##### ● rms value of an alternating current or voltage

`I_rms = i₀/√2 = 0.707 i₀ · V_rms = v₀/√2` — i₀, v₀ = peak values. I in ampere (A), V in volt (V). This is what every ac meter reads.

##### ○ Mean value of an alternating current over half a cycle

`i_mean = 2i₀/π = 0.637 i₀` — in ampere (A). Over a *full* cycle the mean is zero.

##### ● Inductive reactance

`X_L = ωL = 2πνL` — L = self-inductance in henry (H), ν = frequency in hertz (Hz), ω = 2πν in rad s⁻¹. X_L in ohm (Ω).

##### ● Capacitive reactance

`X_C = 1/ωC = 1/(2πνC)` — C = capacitance in farad (F). X_C in ohm (Ω). Infinite at ν = 0, which is why a capacitor blocks dc.

##### ● Impedance of a series LCR circuit

`Z = √(R² + (X_L − X_C)²)` — R, X_L, X_C, Z all in ohm (Ω). Reduces to R alone at resonance.

##### ● Phase angle of a series LCR circuit

`tan φ = (X_L − X_C)/R` — φ in radian or degree. Positive φ means the current lags; negative means it leads.

##### ● Power factor, in terms of the circuit constants

`cos φ = R / Z` — a pure number between 0 and 1. Equal to 1 for a pure resistance and at resonance, 0 for a pure reactance.

##### ● Average power consumed in any ac circuit

`P = V_rms I_rms cos φ` — P in watt (W). V_rms I_rms alone is the apparent power; only the cos φ fraction of it is consumed.

##### ○ Wattless component of the current

`I_wattless = I_rms sin φ` — in ampere (A). This component transfers no net energy over a cycle.

##### ● Resonant frequency of a series LCR circuit

`ω₀ = 1/√(LC) · ν₀ = 1/(2π√(LC))` — L in henry (H), C in farad (F). ω₀ in rad s⁻¹, ν₀ in hertz (Hz).

##### ○ Quality factor, all three forms

`Q = ω₀L/R = (1/R)√(L/C) = ω₀/(ω₂ − ω₁)` — a pure number, no unit. ω₁ and ω₂ are the half-power frequencies. Larger Q means a sharper resonance.

##### ● Transformer equation, all three ratios

`V_S/V_P = N_S/N_P = I_P/I_S` — N = number of turns (no unit), V in volt (V), I in ampere (A). Note the current ratio is inverted.

##### ○ Efficiency of a transformer

`η = (V_S I_S) / (V_P I_P) × 100%` — output power over input power, as a percentage. Always below 100% in practice.

##### ● emf generated by an ac generator

`ε = NBAω sin ωt = ε₀ sin ωt, ε₀ = NBAω` — N = turns, B in tesla (T), A in m², ω in rad s⁻¹. ε in volt (V).

##### ○ Net voltage across a series LCR circuit from the three drops

`V = √(V_R² + (V_L − V_C)²)` — all in volt (V). This is why the three readings can add to more than the source voltage — they add as phasors, not as numbers.

##### ○ Power wasted as heat in a transmission line

`P_loss = I²R` — I = line current in ampere (A), R = total line resistance in ohm (Ω), P_loss in watt (W). Ten times the voltage means a hundredth of the loss.

#### 04 · Questions to attempt

*Question numbers only, from Xam Idea Chapter 7 and the NCERT questions reprinted inside it. Section names are Xam Idea's own.*

##### Tier 1 — must do

*15 questions · these are the 3-mark and 5-mark slots*

| Question | Page | Why |
|---|---|---|
| Long Answer Q1 | p. 249 | Inductor derivation, full |
| Long Answer Q2 | p. 250 | LCR phasor, both variants |
| Long Answer Q3 | p. 252 | Capacitor derivation, disguised |
| Long Answer Q4 | p. 253 | Average power derivation |
| Long Answer Q5 | p. 253 | Resonance plus graph |
| Long Answer Q6 | p. 254 | Generator, three variants |
| Long Answer Q7 | p. 255 | Transformer plus losses |
| Long Answer Q9 | p. 258 | Sharpness and Q |
| Short Answer Q1 | p. 241 | Capacitor in 3 marks |
| Short Answer Q2 | p. 241 | Minimum Z, wattless |
| Short Answer Q3 | p. 241 | Transformer plus transmission |
| Short Answer Q6 | p. 242 | The voltage paradox |
| Short Answer Q8 | p. 243 | Resonance numerical, complete |
| Short Answer Q18 | p. 247 | Three drops, phasor sum |
| NCERT Q8 | p. 230 | Everything at once |

##### Tier 2 — if time

*extra pattern coverage, mostly 1 and 2 marks*

| Question | Page | Why |
|---|---|---|
| NCERT Q1–Q7 | p. 228–229 | rms and power drills |
| Assertion–Reason 1–10 | p. 234 | Whole set, ten minutes |
| MCQ 7, 8, 16 | p. 231–232 | Average-power one-markers |
| MCQ 11, 12, 13, 17, 25, 26 | p. 231–233 | LCR and phasor reasoning |
| MCQ 3, 15, 18, 22, 23, 24 | p. 231–233 | Waveform and reactance graphs |
| MCQ 5, 10, 21 | p. 231–232 | Transformer and transmission |
| Very Short Ans Q1, Q3–Q6 | p. 236–237 | Definitions, written out |
| Very Short Ans Q11 | p. 238 | Black box plus phasor |
| Very Short Ans Q12, Q13 | p. 238 | Generator numericals |
| Very Short Ans Q19, Q20 | p. 240 | Transformer, line loss |
| Short Answer Q4, Q7, Q12 | p. 242–244 | Brightness reasoning |
| Short Answer Q5, Q9, Q10, Q13 | p. 242–245 | Impedance numericals |
| Short Answer Q11, Q19 | p. 244, 248 | Transformer numericals |
| Short Answer Q14, Q16, Q17 | p. 246–247 | Resonance and graphs |
| Long Answer Q8 | p. 257 | Reasoning plus numerical |

##### Tier 3 — skip unless revising

*off-pattern, over-difficult, or a repeat of something above*

**Off the pattern of this unit:** Case Study `Q1` (p. 235) is an RC charging transient — exponential decay in a dc circuit, not an alternating-current question. Very Short Answer `Q9` and `Q10` (p. 237) derive mean and rms values by integration; the paper will give you the results, not ask you to integrate them.

**Duplicates — do one of each pair, not both:** NCERT `Q3` ≡ Very Short Answer `Q17`. NCERT `Q7` ≡ Short Answer `Q8`. NCERT `Q8` ≡ Short Answer `Q14`. NCERT `Q6` is just the resonance formula with numbers in it.

**Already covered by the theory section:** Very Short Answer `Q2, Q7, Q8, Q15, Q16` and Short Answer `Q15` are pure recall you will have from Section 01. Read the answers, do not write them out.

##### The five numerical types this chapter can ask

1. **Peak to rms, and the power a single element takes** — `I_rms = i₀/√2`, then `P = V_rms I_rms cos φ`
2. **Reactance of a coil or capacitor at a stated frequency** — `X_L = 2πνL · X_C = 1/(2πνC)`
3. **Impedance, current and phase angle of a series LCR circuit** — `Z = √(R² + (X_L − X_C)²)`
4. **Resonance: the frequency, the peak current, the individual voltage drops** — `ω₀ = 1/√(LC)`, with Z = R there
5. **Transformer turns and currents, or loss in a transmission line** — `V_S/V_P = N_S/N_P = I_P/I_S`, and `P_loss = I²R`

### Electromagnetic Waves for Six Marks

*Chapter 8 · Electromagnetic Waves — 6 marks. Source: published page `762322ac-2430-4ee0-99aa-22a0cb8e6921`. Plain-text maths, not KaTeX. **Physics, Derived** has one Chapter 8 derivation (PD38, displacement current); the other four here appear nowhere else. This page also adds the theory, the spectrum table, the formula strip and the question tiers.*

> **Scope.** No scope cut. Five derivations only — the rest of the chapter is recall, and the spectrum table is the single most reliably asked thing in it.

#### 01 · Theory

##### 1 · Displacement current

**Definition to write:** displacement current is the current that exists in a region wherever the electric flux through that region is changing with time, given by `I_d = ε₀ (dΦ_E/dt)`. It is not a flow of charge, and it needs no conductor — it exists in vacuum.

Two situations the examiner asks you to separate:

- **Conduction current, no displacement current** — a steady current in a wire. The electric field in the wire is constant, so the flux does not change.
- **Displacement current, no conduction current** — the space between the plates of a capacitor while it charges or discharges. No charge crosses the gap, but the field between the plates is growing, so the flux is changing.

Its whole point is continuity: at every instant `I_d` between the plates equals `I_c` in the wire, so the total current is unbroken all the way round the circuit and Kirchhoff's junction rule survives. This is also why a galvanometer in series with a capacitor kicks momentarily while the capacitor charges on dc, and why current flows continuously when the source is ac.

##### 2 · Characteristics of electromagnetic waves

- They are **transverse**: E and B are perpendicular to each other and both perpendicular to the direction of propagation, which lies along `E × B`.
- E and B are **in phase** — they reach their maxima and their zeros together — and their magnitudes are locked by `E₀/B₀ = c`.
- They need **no material medium** and travel through vacuum at `c = 3 × 10⁸ m s⁻¹`, the same speed for every wavelength.
- They are **electrically neutral**, so electric and magnetic fields do not deflect them.
- They show reflection, refraction, interference, diffraction and **polarisation** — the last one is the direct evidence that they are transverse.
- They carry **energy and momentum**, so they exert pressure on any surface that absorbs them.
- In a medium the speed falls to `v = 1/√(με) = c/n`; the frequency stays as the source set it, so the wavelength shortens.

*Sunlight warming your hand is the everyday evidence for energy; the photoelectric effect is the laboratory evidence. You do not feel the pressure because `p = U/c` and c is enormous.*

##### 3 · The electromagnetic spectrum

| Band | Wavelength | Frequency | How it is produced | One use |
|---|---|---|---|---|
| γ-rays | < 10⁻¹⁰ m | > 3 × 10¹⁸ Hz | Radioactive decay of nuclei; nuclear reactions | Destroying cancer cells |
| X-rays | 10⁻¹⁰ – 10⁻⁸ m | 3 × 10¹⁶ – 3 × 10¹⁸ Hz | Fast electrons stopped by a heavy metal target such as tungsten | Detecting bone fractures |
| Ultraviolet | 10⁻⁸ – 4 × 10⁻⁷ m | 7.5 × 10¹⁴ – 3 × 10¹⁶ Hz | Very hot bodies; the Sun; mercury-vapour arcs and special lamps | Sterilising water in purifiers; LASIK eye surgery |
| Visible light | 4 × 10⁻⁷ – 7.5 × 10⁻⁷ m | 4 × 10¹⁴ – 7.5 × 10¹⁴ Hz | Electrons rearranging in atoms; incandescent bodies | Vision, photography |
| Infrared | 7.5 × 10⁻⁷ – 10⁻³ m | 3 × 10¹¹ – 4 × 10¹⁴ Hz | Vibration of hot bodies, atoms and molecules | Physiotherapy; TV remote controls |
| Microwaves | 10⁻³ – 10⁻¹ m | 3 × 10⁹ – 3 × 10¹¹ Hz | Klystrons, magnetrons and Gunn diodes | Radar for aircraft navigation; microwave ovens |
| Radio waves | > 10⁻¹ m | < 3 × 10⁹ Hz | Accelerated charges in aerials and oscillating LC circuits | Radio and television broadcasting |

*Order to be able to recite in both directions: γ, X, UV, visible, IR, microwave, radio — increasing wavelength, decreasing frequency. Visible light alone runs 400 nm (violet) to 750 nm (red).*

##### 4 · How electromagnetic waves are produced

A charge at rest makes only a static electric field. A charge in uniform motion makes a steady magnetic field as well, but neither field changes, so nothing radiates. Only an **accelerated** charge radiates.

The mechanism to write out: an oscillating charge produces an oscillating electric field in the space around it; that changing electric field produces an oscillating magnetic field; that changing magnetic field produces a further oscillating electric field, and so on. Each field regenerates the other, so the disturbance carries itself outwards through empty space as an electromagnetic wave.

The frequency of the wave equals the frequency of oscillation of the charge. An LC circuit oscillating at `1/(2π√(LC))` is therefore a source of electromagnetic waves at that frequency, and the energy radiated comes out of the source.

*A charge moving in a circle is accelerating — its direction is changing — so it radiates too.*

##### 5 · The atmosphere and the spectrum

- **Earth's warmth.** The Sun's visible and short-wave radiation reaches the ground and warms it. The ground re-radiates at longer infrared wavelengths, and greenhouse gases such as CO₂ and water vapour absorb and trap that infrared. Without an atmosphere there would be no such trapping, so the average surface temperature would be *lower* than it is now.
- **The ozone layer.** Ozone on top of the stratosphere absorbs the Sun's harmful ultraviolet before it reaches the surface. UV damages skin and eyes and causes skin cancer, so this thin layer is what makes life on land possible.
- **X-ray astronomy needs satellites.** The atmosphere absorbs X-rays completely, so an X-ray telescope on the ground would see nothing. Visible light and radio waves pass through, which is why optical and radio telescopes work from the ground.
- **Long-distance radio uses short-wave bands.** Short waves are reflected back to Earth by the ionosphere, so a signal can be bounced over the horizon to a distant receiver instead of escaping into space.
- **Radar uses microwaves.** Their short wavelength gives good directionality and resolution, and they pass through the atmosphere with little diffraction and little absorption.

#### 02 · Derivations

##### D1 · Displacement current — why Ampere's law was incomplete

> A parallel-plate capacitor of plate area A is being charged, so a time-varying current I(t) flows in the connecting wire. Draw a circular loop around the wire, and consider two *different* surfaces that share that same loop as their boundary.

1. Ampere's circuital law: ∮ B·dl = μ₀ I, where I is the current through any surface bounded by the loop
2. Surface A: a flat disc, pierced by the connecting wire
3. Current through surface A = I(t)
4. ∮ B·dl = μ₀ I(t) …(i)
5. Surface B: a pot-shaped surface with the same boundary loop, dipping between the capacitor plates and touching no wire
6. No charge crosses the gap between the plates, so the current through surface B = 0
7. ∮ B·dl = μ₀ × 0 = 0 …(ii)
8. The left-hand side of (i) and (ii) is the same integral over the same loop
9. (i) and (ii) contradict each other, so Ampere's law in this form is incomplete
10. Between the plates the field is E = σ/ε₀
11. Surface charge density σ = Q/A, Q being the charge on a plate
12. E = Q/(ε₀A)
13. Electric flux through surface B: Φ_E = E A
14. Φ_E = [Q/(ε₀A)] × A
15. Φ_E = Q/ε₀
16. Q = ε₀ Φ_E
17. Differentiate with respect to time: dQ/dt = ε₀ (dΦ_E/dt)
18. dQ/dt is the rate at which charge piles up on the plate, which equals the conduction current I_c in the wire
19. I_c = ε₀ (dΦ_E/dt)
20. So a quantity ε₀ (dΦ_E/dt) exists in the gap with exactly the value of the missing current
21. Maxwell named it the displacement current: I_d = ε₀ (dΦ_E/dt)

**Result:** I_d = ε₀ (dΦ_E/dt), and I_d = I_c at every instant

**Diagram:** capacitor plates with a wire entering from the left. Draw the flat disc surface A cutting the wire, and the pot-shaped surface B bulging round the left plate so its mouth is the same circular loop but its bottom lies in the gap. Mark I(t) on the wire and the electric field lines between the plates.

##### D2 · The Ampere–Maxwell law

> Ampere's law repaired by adding the displacement current found in D1. Quote D1's boxed result first — this derivation is only four lines of algebra on top of it.

> **Shared setup:** D1 and D2 are one continuous argument, and CBSE often asks them as a single question. Learn them as one block: D1 finds the missing term, D2 puts it into the law.

1. From D1: surface A carries conduction current I_c and no changing flux
2. From D1: surface B carries no conduction current but a changing electric flux
3. For the law to give the same answer for both, the total current must be I = I_c + I_d
4. I_d = ε₀ (dΦ_E/dt)
5. I = I_c + ε₀ (dΦ_E/dt)
6. Put this total current into ∮ B·dl = μ₀ I
7. ∮ B·dl = μ₀ [I_c + ε₀ (dΦ_E/dt)]
8. ∮ B·dl = μ₀ I_c + μ₀ ε₀ (dΦ_E/dt)
9. Check on surface A: dΦ_E/dt = 0, so ∮ B·dl = μ₀ I_c
10. Check on surface B: I_c = 0, so ∮ B·dl = μ₀ ε₀ (dΦ_E/dt) = μ₀ I_c — *(using step 19 of D1)*
11. Both surfaces now give the same value of ∮ B·dl — the contradiction is gone

**Result:** ∮ B·dl = μ₀ [ I_c + ε₀ (dΦ_E/dt) ]

**What to say after the box:** this is one of Maxwell's four equations. The new term states that a changing electric field produces a magnetic field — the mirror image of Faraday's law, where a changing magnetic field produces an electric field. That symmetry is what makes a self-sustaining electromagnetic wave possible.

##### D3 · Speed of electromagnetic waves, and E₀/B₀ = c

> Free space: no free charges and no conduction current, so `I_c = 0` everywhere. Only two of Maxwell's equations then matter, and they feed each other.

1. Faraday's law: ∮ E·dl = −(dΦ_B/dt) — a changing B makes an E
2. Ampere–Maxwell law from D2 with I_c = 0: ∮ B·dl = μ₀ ε₀ (dΦ_E/dt) — a changing E makes a B
3. Each field regenerates the other, so the disturbance propagates with no medium
4. Maxwell solved these two together for a plane wave and obtained a wave speed c = 1/√(μ₀ε₀)
5. μ₀ = 4π × 10⁻⁷ T m A⁻¹
6. ε₀ = 8.85 × 10⁻¹² C² N⁻¹ m⁻²
7. μ₀ ε₀ = (4 × 3.14 × 10⁻⁷)(8.85 × 10⁻¹²)
8. μ₀ ε₀ = 1.112 × 10⁻¹⁷
9. √(μ₀ ε₀) = 3.335 × 10⁻⁹
10. c = 1 / (3.335 × 10⁻⁹)
11. c = 3.00 × 10⁸ m s⁻¹
12. This equals the measured speed of light, which is how light was identified as an electromagnetic wave
13. For a plane wave along z: E = E₀ sin(kz − ωt) and B = B₀ sin(kz − ωt)
14. Both carry the same k and the same ω, so both travel at the same speed ω/k
15. ω/k = c
16. Maxwell's equations further require the amplitudes to satisfy E₀ = c B₀
17. E₀ / B₀ = c
18. In a medium of permeability μ and permittivity ε: v = 1/√(με)
19. v = 1/√(μ_r μ₀ ε_r ε₀) = c/√(μ_r ε_r) = c/n

**Result:** c = 1/√(μ₀ε₀) = 3 × 10⁸ m s⁻¹ · E₀/B₀ = c · v = c/√(μ_r ε_r)

*Step 4 is the one place a link is quoted rather than worked. That is deliberate: solving the coupled equations needs the wave equation, which is outside Class XII. What CBSE actually asks is "show that 1/√(μ₀ε₀) gives the velocity of an EM wave in free space" — that is steps 5 to 12, the numerical substitution, and you should write every one of them out.*

##### D4 · Transverse nature, and the orientation of E, B and propagation

> A plane electromagnetic wave travelling along the z-axis in free space, written as `E_x = E₀ sin(kz − ωt)` and `B_y = B₀ sin(kz − ωt)`.

1. Gauss's law for electricity in free space: ∮ E·dA = q/ε₀ = 0 — *(no charge enclosed)*
2. Take a small box with two faces perpendicular to the propagation direction z
3. A component of E along z would send flux in through one face and out through the other, unequally as the wave passes
4. That would give a non-zero net flux, contradicting step 1
5. So E has no component along z
6. Gauss's law for magnetism: ∮ B·dA = 0 always — *(no magnetic monopoles)*
7. By the identical argument, B has no component along z
8. Both E and B lie entirely in the plane perpendicular to the propagation direction — the wave is transverse
9. Faraday's law links the B along y to an E that varies along z and points along x
10. The Ampere–Maxwell law links the E along x to a B that varies along z and points along y
11. So E is along x, B is along y, propagation is along z: E ⊥ B, and both ⊥ propagation
12. x̂ × ŷ = ẑ, so the direction of propagation is along E × B
13. E, B and the propagation vector form a right-handed set
14. Both fields carry the same phase (kz − ωt), so they reach their maxima and their zeros at the same instant — E and B are in phase

**Result:** E ⊥ B ⊥ propagation; propagation along E × B; phase difference between E and B is zero

**Diagram:** three axes with z pointing right. Draw the E sinusoid oscillating up and down in the x–z plane and the B sinusoid oscillating in and out in the y–z plane, both crossing zero at the same points along z. Label the propagation arrow along +z.

*Polarisation is the experimental proof of this: only a transverse wave can be polarised, and light can be.*

##### D5 · Energy density and intensity

> The same plane wave, `E = E₀ sin(kz − ωt)` and `B = B₀ sin(kz − ωt)`, travelling through free space.

1. Energy density of an electric field: u_E = ½ ε₀ E²
2. Energy density of a magnetic field: u_B = B² / (2μ₀)
3. From D3: E = cB
4. Substitute in step 1: u_E = ½ ε₀ (cB)²
5. u_E = ½ ε₀ c² B²
6. From D3: c = 1/√(μ₀ε₀), so c² = 1/(μ₀ε₀)
7. u_E = ½ ε₀ B² × 1/(μ₀ ε₀)
8. u_E = B² / (2μ₀)
9. Comparing with step 2: u_E = u_B
10. Total energy density u = u_E + u_B = ½ ε₀ E² + B²/(2μ₀)
11. Since the two halves are equal: u = 2 × (½ ε₀ E²) = ε₀ E²
12. Average over one cycle: ⟨sin²(kz − ωt)⟩ = ½
13. ⟨u_E⟩ = ½ ε₀ E₀² × ½ = ¼ ε₀ E₀²
14. ⟨u_B⟩ = [B₀²/(2μ₀)] × ½ = B₀²/(4μ₀) = ¼ ε₀ E₀² — *(by step 8)*
15. ⟨u⟩ = ⟨u_E⟩ + ⟨u_B⟩ = ¼ ε₀ E₀² + ¼ ε₀ E₀²
16. ⟨u⟩ = ½ ε₀ E₀²
17. E_rms = E₀/√2, so E₀² = 2 E_rms²
18. ⟨u⟩ = ½ ε₀ (2 E_rms²) = ε₀ E_rms²
19. Intensity I = energy crossing unit area per unit time
20. In time t the wave sweeps a cylinder of cross-section A and length ct
21. Energy in that cylinder = ⟨u⟩ × (A c t)
22. I = energy / (A t) = ⟨u⟩ A c t / (A t)
23. I = ⟨u⟩ c
24. I = ½ ε₀ E₀² c

**Result:** u_E = u_B · ⟨u⟩ = ½ε₀E₀² = ε₀E_rms² · I = ½ε₀E₀²c

*Momentum follows: a wave delivering energy U to a fully absorbing surface delivers momentum `p = U/c`, so it presses on that surface. The pressure is tiny only because c is so large.*

#### 03 · Formula strip

*● must be instant · ○ a few seconds is fine*

##### ● Displacement current

`I_d = ε₀ (dΦ_E/dt)` — Φ_E = electric flux in V m (or N m² C⁻¹), ε₀ = 8.85 × 10⁻¹² C² N⁻¹ m⁻². I_d in ampere (A). Equal to the conduction current at every instant.

##### ● Ampere–Maxwell law, the full corrected form

`∮ B·dl = μ₀ [ I_c + ε₀ (dΦ_E/dt) ]` — B in tesla (T), dl in metre (m), I_c = conduction current in ampere (A), μ₀ = 4π × 10⁻⁷ T m A⁻¹.

##### ● Speed of electromagnetic waves in free space

`c = 1/√(μ₀ ε₀) = 3 × 10⁸ m s⁻¹` — same for every wavelength. This equality with the measured speed of light is what identified light as an EM wave.

##### ● Ratio of the electric and magnetic field amplitudes

`E₀ / B₀ = c` — E₀ in V m⁻¹ (or N C⁻¹), B₀ in tesla (T). Also holds instant by instant: E = cB.

##### ● Speed in a material medium

`v = 1/√(με) = c/√(μ_r ε_r) = c/n` — v in m s⁻¹; μ_r, ε_r and n are dimensionless. The frequency is unchanged, so the wavelength shortens by the factor n.

##### ● Frequency, wavelength and speed

`c = ν λ` — ν in hertz (Hz), λ in metre (m). The workhorse of every spectrum numerical.

##### ○ Wave number and angular frequency of a written wave

`E = E₀ sin(kz − ωt), k = 2π/λ, ω = 2πν, c = ω/k` — k in rad m⁻¹, ω in rad s⁻¹. Read λ and ν straight off the coefficients of z and t.

##### ● Energy densities of the electric and magnetic parts

`u_E = ½ ε₀ E² · u_B = B²/(2μ₀)` — both in joule per cubic metre (J m⁻³). In an EM wave these two are equal at every point.

##### ○ Average total energy density of an EM wave

`⟨u⟩ = ½ ε₀ E₀² = ε₀ E_rms²` — in J m⁻³. E₀ = amplitude, E_rms = E₀/√2, both in V m⁻¹.

##### ○ Intensity of an electromagnetic wave

`I = ⟨u⟩ c = ½ ε₀ E₀² c` — in watt per square metre (W m⁻²). Energy crossing unit area per unit time.

##### ○ Momentum delivered by a wave that is fully absorbed

`p = U / c` — U = energy absorbed in joule (J), p in kg m s⁻¹. Halve nothing — for a fully reflecting surface the momentum transferred is 2U/c.

##### ○ Energy of one photon of the radiation

`E = hν = hc/λ` — h = 6.63 × 10⁻³⁴ J s. E in joule; divide by 1.6 × 10⁻¹⁹ to get electronvolt (eV).

##### ● The two constants, with units

`μ₀ = 4π × 10⁻⁷ T m A⁻¹ · ε₀ = 8.85 × 10⁻¹² C² N⁻¹ m⁻²` — permeability and permittivity of free space. You will be asked to substitute these into c = 1/√(μ₀ε₀).

##### ● Wavelength range of visible light, in nanometre

`400 nm (violet) to 750 nm (red)` — 1 nm = 10⁻⁹ m. Anything shorter than 400 nm is ultraviolet, anything longer than 750 nm is infrared.

#### 04 · Questions to attempt

*Question numbers only, from Xam Idea Chapter 8 and the NCERT questions reprinted inside it. Section names are Xam Idea's own. At 6 marks this chapter will not carry a five-mark question, so the Tier 1 list is weighted towards the 3-mark slots.*

##### Tier 1 — must do

*15 questions · the 3-mark slots and the spectrum recall*

| Question | Page | Why |
|---|---|---|
| Short Answer Q10 | p. 279 | Ampere generalised, full |
| Short Answer Q9 | p. 278 | Same argument, shorter |
| Short Answer Q3 | p. 276 | Conduction versus displacement |
| Short Answer Q4 | p. 276 | Current stays continuous |
| Short Answer Q5 | p. 277 | Diagram plus the c substitution |
| Short Answer Q1 | p. 275 | Spectrum table one |
| Short Answer Q2 | p. 275 | Spectrum table two |
| Short Answer Q6 | p. 277 | Identify plus production |
| Short Answer Q11 | p. 280 | Energy, momentum, density |
| Short Answer Q14 | p. 281 | Radar, atmosphere, pressure |
| Short Answer Q16 | p. 281 | Cancer, ozone, momentum |
| Short Answer Q17 | p. 282 | Four bands, ordered |
| Very Short Ans Q7 | p. 273 | The corrected law, stated |
| NCERT Q10 | p. 266 | Proves u_E equals u_B |
| Practice Q11 | p. 284 | Same proof, asked again |

##### Tier 2 — if time

*extra pattern coverage, mostly 1 and 2 marks*

| Question | Page | Why |
|---|---|---|
| NCERT Q1, Q2 | p. 264–265 | Displacement current numericals |
| NCERT Q4, Q7, Q8 | p. 265–266 | E₀, B₀, ω, k drills |
| NCERT Q3, Q5, Q6 | p. 265 | c = νλ one-liners |
| MCQ 1, 2, 3 | p. 267 | Phase, free space, ratio |
| MCQ 23–27 | p. 270 | Density, uses, displacement |
| MCQ 4–22 | p. 268–269 | Rest of the set, fast |
| Assertion–Reason 1–10 | p. 270–271 | Whole set, ten minutes |
| Case Study (i)–(iv) | p. 272 | Order, transverse, wave number |
| Very Short Ans Q1–Q6 | p. 272–273 | Two-mark definitions |
| Very Short Ans Q8–Q14 | p. 274–275 | Spectrum recall, rapid fire |
| Short Answer Q7, Q8 | p. 277–278 | Ordering, dc versus ac |
| Short Answer Q12, Q13 | p. 280 | Oven, radar, sources |
| Practice Q1 (i)–(x), Q2 | p. 283 | One-markers plus assertion |
| Practice Q3, Q4, Q5, Q9 | p. 283 | Short numericals |

##### Tier 3 — skip unless revising

*off the blueprint, or already done above*

**Belongs to a different chapter:** NCERT `Q9` (p. 266) builds a table of photon energies across the spectrum from E = hν. That is Dual Nature material, not this unit's six marks.

**Duplicates — do one of each pair, not both:** NCERT `Q10` ≡ Practice `Q10`. Short Answer `Q15` ≡ Short Answer `Q16`, same three-part shape. Practice `Q12` ≡ Short Answer `Q10`. Practice `Q14` ≡ Short Answer `Q15`. Practice `Q6, Q7, Q8, Q13` are all restatements of Very Short Answer and Short Answer questions already in Tiers 1 and 2.

**Read the answer, do not write it out:** at 6 marks the chapter cannot take more than about four questions on the paper. Once Tier 1 is done, the return on writing out any further recall answer is close to zero — spend the time on Chapter 7 instead.

##### The five numerical types this chapter can ask

1. **Displacement current between the plates of a charging capacitor** — `I_d = ε₀ (dΦ_E/dt) = ε₀A (dE/dt)`, and I_d = I_c
2. **Move between frequency and wavelength anywhere on the spectrum** — `c = νλ`
3. **One field amplitude from the other** — `E₀/B₀ = c`
4. **Read λ, ν, ω and speed off a wave written as an equation** — `k = 2π/λ, ω = 2πν, c = ω/k`
5. **Energy density, intensity or momentum of a beam** — `⟨u⟩ = ½ε₀E₀², I = ⟨u⟩c, p = U/c`

## Appendix — gaps, caveats and open questions

### Chapter 9 physics was never transcribed

Chapter 9 *is* covered here — seven derivations (PD39–PD45, including lenses,
the prism and both instruments) in **Physics, Derived**, twelve entries in
**Every Physics Formula**, and the whole **Ray Optics to 9.4** page. But all of
it was written from NCERT and from that earlier page, never from the teacher's
own lectures, so it carries the physics without the emphasis. There is no
`notes/leph109` to check it against.

Eighteen Ray Optics lecture videos (1.2 GB) sit in Google Drive folder
`1QC3JCSOfLxDxxZfW6rVxAIDAZs4Bkt0v`, and have never been transcribed. The
blocker is Google **Drive** OAuth, not the Gemini ASR key — that one is
configured and working. `DRIVE_CLIENT_ID`, `DRIVE_CLIENT_SECRET` and
`DRIVE_REFRESH_TOKEN` are all empty in `.env`; the access token in there
expired on 3 September. The folder is owned by the teacher rather than the
student, its anonymous download endpoint redirects to a login page, and the
MCP Drive connector caps downloads at 10 MB against files of 17–170 MB.

### A symbol clash still in the source

`notes/leph106` writes the solenoid self-inductance as `L = μ₀n²AL`, using `L`
for both the inductance and the length of the solenoid. Both sheets in this
file write it as `L = μ₀n²Al` and say so explicitly; the underlying note has
not been corrected.

### How much to trust the transcripts

Chemistry Chapter 6 had chunk-seam holes that passed the coverage, gap **and**
duplication checks at the same time — the segments on either side of a seam
overlapped in reported time while skipping real audio, so no automated check
could see the gap. About 36 lines (the SN2 mechanism, ambident nucleophiles,
organolithiums) and six past-year questions were recovered by re-transcribing
the audio windows directly. Anything similar elsewhere would be invisible to
the same checks, so read for sense, not just for coverage.

Where an equation extracted from the NCERT PDF disagrees with a board frame,
**the board frame is authoritative** — PDF flattening mangles the equations.

### Open question

No physics exam date has ever been given. The Ray Optics page was built for a
test that stopped at Section 9.4 and explicitly told the student to skip every
lens, prism and instrument question — advice that is wrong for any paper with a
wider scope, and the reason Physics, Derived covers lenses and instruments
while that page does not. If a physics paper is close, the scope needs
confirming before either is used for it.
