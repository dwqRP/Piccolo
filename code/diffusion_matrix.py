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


if __name__ == "__main__":
    mn = 8
    for o in range(1, 1 << 16):
        t = []
        tmp = o
        for i in range(4):
            t.append(tmp % (1 << 4))
            tmp >>= 4
        t.reverse()
        z = []
        z.append(mul(2, t[0]) ^ mul(3, t[1]) ^ t[2] ^ t[3])
        z.append(mul(2, t[1]) ^ mul(3, t[2]) ^ t[0] ^ t[3])
        z.append(mul(2, t[2]) ^ mul(3, t[3]) ^ t[0] ^ t[1])
        z.append(mul(2, t[3]) ^ mul(3, t[0]) ^ t[1] ^ t[2])

        sum = 0
        for i in range(4):
            if t[i]:
                sum += 1
            if z[i]:
                sum += 1

        mn = min(mn, sum)
    print(mn)
