---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is a method for
## Finding particular integrals

There isn't one.
![[pain1.mp4#play]]

Well that's kinda true, bascially finding them is trial and error. This is the way:

So you have to find the [[particular integral]] of $L[x_1]=f(x)$ (if your confused on what $L[x_1]$ is look at [[general solution of a linear nonhomogeneous equation|this]]):

then do:
$$\begin{align*}
&\frac{d}{dx} f(x)\\
&\frac{d^{2}}{dx^{2}} f(x) 
\end{align*}$$
well atleast do this if your $L[x_1]$ is in the form $A\frac{d^{2}x}{dt^{2}} + B\frac{dx}{dt} + Cx$, basically you are differentiating $f(x)$ till you can sub in for all differentiated forms that $L[x_1]$ requires.

Then make an equation composed of each unique part of the differential multiplied by a constant, and then differentiate that till you have enough to sub back into $L[x_1]$ and solve for the constants, if it can't be solved you will have to adjust your inputs.

### Example
> Find the [[particular integral]] of $\frac{d^{2}x}{dt^{2}} + 5 \frac{dx}{dt} - 9x = \cos 2t$

So first of all $f(x) = \cos 2t$:

$$\begin{align*}
x &= \cos 2t\\
\frac{dx}{dt} &= -2 \sin 2t\\
\frac{d^{2}x}{dx^{2}} &= -4 \cos 2t 
\end{align*}$$

So we have unique bits $\cos 2t$ and $\sin 2t$, so I'm going to make a guess that $A\cos 2t + B\sin 2t$ could be a solution:

$$\begin{align*}
x(t) &= A\cos 2t + B\sin 2t \\
\frac{dx}{dt} &= -2A\sin 2t + 2B\cos 2t \\
\frac{d^{2}x}{dt^{2}} &=  -4A\cos 2t - 4B\sin 2t \\
&&\frac{d^{2}x}{dt^{2}} + 5 \frac{dx}{dt} - 9x &= \cos 2t\\\\
&&(-4A\cos 2t - 4B\sin 2t) + 5 (-2A\sin 2t + 2B\cos 2t) - 9(A\cos 2t + B\sin 2t) &= \cos 2t\\
&& A(-13\cos 2t-10\sin 2t) + B( 10\cos 2t -13\sin 2t ) &= \\
&& -13 A + 10B &= 1 & -10A -13B &= 0\\
&& A&= - \frac{13}{269} & B&= \frac{10}{269}\\
x(t) &= - \frac{13}{269} \cos 2t + \frac{10}{269}\sin 2t
\end{align*}$$

Would you look at that, it is.