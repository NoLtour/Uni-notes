---
aliases: ["adiabetic expansion","adiabetic process","adiabetic compression","no heat transfer process","adiabetic"]
tags: ["Question","QFormat3"]
---

#### What is
## Adiabetic expansion or compression
### Definition
This is a [[process (thermodynamics)|process]] in a [[closed system]] where there is no [[heat]] transfer, as represented on this [[p-v diagrams|pv diagram]]:

![[Pasted image 20211210170233.png]]

Notice that dosn't follow [[isotherms (thermodynamics)|isotherms]].

It should be noted that to get  an [[adiabetic expansion or compression|adiabetic]] process there must be no net heat transfer across the [[system boundary]], to achieve this (or atleast a close approximation) you need to either have the process be incredibly quick or have the [[system (thermodynamics)|system]] be highly insulated.

According to $P(\Delta V)=W$ since there is a change in volume in an [[adiabetic expansion or compression|adiabetic]] process there is [[pressure volume work]] done.

Note that it will be a [[reversible and irreversible processes|reversible process]] if it's frinctionless since there is zero [[heat]] transfer.

### Consequential relationships
These are useful when doing calculations on [[p-v diagrams]] since they can be used to calculate the changes in the properties between [[state (thermodynamics)|states]] where the [[process (thermodynamics)|process]] is [[isothermal expansion or compression|isothermal]].

##### Pressure volume temperature
The [[ideal gas law]] can be used:
> ### $$ \frac{P_1 V_1}{T_1} = \frac{P_2 V_2}{T_2} $$ 
>> where:
>> $P=$ Pressure
>> $V=$ Volume
>> $T=$ Temperature

There is also this guy that applys for adiabetic specificly:
> ### $$ PV^{\gamma} = constant $$ 
>> where:
>> $P=$ Pressure
>> $V=$ Volume
>> $\gamma=$ [[isentropic expansion factor|adiabatic index]]

##### Conservation of energy
> ### $$ \begin{align*}Q_{12} - W_{12} &= E_{u12} \\ - W_{12} &= E_{u12}\end{align*} $$ 
>> where:
>> $E_{u12}=$ [[internal energy]] change from starting to ending conditions
>> $W_{12}=$ work done from starting to ending conditions

##### Work transfer
from [[pressure volume work]]:
> ### $$ W_{12} = \int dW = \int P(V) \cdot dV $$ 
>> where:
>> $W_{12}=$ work done from starting to ending conditions
>> $V=$ volume
>> $P(V)=$ pressure as a function of volume

##### [[heat|Heat]] transfer
$Q_{12}=0$
Nada.

##### [[enthalpy]] change
> ### $$ d E_{h} = C_{p} m dT $$ 
>> where:
>> $C_{p}=$ [[constant pressure specific heat]]
>> $E_{h}=$ [[enthalpy]] 
>> $m=$ mass
>> $T=$ abs temp

### Uses
It is a good approximation of the power and compression strokes in a internal combustion engine.