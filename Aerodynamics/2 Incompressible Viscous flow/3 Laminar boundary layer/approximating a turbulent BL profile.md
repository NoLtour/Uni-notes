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

Turbulent boundary layers tend to have $n$ be around $7$, so if you do not have a value of $n$ the following equations which can be derived using the same methods from [[approximating a laminar BL profile]] and letting $n=7$ are the following:
> ### $$ \frac{\delta*}{x} \approx \frac{0.048}{(Re_{x})^{\frac{1}{5}}} $$ 
> ### $$ \frac{\theta}{x} \approx \frac{0.037}{(Re_{x})^{\frac{1}{5}}} $$ 
> ### $$ C_{f,x} \approx \frac{0.059}{(Re_{x})^{\frac{1}{5}}} $$ 
> ### $$ C_{F} \approx \frac{0.074}{(Re_{L})^{\frac{1}{5}}} $$ 
>> where:
>> $\delta *=$ [[boundary layer displacement thickness|displacement thickness]]
>> $\theta=$ [[boundary layer momentum thickness|momentum thickness]]
>> $x=$ position along flat plate
>> $n=7=$ [[approximating a turbulent BL profile|constant describing turbulant boundary layer profile on flat plate]]
>> $Re_{x}=$ [[Reynolds number]] at $x$
>> $Re_{L}=$ [[Reynolds number]] at $L$
>> $C_{F}=$ [[viscous drag coefficient]]
>> $C_{f,x}=$ [[viscous drag coefficient|local viscous drag coefficient]] at $x$

[[UNFINISHED STUFF]] derive general $n$ case for above equations.

### Issues with the approximation

Well if we look at the vertical velocity gradient $\frac{du}{dy}$ at $y=0$ we can see that:
$$ \left. \frac{du}{dy} \right|_{y=0} = \infty $$
Which implies an infinite [[local wall shear stress#^803cc0|wall shear stress]], this of course is not possible. When dealing with simplified models such as this it isn't a major issue but if our model requires detailed information on conditions near the wall it is clearly necessary to find a more accurate model for near wall conditions.



