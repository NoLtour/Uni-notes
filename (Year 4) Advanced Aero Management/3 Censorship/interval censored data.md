---
aliases:
  - MLE with interval censored data
tags:
---

## Interval censored data

This is where over some interval there exists data, but the exact value of the data is only known to fall within a set range. 

For example, if we check the number of failed components from some set being tested once every 10 hours, our data would be interval censored and look like:
![[Pasted image 20241018164524.png]]


In reality all data is interval censored, since no measurement method has infinite resolution, of course above a certain resolution there's negligible difference between treating it as if it is actually continuous.

### [[maximum likelihood estimation|MLE]] with interval censored data

The process is quite simple, we take the basic [[maximum likelihood estimation|MLE]] equation, and multiply it by the probability that an occurance happened in that interval. 

![[Pasted image 20241018165615.png]]

The of occurrence over an interval is trivial, just take the [[cumulative distribution function|CDF]] and subtract the beginning value from the end value:

$$\begin{align*}
P(T_{I,lb} < t < T_{I,ub}) &= P(T_{I,lb} < t)\land P( t< T_{I,ub})
&&\to& P(T_{I,lb} < t < T_{I,ub}) &= F(T_{ub}) - F(T_{lb})
\end{align*}$$

Slapping that into the [[maximum likelihood estimation|MLE]]:

$$\begin{align*} l(\theta) = \log L(\theta) &=  \log \left[ \left(\prod^{n}_{i=1} f(t_{i} ; \theta)\right) \left(\prod^{n}_{i=1} F(T_{ub};\theta) - F(T_{lb};\theta)\right) \right]\\ &=\left[\sum\limits^{n}_{i=1} \log f(t_{i} ; \theta) \right] + \left[\sum\limits^{n}_{i=1} \log F(T_{ub};\theta) - F(T_{lb};\theta) \right]\end{align*}$$


