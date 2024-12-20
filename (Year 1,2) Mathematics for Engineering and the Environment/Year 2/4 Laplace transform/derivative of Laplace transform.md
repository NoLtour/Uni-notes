---
aliases: [""]
tags: []
---

([[no you will do maths work|I want to go to sleep]])

## Derivative of Laplace transform

### Equation

> ## $$ \mathcal{L}[xf(x)] = - \frac{d\tilde{f}}{ds}  $$ 
> ## $$ \mathcal{L}[xf(x)] = - \frac{d }{ds} \mathcal{L}[f(x)]  $$ 
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
&&&\text{since s and x are independent you can do the following}\\
\frac{d\tilde{f}}{ds} &= \int^{\infty}_{0} f(x) \left(e^{-sx} \frac{d}{ds}\right) \cdot dx\\
 &= \int^{\infty}_{0} f(x) (-xe^{-sx}) \cdot dx\\
 &= -\int^{\infty}_{0} (xf(x)) e^{-sx} \cdot dx\\
 &= -\mathcal{L}[xf(x)]
\end{align*}$$
