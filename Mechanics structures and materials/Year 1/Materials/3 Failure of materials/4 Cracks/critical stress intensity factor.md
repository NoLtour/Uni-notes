---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Critical stress intensity factor ($K_c$)
The critical stress intensity factor is the [[stress intensity factor]] at which the local stress required for fracture to occur is reached.

This is the equation for critical stress intensity factor for an infinate plate:

> ### $$ K_c = \sigma_f \sqrt{\pi a_c} $$ 
>> where:
>> $K_c=$ [[critical stress intensity factor]] 
>> $\sigma_f=$ stress applied at fracture
>> $a_c=$ [[critical crack radius]]

So if we know either $\sigma$ or $a$ we can determine the other.

This is the equation for the critical stress intensity factor for any shape object

> ### $$ K_c = Y \sigma_f \sqrt{\pi a_c} $$ 
>> where:
>> $K_c=$ [[critical stress intensity factor]] 
>> $\sigma_f=$ stress applied at fracture
>> $a_c=$ [[critical crack radius]]
>> $Y=$ A dimensionless parameter which depends on the crack and specimin geometry as well as the mannor of load application

Y can usually be found in books. When searching for values keep in mind that $Y\sqrt{\pi}=\gamma\left(\frac{a}{W}\right)$

### Limitations
It should be notesd that this model is most accurate for thick plates:
![[Pasted image 20211126201617.png]]

(Here $K_{IC}$ is strain fracture toughness)

And that when applying this formula we assume that we are acting with no plastic deformation.
