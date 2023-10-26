---
aliases: [""]
tags: []
---

## Oblique shock interaction

Ok with all this talk of complex interaction how about we just make 2 [[oblique shocks]] intersect and [[peak entertainment|see what happens]]?

![[Pasted image 20231025194904.png]]

Ok so you have all the tools needed to find $\Delta$ (the angle between the slip line and walls). Huh? You've got no idea? Can't believe this.

The primary thing to recognise is the core properties of a [[Mach reflection|slip line]]:
- The velocities across a slip line are parallel (but not continuous)
- The pressure across a slip line is continuous

Velocities must be parallel across the slip line, so the [[oblique shock angles|flow turning angle]] on both walls must create parallel flow. Using this we can figure out both $\theta_{2B}$ and $\theta_{2A}$ using $\Delta$ (for now just guess some value for $\Delta$):
$$\begin{align*}
\theta_{2A} &= \theta_{A} - \Delta & \theta_{2B} &= \theta_{B} + \Delta
\end{align*}$$

Now the problem is "fully defined" and we can calculate $P_{3A}$ and $P_{3B}$... of course our guess probably sucked, so $P_{3A}\neq P_{3B}$; the boundary condition is violated, so we need to adjust $\Delta$ till it works. Boom we've just solved for $\Delta$.
