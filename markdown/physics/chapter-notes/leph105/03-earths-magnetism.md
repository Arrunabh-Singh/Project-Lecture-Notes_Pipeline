# The Earth's Magnetism: Dynamo Effect, Magnetic Axis, and Elements of the Field

## A note on syllabus scope
**This entire lecture covers material that has been removed from the current (rationalised, 2022-23 onward) NCERT Class 12 Physics syllabus.** The current NCERT Chapter 5 raw text jumps directly from Section 5.3 (Magnetism and Gauss's Law) to Section 5.4 (Magnetisation and Magnetic Intensity), with no "Earth's Magnetism" section at all -- in the pre-rationalisation NCERT this was Section 5.4, covering exactly the dynamo-effect theory, magnetic vs. geographic axis, and the three elements (declination, dip, horizontal component) taught in this lecture. Every claim below is therefore given `ncert_section=None` rather than forced onto a current-syllabus number; nothing here should be treated as CBSE-examinable under the present syllabus, though it remains standard, correct physics and is commonly retained in classroom teaching for conceptual completeness (and because some boards/older question banks still reference it).

## Why the earth behaves as a magnet: the dynamo effect
Two historical explanations are contrasted. A "huge bar magnet buried inside the earth" is ruled out, since the core's temperature is far above any material's Curie point -- a permanent magnet simply could not survive there. The accepted picture instead is the **dynamo effect**: the earth's core contains molten iron and nickel existing as mobile ions; their large-scale motion constitutes electric currents, and a moving charge always produces a magnetic field -- this circulating current system is the real source of the earth's magnetism.

## Magnetic axis vs. geographic axis
Treating the earth as though it contains an internal short bar magnet, its **magnetic axis** (through the magnetic N/S poles) is tilted at **11.3°** to the **geographic axis** (the earth's rotation axis, through the true/geographic N/S poles). Since a freely suspended compass needle's own north pole always swings toward geographic north (opposite poles attract), the pole of the earth's "internal magnet" lying near geographic north must, strictly, be a south pole -- but by long-standing convention it is still labelled the earth's "magnetic north pole."

**Field-line direction examples:** with field lines running (loosely) from geographic south to geographic north outside the earth,
- at a place near the geographic south (e.g. **Australia**), field lines appear to emerge **out of** the ground;
- at a place near the geographic north (e.g. **Britain**), field lines appear to go **into** the ground.

## Geographic vs. magnetic: axis, equator, meridian
| Geographic | Magnetic |
|---|---|
| **Axis:** line through geographic N & S poles (earth's rotation axis) | **Axis:** line through magnetic N & S poles |
| **Equator:** great circle perpendicular to the geographic axis | **Equator:** great circle perpendicular to the magnetic axis |
| **Meridian:** vertical plane containing the geographic axis at a place | **Meridian:** vertical plane containing the magnetic axis at a place |

At any given place, the geographic meridian and magnetic meridian planes generally differ by some angle -- which is precisely the first "element" of earth's magnetic field, below.

## The three elements of earth's magnetic field
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


## Verify these spans
- [22:49–22:57] The transcript's last segment (index 92, 1369.5-1405.7s) only NAMES 'angle of dip, also known as magnetic inclination' and then stops entirely -- it never defines the term, never introduces the horizontal component (the 3rd of the '3 elements' the teacher explicitly enumerates at segment 78), and never derives the B_H/B_V/tan(delta) relations or the equator/pole special cases. This does not look like the delayed-repeat fabrication loop (nothing upstream is re-transcribed) -- it reads as the ASR response simply running out near the true end of the audio, similar to lecture 2 in this chapter. The coverage-floor sampler's deduped index.json also stops at t=1200s (floor_000061), but as in lecture 2, the raw frames folder retains later non-deduped frames (up to floor_000069, confirmed to exist and checked directly) that show the angle-of-dip definition fully written out plus the entire horizontal-component derivation with all four equations and both special-case results -- this is a real, temporally progressive board build-up (declination alone at t~860s and t~1140s, dip's definition text complete by the 65th raw frame, horizontal-component equations and special cases added afterward at the 66th-69th raw frames), not an isolated out-of-place frame. Both element-2 and element-3 claims above are grounded from these board-only frames, with no transcript corroboration at all -- flagged here since narration could not confirm them, though the content is standard and consistent with the board's own stated 3-element structure.