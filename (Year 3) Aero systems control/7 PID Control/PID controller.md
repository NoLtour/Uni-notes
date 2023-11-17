---
aliases: [""]
tags: []
---

## PID controller

### Description

The strength's and weaknesses of [[proportional controller|proportional control]], [[integral controller|integral control]] and [[derivative controller|derivative control]] in a closed loop system can be described as the following:

![[Pasted image 20231116222617.png]]
(It should be noted that these correlations may not be exact due to interactions among various terms)

Which means that if we really want to achieve good control... why not combine them to cover each other's weaknesses? This is where [[PID controller]]s become a thing!

> ![[Pasted image 20231116223048.png]]
> ### $$\begin{align*} u(t) &= K_{p}e(t) + K_{i}\int^{t}_{0} e(t)\:dt + K_{d} \frac{de(t)}{dt} \end{align*}$$
> ### $$\begin{align*} G_{c}  &=  K_{p} \left(1 + \frac{1}{T_{i}s} + T_{d} s \right) \end{align*}$$
> ### $$\begin{align*}  T_{i} &= \frac{K_{i}}{K_{p}} & T_{d} &= \frac{K_{d}}{K_{p}} \end{align*}$$
>> where:
>> $G_{c}=$ [[general control system|controller transfer function]]
>> $K_{p}=$ proportional gain
>> $K_{d}=$ derivative gain
>> $K_{i}=$ integral gain
>> $T_{d}=$ derivative time constant
>> $T_{i}=$ integral time constant
