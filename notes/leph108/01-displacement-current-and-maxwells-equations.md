# Displacement Current and Maxwell's Equations

**NCERT sections covered:** 8.1, 8.2

## The problem with Ampere's circuital law (NCERT 8.2)

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

## Maxwell's resolution: displacement current (NCERT 8.2)

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

## Maxwell's four equations (NCERT 8.2, boxed summary)

The board closes the lecture by collecting the complete set of Maxwell's equations in vacuum:

1. **Gauss's law of electrostatics:** $\oint \vec E \cdot d\vec A = Q/\varepsilon_0$
2. **Gauss's law of magnetostatics:** $\oint \vec B \cdot d\vec A = 0$
3. **Faraday's law of EMI:** $\oint \vec E \cdot d\vec l = -\dfrac{d\Phi_B}{dt}$ (i.e. $\varepsilon = -d\phi/dt$)
4. **Modified (Ampere-Maxwell) circuital law:** $\oint \vec B \cdot d\vec l = \mu_0\left(I_c + \varepsilon_0\dfrac{d\Phi_E}{dt}\right)$

This is exactly NCERT's boxed list in section 8.2, same four laws, same order.

## A note on this lecture's transcript

The automated coverage check reports 107% coverage and passes cleanly, but that is misleading
here -- see the uncertain span below. The ASR transcript's real content stalls mid-derivation
(still building $\Phi_E = E\cdot A$) and its last captured sentence cuts off mid-word. It never
narrates the differentiation step, the $I=I_c+I_d$ statement, or Maxwell's four equations by
name at all, even though the board frames show all of this written out, in a natural progressive
build on the same page, well within the lecture's verified 980.19s duration. The final three
claims above (differentiation/$I_d$, and Maxwell's four equations) are therefore grounded from
board frames only.


## Verify these spans
- [13:50–16:20] The transcript's own final segment is timestamped 968.0-1056.0s, which overshoots the video's verified true duration (980.19s) by ~76s -- exactly the 'coverage looks clean but isn't' trap: check_coverage() reports 107% coverage and passes, yet the segment's text cuts off mid-word ('...electric field direction is this is the direction o'), and the delayed-duplicate scanner found no repeated block (0 flagged pairs), so this is neither of the two previously-catalogued failure modes cleanly -- it looks like a silent truncation whose tail segment was also given a stretched/overshot timestamp. Either way, the transcript's real captured content stalls partway through the displacement-current derivation (still building Phi_E = E.A) and never reaches the differentiation step (I_d = eps0 dPhi_E/dt), the I=Ic+Id statement, or any mention of 'Maxwell's equations' / 'Gauss's law' / 'Faraday's law' by name. The board frames, however, show this content completed and written out in full: floor_000030 (sampled at video t=580s -- notably BEFORE the transcript's own claimed timestamp for the Phi_E=E.A discussion, another sign the transcript's internal timestamps are not reliable in this stretch) already has the differentiation and I=Ic+Id; floor_000043 (t=840s) has Maxwell's equations 1-2 being written; floor_000049 (t=960s, near the true end) has all four complete. These three frames sit on the same continuously-built board page as the earlier, transcript-confirmed derivation (visible progression, not a jump to an unrelated page), which is why they are trusted as belonging to this lecture despite having no matching transcript span -- grounded from board frames alone, per claims 7 and 8 above.