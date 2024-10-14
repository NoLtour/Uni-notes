---
aliases:
  - multivariate gaussian distribution
tags:
---

## Multivariate normal distribution

We can take the [[univariate models|univariate]] [[continuous distribution functions|gaussian distribution]] function, and get the generalised [[multivariate models|multivariate]] form:

> ### $$\begin{align*}  \text{Univariate:}&& f(x)  &= \frac{1}{\sigma \sqrt{2\pi}} \exp\left[-\frac{1}{2} \left(\frac{x-\mu}{\sigma}\right)^{2} \right] \\  \text{Multivariate:}&& f(\boldsymbol{x})  &= \frac{1}{\sqrt{(2\pi)^{p}\det\boldsymbol{\Sigma}}} \exp \left[-\frac{1}{2} (\boldsymbol{x} - \boldsymbol{\mu})^{T} \boldsymbol{\Sigma}^{-1} (\boldsymbol{x}-\boldsymbol{\mu}) \right]  \end{align*}$$
> ### $$\begin{align*}  \boldsymbol{x} &= \begin{pmatrix} x_{1}\\ x_{2}\\...\\x_{n} \end{pmatrix} &&& \boldsymbol{\mu} &= \begin{pmatrix} \mu_{1}\\\mu_{3}\\...\\\mu_{n} \end{pmatrix} &&&
\boldsymbol{\Sigma} &=\begin{bmatrix} \Sigma_{11} & \Sigma_{12} & \cdots & \Sigma_{1n} \\ \Sigma_{21} & \Sigma_{22} & \cdots & \Sigma_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ \Sigma_{n1} & \Sigma_{n2} & \cdots & \Sigma_{nn} \end{bmatrix} \end{align*}$$
>> where:
>> $f(...)=$ the [[probability density function]]
>> $x=$ some parameter
>> $\mu=$ location parameter, "[[mean value by integration|mean]]"
>> $\sigma=$ scaling parameter, "[[standard deviation for probabability functions|standard deviation]]"
>> $\boldsymbol{\Sigma}=$ gaussian [[covariance matrix]]

### Example [[probability density function|PDFs]]

#### Independent symmetric case
Here the parameters $x_1$ and $x_2$ hold no relation ([[independent events|independent]]). There isn't even a need to use [[multivariate models]] as the same could be produced using multiple [[univariate models]]. You can clearly tell this by seeing that the [[covariance matrix]] has zero's in all off diagonal entries.

![[Pasted image 20241012161816.png]]

Here is another, but the means shifted a bit:
![[Pasted image 20241012162001.png]]
#### Independent asymmetric case

Here, the variables are still independent, but the spreads of the variables are different. One has half the [[standard deviation for probabability functions|standard deviation]] of the other:

![[Pasted image 20241012162918.png]]

#### Dependent case (positive correlation)
Finally we have a case where the variables are dependent, here there is positive correlation, which can be seen graphically or in the [[covariance matrix]]'s of diagonals:

![[Pasted image 20241012163119.png]]

#### Dependent case (negative correlation)
![[Pasted image 20241012163144.png]]

### Example CDF
![[Pasted image 20241012163258.png]]

