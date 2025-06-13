from utils import compute_values

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
        self._total_cost = None
        self._total_power = None
        self._total_synergy = None
        self._value = None
        self._compute_values()

    def _compute_values(self):
        self._total_cost, self._total_power, self._total_synergy, self._value = compute_values(self.instance, self.solution)

    @property
    def total_cost(self):
        return self._total_cost

    @property
    def total_power(self):
        return self._total_power
    
    @property
    def total_synergy(self):
        return self._total_synergy

    @property
    def value(self):
        return self._value
    