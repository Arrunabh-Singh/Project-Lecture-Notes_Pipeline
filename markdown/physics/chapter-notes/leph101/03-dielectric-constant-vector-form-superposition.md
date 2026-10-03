# Dielectric Constant, Coulomb's Law in Vector Form, and the Superposition Principle

**NCERT sections covered:** 1.5, 1.6

## Dielectric constant

### Force in a medium other than vacuum
$$F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r^2}\quad\text{(vacuum)} \qquad F = \frac{1}{4\pi\varepsilon}\frac{Q_1Q_2}{r^2}\quad\text{(medium, absolute permittivity }\varepsilon\text{)}$$

**Relative permittivity** $\varepsilon_r = \varepsilon/\varepsilon_0$ is preferred to quoting $\varepsilon$ directly, for the same reason density is usually quoted relative to water (density of water $=1$ g/cm$^3$, mercury $=13.6$, kerosene $=0.8$): a dimensionless ratio against a fixed, universal reference is more useful than an absolute value with units.

**Dielectric constant** $K$ is just another name for relative permittivity — there is no physical difference between the two terms:
$$\boxed{F = \frac{1}{4\pi\varepsilon_0 K}\frac{Q_1Q_2}{r^2}}, \qquad K=\varepsilon_r=\varepsilon/\varepsilon_0$$

*(Aside: in the CGS system, the Coulomb's-law constant is taken as exactly $1$, and charge is measured in electrostatic units/statcoulombs, with $1$ C $=3\times10^9$ esu. Mentioned for context; SI is used throughout this course.)*

### Partly-dielectric, partly-vacuum gap
For two charges separated by distance $r$, with a dielectric slab of thickness $t$ (constant $K$) occupying part of the gap and the rest ($r-t$) vacuum: replace the dielectric segment with an **equivalent vacuum distance** $r_0=\sqrt{K}\,t$ (found by equating the force through the real dielectric thickness to the force through an unknown vacuum thickness), then treat the whole path as vacuum with total effective separation $(r-t)+\sqrt{K}t$:
$$F = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{\left[(r-t)+\sqrt{K}\,t\right]^2}$$

## Coulomb's law in vector form (NCERT 1.5)

For charges $Q_1$ at $\vec r_1$ and $Q_2$ at $\vec r_2$, the force on $Q_2$ due to $Q_1$:
$$\vec F_{21} = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2(\vec r_2-\vec r_1)}{|\vec r_2-\vec r_1|^3} = \frac{1}{4\pi\varepsilon_0}\frac{Q_1Q_2}{r_{12}^2}\hat r_{12}$$
By Newton's third law, $\vec F_{12}=-\vec F_{21}$.

## Principle of superposition (NCERT 1.6)

The net force on any one charge due to several others is the **vector sum** of the individual pairwise Coulomb forces, each computed independently as though only that one pair of charges existed, then combined via the triangle/parallelogram law of vector addition. For charges $Q_1,\dots,Q_5$, the force on $Q_4$:
$$\vec F_4 = \vec F_{41}+\vec F_{42}+\vec F_{43}+\vec F_{45}$$
