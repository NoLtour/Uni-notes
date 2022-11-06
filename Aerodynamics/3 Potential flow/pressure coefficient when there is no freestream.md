---
aliases: [""]
tags: []
---

## Pressure coefficient when there is no freestream
In the event where for some reason there is no uniform flow, usually caused by a source or a sink there is no value for [[freestream]] velocity, in this case we need to redefine [[pressure coefficient]]. Since in practical terms freestream velocity is just a convenient number used to non dimensionalise problems and acting as a reference, hence all we need to replace it is something else that works for this purpose.

So we can just replace $U_{\infty}$ with $U_{ref}$:
> ### $$ C_{p} = \frac{p-p_{\infty}}{p_{0}-p_{\infty}} =  \frac{p-p_{\infty}}{\frac{1}{2}\rho_{\infty}V^{2}_{\infty}} $$ 
>> where:
>> $C_{p} =$ [[pressure coefficient]]
>> $p=$ [[static pressure]]
>> $p_{\infty}=$ [[static pressure]] in the [[freestream]]
>> $p_{0}=$ [[stagnation pressure]] in the free stream
>> $\rho_{\infty}=$ [[freestream]] density
>> $V_{\infty}=$ [[freestream]] veolcity