---
aliases: [""]
tags: []
---

## General heat exchanger

> ![[Pasted image 20231214122208.png]]
> ### $$\begin{align*} \text{Hot fluid change:}&&\dot{Q} = \dot{m}_{h} (\mathcal{H}_{h,i} - \mathcal{H}_{h,o}) &= \dot{m}_{h} c_{p,h} (T_{h,i} - T_{h,o})= C_{h} (T_{h,i} - T_{h,o})  \\\\\text{Cold fluid change:}&&\dot{Q} = \dot{m}_{c} (\mathcal{H}_{c,o} - \mathcal{H}_{c,i}) &= \dot{m}_{c} c_{p,c} (T_{c,o} - T_{c,i})= C_{c} (T_{c,o} - T_{c,i}) \\\\\text{Barrier exchange:}&&\dot{Q} = h' A\Delta T_{m} ,\:\:\:\:\: \frac{1}{h'} &= \frac{1}{h_{h}} + \frac{1}{h_{c}} + \frac{\delta}{k_{w}}  \end{align*}$$
>> where:
>> $\dot{Q}=$ heat transfer 
>> $\mathcal{H}=$ specific [[entropy]]
>> $\dot{m}=$ mass flow
>> $T_{i}=$ temp of fluid in
>> $T_{o}=$ temp of fluid out
>> $c_{p}=$ [[constant pressure specific heat]] capacity
>> $C_{p}=$ [[constant pressure specific heat|constant pressure heat]] capacity
>> $h=$ mean [[convection heat transfer coefficient]]
>> $\delta=$ thickness of wall
>> $k_{w}=$ [[material thermal conductivity|thermal conductivity]] of wall

The equation for heat transfer in a heat exchanger is quite trivial to derived, the main problem comes in the fact that calculation of the $h$ values is non trivial. Especially given the uneven temperature gradient depending on the fluids direction of flow and relative temps. As will be seen later.

