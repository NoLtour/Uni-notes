---
aliases: [""]
tags: []
---

## Nyquist stability criterion

One's titled [[bode plot stability criteria]] but this is [[Nyquist stability criterion]], but I can't change it for my notes ([[what do you mean I am being a twat|annoying]]).

> ### $$\begin{align*} \\\text{Unsable if:}&& Z &\neq0 \\\\\text{Nyquist stability criterion:}&& N&= P-Z  \end{align*}$$
> ### $$\begin{align*} N &= \text{Number of counter clockwise encirclements around -1 on the Nyquist diagram} \end{align*}$$
>> where:
>> $P=$ Number of unstable [[control system loop types|open-loop]] poles
>> $Z=$ Number of unstable [[control system loop types|closed-loop]] poles

So summarised, we need an equal amount of counter clockwise loops around -1 on our [[Nyquist plots|Nyquist plot]] to the number of unstable poles in $G_{OL}$.

That instability condition is obvious considering what we learned in [[determination of system stability]]. Clearly using the condition we can find how well our closed loop feedback is stabilising the system! Enabling controller design using [[Nyquist plots]].

### Example 1
![[Pasted image 20231209210025.png]]

Here there are no encirclements of $-1$, so $N=0$.

### Example 2

![[Pasted image 20231209211321.png]]

Given this plot, and the open loop transfer function, for what $K$ is this system stable?

$$\begin{align*}
G_{p} &= \frac{1}{s-3} &&& G_{c} &= K
\end{align*}$$

Through observation, this open loop system clearly has 1 unstable [[system transfer function feature definitions|pole]], so $P=1$. From the plot we can see that when $K>3,N=1$. That can be used with the stability criteria equation to get a function for stability:

$$\begin{align*}
&& P&= 1 && & \text{At: }K&>3 \\
&&& && &  N&= 1 \\
N &= P-Z &&\to& Z&= 1-N  &&\to& 

Z=\left\{\begin{aligned} 
&1,\text{unstable} && K\leq3 \\
&0,\text{stable} && K>3
\end{aligned}\right.
\end{align*}$$
