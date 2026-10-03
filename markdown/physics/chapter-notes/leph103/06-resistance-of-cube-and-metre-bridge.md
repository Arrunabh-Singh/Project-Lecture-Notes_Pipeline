# Resistance of a Cube Network, and the Metre Bridge

**NCERT sections covered:** 3.13

## Resistance of a cube network (worked numerical)

A cube with an identical resistor $R$ on each of its 12 edges — find the effective resistance between two opposite corners along a **body diagonal** ($X$ and $Y$).

**Symmetry argument:** current $I$ entering at $X$ splits equally into three paths of $I/3$ (three edges meet at $X$). At each of the next three vertices, $I/3$ splits further into $I/6+I/6$ (two edges lead onward toward $Y$'s neighbourhood). The six $I/6$ branches recombine in pairs back into three $I/3$ branches, converging at $Y$.

**Applying Kirchhoff's loop rule** along one $X\to Y$ path (edges carrying $I/3$, then $I/6$, then $I/3$, each of resistance $R$), back through the battery (EMF $\mathcal E$):
$$\mathcal E = IR\left(\frac13+\frac16+\frac13\right) = IR\cdot\frac{2+1+2}{6} = \frac56 IR$$
Using $I=\mathcal E/R_\text{eff}$:
$$\boxed{R_\text{eff} = \frac{5}{6}R}$$
— the classic result for a cube's body-diagonal resistance when every edge carries the same $R$.

## The metre bridge (NCERT 3.13, application of the Wheatstone bridge)

A practical device based on the Wheatstone bridge, used to find an **unknown resistance** $X$.

**Method:** take a known resistance $R$ from a resistance box; connect $R$ and $X$ as the two "gap" resistors of the bridge. The other two bridge arms are formed by a $100$ cm resistance wire $AB$ (typically nichrome) stretched over a metre scale. Tap a jockey along the wire until the galvanometer shows **zero deflection** (the null/balance point) at position $C$, splitting the wire into length $l$ (from $A$) and $100-l$ (from $C$ to $B$).

**Balance condition:** the two wire segments act as resistances $R'=\rho l/A$ and $R''=\rho(100-l)/A$ ($\rho$ = wire resistivity, $A$ = cross-sectional area), forming a bridge with $R$ and $X$. The resistivity/area factors cancel in the balance ratio, giving:
$$\boxed{X = \frac{R(100-l)}{l}}$$

**Practical note:** for the best accuracy, the null point $l$ should fall near the **centre** of the wire (around $50$ cm).

---
*Note on this lecture's transcript:* the entire metre bridge section above is grounded from board frames -- the transcript's own 20 segments describe only the cube-resistance problem, with no mention of the metre bridge anywhere. See the flagged span below.


## Verify these spans
- [00:00–17:42] This is an unusually total content-omission failure: the transcript's 20 segments, spanning essentially the entire lecture from t=0 to its stated end, describe ONLY the resistance-of-a-cube numerical -- the metre bridge, the lecture's own second named topic, is never mentioned even once in the transcript. Board frames tell a completely different story: floor_000041.jpg (t=800s) already shows the full metre-bridge setup (heading, method description, and circuit diagram) essentially complete, and floor_000052.jpg (t=1020s, near the true end) shows the full derivation through to the boxed final formula X=R(100-l)/l, plus a practical note about keeping the null point near the wire's centre for accuracy. Since the transcript's own timestamps leave no visible gap for this material (it reads as one continuous narration of the cube problem throughout), this looks like the ASR silently failing to transcribe an entire audio segment covering a real second topic, rather than a duration-truncation or delayed-repetition case seen elsewhere in this project. All metre-bridge claims above are grounded entirely from the two board frames.