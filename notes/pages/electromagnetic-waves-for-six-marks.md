# Electromagnetic Waves for Six Marks

*Chapter 8 · Electromagnetic Waves — 6 marks. Source: published page `762322ac-2430-4ee0-99aa-22a0cb8e6921`. Plain-text maths, not KaTeX. **Physics, Derived** has one Chapter 8 derivation (PD38, displacement current); the other four here appear nowhere else. This page also adds the theory, the spectrum table, the formula strip and the question tiers.*

> **Scope.** No scope cut. Five derivations only — the rest of the chapter is recall, and the spectrum table is the single most reliably asked thing in it.

## 01 · Theory

### 1 · Displacement current

**Definition to write:** displacement current is the current that exists in a region wherever the electric flux through that region is changing with time, given by `I_d = ε₀ (dΦ_E/dt)`. It is not a flow of charge, and it needs no conductor — it exists in vacuum.

Two situations the examiner asks you to separate:

- **Conduction current, no displacement current** — a steady current in a wire. The electric field in the wire is constant, so the flux does not change.
- **Displacement current, no conduction current** — the space between the plates of a capacitor while it charges or discharges. No charge crosses the gap, but the field between the plates is growing, so the flux is changing.

Its whole point is continuity: at every instant `I_d` between the plates equals `I_c` in the wire, so the total current is unbroken all the way round the circuit and Kirchhoff's junction rule survives. This is also why a galvanometer in series with a capacitor kicks momentarily while the capacitor charges on dc, and why current flows continuously when the source is ac.

### 2 · Characteristics of electromagnetic waves

- They are **transverse**: E and B are perpendicular to each other and both perpendicular to the direction of propagation, which lies along `E × B`.
- E and B are **in phase** — they reach their maxima and their zeros together — and their magnitudes are locked by `E₀/B₀ = c`.
- They need **no material medium** and travel through vacuum at `c = 3 × 10⁸ m s⁻¹`, the same speed for every wavelength.
- They are **electrically neutral**, so electric and magnetic fields do not deflect them.
- They show reflection, refraction, interference, diffraction and **polarisation** — the last one is the direct evidence that they are transverse.
- They carry **energy and momentum**, so they exert pressure on any surface that absorbs them.
- In a medium the speed falls to `v = 1/√(με) = c/n`; the frequency stays as the source set it, so the wavelength shortens.

*Sunlight warming your hand is the everyday evidence for energy; the photoelectric effect is the laboratory evidence. You do not feel the pressure because `p = U/c` and c is enormous.*

### 3 · The electromagnetic spectrum

| Band | Wavelength | Frequency | How it is produced | One use |
|---|---|---|---|---|
| γ-rays | < 10⁻¹⁰ m | > 3 × 10¹⁸ Hz | Radioactive decay of nuclei; nuclear reactions | Destroying cancer cells |
| X-rays | 10⁻¹⁰ – 10⁻⁸ m | 3 × 10¹⁶ – 3 × 10¹⁸ Hz | Fast electrons stopped by a heavy metal target such as tungsten | Detecting bone fractures |
| Ultraviolet | 10⁻⁸ – 4 × 10⁻⁷ m | 7.5 × 10¹⁴ – 3 × 10¹⁶ Hz | Very hot bodies; the Sun; mercury-vapour arcs and special lamps | Sterilising water in purifiers; LASIK eye surgery |
| Visible light | 4 × 10⁻⁷ – 7.5 × 10⁻⁷ m | 4 × 10¹⁴ – 7.5 × 10¹⁴ Hz | Electrons rearranging in atoms; incandescent bodies | Vision, photography |
| Infrared | 7.5 × 10⁻⁷ – 10⁻³ m | 3 × 10¹¹ – 4 × 10¹⁴ Hz | Vibration of hot bodies, atoms and molecules | Physiotherapy; TV remote controls |
| Microwaves | 10⁻³ – 10⁻¹ m | 3 × 10⁹ – 3 × 10¹¹ Hz | Klystrons, magnetrons and Gunn diodes | Radar for aircraft navigation; microwave ovens |
| Radio waves | > 10⁻¹ m | < 3 × 10⁹ Hz | Accelerated charges in aerials and oscillating LC circuits | Radio and television broadcasting |

