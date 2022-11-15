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
What we can do is guess that all the elements that make up the structure of the PDE are similar, if that's the case then the solution to the equation without the $F$ term should hold useful information... so for the sake of argument lets solve the homogeneous form of the equation:
$$\begin{align*}
 \frac{\delta y}{\delta t} &=  k^{2} \frac{\delta^{2} y}{\delta x^{2}}   \\
 \dot{T} &=  k^{2} X''
\end{align*}$$
$$\begin{align*}
\text{where:} & & y(0,t) &= 0 & y(1,t)&= 0
\end{align*}$$
(These boundary conditions are used since they are convenient)
This is of course solvable using the content from [[separation of variables]], (not going to prove this because pointless) if this is solved using the boundary conditions from the original equation you get:
$$\begin{align*}
y(x,t) & = \sum\limits^{\infty}_{n=1} T_{n}(t) \sin(n\pi x) 
\end{align*}$$
If we assume that the unknown function $F$ follows this format then it will look like:
$$ F(x,t) = \sum\limits^{\infty}_{n=1} F_{n}(t)\sin(n\pi x) $$
If we guess that these are in fact the solutions of $y$ and $F$ then we can test their validity by subbing back into the original equation and seeing the result:
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
It can be seen that both sides of the equation follow the same behaviour in $x$, this means that the shape of the graph resulting from both sides is similar and so the guess of $F$ and $y$ work! The real reason this method worked is really to do with the result of $\frac{\delta y}{\delta t}$, $\frac{\delta^{2} y}{\delta^{2} x}$ and $F$ all having the same behaviour, written another way:
$$\begin{align*}
\frac{\delta y}{\delta t} &\approx \frac{\delta}{\delta t} (T(t))\sin (knx) & &\to & (...(t))\sin (knx)\\
\frac{\delta^{2} y}{\delta x^{2}} &\approx  (T(t))\left[\frac{\delta^{2}}{\delta x^{2}}\sin (knx)\right] & &\to & (...(t))\sin (knx)\\
F& &&\to& (...(t))\sin(knx)
\end{align*}$$
The goal is to select [[ansatz]] for $y$ and $F$ such that when subbed in the behaviour makes sense, since to get $y$ using the traditional [[separation of variables]] method for it's homogenous case results in that convenient outcome it's suited for producing a good [[ansatz]].

S

