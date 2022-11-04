---
aliases: ["fourier series integration","fourier series differentiation"]
tags: []
---

## Integration and differentiation of fourier series

It's quite ez.

### Differentiation
It's really not complicated, like at all:

$$\begin{align*}
f(x) &= \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \cos \left( \frac{n\pi}{L} x \right) + b_{n} \sin \left(\frac{n\pi}{L} x\right) \right]\\
\dot{f}(x) &=   \sum\limits^{\infty}_{n=1}\left[ - a_{n} \frac{n\pi}{L} \sin \left( \frac{n\pi}{L} x \right) + b_{n}\frac{n\pi}{L} \cos \left(\frac{n\pi}{L} x\right) \right]\\
\ddot{f}(x) &=   \sum\limits^{\infty}_{n=1}\left[ - a_{n} \left(\frac{n\pi}{L}\right)^{2} \cos \left( \frac{n\pi}{L} x \right) - b_{n}\left(\frac{n\pi}{L}\right)^{2} \sin \left(\frac{n\pi}{L} x\right) \right]
\end{align*}$$

Something to keep in mind however is that some [[Fourier Series Overview|Fourier series]] cannot be differentiated. Hence for a fourier series to have a valid differnetial it must satisfy the following:
- $f(x)$ meets the [[fouriers theorem|dirichlet conditions]] (hence can be a [[Fourier Series Overview|Fourier series]])
- $f(x)$ is continuous, including at the edges of the range
- $\dot{f}(x)$ is [[piecewise smooth]] for all x

For example a sawtooth function is not continuous at the edges and therefore is not suitable for differentiation using a Fourier series:
![[Pasted image 20221019214609.png]]

### Integration
Even less complicated [[like shockingly easy|lol]], there are no restrictions as long as you can get the function as a [[Fourier Series Overview|Fourier series]] you can integrate it:

$$\begin{align*}
f(x) &= \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \cos \left( \frac{n\pi}{L} x \right) + b_{n} \sin \left(\frac{n\pi}{L} x\right) \right]\\
\int f(x) \cdot dx &= C + \frac{1}{2} a_{0} x + \sum\limits^{\infty}_{n=1}\left[ a_{n} \frac{L}{n\pi} \sin \left( \frac{n\pi}{L} x \right) - b_{n} \frac{L}{n\pi} \cos \left(\frac{n\pi}{L} x\right) \right]\\ 
\end{align*}$$

Then you just need to find the constant like with any other integral, when finding the constant it's best to substitute $x$ with a value that will cause the other terms to go to zero.
