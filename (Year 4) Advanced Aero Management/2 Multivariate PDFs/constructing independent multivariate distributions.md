---
aliases: [""]
tags: []
---

## Constructing independent multivariate distributions

Doing so for the [[cumulative distribution function|CDF]] is trivially easy, you just multiply them together. The problem comes if you want to then recover the [[probability density function|PDF]]:

> ### $$\begin{align*} F(x_{1} , x_{2} ... x_{n})  &=  \prod^{n}_{i=1} F_{i}(x_{i}) \end{align*}$$
> ### $$\begin{align*} f(x_{1} , x_{2} ... x_{n})  &=  \frac{\partial^{n} F}{\partial x_{1} \partial x_{2} ... \partial x_{n}} \end{align*}$$
>> where:
>> $F(...)=$ [[cumulative distribution function]]
>> $f(...)=$ [[probability density function]]
>> $x=$ some variable

Recovering the [[probability density function|PDF]] isn't that hard, since this is only partial differentiation, but if you've got lots of variables it'll be loooooong.

### Bivariate [[continuous distribution functions|exponential distribution]]

Effectively this is just [[multivariate normal distribution#Independent asymmetric case]], there is no correspondence between our variables. If we wanted to construct a [[cumulative distribution function|CDF]] for a [[continuous distribution functions|exponential distrobution]] from two functions:

$$\begin{align*}
F_{1}(x_{1}) &= 1- e^{-\lambda_{1} x_{1}} &&& F_{2}(x_{2}) &= 1- e^{-\lambda_{2} x_{2}}
\end{align*}$$

Then it would be trivial, we just multiply them together:

$$\begin{align*}
F(x_{1},x_{2}) &= (1- e^{-\lambda_{1} x_{1}} ) (1- e^{-\lambda_{2} x_{2}})
\end{align*}$$

Plotting the CDF we get:

![[Pasted image 20241012172856.png]]

