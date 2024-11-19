import random

num_rounds = 31
con = []
S = [0xE, 0x4, 0xB, 0x2, 0x3, 0x8, 0x0, 0x9, 0x1, 0xA, 0x7, 0xF, 0x6, 0xC, 0x5, 0xD]


def get_random_hex(len):
    num = random.randrange(0, 16**len)
    hex_str = hex(num)[2:]
    hex_str = hex_str.zfill(len)
    return hex_str


def lhalf(x, b=8):
    return x >> b


def rhalf(x, b=8):
    return x % (1 << b)


def cat(x, y, b=8):
    return (x << b) | y


def get_const_seq():
    for i in range(num_rounds):
        stream = 0x6547A98B ^ cat(
            cat(cat(cat(cat(cat(i + 1, 0, 5), i + 1, 5), 0, 2), i + 1, 5), 0, 5),
            i + 1,
            5,
        )
        con.append(lhalf(stream, 16))
        con.append(rhalf(stream, 16))
    # print(len(con))


def F(x):
    l, r = lhalf(x), rhalf(x)
    t = [lhalf(l, 4), rhalf(l, 4), lhalf(r, 4), rhalf(r, 4)]
    for i in range(4):
        t[i] = S[t[i]]
    z = []
    z.append(mul(2, t[0]) ^ mul(3, t[1]) ^ t[2] ^ t[3])
    z.append(mul(2, t[1]) ^ mul(3, t[2]) ^ t[0] ^ t[3])
    z.append(mul(2, t[2]) ^ mul(3, t[3]) ^ t[0] ^ t[1])
    z.append(mul(2, t[3]) ^ mul(3, t[0]) ^ t[1] ^ t[2])
    for i in range(4):
        z[i] = S[z[i]]
    return cat(cat(z[0], z[1], 4), cat(z[2], z[3], 4), 8)


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


def RP(x0, x1, x2, x3):
    return (
        cat(lhalf(x1), rhalf(x3)),
        cat(lhalf(x2), rhalf(x0)),
        cat(lhalf(x3), rhalf(x1)),
        cat(lhalf(x0), rhalf(x2)),
    )


def revRP(x0, x1, x2, x3):
    return (
        cat(lhalf(x3), rhalf(x1)),
        cat(lhalf(x0), rhalf(x2)),
        cat(lhalf(x1), rhalf(x3)),
        cat(lhalf(x2), rhalf(x0)),
    )


