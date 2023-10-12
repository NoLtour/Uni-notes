---
aliases: ["fourier transform","inverse fourier transform"]
tags: []
---

## Fourier transforms

### The equation

Unlike [[defining the fourier series|Fourier series]] which is for repeating things, the fourer transform is for non periodic functions. Simular to how a fourer series can only be found if it obeys the [[fouriers theorem|dirichlet conditions]] for a [[fourier transforms|fourier transform]] to exist it's input function must obey the following conditions:
- $f(t)$ is bounded (it does not go to infinity)
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

### Example

> Find the fourier transform of $f(t)=\begin{dcases} 1, & |t|<1 \\ 0, &else \end{dcases}$

$$\begin{align*}
\mathcal{F}[f(t)] &= \frac{1}{\sqrt{2\pi}} \int^{\infty}_{-\infty} f(t) e^{-j\omega t} \cdot dt 
\end{align*}$$

Since for this function it is zero outside of $-1<x<1$ we can simplify the equation to:

$$\begin{align*}
\mathcal{F}[f(t)] = F(\omega)&= \frac{1}{\sqrt{2\pi}} \int^{-1}_{-\infty}0e^{-j\omega t} \cdot dt + \frac{1}{\sqrt{2\pi}} \int^{1}_{-1} 1 e^{-j\omega t} \cdot dt + \frac{1}{\sqrt{2\pi}} \int^{\infty}_{1} 0 e^{-j\omega t} \cdot dt \\
  &=  \frac{1}{\sqrt{2\pi}} \int^{1}_{-1} e^{-j\omega t} \cdot dt & \sin \omega &= \frac{1}{2j }( e^{j\omega} - e^{-j\omega} )   \\
  &=  \frac{1}{j\omega\sqrt{2\pi}} [ e^{-j\omega t} ]^{1}_{-1} & \sin \omega &= j \frac{1}{2}( e^{-j\omega} - e^{j\omega} ) \\
&= \sqrt{\frac{2}{\pi}} \frac{\sin(\omega)}{\omega}\\
\end{align*}$$

Visualised, you can see the red line representing the frequency distribution, while the blue line is a reconstruction of the original function based off that frequency distribution:
![[Pasted image 20221026180916.png]]
As can be seen the blue is not 100% accurate as it is a sum within limited bounds, aka an approximation.
![[Pasted image 20221026181414.png]]

