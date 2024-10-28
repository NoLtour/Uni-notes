---
aliases: [""]
tags: []
---

## Distributed forces in PMTPE

Let's say instead of applying a force at the nodes, we have a force applied over a surface:

![[Pasted image 20241024170744.png]] ^5b771d

Things become complicated... obviously. Nice thing is if you recall the [[principle of minimum total potential energy|PMTPE]] equation for the strain energy, there's no force term, meaning this will only change our potential energy equation. So let's take the work equation:

$$\begin{align*}
V &= -W &&\to&V&=  -\int^{L_{E}}_{x=0} p_{0} \: dx  \:u(x)
\end{align*}$$
![[Pasted image 20241024171254.png]]

Here we sub in our [[shape function]] for $u$, let's use the one from [[PMTPE in rods]]:

$$\begin{align*}
&&u(x) &= \left(1 - \frac{x}{L}\right) q_{1} + \left(\frac{x}{L }\right) q_{2} \\
V&=  -\int^{L_{E}}_{x=0} p_{0} \: dx  \:u(x) &&\to&  V&=  -\int^{L_{E}}_{x=0} p_{0} \: dx  \:\left[\left(1 - \frac{x}{L_{E}}\right) q_{1} + \left(\frac{x}{L_{E} }\right) q_{2}\right]

&&\to&  V&=  -p_{0}  \:\left[\left(x - \frac{x^{2}}{2L_{E}}\right) q_{1} + \left(\frac{x^{2}}{2L_{E} }\right) q_{2}\right]^{L_{E}}_{x=0}
\end{align*}$$

Cleaning it up:

$$\begin{align*}
V&=  -p_{0}  \:\left[\left(x - \frac{x^{2}}{2L_{E}}\right) q_{1} + \left(\frac{x^{2}}{2L_{E} }\right) q_{2}\right]^{L_{E}}_{x=0} &&\to& 

V&=  -p_{0}  \:\left[\left(L_{E} - \frac{L_{E}}{2}\right) q_{1} + \left(\frac{L_{E}}{2 }\right) q_{2}\right] &&\to& 

V&=  -p_{0} L_{E} \:\left[ \frac{q_{1}}{2} + \frac{q_{2}}{2}\right] &&\to& 

V&=  -\frac{p_{0} L_{E}}{2} \:\left[ q_{1}+q_{2}\right]
\end{align*}$$

If we want to put this into the form preferred for [[shortcuts for PMTPE for springs|shortcuts for PMTPE]]:

$$\begin{align*}
V&=  -\frac{p_{0} L_{E}}{2} \:\left[ q_{1}+q_{2}\right] &&\to& V &= - \begin{pmatrix} \frac{p_{0} L_{E}}{2}\\ \frac{p_{0} L_{E}}{2} \end{pmatrix}^{T}  \begin{pmatrix} q_{1}\\q_{2} \end{pmatrix}

\\\\&&&& &= - \{F\}^{T} \{q\}
\end{align*}$$

Going back to the [[distributed forces in PMTPE#^5b771d|original problem]] then we can sub in these values for the force part of our equation:

![[Pasted image 20241024172637.png]]

Neato, the stiffness matrix just needs to be filled in and we could then solve it.
 