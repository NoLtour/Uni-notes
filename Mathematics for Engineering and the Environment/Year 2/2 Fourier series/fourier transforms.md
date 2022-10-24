---
aliases: ["fourier transform","inverse fourier transform"]
tags: []
---

## Fourier transforms

### The equation

Unlike [[defining the fourier series|Fourier series]] which is for repeating things, the fourer transform is for non periodic functions. Simular to how a fourer series can only be found if it obeys the [[fouriers theorem|dirichlet conditions]] for a [[fourier transforms|fourier transform]] to exist it's input function must obey the following conditions:
- $f(t)$ is bounded ()
- $\int^{\infty}_{-\infty} |f(t)|\cdot dt \neq \infty$ (function must have finite area)
- $f(t)$ has a finite number of extrema and discontinuities.

> ### $$ \text{Fourier Transform:} \:\:\:\:\:\:\:\:\: F(\omega) \equiv \mathcal{F}[f(t)] = \frac{1}{\sqrt{2\pi}} \int^{\infty}_{-\infty} f(t) e^{-j\omega t} \cdot dt $$ 
> ### $$ \text{Inverse Transform:} \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:  f(t) = \frac{1}{\sqrt{2\pi}} \int^{\infty}_{-\infty} F(\omega) e^{j\omega t} \cdot d\omega $$ 
>> where:
>> $f(t)=$ some input function of $t$
>> $F(\omega)=$ the fourier transform of $f(t)$
>> $j=\sqrt{-1}$
>> $\omega=$ frequency
>> $\mathcal{F}[...]=$ fourier transform of some function 


