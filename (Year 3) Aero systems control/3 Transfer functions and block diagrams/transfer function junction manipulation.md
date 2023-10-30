---
aliases:
  - pickoff point manipulation
  - summing junction manipulation
tags:
---

## Transfer function junction manipulation

### Full transfer through a [[block diagram parts|summing junction]]

Like all the other transfers, this is a consequence of [[linear systems|linearity]]. It's possible to transfer entire blocks across [[block diagram parts|summing junctions]]:

> ![[Pasted image 20231029120400.png]]
> ### $$\begin{align*} C &= G[R\mp X] & &\equiv & C &= GR \mp GX \end{align*}$$
>> where:
>> $G(s)=$ [[Laplace transform representation of a system|Laplace domain transfer function]], multiplying it by the input function gets the output function (in the Laplace domain)
>> $R(s),\:X(s)=$ [[Laplace transform|Laplace]] domain input function
>> $C(s)=$ [[Laplace transform|Laplace]] domain response function


### Partial transfer through a [[block diagram parts|summing junction]]

In the event that there are different [[transfer function]]s acting on some [[block diagram parts|signals]] but not others, we can still transfer the blocks we just make use of inverting functions:
 
> ![[Pasted image 20231029121003.png]]
> ### $$\begin{align*} C &= GR \mp X & &\equiv & C &= G\left[ R \mp \frac{1}{G} X \right] \end{align*}$$
>> where:
>> $G(s)=$ [[Laplace transform representation of a system|Laplace domain transfer function]], multiplying it by the input function gets the output function (in the Laplace domain)
>> $R(s),\:X(s)=$ [[Laplace transform|Laplace]] domain input function
>> $C(s)=$ [[Laplace transform|Laplace]] domain response function


### Full transfer through a [[block diagram parts|pickoff point]]

A really similar thing can be done for [[block diagram parts|pickoff points]]:

> ![[Pasted image 20231029121758.png]]
> ### $$\begin{align*} C_{1} &= G R & & & C_{1} &= G R \\ C_{2} &= GR & &\equiv & C_{2} &= G R \\ C_{3} &= G R & & & C_{3} &= G R \end{align*}$$
>> where:
>> $G(s)=$ [[Laplace transform representation of a system|Laplace domain transfer function]], multiplying it by the input function gets the output function (in the Laplace domain)
>> $R(s)=$ [[Laplace transform|Laplace]] domain input function
>> $C_{x}(s)=$ [[Laplace transform|Laplace]] domain response functions

The math's proof is [[I only put it in for consistancy|really something]]. Might be too complex for you though.

### Partial transfer through a [[block diagram parts|pickoff point]]

> ![[Pasted image 20231029121643.png]]
> ### $$\begin{align*} C_{1} &= G R & & & C_{1} &= GR \\ C_{2} &= R & &\equiv & C_{2} &= G \frac{1}{G} R \\ C_{3} &=  R & & & C_{3} &= G \frac{1}{G} R \end{align*}$$
>> where:
>> $G(s)=$ [[Laplace transform representation of a system|Laplace domain transfer function]], multiplying it by the input function gets the output function (in the Laplace domain)
>> $R(s)=$ [[Laplace transform|Laplace]] domain input function
>> $C_{x}(s)=$ [[Laplace transform|Laplace]] domain response functions
