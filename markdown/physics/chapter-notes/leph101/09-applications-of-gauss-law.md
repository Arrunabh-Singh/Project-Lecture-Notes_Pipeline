# Applications of Gauss's Law: Cube Flux Numericals, Infinite Wire, Infinite Sheet, Charged Spherical Shell

**NCERT sections covered:** 1.13, 1.14

## Gauss's law: flux numericals with a cube

**Charge near one face:** a point charge $10$ cm from the centre of one face of a cube — flux through the whole (closed) cube is $q/\varepsilon_0$; since a cube has 6 identical faces, flux through just that one face is $\dfrac{1}{6}\dfrac{q}{\varepsilon_0}$.

**Charge at special points of a cube:**
- **Body centre:** charge fully enclosed by one cube $\Rightarrow$ flux $=q/\varepsilon_0$.
- **Face centre:** charge sits on the boundary shared with one neighbouring cube $\Rightarrow$ effective enclosed charge $q/2$, flux $=\dfrac{q}{2\varepsilon_0}$.
- **Edge centre:** charge shared among the $8$ cubes meeting at that edge $\Rightarrow$ effective enclosed charge $q/8$, flux $=\dfrac{q}{8\varepsilon_0}$.

## Applications of Gauss's law (NCERT 1.14)

Gauss's law gives a shortcut to find $E$ for highly symmetric continuous charge distributions: choose a Gaussian surface matching the symmetry, so $E$ can be pulled outside the flux integral.

### Field due to an infinitely long charged wire (1.14.1)
Linear charge density $\lambda$, field point at perpendicular distance $r$. Gaussian surface: a coaxial cylinder of radius $r$, length $L$. By symmetry $E$ is radial and constant on the curved surface (parallel to its area vector, $\theta=0$), and perpendicular to the two flat end-caps ($\theta=90°$, zero contribution):
$$E(2\pi rL) = \frac{\lambda L}{\varepsilon_0} \;\Rightarrow\; \boxed{E = \frac{\lambda}{2\pi\varepsilon_0 r}}$$
($L$ cancels.) Inversely proportional to $r$ — same rectangular-hyperbola-shaped $E$-vs-$r$ graph family as the point charge and the dipole.

### Field due to an infinite plane sheet (1.14.2)
Surface charge density $\sigma$; field is perpendicular to the sheet, equal magnitude both sides. Gaussian surface: a thin "pillbox" cylinder straddling the sheet, flat circular end-caps of area $A$ parallel to the sheet. $E$ parallel to both end-caps ($\theta=0$, contributing $EA$ each) and perpendicular to the curved side (zero):
$$2EA = \frac{\sigma A}{\varepsilon_0} \;\Rightarrow\; \boxed{E = \frac{\sigma}{2\varepsilon_0}}$$
($A$ cancels.) **Independent of distance** from the sheet — a flat horizontal line on an $E$-vs-$r$ graph.

### Field due to a uniformly charged thin spherical shell (1.14.3)
Total charge $q$, radius $R$.
- **Outside / on the surface** ($r\geq R$, Gaussian sphere concentric with the shell): the whole charge behaves as if concentrated at the centre, exactly like a point charge:
$$E = \frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\ (r>R), \qquad E = \frac{1}{4\pi\varepsilon_0}\frac{q}{R^2}\ (r=R)$$
- **Inside** ($r<R$): a Gaussian sphere strictly inside the shell encloses **zero** charge (all the shell's charge sits on its outer surface). Since the flux integral's surface-area factor $4\pi r^2$ is never zero for $r>0$, this forces:
$$\boxed{E = 0 \text{ everywhere strictly inside a uniformly charged shell}}$$

---
*Note on this lecture's transcript:* both the outside/surface and inside results for the charged spherical shell above are grounded entirely from board frames near the true end of this (very long, 48-minute) lecture -- the transcript itself stops right at the sentence introducing this final application, with no further segments. See the flagged span below.


## Verify these spans
- [46:20–47:38] This is a straightforward truncation rather than a repetition/substitution artifact: the transcript's own last segment is the single sentence 'So, what we do is we consider a thin spherical shell, let us suppose we consider this as a thin spherical shell,' right at the very start of the third application (field due to a charged spherical shell), and no further segments follow even though this was clearly meant to be a full derivation (matching this very long, 48-minute lecture's own title, 'application of gauss th'). Board frames fill the gap completely: floor_000134.jpg and floor_000138.jpg (both well within the true 2858s duration, after the transcript's own cutoff) show the full three-case derivation -- outside/on the surface (Gauss's law with a Gaussian sphere of radius r>=R, giving the point-charge-like result), and inside (Gaussian sphere r<R encloses zero charge, forcing E=0) -- reaching clean, boxed final results in each case. Both spherical-shell claims above are grounded entirely from these two board frames.