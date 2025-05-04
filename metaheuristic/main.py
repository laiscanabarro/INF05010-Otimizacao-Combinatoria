import os
from reader import read_instance
from grasp import grasp

current_dir = os.path.dirname(os.path.abspath(__file__))
instances_folder = os.path.join(current_dir, "..", "sinergias_instancias")

def main():
    for i in range(1, 11):
        instance_file = os.path.join(instances_folder, f"{i:02}.txt")
        instance = read_instance(instance_file)

        alpha = 0.15
        max_iterations = 10
        solution = grasp(instance, alpha, max_iterations)
        
        print(f"\nInstância {i:02}")
        print(f"Número de items: {instance.n}")
        print(f"Orçamento: {instance.budget}")
        print(f"Solução otimizada: {solution.solution}")
        print(f"Custo: {solution.total_cost}")
        print(f"Valor: {solution.value}")

if __name__ == "__main__":
    main()