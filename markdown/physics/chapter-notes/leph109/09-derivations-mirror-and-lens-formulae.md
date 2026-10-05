# Derivations: f = R/2, Mirror Formula, Lens Formula, Lenses in Contact

**NCERT sections covered:** 9.2.2, 9.2.3, 9.5.2, 9.5.4


Four derivations, each with its assumption stated first. The lecture stresses writing the assumption in the exam.

## 1. Relation between f and R for a spherical mirror (NCERT 9.2.2)

**Assumption: the aperture of the mirror is small.**

**Concave mirror.**

1. A ray parallel to the principal axis strikes the mirror at M and reflects through F.
2. CM is the normal at M, so $\angle i = \angle r$.
3. $\angle FCM = i$ (alternate angles, since the incident ray is parallel to the axis), and $\angle FMC = r = i$.
4. So $\triangle CFM$ is **isosceles**, and $CF = FM$.
5. Because the aperture is small, M is very close to P, so $FM \approx FP$.
6. Hence $CF = FP$: **F is the midpoint of P and C**, and $R = PC = 2\,PF$:

$$R = 2f \qquad\text{or}\qquad f = \frac{R}{2}$$

**Convex mirror.** The same steps work behind the mirror:

- the normal at M is CM produced;
- the reflected ray produced backwards passes through F;
- $\triangle FMC$ is isosceles with $FM = FC$;
- small aperture gives $FP = FC$, so again $R = 2f$.

## 2. Mirror formula (NCERT 9.2.3)

**Assumption: the aperture of the mirror is small.**

**Setup.** Take a concave mirror with object AB beyond C.

- The ray from B parallel to the axis hits the mirror at M and reflects through F. The ray from B through F reflects parallel. They meet at B′, so the image A′B′ is between C and F.
- Drop MN perpendicular to the axis. Then $MN = AB$, and by the small aperture, N ≈ P.
- Distances: $PA = u$, $PA' = v$, $PF = f$, so $FA' = PA' - PF = v - f$.

**Triangles A′B′F and MNF are similar:**
$$\frac{A'B'}{AB} = \frac{FA'}{PF} = \frac{v - f}{f} \qquad (1)$$

**Triangles ABP and A′B′P are similar** (the ray to the pole reflects at equal angles):
$$\frac{A'B'}{AB} = \frac{PA'}{PA} = \frac{v}{u} \qquad (2)$$

**Magnification from (2).** A′B′ is below the axis, so $A'B' = -h_i$, while $PA' = -v$ and $PA = -u$:
$$\frac{-h_i}{h_o} = \frac{-v}{-u} \;\Rightarrow\; m = \frac{h_i}{h_o} = -\frac{v}{u}$$

**Equating (1) and (2) and putting in the sign convention** ($u \to -u$, $v \to -v$, $f \to -f$ for a concave mirror with a real image):
$$\frac{-v - (-f)}{-f} = \frac{-v}{-u} \;\Rightarrow\; \frac{-v + f}{-f} = \frac{v}{u}$$
Cross-multiplying gives $-uv + uf = -vf$. Dividing by $uvf$:
$$-\frac{1}{f} + \frac{1}{v} = -\frac{1}{u} \;\Rightarrow\; \boxed{\frac{1}{f} = \frac{1}{v} + \frac{1}{u}}$$

## 3. Lens formula (convex lens)

**Assumption: the lens is thin.** The ray through O then goes undeviated, and distances can be measured from O.

**Setup.** Object AB is between F and 2F, and the image A′B′ is beyond 2F on the other side.

- The ray from B parallel to the axis meets the lens at P (so $OP = AB$) and refracts through F.
- The ray from B through O goes straight on.
- Distances: $OA = u$, $OA' = v$, $OF = f$, so $FA' = v - f$.

**Triangles ABO and A′B′O are similar:**
$$\frac{A'B'}{AB} = \frac{OA'}{OA} = \frac{v}{u} \qquad (1)$$

**Triangles POF and A′B′F are similar** (with $OP = AB$):
$$\frac{A'B'}{AB} = \frac{FA'}{OF} = \frac{v - f}{f} \qquad (2)$$

**Magnification from (1).** With $A'B' = -h_i$, $OA' = +v$ and $OA = -u$:
$$\frac{-h_i}{h_o} = \frac{v}{-u} \;\Rightarrow\; m = \frac{h_i}{h_o} = \frac{v}{u}$$

There is no minus sign here, unlike a mirror.

**Equating (1) and (2) with signs** ($OA = -u$, $OA' = +v$, $OF = +f$):
$$\frac{v}{-u} = \frac{v - f}{f} \;\Rightarrow\; vf = -uv + uf$$
Dividing by $uvf$:
$$\frac{1}{u} = -\frac{1}{f} + \frac{1}{v} \;\Rightarrow\; \boxed{\frac{1}{f} = \frac{1}{v} - \frac{1}{u}}$$

*(When setting this up, the teacher at one point says "OA′ = −v"; the board and the working use $OA' = +v$. NCERT itself reaches the lens formula differently, by combining refraction at the two spherical surfaces — see lecture 11.)*

## 4. Combination of thin lenses in contact (NCERT 9.5.4)

This derivation has been asked in board exams. **Assumption: the lenses are thin**, so their thickness and separation are negligible, and u and v can be measured from either lens.

**Setup.**

- Two lenses $L_1$ (focal length $f_1$) and $L_2$ (focal length $f_2$) are in contact.
- An object O is at distance $u$.
- Lens 1 alone would form an image $I'$ at distance $v'$.
- $I'$ acts as a **virtual object** for lens 2, which forms the final image I at distance $v$.

**For lens 1:**
$$\frac{1}{f_1} = \frac{1}{v'} - \frac{1}{u} \qquad (1)$$

**For lens 2:**
$$\frac{1}{f_2} = \frac{1}{v} - \frac{1}{v'} \qquad (2)$$

**Adding (1) and (2)**, the $1/v'$ terms cancel:
$$\frac{1}{v} - \frac{1}{u} = \frac{1}{f_1} + \frac{1}{f_2}$$

The pair behaves as a single lens that takes an object at $u$ to an image at $v$. Its focal length $f$ therefore satisfies $\frac{1}{v} - \frac{1}{u} = \frac{1}{f}$, so

$$\boxed{\frac{1}{f} = \frac{1}{f_1} + \frac{1}{f_2}}\qquad\text{and, since } P = \frac{1}{f},\qquad \boxed{P = P_1 + P_2}$$

---
*Note on this lecture's transcript:* `gemini-3.5-flash` was in a 503 outage and then out of daily quota when this chapter was processed, so the audio was transcribed by `gemini-3.5-flash-lite` in overlapping five-minute windows, joined where the overlapping speech matches word for word. Lite's clock ran fast (by up to 2x) inside a window; each window was rescaled to its true length, so times quoted here are approximate (roughly ±30 s). Every gap of more than 30 s was re-transcribed on its own to confirm whether speech was missing. Equations are taken from the board frames, not from the transcript.
