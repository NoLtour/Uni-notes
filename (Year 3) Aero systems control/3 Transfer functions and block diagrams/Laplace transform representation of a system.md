---
aliases:
  - Laplace transform of a linear time-invariant system
  - Laplace domain transfer function
tags:
---

## Laplace transform representation of a system

### Intro

In [[Modelling of dynamic systems Overview|topic 2]] we found that the input-output of any [[linear systems|linear]] [[time-variant system|time-invariant]] system can be represented as:

$$\begin{align*}
a_{n}\frac{d^{n}y(t)}{dt^{n}} + ... + a_{2} \frac{d^{2}y(t)}{dt^{2}} + a_{1} \frac{dy(t)}{dt} + a_{0} y(t) &= b_{m}\frac{d^{m}u(t)}{dt^{m}} + ... + b_{2} \frac{d^{2}u(t)}{dt^{2}} + b_{1} \frac{du(t)}{dt} + b_{0} u(t)
\end{align*}$$

($y(t)$ is the response, $u(t)$ is the input)

It doesn't take a genius to realise this form is unwieldy. [[I have used this gag before|If only]] we could represent it as something simple like:

$$\begin{align*}
y &= Gu
\end{align*}$$

Well guess what, we can. Using a [[Laplace transform]]!

### Equation

I'm going to skip over the proof, the take away is that it's really easy to convert that [[linear systems|linear]] [[ordinary differential equation|ODE]] into a [[Laplace transform]]ed version:

> ![[Pasted image 20231028192745.png]]
> ### $$\begin{align*}  a_{n}\frac{d^{n}c(t)}{dt^{n}} + ... + a_{2} \frac{d^{2}c(t)}{dt^{2}} + a_{1} \frac{dc(t)}{dt} + a_{0} c(t) &= b_{m}\frac{d^{m}r(t)}{dt^{m}} + ... + b_{2} \frac{d^{2}r(t)}{dt^{2}} + b_{1} \frac{dr(t)}{dt} + b_{0} r(t) \\ &\downarrow \\ C(s) \:(a_{n}s^{n}+...+ a_{2} s^{2} + a_{1}s + a_{0}) &= R(s)\:(b_{m}s^{m}+...+b_{2}s^{2}+b_{1}s+b_{0}) \\ &\downarrow \\ G(s) = \frac{C(s)}{R(s)} &= \frac{b_{m}s^{m}+...+b_{2}s^{2}+b_{1}s+b_{0}}{a_{n}s^{n}+...+ a_{2} s^{2} + a_{1}s + a_{0} } \end{align*}$$
> ### $$ C(s) = G(s)\:R(s) $$
> ![[Pasted image 20231028193733.png]]
>> where:
>> $a,b=$ are [[time-variant system|time invariant]] coefficients
>> $c(t)=$ is the output signal function (the system's response) 
>> $r(t)=$ is the input signal function
>> $s=$ frequency
>> $G(s)=$ [[Laplace transform|Laplace]] domain [[transfer function]], multiplying it by the input function gets the output function (in the Laplace domain)
>> $R(s)=$ [[Laplace transform|Laplace]] domain input function
>> $C(s)=$ [[Laplace transform|Laplace]] domain response function
>> 
>> Critically, this form assumes that the initial conditions are zero!


That's about it, as will be seen later this form compliment's block diagrams nicely. Allowing for extremely complex systems to be practically managed.

### Example

#### Mass-spring damper

![[Pasted image 20231028194431.png]]

The systems response is a combination of 3 things, the spring, inertia change, damping:
$$\begin{align*}
F_{s} &= -kx & m \frac{d^{2}x}{dt^{2}} &= \sum\limits F & F_{d} &= -c \frac{dx}{dt} \\
& & &\downarrow\\
&&  \frac{d^{2}x}{dt^{2}} &=f-c \frac{dx}{dt} - kx\\
&&m \frac{d^{2}x}{dt^{2}} + c \frac{dx}{dt} + kx &= f(t)
\end{align*}$$

Note that here $f(t)$ represents some external force/input. What the entire goal is, is to find the response (function) to this $f$.

Then using the Laplace transform method, getting the [[transfer function]] is trivial.

$$\begin{align*}
m \frac{d^{2}x}{dt^{2}} + c \frac{dx}{dt} + kx &= f(t) &\to G(s) = \frac{X(s)}{F(s)} &= \frac{1}{ms^{2} + cs + k}
\end{align*}$$
