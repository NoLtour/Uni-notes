---
aliases: ["CDF"]
tags: []
---

## Cumulative distribution function

The [[cumulative distribution function]] is just the integrated form of a [[probability density function]]:

> ### $$\begin{align*} F(t) &= \int^{t_{1}}_{-\infty} f(t) \cdot dt \end{align*}$$
>> where:
>> $F(t)=$ the [[cumulative distribution function]] in terms of $t$
>> $f(t)=$ the [[probability density function]] in terms of $t$
>> $t=$ some parameter, often time 

This is the probability that the measured value falls between $-\infty$ and $t_{1}$, put in human terms: "if we're describing the failure of a part over time, it's the chances that a part has failed before $t_{1}$." As you can imagine, this thing is [[the annoying thing about stats is its really fucking useful|used all over the place]] in lifetime predictions.
As discussed in [[probability density function]], for it to have meaning we generally integrate it. Which is exactly what we do here. Below is it visualised, the red curve is the [[cumulative distribution function|CDF]]:

![[Pasted image 20241007102059.png]]

