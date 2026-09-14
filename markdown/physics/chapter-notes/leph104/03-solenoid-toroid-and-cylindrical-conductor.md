# Magnetic Field Due to a Solenoid and a Toroid, and Inside/Outside a Current-Carrying Conductor

**NCERT sections covered:** 4.6, 4.7

## The solenoid (NCERT 4.7)

A long wire wound as a closely-packed helix. If closely wound (no gaps) and long, individual turns' fields add up along the axis to give a **uniform field inside**. Applying Ampere's circuital law with a rectangular Amperian loop (one side of length $l$ inside the solenoid parallel to the axis, the opposite side far outside where $B\approx0$, the two connecting sides perpendicular to $\vec B$ so $\vec B\cdot d\vec l=0$ there):
$$Bl = \mu_0(nl)I \quad\Rightarrow\quad \boxed{B = \mu_0 n I}$$
where $n$ = turns per unit length.

**Determining polarity from winding:** viewed end-on, current flowing **clockwise** at a face $\Rightarrow$ that face is a **south** pole (field lines converge/enter); **anticlockwise** $\Rightarrow$ **north** pole (field lines emerge) — consistent with field lines running south-to-north inside the solenoid.

## The toroid (application of Ampere's law, NCERT 4.6)

An **endless solenoid**: a solenoid bent into a closed ring. Current enters at one point on the cross-section and exits diametrically opposite, alternating dots/crosses around the ring; field lines inside the core form **concentric circles**.

**Three regions:**
1. **Empty space enclosed by the ring** (the "hole"): no current enclosed $\Rightarrow B=0$.
2. **Outside the toroid entirely:** $B=0$.
3. **Inside the toroid's wound core** — the only region with field:
$$B = \mu_0 n I, \qquad n = \frac{N}{2\pi R_\text{avg}}$$
(same form as a straight solenoid, using the average of the toroid's inner and outer radii for $R_\text{avg}$).

## Field inside/outside a long straight current-carrying conductor (Ampere's law application)

A cylindrical conductor of radius $a$ carries current $I$, uniformly distributed over its cross-section. Using a circular Amperian loop of radius $r$:

- **Outside** ($r>a$): full current $I$ enclosed: $B(2\pi r)=\mu_0 I \Rightarrow \boxed{B=\dfrac{\mu_0 I}{2\pi r}}$ — same as a thin wire, $\propto 1/r$.
- **Inside** ($r<a$): only the enclosed fraction of current counts (uniform current density): $I_\text{enc} = I\dfrac{r^2}{a^2}$, giving $B(2\pi r) = \mu_0 I\dfrac{r^2}{a^2} \Rightarrow \boxed{B = \dfrac{\mu_0 I r}{2\pi a^2}}$ — $\propto r$.
- **At the surface** ($r=a$): both expressions agree, $B=\dfrac{\mu_0 I}{2\pi a}$, the **maximum** value.

$B$-vs-$r$ graph: a straight line rising from the centre to the surface, then a $1/r$ curve falling off outside.
