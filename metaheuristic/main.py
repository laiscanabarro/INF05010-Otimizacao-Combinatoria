import os
from reader import read_instance

current_dir = os.path.dirname(os.path.abspath(__file__))
instances_folder = os.path.join(current_dir, "..", "sinergias_instancias")

for i in range(1, 11):
    instance_file = os.path.join(instances_folder, f"{i:02}.txt")
    
    instance = read_instance(instance_file)

    # Printando os 10 arquivos só pra conferir
    print(f"Orçamento: {instance.budget}")
    print("Itens:")
    for item in instance.items:
        print(f"  ID: {item.id}, Custo: {item.cost}, Poder: {item.power}")
    print("Matriz de Sinergia:")
    for row in instance.synergy:
        print("  ", row)