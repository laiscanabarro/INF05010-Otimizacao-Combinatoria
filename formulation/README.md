# Instrução para execução 

A execução requer os seguintes parâmetros:
- `<filepath>`: Caminho do arquivo de instâncias
- `<time>`: Tempo limite
- `<seed>`: Semente de aleatoriedade

```bash
julia formulation/main.jl <filepath> <time> <seed>
`````

### Exemplo:
```bash
julia formulation/main.jl sinergias_instancias/01.txt 300 1
`````

### Requisitos
- [Julia](https://julialang.org/downloads/)