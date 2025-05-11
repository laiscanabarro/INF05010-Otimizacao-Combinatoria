from instance import Item, Instance

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
                
    return Instance(len(items), budget, items, synergy)
