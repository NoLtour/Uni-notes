---
aliases: [""]
tags: []
---

## Supersonic flow past a tilted flat plate
### Problem
![[Pasted image 20231027123056.png]]

In the diagram we have the following values:

| $M_{1}=2$ | $P_{1}=30\:kN/m^{2}$ | $c=1\:m$ |   $\alpha=10\degree$  | 
| --------- | -------------------- | -------- | --- |

Solve for:
1) $M_{2U}$, $M_{2L}$, $P_{2U}$, $P_{2L}$
2) Lift, drag and pitching moment
3) Find [[centre of pressure]] and [[aerodynamic centre]]
4) Convert 2 and 3 to coefficient's

Although the problem seems daunting, it's just combining [[oblique shock equations]] with the [[Prandtl–Meyer expansion fan|Prandtl-Meyer function]].

#### 1 Find $M_{2U}$, $M_{2L}$, $P_{2U}$, $P_{2L}$

##### Find $M_{2U}$

Looking back at the [[Prandtl–Meyer expansion fan|Prandtl-Meyer function]], either we invert that abomination to solve for $M$ ([[I seem to be saying that a lot this year|good luck lmao]]) or...

We use the shock tables to get the $\nu$ for $M_{1}=2$, then we know that $M_{2}$ will be where $\nu(M_{2U})=\nu(M_{1})+10\degree$:

$$\begin{align*}
&& && && \text{N}&\text{ST}\\
\nu(M_{1}) &= 26.38\degree & &\to & \nu(M_{2U}) &= 36.38\degree & &\to & \nu(2.39) &= 36.38\degree\\
&& && && && \therefore M_{2U}&= 2.385
\end{align*}$$

##### Find $P_{2U}$

Since [[Prandtl–Meyer expansion fan]]s are modelled [[isentropic process|isentropically]] we can use the [[supersonic flow properties equations]] to get $P_{2U}$ (or the isentropic flow table):

$$\begin{align*}
\frac{p_{0}}{p_{1}} &= \left(1 + \frac{\gamma-1}{2} M_{1}^{2}\right)^{\frac{\gamma}{\gamma-1}} & \frac{p_{0}}{p_{2U}} &= \left(1 + \frac{\gamma-1}{2} M_{2U}^{2}\right)^{\frac{\gamma}{\gamma-1}} \\
&= 7.8247 & &= 14.2653
\end{align*}$$
$$\begin{align*}
p_{1}\left(\frac{p_{0}}{p_{1}} \div \frac{p_{0}}{p_{2U}}\right) &= p_{2U}\\
&= 16.5\:kN/m^{2}
\end{align*}$$

##### Find $M_{2L}$


