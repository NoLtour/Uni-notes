---
aliases: [""]
tags: []
---

## Load per unit length on a wing

The wing itself can be thought of as a beam under a set of rather complex loading conditions:
- Lift, this creates a upward force, it follows a elliptical distribution (recall [[elliptic lift distrobution analysis]])
- Gravity, this imparts a downward force proportional to mass
- Inertial, [[load factor]] captures this for our purposes acts similarly to gravity
- Distributed loads exist (eg lift per unit area on the wing)
- Point loads exist (eg the engine)

Drawing the basics on a diagram it'll look something like:
![[Pasted image 20240302193756.png]]

An expression for the load per unit length can be written as the following:

> ### $$\begin{align*} p(x) &= l(x) - nW_{f} (x)|^{b}_{a} - n W_{w}(x) - nW_{e}(x_{e})|_{e}  \end{align*}$$
>> where:
>> $p(x)=$ the function for load per unit length interms of $x$ 
>> $x=$ distance from the wingtip
>> $l(x)=$ lift per unit length
>> $n=$ [[load factor]]
>> $W_{f}(x)|^{b}_{a}=$ weight of the fuel per unit length between distances a to b
>> $W_{w}(x)|^{b}_{a}=$ weight of the wing per unit length
>> $x_{e}=$ distance with reference to the engine
>> $W_{e}(x_{e})|_{e}=$ point weight of the engine from e
