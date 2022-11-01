---
aliases: ["constant describing turbulant boundary layer profile on flat plate"]
tags: []
---

## Approximating a turbulent BL profile

(all this analysis is for working with a flat plate)

### Approximating using an exponential function

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

Subbing the velocity function into the related equations and solving gives us:

> ## $$ \frac{\delta *}{\delta} = 1- \frac{n}{n+1} $$ 
> ## $$ \frac{\theta}{\delta} = \frac{n}{n+1} - \frac{n}{n+2} $$ 
> ## $$ H = \frac{n+2}{n} $$ 
>> where:
>> $\delta *=$ [[boundary layer displacement thickness|displacement thickness]]
>> $\theta=$ [[boundary layer momentum thickness|momentum thickness]]
>> $\delta=$ [[boundary layer thickness]]
>> $H=$ [[boundary layer shape factor|shape factor]]
>> $n=$ [[approximating a turbulent BL profile|constant describing turbulant boundary layer profile on flat plate]]

(I'm not doing the proof for this one, [[did it using online calculators|lazy]])

### Issues with the approximation

Well if we look at the vertical velocity gradient $\frac{du}{dy}$ at $y=0$ we can see that:
$$ \left. \frac{du}{dy} \right|_{y=0} = \infty $$
Which implies an infinite [[local wall shear stress#^803cc0]]
