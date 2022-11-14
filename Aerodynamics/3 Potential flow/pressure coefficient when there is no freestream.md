---
aliases: [""]
tags: []
---

## Pressure coefficient when there is no freestream
In the event where for some reason there is no uniform flow, usually caused by a source or a sink there is no value for [[freestream]] velocity, in this case we need to redefine [[pressure coefficient]]. Since in practical terms freestream velocity is just a convenient number used to non dimensionalise problems and acting as a reference, hence all we need to replace it is something else that works for this purpose.

 

So we can just replace $U_{\infty}$ with $U_{ref}$:
> ### $$ C_{p} =  \frac{p-p_{ref}}{\frac{1}{2}\rho V^{2}_{ref}}= 1-\frac{  u^{2} + w^{2}  }{ V^{2}_{ref} } =   1-\frac{  V_{\theta}^{2} + V_{r}^{2}  }{ V^{2}_{ref} } $$ 
> ### $$  \frac{1}{2}\rho V^{2}_{ref}-  \frac{1}{2}\rho (u^{2} + w^{2})  =   p-p_{ref} $$ 
>> where:
>> $C_{p} =$ [[pressure coefficient]]
>> $p=$ [[static pressure]]
>> $p_{ref}=$ [[static pressure]] in at the reference
>> $\rho=$ density
>> $V_{ref}=$ reference velocity
>> $u,w=$ horizontal and vertical velocity
>> Incompressible flow.

^6ace8a

It is obvious that $V_{ref}$ must be non zero for this to work.