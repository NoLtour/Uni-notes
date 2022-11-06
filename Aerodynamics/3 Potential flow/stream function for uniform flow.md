---
aliases: [""]
tags: []
---

## Stream function for uniform flow
Honestly the whole idea of [[stream function (2D)|stream function]] is kinda abstract, but it is essentially a function that describes the shape of flow.

Lets say we want to find the stream function for a uniform flow:
![[Pasted image 20221106142734.png]]
It's clear that for this sort of uniform flow that:
$$\begin{align*}
V_{z} = w &= U_{\infty} \sin \alpha & V_{x} = u &= U_{\infty} \cos \alpha 
\end{align*}$$
Then we can take the definition of [[stream function (2D)|stream function]] and the method for [[derivative symbols#Example (and how to integrate these)|integrating partial derivatives]] to find the streamfunction:
$$\begin{align*}
V_{x} &= \frac{\delta \psi}{ \delta z } & V_{z} &= - \frac{\delta \psi}{ \delta x }   &  V_{z} = w &= U_{\infty} \sin \alpha & V_{x} = u &= U_{\infty} \cos \alpha \\
 U_{\infty} \cos \alpha &= \frac{\delta \psi}{ \delta z } & U_{\infty} \sin \alpha &= - \frac{\delta \psi}{ \delta x } \\
\int U_{\infty} \cos \alpha \delta z &= \delta \psi}{ \delta z } & U_{\infty} \sin \alpha &= - \frac{\delta \psi}{ \delta x }
\end{align*}$$
