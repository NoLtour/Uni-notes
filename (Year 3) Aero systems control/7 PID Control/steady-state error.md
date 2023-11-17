---
aliases:
  - generic transfer function for steady-state error
tags:
---

## Steady-state error

### Def

Steady state error is simply the difference between the desired value and actual value once a steady state is reached. Of course we want this to be zero (the fundamental goal of control systems), but that isn't always possible.

### Finding steady state error

![[Pasted image 20231116183848.png]]

It's relatively easy to derive the error function:

$$\begin{align*}
E &= \frac{R}{1+G}
\end{align*}$$

Then the [[final value theorem]] can be used to find the [[steady-state error]]:

> ### $$\begin{align*} \lim_{t\to\infty} e(t)  &=  \lim_{s\to0} s \frac{R(s)}{1+G(s)}  =  \lim_{s\to0} s E(s) \end{align*}$$
>> where:
>> $G=$ [[control system loop types|open-loop]] [[transfer function]]
>> $R=$ system input
>> $E=$ [[general control system|system error]]
>> $\lim_{t\to\infty} e(t)=$ [[steady-state error]]

Some inputs like sine waves don't really have "steady-states" in most cases, a common input when looking at steady state error is a [[step function]].

### Generic transfer function

Assume a generic transfer function of the form:

$$\begin{align*}
G(s) &= \frac{K}{s^{n}} \frac{a_{k} s^{k} + ... + a_{1}s + 1}{b_{l} s^{l} + ... + b_{1}s + 1 }
\end{align*}$$

This form of the generic transfer function emphasizes the type of system we are dealing with by capturing the order in the $s^{n}$ term. This allows for characterisation along the following:

$$\begin{align*}
\text{integrator}&\text{ number}&&\text{gain type (K)}\\\\
n &= 0: & K_{p} &= \text{position error constant}\\
n &= 1: & K_{v} &= \text{velocity error constant}\\
n &=2: & K_{a} &= \text{acceleration error constant}\\
\end{align*}$$

Now consider the effect of taking this generic transfer function to the limit $s\to0$:

$$\begin{align*}
\lim_{s\to0}  G(s) &= \lim_{s\to0} \frac{K}{s^{n}} \frac{a_{k} s^{k} + ... + a_{1}s + 1}{b_{l} s^{l} + ... + b_{1}s + 1 }  &&\to & \lim_{s\to0}  G(s) &= \lim_{s\to0} \frac{K}{s^{n}} \frac{0 + ... + 0 + 1}{0 + ... + 0 + 1 }   &&\to & \lim_{s\to0}  G(s) &= \lim_{s\to0} \frac{K}{s^{n}} 
\end{align*}$$

This property is why it is useful to rearrange into this form!

Recalling [[steady-state error#Finding steady state error]] we can sub in:

$$\begin{align*}
\lim_{t\to\infty} e(t)  &=  \lim_{s\to0} s \frac{R(s)}{1+G(s)} & &\to & \lim_{t\to\infty} e(t)  &=  \lim_{s\to0}  \frac{sR(s)}{1+ \frac{K}{s^{n}} }
\end{align*}$$

Then if we sub in various input functions: step input, ramp input, acceleration... We can determine the steady state error's from the integrator number $n$ alone:

![[Pasted image 20231116191614.png]]

(Exam critical ^, memorise)

There is an obvious trend at play here, but the main take away is how the steady state error is very predictable once the transfer function is in this generic form!

#### Examples

![[Pasted image 20231116192050.png]]

