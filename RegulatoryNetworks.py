# Module for solving regulatory networks

import string
import itertools as it
import graphviz as gv
# import networkx as nx
# import matplotlib.pyplot as plt


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
    nodes = [i for i in range(1, num_nodes + 1)]
    possible_expressions = GenerateExpressions(num_nodes, nodes)

    # Init all posibilities for each node.
    result = {}
    for n in nodes:
        result[n] = list(possible_expressions)

        # Based on ALL cycles reduce the possibilities to only legal expressions.
        for cycle in cycles_list:
            result[n] = RemoveIllegalExpressions(n, result[n], cycle)
        ##    print result

    DrawGraph(result)
    solution_list = ListOfSolutions(result)
    return solution_list


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
        domain.append(n * -1)
        duplicates.append((n, n))
        duplicates.append((n, n * -1))
        duplicates.append((n * -1, n))
        duplicates.append((n * -1, n * -1))

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
    return expressions


def RemoveIllegalExpressions(index, expressions, cycle):
    '''
    params:
        index:
            index of node who's expressions we are checking
        expressions:
            list of expression to check
        cycle:
            the cycle to check the expressions through

    returns:
        list of expressions still valid after the checks
    '''
    reduced_list = list(expressions)
    n = len(cycle)
    # for each cycle
    for i in range(n):
        to_remove = []
        for e in reduced_list:
            if not EvaluateExpression(index, cycle[i], cycle[(i + 1) % n], e):
                to_remove.append(e)
        for tr in to_remove:
            reduced_list.remove(tr)
    return reduced_list


def EvaluateExpression(index, prev_state, curr_state, expression):
    '''
    params:
        index:
            index of node who's expressions we are checking
        prev_state:
            previous state,i.e. get the values of the expression from this state
        curr_state:
            current state,i.e. get the value of the index node from this state
        expression:
            the expression with which to compare the index node to

    returns:
        True or False depending if the expression holds or not
    '''

    i1 = abs(expression[0]) - 1
    v1 = prev_state[i1] ^ (expression[0] < 0)
    i2 = abs(expression[1]) - 1
    v2 = prev_state[i2] ^ (expression[1] < 0)
    result = (curr_state[index - 1] == (v1 and v2))
    return result


def ListOfSolutions(results):
    '''
    params:
        results:
            dictionary where key is the node, and value are a list of tuples
            representing the possible inputs to the node
    returns:
        Solution string
    '''
    solutions_list = []
    alphabet = list(string.ascii_uppercase)
    if len(results) > len(alphabet):
        raise Exception("Cannot pass more than %d nodes" % len(alphabet))
    for node in results:
        for possibilities in results[node]:
            value1 = possibilities[0]
            value2 = possibilities[1]

            solutions_list.append((alphabet[node] + " = " + value_to_string(value1, alphabet) + \
                                   " AND " + value_to_string(value2, alphabet)))

    return solutions_list


def value_to_string(number, alphabet):
    '''
    params:
        number:
            node value
        alphabet:
            a list of the capital letters
    returns:
        a string with node number changed to alphabet notation and including
        "NOT" for negatives
    '''
    string = ""
    if number < 0:
        string += "NOT "
    string += alphabet[abs(number)]
    return string

def DrawGraph(nodes):
  '''
  params:
  	nodes:
		  results, dictionary with key being nodes and value being possible expressions for it, e.g.
		  {1: [(-1, 2), (-3, 2)], 2: [(-3, 1), (-2, 1)], 3: [(1, 3), (2, 3), (1, 2), (-2, 3), (-1, 3)]}
  returns:
	  Nothing. It produces all produces all graphs and places in the img folder
  '''
  alphabet = list(string.ascii_uppercase)

  graph_fodder = []
  for n in nodes:
    expressions = []
    for expression in nodes[n]:
      e = []
      e.append(n)
      e.extend(list(expression))
      expressions.append(e)
    graph_fodder.append(expressions)


  possibilities = list(it.product(*graph_fodder))

  # print possibilities

  for i,p in enumerate(possibilities):
    G = gv.Digraph(format='svg')
    for nodes in p:
      into = nodes[0]
      for out in nodes[1:]:
        c = 'green' if out > 0 else 'red'
        G.edge(alphabet[abs(out)], alphabet[into], color = c)
  	G.render("img/graph"+str(i))

