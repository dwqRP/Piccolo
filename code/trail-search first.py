import numpy as np
import csv
import pandas as pd

S = [0xE, 0x4, 0xB, 0x2, 0x3, 0x8, 0x0, 0x9, 0x1, 0xA, 0x7, 0xF, 0x6, 0xC, 0x5, 0xD]
diff = np.zeros([16, 16], dtype=int)
mtx = np.asarray([[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]])
inv = np.asarray([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])


def init_diff():
    for x in range(1 << 4):
        for y in range(1 << 4):
            din = x ^ y
            dout = S[x] ^ S[y]
            diff[din][dout] += 1
    print(diff)


def mul(x, y):
    res = 0
    p = 0b10011
    for i in range(4):
        if x & (1 << i):
            res ^= y << i
    for i in range(7, 3, -1):
        if res & (1 << i):
            res ^= p << (i - 4)
    return res


def init_inv():
    tmp = np.copy(mtx)
    for i in range(4):
        for j in range(4):
            if j == i:
                continue
            ele = 0
            for o in range(16):
                if mul(tmp[i][i], o) == tmp[j][i]:
                    ele = o
                    break
            for o in range(4):
                tmp[j][o] ^= mul(tmp[i][o], ele)
                inv[j][o] ^= mul(inv[i][o], ele)

    for i in range(4):
        for o in range(16):
            ele = 0
            if mul(tmp[i][i], o) == 1:
                ele = o
                break
        for j in range(4):
            inv[i][j] = mul(inv[i][j], ele)

    print(inv)


def dot(X, Y):
    x = X.shape[0]
    y = X.shape[1]
    assert y == Y.shape[0]
    z = Y.shape[1]
    res = np.zeros([x, z], dtype=int)
    for i in range(x):
        for j in range(z):
            for k in range(y):
                res[i][j] ^= mul(X[i][k], Y[k][j])
    return res


def calc(a, b, c, d, x):
    for i in range(16):
        if diff[i][x] != 4:
            continue
        Col = dot(inv, np.asarray([0, 0, 0, i]).reshape(4, 1))
        if (
            diff[a][Col[0][0]] == 4
            and diff[b][Col[1][0]] == 4
            and diff[c][Col[2][0]] == 4
            and diff[d][Col[3][0]] == 4
        ):
            return True
    return False


if __name__ == "__main__":
    init_diff()
    init_inv()
    # print(dot(mtx, inv))
    lst = []
    for d in range(1, 16):
        print("-------", d, "-------")
        for i in range(16):
            if diff[i][d] != 4:
                continue
            Col1 = dot(inv, np.asarray([0, 0, 0, i]).reshape(4, 1))
            # print(Col0)
            for a1 in range(16):
                if diff[a1][Col1[0][0]] != 4:
                    continue
                for b1 in range(16):
                    if diff[b1][Col1[1][0]] != 4:
                        continue
                    for c1 in range(16):
                        if diff[c1][Col1[2][0]] != 4:
                            continue
                        for d1 in range(16):
                            if diff[d1][Col1[3][0]] != 4:
                                continue

                            for j in range(16):
                                if diff[d][j] != 4:
                                    continue
                                Col2 = dot(mtx, np.asarray([0, 0, 0, j]).reshape(4, 1))
                                for a2 in range(16):
                                    if diff[Col2[0][0]][a2] != 4:
                                        continue
                                    for b2 in range(16):
                                        if diff[Col2[1][0]][b2] != 4:
                                            continue
                                        if calc(a1 ^ a2, b1 ^ b2, c1, d1, d) == True:
                                            lst.append([a1, b1, c1, d1, a2])
                                            print(
                                                "[{}, {}, {}, {}] -> {} -> [0, 0, 0, {}] -> [0, 0, 0, {}] -> [0, 0, 0, {}] -> {} -> [{}, {}, *, *]".format(
                                                    a1,
                                                    b1,
                                                    c1,
                                                    d1,
                                                    Col1.reshape(1, 4)[0],
                                                    i,
                                                    d,
                                                    j,
                                                    Col2.reshape(1, 4)[0],
                                                    a2,
                                                    b2,
                                                )
                                            )
    print(lst)
    head = ["a1", "b1", "c1", "d1", "a2"]
    out = pd.DataFrame(columns=head, data=lst)
    out.to_csv("./log/out.csv", index=False)
