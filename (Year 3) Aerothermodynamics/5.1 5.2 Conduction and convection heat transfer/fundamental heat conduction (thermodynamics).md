---
aliases: ["Fourier's law","simple conduction"]
tags: []
---

## Fundamental heat conduction

### A bar connecting two reservoirs

For simple conduction, the equation's quite simple. For a constant material bar, there will be a linear temperature gradient between the resiviours with the rate of heat transfer being determined by thermal conductivity and rod geometry.

> ![[Pasted image 20231210134424.png]]
> ### $$\begin{align*} \dot{Q}  &= \frac{kA}{L} (T_{A} - T_{B})  \end{align*}$$
> ### $$\begin{align*} \dot{q}  &= \frac{k}{L} (T_{A} - T_{B})  \end{align*}$$
>> where:
>> $\dot{Q}=$ [[heat transfer rate]]
>> $\dot{q}=$ [[heat transfer rate|heat transfer rate per area]]
>> $k=$ [[material thermal conductivity|thermal conductivity]] of bar
>> $L=$ length of bar
>> $A=$ cross sectional area of bar

### Differential form ([[fundamental heat conduction (thermodynamics)|Fourier's law]])

Taking that bar equation, and assuming a separation $L=dx$:

$$\begin{align*}
\dot{q}  &= \frac{k}{L} (T_{A} - T_{B}) &&\to& \dot{q}  &= \frac{k}{dx} (-dT) &&\to& \dot{q}  &= -k\frac{dT}{dx}
\end{align*}$$

Derivation of the general case becomes trivial.

> ### $$\begin{align*} \dot{q}  &= -k \frac{dT}{dx}  \end{align*}$$
>> where:
>> $\dot{q}=$ [[heat transfer rate|heat transfer rate per area]]
>> $k=$ [[material thermal conductivity|thermal conductivity]] of bar
>> $\frac{dT}{dx}=$ thermal gradient

The sign indicates that heat transfer is in the opposite direction to the temperature gradient, which makes sense since it's from a hot place to a cold place.

A very general form also exists.

> ### $$\begin{align*} \dot{\vec{q}}  &= -k \nabla T  \end{align*}$$
>> where:
>> $\dot{q}=$ [[heat transfer rate|heat transfer rate per area]] vector
>> $k=$ [[material thermal conductivity|thermal conductivity]] of bar
>> $\nabla=$ [[del operator]]
>> $T=$ temperature [[scalar fields|scalar field]]

