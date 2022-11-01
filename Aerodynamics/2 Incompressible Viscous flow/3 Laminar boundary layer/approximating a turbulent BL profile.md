---
aliases: [""]
tags: []
---

## Approximating a turbulent BL profile
Basically the same similarity discussed in [[similarity in boundary layer velocity profiles]] which was used in [[approximating a laminar BL profile]] can be applied to turbulent boundary layers. The difference is that instead of the flow profile being equivalent to a parabolic equation it's an exponential relationship: 

> ## $$ \frac{u}{U_{\infty}} = \begin{dcases} \frac{y}{\delta}^{\frac{1}{n}} &,\: y\leq \delta \\ 1 &,\: y>\delta \end{dcases} $$ 
> ![[Pasted image 20221101105925.png]]
>> where:
>> $U_{\infty}=$ freestream velocity
>> $u=$ velocity
>> $y=$ position normal to flat plate
>> $\delta=$ [[boundary layer thickness]]
>> $n=$ a value specific to that turbulent boundary layer, which needs to be found through curve fitting

Due to the similarity between points in the turbulent flow, once $n$ is found we can find the profile at any other position given we know the [[boundary layer thickness]]:
![[Pasted image 20221101110119.png]]
