surface = [33, 33, 33, 1]
r0, g0, b0, a0 = surface

overlay = [255, 255, 255, 0.05]
r1, g1, b1, a1 = overlay

a01 = (1 - a0) * a1 + a0

r01 = ((1 - a0) * a1 * r1 + a0 * r0) / a01

g01 = ((1 - a0) * a1 * g1 + a0 * g0) / a01

b01 = ((1 - a0) * a1 * b1 + a0 * b0) / a01

print(r01, g01, b01, a01)


rA = 1 - (1 - a1) * (1 - a0);
rR = r1 * a1 / rA + r0 * a0 * (1 - a1) / rA;
rG = g1 * a1 / rA + g0 * a0 * (1 - a1) / rA;
rB = b1 * a1 / rA + b0 * a0 * (1 - a1) / rA;

print([rR, rG, rB, rA])
