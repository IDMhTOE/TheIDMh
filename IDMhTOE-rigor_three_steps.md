# IDMhTOE-rigor — three open steps
Date: 2026-10-06. Sources: Meta_Self_Timeline_To_10_2_26.txt (section IDMhTOE-rigor), photon brick 2026-10-03, README kernel. Arithmetic checked in this session. Not a claim that the Standard Model has been derived.

Open steps named in the rigor ledger:
1. Hypercharge vs T3 generator table from D0..D3
2. SU(2)_L only on left-handed states — Furey handle, not ZSS-only
3. Numerical VEV ~246 GeV from the ~0.128 kink

## 0. Kernel check (recomputed)
Rotatte undividable. r7 = (e0+e1+e2+e3)/2, |r7|^2 = 1.
D0=e0, D1=e1, D2=e2, D3=e0+e1+e2-3 e3.
Dots with r7: 1/2, 1/2, 1/2, 0. D3 is the unique count-4 direction in this construction orthogonal to r7.
sin^2(1/2) = 0.22984884706593015. PDG sin^2 θ_W(M_Z) is about 0.23122. Delta about -0.00137. Geometry gives a vacuum number; it does not give the running.

Label map used below, not forced by ZSS alone: D0→W+, D1→W−, D2→neutral mix, D3→photon slot.

## 1. Hypercharge vs T3 table
Working basis: four orthogonal Rotatte directions e0,e1,e2,e3. Generators below are the smallest real combinations that match the photon brick. They are a table, not a Lie-algebra proof.

Unbroken direction (massless slot), un-normalized:
D3 = (1, 1, 1, -3)
Normalized photon direction n_A = D3 / √12 = (1, 1, 1, -3)/√12.

Charged pair, orthonormal in the e0–e1 plane:
T+ direction = e0, T− direction = e1.
Cartan in that plane: T3_vec = (e0 - e1)/√2 = (1, -1, 0, 0)/√2.
Orthogonal neutral partner inside the weak 3-space, before mixing: n_W3 candidate = (e0+e1-2 e2)/√6, which is orthogonal to e0-e1 and to (1,1,1) in the first three coords. This is a choice of completion, not read off from ZSS.

Hypercharge direction must be the combination that, mixed with the neutral weak direction, lands on n_A and is orthogonal to the massive leftovers. One vector orthogonal to r7 and to (e0-e1) is
Y_vec = (1, 1, -1, -1)/2, |Y_vec|^2 = 1, Y_vec · r7 = 0.
Y_vec · D3 = (1+1-1+3)/2 = 2 ≠ 0, so Y_vec is not the photon; it mixes.

Proposed assignment (Q = T3 + Y/2 on a doublet-like pair living in span{e0,e1}, singlet in e3):

| slot | vector | · r7 | T3 label | Y label | Q = T3+Y/2 | mass call |
| --- | --- | --- | --- | --- | --- | --- |
| D0 W+ | e0 | 1/2 | +1/2 on the charged plane | +1/2 if doublet | +1 | massive, not orthogonal to r7 |
| D1 W− | e1 | 1/2 | -1/2 | +1/2 | 0 on a pure T3 reading — conflict | massive |
| D2 Z mix | e2 | 1/2 | 0 | mixed | 0 after mixing | massive |
| D3 photon | e0+e1+e2-3 e3 | 0 | 0 | the unbroken combo | 0 | massless by orthogonality |

Conflict that rigor has to close: e1 as “W−” does not by itself carry Q=−1 if T3 and Y are both read as coefficients on the same R^4 basis. W− needs the complex structure (e0 ∓ i e1)/√2, which is not in the real Rotatte list. That complex structure is exactly the quaternionic / Furey handle in step 2. Until that is written, the table identifies one massless direction and three non-orthogonal directions. It does not yet assign electric charges.

Mixing angle forced only if the relative phase between r7 and the neutral count-4 direction is one brick: θ = 1/2 radian, sin^2 θ = sin^2(1/2). Any other split of that phase splits Rotatte, which the kernel forbids. Running from 0.22985 to the measured 0.231 is not derived here.

## 2. Left-handed chirality — Furey handle
ZSS + orthogonality do not know handedness. Pair production gives a pair, not a chiral projection.

What Furey actually supplies (external, not re-derived): one generation from complex octonion chains, or from Cl(8) / Dixon algebra R⊗C⊗H⊗O. Colour SU(3) from the octonion imaginary units acting on an ideal. Electroweak from left multiplication by unit quaternions, which is an SU(2) action on one chiral ideal, while the conjugate / right action is not the same doublet. That is the standard place a left-handed SU(2)_L appears without being inserted by hand into the gauge list.

IDMh attachment, stated as a map:
- Count 4 = quaternionic space = the four directions e0..e3 already used for D0..D3. Left multiplication by i,j,k is the candidate SU(2)_L. It acts on a left ideal, not on the conjugate ideal.
- Count 8 = octonion = Time-Tic = Furey colour / triality handle. Author kernel already places quarks at count 8 and Mac Gregor’s electron at count 4.
- Chirality is the choice of ideal, not a new brick. A right-handed singlet is the state annihilated by that left action (hypercharge only). That matches the open ledger line: SU(2)_L acts only on left-handed states, needs the Furey handle, not ZSS-only.

Not done: explicit left-multiplication table on the count-4 basis showing (e0 ∓ i e1)/√2 are the charged currents, and that the conjugate ideal has T3=0. That is the next executable line. No notebook in the root listing was executed here.

## 3. VEV number 246 GeV from a 0.128 kink
Older status text (README / Mar 2026 X note) says heptagon kink displacement ≈ 0.128 scales to 246 GeV. This kernel does not re-derive 0.128.

Checked geometric residuals near that number:
- 1/8 = 0.125 (one brick over the Time-Tic count)
- 1 - cos(1/2) = 0.122417 (sagitta of one brick)
- (7/2 - π)/π = 0.114085
- 1/e^2 = 0.135335
None of these is 0.128. The figure 0.128 is an older notebook claim, not a count-7 identity in the files read today.

Scale check: 246 / 0.128 = 1921.875 GeV; 246 / 0.125 = 1968 GeV. That quotient is an inserted unit unless a prior count fixes it (Plankette loop to electroweak). No such conversion was in the photon brick or the rigor tail. So: residual-at-7 is derived; “= 246 GeV” is not, until the unit is derived.

## Ledger after this pass
Derived: r7 one brick; D3 orthogonal; three directions not; sin^2(1/2)=0.229848847.
Mapped, not closed: W/Z/photon names; θ_W = one brick.
Open: complex structure so W− has Q=−1; Furey left-ideal table; VEV unit; running of sin^2 θ_W.
Falsifiers unchanged from the 2026-10-03 brick: count 7 closing with no leftover; a fourth massless weak direction after r7; splitting Rotatte to hit 0.231; count 8 deleting r7; calling r7 a colour.
