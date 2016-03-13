from RegulatoryNetworks import Solve, EvaluateExpression


def RunTests():
    print("Running tests")
##    print(EvaluateExpression(1, [1,0,0], [0,1,0], (-1,2)))
    Solve(2, [[(0,0), (1,0), (1,1), (0,1)]])

    # Solve()



def main():
    RunTests()

if __name__ == '__main__':
    main()
