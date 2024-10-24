---
aliases: ["first shift theorem for LT","first shift theorem"]
tags: []
---

## First shift theorem for [[Laplace transform]]

### Theorem

> ## $$ \mathcal{L}[e^{-ax}f(x)] = \tilde{f}(s+a) $$ 
>> where:
>> $a=$ some constant
>> $\mathcal{L}=$ [[Laplace transform]] function
>> $\tilde{f}(s+a)=$ [[Laplace transform]] of $e^{-ax}f(x)$

### Proof

$$\begin{align*}
\mathcal{L}[e^{-ax}f(x)] &= \int^{\infty}_{0} f(x) e^{-ax} e^{-sx} \cdot dx\\
 &= \int^{\infty}_{0} f(x) e^{-(a+s)x} \cdot dx\\
 &=  \tilde{f}(s+a)\\
\end{align*}$$

Pretty [[super ez|ez]]

### Example

> Find the [[Laplace transform]] of $f(x)=e^{-4x}\sin(3x)$

We know from [[Laplace transform of sin]]:
 $$ \mathcal{L}[\sin(ax)] = \frac{a}{s^{2}+a^{2}} $$ 
So if we apply [[first shift theorem for Laplace transform|first shift theorem]] we know that:
 $$\begin{align*}
\mathcal{L}[e^{-4x}\sin(ax)] &= \frac{a}{(s+4)^{2}+a^{2}}\\
\mathcal{L}[e^{-4x}\sin(3x)] &= \frac{3}{(s+4)^{2}+9}
\end{align*}$$