# Torque on a Current-Carrying Loop in a Uniform Magnetic Field

**NCERT sections covered:** 4.9

## Torque on a current-carrying loop (NCERT 4.9)

### Special case: B in the plane of the loop (normal $\perp B$)
Rectangular loop (sides $PQ=RS=l$, $QR=SP=b$, current $I$), $\vec B$ lying in the loop's plane. Forces on the two sides parallel to $B$ (SR, QP) are zero ($I\vec L\times\vec B=0$ there). Forces on the two sides perpendicular to $B$ (PS, RQ) are each $ILB$, equal and opposite but acting along **different** lines — a couple.

$$\tau = (\text{force})\times(\text{perpendicular distance between lines of action}) = (ILB)(b) = I(lb)B = \boxed{IAB}$$
where $A=lb$ is the loop's area. Direction: perpendicular to the plane of $\vec A$ and $\vec B$ (right-hand cross-product rule).

*Mnemonic used in the lecture:* force $=I\vec L\times\vec B$ ("I love Bhopal"), torque $=I\vec A\times\vec B$ ("I admire Bhopal").

### General case: normal at angle $\theta$ to $B$
Now the loop's normal makes angle $\theta$ (not $90°$) with $\vec B$. Forces on the sides perpendicular to the *original* orientation (QR, SP) turn out equal, opposite, and **collinear** — their resultant is zero. Forces on the other pair (PQ, RS) are equal, opposite, but **not collinear** — these constitute the torque:
$$\tau = (ILB\sin\theta)\times b = IAB\sin\theta$$
$$\boxed{\vec\tau = I(\vec A\times\vec B)}, \qquad |\tau| = IAB\sin\theta$$
The special case above ($\theta=90°$, $\sin\theta=1$, $\tau=IAB$) is the **maximum-torque** special case of this general result.


## Verify these spans
- [25:26–25:29] The transcript's last segment ends right as the general-case torque setup is completed ('force on PQ and RS... will constitute torque') but before the final formula is spoken. A board frame just past this point (floor_000072.jpg, t=1420s) shows the completed derivation and the boxed general result torque=I*A*B*sin(theta) (vector form tau=I(A x B)), so the final general-torque claim above is grounded from that frame rather than the transcript's own words, though it is the direct, expected algebraic completion of what the transcript does establish.