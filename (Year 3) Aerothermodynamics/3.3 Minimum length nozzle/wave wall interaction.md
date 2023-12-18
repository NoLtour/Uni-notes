---
aliases: ["wave cancellation","wave reflection"]
tags: []
---

## Wave wall interaction

### Intro

Recall:

![[Pasted image 20231104191936.png]]

We can see that [[Mach lines and domains of influence|characteristic lines]] reflect at the walls, there are 2 thing's that can happen when one hit's a wall:
- Wave reflection, the wave reflects (more common)
- Wave cancellation, there is no reflection (requires very specific conditions)

### Wave reflection

![[Pasted image 20231104192758.png]]

The wall causes the [[Mach lines and domains of influence|characteristic line]] to change direction so it's [[method of characteristics|Riemann invariant]] will be:

$$\begin{align*}
R^{-}_{W} &= \nu_{W} + \theta_{W}
\end{align*}$$

We know that the flow MUST be tangential to the wall (Else we'd have some fucked vacuum or mass deletion... so yeah), this means that at the wall flow angle equals wall angle $\theta=\theta_{W}$). Which means $\theta_{W}$ is known, so we can find $\nu_{W}$ from it's incident [[Mach lines and domains of influence|characteristic line]]'s [[method of characteristics|Riemann invariant]]:

$$\begin{align*}
R^{-}_{A} &= \nu_{W} - \theta_{W} & &\to & R^{-}_{A} + \theta_{W} &= \nu_{W} 
\end{align*}$$

With these two known, finding $R^{-}_{W}$ is trivial.
 
### Wave cancellation

Ok so these [[Mach lines and domains of influence|characteristic lines]] are a consequence of expansion ([[Prandtl–Meyer expansion fan|expansion fans]])... so what would happen if there was no need for a flow direction change? Aka:
$$\begin{align*}
\theta_{A} &= \theta_{W}
\end{align*}$$

![[Pasted image 20231104193645.png]]


