---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How would you get the
## Proof of the differential relationship between load, shear force and bending moment
### Proof
If we take the following diagram:

![[Pasted image 20211025164706.png]]

Then try to analyse it using [[method for constructing shear force and bending moment diagrams|method for evaluating shear force and bending moment diagrams]]:

We can get a diagram for a beam segment

![[Pasted image 20211025164816.png]]

Vertical equalibrium:
$$\begin{align*}
Q &= Q+dQ + dx\cdot w(x)\\
dQ &= -dx\cdot w(x)\\
\frac{dQ}{dx}&= -w(x)
\end{align*}$$
Here we can approximate the load as $dx\cdot w(x)$ because $dx$ is very small.

Prooving the equation:

> $$ \frac{dQ}{dx} = -w(x) $$ 
>> where:
>> $Q=$ The load on the beam
>> $x=$ the position along the beam
>> $w(x)=$ A function representing the load at a given point

If we also take the moment equalibrium (from the right side):
$$\begin{align*}
M + Q\cdot dx + \frac{dx^{2}}{2}w(x) &= M\\\\
Q\cdot dx + M + \frac{dx^{2}}{2}\cdot dx &= M+dM\\
Q\cdot dx &= dM\\
 Q &= \frac{dM}{dx}\\
\end{align*}$$
Note that $(dx)^{2}\approx 0$ because it was so small.

> $$ \frac{dM}{dx} = Q $$ 
>> where:
>> $M=$  The moment on the beam
>> $x=$ The position along the beam
>> $Q=$ The load on the beam

![[equation for the relationship between load, shear force and bending moment]]

### Examples
![[Pasted image 20211025171511.png]]

![[Pasted image 20211025171524.png]]