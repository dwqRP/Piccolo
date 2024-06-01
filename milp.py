from gurobipy import *


num_rounds = 7

Piccolo = Model('Piccolo')

state = {}
linear = {}
dummy = {}
xor = {}
state[0] = Piccolo.addVars(16, vtype=GRB.BINARY, name='plaintext')
expr = LinExpr()
for rd in range(num_rounds):
    linear[rd] = Piccolo.addVars(8, vtype=GRB.BINARY, name='linear' + str(rd))
    dummy[rd] = Piccolo.addVars(10, vtype=GRB.BINARY, name='dummy' + str(rd))
    xor[rd] = Piccolo.addVars(8, vtype=GRB.BINARY, name='xor' + str(rd))
    state[rd+1] = Piccolo.addVars(16, vtype=GRB.BINARY, name='state' + str(rd+1))
    Piccolo.update()
    Piccolo.addConstrs(dummy[rd][0] >= linear[rd][i] for i in range(4))
    Piccolo.addConstrs(dummy[rd][0] >= state[rd][i] for i in range(4))
    expr1 = quicksum(state[rd][i] for i in range(4))
    expr1.add(quicksum(linear[rd][i] for i in range(4)))
    Piccolo.addConstr(expr1 >= 5 * dummy[rd][0])
    
    Piccolo.addConstrs(dummy[rd][1] >= linear[rd][i] for i in range(4,8))
    Piccolo.addConstrs(dummy[rd][1] >= state[rd][i] for i in range(8,12))
    expr2 = quicksum(state[rd][i] for i in range(8,12))
    expr2.add(quicksum(linear[rd][i] for i in range(4,8)))
    Piccolo.addConstr(expr2 >= 5 * dummy[rd][1])
    
    for i in range(4):
        Piccolo.addConstr(dummy[rd][i+2] >= xor[rd][i])
        Piccolo.addConstr(dummy[rd][i+2] >= linear[rd][i])
        Piccolo.addConstr(dummy[rd][i+2] >= state[rd][i+4])
        Piccolo.addConstr(linear[rd][i] + state[rd][i+4] + xor[rd][i] >= 2 * dummy[rd][i+2])
        
        Piccolo.addConstr(dummy[rd][i+6] >= xor[rd][i+4])
        Piccolo.addConstr(dummy[rd][i+6] >= linear[rd][i+4])
        Piccolo.addConstr(dummy[rd][i+6] >= state[rd][i+12])
        Piccolo.addConstr(linear[rd][i+4] + state[rd][i+12] + xor[rd][i+4] >= 2 * dummy[rd][i+6])
    
    Piccolo.addConstr(state[rd+1][0] == xor[rd][0])
    Piccolo.addConstr(state[rd+1][1] == xor[rd][1])
    Piccolo.addConstr(state[rd+1][2] == xor[rd][6])
    Piccolo.addConstr(state[rd+1][3] == xor[rd][7])
    Piccolo.addConstr(state[rd+1][4] == state[rd][8])
    Piccolo.addConstr(state[rd+1][5] == state[rd][9])
    Piccolo.addConstr(state[rd+1][6] == state[rd][2])
    Piccolo.addConstr(state[rd+1][7] == state[rd][3])
    Piccolo.addConstr(state[rd+1][8] == xor[rd][4])
    Piccolo.addConstr(state[rd+1][9] == xor[rd][5])
    Piccolo.addConstr(state[rd+1][10] == xor[rd][2])
    Piccolo.addConstr(state[rd+1][11] == xor[rd][3])
    Piccolo.addConstr(state[rd+1][12] == state[rd][0])
    Piccolo.addConstr(state[rd+1][13] == state[rd][1])
    Piccolo.addConstr(state[rd+1][14] == state[rd][10])
    Piccolo.addConstr(state[rd+1][15] == state[rd][11])
    
    for i in range(4):
        expr.add(state[rd][i])
        expr.add(state[rd][i+8])
        expr.add(linear[rd][i])
        expr.add(linear[rd][i+4])
    
Piccolo.setObjective(expr, GRB.MINIMIZE) 

Piccolo.addConstr(expr >= 1)

# Piccolo.setParam('OutputFlag',0)
Piccolo.optimize()
for v in Piccolo.getVars():
    print(v.VarName, v.x)
print('Obj: %g' % Piccolo.objVal)