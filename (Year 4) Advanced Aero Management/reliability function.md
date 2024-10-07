---
aliases: ["RF"]
tags: []
---

## Reliability function

Reliability engineering concerns with the probability that an item will survive for a stated interval, i.e. that there is no failure in the interval ($0$ to $t_1$).

A reliability function is quite useful as it can be used to define exactly that, it's definitions also quite simple:

> ### $$\begin{align*} R(t) &= \text{NOT } F(t)  \end{align*}$$
> ### $$\begin{align*} R(t_{1})  &=  1 - F(t_{1}) \\&=  1 - \int^{t_{1}}_{-\infty} f(t) \cdot dt = \int^{\infty}_{t_{1}} f(t) \cdot dt \end{align*}$$
>> where:
>> $R(t)=$ the [[reliability function]] in terms of $t$
>> $F(t)=$ the [[cumulative distribution function]] in terms of $t$
>> $f(t)=$ the [[probability density function]] in terms of $t$
>> $t=$ some parameter, often time 

