---
aliases: ["finding beta for oblique shocks","solving oblique problems"]
tags: []
---

## Oblique shock equations



### [[oblique shock angles|Turning angle]] ($\theta$)

![[Pasted image 20231024153441.png]]
 

For a start we need to define [[oblique shock angles|theta]], generally we do this by assuming the streamlines run tangential to the surface of our object, allowing us to take it based on the surfaces angle relative to the incoming flow. 

### [[oblique shock angles|Shock angle]] ($\beta$) and [[Mach number]] ($M_{2}$)

#### Equation

##### tldr

> ### $$\begin{align*}   \tan\theta&= 2 \frac{1}{\tan\beta} \left[\frac{M_{1}^{2} \sin^{2}\beta - 1 }{M_{1}^{2}(\gamma + \cos 2\beta)+2}\right]   \end{align*}$$   $$\begin{align*}   M^{2}_{2}  &= \frac{1}{\sin^{2}(\beta-\theta)}   \frac{(\gamma - 1) M^{2}_{1} \sin^{2} \beta + 2}{2\gamma M^{2}_{1} \sin^{2} \beta - (\gamma - 1)}    \end{align*}$$
> ### $$\begin{align*} M_{n1} &= M_{1} \sin \beta  & \text{find }M_{n2}&\text{ from NST}(M_{n1})\text{ then use}& M _{2} &= \frac{M _{n2}}{\sin (\beta-\theta)} \end{align*}$$
>> where $X_{1}\to X_{2}$ is the [[adiabatic expansion or compression|adiabatic]] expansion across the shock and:
>> $M=$ [[Mach number]] before and after shock
>> $M_{n}=$ [[Mach number]] normal to [[oblique shocks|oblique shock]] before and after
>> $\theta=$ [[oblique shock angles|turning angle]]
>> $\beta=$ [[oblique shock angles|shock angle]]
>> $\text{NST}=$ normal shock tables, equivalent to using [[normal shock properties equations]]
>> 
>> Note that the bottom 2 equations are simply alternative methods of calculation, and practically you will need to find $\beta$ from normal shock tables since rearranging isn't practical.

^774680

##### Proof

First the flow's components need to be defined, this is done normally and tangentially to the [[oblique shock angles|shock angle]].

![[Pasted image 20231024164504.png]]

Drawing it out as done above, it becomes clear we can define these trivially:

$$\begin{align*}
M_{n1} &= M_{1} \sin \beta & M_{n2} &= M_{2} \sin(\beta-\theta) \\
M_{t1} &= M_{1} \cos \beta & M_{t2} &= M_{2} \cos(\beta-\theta)
\end{align*}$$

These can also be described as velocities in terms of tan:
$$\begin{align*}
M_{n1} &= M_{t1} \tan\beta  & M_{n2} &= M_{t2} \tan(\beta-\theta) \\
&\downarrow& &\downarrow\\
V_{n1} &= V_{t1} \tan\beta  & V_{n2} &= V_{t2} \tan(\beta-\theta) 
\end{align*}$$


This helps contextualise the problem but we'll need more, so let's attempt to apply the same control volume method previously done to get [[normal shock properties equations]]:

![[Pasted image 20231024165051.png]]

Here we can consider how the control surface modifies flow normal and tangentially to the [[oblique shocks|oblique shock]]:
- ($V_{n1} > V_{n2}$) Normal flow will undergo changes, likely similar to what's experienced by flow through [[normal shock properties equations|normal shocks]]
- ($V_{t1} = V_{t2}$) Tangential flow doesn't pass through the boundary, hence it will not experience changes

Purely dealing with the velocity components we can apply the above observations across this [[oblique shocks|oblique shock]].

