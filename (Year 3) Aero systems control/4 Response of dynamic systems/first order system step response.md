---
aliases: [""]
tags: []
---

## First order system step response

Ok so we did [[first order system impulse response]] for an instantaneous impulse, but let's try inputting a constant "force". This can be represented with a [[heaviside function]]. Then just like we did for [[first order system impulse response]] we can [[transforms of impulse functions|Laplace transform the heaviside function]] and slap it in our input $R$.

$$\begin{align*}
&& \text{Lap } &\text{trans}\\
r(t) &= H(t) & &\to & R(s) &= \frac{e^{-0s}}{s} = \frac{1}{s}
\end{align*}$$

Then combining this with the [[transfer function]] (assume $T>0$):

$$\begin{align*}
&& && &&\text{Partial }&\text{Fractions}\\
C(s) &= R G & &\to & C(s) &= \frac{1}{s} \frac{K}{Ts+1} & &\to & C(s) &= \frac{K}{s} - \frac{KT}{Ts+1}
\end{align*}$$

We've got a response function, so just perform a inverse Laplace transform to get back to time domain:

$$\begin{align*}
c(t) &= \mathcal{L}^{-1}\left[ C(s) \right] = \mathcal{L}^{-1}\left[ \frac{K}{s} - \frac{KT}{Ts+1}\right] & &\to & c(t) &= K\left(1 - e^{- \frac{t}{T}}\right)
\end{align*}$$

Plotted this becomes:

![[Pasted image 20231029181404.png]]

Considering what we saw in [[first order system impulse response]], that used the same [[transfer function]] and tended to zero, implying some "resistive" response. This time by providing a constant force it tends to some value instead, implying equilibrium between this "resistance" and the input force.
