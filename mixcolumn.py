M = [
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1],
]


def init():
    for i in range(4, 16):
        row = [0] * 16
        for j in range(16):
            if M[i - 4][j] == 1:
                row[(j + 4) % 16] = 1
        M.append(row)
    print(M)


def mul(x, y):
    ans = 0
    p = 0b10011
    for i in range(4):
        if x & (1 << i):
            ans ^= y << i
    for i in range(7, 3, -1):
        if ans & (1 << i):
            ans ^= p << (i - 4)
    return ans


def dot(z):
    res = 0
    for i in range(12, 16):
        tmp = 0
        for j in range(16):
            tmp ^= M[i][j] & z[j]
        res |= tmp << (15 - i)
    return res


if __name__ == "__main__":
    init()
    for i in range(1 << 16):
        t = []
        tmp = i
        for j in range(4):
            t.append(tmp % (1 << 4))
            tmp >>= 4
        t.reverse()
        # ans1 = mul(2, t[0]) ^ mul(3, t[1]) ^ t[2] ^ t[3]
        # ans1 = mul(2, t[1]) ^ mul(3, t[2]) ^ t[0] ^ t[3]
        # ans1 = mul(2, t[2]) ^ mul(3, t[3]) ^ t[0] ^ t[1]
        ans1 = mul(2, t[3]) ^ mul(3, t[0]) ^ t[2] ^ t[1]
        z = []
        for j in range(15, -1, -1):
            if (i & (1 << j)) == 0:
                z.append(0)
            else:
                z.append(1)
        ans2 = dot(z)
        if ans1 != ans2:
            print(i, ans1, ans2)
            print(z)
            break
