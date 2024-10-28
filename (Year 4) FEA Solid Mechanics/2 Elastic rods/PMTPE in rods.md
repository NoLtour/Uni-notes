---
aliases: []
tags:
---

## PMTPE in rods

![[Pasted image 20241024144716.png]]

Previously we worked with springs, now we're working with elastic rods... which are pretty much just springs where their properties are determined by geometry. 

Take the diagram, if we apply [[principle of minimum total potential energy|PMTPE]] using our previous knowledge we can derive strain energy. Recall that in the diagram, [[Youngs modulus]] and area are variable along the length.

$$\begin{align*}
&&&&&&k &= \frac{EA}{dx}\\
U &= \frac{1}{2}\int^{L} F \cdot du &&\to& U &= \frac{1}{2}\int^{L} k \:du \cdot du &&\to& U &= \frac{1}{2}\int^{L} \frac{EA}{dx} \:du \cdot du  &&\to& U &=\frac{1}{2} \int^{L}EA \left(\frac{du}{dx}\right)^{2}\cdot dx &&\to& U &= \frac{1}{2}\int^{L}EA u'^{2}\cdot dx
\end{align*}$$

Now we want to express the displacement throughout the element ($u$) from the displacement at the edges ($q_{1}$ and $q_{2}$) so we can solve that thing. If we assume $EA=const$ then we know that the function of $u$ will be linear:

$$\begin{align*}
u(x) &= a + bx
\end{align*}$$

This form isn't convenient or general though, so instead we do:

$$\begin{align*}
u(x) &= N_{1}(x) q_{1} + N_{2}(x) q_{2}
\end{align*}$$

Here $N$ represents a [[shape function]]. These enable interpolation of the displacement experienced away from nodes ($q$), so a simple approximation would be linear. Let's say that the closer you are to a node, the more representative that node is for the local displacement experienced:

$$\begin{align*}
N_{1} &= 1- \frac{x}{L} & N_{2} &= \frac{x}{L} 
\end{align*}$$

$$\begin{align*}
u(x) &= N_{1}(x) q_{1} + N_{2}(x) q_{2} &&\to& u(x) &= \left(1 - \frac{x}{L}\right) q_{1} + \left(\frac{x}{L }\right) q_{2}
\end{align*}$$
![[Pasted image 20241024152146.png]]

We can demonstrate how they relate the node displacements to the local displacements, for instance let's sub in $x=0,\frac{L}{2},L$ 

$$\begin{align*}
u(0) &= \left(1 - \frac{0}{L}\right) q_{1} + \left(\frac{0}{L }\right) q_{2} &&\to& u(0) &= q_{1} \\
u\left(\frac{L}{2}\right) &= \left(1 - \frac{L/2}{L}\right) q_{1} + \left(\frac{L/2}{L }\right) q_{2} &&\to& u\left(\frac{L}{2}\right) &= \frac{1}{2}(q_{1}+q_{2})\\
u(L) &= \left(1 - \frac{L}{L}\right) q_{1} + \left(\frac{L}{L }\right) q_{2} &&\to& u(L) &= q_{2} \\
\end{align*}$$

As you can see, the local displacement is just being interpolated from the state of the tips. Which is a reasonable assumption of the cross sections have constant properties, but otherwise a more complex [[shape function|interpolation function]] may be used. Obviously this shape function would be an approximation especially as the geometry of the beam becomes increasingly complex.


Hence with $u$ defined we can express the strain $\left(\frac{du}{dx}\right)$ like so:

$$\begin{align*}
u(x) &= \left(1 - \frac{x}{L}\right) q_{1} + \left(\frac{x}{L }\right) q_{2} &&\to&  \frac{du}{dx} &=  - \frac{q_{1}}{L}  + \frac{q_{2}}{L} &&\to&  \varepsilon(x) &= \frac{du}{dx} =  \begin{pmatrix} - \frac{1}{L} & \frac{1}{L} \end{pmatrix} \begin{pmatrix} q_{1}\\ q_{2} \end{pmatrix}
\end{align*}$$

Ok so back to the problem, we need $\frac{du}{dx}$. So let's sub it in.

$$\begin{align*}
&& \frac{du}{dx} &=  - \frac{q_{1}}{L}  + \frac{q_{2}}{L}\\

U &= \frac{1}{2}\int^{L}EA u'^{2}\cdot dx &&\to& U &= \frac{1}{2}\int^{L} \frac{EA}{L^{2}} (q_{2}-q_{1})^{2} \cdot dx
&&\to& U &= \frac{EA}{2L^{2}} (q_{2}-q_{1})^{2}\int^{L} 1 \cdot dx
&&\to& U &= \frac{EA}{2L } (q_{2}-q_{1})^{2} 
\end{align*}$$

Ok so recall [[shortcuts for PMTPE for springs]], we're going to do that here:

$$\begin{align*}
U &= \frac{EA}{2L } (q_{2}-q_{1})^{2}  &&\to&  U &= \frac{1}{2} \begin{pmatrix} q_{1} \\ q_{2} \end{pmatrix}^{T} \begin{pmatrix} \frac{EA}{L} & -\frac{EA}{L}\\-\frac{EA}{L} & \frac{EA}{L} \end{pmatrix}\begin{pmatrix} q_{1} \\ q_{2} \end{pmatrix}
\end{align*}$$

Recognise this form? It's because now the [[stiffness matrix]] has become obvious:

$$\begin{align*}
[K] &=  \begin{pmatrix} \frac{EA}{L} & -\frac{EA}{L}\\-\frac{EA}{L} & \frac{EA}{L} \end{pmatrix}
\end{align*}$$

Just like what was shown last time, this can be combined with a bunch of others to make long chains:

![[Pasted image 20241024164126.png]]
![[Pasted image 20241024164135.png]]

Note that we've completely ignored the potential energy part for [[principle of minimum total potential energy|PMTPE]], that's because it doesn't change. It's just a function of force and displacements so the actual structure between the nodes is irrelevant:

![[shortcuts for PMTPE for springs#^1ce236]]


