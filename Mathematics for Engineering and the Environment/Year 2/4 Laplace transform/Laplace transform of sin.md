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
& & \lim_{s\to\infty} \frac{1}{s} \sin(ax) e^{-sx} & = 0 \:\:\text{when } s>0 \\
&= \int^{\infty}_{0} \frac{a}{s} \cos(ax) e^{-sx} \cdot dx\\
&= \left[- \frac{a}{s^{2}} \cos(ax) e^{-sx} \right]^{\infty}_{0} - \frac{a^{2}}{s^{2}} \int^{\infty}_{0} \sin(ax)e^{-sx}\cdot dx\\
&= \left[- \frac{a}{s^{2}} \cos(ax) e^{-sx} \right]^{\infty}_{0} - \frac{a^{2}}{s^{2}} \mathcal{L}[\sin(ax)]\\
& & \lim_{s\to\infty} - \frac{a}{s^{2}} \cos(ax) e^{-sx}& = 0 \:\:\text{when } s>0 \\
&= \frac{a}{s^{2}} - \frac{a^{2}}{s^{2}} \mathcal{L}[\sin(ax)]\\
&...\\
\mathcal{L}[\sin(ax)] &= \frac{s^{2}}{a^{2}+s^{2}} \frac{a}{s^{2}}\\
&= \frac{a}{s^{2}+a^{2}}
\end{align*}$$
