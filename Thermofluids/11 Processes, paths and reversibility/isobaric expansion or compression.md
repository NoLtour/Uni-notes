---
aliases: ["isobaric","isobaric compression","constant pressure process","isobaric process","isobaric expansion"]
tags: ["Question","QFormat3"]
---

#### What is
## Isobaric expansion or compression
### Definition
This is a [[process (thermodynamics)|process]] in a [[closed system]] where there is no change in pressure, as represented on this [[p-v diagrams|pv diagram]]:

![[Pasted image 20211210154545.png]]

According to $P(\Delta V)=W$ since there is a change in volume in an [[isobaric expansion or compression|isobaric]] process there is [[pressure volume work]] done.

### Consequential relationships
These are useful when doing calculations on [[p-v diagrams]] since they can be used to calculate the changes in the properties between [[state (thermodynamics)|states]] where the [[process (thermodynamics)|process]] is [[isochoric heat transfer|isochoric]].

##### Pressure volume temp relationship
Simply [[ideal gas law]]:
> ### $$ \frac{ V_1}{T_1} = \frac{ V_2}{T_2} $$ 
>> where:
>> $V=$ Volume
>> $T=$ Temperature

##### Conservation of energy
> ### $$ Q_{12} - W_{12} = E_{u12} $$ 
>> where:
>> $Q_{12}=$ [[heat]] transfer from starting to ending conditions
>> $E_{u12}=$ [[internal energy]] change from starting to ending conditions
>> $W_{12}=$ work done from starting to ending conditions

##### Work transfer
from [[pressure volume work]]:
> ### $$ W_{12} = \int dW = P(\Delta V) = \int P(V) \cdot dV $$ 
>> where:
>> $W_{12}=$ work done from starting to ending conditions
>> $V=$ volume
>> $P(V)=$ pressure as a function of volume

##### [[heat|Heat]] transfer
> ### $$\begin{align*} Q_{12} =  E_{u12} + W_{12} &= mC_p (T_2-T_1)\\ &= mC_v (T_2-T_1) + P(V_2-V_1) \end{align*}$$
>> where:
>> $Q_{12}=$ [[heat]] transfer from starting to ending conditions
>> $E_{u12}=$ [[internal energy]] change from starting to ending conditions
>> $W_{12}=$ work done from starting to ending conditions
>> $T_1=$ initial temperature
>> $T_2=$ final temperature
>> $m=$ mass 
>> $C_v=$ [[constant volume specific heat]]
>> $C_p=$ [[constant pressure specific heat]]

##### [[enthalpy]] change
> ### $$ d E_{h} = C_{p} dT $$ 
>> where:
>> $C_{p}=$ [[constant pressure specific heat]]
>> $E_{h}=$ [[enthalpy]] 
>> $T=$ abs temp

### Uses
- boilers
- slow/steady combustion
- gas turbines
