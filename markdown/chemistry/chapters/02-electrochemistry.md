`NCERT Class XII Chemistry · Chapter 2 · Electrochemistry`

# Electrochemistry — Complete Notes

*14 marks — second heaviest on the blueprint. Two engines run this chapter: the Nernst equation and Faraday's laws. Nearly every numerical is one of those two wearing a different hat.*

## The two cell types — *the distinction every question hangs off*

|  | Electrochemical (galvanic) | Electrolytic |
|---|---|---|
| Does | Chemical → electrical | Electrical → chemical |
| Reaction | Spontaneous | Non-spontaneous |
| $\Delta G$ | Negative | Positive |
| Anode | Negative | Positive |
| Cathode | Positive | Negative |

Constant across both: **oxidation at the anode, reduction at the cathode.** Only the charge signs flip.

**Examiner asks:** "two points of difference" (2020) is a standing 2-marker. Give the ΔG and the anode-sign pair — they're the two that can't be waffled.

## Daniell cell and cell notation — *how to write a cell down, and why the salt bridge is there*

Zinc rod in 1 M $\ce{ZnSO4}$, copper rod in 1 M $\ce{CuSO4}$, joined by a salt bridge and an external wire. EMF = **1.1 V** at unit concentration.

$$\ce{Zn(s) -> Zn^2+(aq) + 2e^-} \quad \text{(anode, oxidation)}$$
 $$\ce{Cu^2+(aq) + 2e^- -> Cu(s)} \quad \text{(cathode, reduction)}$$

The zinc rod thins; the copper rod thickens.

#### Cell notation

Anode on the left, cathode on the right. Single line = phase boundary, double line = salt bridge:

$$\ce{Zn(s) | Zn^2+(aq) || Cu^2+(aq) | Cu(s)}$$

#### What the salt bridge actually does

It's a U-tube of electrolyte ($\ce{KCl}$, $\ce{KNO3}$, $\ce{NH4Cl}$) set in agar or gelatin. Without it, $\ce{Zn^2+}$ builds up in the anode compartment and $\ce{SO4^2-}$ in the cathode compartment; the charge separation stalls the cell. The bridge's ions migrate in to neutralise both halves and complete the circuit.

**Examiner asks:** "why is a salt bridge necessary" (2026) — answer with both jobs: maintains electrical neutrality *and* completes the circuit.

## Electrode potential and SHE — *why everything is written as reduction potential*

Dip a metal in a solution of its own ions and charge separates until equilibrium. That potential difference between metal and solution is the **electrode potential**.

By IUPAC convention **every electrode potential is quoted as a reduction potential** — because you can't subtract an oxidation potential from a reduction potential meaningfully. Oxidation and reduction potentials of the same electrode are numerically equal and opposite in sign.

**Standard electrode potential ($E^{\circ}$):** ion concentration 1 M, 298 K, and 1 bar for any gas.

$$E^{\circ}_{\text{cell}} = E^{\circ}_{\text{cathode}} - E^{\circ}_{\text{anode}}$$

Also written $E_{\text{right}} - E_{\text{left}}$, since cathode sits on the right in cell notation. $E_{\text{cell}}$ for a working cell is always positive.

#### Standard hydrogen electrode

A single half-cell's absolute potential can't be measured — you need a second electrode to get a reading at all. So SHE is defined as the reference with $E^{\circ} = 0.00$ V exactly. It's a platinum foil coated with platinum black, $\ce{H2}$ at 1 bar, $\ce{H+}$ at 1 M.

Connect zinc to SHE: electrons flow zinc → SHE, so zinc is the anode, reading 0.76 V. Then $0.76 = 0 - E^{\circ}_{\ce{Zn^2+/Zn}}$, giving $E^{\circ}_{\ce{Zn^2+/Zn}} = -0.76$ V. Copper against SHE reads 0.34 V with electrons flowing the other way, giving $+0.34$ V.

## Electrochemical series — *reading a table of E° values*

Arrange standard electrode potentials in order and the series tells you three things at a glance.

- **High $E^{\circ}$** → reduces easily → **strong oxidising agent.** Fluorine, $+2.87$ V, is the strongest.
- **Low (negative) $E^{\circ}$** → oxidises easily → **strong reducing agent.** Lithium, $-3.05$ V, is the strongest.
- **Feasibility:** the species actually being reduced must have the higher $E^{\circ}$. If a proposed reaction has it backwards, the reaction isn't feasible.

