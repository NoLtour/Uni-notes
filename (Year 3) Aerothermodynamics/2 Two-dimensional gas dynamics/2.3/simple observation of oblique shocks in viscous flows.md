---
aliases: ["sonic line" ]
tags: []
---

## Simple observation of oblique shocks in viscous flows

 

Ok so we like assumptions, they are fun. We mostly deal with [[inviscid flow]] because friction is a real pain in the ass. 

So if we imagine the case where we're dealing with a supersonic [[viscous flow]] over a surface, there will be a [[boundary layer]] as is typical with all real flows over a surface. How this interacts with shocks is absolutely horrible to model. Luckily for this module we only need a high level understanding of this phenomina.

![[Pasted image 20231025160043.png]]

We can take the [[boundary layer]] [[fluid no slip condition]], so there will be a gradient into $M_{1}$ as you leave the wall, clearly there will be some point where it transitions from subsonic to supersonic flow. This is marked by the sonic line. It should also be noted that the decreasing velocity gradient will have a corresponding increasing pressure gradient.

In the image above a incident shock is propagating towards our wall (probably originating from some wall out of the diagrams FOV). We can see this mess as it approaches the boundary layer:
- Across the shock $P_{2}>>P_{1}$, with this being more severe the stronger the shock, which is obviously an adverse pressure gradient
- In most regions the "information" about this pressure gradient can't back propagate as is the nature of supersonic flows
- Near the wall we have a unbroken region of subsonic flow, where information can easily back propagate
- The strong pressure gradient lead's to lots of backflow near the wall, creating separation bubbles and shearing the boundary layer

As we can see by the [[simple observation of oblique shocks in viscous flows|sonic line]], the flow converges then diverges:
- This divergence give's rise to a [[Prandtl–Meyer expansion fan|expansion fan]]. (details elaborated in later weeks)
- The convergence give's rise to compression waves, which coalesce into a single shockwave

Whether these reflective shock's exist depend on how strong the pressure gradient is.

Friction isn't real it can't hurt you. Please let us go back to [[inviscid flow]], I'll never complain about the [[SINGLE LINE EQUATIONS ARE A BLESSING|math vomit]] again! (Good luck [[this is why we make assumptions|modelling]] this lmao.)
 
