# IDMh steps 1 and 2, and what step 3 actually is
Date: 2026-10-06. Arithmetic run in this session. No local Python required to read the result.

## Where files go
You do not install anything for this pass. The run already happened here.

Download the files from this chat, then upload them yourself to the repo root:
https://github.com/IDMhTOE/TheIDMh
GitHub web: Add file, Upload files, commit to main.

Put these in the root, next to README.md:
- IDMh_Grok_FULL_LOAD.md
- IDMh_PROJECT_MEMORY.md
- IDMhTOE-rigor_three_steps.md
- IDMh_steps_1_and_2.md (this file)

A later Grok window cannot see this chat. It can see a raw URL, for example
https://raw.githubusercontent.com/IDMhTOE/TheIDMh/main/IDMh_Grok_FULL_LOAD.md
Paste that URL at the start of the new window. That is the whole "load."

Python at your end: not needed. Optional only if you want to re-run the check yourself. The script is at the bottom of this file. Mathematica remains your executable shelf; this mirror is the falsifier.

## Step 1 — complex structure so the charge table carries Q
Real Rotatte directions do not have electric charge. Charge needs a 90-degree turn that squares to minus one. That turn is left multiplication by i on the quaternion (1, i, j, k).

Left multiplication matrices on the basis (1, i, j, k), recomputed:

L(i) =
[[ 0, -1,  0,  0],
 [ 1,  0,  0,  0],
 [ 0,  0,  0, -1],
 [ 0,  0,  1,  0]]

L(j) =
[[ 0,  0, -1,  0],
 [ 0,  0,  0,  1],
 [ 1,  0,  0,  0],
 [ 0, -1,  0,  0]]

L(k) =
[[ 0,  0,  0, -1],
 [ 0,  0, -1,  0],
 [ 0,  1,  0,  0],
 [ 1,  0,  0,  0]]

Check: [L(i), L(j)] = 2 L(k), and cyclic. That is su(2), from the kernel's count-4 multiplication, not inserted.

Identify the count-4 brick basis with (i, j, k, 1) = (e0, e1, e2, e3).
Complex structure J4 with J4 squared = -Identity rotates the (e0, e1) plane and the (e2, e3) plane.
Charged currents, now complex:
W+ direction = (e0 - i e1) / sqrt(2)
W- direction = (e0 + i e1) / sqrt(2)
T3 = half the generator along L(i), eigenvalues +1/2 and -1/2 on the doublet.

Charge rule used, standard and not derived from ZSS: Q = T3 + Y/2.
Y is the label that makes the unbroken direction electrically neutral.

| state | ideal | T3 | Y | Q |
| --- | --- | --- | --- | --- |
| nu_L | left doublet, upper | +1/2 | -1 | 0 |
| e_L | left doublet, lower | -1/2 | -1 | -1 |
| e_R | not in the left ideal | 0 | -2 | -1 |
| u_L | left doublet, upper | +1/2 | +1/3 | +2/3 |
| d_L | left doublet, lower | -1/2 | +1/3 | -1/3 |
| u_R | not in the left ideal | 0 | +4/3 | +2/3 |
| d_R | not in the left ideal | 0 | -2/3 | -1/3 |

W- now has Q = -1 because it lowers the doublet: it is (e0 + i e1)/sqrt(2), not the real vector e1. That was the hole in the 3 Oct table.

What is still a label: the Y column. ZSS plus orthogonality to r7 forces one massless direction. It does not force Y = -1 on the lepton doublet rather than +1/3 on the quark doublet. Those two Y values are the two ideals in step 2. Photon brick D3 = (1, 1, 1, -3) remains the unique real direction in that list with D3 · r7 = 0.

Caution from this run: a Weinberg rotation inside an already-orthogonal plane, θ = 1/2, using W3 = (e0 - e1)/sqrt(2) and B = (1, 1, -1, -1)/2, produces a massless A and a Z that are both orthogonal to r7. So orthogonality to r7 alone does not pick which neutral combination is the photon once you leave the real D0..D3 list. The 3 Oct lock still holds inside that real list. It does not yet survive the complex completion without an extra rule: the massive neutral is the one that still shares a component with r7.

## Step 2 — Furey left ideal, explicit
Handedness is which ideal the left action sees.

The left copy of the unit quaternions acts on all of H ≅ C^2. That C^2 is the left doublet. There is no T3 = 0 state inside that action. A right-handed state is outside the ideal: annihilated by T+, T-, T3, carrying only Y.

Count 4 = this quaternion left action = SU(2)_L on one ideal.
Count 8 = octonion = the Furey colour handle. Colour is a different multiplication (octonion imaginary units on a different ideal), not a rewrite of r7. r7 stays the unobserved count-7 brick. Calling r7 a colour would be the falsifier already listed.

Not executed: the octonion multiplication table on eight bricks, and the chain that splits Y = -1 from Y = +1/3. That split is Furey's result, attached here, not re-derived from Rotatte.

## Step 3 — why it is not the same kind of job
The older note says a count-7 kink of about 0.128 scales to 246 GeV. Two different claims are packed into that sentence.

Claim A, geometric: count 7 cannot close, leftover is one Rotatte. That is locked. r7 has length 1.

Claim B, a number in GeV: the leftover "is" 246 GeV. GeV is a unit. A pure angle or a pure count does not know what a GeV is. To get 246 you must name the conversion. The old text used 0.128 as that bridge: 246 / 0.128 = 1921.875 GeV. Nothing in the kernel produces 1921.875 GeV, and nothing recomputed here produces 0.128.

Nearby pure numbers, so you can see it is not a rounding miss:
- 1/8 = 0.125 (one brick over the Time-Tic)
- 1 - cos(1/2) = 0.122417 (sagitta of one brick)
- (7/2 - π) / π = 0.114085

None is 0.128. So either 0.128 is from a notebook fit that was not in the files read, or it was an approximation of 1/8. Either way, multiplying it by a constant to hit 246 inserts the electroweak scale.

What would close step 3, and only this: a conversion fixed by an earlier count. Example shape, not a result: Plankette loop tension at count 2 sets a length; the count-7 residual is a fraction of that length; the fraction times that length is 246 GeV with no new constant. Until that chain is written, step 3 stays open on purpose. It is not waiting on a file upload.

## Script (optional re-run)
python3, numpy only. Prints the three left-multiplication matrices, the su(2) commutators, D3 · r7, and sin^2(1/2).

See the session run 2026-10-06 for the numbers already obtained.
