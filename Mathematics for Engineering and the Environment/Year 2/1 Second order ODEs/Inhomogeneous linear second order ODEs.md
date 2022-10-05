---
aliases: [""]
tags: []
---

## Inhomogeneous linear second order ODEs

So now we get to start dealing with ODEs which are not [[homogeneous and nonhomogeneous differential equations|homogeneous]], aka where in the ODE ($\frac{d^{2}y}{dx^{2}} + p(x) \frac{dy}{dx} + q(x)y = r(x)$) the function $r(x) \not\equiv 0$. Note that $r(x)$ is often referred to as a [[source term]].


#### Steps to solve it

1) Solve the homogeneous problem for the linearly independent complementary functions ($y_{1},y_{2}$) to get $c_{1} y_{1}(x) + c_{2} y_{2}(x)$
2) Find a particular integral $y_{p}(x)$
3) Add them together $y = c_{1} y_{1}(x) + c_{2} y_{2}(x) + y_{p}(x)$

Of course this is easier said than done, finding the [[particular integral]] is a pain in the ass quite often but there are methods for getting a solution faster.


