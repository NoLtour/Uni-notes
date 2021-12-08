---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe
## Viscoelasticity in [[polymers]]
As discussed in [[thermoplastic deformation#Necking]] it is possible for polymers to exhibit viscous and eleastic characteristics during deformation. 
This also leads to the material exhibiting time dependent strain, also known as [[creep (materials)|creep]].

### Modeling w math
#### Equations
It is possible to express [[creep (materials)|creep]] in polymers mathamatically:
> ### $$ - \frac{d\sigma}{dt} \propto \sigma $$ 
>> where:
>> $\sigma=$ stress
>> $\frac{d\sigma}{dt}=$ rate of change of stress

> ### $$ \sigma_t = \sigma_0 e^{-\frac{t}{\tau}} $$
> ### $$ \ln\left( \frac{\sigma_t}{\sigma_0} \right)= - \frac{t}{\tau} $$ 
>> where:
>> $\sigma_t=$ stress at time t
>> $\sigma_0=$ origional stress
>> $t=$ time
>> $\tau=$ relaxation time

> ### $$ E_r(t) = \frac{\sigma_t}{\varepsilon_0} $$ 
>> where:
>> $\varepsilon_0=$ the strain 
>> $E_r(t)=$ The relaxation modulus as a function of time
>> $\sigma_t=$ The time dependent stress

#### On a graph
