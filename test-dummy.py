from gurobipy import *

if __name__ == "__main__":
    test = Model("test")
    x = test.addVar(vtype=GRB.INTEGER, name="x")
    y = test.addVar(vtype=GRB.INTEGER, name="y")
    test.update()
    test.addConstr(x == 2 * y + 1)
    test.addConstr(x >= -10)
    test.setObjective(x, GRB.MINIMIZE)
    test.optimize()
    print("Obj: %g" % test.objVal)
