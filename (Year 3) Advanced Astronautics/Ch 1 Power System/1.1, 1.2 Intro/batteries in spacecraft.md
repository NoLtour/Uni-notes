---
aliases: ["battery discharge curve","battery","batteries"]
tags: []
---

## Batteries in spacecraft

### General

Batteries have relatively low energy densities, but since they directly output usable electrical power at a reasonably consistent voltage they can be convenient for short term missions as primary sources or as energy storage ([[primary and secondary power system|secondoary power system]]). 

When used as a [[primary and secondary power system|primary power system]] it's common to make use of more energy dense non-rechargeable battery chemistries, in modern times this is usually LiCFx. It should be noted that all batteries have some degree of non-reversible electrochemistry though in rechargeable batteries this leads to gradual degradation instead on single-use capability.

![[Pasted image 20231013100601.png]]

### Recharging

Thing is this annoying IV, variation doesn't get any better. If you  consider how it varies with charging up/down it'll look something like this:

![[Pasted image 20231013133545.png]]

Additionally most batteries degrade significantly faster when you use them outside of the range 10-90%, some can even become unrechargable if they drop to 0%. So to extend their lifetime and to have it act like a psudo-[[constant voltage source]] we generally operate them in that 10-90% range. (this range depends on the specific battery might be closer to 80-20%).
