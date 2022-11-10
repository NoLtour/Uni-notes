---
aliases: [""]
tags: []
---

## Stream function for a vortex

Consider a flow which is irrotational for all points except for the origin which has a [[circulation]] of $\Gamma$:

![[Pasted image 20221110001216.png]]

The radial and angular velocities can be described as:
$$\begin{align*}
V_{\theta} &= \frac{c}{r} & V_{r} &=0
\end{align*}$$
Then we can use the identity of [[circulation]], but first we need to know the area of interest; here we know that the total [[circulation]] within any sized circle around the origin is $\Gamma$, a infentesimaly small line segment of the perimeter of a circle of radius $r$ can be defined as $d\vec{s}=rd\theta$ which is what we need for the equation of circulation:
$$\begin{align*}
\Gamma &= \int_{C} \vec{V} \cdot d\vec{s} && \to &  \Gamma &= \int_{0}^{2\pi} \vec{V} \cdot rd\theta && \to &  \Gamma &= \int_{0}^{2\pi} c d\theta \\&&&&&&&&&= -2\pi c
\end{align*}$$
Using the definition of $c$:
$$ V_{\theta} = - \frac{\Gamma}{2\pi r} $$
Then using the same method from [[stream function for uniform flow]] we can get it's stream function using the defs of $V_{\theta}$ and $V_{r}$ which with a bit of [[sometimes I cba to do extra detail on the proofs leave me alone|omitted maths]] gives us:
$$\begin{align*}
\psi (r,\theta) &= - \frac{\Gamma}{2\pi} \ln r
\end{align*}$$