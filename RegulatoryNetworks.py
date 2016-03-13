# Module for solving regulatory networks

import string
import itertools as it

ALPHABET = ['ABCDEFGHIJKLMNOPQRSTUVWXYZ']

def Solve(num_nodes, cycles_list):
    '''
    params:
     num_nodes:
        number of nodes
     cycles_list:
        A list of cycles where each individual cycle is a list of tuples.

        Eg. cycles_list = [
            [(1, 0, 0)],
            [(1, 0, 1), (0, 1, 0)]
        ]

    returns:
        A list of logic statements where each logic statement is a tuple. The first element of the tuple is the value
        we are assigning, the remaining two elements are strings representing variables with an optional ! (not).

        Eg. return_value = [("A" , "A", "B"), ("B", "!B", "!A")]
                - A = A && B
                - B = !B && !A
    '''
##    alphabet = list(string.ascii_uppercase)
##    if num_nodes > len(alphabet):
##        raise Exception("Cannot pass more than %d nodes" % len(alphabet))
    nodes = [i for i in range(1,num_nodes+1)]
    possible_expressions = GenerateExpressions(num_nodes, nodes)

    # Init all posibilities for each node.
    result = {}
    for n in nodes:
        result[n] = list(possible_expressions)

        # Based on ALL cycles reduce the possibilities to only legal expressions.
        for cycle in cycles_list:
            result[n] = RemoveIllegalExpressions(n, result[n], cycle)
    print result



def GenerateExpressions(num_nodes, nodes):
    '''
    params:
        num_nodes:
            number of nodes

    returns:
        Generate all AND logic expressions with 2 variables per expression.
        e.g. 2, output:
        [
            ("A","B"),
            ("!A","B"),
            ("A","!B"),
            ("!A","B")
        ]
    '''
    duplicates = []
    domain = []
    for n in nodes:
        domain.append(n)
        domain.append(n*-1)
        duplicates.append((n,n))
        duplicates.append((n,n*-1))
        duplicates.append((n*-1, n))
        duplicates.append((n*-1,n*-1))

    domains = []
    for i in range(2):
        domains.append(domain)

    expressions = list(it.product(*domains))

    for idx, e in enumerate(expressions):
        expressions[idx] = list(e)
        expressions[idx].sort()
        expressions[idx] = tuple(expressions[idx])

    expressions = set(expressions)

    expressions.difference_update(duplicates)
    expressions = list(expressions)
##    print expressions
    return expressions



def RemoveIllegalExpressions(index, expressions, cycle):
    reduced_list = list(expressions)
    n = len(cycle)
    print "NUMBER OF CYCLE: ", n
    # for each cycle
    for i in range(n):
        to_remove = []
        for e in reduced_list:
            if not EvaluateExpression(index, cycle[i], cycle[(i+1)%n], e):
                to_remove.append(e)
        for tr in to_remove:
            reduced_list.remove(tr)
    return reduced_list


def EvaluateExpression(index, prev_state, curr_state, expression):
    i1 = abs(expression[0]) - 1
##    print prev_state
    v1 = prev_state[i1]^(expression[0] < 0)
    i2 = abs(expression[1]) - 1
    v2 = prev_state[i2]^(expression[1] < 0)
##    print "v1: ",v1, "v2: ", v2
    result = (curr_state[index-1] == (v1 and v2))
    return result

