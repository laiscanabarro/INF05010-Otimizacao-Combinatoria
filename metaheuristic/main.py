import os
from reader import read_instance
from local_search import local_search

current_dir = os.path.dirname(os.path.abspath(__file__))
instances_folder = os.path.join(current_dir, "..", "sinergias_instancias")

for i in range(1, 11):
    instance_file = os.path.join(instances_folder, f"{i:02}.txt")
    instance = read_instance(instance_file)

    # Printando os resultados com busca local só pra conferir
    initial_solution = []
    solution = local_search(initial_solution, instance)
    
    print(f"Instância {i:02}")
    print(f"Orçamento: {instance.budget}")
    print(f"Solução inicial: {initial_solution}")
    print(f"Solução otimizada: {solution}")