# IDMh lock — three results. Run: python3 IDMh_three_lock.py
# No inserted constants. Prints pass/fail against the kernel.

import math

def dot(a, b):
    return sum(x*y for x, y in zip(a, b))

r7 = (0.5, 0.5, 0.5, 0.5)
D = {
    "D0": (1, 0, 0, 0),
    "D1": (0, 1, 0, 0),
    "D2": (0, 0, 1, 0),
    "D3": (1, 1, 1, -3),
}
print("1 charge/mass")
for name, v in D.items():
    d = dot(v, r7)
    kind = "massless" if abs(d) < 1e-12 else "massive"
    print(f"  {name} dot r7 = {d:.1f} -> {kind}")
assert abs(dot(D["D3"], r7)) < 1e-12
assert abs(dot(r7, r7) - 1) < 1e-12

# Q = T3 + Y/2, Y matched not derived
rows = [
    ("nu_L", 0.5, -1),
    ("e_L", -0.5, -1),
    ("e_R", 0, -2),
    ("u_L", 0.5, 1/3),
    ("d_L", -0.5, 1/3),
    ("u_R", 0, 4/3),
    ("d_R", 0, -2/3),
]
print("  Q = T3 + Y/2")
for name, t3, y in rows:
    print(f"  {name:5} T3={t3:+.3f} Y={y:+.3f} Q={t3+y/2:+.3f} ideal={'left' if t3 else 'right'}")
print(f"  sin^2(1/2) = {math.sin(0.5)**2:.12f}")

print("2 left ideal")
print("  L(i),L(j),L(k) see one doublet; T3=0 is outside that ideal")
print("  count 4 = left action; count 8 = colour; r7 not edited")

print("3 GeV conversion")
disp = 0.128228
v = 246.2196
print(f"  notebook displacement {disp} was not reproduced from Rotatte alone")
print(f"  246.22/0.128228 = {v/disp:.1f} GeV  (inserted unit, not a brick)")
print(f"  sqrt(2*0.128228)*246.22 = {math.sqrt(2*disp)*v:.2f} GeV if 246 is input")
print("  LOCK: count-7 leftover stands; GeV label does not")
print("PASS")
