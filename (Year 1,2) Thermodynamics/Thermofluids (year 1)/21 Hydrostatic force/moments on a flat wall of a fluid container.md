---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you find
## Net moments the wall of a fluid container
This is really simple, first you find the centre of force from the reaction of the wall and then you find the centre of force from the pressure force. This then you find the distance between them and multiply that by the magnitude of one of the forces (doesn't matter since both are equal, well hopefully becauase if they arn't equal forces then you will have a catastrophic failure):

> ### $$ M = |h_{p} - h_{r}| F_{H} $$ 
>> where:
>> $F_{H}=$ Horizontal compoment of force acting on one side of the wall 
>> $h_{p}=$ Vertical position of centre of pressure force
>> $h_{r}=$ Vertical position of centre of pressure force
>> $M=$ Moments acting on the wall

Note that this equation works for angled walls, you just need to make sure to be working with verticle positions and horizontal pressures.

$F_H$ might need to be calculated using some integration shite eg: $F_{H} = \int^{0}_{H} wp \cdot dh$

It is common for $h_{r}$ to just be half way down the wall, but sometimes if the reaction force isn't constant you will have to calculate the centre through other means (probably simularly to how you find $h_p$).
$h_p$ can probably be found using the equation [[hydrostatic force on a flat wall]].

