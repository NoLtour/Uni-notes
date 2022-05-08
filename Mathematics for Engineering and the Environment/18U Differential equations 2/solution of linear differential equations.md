---
aliases: ["integrating factor"]
tags: ["Question","QFormat3"]
---

#### 
## Solution of linear differential equations

There is some proof for this in the book but I [[shut I cba|cba]] to go into (+I don't have time) so here's the thing you need to know:

> For an equation of the form:
> ### $$ \frac{dx}{dt} + p(t) \times x = r(t) $$ 
> The solution is:
> ### $$ x = e^{-f(t)} \left[ \int e^{f(t)} \times r(t) \cdot dt + C \right] $$
> ### $$ f(t) = \int p(t) \cdot dt $$
>> where:
>> $f(t)=$ [[solution of linear differential equations|integrating factor]]

### Example
> Solve:
> $$ \frac{dx}{dt} + t x = t $$

$$\begin{align*}
f(t) &= \int p(t) \cdot dt\\
& & p(t) &= t & r(t) &= t\\
&= \int t \cdot dt\\
&= \frac{t^{2}}{2}
\end{align*}$$

Subbing into the main formula

$$\begin{align*}
x &= e^{-f(t)} \left[ \int e^{f(t)} \times r(t) \cdot dt + C \right]\\
&= e^{-\frac{t^{2}}{2}} \left[ \int e^{\frac{t^{2}}{2}} \times r(t) \cdot dt + C \right]
\end{align*}$$