*Order to be able to recite in both directions: γ, X, UV, visible, IR, microwave, radio — increasing wavelength, decreasing frequency. Visible light alone runs 400 nm (violet) to 750 nm (red).*

### 4 · How electromagnetic waves are produced

A charge at rest makes only a static electric field. A charge in uniform motion makes a steady magnetic field as well, but neither field changes, so nothing radiates. Only an **accelerated** charge radiates.

The mechanism to write out: an oscillating charge produces an oscillating electric field in the space around it; that changing electric field produces an oscillating magnetic field; that changing magnetic field produces a further oscillating electric field, and so on. Each field regenerates the other, so the disturbance carries itself outwards through empty space as an electromagnetic wave.

The frequency of the wave equals the frequency of oscillation of the charge. An LC circuit oscillating at `1/(2π√(LC))` is therefore a source of electromagnetic waves at that frequency, and the energy radiated comes out of the source.

*A charge moving in a circle is accelerating — its direction is changing — so it radiates too.*

### 5 · The atmosphere and the spectrum

- **Earth's warmth.** The Sun's visible and short-wave radiation reaches the ground and warms it. The ground re-radiates at longer infrared wavelengths, and greenhouse gases such as CO₂ and water vapour absorb and trap that infrared. Without an atmosphere there would be no such trapping, so the average surface temperature would be *lower* than it is now.
- **The ozone layer.** Ozone on top of the stratosphere absorbs the Sun's harmful ultraviolet before it reaches the surface. UV damages skin and eyes and causes skin cancer, so this thin layer is what makes life on land possible.
- **X-ray astronomy needs satellites.** The atmosphere absorbs X-rays completely, so an X-ray telescope on the ground would see nothing. Visible light and radio waves pass through, which is why optical and radio telescopes work from the ground.
- **Long-distance radio uses short-wave bands.** Short waves are reflected back to Earth by the ionosphere, so a signal can be bounced over the horizon to a distant receiver instead of escaping into space.
- **Radar uses microwaves.** Their short wavelength gives good directionality and resolution, and they pass through the atmosphere with little diffraction and little absorption.

## 02 · Derivations

### D1 · Displacement current — why Ampere's law was incomplete

> A parallel-plate capacitor of plate area A is being charged, so a time-varying current I(t) flows in the connecting wire. Draw a circular loop around the wire, and consider two *different* surfaces that share that same loop as their boundary.

1. Ampere's circuital law: ∮ B·dl = μ₀ I, where I is the current through any surface bounded by the loop
2. Surface A: a flat disc, pierced by the connecting wire
3. Current through surface A = I(t)
4. ∮ B·dl = μ₀ I(t) …(i)
5. Surface B: a pot-shaped surface with the same boundary loop, dipping between the capacitor plates and touching no wire
6. No charge crosses the gap between the plates, so the current through surface B = 0
7. ∮ B·dl = μ₀ × 0 = 0 …(ii)
8. The left-hand side of (i) and (ii) is the same integral over the same loop
9. (i) and (ii) contradict each other, so Ampere's law in this form is incomplete
10. Between the plates the field is E = σ/ε₀
11. Surface charge density σ = Q/A, Q being the charge on a plate
12. E = Q/(ε₀A)
13. Electric flux through surface B: Φ_E = E A
14. Φ_E = [Q/(ε₀A)] × A
15. Φ_E = Q/ε₀
16. Q = ε₀ Φ_E
17. Differentiate with respect to time: dQ/dt = ε₀ (dΦ_E/dt)
18. dQ/dt is the rate at which charge piles up on the plate, which equals the conduction current I_c in the wire
19. I_c = ε₀ (dΦ_E/dt)
20. So a quantity ε₀ (dΦ_E/dt) exists in the gap with exactly the value of the missing current
21. Maxwell named it the displacement current: I_d = ε₀ (dΦ_E/dt)

