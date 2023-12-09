---
aliases:
  - simple lag
  - simple lead
  - quadratic lead
  - quadratic lag
  - loop gain function
tags:
---

## Sinusoidal loop gain function factors

Something that get's skimmed over is that we are now working with [[fourier transforms|fourier transformed]] things, instead of [[Laplace transform]]ed things... not sure if that's actually needed knowledge but it's got [[it is not even on the slides just a comment in lectures|something]] to do with the new layouts.

The general form the sinusoidal loop gain function is defined:

> ### $$\begin{align*} \text{With integrators:}&& G_{c}GH  &=  \frac{K}{(j\omega)^{n}} \frac{S_{1}S_{2}...\:Q_{1}Q_{2}...}{S_{k+1} S_{k+2} ...\: Q_{l+1} Q_{l+2}...} \\\\ \text{With differentiators:}&& G_{c}GH  &=  K(j\omega)^{n} \frac{S_{1}S_{2}...\:Q_{1}Q_{2}...}{S_{k+1} S_{k+2} ...\: Q_{l+1} Q_{l+2}...} \end{align*}$$
> ### $$\begin{align*} S_{i} &= j\omega T_{i} + 1 & Q_{i}&= \left(\frac{j\omega}{\omega_{ni}}\right)^{2} + 2 \zeta_{i}  \frac{j\omega}{\omega_{ni}} + 1\end{align*}$$
>> where:
>> $G_{c}GH =$ loop gain function
>> $K=$ [[linear system sinusoidal response|sinusoidal gain]]
>> $S_{i}=$ a simple lead
>> $\frac{1}{S_{i+k}}=$ a simple lag
>> $T_{i}=$ the simple lead/lags time constant
>> $Q_{i}=$ a quadratic lead
>> $\frac{1}{Q_{i+l}}=$ a quadratic lag
>> $\omega_{ni}=$ the quadratic lead/lags natural frequency
>> $\zeta_{ni}=$ the quadratic lead/lags damping ratio
