---
aliases: ["RANS"]
tags: []
---

## Reynolds averaged Navier Stokes equations

This is where we use a "statistical description of the flow". For turbulant flow we know of course they are [[unsteady flow]], the [[Reynolds averaged Navier Stokes equations|RANS]] approach is to convert velocity and pressures into their statistical representations, for example take the velocity of a point:
![[Pasted image 20221101102100.png]]
The velocity is all over the place, but we can define instantaneous velocity as a function of mean velocity of that point plus variation, the same can also be done for pressure and velocity in other directions:
$$\begin{align*}
u(t) &= \bar{u}+u'(t)\\
v(t) &= \bar{v}+v'(t)\\
p(t) &= \bar{p}+p'(t)
\end{align*}$$
The [[Reynolds averaged Navier Stokes equations|RANS]] is where we take measures of the mean and the standard deviation of a property for use in numerical simulation.
> ## $$ \bar{u} = \frac{1}{T}\int^{T}_{0} u \cdot dt $$
> ## $$ \bar{u'} = 0 $$
> ## $$ \bar{u'^{2}} = \frac{1}{T}\int^{T}_{0} (u-\bar{u})^{2} \cdot dt = (\sigma_{u'})^{2} $$ 
>> where:
>> $u=$ horizontal velocity (can also be vertical velocity or pressure, this is more a stand in for some property of the flow)
>> $T=$ time interval to average over
>> $\bar{u}=$ [[mean value by integration|mean]] $u$
>> $u'(t)=$ instantaneous variation of $u$ from $\bar{u}$
>> $\sigma_{u'}=$ [[standard deviation for probabability functions|standard deviation]] of $u'$

By taking the statistical forms of these properties ($u,v,p$) and plugging them into the [[navier stokes equations]] we get terms called "Reynolds stresses" which are the consequences of the variation and hence the cause of mixing in the flow. Accurately modelling the Reynolds stresses is what we need to find a model for to get accurate flow characteristics.

The way this manefests in the [[navier stokes equations]] is similar to what was seen in [[large eddy simulations]]:

$$ \frac{\delta \bar{u}}{ \delta x } + \frac{\delta \bar{v}}{ \delta y } = 0$$
 $$ \bar{u} \frac{\delta \bar{u}}{\delta x} + \bar{v} \frac{\delta \bar{u}}{\delta y}  = - \frac{1}{\rho} \frac{\delta \bar{p}}{\delta x} + \n\bar{u} \left( \frac{\delta^{2} \bar{u} }{ \delta x^{2} } + \frac{\delta^{2} \bar{u} }{ \delta y^{2} } \right)  $$  
$$ \bar{u} \frac{\delta \bar{v}}{\delta x} + \bar{v} \frac{\delta \bar{v}}{\delta y}  = - \frac{1}{\rho} \frac{\delta \bar{p}}{\delta y} + \n\bar{u} \left( \frac{\delta^{2} \bar{v} }{ \delta x^{2} } + \frac{\delta^{2} \bar{v} }{ \delta y^{2} } \right)  $$