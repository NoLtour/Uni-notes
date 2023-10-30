---
aliases: [""]
tags: []
---
!
## Second order system step response

### Setup

Ok the problem setups basically identical to [[first order system step response]], except this time we will use a [[system orders|second order system transfer function]] in the [[transfer function variable names#Second order system|standard second order form]]:

$$\begin{align*}
G(s)&= \frac{K \omega_{n}^{2}}{s^{2} + 2\zeta \omega_{n}s+ \omega_{n}^{2}}
\end{align*}$$

K so we get our response function (representing a constant force, starting at $t=0$), which is just a [[heaviside function]]:


$$\begin{align*}
&& \text{Lap } &\text{trans}\\
r(t) &= H(t) & &\to & R(s) &= \frac{e^{-0s}}{s} = \frac{1}{s}
\end{align*}$$

Then combining this with the [[transfer function]]:

$$\begin{align*}
&& && &&\text{Partial }&\text{Fractions}\\
C(s) &= R G & &\to & C(s) &= \frac{1}{s} \frac{K \omega_{n}^{2}}{s^{2} + 2\zeta \omega_{n}s+ \omega_{n}^{2}} & &\to & C(s) &= \frac{1}{s} + \frac{A_{1}}{s-p_{1}} + \frac{A_{2}}{s-p_{2}}
\end{align*}$$

(Note: that I'm leaving the partial fractions [[in reality I am lazy|really unresolved]], since the inputs are undefined and this isn't a "solving partial fractions" class.)

We've got a response function, so just perform a inverse Laplace transform to get back to time domain:

$$\begin{align*}
c(t) &= \mathcal{L}^{-1}\left[ C(s) \right] = \mathcal{L}^{-1}\left[ \frac{1}{s} + \frac{A_{1}}{s-p_{1}} + \frac{A_{2}}{s-p_{2}}\right] & &\to & c(t) &= 1 + A_{1}e^{p_{1} t} + A_{2}e^{p_{2} t}
\end{align*}$$

Here $p_{1}$ and $p_{2}$ are the [[system transfer function feature definitions|poles]], which is kinda obvious if you recall [[Laplace transform]]s from last year. It doesn't take long to realise that this is going to open the door to oscillators, because it has multiple times in the past. Which is correct!

### Classification

Recalling stuff from previous years, depending on the constants we can get a bunch of different system responses:

![[types of dampening (differentially modelled oscillator)]] 

Since the module's different instead of "[[damping parameter (differentially modelled oscillator)|damping parameter]]" we use "[[transfer function variable names|system damping]] constant". Same thing from a [[got like 4 different docs with their own damping variables lmao|maths POV]].

