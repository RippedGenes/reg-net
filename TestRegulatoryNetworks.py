from RegulatoryNetworks import Solve, EvaluateExpression

def PrettyPrint(list_of_solutions):
    for solution in list_of_solutions:
        print solution


def RunTests():
    print("Running tests")
    PrettyPrint(Solve(3, [[(0,0,0)],[(0,1,0),(1,0,0)]]))


def main():
    RunTests()

if __name__ == '__main__':
    main()
