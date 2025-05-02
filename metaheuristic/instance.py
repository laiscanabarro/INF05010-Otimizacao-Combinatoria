class Item:
    def __init__(self, id, cost, power):
        self.id = id
        self.cost = cost
        self.power = power

class Instance:
    def __init__(self, budget, items, synergy):
        self.budget = budget            
        self.items = items              
        self.synergy = synergy          

    def get_synergy(self, i, j):
        if i == j:
            return 0
        return self.synergy[max(i, j)][min(i, j)]
