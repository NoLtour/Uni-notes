---
aliases: ["derivative symbol","this maths thing","partial derivative"]
tags: ["Question","QFormat3"]
---

#### What are the two
## Derivative symbols
### $d x$
Basically this is the "general case" small distances thing, in the context of something like $\frac{dy}{dx}=$"gradient of tangent of y and x relationship" but if you have some equation such as $y(t,x,z) = x^{4}t + 5xz - \ln z$ then in this case a function $\frac{dy}{dx}=f(t,x,z)$ is correct for all values of $t,x,z$ while still describing the gradient of the tangent of the y,x relationship. 
For this explanation to make sense you need to check out the one for $\delta x$ + the example.

For example, differentiate $y(t,x,z) = x^{4}t^{3} + 5xz - \ln z$:
$$\begin{align*}
y(t,x,z) &= x^{4}t + 5xz - \ln z\\
\frac{dy}{dx} &= 4x^{3}t + x^{4}\left(\frac{d}{dx} t\right) + 5z + 5x \left(\frac{d}{dx} z\right) - \frac{1}{z} 
\end{align*}$$


### $\delta x$
This is used for a [[partial derivative]], it means that for your related values there are no other input variables so $\frac{\delta y}{\delta x}$ is entirely defined by $y$ and $x$ or taken as a constant.


