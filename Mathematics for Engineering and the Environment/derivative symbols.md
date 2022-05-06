---
aliases: ["derivative symbol","this maths thing","partial derivative"]
tags: ["Question","QFormat3"]
---

#### What are the two
## Derivative symbols
### $d x$
Basically this is the "general case" small distances thing, in the context of something like $\frac{dy}{dx}=$"gradient of tangent of y and x relationship" but if you have some equation such as $y(t,x,z) = x^{4}t + 5xz - \ln z$ then in this case a function $\frac{dy}{dx}=f(t,x,z)$ is correct for all values of $t,x,z$ while still describing the gradient of the tangent of the y,x relationship. 
For this explanation to make sense you need to check out the one for $\delta x$ + the example.

For example, differentiate $y(t,x,z) = x^{4}t^{3} + 5xz - \ln z$ with respect to $x$:
$$\begin{align*}
y(t,x,z) &= x^{4}t + 5xz - \ln z\\
\frac{dy}{dx} &= 4x^{3}t + x^{4}\left(\frac{d}{dx} t\right) + 5z + 5x \left(\frac{d}{dx} z\right) - \frac{\frac{d}{dx} z}{z} 
\end{align*}$$

^7f12bb

Here since it is unknown whether $t,x,z$ are dependent on $x$ or not so we keep it ambiguous.

### $\delta x$
This is used for a [[derivative symbols|partial derivative]], it means that for your related values $\frac{\delta y}{\delta x}$ 
For example if $y=4x+c$ then we can determine that $\frac{dy}{dx} = 4 + \frac{d}{dx}c$ but if $c$ is a constant then $\frac{dy}{dx}=4$ and we can also write that $\frac{\delta y}{\delta x}=4$.

Now lets take $y(t,x,z) = x^{4}t + 5xz - \ln z$ and differentiate with respect to $x$ taking all other variables as constants:
$$\begin{align*}
\frac{\delta y}{\delta x} &= 4tx^{3} + 5z
\end{align*}$$

We could even use [[derivative symbols#^7f12bb|this equation]] and substitute in the knowledge that $t=constant$ and $z=constant$ hence:
$$\begin{align*}
\frac{dy}{dx} &= 4x^{3}t + x^{4}\left(\frac{d}{dx} t\right) + 5z + 5x \left(\frac{d}{dx} z\right) - \frac{\frac{d}{dx} z}{z} \\
 &= 4x^{3}t + x^{4} 0 + 5z + 5x 0 - \frac{0 z}{z} \\
&= 4tx^{3} + 5z
\end{align*}$$