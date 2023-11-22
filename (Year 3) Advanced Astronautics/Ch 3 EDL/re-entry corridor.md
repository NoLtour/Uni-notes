---
aliases: ["the won't die region","overshoot boundary","undershoot boundary"]
tags: []
---

## Re-entry corridor

### Description

This is the region in-between the:
- Overshoot boundary, where missing can fling you back out. Depending on velocity possibly out of orbit.
- Undershoot boundary, where you get turned [[not ideal generally|into ash]].

So this is "the won't die region", generally we aim for this.

![[Pasted image 20231108171724.png]]

### How it kills you

Overshoot boundary:
- The minimum deceleration needed to capture the vehicle
- Heat saturation effects, if the vehicle spends too long re-entering and is not designed for long duration heating the internal structure could be compromised as heat seeps through the thermal protection system

Undershoot boundary:
- G forces above design condition
- Max heating above design condition
- Can't decelerate and burn up (unlikely for bodies with a dense atmosphere like Earth)

### Design mitigation (ballistic re-entry)

Considering what we've seen so far, for a ballistic entry there are limited options in changing design parameters to ensure survivability:
- Atmospheric density ($\alpha,\rho_{0}$), lmao good fucking luck changing this one
- Re entry angle ($\gamma$), not impossible but not easy
- Initial velocity, a waste of fuel that we don't have
- Ballistic coefficient, reasonably achievable
- Increase max $\dot Q$ or $\dot V$ tolerances, possible but probably expensive

So to expand the entry corridor our best shot's clearly manipulating ballistic coefficient. Failing that we can redesign the craft to be able to survive harsher conditions, though especially for crewed missions there are squishy components known as "humans" who turn into either paste or bacon if you push them to the extremes.

| Parameter change | max deceleration | max deceleration altitude | max heating rate | max heating altitude | landing accuracy | corridor width |
| ---------------- | ---------------- | ------------------------- | ---------------- | -------------------- | ---------------- | -------------- |
| Higher $V_{0}$   | increases        | no change                 | increases        | no change            | increases        | narrows        |
| Steeper $\gamma$ | increases        | decreases                 | increases        | decreases            | increases        | narrows        |
| Higher $B$       | no change        | decreases                 | increases        | decreases            | increases        | narrows        |
