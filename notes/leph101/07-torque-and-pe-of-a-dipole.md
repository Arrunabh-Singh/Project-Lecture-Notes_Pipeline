# Torque and Potential Energy of a Dipole in a Uniform Electric Field

**NCERT sections covered:** 1.11

## Recap: torque
$$\vec\tau = \vec R\times\vec F,\qquad |\vec\tau| = RF\sin\theta$$
Direction perpendicular to the plane of $\vec R,\vec F$, via the right-hand curl rule. Equivalently, for a **couple** (two equal and opposite forces): $\tau = F\times(\text{perpendicular distance between their lines of action})$.

## Torque on a dipole in a uniform field (NCERT 1.11)

Dipole (charges $+Q,-Q$, length $2L$, moment $p=2QL$) at angle $\theta$ to a uniform field $\vec E$. Each charge feels an equal-magnitude force $F=EQ$, but in different directions (since $\vec E$ points from $+$ to $-$) — a couple. The perpendicular distance between the two forces' lines of action is $2L\sin\theta$, so:
$$\tau = F\times 2L\sin\theta = EQ\times2L\sin\theta = PE\sin\theta$$
In vector form:
$$\boxed{\vec\tau = \vec p\times\vec E}$$
direction perpendicular to the plane of $\vec p,\vec E$ (right-hand curl rule, fingers curling from $\vec p$ to $\vec E$).

**Extremes:** torque is **maximum** ($=PE$) at $\theta=90°$ ($\vec p\perp\vec E$); torque is **zero** at $\theta=0°$ or $180°$ ($\vec p$ parallel or antiparallel to $\vec E$) — even though forces still act on each charge individually, there's no net turning effect once aligned.

## Potential energy of a dipole (NCERT 1.11)

Small work done rotating the dipole by $d\theta$: $dW = \tau\,d\theta = PE\sin\theta\,d\theta$ (rotational analogue of $dW=F\,dx$). Integrating from $\theta_1$ to $\theta_2$ (using $\int\sin\theta\,d\theta=-\cos\theta$):
$$W = PE\left[\cos\theta_1-\cos\theta_2\right]$$
This work is stored as potential energy. Taking $\theta_1=90°$ (where $\cos90°=0$) as the zero-PE reference:
$$\boxed{U = -PE\cos\theta = -\vec p\cdot\vec E}$$

### Worked numerical
A dipole with charge $1~\mu\text{C}$, separated by $1$ cm, placed in $E=2\times10^6$ N/C:
- **(i)** Dipole moment: $p = Q\times2L = 10^{-6}\times10^{-2} = 10^{-8}$ C$\cdot$m
- **(ii)** Maximum torque: $\tau_\max = PE = 10^{-8}\times2\times10^6 = 2\times10^{-2}$ N$\cdot$m
- **(iii)** Work done rotating through $180°$ starting from $\theta=0$: $W = PE[\cos0°-\cos180°] = PE[1-(-1)] = 2PE$

---
*Note on this lecture's transcript:* the worked numerical above is grounded entirely from a board frame near the true end of the lecture -- the transcript repeats earlier material there and then stops well short of the lecture's actual end. See the flagged span below.


## Verify these spans
- [25:06–34:06] Two separate transcript problems compound here. First, from roughly t=1506s the transcript re-transcribes the potential-energy derivation (theta1-to-theta2 rotation, the sin/cos integration, U=-PE cos theta) almost verbatim a second time -- a delayed-repetition artifact, not real re-teaching -- before cutting off mid-sentence at t=1883.7s. Second, and more seriously, this transcript's own timestamped coverage stops there entirely: it has NO segments at all for the final ~163 seconds of the lecture's true 2046.5s duration (a genuine truncation, not just a hidden-by-repetition gap). Board frames fill in what was lost: the last captured frame (floor_000102.jpg, t=2020s, well inside the untranscribed window) shows a 'stable eqm' heading (visible only as a two-word label -- the supporting derivation, if any, is off the top of the captured frame and not recoverable from the sampled images) followed by a fully worked numerical (dipole moment, maximum torque, and work done rotating through 180 degrees from theta=0) plus a small formula-summary box. The worked-numerical claim above is grounded entirely from that frame; the stable-equilibrium point is mentioned only as a heading seen on the board, not as a verified claim, since its derivation isn't visible in any captured frame.