---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe
## Stress transformation for uniaxle loading
### Equations
![[Pasted image 20220221125353.png]]

> ### $$ \sigma_{x'x'} =\sigma_{xx} \cos^{2}\theta $$ 
>> where:
>> $\sigma_{x'x'}=$ normal stress on slice
>> $\sigma_{xx}=$ stress parrallel to external uniaxle loading
>> $\theta=$ angle of slice

> ### $$ \sigma_{x'y'} = \sigma_{xx}\sin\theta \cos\theta = \sigma_{xx} \frac{\sin2\theta}{2} $$ 
>> where:
>> $\sigma_{x'y'}=$ shear stress along slice
>> $\sigma_{xx}=$ stress parrallel to external uniaxle loading
>> $\theta=$ angle of slice

#### Implications
![[Pasted image 20220221125825.png]]

It should be noted that from looking at the graph, even a material in uniaxle loading expereinces a shear stress at 45 degrees equal to half the applied stress. Meaning that if a material has a shear strength less than half of it's longitudional strength then it can fail without getting to its maximum longidudinal load.

So clearly when applying stresses on materials their strength in all the different directions needs to be taken into account even if the force is only applied in one axis. If you think this is getting difficult to consider now, just wait till we get to 3D [[enjoy your slow descent into madness|lmao]].

### Proof

^1a0dc8

The important thing to understand about stresses is for the same stress state, normal and shear stresses depend on the orientation of the surface we are interested in. 

Heres a diagram represening uniaxial loading and a slice at angle theta through it:

![[Pasted image 20220221124420.png]]

It should now be noted that the total force through this slice will be equal to the force through a non angled slice:

![[Pasted image 20220221124604.png]]

So if we define the normal and perpendicular force as components of the force unrotated force we get the following:
$$\begin{align*}
F_{N} &= F \cos\theta & F_{S}&= F\sin\theta 
\end{align*}$$

Now we can also define the area of this slice as:
$$\begin{align*}
A_{\theta} &= \frac{A}{\cos\theta}
\end{align*}$$


![[Pasted image 20220221125036.png]]

So finally it becomes possible to define shear and normal stresses by dividing force by area:

$$\begin{align*}
\sigma_{x'x'} &= \frac{F \cos\theta}{\frac{A}{\cos\theta}} & \sigma_{x'y'} &= \frac{F\sin\theta }{\frac{A}{\cos\theta}}\\
&=\frac{ F}{A} \cos^{2}\theta & &=\frac{F}{A} \sin\theta \cos\theta\\
&=\sigma_{xx} \cos^{2}\theta  & &= \sigma_{xx}\sin\theta \cos\theta 
\end{align*}$$