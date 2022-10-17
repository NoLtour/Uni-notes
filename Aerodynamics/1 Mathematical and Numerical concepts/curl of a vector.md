---
aliases: ["curl","vorticity"]
tags: []
---

## Curl of a vector

This is a vector which measures the vorticity of a point, for a 2D flow it is:

> ### $$ 2D:\:\: \vec {\omega} = \nabla \times \vec{V} = \left(\frac{\delta V_{y}}{\delta x} - \frac{\delta V_{x}}{\delta y} \right) \hat{e}_{z} $$  
>> where:
>> $\vec {\omega}=$ [[curl of a vector ]]
>> $\nabla=$ [[del operator]]
>> $\vec{V}=$ some vector
>> $\hat{e}_{z}=$ [[unit vector]] of $z$ direction (remember [[moment of linear momentum|angular momentum]] is represented in the vector normal to the plane of rotation, that's pretty much what's going on here)

There are 2 terms used to describe the state of some flow:
- Rotational, if vorticity is non-zero at certain point(s) in a flow, the flow is called rotational. This implies that the fluid elements have a finite angular velocity.
- Irrotational, if vorticity is zero at every point in a flow, the flow is called irrotational. This implies that the fluid elements have no angular velocity; rather, their motion through space is a pure translation.

![[Pasted image 20221017154156.png]]