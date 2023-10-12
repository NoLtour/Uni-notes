---
aliases: [""]
tags: []
---

## Finding the neutral axis of a asymmetric cross section

The Neutral Axis (NA) is a line on which the bending stress is zero, so if we take the equation from [[bending a beam with assymetric cross sections|bending a beam with asymmetric cross section]] and set $\sigma_{xx}=0$:

$$\begin{align*}
0  &= \frac{ (M_{zz} I_{yy} - M_{yy} I_{yz}) y  + (M_{yy} I _{zz} - M_{zz} I_{yz}) z }{I_{yy} I_{zz} - I_{yz}^{2}} & &\to &0 &=  (M_{zz} I_{yy} - M_{yy} I_{yz}) y  + (M_{yy} I _{zz} - M_{zz} I_{yz}) z \\&&&& &....\\
&&& & \frac{y}{z} &= - \frac{M_{yy} I_{zz} - M_{z} I_{yz}}{M_{zz} I_{yy} - M_{y} I_{yz}}
\end{align*}$$

Recall that when working with beams we use the centre of area as the z,y origin, which means that the equation above $\frac{y}{z}$ can actually be used to define the gradient along which neutral points exist, and hence the neutral axis of the beam:

![[Pasted image 20230219153632.png]]

> ### $$\begin{align*}  \frac{y}{z}= \tan \phi &= - \frac{M_{yy} I_{zz} - M_{z} I_{yz}}{M_{zz} I_{yy} - M_{y} I_{yz}}  \end{align*}$$
>> where:
>> $M_{zz},M_{yy}=$ bending moments acting in xz and xy planes respectively
>> $I_{yy}, I_{zz}=$ [[second moment of area|2nd moment of area]] (equations found at [[bending a beam with assymetric cross sections#Final equation|this page]])
>> $I_{yz}=$ second moment of area along yz? 
>> $\phi=$ The angle of the neutral axis from z measured clockwise

Note that if the neutral axis is on the z axis or y axis (aka it's symettrical) then $I_{yz}=0$, so:
![[Pasted image 20230219155538.png]]



