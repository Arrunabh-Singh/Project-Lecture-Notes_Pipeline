# Joule's Law, Electric Power, Bulb Ratings, kWh, and Temperature Coefficient of Resistance

**NCERT sections covered:** 3.8, 3.9

## Joule's law of heating (NCERT 3.9)

Current through a resistor converts electrical energy into heat. For charge $dQ$ moved across potential difference $V$ in time $dt$: $dW = V\,dQ = VI\,dt$. Total work (constant $V,I$) over time $t$:
$$W = \int VI\,dt = VIt$$
Using $V=IR$, this heat can also be written:
$$W = I^2Rt = \frac{V^2}{R}t$$

## Electric power (NCERT 3.9)

$$P = \frac{W}{t} = VI = I^2R = \frac{V^2}{R}$$
SI unit: **watt** (W) $=$ J/s.

### Bulb rating numerical
A bulb rated $220$ V, (worked example: $20$ W) consumes that many joules per second at $220$ V.
- **Max permissible current:** $I = P/V$ (e.g. $20/220 = 1/11$ A)
- **Filament resistance:** from $P=V^2/R$, $R = V^2/P$ (e.g. $220\times220/20\ \Omega$)

### Kilowatt-hour
Electricity bills measure energy in **kilowatt-hours (kWh)**, not joules: energy $=$ power (kW) $\times$ time (h). $1$ kWh is the energy an appliance rated $1$ kW consumes running for $1$ hour:
$$1~\text{kWh} = 1000~\text{W}\times3600~\text{s} = 3.6\times10^6~\text{J}$$

## Temperature coefficient of resistance (NCERT 3.8)

$$\Delta R \propto R\,\Delta T \;\Rightarrow\; \alpha = \frac{\Delta R}{R\,\Delta T} = \frac{R_t-R_0}{R_0\,\Delta T} \;\Rightarrow\; \boxed{R_t = R_0(1+\alpha\,\Delta T)}$$
The same relation holds for resistivity $\rho$: $\rho_t=\rho_0(1+\alpha\,\Delta T)$. (This mirrors the general pattern for thermal expansion coefficients: $\alpha=\Delta L/L_0\Delta T$, $\beta=\Delta A/A_0\Delta T$, $\gamma=\Delta V/V_0\Delta T$, with $\alpha:\beta:\gamma=1:2:3$.)

### By material class
- **Metals:** $\alpha$ positive, comparatively large — resistivity **rises** with temperature.
- **Semiconductors:** $\alpha$ **negative** — resistivity **falls** as temperature rises (more charge carriers become available at higher $T$).
- **Alloys** (manganin, constantan, nichrome): $\alpha$ very small — resistance is nearly temperature-independent, which is exactly why these are the materials chosen for precision resistors and heating elements.

---
*Note on this lecture's transcript:* the entire temperature-coefficient section above is grounded from board frames -- the transcript itself never reaches it in words, instead getting sidetracked into a kWh digression and stopping there. See the flagged span below. "Carbon resistor" (also named in this lecture's filename) was not found in either the transcript or the sampled frames and is not covered in this note.


## Verify these spans
- [27:44–35:29] The transcript's real narration (43 segments, no detected repetition) runs through a coherent introduction to 'different types of resistors' (t=1530-1664s: 'standard coil resistors...') before pivoting to a kilowatt-hour digression ('before understanding [resistor types], I just missed out one more thing...') that then runs to the transcript's last segment, ending mid-explanation of the kWh-to-joules conversion. The transcript never returns to resistor types, and never mentions temperature coefficient of resistance in words at all. Board frames tell a fuller story: floor_000071.jpg through floor_000095.jpg (spanning roughly t=1400-1880s, overlapping and extending past the transcript's own covered range) show a complete, thorough 'temperature coefficient of resistance' derivation plus a three-way comparison of metals, semiconductors, and alloys -- none of it narrated in the available transcript. All temperature-coefficient claims above are grounded entirely from these frames. Separately, 'carbon resistor' -- named in this lecture's own filename alongside temperature coefficient -- was NOT found in either the transcript or any of the 32 sampled board frames; rather than guess at its content, it is omitted from this note entirely.