# The Potentiometer: Principle, Sensitivity, and Comparing EMFs

## Why a potentiometer, not a voltmeter, for measuring EMF

EMF is defined as the potential difference across a cell's terminals when **no current** is drawn. A real voltmeter has finite (not infinite) resistance, so it always draws a small current, meaning its reading is never *exactly* EMF. A potentiometer, based on the **null-deflection method**, draws no current from the cell at its balance point — so it measures true EMF exactly.

## Principle of the potentiometer

For a wire of uniform cross-sectional area carrying a **steady current**, the fall of potential across any portion is directly proportional to that portion's length. Since $V=IR=I\rho L/A$ and $I,\rho,A$ are all constant:
$$V = KL, \qquad K = \frac{V}{L} = \text{potential gradient (fall of potential per unit length)}$$
(Analogous to other length-based rate quantities, e.g. temperature gradient $dT/dx$.)

## Sensitivity

The smallest potential difference the potentiometer can detect. Smaller $K$ (potential gradient) $\Rightarrow$ finer resolution $\Rightarrow$ **higher** sensitivity (e.g. $0.1$ V/cm is more sensitive than $1$ V/cm). Increase sensitivity by:
1. **Increasing** the total wire length, or
2. **Decreasing** the potential difference (equivalently, current) across the wire — in practice, by adding a series rheostat in the main circuit.

## Apparatus

A long uniform wire (e.g. $4$ m) from $A$ to $B$, connected in the main circuit to a driver battery, key, and optional rheostat. The two cells being compared connect via a **commutator** (three-way switch, only one cell in the galvanometer branch at a time), with a protective resistance in series with the galvanometer, and a **jockey** to tap along the wire and find the null point.

## Use 1: comparing EMFs of two cells

Connect $\mathcal E_1$ to the galvanometer branch ($\mathcal E_2$ left open); tap the jockey to find the null point (zero galvanometer deflection $\Rightarrow$ zero current drawn from $\mathcal E_1$) at length $L_1$: $\mathcal E_1 = KL_1$. Repeat with $\mathcal E_2$ to get $\mathcal E_2=KL_2$. Then:
$$\boxed{\frac{\mathcal E_1}{\mathcal E_2} = \frac{L_1}{L_2}}$$

**Precaution:** the positive terminal of each cell must connect to the *same* positive terminal of the main circuit — wrong polarity means the potentials add instead of oppose, and no null point will ever be found.

## Use 2: internal resistance of a cell (setup only)

A board heading and circuit diagram show a second use beginning: finding a cell's internal resistance using the potentiometer, with a resistance box added in the cell-and-galvanometer branch, alongside a reminder of $r=\dfrac{(\mathcal E-V)}{V}R$ (a formula derived in an earlier lecture of this chapter specifically for this purpose). Only the setup is confirmed here — see the flagged span below for why the worked derivation isn't included.

---
**A note on syllabus status:** the Potentiometer topic covered in this lecture does not appear anywhere in the current (rationalised) NCERT Class 12 Physics textbook's Current Electricity chapter -- it was one of the topics removed in the CBSE 2022-23 rationalisation. It may still be relevant depending on your specific school's or exam's syllabus, but it is not in the current official NCERT text, so no NCERT section number is cited for any claim in this note.


## Verify these spans
- [32:08–34:07] The transcript's real narration (247 unique segments) runs coherently through the potentiometer's principle, sensitivity, apparatus, and the EMF-comparison use, ending naturally on the positive-terminal precaution at t=1928.7s -- about 119 seconds before the recording's true end. The last captured board frame (floor_000096.jpg, t=1900s) shows a second use of the potentiometer just beginning: 'Find internal resistance of cell using potentiometer', with a circuit diagram (resistance box, galvanometer) and a reminder of the r=[(E-V)/V]R formula derived in an earlier lecture -- but only the heading and circuit setup are visible, with no further frames available to confirm a worked derivation. This second use is included above only as what is directly visible (the setup), not as a completed derivation, since neither the transcript nor any later frame confirms how far it was carried.