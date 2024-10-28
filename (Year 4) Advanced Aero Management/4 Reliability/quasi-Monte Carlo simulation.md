---
aliases: [""]
tags: []
---

## Quasi-Monte Carlo simulation

A significant contributor to the error seen in [[Monte Carlo simulation]] is the fact that the domain isn't efficiently sampled. Take the [[Monte Carlo simulation#Example, area of a shape|shape example]], it's domain is full of large gaps:

![[Pasted image 20241023162845.png]]

Due to random chance, some area's are over sampled while others are under sampled. Obviously that's a reason __why__ we increase sample count, but why not just equally distribute em?

![[Pasted image 20241023164229.png]]

Congrats, this is what [[quasi-Monte Carlo simulation]] is, we replace a random sample with a better spaced sample.

Applying this approach with the [[Monte Carlo simulation#Example, area of a shape|shape example]], the result is huge:

![[Pasted image 20241023164349.png]]

The error functions also different, instead of being proportional to one over the square root of sample count, it's proportional to the inverse of the sample count:

$$\begin{align*}
\text{Monte}&\text{ Carlo} &&& \text{Quasi-Mont}&\text{e Carlo}\\
E_{rr}(\mu) &= \frac{k}{\sqrt{N}} &&& E_{rr}(\mu) &= \frac{k}{{N}}
\end{align*}$$

Note that although at a glance "this is amazing and perfect", it really isn't. There are cases where a Quasi approach actually leads to the result being poor, this is especially the case if the choice of sampling method is poor. It's possible your sampling pattern lines up with a certain sequential feature present in the target, resulting in your result being wholey innacurate.
