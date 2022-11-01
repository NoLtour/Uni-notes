---
aliases: ["virtual origin"]
tags: []
---

## Transition
We know from [[approximating a laminar BL profile]] and [[approximating a turbulent BL profile]] methods for modelling flow:
![[Pasted image 20221101220722.png]]
But the transition between the two cannot be as easily modelled, generally this transition region takes place somewhere between 300k to 1M [[Reynolds number]]. The question is how can we calculate drag while accounting for this region? The answer is that it is much easier than you'd think.

![[Pasted image 20221101233321.png]]

We know that [[momentum thickness and viscous drag|momentum thickness is directly proportional to viscous drag]], of course if we can find the momentum thickness at the end of the turbulent boundary layer we can easily find drag. That is where $x_{0}$ comes in, as can be seen above this "[[calculating drag across a plate with a transition region|virtual origin]]" of the turbulent region marks where the turbulant boundary layer would start from if you trace it's shape forward; hence if you can find length $x_{0}\to end$


