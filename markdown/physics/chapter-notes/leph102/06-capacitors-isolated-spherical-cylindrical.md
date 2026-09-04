# Capacitors and Capacitance: Basics, Isolated Sphere, Spherical Capacitor, Cylindrical Capacitor

**NCERT sections covered:** 2.11

## Capacitors and capacitance (NCERT 2.11)

### Capacitance of a conductor
As charge $Q$ on a conductor increases, its potential $V$ rises proportionally: $Q \propto V$, so
$$Q = CV$$
where $C$, the **capacitance**, is a constant depending only on the conductor's geometry (independent of $Q$ and $V$ themselves). On a $Q$–$V$ graph this is a straight line through the origin; its slope gives $C$.

**Unit:** $1~\text{farad} = 1~\text{coulomb/volt}$ (named for Faraday). **Worked example:** $Q = 10~\mu\text{C}$ raising the potential by $2.5$ V gives $C = Q/V = 4\times10^{-6}$ F.

### Why two plates, not one
A single charged plate's potential rises so much (for a modest amount of charge) that the surrounding air can ionise and charge starts leaking away. Bringing a second, **grounded** plate close by induces opposite charge on it, which sharply lowers the first plate's potential for the *same* stored charge — allowing far more charge to be stored before breakdown. A **capacitor** is this pair of two neighbouring conductors carrying equal and opposite charge. Common shapes: parallel-plate, spherical, and cylindrical (coaxial) capacitors.

### What capacitance depends on
$C$ does **not** depend on $Q$ or $V$ individually (only their ratio) — it depends purely on **geometry**: plate area (directly proportional), separation $d$ (inversely proportional), and the medium between the plates (increases with dielectric constant $K$). For a parallel plate capacitor, $C = K\varepsilon_0 A/d$ (stated here; derived from first principles in a later lecture).

### Capacitance of an isolated spherical conductor
A single charged sphere (charge $Q$, radius $R$), with the "other plate" taken at infinity:
$$V = V_A - V_B = \frac{Q}{4\pi\varepsilon_0 R} - 0 \quad\Rightarrow\quad C = \frac{Q}{V} = 4\pi\varepsilon_0 R \;\;(\text{or } 4\pi\varepsilon_0 KR \text{ with a dielectric of constant } K)$$
So $C \propto R$. **Worked example:** modelling Earth as a spherical conductor of radius $6400$ km gives $C_\text{Earth} \approx 711~\mu\text{F}$.

### Capacitance of a spherical capacitor
Two concentric spherical conductors: inner sphere charge $+Q$ at radius $r_1$, outer shell $-Q$ (grounded) at radius $r_2$. Using a Gaussian surface at radius $r$ between them ($E = \frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}$ in that region only):
$$V = -\int_{r_1}^{r_2}\vec E\cdot d\vec r = \frac{Q}{4\pi\varepsilon_0}\left(\frac{1}{r_1}-\frac{1}{r_2}\right) = \frac{Q}{4\pi\varepsilon_0}\frac{r_2-r_1}{r_1 r_2}$$
$$\boxed{C = \frac{Q}{V} = \frac{4\pi\varepsilon_0\, r_1 r_2}{r_2-r_1}}$$

### Capacitance of a cylindrical capacitor
Two coaxial cylinders of length $L$: inner radius $a$ carrying linear charge density $+\lambda$, outer radius $b$ carrying $-\lambda$ (grounded). Between them, Gauss's law gives $E = \dfrac{\lambda}{2\pi\varepsilon_0 r}$:
$$V = -\int_b^a \vec E\cdot d\vec r = \frac{\lambda}{2\pi\varepsilon_0}\ln\!\left(\frac{b}{a}\right)$$
With $\lambda = Q/L$:
$$\boxed{C = \frac{Q}{V} = \frac{2\pi\varepsilon_0 L}{\ln(b/a)}}$$

---
*Note on this lecture's transcript:* the two derivations above (spherical capacitor, cylindrical capacitor) are grounded entirely in board frames -- the transcript itself does not contain them at all; see the flagged span below for what happened instead. Also note: NCERT's core text (Section 2.11) covers capacitance of a single (isolated) conductor and states the general definition, but does not itself carry closed-form spherical/cylindrical capacitor derivations -- these two results are standard board/exam extensions beyond the strict textbook section, not verified against an NCERT-stated formula, though they follow directly from the same first principles ($V=-\int\vec E\cdot d\vec l$, Gauss's law) taught earlier in the chapter.


## Verify these spans
- [17:40–32:06] This is the most severe transcript failure found in this chapter so far. Board frames show the isolated-sphere derivation is essentially complete by t=1060s (floor_000054); by t=1220s (floor_000062) the board has already moved on to a NEW page titled 'capacitance of a spherical capacitor' with a two-conductor Gaussian-surface diagram; by t=1440s (floor_000073) that derivation is fully worked out to a boxed capacitance formula; by t=1700s (floor_000086) a further new page 'capacitance of a cylindrical capacitor' has begun; and by t=1900s (floor_000096, just 26s before the lecture's true end) that derivation too is complete with a boxed final formula -- exactly the two topics ('spherical, cylindrical') named in this lecture's own filename. The ASR transcript, however, does not follow any of this: from roughly t=1092s to t=1866s it transcribes the SAME 'isolated spherical conductor' derivation (including the identical Earth/711-microfarad example, down to near-identical sentence wording) TWICE in a row, then cuts off mid-sentence at t=1925s ('And say this is the second sphere, okay, surrounding it') just as it appears to begin the topic the board had already finished twenty minutes of board-time earlier. Automated coverage checks did not flag this: the repeated block is not adjacent-duplicate text (a few short transitional segments separate the two copies) so the repetition-loop detector missed it, and the final timestamp lands within the true duration so the duration-fabrication check also passed. The two capacitor-formula claims above (spherical and cylindrical) are grounded entirely from board frames, with no transcript corroboration at all.