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
Here $r(x)=4x + 25e^{3x}$ is made up of $4x$ and $25e^{3x}$ what your looking for is similar things that will probably differentiate into something solvable when subbed in, the method to find these is either intuition, using a "common situations" equation sheet or repeated guessing. Something also which is __very important__ to note is that all terms in the [[complementary function]] do not match those terms in the [[particular integral]] since they must be [[linearly dependent and independent functions|linearly independent functions]]. This is best shown in an example.

###### [[I be adding a funni|An example]]

First you'd find the [[complementary function]] by treating this as a [[homogeneous and nonhomogeneous differential equations|homogeneous equation]], Ima skip steps (the methods from [[solving linear homogeneous constant-coefficient equations|here]]):

$$ y_{c} = c_{1} e^{-2x} + c_{2} xe^{-2x} \to y_{c} = e^{-2x} (c_{1} + x c_{2}) $$

This one gave us the functions $y_{1}=e^{-2x}$ and $y_{2}=xe^{-2x}$ (it was a repeated root), so we need to ensure going forward that our [[particular integral]] we form contains no [[linearly dependent and independent functions|linearly dependent functions]] with $e^{-2x},xe^{-2x}$.

So now we need to take a look at our [[source term]] and break it into bits that will probably differentiate while making sure not to have them be [[linearly dependent and independent functions|linearly dependent functions]] in context to our established $y_{1},y_{2}$.

$$\begin{align*}
4x &\to Ax + B\\
25e^{3x} &\to Ce^{3x}
\end{align*}$$

So your first guess for this situation would be that $y_{p}=Ax+B+Ce^{3x}$ where $A,B,C$ are constants which if found create a valid [[particular integral]] you get a valid final answer:

$$\begin{align*}
\ddot{y} + 4\dot{y} + 4y &= 4x + 25e^{3x} &y_{p}&=Ax+B+Ce^{3x}\\
&&\dot{y}_{p} &= A + 3Ce^{3x}\\
&& \ddot{y}_{p} &= 9Ce^{3x}\\
9Ce^{3x} + 4(A + 3Ce^{3x}) + 4(Ax+B+Ce^{3x}) &=4x + 25e^{3x}\\
25Ce^{3x} + 4A + 4Ax+4B &= 4x + 25e^{3x}
\end{align*}$$
$$\begin{align*}
25Ce^{3x} &= 25 e^{3x} & 4A + 4B &= 0 & 4Ax &= 4x \\
C &= 1 & A &= -B & A &= 1\\
& & B &= -1
\end{align*}$$

$$ \therefore y_{p}(x) = x-1+e^{3x} $$

Since everything cleans up, this is clearly a valid solution. The take away is that it doesn't matter what your [[particular integral]] is, as long as it cleans up the solutions valid. 

###### When your "guess" overlaps with 