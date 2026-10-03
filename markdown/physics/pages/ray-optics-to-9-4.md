# Ray Optics to 9.4

*Chapter 9 · Ray Optics — 9 marks. Source: published page `b7ff23a3-c455-4f36-a2ff-f2896f06c23b`. Maths on this page is plain text, not KaTeX — it predates the KaTeX pipeline. The eighteen Ray Optics lectures have never been transcribed, so this page and the Chapter 9 sections of **Physics, Derived** and **Every Physics Formula** were written from NCERT rather than from class.*

> **Scope.** Ends at Section 9.4. Total internal reflection and its applications are the last thing on the paper — lenses, prisms, dispersion and optical instruments are all off it.

## 01 · Theory

### 1 · Spherical mirrors — the words and the sign convention

A spherical mirror is a slice cut from a hollow sphere, silvered on one side. Silver the bulging side and the reflecting face is hollow — **concave**. Silver the hollow side and the reflecting face bulges out — **convex**.

- **Pole (P)** — the centre of the reflecting surface.
- **Centre of curvature (C)** — the centre of the sphere the mirror was cut from.
- **Radius of curvature (R)** — the distance PC.
- **Principal axis** — the line PC.
- **Principal focus (F)** — where rays parallel to the axis meet after reflection (concave), or appear to come from (convex).
- **Focal length (f)** — the distance PF, and for a small aperture `f = R/2`.

Both laws of reflection hold at every point: the angle of incidence equals the angle of reflection, and incident ray, reflected ray and normal lie in one plane. The normal at any point of a spherical mirror is the radius drawn to that point. Reflection changes neither wavelength nor frequency.

**New Cartesian sign convention** — write this out before every numerical:

- All distances are measured from the pole P.
- Distances measured along the incident light are **positive**; against it, **negative**. A real object is always on the incoming side, so `u` is negative.
- Heights above the principal axis are positive, below it negative.
- Consequence: concave mirror `f` negative, convex mirror `f` positive.

### 2 · Refraction, Snell's law, refractive index

Light entering a new transparent medium changes speed, and if it meets the surface obliquely it changes direction too. That bending is refraction.

- Incident ray, refracted ray and normal lie in one plane.
- **Snell's law:** `sin i / sin r` is a constant for a given pair of media and a given wavelength. That constant is `₁n₂ = n₂/n₁`, the refractive index of medium 2 with respect to medium 1.

The **absolute refractive index** of a medium is `n = c/v` — speed of light in vacuum divided by speed in the medium. Since frequency is fixed by the source and does not change on crossing a boundary, `v = νλ` forces the wavelength to shrink in the denser medium, so `n = λ_air / λ_medium` as well.

Denser to rarer, the ray bends *away* from the normal; rarer to denser, *towards* it. Reversing the light gives `₂n₁ = 1/₁n₂`, and going round a chain of media brings you back to 1: `ₐn_w × _wn_g × _gn_a = 1`. Light passing through a parallel-sided slab emerges parallel to its original direction, only shifted sideways.

*Some questions write μ instead of n. Same quantity.*

### 3 · Total internal reflection

Send light from a denser medium towards a rarer one and it bends away from the normal, so the refracted ray leans further from the normal than the incident ray does. Push the angle of incidence up and the refracted ray eventually grazes along the surface at 90°. The angle of incidence that does this is the **critical angle C**.

**Definition to write:** the critical angle for a pair of media is the angle of incidence in the denser medium for which the angle of refraction in the rarer medium is 90°.

Beyond C there is no angle of refraction left to have, so no light crosses the boundary at all — the surface behaves as a perfect mirror and every bit of the light is reflected back into the denser medium. That is **total internal reflection**.

**The two conditions** (state both, always):

- Light must travel from the denser medium towards the rarer one.
- The angle of incidence in the denser medium must exceed the critical angle for that pair.

It is genuinely total — unlike an ordinary silvered mirror there is no absorbed fraction, so no energy is lost.

### 4 · Where total internal reflection is used

