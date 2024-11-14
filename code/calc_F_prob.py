mod = 19

S = [0xe, 0x4, 0xb, 0x2, 0x3, 0x8, 0x0, 0x9, 0x1, 0xa, 0x7, 0xf, 0x6, 0xc, 0x5, 0xd]

def mul(a, b):
    ans = 0
    for i in range(4):
        if a & (1 << i):
            ans ^= (b << i)
    for i in range(7, 3, -1):
        if ans & (1 << i):
            ans ^= (mod << (i - 4))
    return ans

def F(input_val):
    tmp = [0] * 4
    res = [0] * 4
    out = 0

    # Extract 4 nibbles from input_val
    for i in range(4):
        tmp[i] = input_val % 16
        input_val >>= 4

    # Swap tmp values
    tmp[0], tmp[3] = tmp[3], tmp[0]
    tmp[1], tmp[2] = tmp[2], tmp[1]

    # Apply S-box substitution
    for i in range(4):
        tmp[i] = S[tmp[i]]

    # Calculate res values
    res[0] = mul(2, tmp[0]) ^ mul(3, tmp[1]) ^ tmp[2] ^ tmp[3]
    res[1] = mul(2, tmp[1]) ^ mul(3, tmp[2]) ^ tmp[0] ^ tmp[3]
    res[2] = mul(2, tmp[2]) ^ mul(3, tmp[3]) ^ tmp[0] ^ tmp[1]
    res[3] = mul(2, tmp[3]) ^ mul(3, tmp[0]) ^ tmp[1] ^ tmp[2]

    # Apply S-box to res and construct the output
    for i in range(4):
        res[i] = S[res[i]]
        out = (out << 4) | res[i]

    return out

def main():
    din = 0x1102
    dout = 0x9800
    ans = 0
    mx = (1 << 16)

    for i in range(mx):
        delta = F(i) ^ F(i ^ din)
        if delta == dout:
            ans += 1

    print(f"{ans}/{mx}={ans / mx:.6f}")

if __name__ == "__main__":
    main()