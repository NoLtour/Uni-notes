---
aliases: ["reducing series blocks","series transfer function reduction"]
tags: []
---

## Transfer function series  manipulation

### Math

Going to finally actually show the utility I keep hyping up, take 2 [[transfer function]]s and put them in series:

![[Pasted image 20231029114300.png]]

We can express their inputs and outputs in the Laplace domain, as established in [[Laplace transform representation of a system|previous pages]]:

$$\begin{align*}
M &= G_{1} R & C &= G_{2} M
\end{align*}$$

The neat part comes here:

$$\begin{align*}
&& M &= G_{1} R\\
C &= G_{2} M & &\to & C &= G_{2} G_{1} R\\
&& && \therefore G_{R\to C} &= G_{2} G_{1}
\end{align*}$$

### Block diagram

Recall what's done to simplify electrical circuits ([[simplifying simple circuits]]), we often combine multiple elements into a single object which is equivalent. Well the exact same principle can be used in block diagrams!

![[Pasted image 20231029114933.png]]

This chaining can be continued through countless transfer functions! Allowing for significant simplification of complex systems.