- **Optical fibre** — a thin core of glass or quartz (n ≈ 1.7) clad in a coating of lower index (n ≈ 1.5). Light entering one end at a small angle to the axis strikes the core–cladding wall well above the critical angle, is totally reflected, strikes the far wall, is totally reflected again, and so zig-zags the whole length of the fibre without leaking out. Used to carry telephone and internet signals over long distances, and in endoscopy.
- **Mirage** — on a hot road the air near the surface is hot and rarer, the air above cooler and denser. Light from the sky travelling downwards passes from denser to rarer layers, bending away from the vertical at each layer until it exceeds the critical angle and turns back upwards. The eye traces it back to the ground and sees an inverted patch of sky, read as water.
- **Brilliance of diamond** — diamond's critical angle is only about 24°, so light entering a cut stone strikes face after face above that angle and is trapped through many total reflections before finding a face it can leave by, emerging concentrated.
- **Totally reflecting prisms** — a right-angled isosceles glass prism has a critical angle near 42°, so light striking the hypotenuse at 45° is totally reflected. Used to turn a beam through 90°, through 180°, or to invert an image in binoculars and periscopes.
- **Air bubble in water** shines for the same reason — light going from water into the rarer air of the bubble is totally reflected.

### 5 · Image formation by spherical mirrors

Two of these three rays fix the image: a ray parallel to the axis reflects through F; a ray through F reflects parallel to the axis; a ray through C returns along itself.

| Mirror & object at | Image position | Nature | Size |
|---|---|---|---|
| Concave — infinity | At F | Real, inverted | Point-sized |
| Concave — beyond C | Between F and C | Real, inverted | Diminished |
| Concave — at C | At C | Real, inverted | Same size |
| Concave — between C and F | Beyond C | Real, inverted | Enlarged |
| Concave — at F | At infinity | Real, inverted | Highly enlarged |
| Concave — between F and P | Behind the mirror | Virtual, erect | Enlarged |
| Convex — anywhere | Between P and F, behind | Virtual, erect | Diminished |

A convex mirror gives a virtual erect diminished image wherever the object is put, which is why it is the driver's side mirror — a wide field of view, at the cost of making everything look further away. A concave mirror is the shaving mirror and the dentist's mirror, used inside its focus where the image is virtual, erect and magnified.

*Covering the lower half of a mirror does not cut the image in half. The rays from every point still reach the top half, so the whole image is still formed — only fewer rays arrive, so it is fainter.*

## 02 · Derivations

### D1 · Mirror formula, concave mirror

> Concave mirror with pole P, focus F, centre of curvature C. Object AB stands on the principal axis beyond C, B on the axis. A real inverted image A′B′ is formed. A ray AD from the top of the object runs parallel to the axis, strikes the mirror at D and reflects through F. DN is the perpendicular dropped from D onto the principal axis. Aperture is small.

1. In △ABC and △A′B′C: ∠ABC = ∠A′B′C = 90°
2. ∠ACB = ∠A′CB′ — *(vertically opposite)*
3. △ABC ~ △A′B′C
4. AB / A′B′ = BC / B′C …(i)
5. In △DNF and △A′B′F: ∠DNF = ∠A′B′F = 90°
6. ∠DFN = ∠A′FB′ — *(vertically opposite)*
7. △DNF ~ △A′B′F
8. DN / A′B′ = NF / B′F
9. DN = AB — *(DN is the height of the parallel ray = height of object)*
10. AB / A′B′ = NF / B′F …(ii)
11. From (i) and (ii): BC / B′C = NF / B′F
12. Aperture small ⇒ N lies very close to P ⇒ NF = PF
13. BC / B′C = PF / B′F
14. BC = PB − PC, B′C = PC − PB′, B′F = PB′ − PF
15. (PB − PC) / (PC − PB′) = PF / (PB′ − PF)
16. Sign convention: PB = −u, PB′ = −v, PF = −f, PC = −R = −2f
17. (−u + 2f) / (−2f + v) = (−f) / (−v + f)
18. (−u + 2f)(−v + f) = (−f)(−2f + v) — *(cross-multiplying)*
19. uv − uf − 2fv + 2f² = 2f² − fv
20. uv − uf − 2fv = −fv
21. uv − uf − 2fv + fv = 0
22. uv − uf − fv = 0
23. uv = uf + fv
24. uv / uvf = uf / uvf + fv / uvf — *(divide throughout by uvf)*
25. 1/f = 1/v + 1/u

**Result:** 1/v + 1/u = 1/f

