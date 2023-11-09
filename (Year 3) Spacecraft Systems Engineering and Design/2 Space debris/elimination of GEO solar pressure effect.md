---
aliases: [""]
tags: []
---

## Elimination of GEO solar pressure effect

### Manipulating $\gamma$ and $\Gamma$

Looking back at the equation:

![[causes of GEO orbital precession#^5a6975]]

We can see that for a specific value of $\lambda_{sun} - \omega - \Omega$ we can get $\sin$ to be zero and hence eliminate this term:

$$\begin{align*}
\sin(\lambda_{sun} - \omega - \Omega) &= 0 &&\text{when: }&\omega + \Omega &= 90\degree \text{ or } 270\degree
\end{align*}$$

Tabulated the combinations to achieve this are:
![[Pasted image 20231109160904.png]]

Which is not super useful for operational GEO satellites as it significantly constrains where they can be, but if we want our graveyard orbit satellites to remain in place this fact is incredibly important!

### Manipulating [[orbital eccentricity]]

By keeping the eccentricity low, it actually means that sources of [[space drag]] will not lead to the satellite re-entering protected GEO:

![[Pasted image 20231109161325.png]]

This was found after extensive simulation, and is why we now opt for a tiny eccentricity rather than a large one.
