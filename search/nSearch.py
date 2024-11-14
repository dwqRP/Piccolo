from gurobipy import *
from Bitwise_MILP import *
import time
import sys

Min_sbox = [
    0,
]

if __name__ == "__main__":
    start_time = last_time = time.time()
    p_rounds = 5
    in_rounds = 4
    out_rounds = 4
    Piccolo = Model("Piccolo")
    state_p = {}
    linear = {}
    dummy = {}
    xor = {}
    state_in = {}
    rk_in = {}
    state_out = {}
    rk_out = {}
    # active_words = Piccolo.addVar(vtype=GRB.INTEGER, name="active_words")
    sbox = LinExpr()
    obj_in = LinExpr()
    obj_out = LinExpr()
    obj = Piccolo.addVar(vtype=GRB.INTEGER, name="obj")

    # distinguisher
    state_p[0] = Piccolo.addVars(16, vtype=GRB.BINARY, name="state_p0")
    for rd in range(p_rounds):
        linear[rd] = Piccolo.addVars(8, vtype=GRB.BINARY, name="linear" + str(rd))
        dummy[rd] = Piccolo.addVars(10, vtype=GRB.BINARY, name="dummy" + str(rd))
        xor[rd] = Piccolo.addVars(8, vtype=GRB.BINARY, name="xor" + str(rd))
        state_p[rd + 1] = Piccolo.addVars(
            16, vtype=GRB.BINARY, name="state_p" + str(rd + 1)
        )
        Piccolo.update()
        Piccolo.addConstrs(dummy[rd][0] >= linear[rd][i] for i in range(4))
        Piccolo.addConstrs(dummy[rd][0] >= state_p[rd][i] for i in range(4))
        expr1 = quicksum(state_p[rd][i] for i in range(4))
        expr1.add(quicksum(linear[rd][i] for i in range(4)))
        Piccolo.addConstr(expr1 >= 5 * dummy[rd][0])

        Piccolo.addConstrs(dummy[rd][1] >= linear[rd][i] for i in range(4, 8))
        Piccolo.addConstrs(dummy[rd][1] >= state_p[rd][i] for i in range(8, 12))
        expr2 = quicksum(state_p[rd][i] for i in range(8, 12))
        expr2.add(quicksum(linear[rd][i] for i in range(4, 8)))
        Piccolo.addConstr(expr2 >= 5 * dummy[rd][1])

        for i in range(4):
            Piccolo.addConstr(dummy[rd][i + 2] >= xor[rd][i])
            Piccolo.addConstr(dummy[rd][i + 2] >= linear[rd][i])
            Piccolo.addConstr(dummy[rd][i + 2] >= state_p[rd][i + 4])
            Piccolo.addConstr(
                linear[rd][i] + state_p[rd][i + 4] + xor[rd][i] >= 2 * dummy[rd][i + 2]
            )

            Piccolo.addConstr(dummy[rd][i + 6] >= xor[rd][i + 4])
            Piccolo.addConstr(dummy[rd][i + 6] >= linear[rd][i + 4])
            Piccolo.addConstr(dummy[rd][i + 6] >= state_p[rd][i + 12])
            Piccolo.addConstr(
                linear[rd][i + 4] + state_p[rd][i + 12] + xor[rd][i + 4]
                >= 2 * dummy[rd][i + 6]
            )

        Piccolo.addConstr(state_p[rd + 1][0] == xor[rd][0])
        Piccolo.addConstr(state_p[rd + 1][1] == xor[rd][1])
        Piccolo.addConstr(state_p[rd + 1][2] == xor[rd][6])
        Piccolo.addConstr(state_p[rd + 1][3] == xor[rd][7])
        Piccolo.addConstr(state_p[rd + 1][4] == state_p[rd][8])
        Piccolo.addConstr(state_p[rd + 1][5] == state_p[rd][9])
        Piccolo.addConstr(state_p[rd + 1][6] == state_p[rd][2])
        Piccolo.addConstr(state_p[rd + 1][7] == state_p[rd][3])
        Piccolo.addConstr(state_p[rd + 1][8] == xor[rd][4])
        Piccolo.addConstr(state_p[rd + 1][9] == xor[rd][5])
        Piccolo.addConstr(state_p[rd + 1][10] == xor[rd][2])
        Piccolo.addConstr(state_p[rd + 1][11] == xor[rd][3])
        Piccolo.addConstr(state_p[rd + 1][12] == state_p[rd][0])
        Piccolo.addConstr(state_p[rd + 1][13] == state_p[rd][1])
        Piccolo.addConstr(state_p[rd + 1][14] == state_p[rd][10])
        Piccolo.addConstr(state_p[rd + 1][15] == state_p[rd][11])

        for i in range(4):
            sbox.add(state_p[rd][i])
            sbox.add(state_p[rd][i + 8])
            sbox.add(linear[rd][i])
            sbox.add(linear[rd][i + 4])

    # active_words = quicksum(state_p[0][i] for i in range(16)) + quicksum(
    #     state_p[p_rounds][i] for i in range(16)
    # )
    Piccolo.addConstr(sbox >= 1)
    Piccolo.addConstr(sbox <= 32)

    # kin
    state_in[in_rounds - 1] = Piccolo.addVars(
        8, vtype=GRB.BINARY, name="state_in" + str(in_rounds - 1)
    )
    Piccolo.update()
    for i in range(8):
        Piccolo.addConstr(state_in[in_rounds - 1][i] >= state_p[0][i << 1])
        Piccolo.addConstr(state_in[in_rounds - 1][i] >= state_p[0][i << 1 | 1])
    for rin in range(in_rounds - 1, 0, -1):
        # print(rin)
        state_in[rin - 1] = Piccolo.addVars(
            8, vtype=GRB.BINARY, name="state_in" + str(rin - 1)
        )
        rk_in[rin - 1] = Piccolo.addVars(
            4, vtype=GRB.BINARY, name="rk_in" + str(rin - 1)
        )
        Piccolo.update()
        Piccolo.addConstr(state_in[rin - 1][0] == state_in[rin][6])
        Piccolo.addConstr(state_in[rin - 1][1] == state_in[rin][3])
        Piccolo.addConstr(state_in[rin - 1][4] == state_in[rin][2])
        Piccolo.addConstr(state_in[rin - 1][5] == state_in[rin][7])

        Piccolo.addConstr(state_in[rin - 1][2] >= state_in[rin][0])
        Piccolo.addConstr(state_in[rin - 1][2] >= state_in[rin - 1][0])
        Piccolo.addConstr(state_in[rin - 1][2] >= state_in[rin - 1][1])
        Piccolo.addConstr(state_in[rin - 1][3] >= state_in[rin][5])
        Piccolo.addConstr(state_in[rin - 1][3] >= state_in[rin - 1][0])
        Piccolo.addConstr(state_in[rin - 1][3] >= state_in[rin - 1][1])

        Piccolo.addConstr(state_in[rin - 1][6] >= state_in[rin][4])
        Piccolo.addConstr(state_in[rin - 1][6] >= state_in[rin - 1][4])
        Piccolo.addConstr(state_in[rin - 1][6] >= state_in[rin - 1][5])
        Piccolo.addConstr(state_in[rin - 1][7] >= state_in[rin][1])
        Piccolo.addConstr(state_in[rin - 1][7] >= state_in[rin - 1][4])
        Piccolo.addConstr(state_in[rin - 1][7] >= state_in[rin - 1][5])

        Piccolo.addConstr(rk_in[rin - 1][0] >= state_in[rin - 1][0])
        Piccolo.addConstr(rk_in[rin - 1][0] >= state_in[rin - 1][1])
        Piccolo.addConstr(rk_in[rin - 1][1] >= state_in[rin - 1][4])
        Piccolo.addConstr(rk_in[rin - 1][1] >= state_in[rin - 1][5])
        Piccolo.addConstr(rk_in[rin - 1][2] >= state_in[rin - 1][4])
        Piccolo.addConstr(rk_in[rin - 1][2] >= state_in[rin - 1][5])
        Piccolo.addConstr(rk_in[rin - 1][3] >= state_in[rin - 1][0])
        Piccolo.addConstr(rk_in[rin - 1][3] >= state_in[rin - 1][1])
        for i in range(4):
            obj_in.add(8 * rk_in[rin - 1][i])
            
    # kout
    state_out[0] = Piccolo.addVars(8, vtype=GRB.BINARY, name="state_out0")
    Piccolo.update()
    for i in range(8):
        Piccolo.addConstr(state_out[0][i] >= state_p[p_rounds][i << 1])
        Piccolo.addConstr(state_out[0][i] >= state_p[p_rounds][i << 1 | 1])
    for rout in range(out_rounds - 1):
        # print(rin)
        state_out[rout + 1] = Piccolo.addVars(
            8, vtype=GRB.BINARY, name="state_out" + str(rout + 1)
        )
        rk_out[rout + 1] = Piccolo.addVars(
            4, vtype=GRB.BINARY, name="rk_out" + str(rout + 1)
        )
        Piccolo.update()
        Piccolo.addConstr(state_out[rout + 1][2] == state_out[rout][4])
        Piccolo.addConstr(state_out[rout + 1][3] == state_out[rout][1])
        Piccolo.addConstr(state_out[rout + 1][6] == state_out[rout][0])
        Piccolo.addConstr(state_out[rout + 1][7] == state_out[rout][5])

        Piccolo.addConstr(state_out[rout + 1][0] >= state_out[rout][2])
        Piccolo.addConstr(state_out[rout + 1][0] >= state_out[rout + 1][6])
        Piccolo.addConstr(state_out[rout + 1][0] >= state_out[rout + 1][3])
        Piccolo.addConstr(state_out[rout + 1][5] >= state_out[rout][3])
        Piccolo.addConstr(state_out[rout + 1][5] >= state_out[rout + 1][6])
        Piccolo.addConstr(state_out[rout + 1][5] >= state_out[rout + 1][3])
        
        Piccolo.addConstr(state_out[rout + 1][1] >= state_out[rout][7])
        Piccolo.addConstr(state_out[rout + 1][1] >= state_out[rout + 1][2])
        Piccolo.addConstr(state_out[rout + 1][1] >= state_out[rout + 1][7])
        Piccolo.addConstr(state_out[rout + 1][4] >= state_out[rout][6])
        Piccolo.addConstr(state_out[rout + 1][4] >= state_out[rout + 1][2])
        Piccolo.addConstr(state_out[rout + 1][4] >= state_out[rout + 1][7])

        Piccolo.addConstr(rk_out[rout + 1][0] >= state_out[rout][4])
        Piccolo.addConstr(rk_out[rout + 1][0] >= state_out[rout][5])
        Piccolo.addConstr(rk_out[rout + 1][1] >= state_out[rout][0])
        Piccolo.addConstr(rk_out[rout + 1][1] >= state_out[rout][1])
        Piccolo.addConstr(rk_out[rout + 1][2] >= state_out[rout][0])
        Piccolo.addConstr(rk_out[rout + 1][2] >= state_out[rout][1])
        Piccolo.addConstr(rk_out[rout + 1][3] >= state_out[rout][4])
        Piccolo.addConstr(rk_out[rout + 1][3] >= state_out[rout][5])
        
        for i in range(4):
            obj_out.add(8 * rk_out[rout + 1][i])

    obj_in.add(2 * sbox)
    obj_out.add(2 * sbox)
    Piccolo.addConstr(obj >= obj_in)
    Piccolo.addConstr(obj >= obj_out)
    # Piccolo.setParam("OutputFlag", 0)
    Piccolo.setObjective(obj, GRB.MINIMIZE)
    Piccolo.Params.PoolSearchMode = 2
    Piccolo.Params.PoolSolutions = 1
    Piccolo.Params.PoolGap = 0.0
    Piccolo.optimize()
    print("Model Status:", Piccolo.Status)
    if Piccolo.Status == 2:
        print("SolCount: ", Piccolo.SolCount)
        print("Minimum Obj: %g" % Piccolo.ObjVal)
        # best_prob = 1000

        for k in range(Piccolo.SolCount):
            Piccolo.Params.SolutionNumber = k
            for v in Piccolo.getVars():
                if v.VarName.find("rk_in") != -1:
                    if abs(v.Xn) > 1e-10:
                        print(v.VarName, "=", v.Xn)
                if v.VarName.find("rk_out") != -1:
                    if abs(v.Xn) > 1e-10:
                        print(v.VarName, "=", v.Xn)
                if v.VarName.find("state_p") != -1:
                    print(v.VarName, "=", v.Xn)
                if v.VarName.find("state_in") != -1:
                    print(v.VarName, "=", v.Xn)
        #     temp_time = time.time()
        #     if temp_time - last_time > 5:
        #         last_time = temp_time
        #         print(
        #             "Solved {:.2f}%    Time: {}s".format(
        #                 100 * k / Piccolo.SolCount, round(temp_time - start_time)
        #             )
        #         )
            sys.stdout = open("wordwise_constraints.txt", "w")
            for v in Piccolo.getVars():
                if v.VarName.find("state_p") != -1:
                    print(v.VarName, "=", v.Xn)
                if v.VarName.find("linear") != -1:
                    print(v.VarName, "=", v.Xn)
                # print(v.VarName, v.Xn)
            sys.stdout = sys.__stdout__
            temp_prob = Bitwise_solver(p_rounds, 1000, Piccolo.ObjVal)
        #     # print(temp_prob)
        #     if temp_prob == -1:
        #         continue
        #     if temp_prob < best_prob:
        #         best_prob = temp_prob

        # sys.stdout = sys.__stdout__
        # print("Maximum Probability:", best_prob)
