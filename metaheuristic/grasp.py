import time
import random
from instance import Solution
from local_search import local_search
from random_greedy import random_greedy

def grasp(instance, max_iterations, random_seed, alpha, max_time, start_time):
    random.seed(random_seed)

    best_solution = random_greedy(instance, alpha)
    best_solution, best_value = local_search(instance, best_solution, max_iterations, alpha)

    print(f"\nSolução inicial: {best_solution}")
    print(f"Valor inicial: {best_value}\n")

    i = 2
    while True:
        elapsed_time = time.time() - start_time
        if max_time is not None:
            if elapsed_time >= max_time:
                print(f"\nTempo máximo ({max_time:.2f}s) atingido em {i - 1} iterações")
                break
        elif max_iterations is not None and i > max_iterations:
            break

        solution = random_greedy(instance, alpha)
        solution, value = local_search(instance, solution, max_iterations, alpha)

        if value > best_value:
            best_solution = solution
            best_value = value
            print(f"Nova solução encontrada: {solution} com valor {best_value} em {i} iterações e {elapsed_time:.2f} segundos")
        
        i += 1

    return Solution(instance, best_solution)