**Diagram:** concave mirror on the right, axis horizontal, C and F marked with C further from P. Object arrow AB beyond C pointing up; image arrow A′B′ between C and F pointing down. Show ray AD parallel to the axis reflecting through F, and the second ray from A through C returning on itself. Mark u, v, f from P.

### D2 · Magnification for a spherical mirror

> Same concave mirror, same object AB of height h giving a real inverted image A′B′ of height h′. Take the ray that leaves the top of the object A and strikes the mirror exactly at the pole P. At P the principal axis is the normal, so this ray reflects to A′ with the angle of reflection equal to the angle of incidence.

1. Linear magnification m = h′ / h — *(height of image ÷ height of object, both signed)*
2. Ray AP strikes the pole at angle i to the axis; reflected ray PA′ leaves at angle r
3. i = r — *(law of reflection; axis is the normal at P)*
4. In right △ABP: tan i = AB / BP = h / |u|
5. In right △A′B′P: tan r = A′B′ / B′P = |h′| / |v|
6. i = r ⇒ tan i = tan r
7. h / |u| = |h′| / |v|
8. |h′| / h = |v| / |u| …(i)
9. Sign convention: u < 0, v < 0, h > 0, h′ < 0 — *(real image, inverted)*
10. |u| = −u, |v| = −v, |h′| = −h′
11. Substituting in (i): (−h′) / h = (−v) / (−u)
12. (−h′) / h = v / u
13. h′ / h = −v / u
14. m = −v / u
15. From D1: 1/v = 1/f − 1/u = (u − f) / uf
16. v = uf / (u − f)
17. m = −v/u = −[uf / (u − f)] / u = −f / (u − f)
18. m = f / (f − u)
19. From D1 again: 1/u = 1/f − 1/v = (v − f) / vf
20. u = vf / (v − f)
21. m = −v/u = −v(v − f) / vf = −(v − f) / f
22. m = (f − v) / f

**Result:** m = h′/h = −v/u = f/(f − u) = (f − v)/f

**Diagram:** the same figure as D1, with the extra ray drawn from A to the pole P and reflected down to A′, and the equal angles i and r marked on either side of the axis at P.

*Reading m: negative m means a real inverted image; positive m means a virtual erect one. |m| > 1 enlarged, |m| < 1 diminished.*

### D3 · Real depth and apparent depth at a plane surface

> An object O lies at a depth t below the flat surface of a denser medium of refractive index n (water in a tank, or a pin under a glass slab), viewed from air almost vertically above. A ray OM leaves O along the normal and passes straight out at M. A second ray OP leaves at a small angle of incidence i, meets the surface at P and refracts away from the normal into air at angle r. Extended backwards, the two emergent rays meet at I.

1. I is the virtual image of O, so real depth = OM = t and apparent depth = IM
2. In right △OMP: tan i = MP / OM
3. In right △IMP: tan r = MP / IM
4. Snell's law, denser → air: sin r / sin i = n
5. Viewed nearly vertically, P lies close to M, so i and r are small
6. sin i ≈ tan i and sin r ≈ tan r — *(small-angle approximation)*
7. n = tan r / tan i
8. n = (MP / IM) ÷ (MP / OM)
9. n = (MP / IM) × (OM / MP)
10. n = OM / IM
11. n = real depth / apparent depth
12. Apparent depth IM = OM / n = t / n
13. Apparent shift x = OM − IM = t − t/n
14. x = t (1 − 1/n)

**Result:** n = real depth / apparent depth · x = t (1 − 1/n)

**Diagram:** horizontal water line; O at depth t below M; the normal ray OM straight up; a slanted ray OP refracting away from the normal at P; both emergent rays dashed backwards to meet at I, which sits above O. Mark t, the apparent depth, and the shift x.

*Because n depends on the medium only, the shift does not depend on where the slab sits between the object and the eye.*

### D4 · Critical angle and total internal reflection

> A ray travels inside a denser medium of refractive index n_d and meets a plane boundary with a rarer medium of refractive index n_r, at angle of incidence i. Steps 1–2 are the same Snell's-law starting point as D3 — the difference is that there the small angle was tracked, here the largest one is.

> **Shared setup:** D3 and D4 both begin from Snell's law applied once at a plane surface. If you can set up one, you can set up the other.

