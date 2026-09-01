# Electrostatic Induction, Charge Unit Conversions, and Coulomb's Law

**NCERT sections covered:** 1.4, 1.5

## Electrostatic induction

Charging a conducting body **without physical contact**, by bringing a charged rod nearby:

1. Bring a negatively-charged rod near a grounded conducting sphere (mounted on an insulating stand). By induction, positive charge accumulates on the near side (attracted toward the rod) and negative charge on the far side (repelled free electrons).
2. Ground the sphere: the repelled negative charges flow away into the ground (an effectively infinite charge reservoir), while the positive charges stay put, held by attraction to the rod.
3. Remove the ground connection first, *then* remove the rod.
4. The remaining positive charge redistributes itself uniformly over the sphere (charges settle into the configuration of minimum potential energy) — the sphere is now charged **positively**, without ever touching a charged body to it.

(The gold leaf electroscope shows the same effect: bringing a charged rod near *without touching* still induces a charge separation that causes the leaves to diverge.)

## Worked numerical: charge content of water
How many positive and negative (elementary) charges are in $250$ mL of water? Using $1$ mL $=1$ g, water's molar mass $18$ g/mol ($2\times1+16$), Avogadro's number $6.023\times10^{23}$ molecules/mol, and $10$ protons + $10$ electrons per H$_2$O molecule (O contributes 8, each H contributes 1):
$$\text{molecules in } 250\text{ g} = 6.023\times10^{23}\times\frac{250}{18}$$
Total positive charge count = total negative charge count = $10\times$ that number of molecules.

## Coulomb's law (NCERT 1.5)

**Recap — Newton's law of gravitation:** $F = \dfrac{Gm_1m_2}{r^2}$ — always attractive, independent of the medium between the masses (a universal law).

**Coulomb's law:** for two **point charges** $Q_1,Q_2$ (valid only when their separation is much larger than their own physical size — the electrostatic analogue of a "point object") separated by $r$:
$$F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r^2} = k\frac{Q_1Q_2}{r^2},\qquad k=\frac{1}{4\pi\varepsilon_0}=9\times10^9~\text{N m}^2\text{C}^{-2}$$

**Compared with gravity:** both are central forces (act along the line joining the two objects) and both obey Newton's third law ($\vec F_{12}=-\vec F_{21}$) — but Coulomb's force can be attractive *or* repulsive (gravity is always attractive), and it *depends on the medium* between the charges (gravity doesn't).

### Definition of 1 coulomb
Setting $Q_1=Q_2=1$ C, $r=1$ m: $F = 9\times10^9$ N. So **1 coulomb** is the charge that, placed 1 m from an identical charge in vacuum, repels it with a force of $9\times10^9$ N — evidently an enormous unit for practical electrostatics.

### A note on mass and charging
Charging a body very slightly changes its mass: charging it **negatively** (adding electrons) **increases** mass; charging it **positively** (removing electrons) **decreases** mass.

### Why the coulomb is "too big" a unit, and sub-units (NCERT 1.4)
Practical electrostatics uses smaller sub-units: $1~\text{mC}=10^{-3}$ C, $1~\mu\text{C}=10^{-6}$ C, $1~\text{nC}=10^{-9}$ C. Since charge is quantised ($Q=ne$), 1 coulomb corresponds to
$$n = \frac{1}{1.6\times10^{-19}} = \frac{10^{19}}{1.6} \approx 6.25\times10^{18}$$
elementary charges — consistent with NCERT's own statement that there are about $6\times10^{18}$ electrons in a charge of $-1$ C.

---
*Note on this lecture's transcript:* the unit-conversion / electron-count material just above is grounded entirely from a board frame near the true end of the lecture -- the transcript itself loops back and repeats the water-numerical and gravitation recap instead of transcribing it. See the flagged span below.


## Verify these spans
- [30:29–36:24] The raw ASR transcript loops back after finishing the Coulomb's-law derivation (ending around t=1829s with F=9e9 N for the 1-coulomb definition) and re-transcribes the earlier 'how many charges in 250mL of water' numerical and Newton's-gravitation recap almost verbatim from t=1854s to the transcript's last segment at t=2182s -- a delayed-repetition artifact matching the pattern found repeatedly in this chapter's sibling chapter (Ch2). Board frames tell a different story: floor_000109.jpg (t=2160s, the last captured frame, well within this window) shows a page titled with a '5C, 1C -> very very large value' remark, unit conversions (1mC/microC/nC), and a worked calculation of how many electrons make up 1 coulomb (n=10^19/1.6) -- standard NCERT Section 1.4 content on why the coulomb is an impractically large unit -- none of which appears anywhere in the transcript. The unit-conversion and electron-count claim above is grounded entirely from that board frame.