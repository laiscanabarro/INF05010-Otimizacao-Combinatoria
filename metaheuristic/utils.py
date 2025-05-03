import itertools

def evaluate_solution(solution, instance):
    total_power = sum(instance.items[i].power for i in solution)
    total_synergy = sum(instance.get_synergy(i, j) for i, j in itertools.combinations(solution, 2))
    return total_power + total_synergy

def total_cost(solution, instance):
    return sum(instance.items[i].cost for i in solution)
