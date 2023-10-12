---
aliases: ["curl","vorticity"]
tags: []
---

## Curl of a vector

This is a vector which measures the vorticity of a point, for a 2D flow it is:

> ### $$ 2D:\:\: \vec {\omega} = \nabla \times \vec{V} = \left(\frac{\delta V_{y}}{\delta x} - \frac{\delta V_{x}}{\delta y} \right) \hat{e}_{z} $$
> ### $$ 3D:\:\: \vec {\omega} = \nabla \times \vec{F} = \left( \frac{\delta F_{z}}{\delta y} - \frac{\delta F_{y}}{\delta z} \right)\hat{e}_{x} - \left( \frac{\delta F_{z}}{\delta x} - \frac{\delta F_{x}}{\delta z} \right)\hat{e}_{y} + \left( \frac{\delta F_{y}}{\delta x} - \frac{\delta F_{x}}{\delta y} \right)\hat{e}_{z} = \det\begin{pmatrix} \hat{e}_{x} & \hat{e}_{y} & \hat{e}_{z} \\ \frac{\delta}{\delta x} & \frac{\delta}{\delta y} & \frac{\delta}{\delta z} \\ F_{x}  & F_{y}  & F_{z} \end{pmatrix} $$  
>> where:
>> $\vec {\omega}=$ [[curl of a vector ]]
>> $\nabla=$ [[del operator]]
>> $\vec{V}=$ some vector
>> $\vec{F}=$ some [[vector fields|vector field]] such that $\vec{F}(x,y,z)=F_{x}(x,y,z)\hat{e}_{x}+F_{y}(x,y,z)\hat{e}_{y}+F_{z}(x,y,z)\hat{e}_{z}$
>> $\det=$ [[determinant]] ([[finding the determinant of a 3x3 matrix]])
>> $\hat{e}_{z}=$ [[unit vector]] of $z$ direction (remember [[moment of linear momentum|angular momentum]] is represented in the vector normal to the plane of rotation, that's pretty much what's going on here)

There are 2 terms used to describe the state of some flow:
- Rotational, if vorticity is non-zero at certain point(s) in a flow, the flow is called rotational. This implies that the fluid elements have a finite angular velocity.
- Irrotational, if vorticity is zero at every point in a flow, the flow is called irrotational. This implies that the fluid elements have no angular velocity; rather, their motion through space is a pure translation.

![[Pasted image 20221017154156.png]]

Also a note:
![[Pasted image 20221123123540.png]]