---
aliases: ["crack propagation rate","crack growth rate"]
tags: ["Question","QFormat3"]
---

#### What is
## [[crack propagation (material fatigue)|Crack propagation]] rate (material fatigue) ($\frac{da}{dN}$)
### Intro
Stuff (yes that is the technical term) often contains defects, so we want to design taking into account [[crack propagation rate (material fatigue)|crack growth rate]] so we can maxamize the lifespan of our construction.

Since [[crack propagation rate (material fatigue)|crack propagation rate]] is the rate of change of crack radius per cycle it is equal to $\frac{da}{dN}$
We also know that the [[stress intensity factor|stress intensity]] will vary at the crack tip since under cyclic loading the stress varies and stress effects [[stress intensity factor|stress intensity]].

### Finding [[stress intensity factor]] range at the crack tip

We know you can find [[stress intensity factor|stress intensity]] using:
![[stress intensity factor#^bbe7f1]]

So now since we have values of $\sigma_{max}$ and $\sigma_{min}$:
$$\begin{align*}
\Delta K &= K_{max} - K_{min} & K_{max} &= Y \sigma_{max} \sqrt{\pi a} & K_{min} &= Y \sigma_{min} \sqrt{\pi a}\\
\Delta K &= Y \sigma_{max} \sqrt{\pi a} - Y \sigma_{min} \sqrt{\pi a}\\
\Delta K &=  (\sigma_{max}-\sigma_{min}) Y  \sqrt{\pi a}\\
\Delta K &=  (\Delta \sigma )Y  \sqrt{\pi a}\\
\end{align*}$$
Note that for values where $\sigma_{min}$ is compressive we let $\sigma_{min}=0$

Hence we are left with an equation: $\Delta K =  (\Delta \sigma )Y  \sqrt{\pi a}$ that describes the [[stress intensity factor]] range experienced at the crack tip.

### Crack propigation rate equation
We don't have a single equation as the relationship varies over the stress intensity factor range, as can be seen on this graph:
![[Pasted image 20211203132858.png]]
But we can get an equation for that [[oh damn that graph thicc|thicc]] strait region, known as "Region II". (I know very creatively named)

This is the equation for region II:
> ### $$ \frac{da}{dN} = \log( A (\Delta K)^{m} ) = m\log(\Delta K) + \log(A) $$ 
>> where:
>> $A=$ material constant 
>> $m=$ material constant
>> $a=$ crack radius
>> $K=$ [[stress intensity factor]] 

