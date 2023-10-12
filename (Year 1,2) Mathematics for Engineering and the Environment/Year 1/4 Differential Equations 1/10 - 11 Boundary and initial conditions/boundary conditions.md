---
aliases: ["boundary condition"]
tags: ["Question","QFormat3"]
---

#### What are
## Boundary conditions
#### Theory
These are the values given that should resault in a specific output which can then be used (if sufficient [[boundary conditions]] are supplied) to find the [[general and particular solution|particular solution]] of a [[general and particular solution|general solution]].

#### Example


> [[integration|integrate]] $\frac{dy}{dx} = x^{3} + 69$ given that at at $f(x) = y$ and $f(4)=0$:


$$\begin{align*}
\frac{dy}{dx} &= x^{3} + 69 \\
...
y &=  \frac{x^{4}}{3} + 69x + k & let:\:y=0\:x=4\\
0 &=  \frac{4^{4}}{3} + 69(4) + k\\
k &= - \frac{1084}{3}\\y &=  \frac{x^{4}}{3} + 69x - \frac{1084}{3}\\
\end{align*}$$

Here "$f(4)=0$" is a [[boundary conditions|boundary condition]].