---
aliases: ["mass moment of inertia","angular mass","rotational inertia","inertia matrix"]
tags: ["Question","QFormat3"]
---

#### What is
## Moment of inertia ($\underline{I}$)
The moment of inertia, otherwise known as the mass moment of inertia, angular mass, second moment of mass, or most accurately, rotational inertia, of a rigid body is a quantity that determines the torque needed for a desired angular acceleration about a rotational axis, akin to how mass determines the force needed for a desired acceleration. It depends on the body's mass distribution and the axis chosen, with larger moments requiring more torque to change the body's rate of rotation.
Can be thought of as the objects reaction to torque in some axis.

> ### $$ \underline{H} = \underline{I} \underline{\omega} $$ 
>> where:
>> $\underline{H}=$ [[moment of linear momentum|angular momentum]]
>> $\underline{\omega}=$ [[rigid body rotation around a fixed axis|angular velocity]]
>> $\underline{I}=$ [[moment of inertia]]

### Inertia matrix (For when you need to use moment of inertia in multi)

When dealing with 3D rotation you use the inertia matrix:

> ### $$ \underline{I} = \begin{pmatrix} I_{xx}  & -I_{xy} & -I_{xz} \\ I_{xy} & I_{yy} & -I_{yz}  \\ I_{xz} & -I_{yy} & I_{zz} \end{pmatrix} $$ 
>> where:
>> $\underline{I}=$ [[moment of inertia|inertia matrix]]
>> $I_{xx},I_{yy},I_{zz}=$ [[moment of inertia|moments of inertia]] for individual axis
>> $I_{xy},I_{yz},I_{zx}=$ [[product of inertia]]
 

