# Earth's Magnetism Numericals, Null Point Problems, and the Atom as a Magnetic Dipole

**NCERT sections covered:** 5.4, 5.5

## Earth's magnetism: worked numericals (NCERT 5.4)

Using $B_H = B\cos\delta$ and $B_V=B\sin\delta$ ($\delta$ = angle of dip):
- Given $B_H$ and $\delta$: $B = B_H/\cos\delta$ (e.g. $B_H=0.35$ gauss, $\delta=22°$ $\Rightarrow B=0.35/0.92$).
- Given $B_H, B_V$: $\tan\delta = B_V/B_H$, then solve for $B$.
- **Full 3-D direction of $\vec B$:** first locate the *magnetic meridian* using the angle of **declination** (between geographic and magnetic meridian), then specify the angle within that vertical plane using the angle of **dip**.

## Null point problems (NCERT 5.4)

A null point is where a bar magnet's field exactly cancels Earth's horizontal field $B_H$. Its location depends on the magnet's orientation:
- **North pole toward geographic south:** null points lie on the magnet's **axial** line. $\left(\dfrac{\mu_0}{4\pi}\dfrac{2M}{d^3}=B_H\right)$
- **North pole toward geographic north:** null points lie on the **equatorial** line instead. $\left(\dfrac{\mu_0}{4\pi}\dfrac{M}{d^3}=B_H\right)$

Worked examples solve for the null-point distance (e.g. $14$ cm axial, $11.1$ cm equatorial in two separate problems), including a variant asking for the *new* null-point location after the magnet is turned $180°$ (which swaps axial $\leftrightarrow$ equatorial per the rule above).

## The atom as a magnetic dipole (NCERT 5.5)

Every atom behaves as a tiny magnet: an orbiting electron is a tiny current loop (**orbital** magnetic moment); electron spin contributes a **spin** magnetic moment too (about double the orbital contribution for the same angular momentum, per this lecture). **Direction:** curl the right hand's fingers in the direction of *conventional current* (opposite the electron's actual motion) — thumb gives the direction of $\vec M$, pointing from the loop's south to north face.

### Orbital magnetic moment derivation
Electron (charge $e$, angular speed $\omega$) in a circular orbit radius $r$: equivalent current $I=e/T=e\omega/2\pi$, loop area $A=\pi r^2$:
$$M = IA = \frac{e\omega}{2\pi}\cdot\pi r^2 = \frac{1}{2}e\omega r^2$$

### Connecting to Bohr's theory
Angular momentum is quantised: $mvr = \dfrac{nh}{2\pi}$. Using $v=r\omega$: $mr^2\omega = \dfrac{nh}{2\pi}$. Substituting:
$$M = \frac{neh}{4\pi m}$$
For $n=1$ (ground state), this defines the **Bohr magneton**:
$$\boxed{M = \frac{eh}{4\pi m} = \mu_B = 9.27\times10^{-24}~\text{A}\cdot\text{m}^2}$$

### Alternative form via angular momentum
Since $L = \vec r\times\vec p = mvr = mr^2\omega$, the same result rewrites as:
$$\boxed{M = \frac{e}{2m}L}, \qquad \vec M = -\frac{e}{2m}\vec L~\text{(electron's negative charge flips the direction)}$$
$e/2m$ is the **gyromagnetic ratio** — magnetic moment is directly proportional to angular momentum.


## Verify these spans
- [36:40–39:38] The transcript's real narration follows the Bohr-quantisation derivation closely and reaches M = (1/2)e * (nh/2*pi*m) as its very last segment, essentially arriving at the Bohr magneton result but never simplifying it to the named 'Bohr magneton' with its numerical value, and never mentioning the alternative angular-momentum form M=(e/2m)L or the gyromagnetic ratio at all. A board frame (floor_000116.jpg, t=2300s, within the transcript's own covered time range) shows both of these already written out: the boxed 'for n=1, M=eh/4*pi*m=mu_B=Bohr magneton' with its value 9.27e-24 A.m^2, and a separate derivation via L=r x p leading to M=(e/2m)L (vector form with a minus sign for the electron) plus a right-hand-rule statement for the direction of M. The Bohr-magneton-value and angular-momentum-form claims above are grounded from this frame rather than the transcript's own words.