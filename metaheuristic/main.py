import os
import time
import argparse
from reader import read_instance
from grasp import grasp

def main():
    
    parser = argparse.ArgumentParser(description='GRASP - Problema de Sinergias')
    parser.add_argument('-f', '--filepath', type=str, required=True, help='Caminho do arquivo de instâncias')
    parser.add_argument('-i', '--iterations', type=int, required=True, help='Número máximo de iterações')
    parser.add_argument('-s', '--seed', type=int, required=True, help='Semente de aleatoriedade')
    parser.add_argument('-a', '--alpha', type=float, required=True, help='Parâmetro alpha de aleatoriedade')
    parser.add_argument('-t', '--time', type=int, required=False, help='Tempo máximo de execução')

    args = parser.parse_args()

    file_path = args.filepath
    max_iterations = args.iterations
    random_seed = args.seed
    alpha = args.alpha
    max_time = args.time
        
    file_name = os.path.basename(file_path)
    instance = read_instance(file_path)

    print(f"\nArquivo: {file_name}")
    print(f"Número de items: {instance.n}")
    print(f"Orçamento: {instance.budget}")
    
    start_time = time.time()
    solution = grasp(instance, max_iterations, random_seed, alpha, max_time, start_time)
    elapsed_time = time.time() - start_time
    
    print(f"\nMelhor solução encontrada: {solution.solution}")
    print(f"Custo: {solution.total_cost}")
    print(f"Valor: {solution.value}")
    print(f"Tempo total de execução: {elapsed_time:.2f} segundos\n")
            
if __name__ == "__main__":
    main()
