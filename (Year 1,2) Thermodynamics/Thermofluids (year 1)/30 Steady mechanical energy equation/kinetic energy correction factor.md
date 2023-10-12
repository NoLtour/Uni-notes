---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Kinetic energy correction factor ($\alpha$)
Basically this thing is used to account for the uneven distrobution of mass flow through a cross section due to friction with the wall:
![[Pasted image 20220303164904.png]]
On the left is an ideal situation while the right is more realistic, so we don't have to deal with the headache of calculating it ourselves you usually get given it but heres the formula:

> ### $$ \alpha =  \frac{ KE_{actual\:velocity}}{KE_{average\:velocity}} = \frac{\frac{1}{2} dm U^{2} }{\frac{1}{2} dm \bar{U}^{2} }= \frac{ U^{2} }{ \bar{U}^{2} } $$ 
> ### $$ \alpha \times KE_{average\:velocity} =  KE_{actual\:velocity}  $$ 
>> where:
>> $\alpha=$ [[kinetic energy correction factor]]
>> $KE_{average\:velocity}=$ the kinetic energy using the average velocity of a cross section
>> $KE_{actual\:velocity}=$ the actual kinetic energy through the cross section

So you know how with the [[conservation of energy in flow|conservation of energy in flow equation]] if you narrow a pipe the KE increases, well the same thing happens with pipes that have differential flow:
![[Pasted image 20220303225927.png]]
The total throughput needs to be the same but the velocity difference in the centre relative to the sides acts just like a pipe narrowing, which as we know increases the KE of the water, this difference can be expressed as a ratio which is where $\alpha$ comes in.