1. Snell's law at the boundary: n_d sin i = n_r sin r
2. sin r = (n_d / n_r) sin i
3. n_d > n_r ⇒ n_d/n_r > 1 ⇒ sin r > sin i ⇒ r > i — *(bends away from the normal)*
4. As i increases, r increases faster and reaches 90° first
5. The value of i for which r = 90° is defined as the critical angle C
6. Put i = C, r = 90° in step 1: n_d sin C = n_r sin 90°
7. sin 90° = 1
8. n_d sin C = n_r
9. sin C = n_r / n_d
10. If the rarer medium is air: n_r = 1 and n_d = n
11. sin C = 1 / n
12. C = sin⁻¹ (1 / n)
13. Now take i > C. From step 2: sin r = (n_d/n_r) sin i
14. sin i > sin C ⇒ (n_d/n_r) sin i > (n_d/n_r) sin C
15. (n_d/n_r) sin C = 1 — *(from step 9)*
16. sin r > 1
17. No angle r satisfies sin r > 1, so no refracted ray can exist
18. All the incident energy returns into the denser medium — total internal reflection

**Result:** sin C = n_r/n_d = 1/n · C = sin⁻¹(1/n), and TIR for i > C

**Diagram:** one horizontal boundary, denser medium below. Draw three rays from the same point O on the surface: i < C refracting into the rarer medium; i = C with the refracted ray grazing along the boundary at 90°; i > C reflecting back into the denser medium with the reflected angle equal to i.

*n is larger for violet than for red, so C is smallest for violet — violet is totally reflected before red is.*

## 03 · Formula strip

*● must be instant · ○ a few seconds is fine*

### ● Focal length of a spherical mirror in terms of its radius of curvature

`f = R / 2` — f = focal length, R = radius of curvature. Both in metre (m). Holds for small aperture, concave and convex alike.

### ● Mirror formula

`1/v + 1/u = 1/f` — u = object distance, v = image distance, f = focal length, all measured from the pole and all in metre (m). Signed by the New Cartesian convention.

### ● Linear magnification of a mirror, in terms of u and v

`m = h′/h = −v/u` — h′ = image height, h = object height (both m). m is a pure number, no unit. Negative m = real and inverted.

### ○ Magnification of a mirror written with f instead of a height

`m = f/(f − u) = (f − v)/f` — same m, no unit. Use whichever of u or v the question gives you.

### ● Snell's law, in ratio form and in the n-on-both-sides form

`sin i / sin r = ₁n₂ = n₂/n₁ ⟺ n₁ sin i = n₂ sin r` — i = angle of incidence, r = angle of refraction (degree). n₁, n₂ = absolute refractive indices, no unit.

### ● Absolute refractive index in terms of speed

`n = c / v` — c = speed of light in vacuum = 3 × 10⁸ m s⁻¹, v = speed in the medium (m s⁻¹). n has no unit and is never less than 1.

### ○ Refractive index in terms of wavelength — and what stays fixed

`n = λ_air / λ_medium` — λ in metre (m). Frequency ν (hertz, Hz) is unchanged on refraction; the wavelength shortens in the denser medium.

### ○ Principle of reversibility, as an equation

`₁n₂ = 1 / ₂n₁` — both sides dimensionless. Swapping the two media inverts the refractive index.

### ○ Chain rule for three media in succession

`ₐn_w × _wn_g × _gn_a = 1` — air → water → glass → air. Also gives `_wn_g = ₐn_g / ₐn_w`. Dimensionless.

### ● Refractive index from real and apparent depth

`n = real depth / apparent depth` — both depths in metre (m); n dimensionless. Applies for near-normal viewing only.

### ● Apparent shift produced by a slab of thickness t

`x = t (1 − 1/n)` — t = real thickness or depth, x = shift, both in metre (m). Independent of where the slab is placed.

### ● Critical angle for a denser medium against air

`sin C = 1/n ⇒ C = sin⁻¹(1/n)` — C in degree. n = refractive index of the denser medium w.r.t. air, dimensionless.

### ○ Critical angle for any two media

`sin C = n_r / n_d` — n_r = rarer medium, n_d = denser medium, both dimensionless. Reduces to 1/n when the rarer medium is air.

### ○ Radius of the circle of light escaping from a source at depth H

`r = H tan C = H / √(n² − 1)` — H = depth of the source, r = radius of the bright circle at the surface, both in metre (m). Area escaping = πr².

