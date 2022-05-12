---
aliases: ["isothermal expansion","isothermal","isothermal process","constant temperature process","isothermal compression"]
tags: ["Question","QFormat3"]
---

#### What is
## Isothermal expansion or compression
### Definition
This is a [[process (thermodynamics)|process]] in a [[closed system]] where there is no change in temperature, as represented on this [[p-v diagrams|pv diagram]]:

![[Pasted image 20211210164803.png]]

You can see on the graph that the [[isothermal expansion or compression|isothermal process]] [[path (thermodynamics)|path]] follows the diagrams [[isotherms (thermodynamics)|isotherms]].

It should be noted that to get an [[isothermal expansion or compression|isothermal]] process [[heat]] transfer needs to occur over a negligible temperature difference. A consiquence is that to achieve this requires impractically slow expansion/compression so it's more for theoretical efficiency benchmarking.

According to $P(\Delta V)=W$ since there is a change in volume in an [[isothermal expansion or compression|isothermal]] process there is [[pressure volume work]] done.

Note that it will be a [[reversible and irreversible processes|reversible process]] if it's frinctionless.

### Consequential relationships
These are useful when doing calculations on [[p-v diagrams]] since they can be used to calculate the changes in the properties between [[state (thermodynamics)|states]] where the [[process (thermodynamics)|process]] is [[isothermal expansion or compression|isothermal]].


##### Pressure volume temperature
The [[ideal gas law]] can be used where $T$ is constant:
> ### $$ P_1 V_1 = P_2 V_2 $$ 
>> where:
>> $P=$ Pressure
>> $V=$ Volume

##### Conservation of energy
> ### $$ Q_{12} - W_{12} = E_{u12} = 0 $$ 
> ### $$ E_{u12} = 0$$ 
>> where:
>> $Q_{12}=$ [[heat]] transfer from starting to ending conditions
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
> ### $$\begin{align*} Q_{12} =  W_{12} \end{align*}$$
>> where:
>> $Q_{12}=$ [[heat]] transfer from starting to ending conditions
>> $W_{12}=$ work done from starting to ending conditions

##### [[enthalpy]] change
> ### $$ Q_{12} = E_{h12} $$ 
>> where:
>> $Q_{12}=$ [[heat]] transfer from starting to ending conditions
>> $E_{h12}=$ [[enthalpy]] change from starting to ending conditions

##### [[entropy|Entropy]] change

> ### $$ S_{12} = \frac{Q_{12}}{T_1} = mR \ln\left(\frac{P_1}{P_2}\right) = mR \ln\left(\frac{V_2}{V_1}\right) $$ 
>> where:
>> $Q_{12}=$ [[heat]] transfer from starting to ending conditions
>> $T_1=T_2=$ Temp at 1 or 2
>> $S_{12}=$ [[entropy]] change
>> $R=$ [[individual gas constant|specific gas constant]]
>> $m=$ mass

### Uses
Theoretical engine efficiency benchmarking.