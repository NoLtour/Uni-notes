---
aliases: [""]
tags: []
---

## Laplace transform

> ### $$ \mathcal{L}[f(x)] \equiv \tilde{f}(s) = \int^{\infty}_{0} f(x) e^{-sx} \cdot dx $$ 
>> where:
>> $\mathcal{L}[...]=$ [[Laplace transform]] function
>> $\tilde{f}(s)=$ [[Laplace transform]] of $f(x)$
>> $s=$ frequency, independent variable of [[Laplace transform]]
>> $f(x)=$ some function
>> $x=$ independent variable of function being transformed

Similar to the [[defining the fourier series|Fourier series]] the [[Laplace transform]] does not exist for all functions or values of $s$.  Clearly when substituting into the transform above, if the function multiplied by $e^{-sx}$ tends to infinity at limit infinity there will not be a valid [[Laplace transform]]. ([[example of invalid transform|example seen here]])

### Condition of a Laplace transform

If $f(x)$ is bounded by an exponential $e^{ax}$ 
