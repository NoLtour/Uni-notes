---
aliases: [""]
tags: []
---

## Surface integral

Mmmmmm yes, [[you see it is funny because in reality it is the opposite of that|I love integration]].

### Equation

> ### $$\begin{align*} dA  &= \left| \frac{\delta\vec{r}}{\delta s} \times \frac{\delta\vec{r}}{\delta t} \right| d s \:d t\\ &= a  \:d s \:d t  \end{align*}$$
> ### $$\begin{align*}A=\int dA  &= \int\int\left| \frac{\delta\vec{r}}{\delta s} \times \frac{\delta\vec{r}}{\delta t} \right| d s \:d t\\ &=\int\int a  \:d s \:d t  \end{align*}$$
>> where:
>> $A=$  the [[surface integral]] of a [[defining surfaces|surface]]
>> $\vec{r}(s,t)=$ the [[defining surfaces|surface]]
>> $s,t=$ independent variables representing position on the surface
>> $a=\left| \frac{\delta\vec{r}}{\delta s} \times \frac{\delta\vec{r}}{\delta t} \right|=$ a thing that gets used in convention frequently
>> $\times=$ [[cross product (vectors)|cross product]]

Fuck yes, double integrals! ([[it did seem vector calculus wasnt that bad so far|I love these even more]])

### Theory

![[Pasted image 20221228001531.png]]

K it follows common integration logic, assume we're moving across the surface using really small increments of $s$ and $t$. The difference in position $\delta \vec{r}_{1}$ can be easily found by finding the vector between the points:
$$ \delta \vec{r}_{1} = \vec{r}(s+\delta t, \: t) - \vec{r}(s,t) $$
[[Taylor series|Taylors expansion theorem]] can be applied to $\vec r$ expanding to:
$$\begin{align*}
\vec{r}(s+\delta s, \: t) &= \vec{r}(s,t) + \delta s \frac{\delta \vec{r}}{\delta s}(s,t) + \frac{(\delta s)^{2}}{2} \frac{\delta^{2} \vec{r}}{\delta s^{2}}(s,t) + \frac{(\delta s)^{3}}{6} \frac{\delta^{3} \vec{r}}{\delta s^{3}}(s,t) + \:...\\
&=  \vec{r}(s,t) + \delta s \frac{\delta \vec{r}}{\delta s}(s,t) + O_1(s,t)\\
\delta \vec{r}_{1}&=  \delta s \frac{\delta \vec{r}}{\delta s}(s,t) + O_1(s,t)
\end{align*}$$
The exact same method can be applied for $\delta t$ which will get:
$$\begin{align*}
 \delta \vec{r}_{2}&=  \delta t \frac{\delta \vec{r}}{\delta t}(s,t) + O_{2}(s,t)
\end{align*}$$

Using the equation for the area of a parallelogram with sides $\delta \vec{r}_{1}$ and $\delta \vec{r}_{2}$ we get:
$$\begin{align*}
\delta A &= | \delta \vec{r}_{1} \times \delta\vec{r}_{2} | \\
&= \left| \left( \delta s \frac{\delta \vec{r}}{\delta s}(s,t) + O_{1}(s,t) \right) \times \left(\delta t \frac{\delta \vec{r}}{\delta t}(s,t) + O_{2}(s,t)\right) \right|\\
&= \left|  \delta s \delta t \frac{\delta \vec{r}}{\delta s} \times\frac{\delta \vec{r}}{\delta t}  + O_{1}\times \delta t \frac{\delta \vec{r}}{\delta t}  + O_{2}\times\delta s \frac{\delta \vec{r}}{\delta s} + O_{1}\times O_{2} \right|\\
&\approx  \left| \frac{\delta\vec{r}}{\delta s} \times \frac{\delta\vec{r}}{\delta t} \right|  \delta s \:\delta t
\end{align*}$$
The approximation becomes increasingly accurate as $\delta s$ and $\delta t$ approach zero.

### Examples

These are questions based on the surfaces defined as examples in [[defining surfaces]]:

![[Pasted image 20221228004735.png]]
![[Pasted image 20221228004748.png]]