### ○ Speed of light inside a medium of index n

`v = c / n` — v in m s⁻¹. Combine with n = real/apparent depth to get v straight from a depth measurement.

## 04 · Questions to attempt

*Question numbers only, from Xam Idea Chapter 9 and the NCERT questions reprinted inside it. Section names are Xam Idea's own.*

### Tier 1 — must do

*15 questions · these are the 3-mark and 5-mark slots*

| Question | Page | Why |
|---|---|---|
| Long Answer Q1 | p. 344 | The 5-marker |
| Practice Q40 | p. 362 | Same derivation |
| Short Answer Q1 | p. 331 | Full TIR set |
| Short Answer Q2 (a) | p. 331 | Reasoning from formula |
| Short Answer Q7 | p. 334 | Optical fibre, guaranteed |
| Short Answer Q10 | p. 335 | Two sign cases |
| Short Answer Q11 | p. 336 | Two-equation chain |
| Very Short Ans Q19 | p. 324 | Proves f = R/2 |
| Very Short Ans Q4 | p. 319 | Definition plus geometry |
| Very Short Ans Q2 | p. 318 | Two mirror equations |
| NCERT Q15 | p. 298 | All mirror cases |
| NCERT Q17 | p. 299 | Fibre, full numerical |
| NCERT Q5 | p. 294 | Critical-angle cone |
| NCERT Q3 | p. 293 | Real versus apparent |
| Practice Q5 | p. 359 | Conditions plus graph |

### Tier 2 — if time

*extra pattern coverage, mostly 1 and 2 marks*

| Question | Page | Why |
|---|---|---|
| MCQ 2, 13, 14, 15 | p. 307–308 | TIR one-markers |
| MCQ 7, 12 | p. 308 | Index from depth, speed |
| MCQ 9, 10 | p. 308 | Mirror one-markers |
| Case-based Q4 (i)–(iv) | p. 313 | Whole TIR case study |
| Case-based Q2 (i) | p. 312 | The R/H result |
| NCERT Q1, Q2 | p. 293 | Plain mirror drills |
| NCERT Q4, Q16 | p. 293, 299 | Snell chain, slab shift |
| NCERT Q30 | p. 306 | Mirror turns, ray turns 2θ |
| Very Short Ans Q12 | p. 322 | Snell in a sphere |
| Practice Q12, Q26 | p. 360, 361 | Half-mirror reasoning |
| Practice Q14, Q22, Q24, Q33 | p. 360–361 | Mirror numericals |
| Practice Q25 | p. 361 | Why convex is virtual |
| Practice Q6, Q31 | p. 359, 361 | Index, speed, wavelength |

### Tier 3 — skip unless revising

*out of scope, or right physics in a banned frame*

**Off the syllabus entirely — do not open:** NCERT `Q6–Q14, Q18–Q29, Q31`. MCQ `3, 4, 5, 6, 8, 11, 16–27`. Very Short Answer `Q1, Q3, Q5–Q10, Q13–Q18, Q20–Q34, Q36`. Short Answer `Q2(b), Q3, Q4, Q5, Q6, Q8, Q9, Q12, Q13`. Long Answer `Q2–Q12` — every one of them is a lens, prism or instrument derivation. Case-based `Q1, Q3`. Practice `1(ii)–(v), 2, 3, 4, 8, 9, 10, 11, 13, 15, 17–21, 23, 27–30, 32, 34, 36–39`.

**Correct TIR physics wearing a prism, so the setup is unexaminable:** NCERT `Q21`, Very Short Answer `Q35, Q37`, Practice `Q7, Q16, Q35`. Read them only if you have finished Tiers 1 and 2 and want more critical-angle practice.

### The five numerical types this chapter can ask

1. **Find the image of an object in a spherical mirror** — `1/v + 1/u = 1/f` (then m = −v/u)
2. **Object or mirror moved, or two positions giving the same magnification** — `m = −v/u`, with f = R/2 fixed
3. **Depth of a coin, pin or needle seen through water or a slab** — `n = real depth / apparent depth` (shift x = t(1 − 1/n))
4. **Onset of total internal reflection — fibre, tank, diamond, bubble** — `sin C = 1/n`
5. **Bending, speed or wavelength across one interface or a stack** — `n₁ sin i = n₂ sin r`, with n = c/v = λ_air/λ_medium
