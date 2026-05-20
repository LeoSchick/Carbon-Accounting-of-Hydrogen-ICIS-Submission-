###Basic Optimization Model for Hydrogen Production

import pyomo 



## Input Data 

T = range(168) #Time in Hours

pg = {t: 100 for t in T}  # Price for green hydrogen
pd = {t: 50 for t in T}   # Price for grey hydrogen

pe = {t: 20 for t in T}   # Price of electricity from the grid

eta = 0.8  # Efficiency of the electrolysis process

## Model

model = pyo.ConcreteModel()

# Time Index 

model.T = pyo.Set(initialize=T)

## Variables 


model.qg = pyo.Var(model.T, within=pyo.Reals) # Quantity of green hydrogen sold
model.qd = pyo.Var(model.T, within=pyo.Reals) # Quantity of dirty hydrogen sold

model.bg = pyo.Var(model.T, within=pyo.Reals) # Filling of green hydrogen tank
model.bd = pyo.Var(model.T, within=pyo.Reals) # Filling of dirty hydrogen tank


model.o = pyo.Var(model.T, within=pyo.Reals) # Quantity of electricity bought from the grid

## Objective Function

model.objective = pyo.Objective(
    expr=sum(model.qg[t] * pg[t] + model.qd[t] * pd[t] - model.o[t] * pe[t] for t in model.T),
    sense=pyo.maximize
)

## Constraints

##1 Filling of the green hydrogen tank

def green_tank_capacity_rule(model, t):
    if t == 0:
        return model.bg[t] ==  0 + eta * model.o[t]  # Initial filling of the green hydrogen tank
    return model.bg[t] == model.bg[t-1] + eta * model.o[t] - model.qg[t]  # Balance of the green hydrogen tank

model.green_tank_capacity = pyo.Constraint(model.T, rule=green_tank_capacity_rule)

##2 Filling of the dirty hydrogen tank

def dirty_tank_capacity_rule(model, t):
    if t == 0:
        return model.bd[t] ==  0 + eta * model.o[t]  # Initial filling of the dirty hydrogen tank
    return model.bd[t] == model.bd[t-1] + eta * model.o[t] - model.qd[t]  # Balance of the dirty hydrogen tank

model.dirty_tank_capacity = pyo.Constraint(model.T, rule=dirty_tank_capacity_rule)

###3 Total capacity of the tanks

def total_tank_capacity_rule(model, t):
    return model.bg[t] + model.bd[t] <= 1000  # Total capacity of the tanks

model.total_tank_capacity = pyo.Constraint(model.T, rule=total_tank_capacity_rule)

##4 Selling constraints
#a) Green hydrogen selling constraints
def green_selling_constraints_rule(model, t):
    return model.bg[t] >= model.qg[t]  # Cannot sell more green hydrogen than what is in the tank

model.green_selling_constraints = pyo.Constraint(model.T, rule=green_selling_constraints_rule)

#b) Dirty hydrogen selling constraints
def dirty_selling_constraints_rule(model, t):
    return model.bd[t] >= model.qd[t]  # Cannot sell more dirty hydrogen than what is in the tank

model.dirty_selling_constraints = pyo.Constraint(model.T, rule=dirty_selling_constraints_rule)

#Solving Problem:

solver = pyo.SolverFactory('glpk')
results = solver.solve(model)

for t in model.T:
    print(
        t,
        "grid electricity bought:", pyo.value(model.o[t]),
        "green hydrogen sold:", pyo.value(model.qg[t]),
        "dirty hydrogen sold:", pyo.value(model.qd[t]),  
        "revenue:", pyo.value(model.qg[t] * pg[t] + model.qd[t] * pd[t])
    )