---
aliases: [""]
tags: []
---

## Circulation ($\Gamma$)
Circulation is a measure of a region of a [[vector fields|vector field]] to rotate (like [[curl of a vector|vorticity]] but over some area), if you define a region using the closed curve $C$:
![[Pasted image 20221109190551.png]]
Then we can define the contribution to total circulation at some point on the curve as the tangential velocity to the path $C$, hence it is the component of $V$ acting in the same direction of $C$ at some point and can therefor be described using a [[dot product (vectors)|dot product]]:
$$ d\Gamma = \vec{V} \cdot d\vec{s} $$
Then of course if we do this around the entire curve we get the integral:
$$ \Gamma = \int_{C} \vec{V} \cdot d\vec{s} $$ ^ce6f85

You know how I said it's "kinda" like [[curl of a vector|vorticity]] but over an area, well I lied. It can litterally be defined as [[curl of a vector|vorticity]] but over an area (apparently this can be proven using [[Stokes theorem]], yes that is the [[del operator]]):
$$ \Gamma = \int \int_{S} \nabla \times \vec{V} $$

Of course this means that if the flow is irrotational then the [[circulation]] in the area will be zero. Something to note is just like [[curl of a vector|vorticity]], [[circulation]] is positive in the clockwise direction.