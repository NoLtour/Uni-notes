---
aliases: ["eigenvalue ODE"]
tags: []
---

## Solving eigenvalue ODEs

### Intro

Now your asking "what the fuck are those they sound painful" and the answer is they are not that bad! A eigenvalue ODE is just where you only have 2 terms in the ODE eg:

$$ \frac{d^{2}y}{dx^{2}} + \lambda y = 0 $$

We call them eigenvalue problems since they can be rearranged into:
$$ \frac{d^{2}y}{dx^{2}}  = -\lambda y $$
Which indicates it is possible to find derivatives/integrals simply by multiplying by $\lambda$.

### Example
> Solve:
> $$ \frac{d^{2}y}{dx^{2}} + \lambda y = 0 $$
> Where $y(0)=0$ and $y(\pi)=0$

We solve this using the same method [[solving linear homogeneous constant-coefficient equations#Method (for constant coefficients)|solving linear second order ODEs]] hence we will start with step 1:
$$\begin{align*}
m&=  \frac{0\pm\sqrt{0^{2}-4\times1\times\lambda}}{2\times1} &&\to& m&= \pm\sqrt{-\lambda}
\end{align*}$$
This becomes 3 separate problems, depending on the value of $\lambda$ hence our 3 cases are:
1) $(\lambda=-k^{2})\:\:<0$
