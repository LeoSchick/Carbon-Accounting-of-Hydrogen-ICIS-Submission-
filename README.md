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
## Model Description 

This Table give a short Overview about Key Variables 

|Variable | Description | Dependent |
| :--- | :---: | ---: |
| $$p_t^g$$ | External Market Price for Green Hydrogen | exogenous Input |
| $$q_t^g$$ | Quantity of green Hyrodgen sold on market | endogenous variable Input |
| $$p_t^d$$ | External Market Price for Grey (dirty) Hydrogen | exogenous Input |
| $$q_t^d$$ | Quantity of Grey (dirty) Hyrodgen sold on market | endogenous variable Input |
| $$e_t$$ | Energy (Electricity) Price at Time t | exogenous variable Input |
| $$o_t$$ | Energy (Electricity) Quantity at Time t | exogenous variable Input |
| $$b_t^g$$ | Quantity in Tank at Time t | exogenous variable Input |

**Optimizing Function**

$$
\max_{q} \sum_{t=1}^T p_t^g q_t^g + p_t^d q_t^d - e_to_t
$$

s.t.
$$
 b_t^g = \sum_{k=t_0}^{t-1} [o_k^g - q_k^g]
$$
$$
 b_t^d = \sum_{k=t_0}^{t-1} [o_k^d - q_k^d]
$$

$$
q_t^g <= b_t^g ; t \in T
$$

$$
q_t^d <= b_t^d ; t \in T
$$

$$
b_{max} >= b_t^d + b_t^g ; t \in T
$$

This Table give a short Overview on the optimization Constraints

|Variable | Description | Additional thought |
| :---: | :---: | :---: |
|  $$ b_t^g = \sum_{k=t_0}^{t-1} [o_k^g - q_k^g] $$| The produced amount of hydrogen cannot exceed the purchased and labeled green hydrogen. The sum controls for cumulative values over time horizon T | Here we need to add a constant efficiency factor describing how incoming energy translates into amounts of hydrogen. We can also consider water as an additional input good  |
| $$ b_t^d = \sum_{k=t_0}^{t-1} [o_k^d - q_k^d] $$ | $$b_t^d$$ equal the amount of hydrogen currently available in storage component.The produced amount of hydrogen cannot exceed the purchased and labeled grey hydrogen. The sum controls for cumulative values over time horizon T | endogenous variable Input |
| $$q_t^g <= b_t^g ; t \in T$$ | For each time step t only the amount currently stored in the tank can be sold | How do we model anticipation of higher prices? Is it thoughful to consider strategic storing? |
| q_t^d <= b_t^d ; t \in T | For each time step t only the amount currently stored in the tank can be sold | .. |
| $$b_{max} <= b_t^d + b_t^g ; t \in T$$ | Full Storage Capacity | Factor that needs to be equal in each modeled scenario |




## Model Optimization First Draft

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


