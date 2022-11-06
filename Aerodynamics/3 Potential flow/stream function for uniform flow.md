---
aliases: [""]
tags: []
---

## Stream function for uniform flow
Honestly the whole idea of [[stream function (2D)|stream function]] is kinda abstract, but it is essentially a function that describes the shape of flow. It'll be clearer once this example is done.

Lets say we want to find the stream function for a uniform flow:
![[Pasted image 20221106142734.png]]
It's clear that for this sort of uniform flow that:
$$\begin{align*}
V_{z} = w &= U_{\infty} \sin \alpha & V_{x} = u &= U_{\infty} \cos \alpha 
\end{align*}$$
Then we can take the definition of [[stream function (2D)|stream function]] and the method for [[derivative symbols#Example (and how to integrate these)|integrating partial derivatives]] to find the streamfunction:
$$\begin{align*}
V_{x} &= \frac{\delta \psi}{ \delta z } & V_{z} &= - \frac{\delta \psi}{ \delta x }   &  V_{z}  &= U_{\infty} \sin \alpha & V_{x}  &= U_{\infty} \cos \alpha \\
 U_{\infty} \cos \alpha &= \frac{\delta \psi}{ \delta z } & U_{\infty} \sin \alpha &= - \frac{\delta \psi}{ \delta x } \\
\int U_{\infty} \cos \alpha \delta z &= \int \delta \psi & \int U_{\infty} \sin \alpha \delta x &= - \int \delta \psi\\
zU_{\infty} \cos \alpha + f(x) &= \psi(x,z) & -xU_{\infty} \sin \alpha + f(z) &= \psi(x,z)\\\\
\therefore \:\psi(x,z) &= U_{\infty}( z \cos \alpha - x \sin \alpha )
\end{align*}$$

It is possible to do the same sort of method for finding [[velocity potential]], for defining a potential flow you can use one or the other. (Here if you do this method for [[velocity potential]] you'd get $\phi(x,z)= U_{\infty}( x \cos \alpha + z \sin \alpha )$ which is clearly at 90 degrees to the [[stream function (2D)|stream function]] as expected by defenition).

> ## $$ psi(x,z) = U_{\infty}( z \cos \alpha - x \sin \alpha ) $$ 
>> where:
>> $z,x=$ position
>> $U_{\infty}=$ flow speed
>> $\alpha=$ flow angle
>> $\psi=$ [[stream function (2D)|stream function]] of uniform flow at angle