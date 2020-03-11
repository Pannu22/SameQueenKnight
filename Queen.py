# Queen

def queen(x, y, size_of_chess):
    """

    :param x: X position of Queen
    :param y: Y position of Queen
    :param size_of_chess: Tuple of size of chess board
    :return: list of all attacking positions of Queen
    """
    harm_pos = []
    # Row Up
    for p in range(x):
        harm_pos.append((p, y))

    # Row Down
    for p in range(x + 1, size_of_chess[0]):
        harm_pos.append((p, y))

    # Column Left
    for q in range(y):
        harm_pos.append((x, q))

    # Column Right
    for q in range(y + 1, size_of_chess[1]):
        harm_pos.append((x, q))

    # Left Upper Diagonal
    i = 1
    for p in range(x):
        harm_pos.append((x - i, y - i))
        i = i + 1

    # Right Lower Diagonal
    i = 1
    for p in range(x + 1, size_of_chess[0]):
        harm_pos.append((x + i, y + i))
        i = i + 1

    # Right Upper Diagonal
    i = 1
    for p in range(x):
        harm_pos.append((x - i, y + i))
        i = i + 1

    # Left Lower Diagonal
    i = 1
    for p in range(x + 1, size_of_chess[0]):
        harm_pos.append((x + i, y - i))
        i = i + 1

    # Drop Queen position
    harm_pos = [i for i in harm_pos if i != (x, y)]

    harm_pos = [i for i in harm_pos if i[0] <= 7]
    harm_pos = [i for i in harm_pos if i[1] <= 7]
    harm_pos = [i for i in harm_pos if i[0] > -1]
    harm_pos = [i for i in harm_pos if i[1] > -1]

    return harm_pos