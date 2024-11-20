from gurobipy import *
import sys

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
    with open("./ineqs.txt", "r") as f:
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


def Bitwise_solver(num_rounds, best_prob, min_sbox=1):
    assert num_rounds >= 1

    state[0] = Piccolo.addVars(64, vtype=GRB.BINARY, name="state0")
    # state means the difference of internal states at the beginning of each round
    Piccolo.update()
    Piccolo.addConstr(quicksum(state[0][i] for i in range(64)) >= 1)
    # input difference not all zeros

    obj = LinExpr()
    # objective function

    for rd in range(num_rounds):
        beforeM[rd] = Piccolo.addVars(32, vtype=GRB.BINARY, name="beforeM" + str(rd))
        # beforeM means output of bits[0 to 15] and bits[32 to 47] after S boxes
        Sprobx[rd] = Piccolo.addVars(16, vtype=GRB.BINARY, name="Sprobx" + str(rd))
        Sproby[rd] = Piccolo.addVars(16, vtype=GRB.BINARY, name="Sproby" + str(rd))
        # Sprob means the probability of each S box
        # two bits to represent 3 kind of probability => 00 for 2^0; 01 for 2^{-2}; 10 for 2^{-3}
        afterM[rd] = Piccolo.addVars(32, vtype=GRB.BINARY, name="afterM" + str(rd))
        dummy[rd] = Piccolo.addVars(32, vtype=GRB.INTEGER, name="dummy" + str(rd))
        # afterM means output of bits[0 to 15] and bits[32 to 47] after Mixcolumn
        # dummy are dummy variables to deal with XOR
        Fout[rd] = Piccolo.addVars(32, vtype=GRB.BINARY, name="Fout" + str(rd))
        # Fout means output of bits[0 to 15] and bits[32 to 47] after the whole F function
        beforeRP[rd] = Piccolo.addVars(64, vtype=GRB.BINARY, name="beforeRP" + str(rd))
        # beforeRP means input of bits[0 to 63] before the round permutation
        state[rd + 1] = Piccolo.addVars(
            64, vtype=GRB.BINARY, name="state" + str(rd + 1)
        )
        Piccolo.update()

        # Modeling S-box[0 to 7]
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

        # Modeling MixColumn (Sum of bitwise XOR)
        for i in range(16):
            temp = LinExpr()
            for j in range(16):
                if M[i][j]:
                    temp.add(beforeM[rd][j])
            Piccolo.addConstr(temp == 2 * dummy[rd][i] + afterM[rd][i])
        for i in range(16):
            temp = LinExpr()
            for j in range(16):
                if M[i][j]:
                    temp.add(beforeM[rd][j + 16])
            Piccolo.addConstr(temp == 2 * dummy[rd][i + 16] + afterM[rd][i + 16])

        # Modeling S-box[8 to 15]
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

        # Modeling XOR
        Piccolo.addConstrs(
            beforeRP[rd][i] + state[rd][i] + Fout[rd][i - 16] <= 2
            for i in range(16, 32)
        )
        Piccolo.addConstrs(
            beforeRP[rd][i] + state[rd][i] >= Fout[rd][i - 16] for i in range(16, 32)
        )
        Piccolo.addConstrs(
            beforeRP[rd][i] + Fout[rd][i - 16] >= state[rd][i] for i in range(16, 32)
        )
        Piccolo.addConstrs(
            state[rd][i] + Fout[rd][i - 16] >= beforeRP[rd][i] for i in range(16, 32)
        )
        Piccolo.addConstrs(
            beforeRP[rd][i] + state[rd][i] + Fout[rd][i - 32] <= 2
            for i in range(48, 64)
        )
        Piccolo.addConstrs(
            beforeRP[rd][i] + state[rd][i] >= Fout[rd][i - 32] for i in range(48, 64)
        )
        Piccolo.addConstrs(
            beforeRP[rd][i] + Fout[rd][i - 32] >= state[rd][i] for i in range(48, 64)
        )
        Piccolo.addConstrs(
            state[rd][i] + Fout[rd][i - 32] >= beforeRP[rd][i] for i in range(48, 64)
        )

        # Modeling round permutation
        Piccolo.addConstrs(state[rd + 1][i] == beforeRP[rd][RP[i]] for i in range(64))

        # Calc probability
        for i in range(16):
            obj.add(2 * Sproby[rd][i])
            obj.add(3 * Sprobx[rd][i])

    # Lower bound of probability
    Piccolo.addConstr(obj >= 2 * min_sbox)

    Matsui_bound_constraints(num_rounds)
    Wordwise_constraints()

    Piccolo.setObjective(obj, GRB.MINIMIZE)
    Piccolo.setParam("OutputFlag", 0)
    Piccolo.write("model.lp")
    Piccolo.optimize()
    # print("Model Status:", Piccolo.Status)
    # Piccolo.computeIIS()
    if Piccolo.Status == 2:
        ans = Piccolo.ObjVal
        if Piccolo.ObjVal <= best_prob:
            Output_trail()
        Piccolo.remove(Piccolo.getVars())
        Piccolo.remove(Piccolo.getConstrs())
        # for v in Piccolo.getVars():
        #     print(v.VarName, v.X)
        # print("Maximum Trail Prob: 2^{-%g}" % Piccolo.ObjVal)
        return ans
    else:
        Piccolo.remove(Piccolo.getVars())
        Piccolo.remove(Piccolo.getConstrs())
        return -1