class Piccolo:
    def __init__(self, master_key=None):
        assert master_key != None
        self.begin_round = 0
        self.end_round = num_rounds
        self.init_key(master_key)

    def init_key(self, master_key):
        assert 0 <= master_key < (1 << 128)
        k = []
        for i in range(8):
            k.append(master_key % (1 << 16))
            master_key >>= 16
        k.reverse()
        # for i in range(8):
        #     print(hex(k[i]))
        self.wk = []
        self.wk.append(cat(lhalf(k[0]), rhalf(k[1])))
        self.wk.append(cat(lhalf(k[1]), rhalf(k[0])))
        self.wk.append(cat(lhalf(k[4]), rhalf(k[7])))
        self.wk.append(cat(lhalf(k[7]), rhalf(k[4])))
        # for i in range(4):
        #     print(hex(self.wk[i]))
        self.rk = []
        for i in range(num_rounds << 1):
            if (i + 2) % 8 == 0:
                k[0], k[1], k[2], k[3], k[4], k[5], k[6], k[7] = (
                    k[2],
                    k[1],
                    k[6],
                    k[7],
                    k[0],
                    k[3],
                    k[4],
                    k[5],
                )
                # print(i)
                # for i in range(8):
                #     print(hex(k[i]))
            self.rk.append(k[(i + 2) % 8] ^ con[i])
            # print(hex(con[i]))
        # print(len(self.rk))

    def encrypt(self, plaintext):
        assert 0 <= plaintext < (1 << 64)
        l, r = lhalf(plaintext, 32), rhalf(plaintext, 32)
        x0, x1, x2, x3 = lhalf(l, 16), rhalf(l, 16), lhalf(r, 16), rhalf(r, 16)
        # print(hex(x0), hex(x1), hex(x2), hex(x3))
        if self.begin_round == 0:
            x0 ^= self.wk[0]
            x2 ^= self.wk[1]
        for i in range(self.begin_round, self.end_round - 1):
            x1 ^= F(x0) ^ self.rk[i << 1]
            x3 ^= F(x2) ^ self.rk[(i << 1) | 1]
            x0, x1, x2, x3 = RP(x0, x1, x2, x3)
        if self.end_round == num_rounds:
            x1 ^= F(x0) ^ self.rk[60]
            x3 ^= F(x2) ^ self.rk[61]
            x0 ^= self.wk[2]
            x2 ^= self.wk[3]
        else:
            idx = self.end_round - 1
            x1 ^= F(x0) ^ self.rk[idx << 1]
            x3 ^= F(x2) ^ self.rk[(idx << 1) | 1]
            x0, x1, x2, x3 = RP(x0, x1, x2, x3)
        ciphertext = cat(cat(x0, x1, 16), cat(x2, x3, 16), 32)
        assert 0 <= ciphertext < (1 << 64)
        return ciphertext

    def decrypt(self, ciphertext):
        assert 0 <= ciphertext < (1 << 64)
        l, r = lhalf(ciphertext, 32), rhalf(ciphertext, 32)
        x0, x1, x2, x3 = lhalf(l, 16), rhalf(l, 16), lhalf(r, 16), rhalf(r, 16)
        # print(hex(x0), hex(x1), hex(x2), hex(x3))
        if self.end_round == num_rounds:
            x0 ^= self.wk[2]
            x2 ^= self.wk[3]
            x1 ^= F(x0) ^ self.rk[60]
            x3 ^= F(x2) ^ self.rk[61]
        else:
            x0, x1, x2, x3 = revRP(x0, x1, x2, x3)
            idx = self.end_round - 1
            x1 ^= F(x0) ^ self.rk[idx << 1]
            x3 ^= F(x2) ^ self.rk[(idx << 1) | 1]
        for i in range(self.end_round - 2, self.begin_round - 1, -1):
            x0, x1, x2, x3 = revRP(x0, x1, x2, x3)
            x1 ^= F(x0) ^ self.rk[i << 1]
            x3 ^= F(x2) ^ self.rk[(i << 1) | 1]
        if self.begin_round == 0:
            x0 ^= self.wk[0]
            x2 ^= self.wk[1]
        plaintext = cat(cat(x0, x1, 16), cat(x2, x3, 16), 32)
        assert 0 <= plaintext < (1 << 64)
        return plaintext


def test_linear_key(test_str, r, delta, br):
    er = br + r
    # print(br, er - 1)
    count = 0
    rsk = []
    print("delta =", hex(delta))
    for i in range(br, er):
        rsk.append([])
        for j in range(32):
            for tries in range(1000):
                z = int(get_random_hex(16), 16)
                k = int(get_random_hex(32), 16)
                # print(hex(z), hex(k))

                Piccolo1 = Piccolo(k)
                Piccolo1.begin_round = br
                Piccolo1.end_round = er

                Piccolo2 = Piccolo(k)
                Piccolo2.begin_round = br
                Piccolo2.end_round = er
                if j < 16:
                    Piccolo2.rk[i << 1] ^= 1 << (15 - j)
                else:
                    Piccolo2.rk[(i << 1) | 1] ^= 1 << (31 - j)

                if test_str == "input":
                    y1 = Piccolo1.encrypt(z)
                    y1 ^= delta
                    x1 = Piccolo1.decrypt(y1)
                    y2 = Piccolo2.encrypt(z)
                    y2 ^= delta
                    x2 = Piccolo2.decrypt(y2)
                elif test_str == "output":
                    y1 = Piccolo1.decrypt(z)
                    y1 ^= delta
                    x1 = Piccolo1.encrypt(y1)
                    y2 = Piccolo2.decrypt(z)
                    y2 ^= delta
                    x2 = Piccolo2.encrypt(y2)

                if x1 != x2:
                    count += 1
                    rsk[i - br].append(j)
                    break

    if test_str == "input":
        temp_str = "kin"
    else:
        temp_str = "kout"
    print(temp_str, ":")
    print("count =", count)
    for i in range(br, er):
        print("Round", i, ":", rsk[i - br])
    return count, rsk


if __name__ == "__main__":
    get_const_seq()
    my_piccolo = Piccolo(0x00112233445566778899AABBCCDDEEFF)
    ciphertxt = my_piccolo.encrypt(0x0123456789ABCDEF)
    if ciphertxt == 0x5EC42CEA657B89FF:
        print("Encrypt Passed.")
    if my_piccolo.decrypt(ciphertxt) == 0x0123456789ABCDEF:
        print("Decrypt Passed.")
    test_linear_key("input", 4, 0xDA812700000000C2, 0)
    test_linear_key("output", 4, 0x22C200810000DA00, 9)
