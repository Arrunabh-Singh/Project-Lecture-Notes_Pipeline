# A Dipole in a Uniform Magnetic Field Performs SHM

**NCERT sections covered:** 5.2.3

## Recap: the spring-mass SHM condition (Class 11 link)
Before proving the magnetic result, the lecture re-derives the spring-mass SHM condition as a template: a spring stretched by $x$ has restoring force $F=-kx$, so $ma=-kx \Rightarrow a=-\dfrac{k}{m}x=-\omega^2x$. Since acceleration is proportional to $-(\text{displacement})$, this is simple harmonic motion, obeying the general equation
$$\frac{d^2x}{dt^2}+\omega^2 x = 0$$
The same logic carries over to *angular* quantities: replacing $x\to\theta$ and $a\to\alpha$ (angular acceleration), if $\alpha\propto-\theta$ then $\dfrac{d^2\theta}{dt^2}+\omega^2\theta=0$ and the angular motion is SHM too. This angular version is what the main derivation below needs.

## Derivation: a dipole in a uniform field performs SHM (NCERT 5.2.3)
A magnetic dipole (a short bar magnet, moment $\vec M$) is placed in a uniform field $\vec B$, making angle $\theta$ with it. It experiences a **deflecting torque**
$$\vec\tau = \vec M\times \vec B, \qquad \tau = MB\sin\theta$$
By the rotational analogue of Newton's second law ($F=ma \to \tau=I\alpha$, with moment of inertia $I$ in place of mass and angular acceleration $\alpha$ in place of linear acceleration):
$$I\alpha = -MB\sin\theta$$
The minus sign is because the **restoring** torque set up by the field acts opposite to the deflecting displacement -- exactly like $F=-kx$ in the spring case.

For small angular displacement, $\sin\theta\approx\theta$, so
$$I\alpha = -MB\theta \quad\Rightarrow\quad \alpha = -\frac{MB}{I}\theta$$
Since $\alpha\propto-\theta$, this **is** SHM, with
$$\omega^2 = \frac{MB}{I}, \qquad T = 2\pi\sqrt{\frac{I}{MB}} \quad\left(\text{equivalently } B=\frac{4\pi^2 I}{MT^2}\right)$$
This last rearranged form is useful whenever a problem gives the period of oscillation and asks for the unknown field or moment.

## Worked numerical 1: field from an oscillating magnetic needle
A magnetic needle has moment $M=6.7\times10^{-2}$ A m$^2$ and moment of inertia $I=7.5\times10^{-6}$ kg m$^2$, and completes 10 oscillations in 6.7 s.

**Time period:** $T = \dfrac{6.7}{10} = 0.67$ s.

**Field:** using $B=\dfrac{4\pi^2 I}{MT^2}$,
$$B \approx 0.01~\text{T}$$

## Worked numerical 2: bar magnet vs. equal-moment solenoid (3 parts)
A short bar magnet, axis at $30^\circ$ to an external field $B=800$ G, experiences torque $\tau=0.016$ N m. First convert the field to SI: $1$ T $=10^4$ G, so $B = 800\times10^{-4}~\text{T} = 0.08$ T.

**(i) Find $M$:** from $\tau = MB\sin\theta$,
$$M = \frac{\tau}{B\sin\theta} = \frac{0.016}{0.08\times\sin30^\circ} = 0.4~\text{A m}^2$$

**(ii) Work done moving the magnet from its most stable to its most unstable position.** Most stable is $\vec M\parallel\vec B$ ($\theta_1=0^\circ$); most unstable is $\vec M$ antiparallel to $\vec B$ ($\theta_2=180^\circ$). Work done against the restoring torque:
$$W = \int_{\theta_1}^{\theta_2}\tau\,d\theta = \int_{\theta_1}^{\theta_2}MB\sin\theta\,d\theta = MB\big[\cos\theta_1-\cos\theta_2\big] = MB\big(1-(-1)\big) = 2MB = 0.064~\text{J}$$

**(iii) Same magnet replaced by a solenoid of the same moment $M$**, with cross-sectional area $A=2\times10^{-4}$ m$^2$ and $N=1000$ turns. From $M=NIA$:
$$I = \frac{M}{NA} = \frac{0.4}{1000\times2\times10^{-4}} = 2~\text{A}$$

---
*Note on this lecture:* part (i) of numerical 2 is confirmed in both transcript and board frames, but the transcript audio track trails off mid-sentence right as parts (ii) and (iii) begin, well before reaching either result -- see the flagged span below. Both results were recovered directly from later board frames (`floor_000048.jpg`, `floor_000053.jpg`) that exist in the frames folder on disk but were dropped from the coverage-floor sampler's deduped `index.json` list (likely misjudged as near-duplicates of the preceding frame by the perceptual-hash dedupe step, since the board changes only incrementally as new lines are added below existing text) -- worth flagging upstream, since it means `index.json` alone is not a reliable guide to what content exists in a lecture's frame folder.


## Verify these spans
- [14:48–17:33] The transcript trails off mid-sentence at its last segment ('unstable position means unstable position means', ending 1060s) right as the teacher is setting up part (ii) of the second numerical (most-stable-to-most-unstable work done) -- it never reaches the computation of W, nor part (iii) (replacing the bar magnet with a solenoid to find the current). This does not look like the delayed-repeat fabrication loop (no earlier block is re-transcribed) -- it reads like the ASR response simply ran out/was cut short near the true end of the audio. The board-frame coverage-floor sampler's deduped index (index.json) also stops at t=880s (floor_000045), but the raw frames directory retains later, non-deduped frames (floor_000046 through floor_000053) that a direct check confirms DO carry new content -- floor_000048.jpg shows part (ii)'s full work-done derivation (W=2MB=0.064 J) and floor_000053.jpg shows part (iii)'s solenoid current result (I=2 A) freshly added beside it. Both of the two claims above for parts (ii) and (iii) are grounded from these board-only frames, with no transcript corroboration -- the physics is standard and consistent with the board's own part (i) answer and the given N, A, so treated as reliable, but flagged here since it could not be cross-checked against narration.