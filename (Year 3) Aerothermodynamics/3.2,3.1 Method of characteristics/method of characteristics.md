---
aliases:
  - Riemann invariants
  - Riemann invariant
tags:
---

## Method of characteristics


### Useful bits

For some [[irrotational, homentropic, supersonic flow]] we can calculate the properties downstream through the method of characteristics:
1) Get the [[method of characteristics|Riemann invariants]]
2) Find where 2 [[Mach lines and domains of influence|characteristic lines]] intercept, then solve to get that points $\nu$ and $\theta$
3) Use the calculated $\nu$ to determine Mach number and any other gas properties
4) Find the new $\mu$ (Mach number changed, use [[Mach cone|Mach triangle]])
5) Use geometric properties to determine location of point

All the equations needed for this method are listed below, read the [[method of characteristics#Proof]] to understand.

> [[method of characteristics|Riemann invariants]]:
> ### $$\begin{align*}  \text{Along line C}^{+}:\:\: \text{ R}^{+} &= \nu-\theta =\text{constant}&&&\text{Along line C}^{-}:\:\: \text{ R}^{-} &= \nu+\theta =\text{constant}   \end{align*}$$
>  
> Turning angle and [[Prandtl–Meyer expansion fan|Prandtl-Meyer function]]:
> ### $$\begin{align*}  \nu(M_{P}) &=  \frac{\text{R}^{-}_{B}+\text{R}^{+}_{A}}{2} &&&\theta_{P} &=\frac{\text{R}^{-}_{B}-\text{R}^{+}_{A}}{2}   \end{align*}$$
> 
> Geometric properties:
> ### $$\begin{align*} \alpha_{AP} &= \frac{(\theta+\mu)_{A} + (\theta+\mu)_{P}}{2}  & \alpha_{BP} &= \frac{(\theta-\mu)_{B} + (\theta-\mu)_{P}}{2}\end{align*}$$
> ### $$\begin{align*}  x_{p} &= \frac{x_{B }\tan\alpha_{BP} - x_{A} \tan\alpha_{AP} + y_{A} - y_{B}}{\tan\alpha_{BP} - \tan \alpha_{AP}} & y_{P} &= y_{A} + (x_{P} - x_{A})\tan\alpha_{AP}   \end{align*}$$
> 
>> where:
>> $\theta=$ [[Prandtl–Meyer expansion fan|turning angle]]
>> $\nu=$ [[Prandtl–Meyer expansion fan|Prandtl-Meyer function]]
>> $R^{+}=$ [[method of characteristics|Riemann invariant]] for the characteristic line $C^{+}$
>> $R^{-}=$ [[method of characteristics|Riemann invariant]] for the characteristic line $C^{-}$
>> $\alpha=$ absolute angle of [[Mach lines and domains of influence|characteristic lines]] in cartesian space
>> $x,y=$ [[Cartesian coordinates|cartesian coordinates]]
>> ![[Pasted image 20231104182425.png]]
>> ![[Pasted image 20231104185001.png]]
>> 

^d18a14

### Proof

I'm going to skip over the first step since it involves the introduction of some random matrix stuff, [[characteristics proofs matrix thing|slide showing this step is here]]. The tldr is through fancy manipulation we can re-write the equation from [[Mach lines and domains of influence#Summery]] into a very useful form:

$$\begin{align*}
&&0&= \frac{\partial\bf{Q}}{\partial s}   + \bf{A} \frac{\partial \bf{Q}}{\partial n}\\\\
&&& \downarrow \text{lotsa mathz}\\\\
\frac{\partial (\nu - \theta)}{\partial s} + \tan\mu \frac{\partial (\nu - \theta)}{\partial n} &= 0 &&& \frac{\partial (\nu + \theta)}{\partial s} - \tan\mu \frac{\partial (\nu + \theta)}{\partial n} &= 0
\end{align*}$$

 The reason for this usefulness comes from Riemann invariants.


#### Reimann invariants

![[Pasted image 20231104180451.png]]

This is going to lead somewhere so trust me... let's take some arbitrary property $f$, then regardless of what it is it will have some $df/ds$ and $df/dn$, expressing it's change as a first order [[Taylor series]] linear approximation:

$$\begin{align*}
&& && && \tan x&= \frac{\Delta n}{\Delta s}\\
\Delta f &= \frac{\partial f}{\partial s}\Delta s + \frac{\partial f}{\partial n}\Delta n & &\to & \frac{\Delta f}{\Delta s} &= \frac{\partial f}{\partial s}  + \frac{\partial f}{\partial n} \frac{\Delta n}{\Delta s} & &\to & \frac{\Delta f}{\Delta s} &= \frac{\partial f}{\partial s}  +\tan x \frac{\partial f}{\partial n} \\\\\\
&& && && && &\text{Compare that with:}\\
&& && && && 0&= \frac{\partial (\nu - \theta)}{\partial s} + \tan\mu \frac{\partial (\nu - \theta)}{\partial n}\\
&& && && && 0&= \frac{\partial (\nu + \theta)}{\partial s} - \tan\mu \frac{\partial (\nu + \theta)}{\partial n}\\
\end{align*}$$

What the first equation is stating, is simply the gradient of $f$ change as we follow $x$ is "something"... then we can see that our $\nu,\theta$ equations actually have the same format, but they essentially say that the $\frac{\Delta (\nu - \theta)}{\Delta s}$ is zero so long as we follow $\nu$! The change is zero, hence $\nu-\theta$ and $\nu+\theta$ are constant along their respective [[Mach lines and domains of influence|characteristic lines]]!


> ### $$\begin{align*}  \text{Along line C}^{+}:\:\: \text{ R}^{+} &= \nu-\theta =\text{constant}\\\\\text{Along line C}^{-}:\:\: \text{ R}^{-} &= \nu+\theta =\text{constant}   \end{align*}$$
>> where:
>> $\theta=$ [[Prandtl–Meyer expansion fan|turning angle]]
>> $\nu=$ [[Prandtl–Meyer expansion fan|Prandtl-Meyer function 
>> $R^{+}=$ [[method of characteristics|Riemann invariant]] for the characteristic line $C^{+}$
>> $R^{-}=$ [[method of characteristics|Riemann invariant]] for the characteristic line $C^{-}$

^bb94d9

##### Using Reimann invariants to find properties

Now take the following situation, we know the properties of 2 points $A$ and $B$:

![[Pasted image 20231104182425.png]]

We know $R^{+}_{A}$ and $R^{-}_{B}$, then along these lines we have an equation for $\nu$ and $\theta$, unfortunately that is 1 known and 2 unknowns ($\text{ R}^{+} = \nu-\theta$). If only there was some point where these 2 lines met, which would allow us to solve their equations simultaneously!

Oh wait there is, it's point P:

$$\begin{align*}
\text{ R}^{+}_{A} &= \nu(M_{A})-\theta_{A} &&& \text{ R}^{+}_{B} &= \nu(M_{B})-\theta_{B} \\
   && &\downarrow \text{At P}\\
\text{ R}^{+}_{A} &= \nu(M_{P})-\theta_{P} &&& \text{ R}^{+}_{B} &= \nu(M_{P})-\theta_{P} \\
   && &\downarrow \text{Solve}\\
 \nu(M_{P}) &=  \frac{\text{R}^{-}_{B}+\text{R}^{+}_{A}}{2} &&&\theta_{P} &=\frac{\text{R}^{-}_{B}-\text{R}^{+}_{A}}{2} \\
\end{align*}$$

Since $\nu$ can be used to get Mach number, we can then also get all other properties since this is in [[homentropic flow]] (so long as there is a fully defined point).

##### Finding the interception

Though this doesn't give us an idea of where in space the interception occurs, luckily we know $\theta$ and $\mu$ for A and B, hence it becomes a basic geometry problem:

![[Pasted image 20231104185001.png]]

I said that... but reconsider the fact that the [[Mach lines and domains of influence|characteristic lines]] have angle $\mu$ which is a direct function of $M$. In a real flow the Mach number is going to change continuously, which means that these lines that we draw as straight actually curve. So instead of taking $\alpha$ at $A$ or $B$ a more accurate $\alpha$ that represents the average value between $A\to P$ and $B\to P$ respectively will be the average:

$$\begin{align*}
\alpha_{AP} &= \frac{(\theta+\mu)_{A} + (\theta+\mu)_{P}}{2}  & \alpha_{BP} &= \frac{(\theta-\mu)_{B} + (\theta-\mu)_{P}}{2}
\end{align*}$$

The next stage is just using the $\alpha$ and known $A$ and $B$ positions to get functions of those lines (approximating them as straight) and finding where they intercept by solving simultaneously. The math's not too hard so I'll skip to the result:

$$\begin{align*}
x_{p} &= \frac{x_{B }\tan\alpha_{BP} - x_{A} \tan\alpha_{AP} + y_{A} - y_{B}}{\tan\alpha_{BP} - \tan \alpha_{AP}} & y_{P} &= y_{A} + (x_{P} - x_{A})\tan\alpha_{AP}
\end{align*}$$

And that's it, we can now find the downstream position and properties of some point in a flow given 2 upstream points. 

Something to keep in mind is that at various point's we've approximated the [[Mach lines and domains of influence|characteristic lines]] as straight, which is not the case. In effect this solving method is a [[numerical and analytical solutions|numerical solution]], as such it's accuracy improves the smaller the distance is between points, so if we want a good approximation we'll need lots of points!

