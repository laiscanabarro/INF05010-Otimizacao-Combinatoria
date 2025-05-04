from local_search import local_search
from random_greedy import random_greedy

def grasp(instance, alpha, max_iterations):
    best_solution = []
    best_value = 0

    for _ in range(max_iterations):
        solution = random_greedy(instance, alpha)
        solution = local_search(solution)
        value = solution.get_value()

        if value > best_value:
            best_solution = solution
            best_value = value

    return best_solution