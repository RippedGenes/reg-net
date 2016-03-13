from RegulatoryNetworks import Solve, EvaluateExpression

def PrettyPrint(list_of_solutions):
    for solution in list_of_solutions:
        print solution


def RunTests():
    print("Running tests")
##    print(EvaluateExpression(1, [1,0,0], [0,1,0], (-1,2)))
    PrettyPrint(Solve(3, [[(0,0,0)],[(0,1,0),(1,0,0)]]))

    # Solve()



def main():
    RunTests()

if __name__ == '__main__':
    main()
