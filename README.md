# Carbon-Accounting-of-Hydrogen-ICIS-Submission-
We model the impact of different carbon accounting schemes to make a design decision within our HydroNet Project. 


## Conceptual Approach
See Glenk 2025
https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5338927

See Giovanniello
https://www.nature.com/articles/s41560-023-01435-0

https://github.com/macroenergy/Dolphyn.jl/tree/main/src/GenX/src/load_inputs

1. Model Elektrolyser with and without storage capacity
    Optimize Net Present Value --> See Input Data from Glenk (screening needed)
2. Build Virtual Carbon Storage Unit:
    Limitations: Must equal Zero by the End of year
3. Model over 10 year time horizon: Accounting deadline monthly vs. yearly 

## Activate venv

navigate to C:\HydroNET\HydroNet
then type: .\Scripts\Activate.ps1   


## Model Optimization 

Cost Function: 
Fixed Costs: $C$
Variable Costs: 
$$
 c_t = p_{t,s}*m_{t,s} + \delta*p_{n}*m_n
$$
 t: Time Intervall
 p: Price
 s: Electrcity
 \delta: Dummy Variable for PPA 
 n: PPA 

Revenue:
$$ 
 r_t = h_t*p_{t,b} + h_t*{t,g} 
$$
h: Hydrogen
b: grey classified
g: green classified
Target Function 
$$
max \sum_{t=1}^n r_t - c_t - C
$$