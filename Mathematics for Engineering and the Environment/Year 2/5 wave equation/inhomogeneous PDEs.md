---
aliases: [""]
tags: []
---

## Inhomogeneous PDEs
You thought normal [[separation of variables]] was a pain? Well it gets worse, introducing inhomogeneous PDEs. For example this abomination:

$$ \frac{\delta y}{\delta t} = k^{2} \frac{\delta^{2} y}{\delta x^{2}} + F(x,t) $$

If we try the rearranging process from [[separation of variables#Separation]] we can't get the equation above into something useful, we just end up with:
$$ \frac{\dot{T}}{T} = k^{2} \frac{X''}{X} + \frac{F}{XT} $$
(useless)
What we can do is guess that all the elements that make up the structure of the PDE are similar, if that's the case then the solution to the equation without the $F$ term should hold useful information... so for the sake of argument lets solve the equation:
$$\begin{align*}
 \frac{\delta y}{\delta t} &=  k^{2} \frac{\delta^{2} y}{\delta x^{2}}   \\
 \dot{T} &=  k^{2} X''
\end{align*}$$
This is of course solvable using the content from [[separation of variables]], (not going to prove this because pointless) if this is solved using the boundary conditions from the original equation you get:
$$\begin{align*}
y & = \sum\limits^{\infty}_{n=1} T_{n}(t) \sin(n\pi x) 
\end{align*}$$
If we assume that the unknown function $F$ follows this format such that:
$$ F(x,t) = \sum\limits^{\infty}_{n=1} F_{n}(t)\sin(n\pi x) $$
If we then check the validity of this series of assumptions by subbing back into the original equation:
$$\begin{align*}
y & = \sum\limits^{\infty}_{n=1} T_{n}(t) \sin(n\pi x)
\end{align*}$$
$$\begin{align*}
\frac{\delta y}{\delta t} & = \sum\limits^{\infty}_{n=1} \dot{T}_{n}(t) \sin(n\pi x) & \frac{\delta^{2} y}{\delta x^{2}} & = -\sum\limits^{\infty}_{n=1} n^{2}\pi^{2} T_{n}(t) \sin(n\pi x) 
\end{align*}$$
$$\begin{align*}
 \frac{\delta y}{\delta t} &=  k^{2} \frac{\delta^{2} y}{\delta x^{2}} + F(x,t) & &\to &  \sum\limits^{\infty}_{n=1} \dot{T}_{n}(t) \sin(n\pi x) &=  -k^{2} \sum\limits^{\infty}_{n=1} n^{2}\pi^{2} T_{n}(t) \sin(n\pi x)  + \sum\limits^{\infty}_{n=1} U_{n}(t)\sin(n\pi x)\\
&&&& \sum\limits^{\infty}_{n=1} \dot{T}_{n}(t) \sin(n\pi x) &=  \sum\limits^{\infty}_{n=1} [   F_{n}(t) - (n k \pi)^{2} T_{n}(t) ]\sin(n\pi x)
\end{align*}$$



