from instance import Solution

'''
Local Search Algorithm
Input:
    solution: A list of indices representing the current solution.
    instance: An object containing the problem instance data.
Output:
    best: A list of indices representing the best solution found.
'''

def local_search(solution):
    best = Solution(solution.instance, solution.solution[:])
    best_value = best.get_value()
    improved = True

    while improved:
        improved = False
        for i in range(solution.instance.n):
            if i not in best.solution:
                new_items = best.solution + [i]
                new_solution = Solution(best.instance, new_items)
                if new_solution.get_total_cost() <= best.instance.budget:
                    value = new_solution.get_value()
                    if value > best_value:
                        best = new_solution
                        best_value = value
                        improved = True

    return best
