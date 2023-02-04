---
aliases: ["oblique impact","central impact"]
tags: ["Question","QFormat3"]
---

#### What's the method for
## Modeling particle impacts

We need:
- [[conservation of momentum]]
- [[impulse]]
- This thing: $e\times(velocity\:component \:of\: particles\: moving\: towords \:eachother)=velocity\: component \:of\: particles\: moving \:away\: from\:eachother$

Or put more nicely:
> ### $$ ( \underline{v}_{b1} - \underline{v}_{a1})e = \underline{v}_{a2} - \underline{v}_{b2} $$ 
>> where:
>> $e=$ [[coefficient of restitution]]
>> $\underline{v}_{a1} , \underline{v}_{b1}=$ velocity component parrallel to [[line of impact]] of particles a and b before collision 
>> $\underline{v}_{a2} , \underline{v}_{b2}=$ velocity component parrallel to [[line of impact]] of particles a and b after collision
>> $v_{b2}<v_{a2}$ and $v_{b1}>v_{a1}$

^7e60a8

Although there is a difference between [[modeling particle impacts|oblique impacts]] and [[modeling particle impacts|central impacts]], the equation above works for both... (oblique is just when the [[line of impact]] $\neq$ line of particle motion)

Some important further considerations when modelling particle collisions:
- Most constant/unidirectional forces can be ignored during collisions because the collisions occur over such a short time period
- Friction can still occur! Since the bounce is caused by a normal reaction, a proportional [[dynamic friction force|friction]] [[impulse]] can occur, for [[modeling particle impacts|oblique impacts]] you need to make sure the spheres are smooth!!!
