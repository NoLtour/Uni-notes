---
aliases: [""]
tags: []
---

## Root loci and design

### Proportional gain control

Something to consider is that the [[root locus plot rules]] are for when $K$ aka [[proportional controller|proportional control]] is being varied, in the event that something else like [[integral controller|integral control]] or [[derivative controller|derivative control]] was being varied other properties of the plot would be changed.

![[Pasted image 20231126185122.png]]

In this example, we can see the effect of varying $K$. In the first system it is stable for all value's of $K$, while system 2 suggests that sufficiently high $K$ will put loci in the real axis and hence become unstable.

Clearly if we want more control over these systems we will need to adjust more than just [[proportional controller|proportional control]] $K$.


### Rule use

If the goal is to ensure loci avoid the positive real domain, then we can make clever use of the [[root locus plot rules]], by manipulating the control functions such that we get more zeros:

![[Pasted image 20231126191829.png]]


### Root loci for phase-lead and phase-lag compensation

A common application of systems control is in electrical signal processing
