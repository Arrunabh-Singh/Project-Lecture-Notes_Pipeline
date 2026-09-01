# Oersted's Experiment, Biot-Savart Law, and Field at the Centre of a Coil

**NCERT sections covered:** 4.1, 4.4, 4.5

## Historical introduction (NCERT 4.1)
Magnetism was first known through **lodestone**, a naturally magnetised form of magnetite (an iron ore, $\text{Fe}_3\text{O}_4$), which attracts small pieces of iron. The realisation that electricity and magnetism are connected -- that electricity can produce a magnetic field and a magnetic field can (in turn) produce an electric field -- gave rise to the unified subject of **electromagnetism**, associated with Faraday and Maxwell. A moving charge, or equivalently a **current element** $I\,d\vec l$ (a small length $d\vec l$ of current-carrying wire), is a source of magnetic field.

### Oersted's experiment
A compass needle placed near a current-carrying wire deflects when current flows, showing that a current-carrying wire produces a magnetic field around it -- the first experimental link between electricity and magnetism.

**Teacher's 'SNOW' deflection rule** (a memory device, not itself an NCERT term): if current flows from **S**outh to **N**orth and the wire is **O**ver the needle, the needle's north pole deflects toward **W**est. Reversing the current direction (N to S) flips the deflection to East; placing the wire below the needle instead of above it also flips the result. Physically this is just a special case of the general right-hand rule for the circular field around a straight wire, applied to the fixed N-S rest orientation of a compass needle.

## Magnetic field lines
Compared with electric field lines (Chapter 1):
- **Magnetic field lines always close on themselves** (outside a bar magnet they run N $\to$ S; inside the magnet, S $\to$ N) -- there is no starting or ending point.
- **Electric field lines never form closed loops** -- they start on positive charge and terminate on negative charge. This is the key structural difference between the two, and NCERT states it explicitly (Sec. 4.4, and again in the chapter summary).
- Field lines of either kind **never intersect**: at a crossing point the tangent (which gives the field direction) would have to point in two directions at once, which is impossible.
- **Parallel, equally spaced lines** indicate a **uniform** field; **crowded** lines indicate a stronger field magnitude.

## Biot-Savart law (NCERT 4.4)
For a current element $I\,d\vec l$ carrying current $I$, the magnetic field $d\vec B$ it produces at a point $P$, a distance $r$ away, obeys:

1. $dB \propto I\,dl$
2. $dB \propto \sin\theta$, where $\theta$ is the angle between the current element and the line joining the element to $P$
3. $dB \propto \dfrac{1}{r^2}$

Combining these (in exact analogy with Coulomb's law, replacing $\frac{1}{4\pi\varepsilon_0}$ with $\frac{\mu_0}{4\pi}$):
$$dB = \frac{\mu_0}{4\pi}\,\frac{I\,dl\sin\theta}{r^2}$$

In vector form, since the $\sin\theta$ dependence signals a cross product:
$$d\vec B = \frac{\mu_0}{4\pi}\,\frac{I\,d\vec l \times \hat r}{r^2} = \frac{\mu_0}{4\pi}\,\frac{I\,d\vec l \times \vec r}{r^3}$$

### Finding the direction of $d\vec B$
Three equivalent right-hand rules were used on the board:
1. **Right-hand palm rule:** point the thumb along the current, the centre finger toward $P$; the palm then faces the direction the field emerges from (out of the page $\odot$, or into the page $\otimes$).
2. **Right-hand thumb rule (for a straight wire):** hold the wire with the thumb pointing along the current; the curled fingers give the sense of circulation of $\vec B$ around the wire.
3. **Right-hand screw rule:** $\vec B$ is perpendicular to the plane containing $d\vec l$ and $\hat r$, in the sense obtained by imagining the rotation carrying $d\vec l$ toward $\hat r$ -- this is the exact rule NCERT itself gives as a footnote to the Biot-Savart law. This rule, and the label "$\mu_0$ = permeability of free space", appear worked out on the board but are **not narrated in the transcript at all** -- see the flagged span below.

**Worked example** (from the board): for a vertical wire carrying current downward, with $P$ to its side, the palm-rule construction (thumb down, centre finger toward $P$) gives a palm facing outward, so $\vec B$ at $P$ points out of the page.

## Magnetic field at the centre of a current-carrying circular coil (NCERT 4.5, special case)
For a circular coil of radius $R$ carrying current $I$, every current element $I\,dl$ on the coil is at the same perpendicular distance $R$ from the centre, with $\theta = 90^\circ$ (so $\sin\theta = 1$). By the Biot-Savart law,
$$dB = \frac{\mu_0}{4\pi}\frac{I\,dl}{R^2}$$
Integrating around the full circumference ($\oint dl = 2\pi R$):
$$B = \oint dB = \frac{\mu_0}{4\pi}\frac{I}{R^2}(2\pi R)$$
$$\boxed{B = \frac{\mu_0 I}{2R}}$$
This matches NCERT's own derivation in Sec. 4.5, which reaches the same field-at-the-centre result as the $x=0$ special case of the more general on-axis formula $B = \dfrac{\mu_0 I R^2}{2(x^2+R^2)^{3/2}}$ (the general axis formula itself is developed in the next lecture). The board also sketches the closed-loop field-line pattern threading through a current-carrying loop, consistent with NCERT Fig. 4.10.


## Verify these spans
- [36:50–37:17] Board frames (floor_000068 at 1340s, floor_000077 at 1520s) show a third direction rule -- the 'right-hand screw rule', with a diagram and the label 'mu0 = permeability of free space' -- fully written out on the same page as rules 1 and 2. The transcript, however, never narrates this rule or these words at all ('screw' and 'permeability' have zero hits across the full 141-segment transcript): after finishing rule 2 (right-hand thumb rule, ending ~2210s) it jumps directly to a worked direction example at 2237s and then on to the coil derivation. Automated coverage and repetition checks both pass cleanly here (no duplicated block, no duration overshoot) -- this is a case of the ASR silently skipping real board content rather than looping, not a duration or repetition failure. The screw-rule claim above is grounded from the board frames alone.