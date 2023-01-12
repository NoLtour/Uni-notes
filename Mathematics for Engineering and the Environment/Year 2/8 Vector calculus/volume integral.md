---
aliases: ["volume integrals","the Jacobian","Jacobian"]
tags: []
---

## Volume integral
### Final equations
Read last.

> ### $$\begin{align*} \int\int\int_{V} f \:dV &= \int\int\int_{V} f(x,y,z)\:dx\:dz\:dy \\&= \int\int\int_{V} f(s,t,u) \:J \:ds\:dt\:du \end{align*}$$ 

> ### $$\begin{align*}J &= \frac{\delta(x,y,z)}{\delta(s,t,u)} = \begin{vmatrix} \frac{\delta x}{\delta s} & \frac{\delta x}{\delta t} & \frac{\delta x}{\delta u} \\  \frac{\delta y}{\delta s} & \frac{\delta y}{\delta t} & \frac{\delta y}{\delta u} \\ \frac{\delta z}{\delta s} & \frac{\delta z}{\delta t} & \frac{\delta z}{\delta u} \\ \end{vmatrix}  \end{align*}$$
>> where:
>> $J=$ [[volume integral|the Jacobian]] (for it's corresponding matrix $x,y,z$ are functions of $s,t,u$)
>> $f=$ some function being integrated inside the area
>> $s,t,u=$ any alternative coordinate system, often changes symbols as well to things such as $\theta$ 

Ok with all that hype it doesn't seem thaaat bad...

### Cartesian integration
This is very easy and intuitive, if we want to integrate some scalar function $f$ over some volume it's just:

$$\begin{align*}
\int\int\int_{V} f \:dV &= \int\int\int_{V} f(x,y,z)\:dx\:dz\:dy
\end{align*}$$

You thought that was it? ([[they are slowly combining it all together into one huge abomination|lmao]]) No it gets so much worse that this cute little triple integration.

The thing above is using cartesian coordinates, which is often inconvenient. Generally we will use an alternative coordinate system that is more suitable for the geometry we are dealing with.

### The Jacobian
So with that switching coordinate system idea, things become complicated so we have a general way to transform a volume integral between cartesian and some arbitrary coordinate system.

Start by defining $x,y$ and $z$ in terms of the new coordinates, for example $s,t,u$ like so:

$$\begin{align}x &= x(s,t,u)\\y &= y(s,t,u)\\z &= z(s,t,u)\end{align}$$

$$\begin{align*}
J &= \frac{\delta(x,y,z)}{\delta(s,t,u)} = \begin{vmatrix} \frac{\delta x}{\delta s} & \frac{\delta x}{\delta t} & \frac{\delta x}{\delta u} \\  \frac{\delta y}{\delta s} & \frac{\delta y}{\delta t} & \frac{\delta y}{\delta u} \\ \frac{\delta z}{\delta s} & \frac{\delta z}{\delta t} & \frac{\delta z}{\delta u} \\ \end{vmatrix}
\end{align*}$$

This can then be used to transform $dV$ which is useful for integration:

$$\begin{align*}
dV &= dx\:dz\:dy & &\to & dV &= \frac{\delta(x,y,z)}{\delta(s,t,u)} \:ds\:dt\:du\\
&& && &= \begin{vmatrix} \frac{\delta x}{\delta s} & \frac{\delta x}{\delta t} & \frac{\delta x}{\delta u} \\  \frac{\delta y}{\delta s} & \frac{\delta y}{\delta t} & \frac{\delta y}{\delta u} \\ \frac{\delta z}{\delta s} & \frac{\delta z}{\delta t} & \frac{\delta z}{\delta u} \\ \end{vmatrix}\:ds\:dt\:du
\end{align*}$$

So we have a general form for $dV$ in any coordinate system (eg spherical, cylindrical ect).