Worked · 2023 — E° of a cell

$E^{\circ}_{\ce{Ag+/Ag}} = 0.80$ V, $E^{\circ}_{\ce{Fe^2+/Fe}} = -0.44$ V. Find $E^{\circ}_{\text{cell}}$.

Higher $E^{\circ}$ becomes the cathode, so silver is cathode, iron is anode.

$$E^{\circ}_{\text{cell}} = 0.80 - (-0.44) = 1.24\ \text{V}$$

**Examiner asks:** "which of A and B liberates $\ce{H2}$ from dilute $\ce{H2SO4}$" (2026) — the one with the more negative $E^{\circ}$, because it oxidises more readily.

## Nernst equation — *the workhorse — for when concentrations aren't 1 M*

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

#### Nernst at equilibrium → equilibrium constant

At equilibrium $E_{\text{cell}} = 0$ and $Q = K_c$, so:

$$E^{\circ}_{\text{cell}} = \frac{0.0591}{n}\log K_c$$

**Examiner asks:** "why is $K_c$ related to $E^{\circ}_{\text{cell}}$ and not $E_{\text{cell}}$?" (2026) — because at equilibrium $E_{\text{cell}}$ is zero and generates no current, while $E^{\circ}$ stays constant.

## Gibbs energy and cell EMF — *one equation, two exam uses*

$$\Delta_r G = -nFE_{\text{cell}} \qquad \Delta_r G^{\circ} = -nFE^{\circ}_{\text{cell}}$$

The electrical work a cell does equals the fall in Gibbs energy.

**The intensive/extensive point** the examiner likes: $E_{\text{cell}}$ is **intensive** — multiply the equation by 2 and it doesn't change. $\Delta G$ is **extensive** — it depends on $n$, so doubling the equation doubles it.

Worked · 2025 — ΔG° and log K_c

$\ce{2Cr + 3Cd^2+ -> 2Cr^3+ + 3Cd}$. $E^{\circ}_{\ce{Cd^2+/Cd}} = -0.40$ V, $E^{\circ}_{\ce{Cr^3+/Cr}} = -0.74$ V, $F = 96500$.

Cd is reduced → cathode. $E^{\circ}_{\text{cell}} = -0.40 - (-0.74) = 0.34$ V. Cr loses 3e⁻ × 2 = 6, so $n = 6$.

$$\Delta_r G^{\circ} = -6 \times 96500 \times 0.34 = -196860\ \text{J mol}^{-1} = -196.86\ \text{kJ mol}^{-1}$$

## Conductance, conductivity, molar conductivity — *four quantities that are easy to confuse*

| Quantity | Symbol | Relation | Unit |
|---|---|---|---|
| Resistance | $R$ | $R = \rho \dfrac{l}{A}$ | Ω |
| Resistivity | $\rho$ | $\rho = R\dfrac{A}{l}$ | Ω cm |
| Conductance | $G$ | $G = 1/R$ | S (siemens) |
| Conductivity | $\kappa$ | $\kappa = 1/\rho$ | S cm⁻¹ |
| Molar conductivity | $\Lambda_m$ | $\Lambda_m = \dfrac{\kappa \times 1000}{M}$ | S cm² mol⁻¹ |

#### Cell constant

$l/A$ is fixed for a given conductivity cell, so it's called the **cell constant** $G^*$:

$$G^* = \frac{l}{A} = \kappa \times R$$

Measuring $l$ and $A$ directly is unreliable, so $G^*$ is found by filling the cell with a solution of known conductivity (usually KCl) and measuring resistance. Once known, the same cell gives $\kappa$ for any solution: $\kappa = G^*/R$.

