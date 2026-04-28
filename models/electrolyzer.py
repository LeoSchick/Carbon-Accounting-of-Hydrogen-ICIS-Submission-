class Elektrolyzer:
    def __init__(self, name,id, efficiency, cost_per_kw):
        self.name = name
        self.id = id
        self.efficiency = efficiency
        self.cost_per_kw = cost_per_kw

    def calculate_hydrogen_production(self, power_input):
        return power_input * self.efficiency

    def calculate_cost(self, power_input):
        return power_input * self.cost_per_kw