---
aliases: ["time constant","settling time"]
tags: []
---

## System response time metrics

### Intro

![[Pasted image 20231029175440.png]]

We often want to describe how fast a system responds, so we have standard terms to make communication and visualisation easier.

### Time constant

([[I love naming conflicts|Pretty much]] the same as  [[transfer function variable names|system time constant]])

This is the time in seconds for the decaying exponential transient to reach $1-e^{-1}$ of it's final value:

If we consider the case of [[first order system impulse response]], then it's final value is zero and hence:

> ### $$\begin{align*} \text{Time constant: } \:\:\:\left. e^{\frac{-t}{T}} \right|_{t=T} &= e^{-1}  \end{align*}$$
>> where:
>> $t=$ time variable
>> $T=$ [[transfer function variable names|system time constant]]

It can clearly be seen that it takes 1 time constant to reach $e^{-1}$. (for that case)

### Settling time

This is the time it takes to reach $\approx 100 - 1.8\%$ of the final value. Equivalent to 4 [[system response time metrics|time constant]]s.

If we consider the case of [[first order system impulse response]], then it's final value is zero and hence:

> ### $$\begin{align*} \text{Time constant: } \:\:\:\left. e^{\frac{-t}{T}} \right|_{t=4T} &= e^{-4} \approx 0.018 \end{align*}$$
>> where:
>> $t=$ time variable
>> $T=$ [[transfer function variable names|system time constant]]
>> $4T=$ settling time

Since the system never actually reaches zero, we use settling time to say "meh close enough, basically stopped".
