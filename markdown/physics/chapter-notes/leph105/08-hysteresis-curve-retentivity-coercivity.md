# Hysteresis Curve: Retentivity, Coercivity, and Soft Iron vs. Steel

**NCERT sections covered:** 5.5

## The hysteresis curve (NCERT 5.5)

A solenoid carries current $I$ with an iron rod (magnetizing material) inside. The **hysteresis curve** plots $B$ (total field inside the material — related to how many of its dipoles are aligned) against $H$ (related to the coil current).

**Tracing the loop:**
- **O:** initially $B=0$, $H=0$ (no current).
- **O$\to$A:** current increased $\Rightarrow$ $H$ increases $\Rightarrow$ $B$ increases (domains align with $B$). At **A**, $B$ stops increasing however much $H$ increases further — this is the **saturation point** (all domains now aligned).
- **A$\to$B:** current (and $H$) decreased back toward zero — but $B$ does *not* retrace the same path. When $H=0$, $B$ is still non-zero: $OB$ is the **retentivity** (residual magnetism) — the material stays magnetized after the current is switched off.
- **B$\to$C:** to bring $B$ back to zero, the current must be **reversed** and increased. Where $B=0$ (with $H\ne0$, reversed) is point $C$: $OC$ is the **coercivity** — the reverse field needed to fully demagnetize. Larger coercivity $\Rightarrow$ harder to demagnetize.
- **C$\to$D$\to$...$\to$A:** increasing the reversed current further reaches negative saturation at $D$; repeating the same steps in the forward direction (through $E$, $F$) closes the loop back at $A$.

**Hysteresis:** the phenomenon of $B$ *lagging behind* $H$ when a magnetic specimen is taken through a cycle of magnetisation. The closed $B$–$H$ curve traced is the **hysteresis loop**.

**Area of the loop** = energy dissipated per unit volume, per cycle (the substance heats up) — the bigger the loop, the greater the dissipation.

## Soft iron vs. steel

Comparing their hysteresis loops (steel's is visibly wider):
1. Retentivity: **steel < soft iron**
2. Coercivity: **steel > soft iron** $\Rightarrow$ steel is used for **permanent magnets** (harder to demagnetize)
3. Loop area: **steel > soft iron** $\Rightarrow$ hysteresis loss in soft iron is **less** $\Rightarrow$ soft iron is used in **electromagnets** (repeatedly (de)magnetized, so low loss matters)

### Making a permanent magnet
1. Hold an iron/steel rod in the N–S direction and hammer it repeatedly.
2. Hold a steel rod and stroke it repeatedly (many times), always in the same sense, with one end of a bar magnet.

---
*Note on this lecture's transcript:* the loop-construction explanation (saturation, retentivity, coercivity) is transcribed correctly once, then repeated nearly verbatim a second time -- inflating the transcript's own timestamps past the video's true duration. The final soft-iron-vs-steel comparison and the two permanent-magnet methods are visible in full on the board but never make it into the transcript's own words at all (it cuts off announcing the topic). Both are grounded entirely from frames; see the flagged spans below.


## Verify these spans
- [03:53–17:40] The full explanation of the hysteresis curve's construction (saturation at A, decreasing H giving retentivity at B, reversing current to reach coercivity at C, the fourth/fifth steps) is transcribed once correctly (~t=233-660s) and then transcribed a SECOND time nearly verbatim (~t=692-1015s) -- the same delayed-repetition pattern found repeatedly in this chapter's lectures. This inflated the transcript's own self-reported timestamps: its last segment claims to end at 1724.84s even though the video's true duration is only 1661.0s, confirming the internal duplication pushed later timestamps out of sync with real video time. Content-wise nothing appears lost here (the two passes say the same thing), but the timestamps attached to claims in the back half of this note should be read as approximate.
- [26:46–27:41] The transcript's own words announce the final topic twice ('Now we have hysteresis curve for soft iron and steel', repeated) and then cut off mid-sentence while just starting to draw a B-H curve ('I have a curve something like this... A curve main aise draw kar rahi hoon'), giving the impression the lecture ends before this comparison is actually taught. However, a board frame (floor_000067.jpg) -- whose own true video timestamp (t=1320s) falls chronologically BEFORE this final transcript segment's self-reported (drifted, see the span above) timestamp -- shows the soft-iron-vs-steel comparison already fully written out: three comparison properties (retentivity, coercivity, loop area/hysteresis loss) plus two practical methods for making a permanent magnet. This confirms the teacher did complete this topic on the board within the true 1661s runtime; the transcript simply never captured the spoken explanation of it. All of the soft-iron/steel and permanent-magnet content in this note is grounded entirely from that frame, not from the transcript's own words.