---
aliases: [""]
tags: []
---

## Something

We 

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
U_\infty\frac{ \delta}{ L } &\to  v 
\end{align*}$$
(This type of analysis gives us the [[mmmmm dimensional analysis|rough]] order of magnitude of $v$) It can be seen that for v to be small $L$ must be large relative to $\delta$, hence a descent estimate can be found even if we ignore $v$ for a long plate.
We can preform the same analysis on the momentum equations to find the relative size of different terms:
 $$ u \frac{\delta u}{\delta x} + v \frac{\delta u}{\delta y}  = - \frac{1}{\rho} \frac{\delta p}{\delta x} + \nu \left( \frac{\delta^{2} u }{ \delta x^{2} } + \frac{\delta^{2} u }{ \delta y^{2} } \right)  $$  
 We know there is no pressure gradient hence $\frac{\delta p}{\delta x}$ can be ignored, then we split the equation into it's components:
 $$\begin{align*}
u &\frac{\delta u}{\delta x} \to \frac{U^{2}}{\delta} & v &\frac{\delta u}{\delta y} \to \frac{U^{2}}{L}\\
\end{align*}$$