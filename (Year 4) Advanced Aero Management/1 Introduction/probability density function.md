---
aliases: ["PDF","probability density functions","PDFs"]
tags: []
---

## Probability density function

If we take a [[frequency histogram|histogram]] with infinite samples, then keep decreasing the bin size towards zero we approach a perfect continuous curve. This continuous representation of the probability is a [[probability density function]] (PDF).  

A [[probability density function]] is effectively the relative probability that outcome $t$ will occur, the chance of any specific $t$ occurring is infinitesimally small though ($P(t=x)\approx 0$). This is because $t$ has infinite possible values since it's continuous; for it to have useful meaning it needs to either be compared against another probability density value or integrated over some interval. Hence it gives "probability density".

> ### $$\begin{align*} 1  &= \int^{\infty}_{\infty} f(t) \cdot dt \end{align*}$$
>> where:
>> $f(t)=$ the [[probability density function]] in terms of $t$
>> $t=$ some parameter, often time

Obviously the integral over infinity is one, and if you want to recover the histogram you simply discretize it.
