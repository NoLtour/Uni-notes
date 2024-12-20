---
aliases: ["adiabatic expansion","adiabatic process","adiabatic compression","no heat transfer process","adiabatic"]
tags: ["Question","QFormat3"]
---

#### What is
## Adiabatic expansion or compression
### Definition
This is a [[process (thermodynamics)|process]] in a [[closed system]] where there is no [[heat]] transfer, as represented on this [[p-v diagrams|pv diagram]]:

![[Pasted image 20211210170233.png]]

Notice that dosn't follow [[isotherms (thermodynamics)|isotherms]].

It should be noted that to get  an [[adiabatic expansion or compression|adiabetic]] process there must be no net heat transfer across the [[system boundary]], to achieve this (or atleast a close approximation) you need to either have the process be incredibly quick or have the [[system (thermodynamics)|system]] be highly insulated.

According to $P(\Delta V)=W$ since there is a change in volume in an [[adiabatic expansion or compression|adiabetic]] process there is [[pressure volume work]] done.

Note that it will be a [[reversible and irreversible processes|reversible process]] if it's frinctionless since there is zero [[heat]] transfer.

### Consequential relationships (assuming is reversible)
These are useful when doing calculations on [[p-v diagrams]] since they can be used to calculate the changes in the properties between [[state (thermodynamics)|states]] where the [[process (thermodynamics)|process]] is [[isothermal expansion or compression|isothermal]].

Note that these __only__ apply if the process is reversible, for an [[reversible and irreversible processes|irreversible process]] refer to [[Joule expansion]].

##### Pressure volume temperature
The [[ideal gas law]] can be used:
> ### $$ \frac{P_1 V_1}{T_1} = \frac{P_2 V_2}{T_2} $$ 
>> where:
>> $P=$ Pressure
>> $V=$ Volume
>> $T=$ Temperature

There is also this guy that applys for adiabetic specificly:
> ### $$ PV^{\gamma} = constant $$
> ### $$ P_{1} V_{1}^{\gamma} = P_{2} V_{2}^{\gamma} $$ 
>> where:
>> $P=$ Pressure
>> $V=$ Volume
>> $\gamma=$ [[isentropic expansion factor|adiabatic index]]

^7c299a

##### Conservation of energy
> ### $$ \begin{align*}Q_{12} - W_{12} &= E_{u12} \\ - W_{12} &= E_{u12}\end{align*} $$ 
>> where:
>> $E_{u12}=$ [[internal energy]] change from starting to ending conditions
>> $W_{12}=$ work done from starting to ending conditions

##### Work transfer
from [[pressure volume work]]:
> ### $$ W_{12} = \int dW = \int P(V) \cdot dV $$ 
> ### $$ W_{12} = \frac{P_{1}}{1-\gamma}  \left( \frac{V_{1}^{\gamma}}{V_{2}^{\gamma-1}} - V_{1} \right) = \frac{P_{2}V_{2} - P_{1}V_{1}}{1-\gamma} $$ 
>> where:
>> $W_{12}=$ work done from starting to ending conditions
>> $V=$ volume
>> $P(V)=$ pressure as a function of volume
>> $\gamma=$ [[isentropic expansion factor|adiabatic index]]

##### [[heat|Heat]] transfer
$Q_{12}=0$
Nada.

##### [[enthalpy]] change
> ### $$ d E_{h} = C_{p} m dT $$ 
>> where:
>> $C_{p}=$ [[constant pressure specific heat]]
>> $E_{h}=$ [[enthalpy]] 
>> $m=$ mass of [[ideal gas law|ideal gas]]
>> $T=$ abs temp

### Uses
It is a good approximation of the power and compression strokes in a internal combustion engine.