---
aliases: [""]
tags: []
---

## Solving laminar boundary layer equations

If we want to solve the motion equations to get the relevant coefficients for a flat plate it isn't really possible using the unsimplified [[navier stokes equations]] (without a super computer), it is however possible to solve them if we make (lots) of assumptions, with the results being useful for getting rough solutions

Starting with the [[navier stokes equations]]:
 $$ \frac{\delta u}{ \delta x } + \frac{\delta v}{ \delta y } = 0$$
 $$ u \frac{\delta u}{\delta x} + v \frac{\delta u}{\delta y}  = - \frac{1}{\rho} \frac{\delta p}{\delta x} + \nu \left( \frac{\delta^{2} u }{ \delta x^{2} } + \frac{\delta^{2} u }{ \delta y^{2} } \right)  $$  
 $$ u \frac{\delta v}{\delta x} + v \frac{\delta v}{\delta y}  = - \frac{1}{\rho} \frac{\delta p}{\delta y} + \nu \left( \frac{\delta^{2} v }{ \delta x^{2} } + \frac{\delta^{2} v }{ \delta y^{2} } \right)  $$  

To non dimensionalise these we need scales that make sense for each variable ($x,y,u,v$):
- $x$ can be expressed as a fraction of length of the plate $L$ hence $x\to L$
- $y$ can be expressed as a fraction of the [[boundary layer thickness]] $\delta$ hence $y\to \delta$
- $u$ is often described as a fraction of the free stream velocity hence: $u \to U_\infty$
- $v$ is generally assumed to be negligible relative to the effect of $u$, but this needs to be verified

So to get an order of magnitude estimate of $v$ we can use the equation for [[mass continuity using divergence#^31084a|mass continuity]] and plug in the non dimensionalising parameters discussed above:
$$\begin{align*}
\frac{\delta u}{ \delta x } + \frac{\delta v}{ \delta y } &= 0\\
\frac{\delta u}{ \delta x } &= - \frac{\delta v}{ \delta y } \\
U_\infty\frac{ \delta}{ L } &\approx    v 
\end{align*}$$
(This type of analysis gives us the [[mmmmm dimensional analysis|rough]] order of magnitude of $v$) It can be seen that for v to be small $L$ must be large relative to $\delta$, hence a descent estimate can be found even if we ignore $v$ for a long plate.
We can preform the same analysis on the momentum equations to find the relative size of different terms:
 $$ u \frac{\delta u}{\delta x} + v \frac{\delta u}{\delta y}  = - \frac{1}{\rho} \frac{\delta p}{\delta x} + \nu \left( \frac{\delta^{2} u }{ \delta x^{2} } + \frac{\delta^{2} u }{ \delta y^{2} } \right)  $$  
 We know there is no pressure gradient hence $\frac{\delta p}{\delta x}$ can be ignored, then we split the equation into it's components:
 $$\begin{align*}
u &\frac{\delta u}{\delta x} \to \frac{U^{2}}{L} & v &\frac{\delta u}{\delta y} \to \frac{U_\infty\frac{ \delta}{ L }U_\infty}{\delta} = \frac{U^{2}}{L} & \nu \frac{\delta^{2} u }{ \delta x^{2} } \to \nu \frac{U }{L^{2}} &  & \nu \frac{\delta^{2} u }{ \delta y^{2} } \to \nu \frac{U}{\delta^{2}} \\
\end{align*}$$
Since $\delta$ is small relative to $L$ we know that $\frac{1}{L^{2}} << \frac{1}{\delta^{2}}$ hence in the momentum equation $\nu \left( \frac{\delta^{2} u }{ \delta x^{2} } + \frac{\delta^{2} u }{ \delta y^{2} } \right)$ the effect of $\frac{\delta^{2} u }{ \delta x^{2} }$ can be ignored. Using this knowledge to simplify the momentum equation we get:
$$\begin{align*}
 \frac{U^{2}}{L} &\approx    \nu  \frac{ U }{ \delta ^{2} }  \\
 \frac{ \delta ^{2} }{L^{2}} &\approx    \nu  \frac{ U }{U^{2} L }  \\
 \frac{ \delta   }{L } &\approx   \sqrt { \frac{ \nu }{U  L }}  \\
&\approx \frac{1}{\sqrt{Re_{L}}}
\end{align*}$$

This heavily approximated result actually is quite accurate for laminar boundary layers:

> ## $$  \frac{ \delta   }{L } \underset{\sim}{\propto} \frac{1}{\sqrt{Re_{L}}}  $$  
>> where:
>> $\delta=$ [[boundary layer displacement thickness|displacement thickness]] 
>> $Re_{L}=$ [[Reynolds number]] for length $L$
>> $L=$ plate length

The solution for [[boundary layer|turbulent boundary layers]] is actually quite similar: $\frac{ \delta   }{L } \underset{\sim}{\propto} \frac{1}{{Re_{L}^{0.2}}}$