**Result:** I_d = ε₀ (dΦ_E/dt), and I_d = I_c at every instant

**Diagram:** capacitor plates with a wire entering from the left. Draw the flat disc surface A cutting the wire, and the pot-shaped surface B bulging round the left plate so its mouth is the same circular loop but its bottom lies in the gap. Mark I(t) on the wire and the electric field lines between the plates.

### D2 · The Ampere–Maxwell law

> Ampere's law repaired by adding the displacement current found in D1. Quote D1's boxed result first — this derivation is only four lines of algebra on top of it.

> **Shared setup:** D1 and D2 are one continuous argument, and CBSE often asks them as a single question. Learn them as one block: D1 finds the missing term, D2 puts it into the law.

1. From D1: surface A carries conduction current I_c and no changing flux
2. From D1: surface B carries no conduction current but a changing electric flux
3. For the law to give the same answer for both, the total current must be I = I_c + I_d
4. I_d = ε₀ (dΦ_E/dt)
5. I = I_c + ε₀ (dΦ_E/dt)
6. Put this total current into ∮ B·dl = μ₀ I
7. ∮ B·dl = μ₀ [I_c + ε₀ (dΦ_E/dt)]
8. ∮ B·dl = μ₀ I_c + μ₀ ε₀ (dΦ_E/dt)
9. Check on surface A: dΦ_E/dt = 0, so ∮ B·dl = μ₀ I_c
10. Check on surface B: I_c = 0, so ∮ B·dl = μ₀ ε₀ (dΦ_E/dt) = μ₀ I_c — *(using step 19 of D1)*
11. Both surfaces now give the same value of ∮ B·dl — the contradiction is gone

**Result:** ∮ B·dl = μ₀ [ I_c + ε₀ (dΦ_E/dt) ]

**What to say after the box:** this is one of Maxwell's four equations. The new term states that a changing electric field produces a magnetic field — the mirror image of Faraday's law, where a changing magnetic field produces an electric field. That symmetry is what makes a self-sustaining electromagnetic wave possible.

### D3 · Speed of electromagnetic waves, and E₀/B₀ = c

> Free space: no free charges and no conduction current, so `I_c = 0` everywhere. Only two of Maxwell's equations then matter, and they feed each other.

1. Faraday's law: ∮ E·dl = −(dΦ_B/dt) — a changing B makes an E
2. Ampere–Maxwell law from D2 with I_c = 0: ∮ B·dl = μ₀ ε₀ (dΦ_E/dt) — a changing E makes a B
3. Each field regenerates the other, so the disturbance propagates with no medium
4. Maxwell solved these two together for a plane wave and obtained a wave speed c = 1/√(μ₀ε₀)
5. μ₀ = 4π × 10⁻⁷ T m A⁻¹
6. ε₀ = 8.85 × 10⁻¹² C² N⁻¹ m⁻²
7. μ₀ ε₀ = (4 × 3.14 × 10⁻⁷)(8.85 × 10⁻¹²)
8. μ₀ ε₀ = 1.112 × 10⁻¹⁷
9. √(μ₀ ε₀) = 3.335 × 10⁻⁹
10. c = 1 / (3.335 × 10⁻⁹)
11. c = 3.00 × 10⁸ m s⁻¹
12. This equals the measured speed of light, which is how light was identified as an electromagnetic wave
13. For a plane wave along z: E = E₀ sin(kz − ωt) and B = B₀ sin(kz − ωt)
14. Both carry the same k and the same ω, so both travel at the same speed ω/k
15. ω/k = c
16. Maxwell's equations further require the amplitudes to satisfy E₀ = c B₀
17. E₀ / B₀ = c
18. In a medium of permeability μ and permittivity ε: v = 1/√(με)
19. v = 1/√(μ_r μ₀ ε_r ε₀) = c/√(μ_r ε_r) = c/n

**Result:** c = 1/√(μ₀ε₀) = 3 × 10⁸ m s⁻¹ · E₀/B₀ = c · v = c/√(μ_r ε_r)

