import numpy as np
import csv
import pandas as pd

S = [0xE, 0x4, 0xB, 0x2, 0x3, 0x8, 0x0, 0x9, 0x1, 0xA, 0x7, 0xF, 0x6, 0xC, 0x5, 0xD]
diff = np.zeros([16, 16], dtype=int)
mtx = np.asarray([[2, 3, 1, 1], [1, 2, 3, 1], [1, 1, 2, 3], [3, 1, 1, 2]])
inv = np.asarray([[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]])
ans = -1000


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


def dfs1(var, din, prob, para):
    # print(var)
    # print(din)
    # print(prob)
    # print(para)
    global ans
    if prob < ans:
        return
    # print(ans)
    for i in range(16):
        if diff[din][i] == 0:
            continue
        if diff[din][i] == 2:
            new_prob = prob - 3
        if diff[din][i] == 4:
            new_prob = prob - 2
        para[var] = i
        if var == "xs":
            Col = dot(mtx, np.asarray([0, i, 0, 0]).reshape(4, 1))
            para["a1r"], para["b1r"], para["c1r"], para["d1r"] = (
                Col[0][0],
                Col[1][0],
                Col[2][0],
                Col[3][0],
            )
            dfs1("a1", Col[0][0], new_prob, para)
        if var == "a1":
            dfs1("b1", para["b1r"], new_prob, para)
        if var == "b1":
            dfs1("c1", para["c1r"], new_prob, para)
        if var == "c1":
            dfs1("d1", para["d1r"], new_prob, para)
        if var == "d1":
            dfs2("xr", para["x"], new_prob, para)
    return


def dfs2(var, dout, prob, para):
    # print(var)
    # print(din)
    # print(prob)
    # print(para)
    global ans
    if prob < ans:
        return
    # print(ans)
    for i in range(16):
        if diff[i][dout] == 0:
            continue
        if diff[i][dout] == 2:
            new_prob = prob - 6
        if diff[i][dout] == 4:
            new_prob = prob - 4
        para[var] = i
        if var == "xr":
            Col = dot(inv, np.asarray([0, i, 0, 0]).reshape(4, 1))
            para["a2s"], para["b2s"], para["c2s"], para["d2s"] = (
                Col[0][0],
                Col[1][0],
                Col[2][0],
                Col[3][0],
            )
            dfs2("a2", Col[0][0], new_prob, para)
        if var == "a2":
            dfs2("b2", para["b2s"], new_prob, para)
        if var == "b2":
            dfs2("c2", para["c2s"], new_prob, para)
        if var == "c2":
            dfs2("d2", para["d2s"], new_prob, para)
        if var == "d2":
            if new_prob > ans:
                ans = new_prob
                print("Best Prob:", ans)
                print(para)
    return


if __name__ == "__main__":
    init_diff()
    init_inv()
    for x in range(1, 16):
        para = {}
        para["x"] = x
        dfs1("xs", x, 0, para)
