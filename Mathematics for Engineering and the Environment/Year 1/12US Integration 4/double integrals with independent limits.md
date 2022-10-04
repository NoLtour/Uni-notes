---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe how to solve
## Double integrals with independent limits
### Theory
Basically so far you have been dealing with single integrals, things that are integrated with respect to one variable, but of course many things have their values depend on multiple input variables so this is where things get difficult... is what I would say if it was, it's actually not that bad, litterally just integrating the normal way twice for 2 speretate variables for example:

$$\begin{align*}
D_{nuts} &= \int \int \int \int f(t,r,o,l)\cdot dt \cdot dr \cdot do \cdot dl & f(t,r,o,l) &= trol^{2} \\
 &= \int \int \int \int trol^{2}\cdot dt \cdot dr \cdot do \cdot dl\\
&= \int \left(\int \left(\int \left(\int t\cdot dt\right)rol^{2} \cdot dr\right) \cdot do\right) \cdot dl\\
&= \int \left(\int \left(\int \left( \frac{t^{2}}{2}+k_{1}\right)rol^{2} \cdot dr\right) \cdot do\right) \cdot dl\\
&= \int \left(\int \left(\int \left( \frac{t^{2}}{2}+k_{1}\right)r \cdot dr\right)ol^{2} \cdot do\right) \cdot dl\\
&= \int \left(\int \left( \left( \frac{t^{2}}{2}+k_{1}\right) \frac{r^{2}}{2} + k_{2} \right)ol^{2} \cdot do\right) \cdot dl\\
&= \int \left(\int \left( \left( \frac{t^{2}}{2}+k_{1}\right) \frac{r^{2}}{2} + k_{2} \right)o \cdot do\right)l^{2} \cdot dl\\
&= \int \left( \left( \left( \frac{t^{2}}{2}+k_{1}\right) \frac{r^{2}}{2} + k_{2} \right) \frac{o^{2}}{2} + k_{3} \right)l^{2} \cdot dl\\
&= \left( \left( \left( \frac{t^{2}}{2}+k_{1}\right) \frac{r^{2}}{2} + k_{2} \right) \frac{o^{2}}{2} + k_{3} \right) \frac{l^{3}}{3} + k_{4} \\
\end{align*}$$

Something else that's noteworthy is that since all the variables are independent we can actually write the integration like this (this is essentially the same as rearranging multiplication order):
$$\begin{align*}
D_{nuts} &= \int \int \int \int trol^{2}\cdot dt \cdot dr \cdot do \cdot dl\\
 &= \left(\int t\cdot dt\right)\left(\int r \cdot dr\right)\left(\int o \cdot do\right) \left(\int l^{2} \cdot dl\right)\\
 &= \left( \frac{t^{2}}{2} + k_{1} \right)\left(\frac{r^{2}}{2} + k_{2} \right)\left(\frac{o^{2}}{2} + k_{3}\right) \left(\frac{l^{3}}{3} + k_{4}\right)
\end{align*}$$

My examples kinda cursed but I hope you get the idea, it's just single integration over and over again. The hard part's really just getting the limits right, so yeah, I want to say skill issue but I've overused that now, uuuuh [[git guuuuudd aoifijuwlaoihjflkjawfdlk|get good?]].

Some notes:
- The important notation that needs to be learned is that now when defining limits on integrals you need to also note the variable it is assosiated with, as seen in the example below.
- The order you integrate in can be changed (but remember to adjust limits if you change it!!!), the final resault will be equivilent though the steps to get that resault may be more difficult depending on integration order.
- When integrating you must fully expand all functions that use the variable you are currently integrating for as an input
- The most obvious thing when working with multidimentional integration is volume but any situation with multiple independent variables can use this type of integration

### Example
> Given that $y=zB\sin( x  )+x\sin(z)$ find an expression for the volume enclosed within $x=0\to X$ and $z=0\to Z$:
> ![[Pasted image 20220225212649.png]]
> (the image isn't accurate but I hope you get the idea)

We know that the area of a 3D cube is $V=xyz$, and that over small differences in x and z you can take y as constant so: $dV = y\cdot dz \cdot dx$, that equation will be our starting point. 

$$\begin{align*}
dV &= y \cdot dz \cdot dx \\
\int^{V}_{0} 1\cdot dV &= \int^{x=X}_{x=0} \int^{z=0}_{z=Z} y \cdot dz \cdot dx \\
V &= \int^{x=X}_{x=0} \int^{z=0}_{z=Z} \left( zB\sin( x  )+x\sin(z) \right) \cdot dz \cdot dx \\
 &= \int^{x=X}_{x=0}  \left[ \frac{z^{2}}{2} B\sin(x) - x\cos(z) \right]^{z=0}_{z=Z} \cdot dx \\
 &= \int^{x=X}_{x=0}  \left( \frac{Z^{2}}{2} B\sin(x) - x\cos(Z) - \frac{0^{2}}{2} B\sin(x) + x\cos(0) \right) \cdot dx \\
 &= \int^{x=X}_{x=0}  \left( \frac{Z^{2}}{2} B\sin(x) - x\cos(Z) + x \right) \cdot dx \\
 &= \int^{x=X}_{x=0}  \left( \frac{Z^{2}}{2} B\sin(x) + x(1 - \cos(Z)) \right) \cdot dx \\
 &=  \left[ -\frac{Z^{2}}{2} B\cos(x) + \frac{x^{2}}{2} (1 - \cos(Z)) \right]^{x=X}_{x=0} \\
 &=  -\frac{Z^{2}}{2} B\cos(X) + \frac{X^{2}}{2} (1 - \cos(Z)) + \frac{Z^{2}}{2} B\cos(0) - \frac{0^{2}}{2} (1 - \cos(Z))  \\
 &=   \frac{X^{2}}{2} (1 - \cos(Z)) -\frac{BZ^{2}}{2} \cos(X) + \frac{BZ^{2}}{2} \\
 &=   \frac{X^{2}}{2} (1 - \cos(Z)) + \frac{BZ^{2}}{2}(1 - \cos(X)) \\
\end{align*}$$

Final expression is:
$$ V = \frac{X^{2}}{2} (1 - \cos Z) + \frac{BZ^{2}}{2}(1 - \cos X) $$