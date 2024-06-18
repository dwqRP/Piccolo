S = [0xe, 0x4, 0xb, 0x2, 0x3, 0x8, 0x0, 0x9, 0x1, 0xa, 0x7, 0xf, 0x6, 0xc, 0x5, 0xd]
diff = []
points = []
for din in range(16):
    diff.append([0]*16)
    for x in range(16):
        dout = S[x] ^^ S[x ^^ din]
        diff[din][dout] += 1

for i in range(16):
    for j in range(16):
        if diff[i][j] > 0:
            point = []
            for p in range(3, -1, -1):
                if i & (1 << p):
                    point.append(1)
                else:
                    point.append(0)
            for p in range(3, -1, -1):
                if j & (1 << p):
                    point.append(1)
                else:
                    point.append(0)
            points.append(point)
poly = Polyhedron(vertices = points)
for l in poly.inequality_generator():
    print(l)
