import itertools as it

from RegulatoryNetworks import Solve, SolveForRules, EvaluateExpression


def PrettyPrintSolutionRules(solution_rules):
    '''Pretty print the solution rules.

    TODO
    '''
    for individual_node_rules in solution_rules:
        for individual_node_solution in individual_node_rules:
            print individual_node_solution


def PrettyPrint(solutions):
    for solution in solutions:
        print solution


def ValidateInput(solutions, minimum_steady_states):
    '''Checks if solutions are valid.

    params:
      list_of_solutions:
        List of the solutions in human readable format.
      minimum_steady_states:
        Initial steady states passed into solve which generated soltions.
    raises:
        Exception if input is invalid
    '''
    pass



def RunTests():
    print("Running tests")
    solutions = Solve(3, [[(0,0,0)],[(0,1,0),(1,0,0)]])
    solution_rules = SolveForRules(3, [[(0,0,0)],[(0,1,0),(1,0,0)]])
    print "Pretty print solution: "
    PrettyPrint(solutions)
    print "Pretty print solution rules: "
    PrettyPrintSolutionRules(solution_rules)
    # PrettyPrint(solutions)
    # ValidateInput(solutions , [[(0,0,0)],[(0,1,0),(1,0,0)]])


def main():
    RunTests()


if __name__ == '__main__':
    main()
