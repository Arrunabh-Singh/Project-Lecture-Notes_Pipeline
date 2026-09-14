# Capacitance of a Parallel Plate Capacitor: No Dielectric, Fully Filled, Partially Filled

**NCERT sections covered:** 2.12, 2.13

## Capacitance of a parallel plate capacitor (NCERT 2.12, 2.13)

### Without dielectric (medium = air/vacuum)
Plates of area $A$, separation $D$. Field between the plates: $E = \dfrac{\sigma}{\varepsilon_0} = \dfrac{Q}{A\varepsilon_0}$. Since $Q=CV$ and (for a uniform field) $V = ED$:
$$V = \frac{QD}{A\varepsilon_0} \quad\Rightarrow\quad \boxed{C = \frac{A\varepsilon_0}{D}}$$

### With dielectric completely filling the gap (dielectric constant $K$)
Inside the dielectric the field is reduced by a factor of $K$: $E = \dfrac{\sigma}{K\varepsilon_0} = \dfrac{Q}{AK\varepsilon_0}$. The same route as above gives:
$$\boxed{C = \frac{KA\varepsilon_0}{D}}$$
Capacitance increases by a factor of $K$ compared to the no-dielectric case. (Real capacitors are commonly built this way -- e.g. paper capacitors, electrolytic capacitors -- using a dielectric layer between the plates.)

### With a dielectric slab partially filling the gap
Slab of thickness $t < D$ and dielectric constant $K$ inserted between the plates (remaining $D-t$ is air). The field is $\sigma/\varepsilon_0$ across the air gap and $\sigma/(K\varepsilon_0)$ across the slab; adding the two potential-drop contributions:
$$V = \frac{Q}{A\varepsilon_0}\left[(D-t) + \frac{t}{K}\right] \quad\Rightarrow\quad \boxed{C = \frac{A\varepsilon_0}{D-t+\dfrac{t}{K}}}$$

**General shortcut** for any number of stacked layers (dielectric slabs and/or air gaps) between the plates:
$$C = \frac{A\varepsilon_0}{\dfrac{t_1}{K_1}+\dfrac{t_2}{K_2}+\cdots}$$
where each $t_i$ is a layer's thickness and $K_i$ its dielectric constant (air is just a layer with $K=1$). The single-slab case above is the special case $t_1=t,\,K_1=K$ and $t_2=D-t,\,K_2=1$.

### Consistency checks
- Setting $t=D$ (slab fills the entire gap) in the partially-filled formula reduces it to $C = KA\varepsilon_0/D$ -- matching the fully-filled result, as it must.
- If the inserted slab is a **metal** rather than a dielectric, that's the limit $K\to\infty$: $C \to \infty$.

---
*Note on this lecture's transcript:* the two consistency-check results above are grounded from a board frame near the true end of the audio; the transcript itself doesn't reach them. See the flagged span below.


## Verify these spans
- [11:00–13:22] Board frame floor_000034.jpg (t=660s, comfortably within the true 802.67s duration) shows two consistency checks worked out after the main partially-filled-dielectric formula: substituting t=D to recover the fully-filled result, and the K->infinity (metal slab) limit giving C->infinity. Neither appears anywhere in the transcript's 37 segments, which end (at a coherent, naturally-concluding sentence) on the T1/K1+T2/K2 shortcut applied to this lecture's specific numbers. This is a much smaller gap than the severe substitution found in the previous lecture (14 ch2 capacitors) -- most likely a short board-only aside that went untranscribed near the true end of the audio, rather than sustained content substitution. The metal-slab/K-to-infinity claim above is grounded from the board frame only.