---
aliases: [""]
tags: []
---

## Thrust within an atmospheric environment

The [[the basic rocket equation|rocket equation]] is nice and all but it doesn't account for the effect of ambient pressure and how that interacts with the exhaust:

![[Pasted image 20221023104126.png]]

If we imagine the exit of the nozzle as a flat plate where the internal pressure and external pressure meet, we can calculate the net force acting in the direction of motion from the pressure difference:
$$ (P_{a} - P_{e})A_{e} = F_{atm} $$
A lower pressure inside the nozzle of course leads to a sort of vacuum effect which "pulls the rocket down" ([[um actually there is no such thing as suction just a difference in pressure which leads to the illusion of a vacuum creating a suction force|also stfu]]).

If we slap this onto the thrust equation we get:

> ### $$ T = \sigma V_{e} + (P_{a} - P_{e})A_{e} $$
>> where:
>> $V_{ex}=$ exhaust velocity (constant)
>> $T=$ thrust
>> $\sigma= \frac{dm}{dt}=$ mass flow rate of exhaust
>> $P_{a}=$ atmospheric pressure
>> $P_{e}=$ exhust pressure
>> $A_{e}=$ cross section area of nozzle exit

Depending on the relative size of $P_{a}$ compared to $P_{e}$ we either call the exhust over or under expanded:
- When $P_{e}<P_{a}$ it's over expanded, creating a 

