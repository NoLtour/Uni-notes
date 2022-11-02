---
aliases: [""]
tags: []
---

([[no you will do maths work|I want to go to sleep]])

## Derivative of Laplace transform

### Equation

> ## $$ \mathcal{L}[xf(x)] = - \frac{d\tilde{f}}{ds}  $$ 
>> where:
>> $\mathcal{L}[...]=$ [[Laplace transform]] function
>> $\tilde{f}(s)=$ [[Laplace transform]] of $f(x)$
>> $s=$ frequency, independent variable of [[Laplace transform]]
>> $f(x)=$ some function of $x$
>> $x=$ independent variable of function being transformed

### Proof

$$\begin{align*}
 \tilde{f}(s) &= \int^{\infty}_{0} f(x) e^{-sx} \cdot dx\\
 \frac{d\tilde{f}}{ds} &= \frac{d}{ds} \int^{\infty}_{0} f(x) e^{-sx} \cdot dx\\
\end{align*}$$
