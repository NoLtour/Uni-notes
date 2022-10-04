---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What's the method for
## Proof of differentiating tring inverse functions

To differentiate $\sin^{-1}(x)$

$$ 
\begin{align*}
	y&=\sin^{-1}(x)\\
\sin(y) &= x\\\\
\sin^2(y)&=x^2\\
\sin^2(y)+\cos^2(y)&=1\\
\cos(y)&=\sqrt{1-sin^2(y)}\\
\cos(y)&=\sqrt{1-x^2}
\end{align*}
$$
We know [[Differentiating sin(x)]], so...
$$
\begin{align*}\\
x &= sin(y)\\
\dfrac{dx}{dy} &= \cos(y)\\
\dfrac{dx}{dy} &= \sqrt{1-x^2}\\
\dfrac{dy}{dx} &= \dfrac{1}{\sqrt{1-x^2}}
\end{align*}
$$
