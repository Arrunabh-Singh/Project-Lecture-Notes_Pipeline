# Redistribution of Charges, Dielectric Strength, and Kirchhoff's Laws for Capacitor Networks

**NCERT sections covered:** 2.11

## Redistribution of charges (NCERT 2.11, cf. Example 2.10)

Two capacitors, separately charged ($Q_1=C_1V_1$, $Q_2=C_2V_2$), connected together (positive plate to positive plate): once connected, charge redistributes until both reach the **same potential** $V$. This makes them effectively **parallel** (same $V$, different $Q_1', Q_2'$), even though the connection can visually resemble a series arrangement.

By charge conservation, $Q_1+Q_2 = Q_1'+Q_2'$, and the common potential is:
$$V = \frac{Q_1+Q_2}{C_1+C_2} = \frac{C_1V_1+C_2V_2}{C_1+C_2}$$

### Energy loss on redistribution
Even though charge is conserved, energy is **not**. Using $U=\frac12CV^2$ for the initial (separate) and final (common-potential) states and simplifying:
$$\Delta U = U_i - U_f = \frac{1}{2}\frac{C_1C_2}{C_1+C_2}(V_1-V_2)^2$$
This is always $\geq 0$ (a squared quantity), so $U_i \geq U_f$ whenever $V_1\neq V_2$ — the "lost" energy is dissipated as heat in the connecting wires during the transient redistribution. Nothing about this process is free.

**Worked numerical** (matching the structure of NCERT Example 2.10): a $10~\mu\text{F}$ capacitor charged by $30$ V DC is connected to an uncharged $50~\mu\text{F}$ capacitor — find the common potential, the initial and final energies, and account for the difference.

### Worked example: which way do charges flow?
Two spheres — radius $r$ with charge $+q$, radius $R$ with charge $+Q$ — connected by a wire. Using potential-inside-a-sphere-equals-potential-on-surface (from an earlier lecture):
$$V_A - V_B = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{r}-\frac{1}{R}\right)$$
Since $r<R$, this is positive, so $V_A > V_B$: charges flow from the **smaller** sphere to the **larger** one. The general rule is charges flow from **higher to lower potential**, not simply from "more charge" to "less charge" — the two are not the same thing.

## Dielectric strength (NCERT 2.11)

Distinct from dielectric constant $K$ (dimensionless): the **dielectric strength** of a material is the maximum electric field it can withstand without breakdown of its insulating property. Vacuum's dielectric strength is infinite (nothing there to ionise); air's is about $3\times10^6$ V/m. Beyond this field, bound charges get torn free and the material starts conducting, letting stored charge leak away — this is why a capacitor's practical charge-storage limit is set by breakdown, not just by $C=Q/V$ alone.

## Kirchhoff's laws for capacitor networks

1. **Charge conservation in an isolated system:** the net charge is constant, $\sum Q = 0$ for any change.
2. **Loop rule:** around any closed loop in a capacitor network, $\sum V + \sum \dfrac{Q}{C} = 0$ — the capacitor-network analogue of Kirchhoff's voltage law used for resistor circuits (covered in the Current Electricity chapter).

---
*Note on this lecture's transcript:* the Kirchhoff's-laws section above is grounded entirely from a board frame -- the transcript's own narration never reaches it, instead getting stuck repeating a dielectric-strength worked example and ending on an unresolved question. See the flagged span below.


## Verify these spans
- [38:00–43:10] Board frames show a page titled 'Kirchhoff's laws in capacitors' beginning to be written at t=2120s (floor_000107, page still blank) and fully complete with both stated laws and a worked circuit by t=2240s (floor_000113) -- comfortably within this lecture's own duration and matching the third topic named in its filename. The transcript, however, never once mentions Kirchhoff -- its own narration is still mid-way through the dielectric-strength discussion (vacuum/air breakdown fields, a paper-capacitor breakdown example, and a 'can you charge a 1m-radius sphere with 1 coulomb?' worked question) right up to its last segment at t=2603s, with the paper-breakdown example itself repeated near-verbatim twice (t=2378-2467s and again t=2499-2581s) before the transcript ends without ever resolving the sphere-charging question. This matches the same delayed-repetition-then-substitution pattern found in other lectures in this chapter. The Kirchhoff's-laws claim above is grounded entirely from the board frame; the dielectric-strength claim above uses only the transcript's first (non-duplicated) pass through that material.