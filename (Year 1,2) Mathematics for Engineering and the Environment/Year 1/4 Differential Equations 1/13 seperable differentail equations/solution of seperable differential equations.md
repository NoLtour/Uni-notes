---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the method for the
## Solution of seperable differential equations
### Theory
Given some differential equation, if possible rearrange it so that like variables are on the same side:

> ### $$ \begin{align*}given: \:\:\frac{dy}{dx} &= f(x, y)\\g(y) \frac{dy}{dx} &= h(x)\\g(y)\cdot dy &= h(x) \cdot dx\end{align*} $$ 

You can see it is easy to solve in it's final form.

### Example

> Solve the equation $\frac{dx}{dt} = 4xt$, where $x>0$

$$\begin{align*}
\frac{dx}{dt} &= 4xt\\
\frac{1}{x} \cdot dx &= 4t \cdot dt\\
\int \frac{1}{x} \cdot dx &= \int 4t \cdot dt\\
\ln(x) &= 2t^{2} + k\\
x &= k e^{2t^{2}}
\end{align*}$$
