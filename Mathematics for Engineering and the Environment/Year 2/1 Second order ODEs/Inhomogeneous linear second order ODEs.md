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

##### Finding the particular integral
When looking for a solution for the particular integral what you are looking for is "the most general form" of each part of the [[source term]], for example take the following ODE:
$$ \ddot{y} + 4\dot{y} + 4y = 4x + 25e^{3x} $$
Here $r(x)=4x + 25e^{3x}$ is made up of $4x$ and $25e^{3x}$ what your looking for is similar things that will probably differentiate into something solvable when subbed in, the method to find these is either intuition, using a "common situations" equation sheet or repeated guessing. In this example:
$$\begin{align*}
4x &\to Ax + B\\
25e^{3x} &\to Ce^{3x}
\end{align*}$$

So your first guess for this situation would be that $y_{P}=Ax+B+Ce^{3x}$ where $A,B,C$ are constants which if found create a valid [[particular integral]] you get a valid final answer:

$$\begin{align*}
y_{P}&=Ax+B+Ce^{3x}\\
\dot{y}_{P} &= A + 3Ce^{3x}\\
\ddot{y}_{P} &= 9Ce^{3x}\\
&
\end{align*}$$
