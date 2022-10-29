---
aliases: ["displacement thickness"]
tags: ["Question","QFormat3"]
---

#### Describe
## Boundary layer displacement thickness ($\delta*$)

The current definition used to define the position of the boundary layer is where the local stream velocity is 99% of the [[freestream]] velocity ($U=U_{\infty}$). This definition is not very useful for calculations so instead boundary layer thickness is often defined through "displacement thickness".

Displacement thickness is technically defined as "the distance by which a surface would have to be moved in the direction parallel to its normal vector towards the reference plane in an [[inviscid flow|inviscid fluid stream]] of velocity $U_{0}$ to give the same mass flow rate as occurs between the surface and the reference plane in a real fluid."

Or put simply the displacement needed from the surface to encapsulate a volume equal to the volume of "missing flow" caused by the boundary layer:
![[Pasted image 20220426222934.png]]

This can be defined algebraically:

> ### $$ \delta * = \int^{\infty}_{0} \left( 1 - \frac{U(y)}{U_{\infty}} \right) dy $$ 
>> where:
>> $\delta *=$ [[boundary layer displacement thickness]] 
>> $U(y)=$ flow rate as a function of y
>> $y=$ displacement relative to surface
>> $U_{\infty}=$ [[freestream]] velocity 
>> Flow is incompressible


> ### $$ \delta * = \int^{\infty}_{0} \left( 1 - \frac{\rho(y) U(y)}{\rho_{0} U_{\infty}} \right) dy $$ 
>> where:
>> $\delta *=$ [[boundary layer displacement thickness]] 
>> $U(y)=$ flow rate as a function of y
>> $\rho(y)=$ density as a function of y
>> $y=$ displacement relative to surface
>> $U_{\infty}=$ [[freestream]] velocity 
>> $\rho_{0}=$ Free stream density??
>> Flow is compressible

