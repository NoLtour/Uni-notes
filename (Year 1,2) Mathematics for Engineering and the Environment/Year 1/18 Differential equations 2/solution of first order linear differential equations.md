---
aliases: ["integrating factor","solving first order inhomogeneous ODEs"]
tags: ["Question","QFormat3"]
---

#### 
## Solution of linear differential equations

There is some proof for this in the book but I [[shut I cba|cba]] to go into (+I don't have time) so here's the thing you need to know:

> For an equation of the form:
> ### $$ \frac{dx}{dt} + p(t) \times x = r(t) $$ 
> The solution is:
> ### $$ x = e^{-f(t)} \left[ \int e^{f(t)} \times r(t) \cdot dt + C \right]= \frac{1}{e^{f(t)}} \left[ \int e^{f(t)} \times r(t) \cdot dt + C \right] $$
> ### $$ f(t) = \int p(t) \cdot dt $$
>> where:
>> $f(t)=$ [[solution of first order linear differential equations|integrating factor]]

Alternative form (more directly applicable for [[standard form first-order ODE]], which is used in year 3 aero systems control):
> For an equation of the form:
> ### $$\begin{align*} \tau \frac{dy}{dt} + y  &= f(t)  \end{align*}$$
> The solution is: 
> ### $$\begin{align*} y(t) &= e^{-\frac{ t}{\tau}} \left[ \int e^{\frac{t}{\tau}} \times f(t) \cdot dt + C \right]  \end{align*}$$ 

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
&= e^{-\frac{t^{2}}{2}} \left[ \int e^{\frac{t^{2}}{2}} \times t \cdot dt + C \right]\\
&= e^{-\frac{t^{2}}{2}}\left(e^{\frac{t^{2}}{2}} + C\right)\\
&= 1 + Ce^{-\frac{t^{2}}{2}}
\end{align*}$$
