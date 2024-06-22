a = []
RP = []
st = [2, 7, 4, 1, 6, 3, 0, 5]
for i in range(64):
    a.append(i)

for i in range(8):
    for j in range(8):
        RP.append(a[st[i] * 8 + j])
print(RP)
