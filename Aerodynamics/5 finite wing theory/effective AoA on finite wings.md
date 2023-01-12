---
aliases: ["finite wing induced drag"]
tags: []
---

## Effective AoA on finite wings

> ### $$\begin{align*} \alpha_{eff}=\alpha - \alpha_{i}  \end{align*}$$
> ### $$\begin{align*} C_{l} &= a_{0}( \alpha - \alpha_{i} - \alpha_{L=0} )  \end{align*}$$
>> where:
>> $=$ 
>> $=$
>> $=$

The downwash from [[tip vortecies and downwash|tip vorticies]] changes the direction of the oncoming flow, this effectively changes the AoA of the airfoil:

![[Pasted image 20221210111635.png]]

The effective AoA is simply $\alpha_{eff}=\alpha - \alpha_{i}$. Since the direction of the oncoming flow is changed the lift and drag will also change by the angle induced on the flow $\alpha_{i}$. Something that should be kept in mind is that since the magnitude of downwash varies with distance from the win tips the induced and therefore effective angles of attack also vary along the wing.

If we calculate the $D'$ drag:

$$\begin{align*}
D' &= D \cos\alpha_{i} + L \sin\alpha_{i}
\end{align*}$$

If $w<<V_{\infty}$ then we can say:

$$\begin{align*}
D' &= D + L \alpha_{i}
\end{align*}$$
This is actually [[induced drag coefficient|induced drag]], and will exist even in the inviscid case:

$$\begin{align*}
D_{i}' &=  L \alpha_{i}
\end{align*}$$



