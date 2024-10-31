---
aliases:
  - compuned model
  - multi-risk model
  - competing risk models
  - series system component model
tags:
---

## Competing risk models

Real world components are often more complex than a single [[probability density function|PDF formula]] can capture, this is especially true when we have multiple failure mechanisms which can cause the part to fail.

The solution's quite simple though, we simply treat the component like a system and create a resultant [[probability density function|PDF]] from all it's constituent means of failure (this method is JUST series).

The methods outlined here can only be used if:
- The failure modes are modelled as completely independent
- The component fails when any mode is encountered
- Each mode has it's own distribution

If any failure mode occurs, the part fails. This is clearly just a [[complex reliability model|series reliability model]] hence we can state it's [[cumulative distribution function]] and [[reliability function]] are:

$$\begin{align*}
F(t) &= 1 - \prod^{n}_{i=1} R_{i}(t) &&& R(t) &= \prod^{n}_{i=1} R_{i}(t)
\end{align*}$$

Obviously, we can extract the [[probability density function]] from the systems [[reliability function]], or anything else like the [[hazard function|hazard rate]]:

$$\begin{align*}
F(t) &= 1 - \prod^{n}_{i=1} R_{i}(t) &&\to& \int^{t_{1}}_{-\infty} f(t) \cdot dt &= 1 - \prod^{n}_{i=1} R_{i}(t) &&\to& f(t) &= \frac{d}{dt}\left(1 - \prod^{n}_{i=1} R_{i}(t)\right)
\end{align*}$$

The general form ends up being:

> ### $$\begin{align*} f(t)  &= R(t) \left[\sum\limits^{n}_{i=1} \frac{f_{i}(t)}{R_{i}(t)} \right] \end{align*}$$
>> where:
>> $f(t)=$ the [[probability density function]] of the component as a whole
>> $R(t)=$ the [[reliability function]] of the component as a whole
>> $f_{i}(t)=$ the [[probability density function]] of the $i_{th}$ failure mode
>> $R_{i}(t)=$ the [[reliability function]] of the $i_{th}$ failure mode

### Example

![[Pasted image 20241031115021.png]]
![[Pasted image 20241031115033.png]]
![[Pasted image 20241031115044.png]]
