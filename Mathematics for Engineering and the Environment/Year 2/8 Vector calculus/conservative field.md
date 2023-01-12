---
aliases: ["conservative fields" ,"conservative vector field","curl of a conservative field"]
tags: []
---

## Conservative field

### Conservative field definition

A conservative vector field can be defined as the following:

> ### $$\begin{align*} \vec{F}  &=  - \nabla  \phi(x,y,z) \end{align*}$$
>> where:
>> $\vec{F}=$ a conservative [[vector fields|vector field]]
>> $\phi(x,y,z)=$ a [[scalar fields|scalar field]] where the [[del operator|grad]] can be evaluated at every point in the domain (continuous across domain)
>>
>>Note that $\phi(x,y,z)$ can be referred to as the potential for $\vec F$

This is often used when dealing with forces and potential energies, imagine a 3D chart representing terrain height then the terrain represents the potential and the gradient of the terrain represents the force needed to climb it. This interpretation of potentials in a force field is where the conservative nature comes in, since irrelevant of path the difference in height between two points in the potential field will be the same.

Something to note is that since this is a differential operator information is lost, for example it is the case that:
$$\begin{align*}
 \vec{F}  &=  - \nabla  \phi(x,y,z)=  - \nabla  (\phi(x,y,z) + C)
\end{align*}$$
Since in taking the gradient the effect of the constant $C$ is lost.

### Work done by a conservative vector field

As discussed previously, if we calculate work done to get between two points in the field $A,B$ then the potential difference is the same regardless of path. This is just [[line integral of a vector field]] and can be expressed as:

> ### $$\begin{align*} \int^{B}_{A} \vec F \cdot d\vec{s}  &= \phi(A) - \phi(B)  \end{align*}$$
>> where:
>> $A,B=$ 2 points in the field
>> $\vec{F}=-\nabla \phi=$ a [[conservative field]]
>> $\vec{s}=$ the [[formal definition of a parametric curve|curve]] describing the path between $A$ and $B$ where $\vec s$ can be any path

### Additional properties of a conservative field

 For a conservative field [[curl of a vector|curl]] is zero, the reverse is also true so if [[curl of a vector|curl]] is non zero the field is not conservative:
> ### $$\begin{align*} \text{conservative field:}&& \nabla \times \vec F &=  0\\\\ \text{non-conservative field:}&& \nabla \times \vec F &\neq  0 \end{align*}$$
>> where:
>> $\vec{F}=$  some [[vector fields|vector field]]
>> $\nabla \times...=$ [[curl of a vector]]

This becomes clear if you consider from [[vector identities]] that the [[curl of a vector|curl]] of the [[del operator|grad]] of a scalar field is always zero, and since the definition of a conservative field is $\vec F = - \nabla  \phi$ then the curl of $\vec F$ would be:
$$ \nabla\times(- \nabla  \phi) \equiv0 $$