Simply applying the [[normal shock properties equations]] to $M_{n1}$ we can get $M_{n2}$, it can be further expanded by subbing in $M_{n1} = M_{1} \sin \beta$:
$$\begin{align*}
&&M^{2}_{n1} &= M^{2}_{1} \sin^{2} \beta\\
M_{n2}^{2}  &= \frac{(\gamma - 1) M_{n1}^{2} + 2}{2\gamma M_{n1}^{2} - (\gamma - 1)} & &\to & M_{n2}^{2}  &= \frac{(\gamma - 1) M^{2}_{1} \sin^{2} \beta + 2}{2\gamma M^{2}_{1} \sin^{2} \beta - (\gamma - 1)} 
\end{align*}$$


We want $M_{2}$ not $M_{n2}$, which we found in previous relations:

$$\begin{align*}
M_{n2} &= M_{2} \sin(\beta-\theta) & &\to & M^{2}_{2} &= \frac{M^{2}_{n2}}{\sin^{2}(\beta-\theta)}\\
&& M_{n2}^{2}  &= \frac{(\gamma - 1) M^{2}_{1} \sin^{2} \beta + 2}{2\gamma M^{2}_{1} \sin^{2} \beta - (\gamma - 1)} & &\to &  M^{2}_{2}  &= \frac{1}{\sin^{2}(\beta-\theta)}   \frac{(\gamma - 1) M^{2}_{1} \sin^{2} \beta + 2}{2\gamma M^{2}_{1} \sin^{2} \beta - (\gamma - 1)} 
\end{align*}$$
Congrats, we've finished the method for finding Mach number, but without knowing $\beta$, we can't go anywhere... So let's tackle that issue.


We know that mass is conserved over the shock, so taking normal flow:

$$\begin{align*}
\dot{m} &= \rho VA\\
\therefore \rho_{1} V_{n1} A &= \rho_{2} V_{n2} A & &\to & \frac{\rho_{1}}{\rho_{2}} &= \frac{V_{n2}}{V_{n1}}
\end{align*}$$

It's clear we can sub in $V_{n1} = V_{t1} \tan\beta$ and $V_{n2} = V_{t2} \tan(\beta-\theta)$ into this:

$$\begin{align*}
\frac{\rho_{1}}{\rho_{2}} &= \frac{V_{n2}}{V_{n1}} & &\to & \frac{\rho_{2}}{\rho_{1}} &= \frac{V_{n1}}{V_{n2}} & &\to & \frac{\rho_{2}}{\rho_{1}} &= \frac{V_{t1} \tan\beta}{V_{t2} \tan(\beta - \theta)} 
\end{align*}$$


We can also get $\frac{\rho_{1}}{\rho_{2}}$ from the density relations in the [[normal shock properties equations]], subbing in $M_{n1} = M_{1} \sin\beta$ like done previously:
$$\begin{align*}
&&M^{2}_{n1} &= M^{2}_{1} \sin^{2} \beta\\
\frac{\rho_{2}}{\rho_{1}} &= \frac{M_{n1}^{2} (\gamma + 1)}{(\gamma-1)M_{n1}^{2} + 2} & &\to & \frac{\rho_{2}}{\rho_{1}} &= \frac{M_{1}^{2}\sin^{2} \beta  (\gamma + 1)}{(\gamma-1)M_{1}^{2}\sin^{2} \beta + 2}
\end{align*}$$

Two different forms of the density ratio means we can equate them... which allows us to solve for $\theta$!

$$\begin{align*}
&& \text{painful}&\text{ rearangement}\\
\frac{M_{1}^{2}\sin^{2} \beta  (\gamma + 1)}{(\gamma-1)M_{1}^{2}\sin^{2} \beta + 2} &= \frac{V_{t1} \tan\beta}{V_{t2} \tan(\beta - \theta)} & &\to & \tan\theta&= 2 \frac{1}{\tan\beta} \left[\frac{M_{1}^{2} \sin^{2}\beta - 1 }{M_{1}^{2}(\gamma + \cos 2\beta)+2}\right]
\end{align*}$$

Easy. ([[as fucking if we both know you are not going to try|the rearrangement is left as an exercise for the reader]])

Now something to realise is that we generally know $\theta$, so this equation is the wrong way around! Good luck rearranging for $\beta$ lmao, this is where the normal shock tables and online calculators save us.