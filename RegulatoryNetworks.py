# Module for solving regulatory networks

def Solve(cycles_list):
    """
    params:
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
    """
