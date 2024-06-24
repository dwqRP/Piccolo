from gurobipy import *
import time

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

if __name__ == "__main__":
    start = time.time()
    test = Model("test")
    test.setParam("OutputFlag", 0)
    input = test.addVars(16, vtype=GRB.BINARY, name="input")
    output = test.addVars(16, vtype=GRB.BINARY, name="output")
    dummy = test.addVars(16, vtype=GRB.INTEGER, name="dummy")
    test.update()
    for i in range(16):
        temp = LinExpr()
        for j in range(16):
            if M[i][j]:
                temp.add(input[j])
        test.addConstr(temp == 2 * dummy[i] + output[i])
    test.setObjective(quicksum(dummy[i] for i in range(16)), GRB.MINIMIZE)
    for i in range(1 << 16):
        if i % 10000 == 0:
            print(time.time() - start, "s")
        xor_in = [0] * 16
        xor_out = [0] * 16
        for j in range(16):
            if i & (1 << j):
                test.addConstr(input[15 - j] == 1)
                xor_in[15 - j] = 1
            else:
                test.addConstr(input[15 - j] == 0)
        # test.write("test.lp")
        test.optimize()
        for j in range(16):
            for k in range(16):
                if M[j][k]:
                    xor_out[j] ^= xor_in[k]
        for v in test.getVars():
            # print(v.VarName, v.X)
            if v.VarName.find("output") != -1:
                l = v.VarName.find("[")
                r = v.VarName.find("]")
                idx = int(v.VarName[l + 1 : r])
                if v.X != xor_out[idx]:
                    print("!!!!!")

        test.remove(test.getConstrs()[16:])
