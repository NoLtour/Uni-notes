---
aliases: ["determining properties from poles and zeros"]
tags: []
---

## Determination of system stability

Well we've set the stage now, it's possible to look at [[system transfer function feature definitions|system transfer function features]] and determine stability at a glance.

### First order systems

Back in [[first order system step response]] we showed that system to be stable, but recall we stated that $T>0$. That is what determines stability. If we take the [[system transfer function feature definitions|poles]] of that system and slap em on a [[system pole-zero pattern|pole–zero plot]]:

![[Pasted image 20231029202441.png]]

For all values of $T>0$ it will be in the yellow region. What this actually translates to is stability. So long as the pole is negative the system will be stable.

You can prove this with [[too much math I skip|math]], but looking back at [[first order system step response]] and thinking about the effects of negative $T$ is good enough.

Also recall [[simple system response time metrics]], decreasing $T$ will obviously increase the rate at which you get a response. On the [[system pole-zero pattern|pole–zero plot]] this represents as, the more extreme the value (in the real axis), the faster the response.

### Second order systems

$$\begin{align*}
G(s)&= \frac{K \omega_{n}^{2}}{s^{2} + 2\zeta \omega_{n}s+ \omega_{n}^{2}}
\end{align*}$$

The [[system transfer function feature definitions|poles]] of a second order system, can be derived easily to the equation:

$$\begin{align*}
&s^{2} + 2\zeta \omega_{n}s+ \omega_{n}^{2} & &\to &  p_{1,2} &= \frac{-2\zeta \omega_{n} \pm \sqrt{4\zeta^{2} \omega_{n}^{2} - 4\omega_{n}^{2}}}{2}\\
&& && &= -\zeta \omega_{n} \pm \omega_{n}\sqrt{\zeta^{2} - 1}
\end{align*}$$

#### Real negative [[system transfer function feature definitions|poles]]

To get real poles $\sqrt{\zeta^{2} - 1}>0$, so (remember that $\zeta>0$):
$$\begin{align*}
\zeta^{2} - 1 &>  0 & & \to & \zeta^{2}  &>  1 & &\to & \zeta  &> 1
\end{align*}$$


Consequentially real negative poles must also mean the system is [[types of dampening (differentially modelled oscillator)|over damped]]. Plotting these poles on the [[system pole-zero pattern|pole–zero plot]]:

![[Pasted image 20231029210453.png]]

It can be seen that, so long as the poles are on the real axis the system will be [[types of dampening (differentially modelled oscillator)|over damped]]. If both poles are negative they will be stable.

#### Single negative pole

In the event of a single pole:
 

$$\begin{align*}
p_{1} &=  p_{2} \\
-\zeta \omega_{n} + \omega_{n}\sqrt{\zeta^{2} - 1}  &=  -\zeta \omega_{n} - \omega_{n}\sqrt{\zeta^{2} - 1} & &\to & \sqrt{\zeta^{2} - 1}  &=  - \sqrt{\zeta^{2} - 1} & &\to & \zeta  &=  1
\end{align*}$$

Hence the system must be [[types of dampening (differentially modelled oscillator)|critically damped]] and it's pole is real. On the [[system pole-zero pattern|pole–zero plot]] it will be:

![[Pasted image 20231029211011.png]]

It's stable so long as it is negative.

#### Complex poles

To get complex poles $\sqrt{\zeta^{2} - 1}<0$, so:
$$\begin{align*}
\zeta^{2} - 1 &<  0 & & \to & \zeta^{2}  &<  1 & &\to & \zeta  &<  1
\end{align*}$$

Hence the system must be [[types of dampening (differentially modelled oscillator)|under damped]]. On the [[system pole-zero pattern|pole–zero plot]] it will be:

![[Pasted image 20231029211736.png]]

Doing a bit of geometry:

$$\begin{align*}
H &= \sqrt{ (\omega_{n}  \sqrt{1-\zeta^{2}})^{2} + (-\zeta \omega_{n})^{2} } & &\to & H &= \omega_{n}\sqrt{   (1-\zeta^{2}) + \zeta^{2} } & &\to & H &= \omega_{n} 
\end{align*}$$

$$\begin{align*}
\cos(\phi)&= \frac{A}{H}= \frac{-\zeta \omega_{n}}{\omega_{n}} & &\to & \cos(\phi) &= -\zeta  & &\to & \zeta &= \cos\phi
\end{align*}$$

These geometric fact's mean that the [[system pole-zero pattern|pole–zero plot]] can have [[system transfer function feature definitions|poles]] anywhere on the line:

![[Pasted image 20231029212913.png]]

This gives a few interesting deductions:
- A lower damping ratio, means a lower magnitude real component
- A smaller magnitude real component implies lower stability
- Hence increasing damping ratio, increases stability
- Natural frequency is the hypotonus, hence it controls the magnitude of the system
- A higher natural frequency will cause faster system responses

![[Pasted image 20231029213246.png]]
