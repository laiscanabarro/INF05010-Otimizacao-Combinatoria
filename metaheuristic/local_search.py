import numpy as np
from utils import compute_values

'''
Local Search Algorithm
Input:
    solution: A list of indices representing the current solution.
    instance: An object containing the problem instance data.
Output:
    best: A list of indices representing the best solution found.
'''

def local_search(instance, solution, max_iterations, alpha): 
    best = solution[:]
    best_set = set(best)
    total_cost, total_power, total_synergy, best_value = compute_values(instance, solution)

    synergy_matrix = np.array(instance.synergy)

    for _ in range(max_iterations):
        improved = False

        for i in best[:]:
            item_out = instance.items[i]

            remaining_items = [j for j in range(instance.n) if j not in best_set]
            remaining_items.sort(key=lambda j: instance.items[j].power / instance.items[j].cost, reverse=True)
            size = max(1, int(len(remaining_items) * alpha))
            top_candidates = remaining_items[:size]

            for j in top_candidates:
                item_in = instance.items[j]
                new_cost = total_cost - item_out.cost + item_in.cost

                if new_cost <= instance.budget:
                    new_power = total_power - item_out.power + item_in.power

                    best_without_i = [x for x in best if x != i]
                    synergy_loss = synergy_matrix[i, best_without_i].sum()
                    synergy_gain = synergy_matrix[j, best_without_i].sum()
                    
                    new_synergy = total_synergy - synergy_loss + synergy_gain

                    new_value = new_power + new_synergy

                    if new_value > best_value:
                        best.remove(i)
                        best.append(j)
                        best_set.remove(i)
                        best_set.add(j)
                        total_cost = new_cost
                        total_power = new_power
                        total_synergy = new_synergy
                        best_value = new_value
                        improved = True
                        break
            if improved:
                break
        if not improved:
            break

    return best, best_value
