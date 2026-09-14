# Internal Resistance, EMF, Terminal PD, and Combination of Cells

**NCERT sections covered:** 3.10, 3.11

## Internal resistance (NCERT 3.10)

A cell's electrolyte hinders current flow just like an external resistor. Internal resistance $r$ depends on the electrolyte's nature, temperature, and concentration; it is directly proportional to electrode separation $l$ and inversely proportional to immersed electrode area $A$:
$$r = \frac{cl}{A}\quad\text{(at a given temperature)}$$
$r$ **decreases** with increasing temperature, and **increases** as a cell ages with use.

## EMF and terminal potential difference (NCERT 3.10)

**EMF** ($\mathcal E$): despite the name, has nothing to do with force — unit is the **volt**, not newton (a historical misnomer). Defined as work done per unit charge; equals the potential difference across a cell's terminals when **no current is drawn** (open circuit).

**Terminal PD** ($V$): once current flows through an external resistor $R$ (closed circuit), the measured PD across the cell's terminals:
$$\mathcal E = V + Ir \quad\Leftrightarrow\quad V = \mathcal E - Ir$$
During **discharging** (normal use), $\mathcal E > V$. Rearranged forms: $I = \dfrac{\mathcal E}{R+r}$, and $r = \dfrac{\mathcal E - V}{V}R$ (this last form is reused later for the potentiometer method of measuring internal resistance).

**During charging**, current direction through the cell reverses: $V = \mathcal E + Ir$, so $V > \mathcal E$.

## Combination of cells (NCERT 3.11)

**Sign-convention / potential-walk method:** pick a current direction; a potential *drop* in the direction of current is negative, a *rise* is positive. Walking from one circuit point to another, sum each EMF and $Ir$ term with its sign — e.g. $V_A - V_B = \mathcal E_1 - ir_1$ for one branch. (This same method is reused later for potentiometer problems.)

### Cells in parallel
Two cells $(\mathcal E_1,r_1)$ and $(\mathcal E_2,r_2)$ between the same points $A,B$, supplying $I_1=\dfrac{\mathcal E_1-V}{r_1}$, $I_2=\dfrac{\mathcal E_2-V}{r_2}$, with $I=I_1+I_2$. Solving for $V$ in terms of total current $I$ gives an equivalent single cell:
$$\mathcal E_{eq} = \frac{\mathcal E_1 r_2+\mathcal E_2 r_1}{r_1+r_2}, \qquad \frac{1}{r_{eq}} = \frac{1}{r_1}+\frac{1}{r_2}\quad(\text{i.e. } r_{eq}=\frac{r_1 r_2}{r_1+r_2})$$
$$V = \mathcal E_{eq} - I\,r_{eq}$$
Internal resistances combine exactly like the reciprocal (parallel) rule for resistors; the equivalent EMF is a resistance-weighted combination of the two.

---
*Note on this lecture's transcript:* the cells-in-parallel derivation above is grounded entirely from a board frame near the true end of the lecture -- the transcript's own narration stops mid-way through setting up the series case. See the flagged span below.


## Verify these spans
- [23:41–33:10] The transcript's real (non-repeated) narration introduces 'combination of cells' and demonstrates the sign-convention potential-walk method for a series-like arrangement (deriving VA-VB=E1-ir1 and VB-VC=E2-ir2 for two cells), then cuts off exactly at the true end of the recording, right as a new worked-numerical circuit is being set up. Board frames extend past this: floor_000088.jpg through floor_000097.jpg (t=1740-1920s, within the true duration) show a full 'cells in parallel' page already in progress and then complete, deriving the equivalent EMF and equivalent internal resistance for two cells in parallel -- none of it narrated in the available transcript. The cells-in-parallel claim above is grounded entirely from the final frame. The corresponding final compact formula for cells in SERIES (which would logically precede the parallel case, analogous to E_eq=E1+E2, r_eq=r1+r2 for aligned cells) was not found written out on any sampled frame either, so it is intentionally left out of this note rather than assumed from the general pattern.