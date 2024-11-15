---
aliases: [""]
tags: []
---

## Dynamics of rods FEA

![[Pasted image 20241112162625.png]]

This is similar to what we did in [[PMTPE in rods]], we also have the convenience that the [[shape function]] is the same so that doesn't need calculating. We only need to derive the [[shortcuts for Hamiltons Principle|mass matrix]].

Obviously we can't use point masses again, since now the mass is distributed along the length of the rod between our nodes. Writing out the kinetic energy equation for a small segment we get:

$$\begin{align*}
T &= \frac{1}{2} m \: dx \: [ \dot{u}(x,\:t) ]^{2} &&\to& T &= \frac{1}{2} \: \int^{L}_{0} m[ \dot{u}(x,\:t) ]^{2} \cdot dx
\end{align*}$$

The problem we encounter is that the local displacement and rate of change of displacement ($\dot{u}$) is obviously changing between the nodes, so we need a way to locally approximate it, probably based on the measurements of $q_{1}$ and $q_{2}$... aka we use the [[shape function]], like we did in [[PMTPE in rods]].

Once again a linear shape functions suitable, so we define:

$$\begin{align*}
u(x,t) &=  g_{1}(x) \dot{q}_{1}(t) + g_{2}(x) \dot{q}_{2}(t)
\end{align*}$$
$$\begin{align*}
g_{1}(x) &= 1 - \frac{x}{L} &&& g_{2}(x) &=  \frac{x}{L} 
\end{align*}$$

Subbing this back into the integral, we can reach our [[shortcuts for Hamiltons Principle|mass matrix]]:

$$\begin{align*}
T &= \frac{1}{2} \: \int^{L}_{0} m[ \dot{u}(x,\:t) ]^{2} \cdot dx &&\to& T &= \frac{1}{2} \: \int^{L}_{0} m[g_{1}(x) \dot{q}_{1}(t) + g_{2}(x) \dot{q}_{2}(t) ]^{2} \cdot dx &&\to& &... &&\to& T &= \frac{1}{2} \begin{pmatrix} \dot{q}_{1} \\ \dot{q}_{2} \end{pmatrix}^{T} \begin{pmatrix} \dfrac{mL}{3} & \dfrac{mL}{6} \\ \dfrac{mL}{6} & \dfrac{mL}{3} \end{pmatrix} \begin{pmatrix} \dot{q}_{1} \\ \dot{q}_{2} \end{pmatrix} 
\end{align*}$$

$$\begin{align*}
[M] &= \begin{pmatrix} \dfrac{mL}{3} & \dfrac{mL}{6} \\ \dfrac{mL}{6} & \dfrac{mL}{3} \end{pmatrix} 
\end{align*}$$

Then it's just subbing back into the equation in [[shortcuts for Hamiltons Principle]] after combining however many nodes you're dealing with.



