class Storage:
    def __init__(self, name,id, max_capacity):
        self.name = name
        self.id = id
        self.max_capacity = max_capacity
###Define Functions that the Storage Unit needs to cover
    def calculate_hydrogen_production(self, power_input):
        return power_input * self.efficiency

    def calculate_cost(self, power_input):
        return power_input * self.cost_per_kw