# Instrução para execução 

A execução requer os seguintes parâmetros:
- `--filepath` ou `-f`: Caminho do arquivo de instâncias
- `--iterations` ou `-m`: Número máximo de iterações
- `--seed` ou `-s`: Semente de aleatoriedade
- `--alpha` ou `-a`: Parâmetro alpha de aleatoriedade
- `--time` ou `-t`: Tempo máximo de execução (em segundos).

### Exemplos:

#### Exemplo 1
```bash
python3 metaheuristic/main.py --filepath sinergias_instancias/01.txt --iterations 100 --seed 1 --alpha 0.05 --time 300
`````

#### Exemplo 2
```bash
python3 metaheuristic/main.py -f sinergias_instancias/01.txt -m 100 -s 1 -a 0.05 -t 300
`````

### Requisitos
- [Python versão 3](https://www.python.org/downloads/)

