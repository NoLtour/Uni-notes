---
aliases: ["proportional control","integral controller","differential controller"]
tags: []
---

## Proportional controller 

### Concept

This is the simplest form of feedback control: If there is an error, respond in direct proportion to it's magnitude.

![[Pasted image 20231116181704.png]]

In real systems there is a "proportional band" beyond which you can't have a stronger response, in this module we ignore that.

### Transfer function

The [[transfer function]] is trivial:

> ### $$\begin{align*} u(t)  &= K_{p}e(t)  \end{align*}$$
> ### $$\begin{align*} G_{c}  &= K_{p}  \end{align*}$$
>> where:
>> $G_{c}=$ proportional [[general control system|controller transfer function]]
>> $K_{p}=$ proportionality constant
>> $u(t)=$ controller response
>> $e(t)=$ error

### Response (first order)

To aid in the characterisation of the response, I'm going to use a simple [[general control system|plant dynamics transfer function]]

![[Pasted image 20231116192718.png]]

The system transfer function can be easily found, and then we can simplify and rearrange it to be in [[transfer function variable names#First order system|a standard first order system form]]:

$$\begin{align*}
\frac{C}{R} &= \frac{K_{P} \frac{1}{Ts+1}}{1+ K_{P} \frac{1}{Ts+1}} & &\to & \frac{C}{R} &= \frac{\left(\frac{ K_{p}}{1+  K_{P}}\right)}{\left(\frac{T}{1+  K_{P}}\right)s + 1}
\end{align*}$$

From this it's obvious that the [[transfer function variable names|system gain]] and [[transfer function variable names|system time constant]] have the equations:

$$\begin{align*}
K_{gain} &= \frac{ K_{p}}{1+   K_{P}} & \tau_{s} &= \frac{T}{1+  K_{P}}
\end{align*}$$

Clearly overall system gain increases with $K_{p}$ and the response time decreases. 

#### Steady state error

From [[steady-state error#Generic transfer function]] we can tell that since this is a system with $n=0$ if given a step input the resulting [[steady-state error]] would be:

$$\begin{align*}
e_{ss} &= \frac{1}{1+K_{P}}
\end{align*}$$

Then charting the step input response over a range of $K_{p}$ values:

![[Pasted image 20231116195330.png]]

Clearly at least for a step input, increasing the gain will both:
- Decrease [[simple system response time metrics|settling time]] (a function of $\tau_{s}$)
- Decrease [[steady-state error]]

In reality there may be practical limitations in the magnitude of proportional response that can be provided.

### Response (second order)

![[Pasted image 20231116200007.png]]

The transfer function is easily derived:

$$\begin{align*}
\frac{C}{R} &= \frac{K_{P}}{s^{2} + as + (b+K_{P})}
\end{align*}$$

Then the effect of varying $K_{p}$ can be described by how it effects [[transfer function variable names|system natural frequency]] and [[transfer function variable names|system damping]]. After subbing into those relationships ([[proof not needed bozo|skipping]] the working):

$$\begin{align*}
\omega_{n} &= \sqrt{b + K_{p}} & \zeta &= \frac{a}{2\sqrt{b+K_{p}}}
\end{align*}$$

Hence we can see that making the proportional controller gain greater will:
- Increase natural frequency, hence increasing oscillation rate
- Decrease damping, hence making the oscillation's more intense

#### Steady state error

From [[steady-state error#Generic transfer function]] we can tell that since this is a system with $n=0$ if given a step input the resulting [[steady-state error]] would be:

$$\begin{align*}
e_{ss} &= \frac{1}{1+K_{P}}
\end{align*}$$
Which is exactly what was seen in a first order [[general control system|plant dynamics transfer function]].

Then charting the step input response over a range of $K_{p}$ values:

![[Pasted image 20231116201203.png]]

Clearly at least for a step input, increasing the gain will both:
- Decrease steady state error
- Decrease [[simple system response time metrics|settling time]]
- Increase oscillation intensity and rate

Although similar to the previous result, the key observation is that in higher order systems proportional control systems induce generally undesired oscillatory motion. So any solution using purely proportional control has serious trade offs.
