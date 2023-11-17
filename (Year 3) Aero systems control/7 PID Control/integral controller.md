---
aliases: ["integral control"]
tags: []
---
 
### Concept

A simpleish form of feedback control: If there is an error, respond in proportion to it's integral.

![[Pasted image 20231116202255.png]]

### Transfer function

The [[transfer function]] is trivial:

> ### $$\begin{align*} u(t)  &= K_{i} \int^{t}_{0} e(t) \:dt \end{align*}$$
> ### $$\begin{align*} G_{c}  &= \frac{K_{p}}{s} \end{align*}$$
>> where:
>> $G_{c}=$ integral [[general control system|controller transfer function]]
>> $K_{p}=$ integral gain constant
>> $u(t)=$ controller response
>> $e(t)=$ error

### Response

To aid in the characterisation of the response, I'm going to use a simple [[general control system|plant dynamics transfer function]].

![[Pasted image 20231116202844.png]]

That being said the system isn't first order like what was observed in [[proportional controller|proportional control]]:
$$\begin{align*}
G &= \frac{K_{i}}{s} \frac{1}{Ts+1} & &\to & G &= \frac{K_{i}}{Ts^{2}+s}
\end{align*}$$

Unlike [[proportional controller|proportional control]] attempting to find key properties such as [[transfer function variable names|system natural frequency]] and [[transfer function variable names|system damping]] will yield invalid values, this is because 

From [[steady-state error#Generic transfer function]] we can tell that since this is a system with $n=1$ if given a step input the resulting [[steady-state error]] would be:

$$\begin{align*}
e_{ss} &= 0
\end{align*}$$

Then charting the step input response over a range of $K_{i}$ values:

![[Pasted image 20231116210508.png]]

As predicted, regardless of the magnitude of $K_{i}$ for this simple system it will always fully eliminate error!

Clearly at least for a step input, increasing the gain will increase response rate. That being said, comparing this to [[proportional controller|proportional control]] the response is REALLY slow. There are other effects also, especially with higher order systems, though these are best discussed when using the full PID stack.
