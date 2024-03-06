---
aliases: [""]
tags: []
---

## Full load and light load wing forces

### Load factor

Something of significance when considering the [[load per unit length on a wing]] is the state of the fuel:
- Where the tanks are located
- Their relative sizes
- The fuel contained inside

Consider the two extreme cases, one where the tanks are empty vs full, how do the load factors vary?

Assuming steady level flight $W_{f}n$ doesn't actually change, since $n= \frac{L}{W}$ where $L=W$ aka $n=1$. 

But in the event of [[effect of gusts on load factor|gusts and then their effect on load factor]], we get different load factors depending on the fuel weight:

$$\begin{align*}
n_{full}-1 &= \frac{\Delta L-\Delta P}{W_{full}} &&& n_{empty}-1 &= \frac{\Delta L-\Delta P}{W_{empty}}
\end{align*}$$

Considering the fact that $W_{full}>W_{empty}$ and that the lift changes are the same in both cases:

$$\begin{align*}
n_{empty}-1 &= \frac{\Delta L-\Delta P}{W_{empty}} &&\to& (n_{empty}-1)W_{empty} &=  \Delta L-\Delta P \\
&&n_{full}-1 &= \frac{\Delta L-\Delta P}{W_{full}} &&\to& W_{full} &= \frac{(n_{empty}-1)W_{empty}}{n_{full}-1}
\end{align*}$$
Then:
$$\begin{align*}
W_{full}&> W_{empty} &&\to& \frac{(n_{empty}-1)W_{empty}}{n_{full}-1}&> W_{empty}  &&\to& \frac{ n_{empty}-1 }{n_{full}-1}&> 1  &&\to&   n_{empty} &> n_{full} 
\end{align*}$$
Which makes sense, a lighter aircraft is more susceptible to the effect of external forces. This will of course have effects on the peak torsion, moments and shear experienced along the wing, so obviously we need to be able to model and design for this.

### Forces and moments

Although you might be inclined to think that this means that the forces experienced on the wings are lower in the full case, if you also consider the increase due to fuel weight the forces actually increase depending on the point on the wing! So it's complicated

![[Pasted image 20240302210319.png]]

Consider the case where we have 3 loading states:
- Case 1, small amount of fuel
- Case 2, medium amount of fuel located in one tank
- Case 3, full with fuel distributed across 2 tanks

Based purely on total weight: $n_{1}>n_{2}>n_{3}$, but the forces are quite messy: 
- If we consider the additional force created by a gust, represented in grey, it's the same total force in all cases.
- The wing's actual __structural__ weight ($W_{s}$) is the same in all cases, but it's effective weight ($W_{s}n$) is highest in case 1. The effective weight is represented with purple.
- The effective __engine__ weight ($W_{e}n$) is also highest in case 1, this is represented with a red arrow
- The interesting thing happens when considering the effective weight of fuel ($W_{f} n$), it's highest in case 3

As a consequence of these loading conditions:
- The moments about the root of the wing are easily predictable ($n_{1}>n_{2}>n_{3}$) leads to $M_{r1}>M_{r2}>M_{r3}$
- The moments about the pylon (engine bit) are highest in the heavy case (due to the fuel) $M_{p3}>M_{p1}$


