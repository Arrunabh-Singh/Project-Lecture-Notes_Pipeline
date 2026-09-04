# Magnetizing Intensity, Intensity of Magnetization, Permeability, and Susceptibility

**NCERT sections covered:** 5.4

## Magnetizing intensity, intensity of magnetization, and permeability (NCERT 5.4)

**Magnetizing intensity $H$:** from the solenoid result $B_0=\mu_0 nI$, the quantity $nI$ (turns/length $\times$ current), independent of any material, is called $H$. So $B_0=\mu_0 H$ for an air/vacuum core, or generally $B=\mu H$ with a material core. SI unit: A/m.

**Intensity of magnetization $I$ (or $M$):** a vector, defined as magnetic moment per unit volume of a material placed in the magnetizing field — the material's atomic dipoles align with the field:
$$I = \frac{m}{V}$$
Same SI unit as $H$ (A/m), despite representing a different physical quantity (external coil/current setup vs. the material's own response).

**Magnetic permeability $\mu$:** quantifies how readily a magnetic field can penetrate a material (e.g. an iron bar between magnet poles draws field lines through it far more than air would). $\mu = B/H$. SI units: T$\cdot$m$\cdot$A$^{-1}$ (equivalently Wb$\cdot$m$^{-1}\cdot$A$^{-1}$).

### Relation between permeability and susceptibility
Total field $B = B_0+B_m = \mu_0 H + \mu_0 I$ (the material's own contribution $B_m=\mu_0 I$ adds to the bare $\mu_0 H$). **Magnetic susceptibility** $\chi_m = I/H$, so $I=\chi_m H$:
$$B = \mu_0 H(1+\chi_m)$$
Comparing with $B=\mu H$:
$$\boxed{\mu = \mu_0(1+\chi_m)}, \qquad \mu_r = \frac{\mu}{\mu_0} = 1+\chi_m$$

### Worked numericals
- **Rowland ring:** mean radius $15$ cm, $3500$ turns on a ferromagnetic core ($\mu_r=800$), current $1.2$ A. $n=N/2\pi r$, $B=\mu_0\mu_r nI = 4.48$ T.
- **Steel magnet:** $M=2.5$ A$\cdot$m$^2$, mass $6.6$ g, density $7.9\times10^3$ kg/m$^3$. Find $I$: get volume from mass/density, then $I=M/V$.
- **Iron rod:** cross-section $0.2$ cm$^2$, $H=1200$ A/m, $\chi_m=599$. Find $\mu$ and flux $\phi$: $\mu_r=1+\chi_m=600$, $\mu=\mu_0(1+\chi_m)=7.536\times10^{-4}$ T$\cdot$m$\cdot$A$^{-1}$; then $\phi=BA$ with $B=\mu H$.

---
*Note on this lecture's transcript:* the susceptibility relation and all three worked numericals above are grounded entirely from board frames -- the transcript itself never mentions susceptibility at all, instead getting stuck repeating the permeability and magnetization definitions several times over. See the flagged span below.


## Verify these spans
- [07:32–23:52] This is one of the most severely corrupted transcripts found in this project: after cleanly covering magnetizing intensity H and intensity of magnetization I, the transcript's narration of 'magnetic permeability' repeats itself at least four to five times over (near-identical short phrases like 'to which magnetic field can penetrate a material' and 'mu is equal to B upon H' recur at t=452s, 623s, 814s, 997s, and 1129s), then the 'intensity of magnetization' definition is re-transcribed a second time (t=1160-1420s) nearly verbatim from its first pass (t=194-445s) -- all classic delayed-repetition artifacts. Crucially, the transcript NEVER once mentions magnetic susceptibility, despite board frames showing it is thoroughly covered: floor_000047.jpg (t=920s) shows the full permeability-susceptibility relation derivation (chi_m=I/H, mu=mu0(1+chi_m)); floor_000050.jpg through floor_000060.jpg (t=980-1180s) show a complete Rowland-ring numerical; and floor_000060.jpg through floor_000069.jpg (t=1180-1360s) show a magnet intensity-of-magnetization numerical and an iron-rod susceptibility numerical, both fully worked. Roughly the back half of this lecture (everything from the susceptibility relation onward) is grounded entirely from these frames.