from utils import evaluate_solution, total_cost
'''
Local Search Algorithm
Input:
    solution: A list of indices representing the current solution.
    instance: An object containing the problem instance data.
Output:
    best: A list of indices representing the best solution found.
'''
def local_search(solution, instance):
    best = solution[:]
    best_value = evaluate_solution(best, instance)
    n = len(instance.items)
    improved = True

    while improved:
        improved = False
        for i in range(n):
            if i not in solution:
                new_solution = solution + [i]
                if total_cost(new_solution, instance) <= instance.budget:
                    value = evaluate_solution(new_solution, instance)
                    if value > best_value:
                        best = new_solution
                        best_value = value
                        improved = True

        solution = best[:]

    return best
