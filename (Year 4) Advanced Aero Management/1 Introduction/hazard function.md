---
aliases: ["HF","hazard rate"]
tags: []
---

## Hazard function

This is the function for the probability density of occurrence, given it hasn't occurred previously (hence it's a [[probability convention for advanced management|conditional probability]]). It's written as:

> ### $$\begin{align*} h(t)  &= \frac{f(t)}{R(t)} = \frac{f(t)}{1-F(t)} \end{align*}$$
>> where:
>> $h(t)=$ the [[hazard function]] in terms of $t$ 
>> $R(t)=$ the [[reliability function]] in terms of $t$
>> $F(t)=$ the [[cumulative distribution function]] in terms of $t$
>> $f(t)=$ the [[probability density function]] in terms of $t$
>> $t=$ some parameter, often time 

This can be thought of as the probability of imminent failure at t or an indicator of the “proneness” to failure after t, it's very useful when dealing with components that are in operation.
