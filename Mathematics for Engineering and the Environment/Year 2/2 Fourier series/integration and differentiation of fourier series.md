---
aliases: ["fourier series integration","fourier series differentiation"]
tags: []
---

## Integration and differentiation of fourier series

It's really not complicated, like at all:

$$\begin{align*}
f(x) &= \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \cos \left( \frac{n\pi}{L} x \right) + b_{n} \sin \left(\frac{n\pi}{L} x\right) \right]\\
\dot{f}(x) &=   \sum\limits^{\infty}_{n=1}\left[ - a_{n} \frac{n\pi}{L} \sin \left( \frac{n\pi}{L} x \right) + b_{n}\frac{n\pi}{L} \cos \left(\frac{n\pi}{L} x\right) \right]\\
\ddot{f}(x) &=   \sum\limits^{\infty}_{n=1}\left[ - a_{n} \left(\frac{n\pi}{L}\right)^{2} \cos \left( \frac{n\pi}{L} x \right) - b_{n}\left(\frac{n\pi}{L}\right)^{2} \sin \left(\frac{n\pi}{L} x\right) \right]
\end{align*}$$