*Step 4 is the one place a link is quoted rather than worked. That is deliberate: solving the coupled equations needs the wave equation, which is outside Class XII. What CBSE actually asks is "show that 1/√(μ₀ε₀) gives the velocity of an EM wave in free space" — that is steps 5 to 12, the numerical substitution, and you should write every one of them out.*

### D4 · Transverse nature, and the orientation of E, B and propagation

> A plane electromagnetic wave travelling along the z-axis in free space, written as `E_x = E₀ sin(kz − ωt)` and `B_y = B₀ sin(kz − ωt)`.

1. Gauss's law for electricity in free space: ∮ E·dA = q/ε₀ = 0 — *(no charge enclosed)*
2. Take a small box with two faces perpendicular to the propagation direction z
3. A component of E along z would send flux in through one face and out through the other, unequally as the wave passes
4. That would give a non-zero net flux, contradicting step 1
5. So E has no component along z
6. Gauss's law for magnetism: ∮ B·dA = 0 always — *(no magnetic monopoles)*
7. By the identical argument, B has no component along z
8. Both E and B lie entirely in the plane perpendicular to the propagation direction — the wave is transverse
9. Faraday's law links the B along y to an E that varies along z and points along x
10. The Ampere–Maxwell law links the E along x to a B that varies along z and points along y
11. So E is along x, B is along y, propagation is along z: E ⊥ B, and both ⊥ propagation
12. x̂ × ŷ = ẑ, so the direction of propagation is along E × B
13. E, B and the propagation vector form a right-handed set
14. Both fields carry the same phase (kz − ωt), so they reach their maxima and their zeros at the same instant — E and B are in phase

**Result:** E ⊥ B ⊥ propagation; propagation along E × B; phase difference between E and B is zero

**Diagram:** three axes with z pointing right. Draw the E sinusoid oscillating up and down in the x–z plane and the B sinusoid oscillating in and out in the y–z plane, both crossing zero at the same points along z. Label the propagation arrow along +z.

*Polarisation is the experimental proof of this: only a transverse wave can be polarised, and light can be.*

### D5 · Energy density and intensity

> The same plane wave, `E = E₀ sin(kz − ωt)` and `B = B₀ sin(kz − ωt)`, travelling through free space.

1. Energy density of an electric field: u_E = ½ ε₀ E²
2. Energy density of a magnetic field: u_B = B² / (2μ₀)
3. From D3: E = cB
4. Substitute in step 1: u_E = ½ ε₀ (cB)²
5. u_E = ½ ε₀ c² B²
6. From D3: c = 1/√(μ₀ε₀), so c² = 1/(μ₀ε₀)
7. u_E = ½ ε₀ B² × 1/(μ₀ ε₀)
8. u_E = B² / (2μ₀)
9. Comparing with step 2: u_E = u_B
10. Total energy density u = u_E + u_B = ½ ε₀ E² + B²/(2μ₀)
11. Since the two halves are equal: u = 2 × (½ ε₀ E²) = ε₀ E²
12. Average over one cycle: ⟨sin²(kz − ωt)⟩ = ½
13. ⟨u_E⟩ = ½ ε₀ E₀² × ½ = ¼ ε₀ E₀²
14. ⟨u_B⟩ = [B₀²/(2μ₀)] × ½ = B₀²/(4μ₀) = ¼ ε₀ E₀² — *(by step 8)*
15. ⟨u⟩ = ⟨u_E⟩ + ⟨u_B⟩ = ¼ ε₀ E₀² + ¼ ε₀ E₀²
16. ⟨u⟩ = ½ ε₀ E₀²
17. E_rms = E₀/√2, so E₀² = 2 E_rms²
18. ⟨u⟩ = ½ ε₀ (2 E_rms²) = ε₀ E_rms²
19. Intensity I = energy crossing unit area per unit time
20. In time t the wave sweeps a cylinder of cross-section A and length ct
21. Energy in that cylinder = ⟨u⟩ × (A c t)
22. I = energy / (A t) = ⟨u⟩ A c t / (A t)
23. I = ⟨u⟩ c
24. I = ½ ε₀ E₀² c

