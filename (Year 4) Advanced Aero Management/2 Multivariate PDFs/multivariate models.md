---
aliases:
  - multivariate model
  - multivariate
tags:
---

## Multivariate models

Multivariate models are used when we have a set of factors that are not [[independent events|independent]]. Generally in these cases, it becomes too complex to model analytically and derive a closed form solution, hence requiring numerical approaches. 

If we plotted a [[multivariate models|multivariate model]], 2D [[continuous distribution functions|gaussian distribution]], it may look like:

![[Pasted image 20241012154444.png]]
#### Calculating total chance

Since they are not [[independent events|independent]] we can't just string together a few [[univariate models]], now our functions are something like $f(x,y)$. If we were to plot the [[cumulative distribution function|CDF]] of a [[multivariate models|multivariate model]] it may looks something like:
![[Pasted image 20241012152558.png]]

Note here the model shown has 2 variables, so we can visualise it in 2D. Up to 3D it's still not so hard to visualise, but you can imagine thing's become difficult fast [[good luck visualising a 6D space|lol]]. To calculate the probability that failure exists in those 2D bounds we would imply sub divide it into rectangles and subtract the extra regions:

$$\begin{align*}
F(a_{1}<x<b_{1},\:a_{2}<y<b_{2}) &=  F(b_{1},b_{2}) - F(a_{2},b_{2}) - F(b_{1},a_{2}) + F(a_{1}, a_{2})
\end{align*}$$

Recall this is because $F$ is the [[cumulative distribution function]]. This approach also works for higher dimensions, but obviously becomes longer.

### Deriving the [[cumulative distribution function|CDF]]

Derivation of a [[cumulative distribution function|CDF]] is quite intuitive, we basically just integrate it in more axes. For example:

> ### $$\begin{align*} \text{Univariate:}&&& f(x_{1}) &&\to &F(a) &= \int^{a}_{-\infty} f(x_{1}) \cdot dx \\ \text{Multivariate (2D):}&&& f(x_{1},x_{2}) &&\to &F(a,b) &= \int^{a}_{-\infty}\int^{b}_{-\infty} f(x_{1},x_{2}) \cdot dx_{1} \: dx_{2} \end{align*}$$
>> where:
>> $F(...)=$ the [[cumulative distribution function]]
>> $f(...)=$ the [[probability density function]]
>> $a,b=$ bounds of [[cumulative distribution function]]
>> $x_{n}=$ some parameter

Obviously, the [[cumulative distribution function]] is 1 when it's bounds are all infinity, this occurs regardless of the number of variables.



