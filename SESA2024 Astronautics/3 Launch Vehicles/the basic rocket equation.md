---
aliases: ["the rocket equation","basic rocket equation","rocket equation"]
tags: []
---

## The (basic) rocket equation

[[rocket science|Hey it's the thing! We made it to the thing!]]

### The equation

> ### $$ \Delta V = V_{ex} \ln\left( \frac{M_{0}}{M_{b}} \right) $$ 
> ### $$ V = V_{ex} \ln\left( \frac{M_{0}}{M} \right) + V_{0} $$ 
> ### $$ T=\sigma V_{ex} $$ 
>> where:
>> $V=$ current rocket velocity
>> $V_{ex}=$ exhaust velocity (constant)
>> $M_{0}=$ initial rocket mass
>> $M_{b}=$ final rocket mass
>> $M=$ current mass
>> $V_{0}=$ initial rocket velocity
>> $T=$ thrust
>> $\sigma= \frac{dm}{dt}=$ mass flow rate of exhaust

The equation's quite simple, it just represents how much push you get for the stuff you throw below you. No matter how fancy your propulsion method this equation is what enables all rockets to move (unless your some sort of [[space boat cringe|cringe solar sail]]).

### The proof

Pretty simple proof ngl:

![[Pasted image 20221022171006.png]]

We know a few things:
- The mass expelled can be defined as mass flow rate $Q= -\frac{dM}{dt}$ which is also mass lost from the rocket
- At the instant of expulsion the relative velocity of the exhaust is $V_{ex}$ (modelling it as constant)
- The impulse that accelerates the exhaust has an equal and opposite effect on the rocket $\frac{dV}{dt} M = Q V_{ex}$

Then it's as simple as combining and integrating:

$$\begin{align*}
\frac{dV}{dt} M &= Q V_{ex} & Q= -\frac{dM}{dt}\\
\frac{dV}{dt} M &= -\frac{dM}{dt} V_{ex}\\
\int^{V}_{V_0} dV &= -V_{ex} \int^{M}_{M_{0}}  \frac{1}{M} dM \\
V - V_{0} &= -V_{ex} \ln \frac{M}{M_{0}} \\
V &= V_{ex} \ln \frac{M_{0}}{M} + V_{0} \\
\end{align*}$$

Also note that $\frac{dV}{dt} M  = -\frac{dM}{dt} V_{ex}$ can be written as $T=\sigma V_{ex}$ where $\sigma$ is mass expelled and $T$ is thrust.
