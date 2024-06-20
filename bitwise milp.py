from gurobipy import *

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

RP = [
    16,
    17,
    18,
    19,
    20,
    21,
    22,
    23,
    56,
    57,
    58,
    59,
    60,
    61,
    62,
    63,
    32,
    33,
    34,
    35,
    36,
    37,
    38,
    39,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    48,
    49,
    50,
    51,
    52,
    53,
    54,
    55,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    47,
]


def process_sage_output():
    coeff = []
    with open("Convex hull of S box with prob.txt", "r") as f:
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
    # print(len(coeff))
    # print(coeff)
    return coeff


if __name__ == "__main__":
    coeff = process_sage_output()

    num_rounds = 6
    Piccolo = Model("Piccolo")
    state = {}
    beforeM = {}
    Sprobx = {}
    Sproby = {}
    afterM = {}
    Fout = {}
    beforeRP = {}
    state[0] = Piccolo.addVars(64, vtype=GRB.BINARY, name="state0")
    expr = LinExpr()
    for rd in range(num_rounds):
        beforeM[rd] = Piccolo.addVars(32, vtype=GRB.BINARY, name="beforeM" + str(rd))
        # beforeM means output of bits[0 to 15] and bits[32 to 47] after S boxes
        Sprobx[rd] = Piccolo.addVars(16, vtype=GRB.BINARY, name="Sprobx" + str(rd))
        Sproby[rd] = Piccolo.addVars(16, vtype=GRB.BINARY, name="Sproby" + str(rd))
        # Sprob means the probability of each S box
        # two bits to represent 3 kind of probability => 00 for 2^0; 01 for 2^{-2}; 10 for 2^{-3}
        afterM[rd] = Piccolo.addVars(32, vtype=GRB.BINARY, name="afterM" + str(rd))
        # afterM means output of bits[0 to 15] and bits[32 to 47] after Mixcolumn
        Fout[rd] = Piccolo.addVars(32, vtype=GRB.BINARY, name="Fout" + str(rd))
        # Fout means output of bits[0 to 15] and bits[32 to 47] after the whole F function
        beforeRP[rd] = Piccolo.addVars(64, vtype=GRB.BINARY, name="beforeRP" + str(rd))
        # beforeRP means input of bits[0 to 63] before round permutation
        state[rd + 1] = Piccolo.addVars(
            64, vtype=GRB.BINARY, name="state" + str(rd + 1)
        )
        # state means the internal states at the beginning of each round
        Piccolo.update()
        for i in range(4):
            for eff in coeff:
                temp = LinExpr()
                for j in range(4):
                    if eff[j] != 0:
                        temp.add(eff[j] * state[rd][4 * i + j])
                for j in range(4):
                    if eff[4 + j] != 0:
                        temp.add(eff[4 + j] * beforeM[rd][4 * i + j])
                if eff[8] != 0:
                    temp.add(eff[8] * Sprobx[rd][i])
                if eff[9] != 0:
                    temp.add(eff[9] * Sproby[rd][i])
                Piccolo.addConstr(temp >= eff[10])
        for i in range(4):
            for eff in coeff:
                temp = LinExpr()
                for j in range(4):
                    if eff[j] != 0:
                        temp.add(eff[j] * state[rd][32 + 4 * i + j])
                for j in range(4):
                    if eff[4 + j] != 0:
                        temp.add(eff[4 + j] * beforeM[rd][16 + 4 * i + j])
                if eff[8] != 0:
                    temp.add(eff[8] * Sprobx[rd][i + 4])
                if eff[9] != 0:
                    temp.add(eff[9] * Sproby[rd][i + 4])
                Piccolo.addConstr(temp >= eff[10])
        for i in range(16):
            temp = LinExpr()
            for j in range(16):
                if M[i][j]:
                    temp.add(beforeM[rd][j])
            Piccolo.addConstr(afterM[rd][i] == temp)
        for i in range(16):
            temp = LinExpr()
            for j in range(16):
                if M[i][j]:
                    temp.add(beforeM[rd][j + 16])
            Piccolo.addConstr(afterM[rd][i + 16] == temp)
        for i in range(4):
            for eff in coeff:
                temp = LinExpr()
                for j in range(4):
                    if eff[j] != 0:
                        temp.add(eff[j] * afterM[rd][4 * i + j])
                for j in range(4):
                    if eff[4 + j] != 0:
                        temp.add(eff[4 + j] * Fout[rd][4 * i + j])
                if eff[8] != 0:
                    temp.add(eff[8] * Sprobx[rd][i + 8])
                if eff[9] != 0:
                    temp.add(eff[9] * Sproby[rd][i + 8])
                Piccolo.addConstr(temp >= eff[10])
        for i in range(4):
            for eff in coeff:
                temp = LinExpr()
                for j in range(4):
                    if eff[j] != 0:
                        temp.add(eff[j] * afterM[rd][16 + 4 * i + j])
                for j in range(4):
                    if eff[4 + j] != 0:
                        temp.add(eff[4 + j] * Fout[rd][16 + 4 * i + j])
                if eff[8] != 0:
                    temp.add(eff[8] * Sprobx[rd][i + 12])
                if eff[9] != 0:
                    temp.add(eff[9] * Sproby[rd][i + 12])
                Piccolo.addConstr(temp >= eff[10])
        Piccolo.addConstrs(beforeRP[rd][i] == state[rd][i] for i in range(16))
        Piccolo.addConstrs(beforeRP[rd][i] == state[rd][i] for i in range(32, 48))
        Piccolo.addConstrs(
            beforeRP[rd][i] == state[rd][i] + Fout[rd][i - 16] for i in range(16, 32)
        )
        Piccolo.addConstrs(
            beforeRP[rd][i] == state[rd][i] + Fout[rd][i - 32] for i in range(48, 64)
        )
        Piccolo.addConstrs(state[rd + 1][i] == beforeRP[rd][RP[i]] for i in range(64))
        for i in range(16):
            expr.add(2 * Sproby[rd][i])
            expr.add(3 * Sprobx[rd][i])

    Piccolo.setObjective(expr, GRB.MINIMIZE)
    Piccolo.addConstr(expr >= 1)
    Piccolo.optimize()
    # for v in Piccolo.getVars():
    #     if v.VarName.find("Sprob") != -1:
    #         print(v.VarName, v.X)
    # print("Obj: %g" % Piccolo.objVal)
