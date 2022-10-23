---
aliases: [""]
tags: []
---

## Thrust within an atmospheric environment

The [[the basic rocket equation|rocket equation]] is nice and all but it doesn't account for the effect of ambient pressure and how that interacts with the exhaust:

![[Pasted image 20221023104126.png]]

If we imagine the exit of the nozzle as a flat plate where the internal pressure and external pressure meet, we can calculate the net force acting in the direction of motion from the pressure difference:
$$ (P_{a} - P_{e})A_{e} = F_{atm} $$
A lower pressure inside the nozzle of course leads to a sort of vacuum effect which "pulls the rocket down" ([[um actually there is no such thing as suction just...|also stfu]]).

If we slap this onto the thrust equation we get:
$$ T = \sigma V_{e} + (P_{a} - P_{e})A_{e} $$
