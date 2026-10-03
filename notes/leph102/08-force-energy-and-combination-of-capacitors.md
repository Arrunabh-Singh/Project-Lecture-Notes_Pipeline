# Force Between Capacitor Plates, Energy Stored, Energy Density, and Combination of Capacitors

**NCERT sections covered:** 2.14, 2.15

## Force between the plates of a capacitor (NCERT 2.14 context)

The force on plate 1 is due to the field produced by plate 2 *alone* (a plate cannot exert a net force on its own charge), so the relevant field is $E = \sigma/2\varepsilon_0$, not the full inter-plate field $\sigma/\varepsilon_0$:
$$F = \left(\frac{\sigma}{2\varepsilon_0}\right)q = \frac{q^2}{2A\varepsilon_0}$$
The plates attract each other with this force.

## Energy stored in a capacitor (NCERT 2.15)

Charging a capacitor means moving successive small charges $dQ$ onto it against the potential $V=Q/C$ already built up. Total work done charging from $0$ to final charge $q$:
$$U = \int_0^q \frac{Q}{C}\,dQ = \frac{q^2}{2C} = \frac{1}{2}CV^2 = \frac{1}{2}qV$$

**Subtlety worth remembering for exams:** the battery does total work $QV$, but only **half** of that, $\frac{1}{2}QV$, ends up stored as the capacitor's potential energy. The other half is dissipated as heat in the connecting wires during charging -- both statements are correct simultaneously, they're just different quantities.

### Energy density
Starting from $U = \frac{1}{2}Q^2/C$ with $C = K\varepsilon_0 A/d$ and $Q = K\varepsilon_0 E A$ (from $\sigma = Q/A = K\varepsilon_0 E$), and using $\text{volume} = Ad$:
$$\boxed{u = \frac{U}{Ad} = \frac{1}{2}K\varepsilon_0 E^2}$$
the electrostatic energy stored per unit volume of the field region (NCERT states the vacuum case $u=\frac12\varepsilon_0E^2$; this is the direct generalisation for a linear dielectric medium of constant $K$, using the field actually present inside it).

## Combination of capacitors (NCERT 2.14)

### Series (2.14.1)
Every capacitor in series carries the **same charge** $Q$ (by induction at each junction — the series analogue of current, not voltage, being shared in series resistors), while voltages **add**:
$$V = V_1+V_2+V_3 = \frac{Q}{C_1}+\frac{Q}{C_2}+\frac{Q}{C_3} \quad\Rightarrow\quad \boxed{\frac{1}{C_\text{eff}} = \frac{1}{C_1}+\frac{1}{C_2}+\frac{1}{C_3}}$$
Structurally the *opposite* of series resistors, where $R_\text{eff}=R_1+R_2+R_3$ directly.

### Parallel (2.14.2)
Every capacitor sees the **same voltage** $V$; capacitances simply add:
$$\boxed{C_\text{eff} = C' + C''}$$

### Balanced Wheatstone-bridge network of capacitors
For a bridge arrangement of five capacitors $C_1,\dots,C_5$ ($C_5$ bridging the two midpoints), if
$$\frac{C_1}{C_2} = \frac{C_3}{C_4}$$
the bridge is **balanced** and $C_5$ carries no charge — it can simply be removed from the circuit, leaving a plain series–parallel reduction of $C_1$–$C_4$.

---
*Note on this lecture's transcript:* the raw ASR transcript repeats the energy-density derivation (the "$\frac12K\varepsilon_0E^2$" section, roughly t=934s onward) two-to-three times in a row with different timestamps before moving on -- a delayed-repetition artifact, not a sign the teacher re-taught it live (a single board frame, floor_000038.jpg, shows the derivation written out exactly once). The physics content above reflects that single, real derivation; the duplicate text was not used for anything beyond confirming the same content twice.
