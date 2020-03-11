# Knight

def knight(x, y):
    """

    :param x: X position of Knight
    :param y: Y position of Knight
    :return: List of tuple of all possible attacking positions of Knight
    """
    harm_pos = [(x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2), (x + 2, y + 1), (x + 2, y - 1),
                (x - 2, y + 1), (x - 2, y - 1)]

    harm_pos = [i for i in harm_pos if i[0] <= 7]
    harm_pos = [i for i in harm_pos if i[1] <= 7]
    harm_pos = [i for i in harm_pos if i[0] > -1]
    harm_pos = [i for i in harm_pos if i[1] > -1]

    return harm_pos


# def knightPlace(x, y):
#     """
#
#     :param x: X position of Knight
#     :param y: Y position of Knight
#     :return: List of tuple of all possible placing positions of Knight
#     """
#     place_pos = [(x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1)]
#
#     place_pos = [i for i in place_pos if i[0] > -1]
#     place_pos = [i for i in place_pos if i[1] > -1]
#
#     return place_pos