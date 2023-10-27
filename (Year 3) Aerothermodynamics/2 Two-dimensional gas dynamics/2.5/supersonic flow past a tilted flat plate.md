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

Practically, we've got to use either [[oblique shock chart]]s or the online calculator, doing this get's you:
$$\begin{align*}
\beta_{1L} &= 23.9\degree
\end{align*}$$
 

Can use the equation from [[oblique shock equations#^774680]] or a [[normal shock table]] using the method discussed there (we're using that method):

We'll get $M_{n1L}$ using:
$$\begin{align*}
M_{n1L} &= M_{1} \sin \beta & &\to & M_{n1L} &= 2 \sin 39\degree\\
&& && &= 1.259
\end{align*}$$

Then looking that up in the normal shock table, get's $M_{n2L}$ which is about 0.8077. Now to get $M_{2L}$ we use the inversion formula from [[oblique shock equations]]:

$$\begin{align*}
M_{2L} &= \frac{M_{n2L}}{\sin(\beta-\alpha)}\\
&= 1.67
\end{align*}$$

##### Find $P_{2L}$

We can get this quite easy from the NST getting: $p_{2L}=50.5\:kN/m^{2}$

### 2 Find lift, drag and pitching moment

This is actually quite easy. It's important to recognise that the only thing's actually exerting force on the plate are pressure forces, so we can ignore everything downstream. First draw a basic diagram to get an idea of how forces act:

![[Pasted image 20231027172412.png]]

The total force $N_{top}$ and $N_{bot}$ can be easily defined since pressure is constant across the top and bottom:

$$\begin{align*}
N_{t} &= c p_{2U} & N_{b} &= c p_{2L}\\
&= 16.5 \: kN/m & &= 50.5 \:kN/m & N &=    N_{b} - N_{t} \\
&& &&  &= 34\: kN/m
\end{align*}$$

So lift and drag can be [[skillz|easily]] defined:
$$\begin{align*}
L &=  N \sin\alpha  & D &= N\cos\alpha\\
&= 33.5 \:kN/m & &= 5.9\:kN/m
\end{align*}$$

Interestingly, this shows that even under the [[inviscid flow|inviscid]] assumption we can still get drag. This makes sense considering the entropy increase seen across [[oblique shocks]]. Unlike what was observed in [[Potential flow Overview|potential flow]] where we found [[flow over a rotating cylinder#Drag|drag to always be zero]].

This drag is [[wave drag]].

To get the pitching moment about the leading edge:

$$\begin{align*}
M_{LE} &= \int^{c}_{0} (p_{2U} - p_{2L})x\:dx\\
...\\
&= -17\:kN
\end{align*}$$

### 3 Find [[centre of pressure]] and [[aerodynamic centre]]

The centre of pressure's pretty easy to figure out intuitively, it will be at $c=0.5$ since the pressure is constant on the upper and lower surfaces.

The [[aerodynamic centre]] is equally trivial, since the [[centre of pressure]] is constant we know the [[aerodynamic centre]] must be located at the same spot ($c=0.5$).

This is quite different to what we generally see in normal aerofoils.

