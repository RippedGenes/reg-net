from RegulatoryNetworks import Solve, EvaluateExpression


def RunTests():
    print("Running tests")
##    print(EvaluateExpression(1, (0,0), (1,0), (-2,1)))
    Solve(3, [[(0,0,0)],[(0,1,0),(1,0,0)]])

def main():
    RunTests()

if __name__ == '__main__':
    main()
