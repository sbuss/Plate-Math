plates = [45, 35, 25, 10, 5, 2.5]


def greedy(goal_weight):
    """ Greedy knapsack solution.

    A greedy solution to the constrained knapsack problem that is plate math.
    Don't forget to subtract the weight of your bar from goal_weight.

    Usage:
    Given a 45LB bar:
    >> from plate_math import greedy
    >> bar_weight = 45
    >> goal_weight = 285
    >> plates = greedy(goal_weight - bar_weight)
    """

    # Init the number of plates
    num_plates = dict((plate, 0) for plate in plates)

    if goal_weight < 0:
        return num_plates

    def total_weight():
        return sum([p * n for (p, n) in num_plates.iteritems()])

    def add_plates(plate):
        num_plates[plate] = 2 * ((goal_weight - total_weight()) // (2 * plate))

    for plate in plates:
        add_plates(plate)

    return num_plates
