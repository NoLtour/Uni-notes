---
aliases:
  - hermite cubics
tags:
---

## Beam elements in pure bending

Previously we investigated [[PMTPE in rods and springs]], both of these elements are *basically* the same. They are just compressible elements, now we'll look at elements that can deflect transversely, beams. In this page we'll assume the beams rigid longitudinally, and just focus on transverse deformation.

Since we're now dealing with bending not only is the direction of deformation different, but we have rotation as an additional degree of freedom. This means that a two node beam (in pure bending) has 4 degrees of freedom! Which as we'll come to see really fucks with the [[shape function]].

Recalling the equation for bending, it's a function of [[second moment of area]] and [[Youngs modulus]]. We'll be taking the [[Euler-Bernoulli hypothesis assumptions]] for our analysis.

![[Pasted image 20241028102702.png]]

The strain energy stored in a bent beam can be given as:

$$\begin{align*}
U &= \frac{1}{2} \int^{L}_{0} EI \:[w''(x)]^{2} \cdot dx
\end{align*}$$

If we compare this to what we were working with in [[PMTPE in rods]]:

$$\begin{align*}
U &= \frac{1}{2}\int^{L}EA u'^{2}\cdot dx
\end{align*}$$

Then we can see that in this case there is an additional level of differentiation, if we want to avoid the long method of [[principle of minimum total potential energy|PMTPE]] described at the very start we need to adjust our approach. We skip over the proof, but switching out the linear [[shape function]] for a cubic one is the adjustment.

So in contrast to the 2 node linear one, we use what are called "[[beam elements in pure bending|hermite cubics]]" to capture the rotation and bending at the 2 nodes (4 DOF):

![[Pasted image 20241028105901.png]]

Which define the continuous function for transverse deflection $w(x)$ as:

$$\begin{align*}
w(x) &= f_{1}(x) q_{1} + f_{2}(x) q_{2}+ f_{3}(x) q_{3}+ f_{4}(x) q_{4}
\end{align*}$$
Looking at the equation, we can see that at the tips $q_{1}$ and $q_{3}$ are the value of $w$ ($w(0)=q_{1}$ and $w(L)=q_{3}$). It shouldn't come as a surprise then that by convention:
- $q_{1}=$ transverse deflection at node 1
- $q_{2}=$ rotation at node 1
- $q_{3}=$ transverse deflection at node 2
- $q_{4}=$ rotation at node 2

But how do we recover rotation? Recall we're operating under the [[Euler-Bernoulli hypothesis assumptions]], hence dealing with small deformations. We can use the small angle approximation to state that:

$$\begin{align*}
\theta &= \frac{dw}{dx}
\end{align*}$$

Now if you recall the plots of the shape function, if we looked at the value of the derivative at the ends they equal the angle values at the end ($w'(0)=q_{2}$ and $w'(L)=q_{4}$). Let's find $w''(x)$:

$$\begin{align*}
f_{1}(x) &= 1 - 3 \frac{x^{2}}{L^{2}} + 2 \frac{x^{3}}{L^{3}} &&\to& f_{1}'(x) &= - 6 \frac{x}{L^{2}} + 6 \frac{x^{2}}{L^{3}} &&\to& f_{1}''(x) &=  -  \frac{6}{L^{2}} + 12 \frac{x}{L^{3}} \\\\
f_{2}(x) &= x - 2 \frac{x^{2}}{L} + \frac{x^{3}}{L^{2}} &&\to& f_{2}'(x) &= 1 - 4 \frac{x}{L} + 3\frac{x^{2}}{L^{2}} &&\to& f_{3}''(x) &= - \frac{4}{L} + 6\frac{x}{L^{2}}\\\\
f_{3}(x) &=  3 \frac{x^{2}}{L^{2}} - 2 \frac{x^{3}}{L^{3}} &&\to& f_{3}'(x) &=  6 \frac{x}{L^{2}} - 6 \frac{x^{2}}{L^{3}} &&\to& f_{3}''(x) &=  \frac{6}{L^{2}} - 12 \frac{x}{L^{3}}  \\\\
f_{4}(x) &=  -  \frac{x^{2}}{L} + \frac{x^{3}}{L^{2}} &&\to& f_{4}'(x) &= - 2 \frac{x }{L} + 3\frac{x^{2}}{L^{2}} &&\to& f_{4}''(x) &=-  \frac{2}{L} + 6\frac{x }{L^{2}} \\\\
\end{align*}$$

Hence:

$$\begin{align*}
w(x) &= f_{1}(x) q_{1} + f_{2}(x) q_{2}+ f_{3}(x) q_{3}+ f_{4}(x) q_{4} &&\to& w''(x) &= f_{1}''(x) q_{1} + f_{2}''(x) q_{2}+ f_{3}''(x) q_{3}+ f_{4}''(x) q_{4} 
\end{align*}$$

Note that we didn't expand it, that's because when we sub back into the equation we actually care about:

$$\begin{align*}
U &= \frac{1}{2} \int^{L}_{0} EI \:[w''(x)]^{2} \cdot dx &&\to&   U &= \frac{1}{2} \int^{L}_{0} EI \:[f_{1}''(x) q_{1} + f_{2}''(x) q_{2}+ f_{3}''(x) q_{3}+ f_{4}''(x) q_{4} ]^{2} \cdot dx 
\end{align*}$$

Expanding it will become horrible, but eventually you can organise it into:

$$\begin{align*}
U &= ... &&\to& U &= \frac{1}{2} EI \begin{pmatrix} q_{1}\\q_{2}\\q_{3}\\q_{4} \end{pmatrix}^{T} \begin{pmatrix} 12 & 6L & -12 & 6L\\6L & 4L^{2} & -6L & 2L^{2}\\ -12 & -6L & 12 & -6L\\ 6L & 2L^{2} & -6L & 4L^{2} \end{pmatrix} \begin{pmatrix} q_{1}\\q_{2}\\q_{3}\\q_{4} \end{pmatrix} \\&&&& [K] &= IE \begin{pmatrix} 12 & 6L & -12 & 6L\\6L & 4L^{2} & -6L & 2L^{2}\\ -12 & -6L & 12 & -6L\\ 6L & 2L^{2} & -6L & 4L^{2} \end{pmatrix}
\end{align*}$$

There you go, we have the stiffness matrix!

