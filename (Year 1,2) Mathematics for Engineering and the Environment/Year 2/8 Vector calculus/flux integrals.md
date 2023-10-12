---
aliases: ["vector element of area","flux integral"]
tags: []
---

## Flux integrals

### Equation

> ### $$\begin{align*}  \int\int_{S} \vec{F} \cdot  d\vec{S} &=  \int\int_{S} \left[\vec{F}(\vec{r}(s,t)) \cdot  \left( \frac{\delta\vec{r}}{\delta s} \times \frac{\delta\vec{r}}{\delta t} \right)\right] \: d s \:d t \end{align*}$$
>> where:
>> $\vec{F}=$  the [[vector fields|vector field]], when integrating is in terms of $s,t$
>> $d\vec{S}=\left( \frac{\delta\vec{r}}{\delta s} \times \frac{\delta\vec{r}}{\delta t} \right)d s \:d t=$ a thing that exists for convention
>> $\vec{r}(s,t)=$ the equation for position on the [[defining surfaces|surface]]
>>$s,t=$  independent variables for position on the surface
>>$\times=$ [[cross product (vectors)|cross product]]
>>$\cdot=$ [[dot product (vectors)|dot product]]
>>
>>Note that the order for the cross product matters! The order must be chosen such that the normal faces the appropriate direction relative to the surface!


### Bit more in depth theory

Though this sounds horrible it's not that complicated, basically it's measuring the magnitude of a vector field that is passing through a surface. If it was a velocity field for a fluid then it might be the cross section of a pipe to get flow.
The magnitude of the vector passing through the [[defining surfaces|surface]] is measured normal to the surface ($\vec{F}\cdot \hat{n}$) like so:
![[Pasted image 20221228120425.png]]

The integral can be written as:
$$\begin{align*}
\int\int_{S} \vec{F} \cdot \hat{n} \: dA
\end{align*}$$

There is something called the "vector element of area" which is $d\vec{S} = \hat{n}\:dA$, it's meaning is a vector of magnitude $dA$ and direction $\vec{n}$, used to clean up the equation above into:
$$\begin{align*}
\int\int_{S} \vec{F} \cdot  d\vec{S}
\end{align*}$$

This is just a pointless convention thing though, ok so back to the starting equation. It can be combined with the equation for $dA$ from [[surface integral#Equation]] to get:
$$\begin{align*}
&\int\int_{S} \vec{F} \cdot \hat{n} \: dA & dA  &= \left| \frac{\delta\vec{r}}{\delta s} \times \frac{\delta\vec{r}}{\delta t} \right| d s \:d t\\ 
&\int\int_{S} \vec{F} \cdot \hat{n} \: \left| \frac{\delta\vec{r}}{\delta s} \times \frac{\delta\vec{r}}{\delta t} \right| d s \:d t\\
&\int\int_{S} \left[\vec{F} \cdot  \left( \frac{\delta\vec{r}}{\delta s} \times \frac{\delta\vec{r}}{\delta t} \right)\right] \: d s \:d t\\
\end{align*}$$

This form can be evaluated, which is neat.
