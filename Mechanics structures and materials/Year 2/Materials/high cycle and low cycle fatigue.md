---
aliases: ["HCF","LCF","high cycle fatigue","low cycle fatigue","fatigue strength coefficient","fatigue strength exponent","fatigue ductility coefficient","fatigue ductility exponent","modeling high cycle fatigue","modeling low cycle fatigue"]
tags: []
---

## High cycle and low cycle fatigue
### Description
These are just classifications for how many cycles it takes for something to break. ([[final fracture (material fatigue)]]) As with most classifications in materials it is arbitrary kek:
- [[high cycle and low cycle fatigue|high cycle fatigue]] where fracture occurs after 10^5 cycles
- [[high cycle and low cycle fatigue|low cycle fatigue]] where fracture occurs before 10^5 cycles
 
![[Pasted image 20230211120852.png]]

An object like a turbine blads probably going to experience [[high cycle and low cycle fatigue|low cycle fatigue]] while something like a lathe is probably going to experience [[high cycle and low cycle fatigue|high cycle fatigue]].  
Note that on that [[S-N curves|S-N curve]] we used [[stress amplitude]] but depending on what's significant in determining the lifetime a strain curve may be used instead. (strain may be more important than stress depending on object geometry and other [[idk material science seems mostly experimental solutions|shite]])

### Modelling

#### High cycle fatigue

![[Pasted image 20230211121539.png]]

> ### $$\begin{align*}  \frac{\Delta \sigma}{2} &= \sigma_{f}' (2N_{f})^{b} \end{align*}$$
>> where:
>> $\Delta \sigma=$ [[stress range]]
>> $N_{f}=$ [[fatigue life (material fatigue)|cycles to failure]]
>> $\sigma_{f}'=$ [[high cycle and low cycle fatigue|fatigue strength coefficient]]
>> $b=$ [[high cycle and low cycle fatigue|fatigue strength exponent]]

Note that [[high cycle and low cycle fatigue|fatigue strength exponent]] and [[high cycle and low cycle fatigue|fatigue strength coefficient]] are generally just empirically determined values which relate to some specific situation.

Also something to keep in mind is that under HCF you generally have low strain so the way cracks grow will be during processes that can occur under mostly elas

#### Low cycle fatigue

So you know what I was saying about strain usually being more important for [[high cycle and low cycle fatigue|low cycle fatigue]] well that's reflected in this equation describing LCF and [[fatigue life (material fatigue)|cycles to failure]]. This is because in [[high cycle and low cycle fatigue|HCF]] cases plastic deformation is usually the main thing driving crack propagation.

![[Pasted image 20230211122027.png]]

> ### $$\begin{align*}  \frac{\Delta \varepsilon}{2} &= \varepsilon_{f}' (2N_{f})^{c} \end{align*}$$
>> where:
>> $\Delta \varepsilon=$ [[strain range]]
>> $N_{f}=$ [[fatigue life (material fatigue)|cycles to failure]]
>> $\varepsilon_{f}'=$ [[high cycle and low cycle fatigue|fatigue ductility coefficient]]
>> $c=$ [[high cycle and low cycle fatigue|fatigue ductility exponent]]
