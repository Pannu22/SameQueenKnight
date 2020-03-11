# Chess Board

def board(a, b):
    """

    :param a: Length of X-axis of Chess Board
    :param b: Length of Y-axis of Chess Board
    :return: list of Tuple of all possible locations
    """
    list_all_possible = []
    for n in range(a):
        for m in range(b):
            tup = (n, m)
            list_all_possible.append(tup)

    return list_all_possible