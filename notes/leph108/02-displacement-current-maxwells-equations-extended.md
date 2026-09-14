# Displacement Current, Maxwell's Equations, and the E-B Symmetry

**NCERT sections covered:** 8.1, 8.2

## Relationship to the other Displacement-Current lecture in this chapter

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

## The problem with Ampere's circuital law (NCERT 8.2)

Ampere's circuital law states $\oint \vec B \cdot d\vec l = \mu_0 I$. For a capacitor being
charged by a time-varying current $i(t)$, two different surfaces bounded by the same loop give
different answers: a small surface $C_1$ that the wire's conduction current pierces gives
$\oint \vec B\cdot d\vec l = \mu_0 I$, while a larger surface $C_2$ bulging through the capacitor
gap (where no conduction current crosses) gives $\oint \vec B \cdot d\vec l = 0$. Same loop, same
law, two different results -- and the same picture looks like it violates Kirchhoff's junction
rule too, since current flowing in at a point $P$ seems to vanish across the gap and reappear at
a point $Q$ on the other plate.

## Displacement current and the modified Ampere-Maxwell law (NCERT 8.2)

Between the plates, $\Phi_E = \vec E\cdot\vec A = Q/\varepsilon_0$. As the current varies, the
charge on the plates -- and hence $\Phi_E$ -- changes with time. Outside the plates only
conduction current flows; inside the gap only **displacement current**,

$$I_d = \varepsilon_0\frac{d\Phi_E}{dt}$$

flows, with $I_c = I_d$. This gives the corrected, general Ampere-Maxwell law:

$$\oint \vec B \cdot d\vec l = \mu_0 I_c + \mu_0\varepsilon_0\frac{d\Phi_E}{dt} = \mu_0(I_c + I_d)$$

With displacement current in the picture, Kirchhoff's rule is no longer violated -- current just
outside $P$ is conduction current, current in the gap is displacement current, and the two are
equal, so the total current is continuous through the whole loop after all.

### A symmetry worth noting
The lecture pauses here to connect this back to electromagnetic induction (Ch. 7): a
time-varying **magnetic** field generates an **electric** field (Faraday's law). The
displacement-current result just derived shows the converse also holds -- a time-varying
**electric** field generates a **magnetic** field. The two effects are symmetric/interchangeable,
which is part of why light (an oscillating $E$ and $B$ sustaining each other) can propagate
without a medium.

## Maxwell's four equations (NCERT 8.2, boxed summary)

1. **Gauss's law of electrostatics:** $\oint \vec E\cdot d\vec s = Q/\varepsilon_0$
2. **Gauss's law of magnetostatics:** $\oint \vec B\cdot d\vec s = 0$
3. **Faraday's law of EMI:** $\text{emf} = -d\Phi/dt$, i.e. $\oint \vec E\cdot d\vec l = -d\Phi_B/dt$
4. **Modified Ampere-Maxwell law:** $\oint \vec B\cdot d\vec l = \mu_0\left(I_c + \varepsilon_0\dfrac{d\Phi_E}{dt}\right)$

Matches NCERT's boxed list in 8.2 exactly, same four laws and order. The board's final line for
this lecture -- "light is EM waves $\Rightarrow$ it consists of electric field and magnetic field
intensities" -- previews the chapter's next topic (NCERT 8.1's remark that Maxwell's predicted EM
wave speed matching light's speed is what identifies light itself as an electromagnetic wave).

## A note on this lecture's transcript

Coverage checks report 103.5% and pass cleanly, but (as with lecture 01) that is misleading --
the transcript's real content cuts off mid-sentence while defining EMF, before the fourth
equation is explicitly re-stated in the summary and before the "light is EM waves" note. Both are
grounded from board frames only -- see the uncertain span below. Unlike lecture 01, though, this
transcript *does* narrate all four equations by name and formula, and derives displacement
current with a fully spoken formula, before that late cutoff -- so the gap here is much smaller
and confined to the closing recap.


## Verify these spans
- [16:40–17:43] check_coverage() reports 103.5% coverage and passes cleanly (the last segment is timestamped 1036.5-1101.1s, overshooting the video's verified true duration of 1063.3s by ~38s) -- the same 'clean-looking but misleading' pattern seen in the companion lecture 01. The delayed-duplicate scanner found no repeated block here either (only one short flagged pair, segments 27 vs 30 at ratio 0.73, which is just the teacher naturally repeating the short phrase 'modified ampere circuited law' a few sentences apart, not a real loop). The transcript's actual content, however, cuts off mid-sentence while defining EMF from Faraday's law ('...we can also write EMF as...'). Two things past that cutoff are grounded from board frames only: the explicit restatement of Maxwell's 4th equation in the summary list (already independently derived and narrated earlier in the lecture, at ~610-655s, so this is a recap gap, not a missing-content gap), and the 'light is EM waves' bridging note, which is not spoken anywhere in the available transcript at all. Frame floor_000052 (t=1020s), close to the true end of the video, is a direct continuation of the same board page built up continuously from floor_000041 onward, so it is trusted as belonging to this lecture.