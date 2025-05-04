import os
import time
from reader import read_instance
from grasp import grasp

current_dir = os.path.dirname(os.path.abspath(__file__))
instances_folder = os.path.join(current_dir, "..", "sinergias_instancias")

def main():
    total_time = 0

    for i in range(1, 11):
        instance_file = os.path.join(instances_folder, f"{i:02}.txt")
        instance = read_instance(instance_file)

        alpha = 0.15
        max_iterations = 10

        start_time = time.time()

        solution = grasp(instance, alpha, max_iterations)

        elapsed_time = time.time() - start_time
        total_time += elapsed_time
        
        print(f"\nInstância {i:02}")
        print(f"Número de items: {instance.n}")
        print(f"Orçamento: {instance.budget}")
        print(f"Solução otimizada: {solution.solution}")
        print(f"Custo: {solution.total_cost}")
        print(f"Valor: {solution.value}")
        print(f"Tempo de execução: {elapsed_time:.2f} segundos")
    
    print(f"\nTempo total das 10 instâncias: {total_time:.2f} segundos")

if __name__ == "__main__":
    main()