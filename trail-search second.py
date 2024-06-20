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


def check1(c3, d3, c1, d1):
    res = []
    for c3s in range(16):
        if diff[c3][c3s] == 0:
            continue
        for d3s in range(16):
            if diff[d3][d3s] == 0:
                continue
            Col = dot(mtx, np.asarray([0, 0, c3s, d3s]).reshape(4, 1))
            if Col[0][0] == 0 and diff[Col[2][0]][c1] != 0 and diff[Col[3][0]][d1] != 0:
                for i in range(16):
                    if diff[Col[1][0]][i] != 0:
                        if res.count(i) == 0:
                            res.append(i)
    return res


def check2(x, a, b, c):
    res = []
    for xs in range(16):
        if diff[x][xs] == 0:
            continue
        Col = dot(mtx, np.asarray([0, xs, 0, 0]).reshape(4, 1))
        if (
            diff[Col[0][0]][a] != 0
            and diff[Col[1][0]][b] != 0
            and diff[Col[2][0]][c] != 0
        ):
            for i in range(16):
                if diff[Col[3][0]][i] != 0:
                    if res.count(i) == 0:
                        res.append(i)
    return res


def calc(p, q, x, y, z):
    for ps in range(16):
        if diff[p][ps] == 0:
            continue
        for qs in range(16):
            if diff[q][qs] == 0:
                continue
            Col = dot(mtx, np.asarray([0, ps, 0, qs]).reshape(4, 1))
            if (
                Col[0][0] == 0
                and diff[Col[1][0]][x] != 0
                and diff[Col[2][0]][y] != 0
                and diff[Col[3][0]][z] != 0
            ):
                return True
    return False


def dfs(var, din, prob, para):
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
            new_prob = prob - 1
        if diff[din][i] == 4:
            new_prob = prob
        para[var] = i
        if var == "c2":
            dfs("d2", 4, new_prob, para)
        if var == "d2":
            dfs("c2s", para["c2"], new_prob, para)
        if var == "c2s":
            dfs("d2s", para["d2"], new_prob, para)
        if var == "d2s":
            Col = dot(mtx, np.asarray([0, 0, para["c2s"], para["d2s"]]).reshape(4, 1))
            if Col[0][0] != 0:
                continue
            para["Col10"], para["Col20"], para["Col30"] = (
                Col[1][0],
                Col[2][0],
                Col[3][0],
            )
            dfs("b3", Col[1][0], new_prob, para)
        if var == "b3":
            dfs("c3", para["Col20"], new_prob, para)
        if var == "c3":
            dfs("d3", para["Col30"], new_prob, para)
        if var == "d3":
            dfs("c3s", para["c3"], new_prob, para)
        if var == "c3s":
            dfs("d3s", para["d3"], new_prob, para)
        if var == "d3s":
            Col = dot(mtx, np.asarray([0, 0, para["c3s"], para["d3s"]]).reshape(4, 1))
            if (
                Col[0][0] != 0
                or diff[Col[2][0]][para["c1"]] == 0
                or diff[Col[3][0]][para["d1"]] == 0
            ):
                continue
            if diff[Col[2][0]][para["c1"]] == 2:
                new_prob -= 1
            if diff[Col[3][0]][para["d1"]] == 2:
                new_prob -= 1
            dfs("b4", Col[1][0], new_prob, para)
        if var == "b4":
            dfs("b3s", para["b3"], new_prob, para)
        if var == "b3s":
            Col = dot(mtx, np.asarray([0, para["b3s"], 0, 0]).reshape(4, 1))
            vone = para["a1"] ^ para["a2"]
            vtwo = para["b1"] ^ 5
            if (
                diff[Col[0][0]][vone] == 0
                or diff[Col[1][0]][vtwo] == 0
                or diff[Col[2][0]][para["c2"]] == 0
            ):
                continue
            if diff[Col[0][0]][vone] == 2:
                new_prob -= 1
            if diff[Col[1][0]][vtwo] == 2:
                new_prob -= 1
            if diff[Col[2][0]][para["c2"]] == 2:
                new_prob -= 1
            dfs("d4", Col[3][0], new_prob, para)
        if var == "d4":
            dfs("b4s", para["b4"], new_prob, para)
        if var == "b4s":
            dfs("d4s", para["d2"] ^ para["d4"], new_prob, para)
        if var == "d4s":
            Col = dot(mtx, np.asarray([0, para["b4s"], 0, para["d4s"]]).reshape(4, 1))
            if (
                Col[0][0] != 0
                or diff[Col[1][0]][para["b3"]] == 0
                or diff[Col[2][0]][para["c3"]] == 0
                or diff[Col[3][0]][para["d3"]] == 0
            ):
                continue
            if diff[Col[1][0]][para["b3"]] == 2:
                new_prob -= 1
            if diff[Col[2][0]][para["c3"]] == 2:
                new_prob -= 1
            if diff[Col[3][0]][para["d3"]] == 2:
                new_prob -= 1
            if new_prob > ans:
                ans = new_prob
                print("Best Prob:", ans)
                print(para)

    return


if __name__ == "__main__":
    init_diff()
    init_inv()
    # print(dot(mtx, inv))
    input = pd.read_csv("out.csv")
    for i in range(64):
        para = input.loc[i]
        # a1, b1, c1, d1, a2 = (
        #     para["a1"],
        #     para["b1"],
        #     para["c1"],
        #     para["d1"],
        #     para["a2"],
        # )
        # print(a1, b1, c1, d1, a2)
        # d = b2 = 5
        # 2 2 6 4
        para["d"] = 5
        para["b2"] = 5
        # print(para)
        dfs("c2", 6, -70, para)
        # for c2 in range(16):
        #     if diff[6][c2] == 0:
        #         continue
        #     if diff[6][c2] == 2:
        #         prob -= 1
        #     for d2 in range(16):
        #         if diff[4][d2] == 0:
        #             continue
        #         if diff[4][d2] == 2:
        #             prob -= 1
        #         for c2s in range(16):
        #             if diff[c2][c2s] == 0:
        #                 continue
        #             if diff[c2][c2s] == 2:
        #                 prob -= 1
        #             for d2s in range(16):
        #                 if diff[d2][d2s] == 0:
        #                     continue
        #                 if diff[d2][d2s] == 2:
        #                     prob -= 1
        #                 Col1 = dot(mtx, np.asarray([0, 0, c2s, d2s]).reshape(4, 1))
        #                 if Col1[0][0] != 0:
        #                     continue
        #                 for b3 in range(16):
        #                     if diff[Col1[1][0]][b3] == 0:
        #                         continue
        #                     if diff[Col1[1][0]][b3] == 2:
        #                         prob -= 1
        #                     for c3 in range(16):
        #                         if diff[Col1[2][0]][c3] == 0:
        #                             continue
        #                         for d3 in range(16):
        #                             if diff[Col1[3][0]][d3] == 0:
        #                                 continue
        #                             b4_lst = check1(c3, d3, c1, d1)
        #                             d4_lst = check2(b3, a1 ^ a2, b1 ^ b2, c2)
        #                             if b4_lst == [] or d4_lst == []:
        #                                 continue
        #                             for b4 in b4_lst:
        #                                 for d4 in d4_lst:
        #                                     if calc(b4, d2 ^ d4, b3, c3, d3) == True:
        #                                         print("1111")
