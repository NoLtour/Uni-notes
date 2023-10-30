---
aliases: [""]
tags: []
---

## [[system orders|First order system]] impulse response

Consider the following first order system:

![[Pasted image 20231029172722.png]]

Here $T>0$, it's transfer function is obviously $\frac{1}{Ts+1}$. 

We want to see how the system responds to an instantaneous [[impulse]]. So to do this will involve putting a representation of an instantaneous impulse into the system "$R$".

An appropriate mathematical response of a instantaneous impulse that has a finite value would be a [[dirac delta function|impulse function]]. So if we plug that as our input $r$ and do a [[transforms of impulse functions#Laplace transform of dirac delta function|Laplace transform of a impulse function]] we can slap it against our [[transfer function]] and get a response.

$$\begin{align*}
&& \text{Lap } &\text{trans}\\
r(t) &= \delta(t) & &\to & R(s) &= e^{-0s} =1
\end{align*}$$

Then combining this with the [[transfer function]]:

$$\begin{align*}
C(s) &= R G & &\to & C(s) &= \frac{1}{Ts+1}
\end{align*}$$

Considering how simple the input is, it's quite trivial. We're also going to put [[transfer function variable names|system gain]] back in, in this case $K=1$.

$$\begin{align*}
C(s) &= \frac{1}{Ts+1}& &\to & C(s) &= \frac{K}{Ts+1}
\end{align*}$$

We've got a response function, so just perform a inverse Laplace transform to get back to time domain:

$$\begin{align*}
c(t) &= \mathcal{L}^{-1}\left[ C(s) \right] = \mathcal{L}^{-1}\left[ \frac{K}{Ts+1} \right] & &\to & c(t) &= \frac{K}{T} e^{\frac{-t}{T}} \theta(t)
\end{align*}$$

Note here $\theta$ is a [[heaviside function]], also although I glossed over how you invert these you need to be able to so. 

Plotted we can see the systems response:

![[Pasted image 20231029175010.png]]

Observation:
- The instantaneous impulse results in the system "starting" at a non zero value
- Initially the output is $c(0)=K/T$
- As time tends to infinity the response tends to zero
- Decay is exponential
