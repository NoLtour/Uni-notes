---
aliases: [""]
tags: []
---

## [[Laplace transform]] of $\sin(ax)$

### Main bit

> ## $$ \mathcal{L}[\sin(ax)] = \frac{a}{s^{2}+a^{2}} $$ 
>> requires:
>> $s>0$
>
>> where:
>> $\mathcal{L}[...] =$ [[Laplace transform]] of a function
>> $a=$ some variable independent of $x$
>> $s=$ independent variable of [[Laplace transform]]
>> $x=$ independent variable of $\sin(ax)$

### Proof

$$\begin{align*}
\mathcal{L}[\sin(ax)] &= \int^{\infty}_{0} \sin(ax) e^{-sx} \cdot dx\\
&= \left[ \frac{1}{s} \sin(ax) e^{-sx} \right]^{\infty}_{0} + \int^{\infty}_{0} \frac{a}{s} \cos(ax) e^{-sx} \cdot dx\\
&= 
\end{align*}$$
