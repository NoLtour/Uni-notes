---
aliases:
  - sinusoidal gain
  - sinusoidal phase shift
tags:
---

## Linear system sinusoidal response

### Input, output response

When a [[linear systems|linear system]] has a sinusoidal input, it's response is also a sinusoidal wave with the same frequency as the input:

![[Pasted image 20231208175536.png]]

Although the frequency doesn't change, amplitude and phase often do! In this module we only consider single frequency input systems, it's a whole different level of difficulty when dealing with more complex inputs.

### Wave characterisation

For this module, we assume the input phase $\sigma$ to be zero, simplifying the input:

$$\begin{align*}
&& \sigma&= 0\\
u(t) &= \sin(\sigma + \omega t) & &\to& u(t) &= \sin( \omega t)
\end{align*}$$

We make use of [[complex numbers]] to represent sine waves. Just like what was done with [[phasor representation]] in year 1. Subbing in for $s$ with:
$$\begin{align*}
&& \sigma&= 0\\
s &= \sigma + j\omega & &\to& s &= j\omega 
\end{align*}$$

There is a proof for it, but that doesn't matter. What happens for a generic [[block diagram parts|system]] [[transfer function]] is the following result:

> ### $$\begin{align*} u(t) &= \sin(\omega t) \end{align*}$$
> ### $$\begin{align*} y(t)  &= |G(j\omega)| \:\sin(\omega t + \angle G(j\omega)\:) \\ &= M\sin(\omega  t + \phi) \end{align*}$$
> ### $$\begin{align*} \phi &= \angle G(j\omega) & M&= |G(j\omega)|\end{align*}$$
>> where:
>> $u=$ Sinusoidal input (with magnitude 1)
>> $\omega=$ Input and response frequency
>> $y=$ System response
>> $M=$ Gain of $G$
>> $\phi=$ Phase shift of $G$
>> $G=$ system [[transfer function]]


### Frequency effect

Here a transfer function is applied to s simple sinusoidal input, note that the response actually changes with frequency! Both the magnitude and phase are changing, learning how to determine how a controller's frequency responds to different input's is the target of this topic. (which has lot's of [[it is quite useful|utility]])

![[Pasted image 20231208181531.png]]
