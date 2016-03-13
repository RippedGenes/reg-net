import itertools as it

from RegulatoryNetworks import Solve, SolveForRules, EvaluateExpression


def PrettyPrintSolutionRules(solution_rules):
    '''Pretty print the solution rules.'''
    for individual_node_rules in solution_rules:
        for individual_node_solution in individual_node_rules:
            print individual_node_solution


def PrettyPrint(solutions):
    '''Pretty print list of solutions'''
    for solution in solutions:
        print solution


def ValiateAllSolutions(solutions, minimum_steady_states):
    '''Checks if solutions are valid.

    params:
      list_of_solutions:
        List of the solutions, each solution as a tuple
      minimum_steady_states:
        Initial steady states passed into solve which generated the solutions.
    raises:
        Exception if input is invalid
    '''
    for solution in solutions:
        pass #TODO



def TestPrinting():
    ''' Test all pretty printing functions'''
    print("Test Printing: ")
    solutions = Solve(3, [[(0,0,0)],[(0,1,0),(1,0,0)]])
    solution_rules = SolveForRules(3, [[(0,0,0)],[(0,1,0),(1,0,0)]])
    print "Pretty print solution: "
    PrettyPrint(solutions)
    print "Pretty print solution rules: "
    PrettyPrintSolutionRules(solution_rules)
    # TODO validate in code


def TestSolve():
    '''Test the solve function against various inputs.'''
    solutions = Solve(3, [[(0,0,0)],[(0,1,0),(1,0,0)]])



def TestAll():
    '''Run all our tests.'''
    TestPrinting()
    TestSolve()


def main():
    TestAll()


if __name__ == '__main__':
    main()
