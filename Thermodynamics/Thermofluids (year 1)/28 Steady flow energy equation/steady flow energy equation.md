---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Steady flow energy equation
![[Pasted image 20220222145815.png]]

The equation below ([[steady flow energy equation]]) is really just an expression for the description above.

> ### $$ Q - W = \sum\limits_{out} m \left( C_{v} T + \frac{U^{2}}{2} + \frac{p}{\rho} + gz \right) - \sum\limits_{in} m\left(C_{v} T + \frac{U^{2}}{2} + \frac{p}{\rho} + gz\right) $$ 
> ### $$ Q - W = \sum\limits_{out} m \left( e_{h} + \frac{U^{2}}{2} + gz \right) - \sum\limits_{in} m\left(e_{h} + \frac{U^{2}}{2} + gz\right) $$ 
>> where:
>> $e_{h}=$ [[specific enthalpy]]
>> $C_{v}=$ [[constant volume specific heat]]
>> $Q=$ [[heat]] transfer into system across the [[system boundary]] (positive is heat in)
>> $W=$ work done, ’non-fluid’ energy transfer. For example electrical work increasing the fluid pressure in a pump. (positive is work extracted, negative is work in [[UNFINISHED STUFF|not 100% sure]])
>> $m=$ mass
>> $U=$ speed
>> $p=$ pressure
>> $\rho=$ density
>> $g=$ gravitational acceleration
>> $z=$ average height


This equation works on the assumption that the flow is [[steady flow|steady]] and [[inviscid flow|inviscid]], we can account for compressibility now if we need to via a density change.  

Tips:
- When dealing with ideal gasses it is often convenient to use the second form of the equation along with [[enthalpy#^a0bd5b]].
- Using [[ideal gas law#^e2b3c4|this form]] of the [[ideal gas law]] can be useful for determining pressure or density 