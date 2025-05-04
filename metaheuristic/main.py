import os
from reader import read_instance
from local_search import local_search
from random_greedy import random_greedy

current_dir = os.path.dirname(os.path.abspath(__file__))
instances_folder = os.path.join(current_dir, "..", "sinergias_instancias")

def main():
    for i in range(1, 11):
        instance_file = os.path.join(instances_folder, f"{i:02}.txt")
        instance = read_instance(instance_file)

        # Printando os resultados com busca local só pra conferir
        alpha = 0.15
        solution = random_greedy(instance, alpha)
        solution = local_search(solution)
        
        print(f"\nInstância {i:02}")
        print(f"Número de items: {instance.n}")
        print(f"Orçamento: {instance.budget}")
        print(f"Solução otimizada: {solution.solution}")
        print(f"Custo: {solution.total_cost}")
        print(f"Valor: {solution.value}")

if __name__ == "__main__":
    main()