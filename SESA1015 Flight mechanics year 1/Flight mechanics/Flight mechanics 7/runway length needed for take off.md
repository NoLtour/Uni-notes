---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you find the
## Runway length needed for take off
### Equation

![[Pasted image 20211124134849.png]]

This is basically just the distance needed to accelerate up to [[screen speed]] from rest.

> ### $$ s_1 = \frac{1.44 }{\left(\frac{T}{W} - \mu\right)\rho S C_{Lmax} } \frac{W}{g} $$ 
> ### $$ s_1 = \frac{(V_2)^{2}}{2g\left(\frac{T}{W} - \mu\right) } $$
>> where:
>> $T=$ Thrust
>> $W=$ Weight
>> $\mu=$ resistance due to runway friction
>> $s_1=$ Ground run distance

Also note that this equation assumes there is no wind and that the runway is level, but in reality you could get a shorter runway length required by taking off downhill against the wind.

#### Implications

So this tells us that to minimise runway length we need to:
- minamise weight
- maxamise air density
- get a high $C_{Lmax}$
- have a high thrust to weight ratio
- minimise $\mu$ (the runway friction)
- maxamise $S$

### Proof
![[Pasted image 20211124132645.png]]

We can use these forces to find the acceleration of the aircraft and it's velocity over the length of the runway:

$$\begin{align*}
   (T-D) - \mu(W-L) &= m \frac{dV}{dt} & \frac{W}{g} &= m \\
(T-D) - \mu(W-L) &= \frac{W}{g} \frac{dV}{dt} \\
\frac{T}{W} - \frac{D}{W} - \mu\frac{W-L}{W} &= \frac{1}{g} \frac{dV}{dt} & & & V\frac{dV}{dx} &= \frac{dV}{dt}\\
\frac{T}{W} - \frac{D}{W} - \mu\left(1-\frac{L}{W}\right) &= \frac{V}{g} \frac{dV}{dx}
\end{align*}$$

To find the take off distance to reach the [[screen speed]] the values of L and D must be substituted in the equation of motion which must then be integrated from 0 to [[screen speed]]. An approximate estimate of the distance can be found by making the following assumptions:
- $\frac{T}{W}=constant$, this is basically true since total fuel loss is usually minimal and thrust is roughly constant
- $\frac{D}{W} \approx 0$ and $\frac{L}{W} \approx 0$, this works since the relative values of $L,D$ are small compared to $W$ prior to lift off.

Using these assumptions on the previous equation:
$$\begin{align*}
\frac{T}{W} -0- \mu\left(1-0\right) &= \frac{V}{g} \frac{dV}{dx}\\
\frac{T}{W} - \mu &= \frac{V}{g} \frac{dV}{dx}\\
\int^{s_1}_0 \frac{T}{W} - \mu\cdot dx&= \int^{V_2}_0 \frac{V}{g} \cdot dV\\
\left[x \frac{T}{W} - \mu x\right]^{s_1}_0 &=  \left[\frac{V^{2}}{2g} \right]^{V_2}_0\\
s_1 \frac{T}{W} - \mu s_1 - 0 &= \frac{(V_2)^{2}}{2g} - 0\\
s_1 &= \frac{\frac{(V_2)^{2}}{2g}}{\frac{T}{W} - \mu }\\
&= \frac{(V_2)^{2}}{2g\left(\frac{T}{W} - \mu\right) }
\end{align*}$$

We can take $V_2$ ([[screen speed]]) as $V_2 = 1.2 V_s$ and use $C_{Lmax}$:

$$\begin{align*}
& & V_2 &= 1.2 V_s & \sqrt\frac{2W}{\rho S C_{Lmax}} &= V_s\\
s_1 &= \frac{(V_2)^{2}}{2g\left(\frac{T}{W} - \mu\right) } & V_2 &= 1.2 \sqrt\frac{2W}{\rho S C_{Lmax}}\\
s_1 &= \frac{(1.2 \sqrt\frac{2W}{\rho S C_{Lmax}})^{2}}{2g\left(\frac{T}{W} - \mu\right) }\\
s_1 &= \frac{1.2^{2} \frac{2W}{\rho S C_{Lmax}} }{2g\left(\frac{T}{W} - \mu\right) }\\
s_1 &= \frac{1.44 }{\left(\frac{T}{W} - \mu\right)\rho S C_{Lmax} } \frac{W}{g}
\end{align*}$$