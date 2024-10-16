---
aliases: ["momentum thickness"]
tags: ["Question","QFormat3"]
---

#### Describe
## Boundary layer momentum thickness ($\theta$)
The momentum thickness, θ  is the distance by which a surface would have to be moved perpendicular from the reference plane in an inviscid fluid stream of velocity $U_{0}$ to give the same total momentum as exists between the surface and the reference plane in a real fluid.

The definition is confusing, but essentially it's the [[boundary layer displacement thickness|displacement thickness]] but instead of measuring the missing displacement it's measuring the missing momentum, hence the equations are the same just one is multiplied by velocity again. 

> ### $$ \theta = \int^{\infty}_{0} \frac{U(y)}{U_{\infty}}\left( 1 - \frac{U(y)}{U_{\infty}} \right) dy= \int^{\infty}_{0} \frac{ U}{U_{\infty}}\left( 1 - \frac{U }{U_{\infty}} \right) dy $$ 
> ### $$ \theta \approx \int^{\delta_{99}}_{0} \frac{ U}{U_{\infty}}\left( 1 - \frac{U }{U_{\infty}} \right) dy $$ 
>> where:
>> $\theta=$ [[boundary layer momentum thickness]]
>> $U(y)=$ flow rate as a function of y
>> $y=$ displacement relative to surface
>> $U_{\infty}=$ [[freestream]] veloicty
>> $\delta_{99}=$ [[boundary layer thickness]]
>> Flow is incompressible

Note how it can be approximated by limiting the bounds to the [[boundary layer thickness]], because at this point $U = U_{\infty} * 0.99$ hence it will lead to a "good enough" approximation of $\theta$.