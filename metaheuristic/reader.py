from instance import Item, Instance
'''
    - a primeira linha do arquivo informa o orçamento (O) e o número de equipamentos (n)

    - a segunda linha até a n+1-ésima linha do arquivo possuem o custo (ci) e o poder (pi) dos n equipamentos correspondentes

    - as linhas n+2 até 2n+1 possuem n valores cada (formam uma matriz quadrada), destes só os valores do triângulo inferior 
      (onde i > j, sendo i a linha da matriz e j a coluna da matriz) são não zero (isto é, o valor da sinergia para quaisquer
      equipamentos a e b fica em s[max(a,b), min(a,b)])
'''
def read_instance(filepath):
    with open(filepath, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]

    budget, n = map(int, lines[0].split())
    items = []

    for i in range(1, n + 1):
        cost, power = map(int, lines[i].split())
        items.append(Item(i - 1, cost, power))

    synergy = [[0] * n for _ in range(n)]
    for i in range(n):
        row = list(map(int, lines[n + 1 + i].split()))
        for j in range(len(row)):
            if i > j:
                synergy[i][j] = row[j]
                synergy[j][i] = row[j]  
                
    return Instance(budget, items, synergy)
