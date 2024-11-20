from Search import *

ans = 0
lst = []

if __name__ == "__main__":
    for i in range(2, 6):
        for p in range(1, 7):
            for j in range(2, 6):
                print("================(", i, p, j, ")================")
                comp = Wordwise_solver(i, p, j)
                if comp < 128:
                    if i + p + j > ans:
                        ans = i + p + j
                        lst.clear()
                        lst.append((i, p, j, comp))
                    elif i + p + j == ans:
                        lst.append((i, p, j, comp))

    print(ans)
    print(lst)
