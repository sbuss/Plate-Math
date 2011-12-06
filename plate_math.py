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
    >> (plates, num_plates) = greedy(goal_weight - bar_weight)
    """

    # Init the number of plates
    num_plates = [0 for p in plates]

    # Not the most useful of closures, but it avoids passing an array, and
    # is thread-safe (Closures are neat!)
    def do_greedy(goal_weight):
        v = sum([p*n for (p,n) in zip(plates, num_plates)])
        if v < goal_weight:
            for pli in range(len(plates)):
                if v + 2*plates[pli] <= goal_weight:
                    num_plates[pli]+=2;
                    do_greedy(goal_weight)
                    break;

    do_greedy(goal_weight)
    return (plates, num_plates)

