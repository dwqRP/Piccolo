import numpy as np

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


def process_sage_output():
    coeff = []
    with open("./log/Convex hull of S box with prob.txt", "r") as f:
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


if __name__ == "__main__":
    coeff = process_sage_output()
    # print(coeff)

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
    print(diff)
