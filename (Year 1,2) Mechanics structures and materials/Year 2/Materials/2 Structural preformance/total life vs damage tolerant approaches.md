---
aliases: ["total life approach","damage tolerant approach"]
tags: []
---

## Total life vs damage tolerant approaches

It can be a bitch to calculate the lifetime of a object, the 2 important ways are:
- Total life approach, prediction of both [[crack initiation (material fatigue)|crack initiation time]] and [[crack propagation rate (material fatigue)|crack propagation rate]]. May use notch models to account of stress concentration from geometry.
- Damage tolerant approach, [[you have to be shitting me are you this childish|based]] on typical inevitable starting cracks estimate the [[crack propagation rate (material fatigue)|crack propagation rate]] to get life.

So far we've mostly been considering using [[S-N curves]] and [[miners rule]] ect to find total life, but if you want to generate the [[S-N curves|S-N curve]] for a particular material you'll need to do [[testing to create S-N curves]], in these tests the surface finish matters a shit tone in how long it takes for [[crack initiation (material fatigue)|crack initiation]] which has a significant effect on material life. 
For these tests we generally use smoother materials and are therefore designing against [[crack initiation (material fatigue)|crack initiation times]] rather than [[crack propagation rate (material fatigue)|crack propagation]] (since generally initiation takes longer than propagation when considering fatigue). This is probably not realistic considering most products will start out with defects (unless it's some small or super polished thingy which does happen, think turbine blades). 
When considering most typical components a damage tolerant approach often makes more sense, for this we'll need to first find the typical starting defects for whatever we're working with then go from there.