**Result:** u_E = u_B · ⟨u⟩ = ½ε₀E₀² = ε₀E_rms² · I = ½ε₀E₀²c

*Momentum follows: a wave delivering energy U to a fully absorbing surface delivers momentum `p = U/c`, so it presses on that surface. The pressure is tiny only because c is so large.*

## 03 · Formula strip

*● must be instant · ○ a few seconds is fine*

### ● Displacement current

`I_d = ε₀ (dΦ_E/dt)` — Φ_E = electric flux in V m (or N m² C⁻¹), ε₀ = 8.85 × 10⁻¹² C² N⁻¹ m⁻². I_d in ampere (A). Equal to the conduction current at every instant.

### ● Ampere–Maxwell law, the full corrected form

`∮ B·dl = μ₀ [ I_c + ε₀ (dΦ_E/dt) ]` — B in tesla (T), dl in metre (m), I_c = conduction current in ampere (A), μ₀ = 4π × 10⁻⁷ T m A⁻¹.

### ● Speed of electromagnetic waves in free space

`c = 1/√(μ₀ ε₀) = 3 × 10⁸ m s⁻¹` — same for every wavelength. This equality with the measured speed of light is what identified light as an EM wave.

### ● Ratio of the electric and magnetic field amplitudes

`E₀ / B₀ = c` — E₀ in V m⁻¹ (or N C⁻¹), B₀ in tesla (T). Also holds instant by instant: E = cB.

### ● Speed in a material medium

`v = 1/√(με) = c/√(μ_r ε_r) = c/n` — v in m s⁻¹; μ_r, ε_r and n are dimensionless. The frequency is unchanged, so the wavelength shortens by the factor n.

### ● Frequency, wavelength and speed

`c = ν λ` — ν in hertz (Hz), λ in metre (m). The workhorse of every spectrum numerical.

### ○ Wave number and angular frequency of a written wave

`E = E₀ sin(kz − ωt), k = 2π/λ, ω = 2πν, c = ω/k` — k in rad m⁻¹, ω in rad s⁻¹. Read λ and ν straight off the coefficients of z and t.

### ● Energy densities of the electric and magnetic parts

`u_E = ½ ε₀ E² · u_B = B²/(2μ₀)` — both in joule per cubic metre (J m⁻³). In an EM wave these two are equal at every point.

### ○ Average total energy density of an EM wave

`⟨u⟩ = ½ ε₀ E₀² = ε₀ E_rms²` — in J m⁻³. E₀ = amplitude, E_rms = E₀/√2, both in V m⁻¹.

### ○ Intensity of an electromagnetic wave

`I = ⟨u⟩ c = ½ ε₀ E₀² c` — in watt per square metre (W m⁻²). Energy crossing unit area per unit time.

### ○ Momentum delivered by a wave that is fully absorbed

`p = U / c` — U = energy absorbed in joule (J), p in kg m s⁻¹. Halve nothing — for a fully reflecting surface the momentum transferred is 2U/c.

### ○ Energy of one photon of the radiation

`E = hν = hc/λ` — h = 6.63 × 10⁻³⁴ J s. E in joule; divide by 1.6 × 10⁻¹⁹ to get electronvolt (eV).

### ● The two constants, with units

`μ₀ = 4π × 10⁻⁷ T m A⁻¹ · ε₀ = 8.85 × 10⁻¹² C² N⁻¹ m⁻²` — permeability and permittivity of free space. You will be asked to substitute these into c = 1/√(μ₀ε₀).

### ● Wavelength range of visible light, in nanometre

`400 nm (violet) to 750 nm (red)` — 1 nm = 10⁻⁹ m. Anything shorter than 400 nm is ultraviolet, anything longer than 750 nm is infrared.

## 04 · Questions to attempt

*Question numbers only, from Xam Idea Chapter 8 and the NCERT questions reprinted inside it. Section names are Xam Idea's own. At 6 marks this chapter will not carry a five-mark question, so the Tier 1 list is weighted towards the 3-mark slots.*

### Tier 1 — must do

