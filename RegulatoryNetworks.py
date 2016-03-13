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
    alphabet = list(string.ascii_uppercase)
    if num_nodes > len(alphabet):
        raise Exception("Cannot pass more than %d nodes" % len(alphabet))
    nodes = [alphabet[i] for i in range(num_nodes)]
    possible_expressions = GenerateExpressions(num_nodes, nodes)

##    # Init all posibilities for each node.
##    result = {}
##    for n in nodes:
##        result[n] = list(possible_expressions)
##
##        # Based on ALL cycles reduce the possibilities to only legal expressions.
##        for cycle in cycles_list:
##            result[n] = RemoveIllegalExpressions(result[n], cycle)



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
        domain.append("!" + n)
        duplicates.append((n,n))
        duplicates.append((n,"!" + n))
        duplicates.append(("!" + n, n))
        duplicates.append(("!" + n,"!" + n))

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
    print expressions



def RemoveIllegalExpressions(expressions, cycle):
    pass