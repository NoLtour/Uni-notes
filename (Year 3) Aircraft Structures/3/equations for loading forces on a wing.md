---
aliases: [""]
tags: []
---

## Equations for loading forces on a wing

Applying year 1 beams knowledge, we can obviously get bending and shear through integration:
 

> ### $$\begin{align*} \text{Shear force:}&& S(x)  &= \int^{s}_{x} p(x) \:dx\\\\\text{Bending moment:}&& M_{1}(x)  &= \int^{s}_{x} S(x) \:dx = \int^{s}_{x}\int^{s}_{x} p(x) \:dx\\\\\text{Torsion moment:}&& M_{2}(x)  &= \int^{s}_{x} m_{2}(x) \:dx \end{align*}$$
>> where:
>> $S(x)=$ shear force as a function of $x$
>> $M_{1}(x)=$ bending moment as a function of $x$
>> $M_{2}(x)=$ torsion moment as a function of $x$
>> $m_{2}(x)=$ torsion per unit length function
>> $p(x)=$ [[load per unit length on a wing]]
>> $s=$ length of the wing
>> $x=$ distance from wing tip

Of course since this is just applying distributed and point loads ([[load per unit length on a wing]]), the specifics can change. Conditions such as amount of fuel, drag and wing configuration will change the equation, but at the end of the day it's [[I am just vibing to this music|just a complicated beam]].

(the diagram uses $z$ instead of $x$ for the span wise coordinate, because WHY WOULD YOU BE CONSISTANT. ffs this is cancer.)
![[Pasted image 20240302203746.png]]
