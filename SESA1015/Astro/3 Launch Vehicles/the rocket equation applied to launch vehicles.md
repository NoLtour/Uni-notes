---
aliases: [""]
tags: []
---

## The rocket equation applied to launch vehicles

[[the basic rocket equation|The basic rocket equation]] is nice and all, but it doesn't account for drag, launch angle or gravity. This version does, I'm not doing the proof out of laziness though:

> ### $$ \Delta V = - V_{ex} \int^{M_{b}}_{M_{0}} \frac{1}{M} \cdot dM - \int^{t}_{0} g \sin(\gamma) \cdot dt - \int^{t}_{0} \frac{D}{M} \cdot dt $$ 
> ### $$ \Delta V = \Delta V_{ideal} - \Delta V_{g} - \Delta V_{D} $$ 
>> where:
>> $\Delta V=$ velocity change
>> $\Delta V_{ideal}=$ [[the basic rocket equation|ideal change in veloicty from exhust]]
>> $\Delta V_{g}=$ gravity loss
>> $\Delta V_{D}=$ [[drag force (dynamics)|drag]] loss
>> ![[Pasted image 20221022173350.png]]
