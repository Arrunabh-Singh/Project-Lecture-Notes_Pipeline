# The Cyclotron

**NCERT sections covered:** 4.3

## The cyclotron (NCERT 4.3)

A device (developed by Lawrence) that accelerates **positively charged particles** (proton, deuteron, alpha particle) to high energies using repeated passes through a comparatively small oscillating electric field, combined with a strong magnetic field.

### Construction
Two hollow, evacuated D-shaped metal chambers ("Dees", $D_1,D_2$) separated by a small gap, connected to a high-frequency oscillator (providing the oscillating field across the gap), placed in a strong magnetic field perpendicular to the Dees' plane.

### Working
A positive charge injected near the centre accelerates across the gap into one Dee, traces a **semicircular path** inside it (magnetic force only — no field inside a hollow conducting Dee), returns to the gap just as the oscillator's polarity reverses, gets accelerated again, and traces a **larger** semicircle in the next Dee (higher speed now). This repeats — spiralling outward — until the particle exits through a window with high velocity and strikes a target.

### Mathematics
Inside a Dee, the magnetic force supplies centripetal force:
$$Bqv = \frac{mv^2}{r} \;\Rightarrow\; r = \frac{mv}{Bq}$$
Using $v=r\omega$:
$$\boxed{\omega = \frac{Bq}{m}}, \qquad T = \frac{2\pi m}{Bq}$$
$\omega$ (and $T$) are **independent of radius** $r$ — as the radius grows with each pass, speed grows proportionally, keeping each semicircle's transit time constant. This is exactly why the oscillator, tuned to this fixed period, stays synchronized with the particle across every pass.

### Why not electrons?
An electron's tiny rest mass means it reaches relativistic speeds almost immediately, so its **relativistic mass** $m=m_0/\sqrt{1-v^2/c^2}$ grows with speed rather than staying constant. Since $T=2\pi m/(Bq)$ depends on mass, a growing mass breaks the match with the fixed-frequency oscillator — the electron drifts **out of phase** and stops being properly accelerated. Heavier particles (protons, deuterons, alpha particles) are far less affected by this at cyclotron energies, so cyclotrons work well for them but not for electrons.
