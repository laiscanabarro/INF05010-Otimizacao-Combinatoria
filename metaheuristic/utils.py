import itertools

def compute_values(instance, solution):
    total_cost = 0
    total_power = 0
    total_synergy = 0

    for i in range(len(solution)):
        item_i = instance.items[solution[i]]
        total_cost += item_i.cost
        total_power += item_i.power
        for j in range(i):
            total_synergy += instance.get_synergy(solution[i], solution[j])

    value = total_power + total_synergy

    return total_cost, total_power, total_synergy, value
