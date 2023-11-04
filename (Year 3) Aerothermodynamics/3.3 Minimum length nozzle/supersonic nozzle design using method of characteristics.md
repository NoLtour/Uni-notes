---
aliases: [""]
tags: []
---

## Supersonic nozzle design using method of characteristics

### Goal

So we hit a bit of a bombshell with [[wave wall interaction#Wave cancellation|wave cancellation]], if we eliminate all [[Mach lines and domains of influence|characteristic lines]] we can achieve a uniform straight flow out of our nozzle! Which is awesome!!!

![[Pasted image 20231104193853.png]]

That is basically what we are going to be doing now.

### Method

#### Setup

Problem simplification, the goal is to take the flow around a corner then design it's geometry such that the [[Mach lines and domains of influence|characteristic lines]] of the [[Prandtl–Meyer expansion fan]] get cancelled such that we get a uniform exit flow at a target Mach number$M_{e}$.

First of all, we can simplify the problem by exploiting symmetry.
![[Pasted image 20231104194156.png]]

Along the centre line we can work as if the [[Mach lines and domains of influence|characteristic lines]] are experiencing [[wave wall interaction|wave reflection]].

##### Setting $M_{e}$

$M_{e}$ will be a consequence of the angle of divergence at the throat $\theta_{max}$. This can be seen by looking at point D and working backwards to get the relationship. 

Starting at point D, we know that the flow must be normal to the centre line $\theta_{D}=0$, this allows us to get $R_{D}^{-}$ pretty easily:

$$\begin{align*}
R_{D}^{-} &= \theta_{D} + \nu_{D} & &\to & R_{D}^{-} &=   \nu(M_{e})
\end{align*}$$

Since this is a [[method of characteristics|Riemann invariant]] on the same [[Mach lines and domains of influence|characteristic line]] as C, we can equate $R_{C}^{-}$ and $R^{-}_{D}$. Then we can use the fact this is a [[Prandtl–Meyer expansion fan]] in a throat (aka flow is $M=1$ because [[converging diverging nozzles|choked]]) to get $\theta_{max}$ as a direct function of $M_{e}$:

$$\begin{align*}
&& R_{D}^{-} &=   \nu(M_{e}) &&& R_{C}^{-} &= \theta_{max} + \nu_{C} && & \theta_{max} &= \nu_{C} - \nu(M=0)\\
R_{C}^{-} &= R^{-}_{D} & &\to & R_{C}^{-} &= \nu(M_{e}) & &\to & \theta_{max} + \nu_{C}&= \nu(M_{e}) & &\to & \theta_{max} &=  \frac{\nu(M_{e})}{2}
\end{align*}$$

##### Finding centreline point coordinates

It's pretty much [[method of characteristics#Finding the interception]], but with some simplifications since we know it occurs on $y=0$. Just going to slap a slide in:

![[Pasted image 20231104202019.png]]

##### Setting up lines

![[Pasted image 20231104202113.png]]

As discussed previously this is a [[numerical and analytical solutions|numerical solution]], so the number of lines we draw from our [[Prandtl–Meyer expansion fan|expansion fan]] determines the accuracy. Thing's to note:
- The first line is at $90\degree$ so there is no point in doing anything with it
- The angles between $0\to \mu_{2}$ (angle of [[Prandtl–Meyer expansion fan#Terms|last mach line]]) are evenly spaced
- $\mu_{1}=0$ since this is [[converging diverging nozzles|choked flow]] so the entry Mach must be 1

#### Solving

##### Table setup

You can think of the problem in a table, first populate it with the known starting conditions:
![[Pasted image 20231104202627.png]]

##### Work out $R$'s

Then working out $R's$ is trivial. ([[method of characteristics#^bb94d9|Riemann invariant]])

![[Pasted image 20231104202811.png]]

##### Find other point properties

Mach number can be found from $\nu$ ([[Prandtl–Meyer expansion fan#Calculating|Prandtl-Meyer function]]), from there $\mu$ can be found ([[Mach cone|Mach triangle]]) and then the others are trivial.

![[Pasted image 20231104203200.png]]

##### Trace $R^{+}$ values

Tracing the [[Mach lines and domains of influence|characteristic lines]] from $C$ allows you to fill in $R^{+}$ since [[method of characteristics|Riemann invariants]] don't change:
![[Pasted image 20231104203430.png]]

### Find $R^{-}$ and trace values then calculate $\nu$ and $\theta$

1) We know at point 1 flow must be tangential to the centre line, hence $\theta_{1}=0$
2) From this $R^{+}$ can be found ([[method of characteristics#^bb94d9|Riemann invariant]])
3) Since 2, 3, 4 are on the same [[Mach lines and domains of influence|characteristic line]] they have the same $R^{+}$
4) With both [[method of characteristics|Riemann invariants]] we can find $\theta$ and $\nu$

![[Pasted image 20231104203620.png]]


##### Find other point properties

Mach number can be found from $\nu$ ([[Prandtl–Meyer expansion fan#Calculating|Prandtl-Meyer function]]), from there $\mu$ can be found ([[Mach cone|Mach triangle]]) and then the others are trivial.

![[Pasted image 20231104203959.png]]

##### Find no reflection properties for point 5

Since we have [[wave wall interaction|wave cancellation]], point 5 will have the same properties as point 4. Then we can find $x$ and $y$.

![[Pasted image 20231104204102.png]]

##### Repeat

Now simply keep repeating the last few steps till everything's calculated!

![[Pasted image 20231104204251.png]]

Keep track of which points are on the wall, so we can form a nozzle.

![[Pasted image 20231104204339.png]]
