import itertools

class Item:
    def __init__(self, id, cost, power):
        self.id = id
        self.cost = cost
        self.power = power

class Instance:
    def __init__(self, n, budget, items, synergy):
        self.n = n
        self.budget = budget
        self.items = items
        self.synergy = synergy

    def get_synergy(self, i, j):
        if i == j:
            return 0
        return self.synergy[max(i, j)][min(i, j)]

class Solution:
    def __init__(self, instance, solution):
        self.instance = instance
        self.solution = solution
        self.total_cost = self.get_total_cost()
        self.total_power = self.get_total_power()
        self.total_synergy = self.get_total_synergy()
        self.value = self.get_value()
    
    def get_total_cost(self):
        return sum(self.instance.items[i].cost for i in self.solution)
        
    def get_total_power(self):
        return sum(self.instance.items[i].power for i in self.solution)
    
    def get_total_synergy(self):
        return sum(self.instance.get_synergy(i, j) for i, j in itertools.combinations(self.solution, 2))
    
    def get_value(self):
        return self.get_total_power() + self.get_total_synergy()
    