import random

'''
Random Greedy Algorithm
Input:
    instance: A problem instance.
    alpha: % of solutions that satisfy new clauses and from which a random solution will be chosen.
Output:
    best: A list of indices representing the best solution found.
'''

def generate_candidates(instance, remaining_items, remaining_budget, partial_solution):
    candidates = []

    for item in remaining_items:
        if instance.items[item].cost <= remaining_budget:
            synergy_sum = sum(instance.get_synergy(item, j) for j in partial_solution) if partial_solution else 0
            merit = (instance.items[item].power + synergy_sum) / instance.items[item].cost
            candidates.append((item, merit))
    
    return sorted(candidates, key=lambda x: x[1], reverse=True)

def choose_random(candidates, alpha):
    size = max(1, int(len(candidates) * alpha))
    limited_list = candidates[:size]
    return random.choice(limited_list)[0] if limited_list else None

def random_greedy(instance, alpha):
    best = []
    remaining_items = list(range(instance.n))
    random.shuffle(remaining_items)
    remaining_budget = instance.budget
    
    while True:
        candidates = generate_candidates(instance, remaining_items, remaining_budget, best)

        if not candidates:
            break
        
        chosen_item = choose_random(candidates, alpha)

        if chosen_item is None:
            break
        
        best.append(chosen_item)
        remaining_budget -= instance.items[chosen_item].cost
        remaining_items.remove(chosen_item)

    return best
     