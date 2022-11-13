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

This becomes 3 separate problems, depending on the value of $\lambda$ 
