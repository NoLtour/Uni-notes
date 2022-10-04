---
aliases: ["general solution","particular solution"]
tags: ["Question","QFormat3"]
---

#### What is a
## General solution
A general solution is a solution that contains undefined constants for example:

> [[integration|integrate]] $\frac{dy}{dx} = x^{3} + 69$ 

$$\begin{align*}
\frac{dy}{dx} &= x^{3} + 69 \\
\int 1\cdot dy &= \int x^{3} + 69 dx\\
y &=  \frac{x^{4}}{3} + 69x + k
\end{align*}$$

The solution $y = \frac{x^{4}}{3} + 69x + k$ is a [[general and particular solution|general solution]], since it has the arbitary constant $k$.

If I then said:

> [[integration|integrate]] $\frac{dy}{dx} = x^{3} + 69$ given that at at $y=0$ $x=4$

$$\begin{align*}
\frac{dy}{dx} &= x^{3} + 69 \\
...
y &=  \frac{x^{4}}{3} + 69x + k & let:\:y=0\:x=4\\
0 &=  \frac{4^{4}}{3} + 69(4) + k\\
k &= - \frac{1084}{3}\\y &=  \frac{x^{4}}{3} + 69x - \frac{1084}{3}\\
\end{align*}$$

We now have a [[general and particular solution|particular solution]] $y =  \frac{x^{4}}{3} + 69x - \frac{1084}{3}$, since it contains no arbitrary constants.