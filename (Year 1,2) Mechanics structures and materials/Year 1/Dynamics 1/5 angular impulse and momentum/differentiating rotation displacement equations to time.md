---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Differentiating rotation displacement equations to time
Might have this somewhere else in my notes as well buy a bit of redundancy's fine:

> ### $$ v = \omega \frac{dx}{d\theta} $$ 
>> where:
>> $v=$ velocity
>> $\omega=$ angular velocity
>> $\theta=$ angle
>> $x=$ displacement

### Example
> Write an expression for $v$ in terms of $\theta$ for:
> ![[Pasted image 20220503150953.png]]

First displacement angle equation is ezz:
$$\begin{align*}
x &= l \cos \theta 
\end{align*}$$
Now just differentiate to get $v$:
$$\begin{align*}
v &= -l\sin\theta
\end{align*}$$
IS WRONG! because in reality:
$$\begin{align*}
x &= l \cos \theta \\
\frac{dx}{d\theta} &= -l \sin \theta
\end{align*}$$
So this is where you use the equation above to get from $\frac{dx}{d\theta}$ to $\frac{dx}{dt}$:
$$\begin{align*}
\frac{dx}{d\theta} &= -l \sin \theta & v &= \omega \frac{dx}{d\theta}\\
& & &= - \omega l \sin\theta
\end{align*}$$