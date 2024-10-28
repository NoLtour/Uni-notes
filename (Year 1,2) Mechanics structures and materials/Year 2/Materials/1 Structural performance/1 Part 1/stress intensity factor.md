---
aliases: ["stress intensity factor (Year 2)","shape factor" ]
tags: []
---

## Stress intensity factor ($K$)

### Description

This was somewhat touched in [[stress intensity factor (Year 1)]], but that was in a specific context so I'm making a separate page for the year 2 stuff.

The stress intensity factor, K, is used in fracture mechanics to predict the stress state near the tip of a crack caused by a remote load or residual stresses. Stress intensity factor is 

> ### $$\begin{align*} \sigma_{ij} &= \frac{K}{\sqrt{2\pi r}} f_{ij}(\theta) + \text{HOT} \end{align*}$$
> ![[Pasted image 20230204133454.png]]
> ### $$ \sigma_{f} = \sqrt{ \frac{2E\gamma}{\pi a} } $$
> ### $$ \sigma_{f} \sqrt{\pi a} = \sqrt{ 2 E \gamma } = K_{C} $$
> ### $$ K_{C} = Q \sigma_{f} \sqrt{ \pi a } $$
>> where:
>> $\sigma_{ij}=$ function of stress at some separation from the crack tip (using polar coordinates)
>> $f_{ij}(\theta)=$  A function of angle, where $f_{ij}(0) = 1$
>> $\text{HOT}=$ higher order terms, they exist and are some complex function but since their effect's generally insignificant they can be ignored for now
>> $r=$  polar coordiantes, distance from crack tip
>> $a=$ crack radius 
>> $\gamma=$ material yield stress
>> $E=$ stiffness ([[Youngs modulus]])
>> $K=$ Stress intensity factor, describes magnitude of local stresses for a particular crack tip
>> $K_{C}=$ [[critical stress intensity factor]]
>> $Q=$ Shape factor for 
>> $\sigma_{f}=$ fracture stress

What's especially useful is that it links to the energy balance approaches ([[griffith energys relationship with stress intensity factor]]), and is useful for a wide range of conditions. Below multiple loading conditions can be seen each has it's own critical stress intenstiy factor, where mode 1, mode 2 and mode 3 would have critical stress intensity factors of $K_{IC},K_{IIC},$ and $K_{IIIC}$ respectively (particular case stress intensity factors). Generally mode 1 loading is the most likely failure mode so that is where lots of analysis is done.

![[Pasted image 20230204133837.png]]


### Validity


![[Pasted image 20230204135249.png]]

An issue is that stress intensity factor is derived using elastic assumptions and we've just been showing that a thing called the [[stress concentration at a crack tip|plastic zone]] exists, which kinda fucks our stress factor prediction... but if you look at the chart it can be seen that outside of the plastic zone the equation still works! So basically as a rule of thumb if the plastic zone is small relative to the crack length (less than 1/50th of the cracks length) then stress intensity factor models are effective predictors of material behaviour.

#### Sheet materials

![[Pasted image 20230204140250.png]]

An example of where $K_{crit}$ is not constant is for thin sheets, as seen above the really thin sheets have variable $K_{crit}$'s, but above a certain thickness it is constant. This is because for thinner sheets they experience [[plane stress (generalised hookes law)|plane strain]] (or a close enough approximation) aka 2D loading, remember that because of [[poisson's ratio]] the thickness will change under loading, when the sheet is thin there is no material to restrict this contraction (coz it's too thin). This is also why the facture is at 45 degrees to the plain. 
In thicker sheets the thickness contraction is constrained in the centre of the sheet, so no strain in the thickness direction (but there is stress!). This high degree of constraint can be summed up as a triaxial stress state but a axial strain state. This is also why it's the weakest geometry.