*15 questions · the 3-mark slots and the spectrum recall*

| Question | Page | Why |
|---|---|---|
| Short Answer Q10 | p. 279 | Ampere generalised, full |
| Short Answer Q9 | p. 278 | Same argument, shorter |
| Short Answer Q3 | p. 276 | Conduction versus displacement |
| Short Answer Q4 | p. 276 | Current stays continuous |
| Short Answer Q5 | p. 277 | Diagram plus the c substitution |
| Short Answer Q1 | p. 275 | Spectrum table one |
| Short Answer Q2 | p. 275 | Spectrum table two |
| Short Answer Q6 | p. 277 | Identify plus production |
| Short Answer Q11 | p. 280 | Energy, momentum, density |
| Short Answer Q14 | p. 281 | Radar, atmosphere, pressure |
| Short Answer Q16 | p. 281 | Cancer, ozone, momentum |
| Short Answer Q17 | p. 282 | Four bands, ordered |
| Very Short Ans Q7 | p. 273 | The corrected law, stated |
| NCERT Q10 | p. 266 | Proves u_E equals u_B |
| Practice Q11 | p. 284 | Same proof, asked again |

### Tier 2 — if time

*extra pattern coverage, mostly 1 and 2 marks*

| Question | Page | Why |
|---|---|---|
| NCERT Q1, Q2 | p. 264–265 | Displacement current numericals |
| NCERT Q4, Q7, Q8 | p. 265–266 | E₀, B₀, ω, k drills |
| NCERT Q3, Q5, Q6 | p. 265 | c = νλ one-liners |
| MCQ 1, 2, 3 | p. 267 | Phase, free space, ratio |
| MCQ 23–27 | p. 270 | Density, uses, displacement |
| MCQ 4–22 | p. 268–269 | Rest of the set, fast |
| Assertion–Reason 1–10 | p. 270–271 | Whole set, ten minutes |
| Case Study (i)–(iv) | p. 272 | Order, transverse, wave number |
| Very Short Ans Q1–Q6 | p. 272–273 | Two-mark definitions |
| Very Short Ans Q8–Q14 | p. 274–275 | Spectrum recall, rapid fire |
| Short Answer Q7, Q8 | p. 277–278 | Ordering, dc versus ac |
| Short Answer Q12, Q13 | p. 280 | Oven, radar, sources |
| Practice Q1 (i)–(x), Q2 | p. 283 | One-markers plus assertion |
| Practice Q3, Q4, Q5, Q9 | p. 283 | Short numericals |

### Tier 3 — skip unless revising

*off the blueprint, or already done above*

**Belongs to a different chapter:** NCERT `Q9` (p. 266) builds a table of photon energies across the spectrum from E = hν. That is Dual Nature material, not this unit's six marks.

**Duplicates — do one of each pair, not both:** NCERT `Q10` ≡ Practice `Q10`. Short Answer `Q15` ≡ Short Answer `Q16`, same three-part shape. Practice `Q12` ≡ Short Answer `Q10`. Practice `Q14` ≡ Short Answer `Q15`. Practice `Q6, Q7, Q8, Q13` are all restatements of Very Short Answer and Short Answer questions already in Tiers 1 and 2.

**Read the answer, do not write it out:** at 6 marks the chapter cannot take more than about four questions on the paper. Once Tier 1 is done, the return on writing out any further recall answer is close to zero — spend the time on Chapter 7 instead.

### The five numerical types this chapter can ask

1. **Displacement current between the plates of a charging capacitor** — `I_d = ε₀ (dΦ_E/dt) = ε₀A (dE/dt)`, and I_d = I_c
2. **Move between frequency and wavelength anywhere on the spectrum** — `c = νλ`
3. **One field amplitude from the other** — `E₀/B₀ = c`
4. **Read λ, ν, ω and speed off a wave written as an equation** — `k = 2π/λ, ω = 2πν, c = ω/k`
5. **Energy density, intensity or momentum of a beam** — `⟨u⟩ = ½ε₀E₀², I = ⟨u⟩c, p = U/c`
