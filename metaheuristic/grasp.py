import time
import random
from local_search import local_search
from random_greedy import random_greedy

def grasp(instance, max_iterations, random_seed, alpha, max_time, start_time):
    random.seed(random_seed)
    best_solution = []
    best_value = 0

    for i in range(max_iterations):
        solution = random_greedy(instance, alpha)
        solution = local_search(solution)
        value = solution.get_value()

        if value > best_value:
            best_solution = solution
            best_value = value
            elapsed_time = time.time() - start_time
            print(f"Nova solução encontrada: {solution.solution} com valor {best_value} em {elapsed_time:.2f} segundos")
        
        if elapsed_time > max_time:
            print(f"Tempo máximo atingido em {i} iterações")
            break

    return best_solution