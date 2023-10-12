---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the relationship between
## Torque and deformation in a circular beam
### Equation
#### Specific for circular beams
> ### $$ T =\frac{\pi G R^{4} \theta }{2L}  $$ 
>> where:
>> $R=$ Radius of circular beam
>> $G=$ [[shear modulus]]
>> $L=$ Beam length
>> $\theta=$ Rotation between beam faces
>> $T=$ Torque

#### Note this is a general formula
> ### $$ T = \frac{GJ\theta}{L} $$ 
>> where:
>> $J=$ [[polar second moment of area]]
>> $G=$ [[shear modulus]]
>> $L=$ Beam length
>> $\theta=$ Rotation between beam faces
>> $T=$ Torque

### Proof
We know that torque is just a moment acting around the midpoint:
![[Pasted image 20211207132036.png]]

If we take a slice as shown above, then find the force acting over a small distance and multiply it by the distance from where we are taking moments about (the centre) we can find the moment that counteracts the torque.
This force that is acting over the small distance can be expressed using the known [[shear stress in a circular beam (torsion)|stress that acts here]].

So we can get an expression for the force acting on this small section in a ring at distance r:

$$\begin{align*}
dF &= \tau (r\times d\psi \times dr)
\end{align*}$$
Since it's a small area we can multiply it by its distance to get the torque it resaults in:
$$\begin{align*}
dT &= r\times dF \\
&= r^{2}\times  \tau \times d\psi \times dr
\end{align*}$$

![[Pasted image 20211207133148.png]]

We also know that the total torque is the sum of all these tiny rings along the beams radius, hence:
$$\begin{align*}
T &= \int^{R}_0 \int^{2\pi}_0 r^{2}  \tau \cdot d\psi \cdot dr & \tau&=\frac{Gr\theta}{L}\\
T &= \int^{R}_0 \left[ r^{2} \frac{Gr\theta}{L}  \psi\right]^{2\pi}_0 \cdot dr\\
T &=  \int^{R}_0  \frac{Gr^{3}\theta}{L}  2\pi \cdot dr\\
T &= 2\pi \left[ \frac{Gr^{4}\theta}{4L}  \right]^{R}_0 \\
\therefore T &=\frac{\pi G R^{4} \theta }{2L} 
\end{align*}$$

This can then be simplified interms of the [[polar second moment of area]]:

$$\begin{align*}
T &= \frac{GJ\theta}{L}
\end{align*}$$