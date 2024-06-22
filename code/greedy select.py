import numpy as np
import random

M = [
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0],
    [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0],
    [0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0],
]


def init_DDT():
    S = [0xE, 0x4, 0xB, 0x2, 0x3, 0x8, 0x0, 0x9, 0x1, 0xA, 0x7, 0xF, 0x6, 0xC, 0x5, 0xD]
    # Modify your sbox here
    ddt = np.zeros([16, 16], int)
    for din in range(16):
        for x in range(16):
            dout = S[x] ^ S[x ^ din]
            ddt[din][dout] += 1
    return ddt


def process_sage_output():
    coeff = []
    with open("./log/Convex hull of S box with prob.txt", "r") as f:
        # Put your sage output in this file
        for line in f.readlines():
            lst = []
            line = line.strip("\n")
            assert line.startswith("An inequality (")
            line = line[14:]
            w = 1
            for idx, ch in enumerate(line):
                if ch == "(" or ch == " ":
                    pos = idx + 1
                if ch == "," or ch == ")":
                    lst.append(int(line[pos:idx]))
                if ch == "+":
                    w = -1
                    fpos = idx + 2
                if ch == "-":
                    fpos = idx + 2
                if ch == ">":
                    lst.append(w * int(line[fpos : idx - 1]))
            coeff.append(lst)
    # print(coeff)
    return coeff


def check(p, q):
    res = 0
    for i in range(10):
        res += p[i] * q[i]
    return res >= q[10]


def Output_to_file(choose):
    extra_prob = -1
    # Input this probablity to add extra inequalities to model
    w = open("./log/Convex hull of S box with prob after selected.txt", "w")
    with open("./log/Convex hull of S box with prob.txt", "r") as f:
        idx = 0
        for line in f.readlines():
            if choose[idx]:
                w.write(line)
            else:
                if random.random() < extra_prob:
                    w.write(line)
            idx += 1


if __name__ == "__main__":
    coeff = process_sage_output()
    # print(coeff)
    ddt = init_DDT()
    diff = np.zeros([16, 16], int)
    # print(diff)
    for i in range(1 << 10):
        flag = 1
        for eff in coeff:
            res = 0
            for j in range(10):
                if i & (1 << (9 - j)):
                    res += eff[j]
            if res < eff[10]:
                flag = 0
                break
        if flag:
            # print(i)
            tmp = i
            k = tmp % 4
            tmp >>= 2
            y = tmp % (1 << 4)
            tmp >>= 4
            x = tmp
            assert k == 0 or k == 1 or k == 2
            if k == 0:
                diff[x][y] = 16
            elif k == 1:
                diff[x][y] = 4
            else:
                diff[x][y] = 2
    assert (ddt == diff).all() == True
    print("The sage output is right.")

    Q = coeff.copy()
    P = []
    for i in range(1 << 10):
        tmp = []
        for j in range(10):
            if i & (1 << j):
                tmp.append(1)
            else:
                tmp.append(0)
        for q in Q:
            if check(tmp, q) == 0:
                P.append(tmp)
                break

    print("Number of points that should be filtered: %d." % len(P))
    print("Number of inequalities: %d." % len(Q))
    choose = [0] * len(Q)
    ans = 0
    while len(P):
        cnt = [0] * len(Q)
        mx = 0
        for idx, q in enumerate(Q):
            if choose[idx]:
                continue
            for p in P:
                if check(p, q) == 0:
                    cnt[idx] += 1
            mx = max(mx, cnt[idx])
        # print(cnt)
        for idx, q in enumerate(Q):
            if mx == cnt[idx]:
                ans += 1
                choose[idx] = 1
                for p in P[:]:
                    if check(p, q) == 0:
                        P.remove(p)
                print(
                    "index of chosen inequality: {}  efficient: {}  elements filtered: {}  elements left: {}.".format(
                        idx, q, mx, len(P)
                    )
                )
                break
    print("Total number: %d." % ans)
    Output_to_file(choose)
