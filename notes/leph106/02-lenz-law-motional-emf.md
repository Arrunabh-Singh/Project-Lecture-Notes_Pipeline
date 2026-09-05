# Lenz's Law and Motional EMF

**NCERT sections covered:** 6.4, 6.5, 6.6

## Recap: Faraday's law gives magnitude only (NCERT 6.4)
$$|\varepsilon| = N\frac{d\Phi_B}{dt}$$
This tells you *how much* emf is induced, but not its *direction* -- for that, we need **Lenz's law**.

## Lenz's Law (NCERT 6.5)
**Statement:** the direction of an induced emf (and the current it drives) is always such that it **opposes the cause that produces it**.

**Why -- derived from energy conservation, not asserted:** bring the north pole of a magnet towards a coil.
- *Suppose* the coil's near face became a **south** pole. South attracts north, so the coil would pull the magnet in on its own, with **no work done by you** -- yet a current (energy) would appear. That is a free lunch, forbidden by conservation of energy.
- So the near face **must** become **north** instead. You now have to do mechanical work pushing the magnet in *against* this repulsion -- and it is exactly that mechanical work which converts into the induced electrical energy.

Run the same argument with the magnet being *withdrawn*: the near face must become attractive (opposite pole), so you do work pulling it away against attraction -- which is also why the induced current reverses direction between approach and withdrawal (matching Experiment 1 from Lecture 1). **Lenz's law is thus a restatement of conservation of energy**, and the minus sign in $\varepsilon = -N\,d\Phi_B/dt$ (restored explicitly later this lecture) is its mathematical signature.

### Worked Lenz's-law problems (direction-finding practice)
The board works through several loop-crossing-a-field-boundary problems using the right-hand rule (curl fingers along the trial current, thumb gives the field that current would create; the real current must be whichever direction makes that field **oppose** the actual flux change):
- A triangular loop $ABC$ dragged through a field region into the page: **anti-clockwise** while entering (opposing increasing flux), **no current** while fully inside and flux is momentarily steady, **clockwise** while leaving (opposing decreasing flux).
- The same technique repeated for circular and square loops crossing a field boundary.
- A straight current-carrying wire next to a small coil: coil current is clockwise when the wire's current (and hence its field) is increasing.
- A coil approaching a bar magnet's field region, solved by the pole-facing method.

*(These worked examples are grounded from board frames -- see the flagged spans below for why the transcript is not a reliable source for this material.)*

## Motional EMF (NCERT 6.6)
**Setup:** since $\Phi_B = BA\cos\theta$, emf can be induced by changing $B$, changing $A$, or changing $\theta$. Changing $B$ is the Faraday/Lenz case just covered; changing the **area** is new and gives **motional emf**.

**Derivation (flux rule).** A conducting rod $ab$ of length $l$ slides with velocity $v$ along rails, in a uniform field $B$ into the page. In time $dt$ it sweeps extra area $dA = l\,dx$:
$$d\Phi_B = B\,dA = B\,l\,dx \quad\Rightarrow\quad \varepsilon = -\frac{d\Phi_B}{dt} = -Bl\frac{dx}{dt} = -Blv$$
Because the emf here comes from the conductor's own **motion** (not a changing $B$), this is called **motional emf**:
$$\boxed{\varepsilon = -Blv} \qquad (B, l, v \text{ mutually perpendicular})$$

**Direction -- Fleming's Right Hand Rule (FRHR):** thumb = direction of motion ($v$), forefinger = magnetic field ($B$), centre finger = induced current.

**Special and general cases:**
- If $v \parallel B$: **no emf is induced** (the rod's motion has no component driving charges along its length relative to the field).
- If the rod and its velocity are both inclined at angle $\theta$ to $B$ (the fully general case): $\varepsilon = Blv\sin\theta$.

---
*Note on this lecture's transcript:* the opening recap and the Lenz's-law energy-conservation argument (roughly the first 950 seconds of real content) are well corroborated by both transcript and board frames. Past that point, the transcript becomes unreliable -- a large block of earlier material gets re-transcribed a second and even a third time with fabricated later timestamps, silently standing in for the real audio. As a direct result, **every worked Lenz's-law practice problem past the ABC-loop case, the explicit $\varepsilon=-N\,d\Phi_B/dt$ recombination, and this lecture's entire motional-emf derivation (its own named second topic) are grounded from board frames alone.** See the flagged spans below for the full timeline and why the automated coverage/repetition checks did not catch it.


## Verify these spans
- [10:46–35:34] Severe delayed-duplication, worse than a single repeat: the same block of content (magnet-withdrawal Lenz argument through the ABC-loop right-hand-rule problem, corresponding to real segments ~44-100) appears to have been re-transcribed by the model a SECOND time as segments 101-132 (timestamps 1632.2-1888.8s) and a THIRD time as segments 133-167 (timestamps 1888.8-2134.8s, i.e. running to and past the true 2129.8s end) -- e.g. segment 71@1070s / 143@1966s / 159@2072s are a near-verbatim ratio=1.00 triple, as are several dozen other pairs the delayed-duplicate scan flagged (54 pairs total, ratios 0.71-1.00). check_coverage()/sanitize_segments() do not catch this: duration coverage is ~100% and repetition_detected is False, because none of the duplicate segments are ADJACENT to their earlier twin -- each recurrence is separated by many segments, exactly the blind spot this scan exists for.
- [15:50–35:29] Consequence of the above: essentially everything the board shows from floor_000049 (t=960s) onward is missing from the ASR transcript, which spends that entire real-time window re-outputting earlier material under fabricated later timestamps instead. No transcript segment anywhere in this 168-segment transcript contains the words 'motional', 'Blv', 'Fleming', or 'Lorentz' -- despite 'motional emf' being this lecture's own named second topic, and despite a complete board derivation of it existing on schedule, well inside the verified 2129.8s duration. Board timeline used to ground this note: floor_000049 (960s) circle/square/triangle Lenz practice problems; floor_000059 (1160s) current-carrying-wire-and-coil problem; floor_000063/65 (1240-1280s) coil-approaching-magnet problem; floor_000071/73 (1400-1440s) Faraday+Lenz recombined WITH the minus sign, then 'ways to induce emf'; floor_000077-87 (1520-1720s) the full motional-emf flux-rule derivation to eps=-Blv; floor_000089/91 (1760-1800s) Fleming's Right Hand Rule; floor_000095-106 (1880-2100s, the last extracted frame) the v-parallel-to-B null case and the general eps=Blv*sin(theta) case, which is where the board's own content ends, matching the lecture's true runtime closely. Every claim in this note past 'the ABC-loop problem' is grounded from board frames alone for exactly this reason.