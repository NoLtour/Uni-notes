---
aliases: ["root locus gain factor","zeros","poles","system zeros","system poles","sytem characeristic equation","system characteristic polynomial"]
tags: []
---


## System transfer function feature definitions
### Context
Let's say we want to predict the behaviour of a [[block diagram parts|system]], it's possible to do so from just looking at it's equation. But to make discussing features simpler we need names for them.

Take the following [[transfer function]] as a reference, we will use it to help in explaining what feature names refer to.

$$\begin{align*}
\frac{C}{R} = G(s) &= \frac{K(s+2)}{(s+1)(s+3)} = K\frac{s+2}{s^{2}+4s+3}
\end{align*}$$

### Defs
#### Zeros of C, G and R

These are the root's of the numerator polynomial, in this case:
$$\begin{align*}
s &= -2
\end{align*}$$

#### Poles of C, G and R

These are the roots of the denominator polynomial, in this case:
$$\begin{align*}
s &= -1, & s&= -3
\end{align*}$$

#### System zeros and system poles

The roots and zeros when applied to the whole system.

In this example case the poles and roots seen so far are the system's zeros and poles. It is possible to apply this to a subsection of a system though. Hence the distinction existing.

#### System characteristic polynomial

The name used for the denominator of the system transfer function, in this case:
$$\begin{align*}
(s^{2} + 4s + 3)
\end{align*}$$

#### System characteristic equation

Result if the system characteristic polynomial is equated to zero. Its roots are obviously just the system poles.

#### Root locus gain factor

That which results if the coefficients of the highest powers of 𝑠 in numerator and denominator are made equal to unity.

According to chat GPT it's $K$ in this example? ngl I need clarity on this, can't find it mentioned again or on interwebz.