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


coeff = []


def check(p):
    for eff in coeff:
        res = 0
        for j in range(10):
            if p & (1 << (9 - j)):
                res += eff[j]
        if res < eff[10]:
            return 0
    return 1


if __name__ == "__main__":
    with open("./log/Convex hull of S box with prob after selected.txt", "r") as f:
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

    ddt = init_DDT()
    diff = np.zeros([16, 16], int)
    # print(diff)
    for i in range(1 << 10):
        if check(i):
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
    state = 0xA5
    state = (state << 2) | (0b01)
    print(check(state))
