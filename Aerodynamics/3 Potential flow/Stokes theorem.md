---
aliases: ["curl theorem"]
tags: []
---

## Stokes theorem

Stokes theorem is somewhat similar to [[divergence theorem]] since it equates the perimeter of an object and the region within that object, that's about where the similarities end though since stokes theorem applies to the surface bound by a closed.
Stokes theorem states that the [[curl of a vector|vorticity]] of a vector field bound by a surface is equal to the integral of the vector field acting in the same direction as the closed curve that bounds that surface:

> ### $$\begin{align*} \iint_{S} ( \nabla \times \vec{F} ) \cdot d\vec{S} &= \oint_{C=\delta S} \vec{F} \cdot d\vec{r}  \end{align*}$$
>> where:
>> $\oint_{C=\delta S}=$ integral of a closed curve $r$ around the surface $S$
>> $\nabla\times=$ [[curl of a vector]]
>> $S=$ the [[defining surfaces|surface]]
>> $r=$ the closed curve around the [[defining surfaces|surface]]
>> 
>> The page on [[flux integrals]] and [[line integral of a vector field]] will probably be useful when evaluating

This can also be applied such that:
$$\begin{align*}
\iint_{S_{1}} ( \nabla \times \vec{F} ) \cdot d\vec{S} &= \iint_{S_{2}} ( \nabla \times \vec{F} ) \cdot d\vec{S}
\end{align*}$$
Where both are bound by the same curve.