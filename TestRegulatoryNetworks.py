import itertools as it
from RegulatoryNetworks import Solve, SolveForRules, EvaluateExpression, value_to_string
import string

def PrettyPrintSolutionRules(solution_rules):
    '''Pretty print the solution rules.'''
    for individual_node_rules in solution_rules:
        for individual_node_solution in individual_node_rules:
            print individual_node_solution


def PrettyPrint(solutions):
    '''Pretty print list of solutions'''
    for solution in solutions:
        print solution


def GenerateInitialStates(num_nodes):
    '''Generate all possible initial states.

    TODO
    '''
    list_of_node_states = []
    binary_switch = [1, 0]
    for index in range(num_nodes):
        list_of_node_states.append(binary_switch)

    return it.product(*list_of_node_states)


def GetNextNodeState(current_state, solution_string):
    # current_state = (1, 1, 1)
    # solution_string: 'A = not B and C'
    # for index in range(len(current_state)):

    # Get part on right side of equals
    expression_string = solution_string[4:]

    expression_string = expression_string.replace("A" , str(current_state[0]))
    expression_string = expression_string.replace("B" , str(current_state[1]))
    expression_string = expression_string.replace("C" , str(current_state[2]))

    boolean_value = eval(expression_string)

    if boolean_value:
        return 1
    else:
        return 0


def GetNextState(current_state, solution):
#     print "asdf"
#     print current_state
#     print solution
#     asdf
#     (1, 1, 1)
#     ('A = not B and C', 'B = not D and B', 'C = B and D')
    next_state_as_list = []

    for index in range(len(current_state)):
        next_state_as_list.append(GetNextNodeState(current_state, solution[index]))

    return tuple(next_state_as_list)


def FindAllCyclesForSolution(initial_states, solution):
    '''Return a list of list of tuples representing all cycles'''
    visited_initial_states = []
    cycles = []

    for initial_state in initial_states:
        # If we have already visited this initial state then it is part of a cycle already.
        if initial_state in visited_initial_states:
            continue

        start_of_noose_or_cycle = initial_state

        # Otherwise must be a new cycle
        could_be_noose_cycle = [initial_state]
        visited_initial_states.append(initial_state)
        next_state = GetNextState(initial_state, solution)

        while(next_state not in could_be_noose_cycle):
            could_be_noose_cycle.append(next_state)
            next_state = GetNextState(next_state, solution)

        if next_state == start_of_noose_or_cycle:
            # this is a new cycle (not noose)
            for state in could_be_noose_cycle:
                if state not in visited_initial_states:
                    visited_initial_states.append(state)

            cycles.append(could_be_noose_cycle)

    return cycles

def SortInner(cycles_for_solution):
    cycles_inner_sorted = []

    for cycle_for_solution in cycles_for_solution:
        cycles_inner_sorted.append(sorted(cycle_for_solution))

    return cycles_inner_sorted



def ValidateSolution(solution, num_nodes, input_cycle_list):
    '''Validate a single solution

    Pseudo:
        1. Get all initial states
        2. Put in initial states and detect all cycles
        3. Verify that solution cycles is a superset (or equal) of steady_states_input_cycles
    '''
    initial_states = GenerateInitialStates(num_nodes)
    cycles_for_solution = FindAllCyclesForSolution(initial_states, solution)

    for input_cycle in input_cycle_list:
        if sorted(input_cycle) not in SortInner(cycles_for_solution):
            return False

    return True

def ValidateSolutionComplete(solution, num_nodes, input_cycle_list):
    '''Validate a single solution is complete.'''
    initial_states = GenerateInitialStates(num_nodes)
    cycles_for_solution = FindAllCyclesForSolution(initial_states, solution)
    return sorted(SortInner(input_cycle_list)) == sorted(SortInner(cycles_for_solution))

def ValiateAllSolutions(solutions, input_cycle_list):
    '''Checks if solutions are valid.

    params:
      list_of_solutions:
        List of the solutions, each solution as a tuple
      input_cycle_list:
        Initial cycles passed into solve which generated the solutions.
    raises:
        Exception if input is invalid
    '''
    for solution in solutions:
        #print len(solution)
        if ValidateSolution(solution, len(solution), input_cycle_list) == True:
            continue
        else:
            print "Solution NOT valid: " + str(solution)
            raise Exception("Solution not valid")


    print "All solutions are valid"


def PrintOnlyCompleteSolutions(solutions, input_cycle_list):
    '''Use to see if any complete solutions exist'''
    print "Checking for complete solutions below"
    for solution in solutions:
        if ValidateSolutionComplete(solution, len(solution), input_cycle_list) == True:
            print solution




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
    ValiateAllSolutions(solutions, [[(0,0,0)],[(0,1,0),(1,0,0)]])


def TestCompleteness():
    solutions = Solve(3, [[(0,0,0)],[(0,1,0),(1,0,0)]])
    PrintOnlyCompleteSolutions(solutions, [[(0,0,0)],[(0,1,0),(1,0,0)]])


def TestAll():
    '''Run all our tests.'''
    TestPrinting()
    TestSolve()
    TestCompleteness()

def main():
    TestAll()


if __name__ == '__main__':
    main()
