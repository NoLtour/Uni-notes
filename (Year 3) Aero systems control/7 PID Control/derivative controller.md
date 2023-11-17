---
aliases: ["derivative control"]
tags: []
---

### Concept

A simpleish form of feedback control: If there is an error, respond in proportion to it's derivative.

![[Pasted image 20231116212155.png]]

### Transfer function

The [[transfer function]] is trivial:

> ### $$\begin{align*} u(t)  &= K_{d} \frac{de(t)}{dt} \end{align*}$$
> ### $$\begin{align*} G_{c}  &= K_{i} s \end{align*}$$
>> where:
>> $G_{c}=$ derivative [[general control system|controller transfer function]]
>> $K_{i}=$ derivative gain constant
>> $u(t)=$ controller response
>> $e(t)=$ error

### Response

To aid in the characterisation of the response, I'm going to use a simple [[general control system|plant dynamics transfer function]].

![[Pasted image 20231116214058.png]]

The system is a bit funky:
$$\begin{align*}
G &=  \frac{K_{i} s  }{Ts+1} 
\end{align*}$$
It's not something that should really be used by itself, since it's unstable!

From [[steady-state error#Generic transfer function]] we can tell that since this is a system with $n=-1$ if given a step input the resulting [[steady-state error]] would be:

$$\begin{align*}
e_{ss} &= \infty
\end{align*}$$

Attempting to provide a pure derivative controller with a step input lead's to significant issues creating a highly unstable system... a step input actually creates an infinite response at time zero, and other functions also lead to extreme instability.

Proving it's effects in isolation are a pain, but the results are:
- Increases damping, but tends to amplify noise
- Doesn't really help in achieving steady state
- Also relatively insensitive to slowly changing errors

