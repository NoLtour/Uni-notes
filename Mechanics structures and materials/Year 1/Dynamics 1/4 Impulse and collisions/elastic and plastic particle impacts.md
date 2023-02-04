---
aliases: ["elastic impact","plastic impact"]
tags: ["Question","QFormat3"]
---

#### What are
## Elastic and plastic particle impacts
### Stuff
Basically take what you learned from [[modeling particle impacts]] more specifically [[coefficient of restitution]] and:
- $e=1$ means [[elastic and plastic particle impacts|elastic impact]]
- $0<e<1$ non elastic impact, some KE lost
- $e=0$ [[elastic and plastic particle impacts|plastic impact]], maximum energy dissipation (lots of KE loss), after the impact the particles stick together moving off with a single velocity

Heres the slide on how to solve these if you haven't figured it out already:
![[Pasted image 20220214120757.png]]

### Example
> Given the following situation:
> ![[Pasted image 20220214122237.png]]
> If balls a and b are the same density and $e$ is known and equal for all collisions write an expression for the max height A reaches, modelling both as particles. A is the smaller ball.

First we need an expression for velocity at the instant of impact with the ground as well as expressions for the mass of A and B:
$$\begin{align*}
v_{0} &= Hg & m_{A} &=  \frac{4\rho \pi r^{3}}{3} & m_{B} &=  \frac{4\rho \pi (kr)^{3}}{3}\\
\end{align*}$$

[[UNFINISHED LIGHT (tm)|UNFINISHED (LIGHT)]]:$v_{0} &= Hg$ is wrong, also recheck working

Now we find the momentum of B after it's impact with the ground, I'm taking $v_{0}$ as down and $v_{B1}$ as upward:
$$\begin{align*}
ev_{0}&= v_{B1}
\end{align*}$$

Now we can find the momentum of A from it's collision with B, I should draw a sketch but I'm assuming that A and B both move upwards after the collision (taking up as positive vel):
$$\begin{align*}
e(v_{B1} + v_{0}) &= v_{A2} - v_{B2}  & m_{B}v_{B1} + m_{A}v_{0} &= m_{B}v_{B2} - m_{A} v_{A2}\\
e(ev_{0} + v_{0}) &=  & m_{B}ev_{0} + m_{A}v_{0} &= m_{B}v_{B2} - m_{A} v_{A2}\\
e v_{0}(e + 1) &=   &  \frac{m_{B}ev_{0} + m_{A}v_{0} +  m_{A} v_{A2}}{m_{B}}&=v_{B2}\\
& & ev_{0}+\frac{ m_{A}(v_{0} + v_{A2})}{m_{B}}&=v_{B2}\\
e v_{0}(e + 1) &=v_{A2} -ev_{0}-\frac{ m_{A}(v_{0} + v_{A2})}{m_{B}}  \\
e v_{0}(e + 1) &=v_{A2}- ev_{0}-\frac{ m_{A}v_{0} }{m_{B}} -\frac{ m_{A} v_{A2}}{m_{B}} \\
e v_{0}(e + 1) + \frac{ m_{A}v_{0} }{m_{B}} + ev_{0} &= v_{A2}-\frac{ m_{A} v_{A2}}{m_{B}}  \\
e v_{0}(e+2 ) + \frac{ m_{A}v_{0} }{m_{B}}  &= v_{A2}-\frac{ m_{A} v_{A2}}{m_{B}} & \frac{m_{A}}{m_{B}}&=\frac{4\rho \pi r^{3}}{3}/\frac{4\rho \pi (kr)^{3}}{3}\\
& & &=\frac{1}{k^{3}}\\
e v_{0}(e+2 ) + \frac{ v_{0} }{k^{3}}  &= v_{A2}-\frac{  v_{A2}}{k^{3}}\\
v_{0} \frac{e (e+2 ) + \frac{ 1 }{k^{3}}}{ 1-1/k^{3} }  &= v_{A2} \\
gH \frac{ek^{3} (e+2 ) + 1}{ k^{3}-1 }  &= v_{A2} 
\end{align*}$$
Now finally we can use the equation $h = \frac{v^{2}}{2g}$:
$$\begin{align*}
h_{max} &= \frac{\left(gH \frac{ek^{3} (e+2 ) + 1}{ k^{3}-1 }\right)^{2}}{2g} \\
h_{max} &=   \frac{g}{2} \left(H \frac{ek^{3} (e+2 ) + 1}{ k^{3}-1 }\right)^{2} \\
\end{align*}$$
Not 100% sure if that's right but, you get the point... the maths is doable using the methods layed out. In reality these equations work for plastic and elastic collisions, you only really need to care about that if you want to simplify your equations.