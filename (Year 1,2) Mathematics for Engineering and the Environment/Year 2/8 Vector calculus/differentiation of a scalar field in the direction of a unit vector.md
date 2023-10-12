---
aliases: ["directional derivative"]
tags: []
---

## Differentiation of a scalar field in the direction of a unit vector

Upto this point when working with differentiation of [[scalar fields]] it's clear how to do it along the defined axis ($x,y,z$) but not for some arbitrary direction, turns out it's not that hard:

> ### $$ \frac{\delta f}{\delta \vec{\hat{n}}} = \nabla f \cdot \vec{\hat{n}} = |\nabla f|\cos\theta $$ 
>> where:
>> [[dot product (vectors)|dot product]] is used
>> $f=$ the function of some [[scalar fields|scalar field]]
>> $\vec{\hat{n}}=$ some arbitrary [[unit vector]]
>> $\nabla=$ [[del operator]]
>> $\theta=$ the angle between the $\nabla f$ and the unit vector $\vec{\hat{n}}$

If we breakdown what the above is essentially doing, it gets the gradient of the field using $\nabla f$ then by taking the [[dot product (vectors)|dot product]] with the unit vector it gets the magnitude of the gradient in the direction of the [[unit vector]], hence effectively finding the gradient in the direction of the unit vector which is equivilent to differentiating in the direction of the unit vector. ([[I wanted to a mem|pog]])

It also becomes obvious that in the case that:
- $\nabla f \cdot \vec{\hat{n}}=0$, the unit vector is tangent to the [[level line]]
- $\nabla f \cdot \vec{\hat{n}}=\nabla f$, the unit vector is tangent to the gradiant