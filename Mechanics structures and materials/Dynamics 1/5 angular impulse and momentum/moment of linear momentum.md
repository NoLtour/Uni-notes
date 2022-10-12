---
aliases: ["moment of momentum","angular momentum"]
tags: ["Question","QFormat3"]
---

#### What is a
## Moment of linear momentum ($H_{O}, \underline{H_{O}}$)
Moment of linear momentum is basically the general case of [[moment of linear momentum|angular momentum]].

Moment of momentum measures an objects tendency to continue to spin, it describes the rotary inertia of a system in motion about an axis. It can be applied to situations involving [[Curvilinear motion notes|curvilinear motion]].

### Angular momentum of a point mass

> ### $$ \underline{H_{O}} = \underline{r} \times (m \underline{v}) $$ 
> ### $$ \underline{H_{O}} = \underline{r} \times \underline{p} $$ 
>> where:
>> $\underline{H_{O}}=$ [[moment of linear momentum]]
>> $\underline{p}=$ particles momentum
>> $\underline{r}=$ the position expressed as a displacement vector from the origin (often the point it's rotating around)
>> $m=$ mass
>> $\underline{v}=$ [[velocity and speed|velocity]]
>> (This is making use of [[cross product (vectors)|cross product]])

The equation above works for 3D and 2D, but for 2D problems it is often easyer to use:

> ### $$ H_{O} = mvr \sin \theta $$ 
>> where:
>> $=$ 
>> $=$[[UNFINISHED STUFF]]
>> $=$

![[Pasted image 20220221183830.png]]

### Angular momentum of a rotating body
The point mass is kinda useless for most of our use cases, so this form is what we'll often use:

> ### $$ \underline{H} = \underline{I} \underline{\omega} $$ 
>> where:
>> $\underline{H}=$ [[moment of linear momentum|angular momentum]]
>> $\underline{\omega}=$ [[rigid body rotation around a fixed axis|angular velocity]]
>> $\underline{I}=$ [[moment of inertia]]
 
As long as you have some definition for the [[moment of inertia]] it becomes easy to relate [[rigid body rotation around a fixed axis|angular velocity]] and [[moment of linear momentum|angular momentum]].

In 3D you get this:
> ### $$ \underline{H} = \begin{pmatrix} I_{xx}  & -I_{xy} & -I_{xz} \\ I_{xy} & I_{yy} & -I_{yz}  \\ I_{xz} & -I_{yy} & I_{zz} \end{pmatrix} \begin{pmatrix} \omega_{z} & \omega_{y}  & \omega_{z} \end{pmatrix} $$ 
>> where:
>> $\underline{H}=$ [[moment of linear momentum|angular momentum]]
>> $\underline{\omega}=\begin{pmatrix} \omega_{z} & \omega_{y}  & \omega_{z} \end{pmatrix}=$ [[angul;a]]
>> $\underline{I}=\begin{pmatrix} I_{xx}  & -I_{xy} & -I_{xz} \\ I_{xy} & I_{yy} & -I_{yz}  \\ I_{xz} & -I_{yy} & I_{zz} \end{pmatrix}=$ [[moment of inertia]] ([[moment of inertia|inertia matrix]])