def Matsui_bound_constraints(num_rounds):
    Best_prob = [0, 0, 10, 20, 31, 41, 64]
    bound_forward = LinExpr()
    bound_backward = LinExpr()
    for rd in range(num_rounds - 1):
        for i in range(16):
            bound_forward.add(2 * Sproby[rd][i])
            bound_forward.add(3 * Sprobx[rd][i])
            bound_backward.add(2 * Sproby[num_rounds - 1 - rd][i])
            bound_backward.add(3 * Sprobx[num_rounds - 1 - rd][i])
        Piccolo.addConstr(bound_forward >= Best_prob[rd + 1])
        Piccolo.addConstr(bound_backward >= Best_prob[rd + 1])


def Wordwise_constraints():
    with open("wordwise_constraints.txt") as f:
        for line in f.readlines():
            # if line.find("num_rounds") != -1:
            #     pos = line.find(":")
            #     nr = int(line[pos + 2 :])
            #     assert nr == num_rounds
            l = line.find("[")
            r = line.find("]")
            pos = line.find("=")
            idx = int(line[l + 1 : r])
            rd = int(line[l - 1 : l])
            val = float(line[pos + 2 : -1])
            assert abs(1 - val) < 1e-10 or abs(val) < 1e-10
            # print(rd, idx, val)
            if line.find("state") != -1:
                if abs(val) < 1e-10:
                    Piccolo.addConstrs(
                        state[rd][i] == 0 for i in range(4 * idx, 4 * idx + 4)
                    )
                else:
                    Piccolo.addConstr(
                        quicksum(state[rd][i] for i in range(4 * idx, 4 * idx + 4)) >= 1
                    )
            if line.find("linear") != -1:
                if abs(val) < 1e-10:
                    Piccolo.addConstrs(
                        afterM[rd][i] == 0 for i in range(4 * idx, 4 * idx + 4)
                    )
                else:
                    Piccolo.addConstr(
                        quicksum(afterM[rd][i] for i in range(4 * idx, 4 * idx + 4))
                        >= 1
                    )


def Output_trail():
    print("Differential characteristic found: Probability = 2^{-%d}" % Piccolo.ObjVal)
    rd = i = j = 0
    sti = ""
    stj = ""
    for v in Piccolo.getVars():
        if v.VarName.find("state") != -1:
            j += 1
            stj += str(int(v.X))
            if j == 16:
                j = 0
                i += 1
                sti += "{:#06X}".format(int(stj, 2))[2:] + " "
                stj = ""
                if i == 4:
                    i = 0
                    print("Round " + str(rd) + ": " + sti)
                    sti = ""
                    rd += 1


coeff = process_sage_output()
Piccolo = Model("Piccolo")
state = {}
beforeM = {}
Sprobx = {}
Sproby = {}
afterM = {}
dummy = {}
Fout = {}
beforeRP = {}


if __name__ == "__main__":
    # sys.stdout = open("./log/output.txt", "w")
    Bitwise_solver(5, 1000, 25)
    # When only the bitwise milp is running, specify the num_rounds
