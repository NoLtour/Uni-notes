---
aliases: [""]
tags: []
---

## Line integral of a vector field
### The method
Integration is the same as normal, just makes use of [[dot product (vectors)|dot product]] (converts the vector to a scalar), redefining $\vec{F}(x,y,z)$ as a function of $t$ by using the given equation of the [[formal definition of a parametric curve|curve]], then we can integrate after applying [[integration using the general composite rule#^11dcf7|integration by substitution]].

> ### $$\begin{align*} \vec{r}(t) &= v_{x}(t)i + v_{y}(t)j + v_{z}(t)k & & \:\:\:\:t_{0}\leq t\leq t_{1} \end{align*}$$
> ### $$\begin{align*} x:\vec{r}(t) &= v_{x}(t) & y:\vec{r}(t) &= v_{y}(t) & x:\vec{r}(t) &= v_{z}(t)   \end{align*}$$ 
> $$ $$
> ### $$\begin{align*} \vec{F}(x,y,z) &= f_{x}(x,y,z) i + f_{y}(x,y,z) j + f_{z}(x,y,z) k & &\to & \vec{F}(r(t)) &= f_{x}(v_{x},v_{y},v_{z}) i + f_{y}(v_{x},v_{y},v_{z}) j + f_{z}(v_{x},v_{y},v_{z}) k  \\&&&&&= f_{x}(t) + f_{y}(t) + f_{z}(t) \end{align*}$$
> $$ $$
> ### $$\begin{align*} \int_{C}\vec{F} \cdot d\vec{r} &= \int^{t_{1}}_{t_{0}} \left[\vec{F}(r(t))\cdot \frac{d\vec{r}}{dt}\right] dt \\ &= \int^{t_{1}}_{t_{0}} \left[ f_{x}(t) \frac{dv_{x}(t)}{dt} + f_{y}(t) \frac{dv_{y}(t)}{dt} + f_{y}(t) \frac{dv_{y}(t)}{dt} \right] dt \end{align*}$$
>> where:
>> [[dot product (vectors)|dot product]] is used
>> $\vec{F}=$ some function
>> $\vec{r}(t)=$ the function of the [[formal definition of a parametric curve|curve]]
>> $t_{0},t_{1}=$ limits of the curve $\vec{r}$
>> 

^da24c6

It looks kinda complex but it's really not, just look at this [[line integral of a vector field#Example]].

### Work done
If we have a [[vector fields|vector field]] that represents the force acting on a body at some point in space then it is really easy to define the [[work done in dynamics|work done]] by that body along the path taken $\vec{r}(t)$:
$$ W = \int^{b}_{a} \vec{F}(t) \cdot \frac{d\vec{r}}{dt}dt = \int^{b}_{a} \vec{F}(t) \cdot  d\vec{r} $$
It's obvious that even in the case where the start and end of $\vec{r}$ are the same, you can get 2 different values of work done depending on path taken:
![[Pasted image 20221122144659.png]]
In the special case where the path doesn't matter as long as  the end points are the same, we call that the [[conservative force|conservative case]].

### Example

> Solve:
> $$ \int_{C}\vec{F}\cdot d\vec{r} $$
> Where: 
> - $\vec{F}=(y+2)i+xj$ 
> - $\vec{r}(t)=(\sin t)i+(\cos t)j$ 
> - $0\leq t \leq \frac{\pi}{2}$

K so this is just using all the info from [[line integral of a vector field#^da24c6]], lets start by defining $\vec{F}(t)$:

$$\begin{align*}
\vec{r}(t)&= (\sin t)i+(\cos t)j
\end{align*}$$
$$\begin{align*}
x:\vec{r}(t)&= \sin t & y:\vec{r}(t)&= \cos t
\end{align*}$$
Subbing this into $\vec{F}(x,y)$:
$$\begin{align*}
 \vec{F}(x,y)&= (y+2)i+xj & &\to & \vec{F}(t)&= (\cos t+2)i+(\sin t)j
\end{align*}$$
Then we need $\frac{d\vec{r}}{dt}$ which is easy it's just deriving everything with respect to $t$:
$$\begin{align*}
\vec{r}(t)&= (\sin t)i+(\cos t)j &\to& & \frac{d\vec{r}}{dt}&= (\cos t)i-(\sin t)j
\end{align*}$$
Finally sub this into the formula for the integral:
$$\begin{align*}
\int_{C}\vec{F} \cdot d\vec{r} &= \int^{t_{1}}_{t_{0}} \left[\vec{F}(r(t))\cdot \frac{d\vec{r}}{dt}\right] dt\\
&= \int^{\frac{\pi}{2}}_{0} [ (\cos t+2)i+(\sin t)j ] \cdot [ (\cos t)i-(\sin t)j ] dt\\
&= \int^{\frac{\pi}{2}}_{0} [ \cos^{2} t+2\cos t-\sin^{2} t ] dt\\
&= \left[ \frac{1}{2} \sin 2t + 2\sin t \right]^{\frac{\pi}{2}}_{0}\\
&= 2
\end{align*}$$