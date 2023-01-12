---
aliases: [""]
tags: []
---

## Divergence theorem

Basically this states that the [[flux integrals|flux integral]] of some vector field $\vec{F}$ over some closed surface is equal to the same functions [[divergence operator|divergence]] of the volume bound by that surface. Expressed mathematically that is:

> ### $$\begin{align*} \iiint_{V} ( \nabla \cdot \vec{F} ) \: dV  &=  {{\subset\!\supset} \mathllap{\iint}}_{S=\delta V} \vec{F} \cdot d\vec{S} \end{align*}$$
>> where:
>> ${{\subset\!\supset} \mathllap{\iint}}_{S=\delta V}=$  this means the integral of a [[closed surface]] where $S$ is the [[defining surfaces|surface]] corresponding to the volume $V$
>> $\nabla\cdot=$ [[divergence operator]]
>> $\vec{F}=$ some vector field
>> $S=$ the closed [[defining surfaces|surface]] corresponding to the volume $V$
>> $V=$ 3D volume of interest

Thing is calculating [[flux integrals]] is hard, most of the time with flux integrals you have to break down the shape into multiple surfaces then solve tones of double integrals... so by using [[divergence theorem]] you can just work with the 3D geometry instead.

The [[divergence theorem]] is really useful when dealing with engineering problems and especially conservation problems. For instance mass conservation, we know that mass can only change if there is mass flow out of the system, [[divergence theorem]] can be used to quantify this.