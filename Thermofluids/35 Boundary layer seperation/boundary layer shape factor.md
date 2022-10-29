---
aliases: ["shape factor"]
tags: ["Question","QFormat3"]
---

#### What is
## Boundary layer shape factor ($H$)
A shape factor is a value that describes the nature of flow:

> ### $$ H = \frac{\delta *}{\theta} $$ 
>> where:
>> $H=$ [[boundary layer shape factor]]
>> $\delta *=$ [[boundary layer displacement thickness]]
>> $\theta=$ [[boundary layer momentum thickness]]

The greater the value of H, the stronger the adverse pressure gradient. A high adverse pressure gradient can greatly reduce the [[reynolds number]] at which transition into turbulence may occur. Hence this also increases risk of [[boundary layer separation]], so you want a small value of $H$ for most applications.

When you consider the physical meaning behined the shape factor. [[boundary layer displacement thickness|displacement thickness]] is a measure of lost volumetric flow and [[boundary layer momentum thickness|momentum thickness]] is a measure of lost momentum in flow, so consider:
$$ \frac{\theta}{\delta*} $$
This could be considered as the lost momentum per lost volumetric flow which when considering a flow profile:
![[Pasted image 20221029185004.png]]
Profiles with a less even velocity distribution, such as [[boundary layer|turbulent flows]] will have greater momentum lost relative to volumetric flow, since $H=(\frac{\theta}{\delta*})^{-1}$ we can therefore see that such concentrated flow profiles have lower $H$ numbers, hence laminar flows have higher [[boundary layer shape factor|shape factor]]s and turbulent lower.

Generally a $H>2.3$ will be laminar and $H<1.8$ will be turbulent (these are guidelines [[but it should atleast give a vague idea of the flows characterisation at a glance|not exact]]).