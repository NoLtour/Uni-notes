---
aliases: ["dominant pole"]
tags: []
---

## Effect of additional system poles

![[Pasted image 20231031123438.png]]

Here we slapped another [[transfer function]] into the system, this one adds a single [[system transfer function feature definitions|system pole]]. It's strength is clearly a function of $T_{a}$ (it's [[transfer function variable names|time constant]]).

Going to skip over the horrible math's, the takeaway is this graph:

![[Pasted image 20231031123721.png]]

Plotting the response (to a instantaneous impulse). We can see that as the strength of the added pole increases:
- The rate of oscillation slows
- The [[dynamic system response time metrics|rise time]] increases
- The [[dynamic system response time metrics|maximum overshoot]] increases

The reason this is the case is the systems "dominant [[system transfer function feature definitions|pole]]".
