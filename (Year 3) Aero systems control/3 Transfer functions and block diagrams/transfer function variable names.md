---
aliases:
  - system gain
  - system time constant
  - system natural frequency
  - system damping
tags:
---

## Transfer function variable names
### Intro

Often when working with systems, we'll give names to some of the coefficients after rearranging the [[transfer function]] into a standard form. The specific's depend on the [[system orders|system order]].

### First order system

> ### $$ a_{1} \frac{dc}{dt} + a_{0} c = b_{0} r $$
> ### $$\begin{align*}   G(s)&= \frac{b_{0}}{a_{1}s+a_{0}}& &\to & G(s)&= \frac{b_{0}/a_{0}}{a_{1}/a_{0}s+a_{0}/a_{0}}& &\to & G(s)&= \frac{K_{p}}{\tau_{p} s+1}\end{align*}$$
> ### $$\begin{align*} K_{p} &= \frac{b_{0}}{a_{0}} & \tau_{p} &= \frac{a_{1}}{a_{0}} \end{align*}$$
>> where:
>> $a,b=$ are [[time-variant system|time invariant]] coefficients
>> $c(t)=$ is the output signal function (the system's response) 
>> $r(t)=$ is the input signal function
>> $s=$ frequency
>> $G(s)=$ [[Laplace transform|Laplace]] domain [[transfer function]], multiplying it by the input function gets the output function (in the Laplace domain)
>> $K_{p}=$ system gain, which determines how much the output will change for a given input.
>> $\tau_{p}=$ system time constant, determines speed of response to a change of input.

### Second order system

> ### $$\begin{align*}a_{2} \frac{d^{2}c}{dt^{2}} +a_{1} \frac{dc}{dt} + a_{0} c &= b_{0} r \end{align*}$$
> ### $$\begin{align*}G(s)&= \frac{b_{0}}{a_{2}s^{2} + a_{1}s+ a_{0}} & &\to & G(s)&= \frac{b_{0}/a_{2}}{a_{2}/a_{2}\:s^{2} + a_{1}/a_{2}\:s+ a_{0}/a_{2}} & &\to & G(s)&= \frac{K \omega_{n}^{2}}{s^{2} + 2\zeta \omega_{n}s+ \omega_{n}^{2}} \end{align*}$$
> ### $$\begin{align*} \omega_{n} &= \sqrt{\frac{a_{0}}{a_{2}}} & K &= \frac{b_{0}}{a_{2} \omega_{n}^{2}} = \frac{b_{0} }{ a_{0}} & \zeta &= \frac{a_{1}}{2a_{2} \omega_{n}} = \frac{a_{1}}{2\sqrt{a_{2}a_{0}} } \end{align*}$$
>> where:
>> $a,b=$ are [[time-variant system|time invariant]] coefficients
>> $c(t)=$ is the output signal function (the system's response) 
>> $r(t)=$ is the input signal function
>> $s=$ frequency
>> $G(s)=$ [[Laplace transform|Laplace]] domain [[transfer function]], multiplying it by the input function gets the output function (in the Laplace domain)
>> $K=$ system gain, which determines how much the output will change for a given input.
>> $\zeta=$ a measure of damping in the system
>> $\omega_{n}=$ natural frequency of oscillation

If you recognise this stuff from [[modelling oscillations of damped elastic systems using constant-coefficient differential equations]], well congrats. It's the [[no swear words in my Christian notes bigot|same shit]].