*Resistance is measured on a Wheatstone bridge with an **AC** source (DC would electrolyse the solution and change its composition) and a purpose-built conductivity cell (a solution can't be wired into the bridge directly).*

Worked · 2024 — resistivity, conductivity, molar conductivity

0.05 M NaOH, cell constant 50 cm⁻¹, resistance $4.5 \times 10^3$ Ω.

$$\kappa = \frac{G^*}{R} = \frac{50}{4.5\times10^3} = 0.011\ \text{S cm}^{-1}$$
 $$\rho = \frac{1}{\kappa} = 90\ \Omega\,\text{cm}$$
 $$\Lambda_m = \frac{0.011 \times 1000}{0.05} = 220\ \text{S cm}^2\text{mol}^{-1}$$

#### Variation with dilution — the two go opposite ways

- **Conductivity falls** on dilution: fewer ions per cm³.
- **Molar conductivity rises** on dilution: the volume holding one mole of electrolyte increases, and interionic attraction weakens.

> **Trap:** these two moving in opposite directions is itself an exam question. Conductivity is per unit *volume*; molar conductivity is per *mole*.

#### Strong vs weak electrolyte on the graph

Plot $\Lambda_m$ against $\sqrt{c}$:

- **Strong electrolyte** — starts high, rises gently and **linearly**. Extrapolate to zero concentration to read $\Lambda_m^{\circ}$ straight off the graph.
- **Weak electrolyte** — starts low, then shoots up steeply near zero concentration, running almost **parallel to the y-axis**. Cannot be extrapolated; you must use Kohlrausch's law instead.

## Kohlrausch's law — *and its three applications*

**Kohlrausch law of independent migration of ions:** the limiting molar conductivity of an electrolyte is the sum of the individual contributions of its cation and anion.

$$\Lambda^{\circ}_m(\ce{NaCl}) = \lambda^{\circ}_{\ce{Na+}} + \lambda^{\circ}_{\ce{Cl-}}$$
 $$\Lambda^{\circ}_m(\ce{BaCl2}) = \lambda^{\circ}_{\ce{Ba^2+}} + 2\lambda^{\circ}_{\ce{Cl-}}$$

> **Trap:** the stoichiometric multiplier. $\ce{Al2(SO4)3}$ needs $2\lambda^{\circ}_{\ce{Al^3+}} + 3\lambda^{\circ}_{\ce{SO4^2-}}$. Forgetting the 2 and 3 is the whole mistake.

#### 1 · Λ° of a weak electrolyte

Can't be read off a graph, so build it from strong electrolytes that share ions:

$$\Lambda^{\circ}(\ce{CH3COOH}) = \Lambda^{\circ}(\ce{CH3COONa}) + \Lambda^{\circ}(\ce{HCl}) - \Lambda^{\circ}(\ce{NaCl})$$

The $\ce{Na+}$ and $\ce{Cl-}$ terms cancel, leaving exactly $\lambda^{\circ}_{\ce{CH3COO-}} + \lambda^{\circ}_{\ce{H+}}$.

#### 2 · Degree of dissociation

$$\alpha = \frac{\Lambda_m}{\Lambda^{\circ}_m}$$

#### 3 · Dissociation constant

$$K_a = \frac{c\,\alpha^2}{1-\alpha}$$

Worked · 2020 — limiting ionic conductivity from Kohlrausch

$\Lambda^{\circ}(\ce{Al2(SO4)3}) = 858$, $\lambda^{\circ}_{\ce{SO4^2-}} = 160$ S cm² mol⁻¹. Find $\lambda^{\circ}_{\ce{Al^3+}}$.

$$858 = 2\lambda^{\circ}_{\ce{Al^3+}} + 3(160) \Rightarrow 2\lambda^{\circ}_{\ce{Al^3+}} = 858 - 480 = 378$$
 $$\lambda^{\circ}_{\ce{Al^3+}} = 189\ \text{S cm}^2\text{mol}^{-1}$$

## Faraday's laws of electrolysis — *the second engine of this chapter*

#### First law

Mass deposited is proportional to the charge passed:

$$w = \frac{M \, I \, t}{n \, F}$$

$M$ = molar mass, $I$ = current in amperes, $t$ = time in **seconds**, $n$ = electrons gained per ion, $F = 96500$ C mol⁻¹.

#### Second law

Same charge through different electrolytes deposits masses in the ratio of their **equivalent weights**:

$$\frac{w_1}{w_2} = \frac{E_1}{E_2}, \qquad E = \frac{\text{atomic mass}}{n}$$

So Na (23/1), Mg (24/2 = 12), Al (27/3 = 9) deposit in the ratio 23 : 12 : 9 per faraday.

> **Trap:** time in minutes. Convert to seconds first — this single slip has cost more marks in this chapter than any conceptual error.

Worked · 2017 — mass deposited

2 A through $\ce{AgNO3}$ for 15 min. $M(\ce{Ag}) = 108$.

$t = 15 \times 60 = 900$ s. $\ce{Ag+ + e^- -> Ag}$, so $n = 1$.

$$w = \frac{108 \times 2 \times 900}{1 \times 96500} = 2.014\ \text{g}$$

#### Charge in faradays — without the formula

Often faster to reason directly. To reduce 1 mol $\ce{Zn^2+}$ you need 2 mol of electrons = **2 F** = 193000 C. To reduce 1 mol $\ce{MnO4-}$ to $\ce{Mn^2+}$, Mn goes +7 → +2, so 5 mol electrons = **5 F**.

## Products of electrolysis — *the E° comparison, and the overpotential exception*

In aqueous solution, water competes with the dissolved ions at both electrodes. Two rules decide the winner:

- **At the cathode:** the species with the **higher** $E^{\circ}$ is reduced.
- **At the anode:** the species with the **lower** $E^{\circ}$ is oxidised.

#### Aqueous NaCl — the standard case

**Cathode:** $\ce{Na+}$ ($-2.71$ V) vs $\ce{H+}$ (0.00 V). Hydrogen wins → $\ce{H2}$ gas.

**Anode:** $\ce{Cl-}$ (1.36 V) vs water → $\ce{O2}$ (1.23 V). By the rule oxygen should win — **but it doesn't.** Oxygen evolution is kinetically slow and needs extra voltage (**overpotential**) to proceed at a useful rate, so chlorine is released instead.

Net: $\ce{NaCl(aq) + H2O -> NaOH + 1/2 H2 + 1/2 Cl2}$

> **Trap:** the overpotential exception is the entire point of this question. Answering "oxygen, because 1.23 < 1.36" is the trap being set. Name overpotential explicitly.

#### Molten vs aqueous

Molten NaCl has no water, so there's no competition: sodium at the cathode, chlorine at the anode.

#### Sulphuric acid

Dilute $\ce{H2SO4}$ → oxygen at the anode. Concentrated → peroxodisulphate, $\ce{2SO4^2- -> S2O8^2- + 2e^-}$ ($E^{\circ} = 1.96$ V).

## Batteries and fuel cells — *four devices, and the one fact asked about each*

#### Primary — cannot be recharged

**Dry cell (Leclanché):** zinc container = anode, graphite rod surrounded by $\ce{MnO2}$ and carbon = cathode, moist $\ce{NH4Cl}$/$\ce{ZnCl2}$ paste = electrolyte. Used in transistors and clocks.

$$\text{Anode: } \ce{Zn -> Zn^2+ + 2e^-}$$
 $$\text{Cathode: } \ce{MnO2 + NH4+ + e^- -> MnO(OH) + NH3}$$

**Mercury cell:** used in hearing aids and watches. Its selling point — and the exam answer — is that **the potential stays constant through its life**, because no ions appear in the overall reaction, so no concentration changes:

$$\ce{Zn(Hg) + HgO(s) -> ZnO(s) + Hg(l)}$$

#### Secondary — rechargeable

**Lead storage battery** (automobiles, inverters): Pb anode, $\ce{PbO2}$ on a lead grid as cathode, 38% $\ce{H2SO4}$ electrolyte.

$$\ce{Pb + PbO2 + 2H2SO4 -> 2PbSO4 + 2H2O}$$

On **charging** the whole thing runs backwards: $\ce{2PbSO4 + 2H2O -> Pb + PbO2 + 2H2SO4}$.

**Nickel–cadmium:** Cd anode, $\ce{NiO2}$ cathode, KOH electrolyte. Longer life than lead storage but more expensive to make.

#### Fuel cell

Converts a fuel's chemical energy *directly* to electricity, with reactants fed in continuously. The $\ce{H2}$–$\ce{O2}$ cell powered the **Apollo programme**, and its product water was condensed into the astronauts' drinking supply.

$$\text{Anode: } \ce{H2 + 2OH^- -> 2H2O + 2e^-}$$
 $$\text{Cathode: } \ce{O2 + 2H2O + 4e^- -> 4OH^-}$$
 $$\text{Overall: } \ce{2H2 + O2 -> 2H2O}$$

**Two advantages** (the standard 2-marker): ~70% efficiency against ~40% for a thermal plant, and it's pollution-free.

## Corrosion — *the electrochemical explanation, and two preventions*

Corrosion is chemical attack by atmospheric gases and moisture on a metal surface, giving oxides, sulphides and carbonates. Rusting is the electrochemical case:

$$\ce{2Fe + O2 + 4H+ -> 2Fe^2+ + 2H2O}, \qquad E^{\circ} = 1.67\ \text{V}$$

$\ce{Fe^2+}$ is then oxidised further by atmospheric oxygen to $\ce{Fe^3+}$, and rust is **hydrated ferric oxide**, $\ce{Fe2O3.xH2O}$.

#### Prevention

- **Barrier protection** — paint, bisphenol, or a coat of another metal (Sn, Zn) between iron and the air.
- **Sacrificial protection** — attach a *more reactive* metal (Mg, Zn). It has the more negative $E^{\circ}$, so it oxidises in preference to the iron and corrodes away while the iron survives.

**Examiner asks:** "why are magnesium blocks fixed to iron pipelines" — sacrificial anode; magnesium is more reactive, more negative $E^{\circ}$, oxidises preferentially.

## Numerical patterns, collected — *five patterns, one model each*

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

## Past year questions · question types — *ranked by how often they turn up*

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

## Past year questions · mark slots — *what each type is worth*

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

## Past year questions · repeat offenders — *appeared more than once — highest probability in the chapter*

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

## Past year questions · cold practice — *answers only — work them before you look*

#### Nernst / EMF

- 2020 Q2 — write cell notation and the Nernst equation for $\ce{Mg + 2Ag+ -> Mg^2+ + 2Ag}$. $\ce{Mg|Mg^2+||Ag+|Ag}$; $E = E^{\circ} - \frac{0.0591}{2}\log\frac{[\ce{Mg^2+}]}{[\ce{Ag+}]^2}$

- 2026 Q19 — EMF of $\ce{Sn|Sn^2+||H+|H2}$ at 298 K with concentrations given. Apply Nernst with $n=2$; $\ce{H2}$ omitted as a gas at 1 bar

#### ΔG° and K_c

- 2026 Q23 — $E^{\circ}$ for $\ce{Cu + 2Ag+ <=> Cu^2+ + 2Ag}$ at equilibrium, $K_c = 10^{15}$. $E^{\circ} = \frac{0.0591}{2}\times 15 = 0.44$ V

#### Conductivity

- Lecture PYQ — 0.05 M KCl, $l = 50$ cm, $A = 0.625$ cm², $R = 5\times10^3$ Ω. Find ρ, κ, Λ_m. 62.5 Ω cm; 0.016 S cm⁻¹; 320 S cm² mol⁻¹

- Lecture PYQ — cell gives 164 Ω with 0.02 M KCl (κ = 2.768×10⁻³), then 78.5 Ω with 0.05 M $\ce{AgNO3}$. Find κ and Λ_m of $\ce{AgNO3}$. $G^* = 0.4539$; κ = 5.78×10⁻³; Λ_m = 115.6 S cm² mol⁻¹

- 2026 Q22 — 0.1 M NaCl, κ = 1.06×10⁻² S cm⁻¹, $\lambda^{\circ}$ Na⁺ = 50.1, Cl⁻ = 76.5. Find Λ_m and α. 106 S cm² mol⁻¹; Λ° = 126.6; α = 0.837

- 2022 Q13(b) — α of acetic acid if Λ_m = 48 and Λ°_m = 400. 0.12

#### Kohlrausch

- 2021–22 — Λ° of $\ce{MgCl2}$ given $\lambda^{\circ}$ Mg²⁺ = 106, Cl⁻ = 76.3. 285.6 S cm² mol⁻¹ (remember the 2×)

#### Faraday's laws

- 2014 — 5 A through $\ce{Ni(NO3)2}$ for 20 min, $M = 58.7$. Mass of Ni? 1.825 g

- 2015 — charge to reduce 1 mol $\ce{Zn^2+}$ to Zn. 2 F = 193000 C

- 2026 Q25(b) — faradays to produce 40 g Al from molten $\ce{Al2O3}$, $M = 27$. 4.44 F

Built from Sourabh Raina's Electrochemistry one-shot and PYQ videos, cross-checked against NCERT Class XII Chemistry Chapter 2 (Rationalised 2022–23). Verified against NCERT: "Kohlrausch law of independent migration of ions"; Faraday constant 96487 C mol⁻¹ (taken as 96500 in working); Daniell cell 1.1 V at unit concentration.
