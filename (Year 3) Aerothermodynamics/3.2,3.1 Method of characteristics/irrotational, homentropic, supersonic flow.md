---
aliases: [""]
tags: []
---

## Irrotational, homentropic, supersonic flow

### Key flow characteristic



> ### $$\begin{align*}  0&=  \frac{\partial \theta}{\partial s} -  \tan \mu\frac{\partial\nu }{\partial n} \end{align*}$$
> ### $$\begin{align*}  0  &=   \frac{\partial\nu}{\partial s}-\tan  \mu  \frac{\partial \theta}{\partial n}  \end{align*}$$
> ### $$\begin{align*} 0&= \frac{\partial}{\partial s} \begin{pmatrix} \nu \\ \theta \end{pmatrix} + \begin{pmatrix} 0  & -\tan\mu \\ -\tan\mu   & 0\end{pmatrix} \frac{\partial}{\partial n} \begin{pmatrix} \nu \\ \theta \end{pmatrix} & \to && 0&= \frac{\partial\bf{Q}}{\partial s}   + \bf{A} \frac{\partial \bf{Q}}{\partial n}    \end{align*}$$
>> where:
>> $\theta=$ [[Prandtl–Meyer expansion fan|turning angle]]
>> $\nu=$ [[Prandtl–Meyer expansion fan|Prandtl-Meyer function]]
>> $\frac{\partial n}{\partial s}=$ streamline "expansion" with distance along streamline
>> $s=$ distance along streamline
>> $\mu=$ [[Mach cone|Mach angle]]
>> 
>> $\mathbf{Q}=$ represents the [[Prandtl–Meyer expansion fan|Prandtl-Meyer function]] and the [[Prandtl–Meyer expansion fan|turning angle]], so it is a representation of the angle of flow and the expansion wave angle. It characterises flow property change.
>> $\mathbf{A}=$ is a matrix representing the [[Mach cone|Mach angle]], which going back to the [[Mach cone#Supersonic]] can be seen to reflect how information propagates downstream, with the angle being a pure function of Mach number



### Deriving relations

A bunch of the setup of the environment is similar to what  we did in [[Aerodynamics overview|the Aerodynamics module]], here we'll start by taking a [[control volume]] between two [[streamlines]] in [[n-t diagram|n-t space]]:

![[Pasted image 20231103191829.png]]

Through simple geometry the following relationship can be seen:
$$\begin{align*}
\Delta s &= R \: \Delta \theta & &\to & \frac{1}{R} &= \frac{\Delta \theta}{\Delta s} 
\end{align*}$$

We want to derive an expression for the change in area between streamlines after a small change in $s$, aka $\Delta n' - \Delta n$. This relationship can be simply seen then expanded:
$$\begin{align*}

\Delta n' - \Delta n &= \Delta s \: \Delta \theta & &\to & \Delta n' - \Delta n &= \Delta s \: \left(\frac{\Delta \theta}{\Delta n} \Delta n\right) & &\to & \frac{1}{\Delta n} \left(\frac{\Delta n' - \Delta n}{\Delta s}  \right) &= \:  \frac{\Delta \theta}{\Delta n}   
\end{align*}$$

Consider that this is a small control region, and as it tends to be smaller the following simplifications can be done:

$$\begin{align*}&& \Delta s &\to 0\\
\frac{1}{\Delta n} \left(\frac{\Delta n' - \Delta n}{\Delta s}  \right) &= \:  \frac{\Delta \theta}{\Delta n}   & &\to & \frac{1}{\Delta n} \left(\frac{\partial \Delta n}{\partial s}  \right) &= \:  \frac{\partial \theta}{\partial n}  \\
\frac{1}{R} &= \frac{\Delta \theta}{\Delta s}  & &\to & \frac{1}{R} &= \frac{\partial \theta}{\partial s} 
\end{align*}$$

These will be useful later.

#### [[homentropic flow|Homentropic flow]]


![[Pasted image 20231103194300.png]]

Since we are dealing with a [[control volume]] we have the equation of momentum conservation, it can be put into our context (the momentum and pressure flux above):

$$\begin{align*} 
&& && && \dot{m}&= \rho u \Delta n \\
\vec{F}  &=  \sum\limits \vec{P}_{n} A_{n} + \sum\limits_{\text{in}} \vec{V}_{n} \dot{m}_{n}   - \sum\limits_{\text{out}} \vec{V}_{n} \dot{m}_{n}  & &\to & \dot{m} \left( u+\frac{\partial u}{\partial s}\right) - \dot{m} u &= - \left(\frac{\partial p }{\partial s}\Delta s\right) \Delta n  & &\to & \rho u \Delta n \: \left( u+\frac{\partial u}{\partial s}\right) -  \rho u \Delta n \: u &= - \left(\frac{\partial p }{\partial s}\Delta s\right) \Delta n  \end{align*}$$

Expanding this out and removing higher order terms, then rearranging yields:

$$\begin{align*}
\rho u \Delta n \: \left( u+\frac{\partial u}{\partial s}\right) -  \rho u \Delta n \: u &= - \left(\frac{\partial p }{\partial s}\Delta s\right) \Delta n  & &\to & \rho u \frac{\partial u}{\partial s} &= - \frac{\partial p}{\partial s} & &\to & \rho u \frac{\partial u}{\partial s} &= - \frac{\partial p}{\partial \rho} \frac{\partial \rho}{\partial s}
\end{align*}$$

If we assume it to be [[homentropic flow]] then we can rearrange:

$$\begin{align*} && \left.\frac{\partial p}{\partial \rho} \right|_{S=const} &= a^{2}\\
\rho u \frac{\partial u}{\partial s} &= - \left.\frac{\partial p}{\partial \rho} \right|_{S=const} \: \frac{\partial \rho}{\partial s} & &\to & \rho u \frac{\partial u}{\partial s} &= - a^{2} \frac{\partial \rho}{\partial s}
\end{align*}$$


#### Vorticity

We'll also get [[curl of a vector|vorticity]] into this [[n-t diagram|n-t coordinate system]] (this will be useful later), changing coordinate systems is a pain so:

$$\begin{align*}&& \text{m}&\text{agic}\\
\omega &= \frac{\partial v}{\partial x} - \frac{\partial u}{\partial y} & &\to & \omega &=u \frac{\partial \theta}{\partial s} - \frac{\partial u}{\partial n}
\end{align*}$$

#### Mass continuity

Ok so, since mass cannot cross between streamlines we can derive a simple expression for mass transfer in our [[control volume]]:

$$\begin{align*}
&& \text{}&\\ 
\dot{m}_{in} &= \dot{m}_{out} & &\to & \rho u \Delta n &= \left(\rho +\frac{\partial \rho}{\partial s} \Delta s\right) \left(u +\frac{\partial u}{\partial s} \Delta s\right) \left(\Delta n +\frac{\partial \Delta n}{\partial s} \Delta s\right)\\\\\
&& && &\downarrow \text{Expand and remove higher order terms}\\\\
&& &&  \rho u \Delta n&= \rho u \:\Delta n + \rho u \frac{\partial \Delta n}{\partial s} \Delta s + \rho \: \Delta n \frac{\partial u}{\partial s} \Delta s + u\: \Delta n \frac{\partial \rho}{\partial s} \Delta s &&\to& 0 &= \frac{1}{\Delta n} \frac{\partial \Delta n}{\partial s} + \frac{1}{u} \frac{\partial u}{\partial s} + \frac{1}{\rho} \frac{\partial \rho}{\partial s}
\end{align*}$$

Then using a previously derived equation can be put into it's final form:

$$\begin{align*}
& & \frac{1}{\Delta n} \left(\frac{\partial \Delta n}{\partial s}  \right) &= \:  \frac{\partial \theta}{\partial n} \\
0 &= \frac{1}{\Delta n} \frac{\partial \Delta n}{\partial s} + \frac{1}{u} \frac{\partial u}{\partial s} + \frac{1}{\rho} \frac{\partial \rho}{\partial s} & &\to & 0 &=  \frac{\partial \theta}{\partial n} + \frac{1}{u} \frac{\partial u}{\partial s} + \frac{1}{\rho} \frac{\partial \rho}{\partial s}
\end{align*}$$

#### Relating angle divergence $\nu$ and velocity $u$ 

Ok so recap on all the equations we've gathered now:

$$\begin{align*}
\text{Euler s-}&\text{equation} & \text{Homoen}&\text{tropic flow} & \text{}&\text{ Mass Continuity}  & \text{}&\text{Vorticity}   \\
\rho u \frac{\partial u}{\partial s} &= - \frac{\partial p}{\partial s} & \rho u \frac{\partial u}{\partial s} &= - a^{2} \frac{\partial \rho}{\partial s} & 0 &=  \frac{\partial \theta}{\partial n} + \frac{1}{u} \frac{\partial u}{\partial s} + \frac{1}{\rho} \frac{\partial \rho}{\partial s} & \omega &=u \frac{\partial \theta}{\partial s} - \frac{\partial u}{\partial n}
\end{align*}$$

These can be combined:

$$\begin{align*}
& &\text{re}&\text{arrange}\\
0 &=  \frac{\partial \theta}{\partial n} + \frac{1}{u} \frac{\partial u}{\partial s} + \frac{1}{\rho} \frac{\partial \rho}{\partial s} & &\to & -\rho\left(\frac{\partial \theta}{\partial n} + \frac{1}{u} \frac{\partial u}{\partial s}\right) &=     \frac{\partial \rho}{\partial s}\\ &&&&\text{sub}& \downarrow \\
  && \rho u \frac{\partial u}{\partial s} &= - a^{2} \frac{\partial \rho}{\partial s} & &\to &  \rho u \frac{\partial u}{\partial s} &=   a^{2}  \rho\left(\frac{\partial \theta}{\partial n} + \frac{1}{u} \frac{\partial u}{\partial s}\right)\\
  && && &&   u \frac{\partial u}{\partial s} &=   a^{2}  \left(\frac{\partial \theta}{\partial n} + \frac{1}{u} \frac{\partial u}{\partial s}\right)\\
  && && &&   \frac{u^{2}}{a^{2}} \frac{\partial u}{\partial s}- \frac{\partial u}{\partial s}  &=       u\frac{\partial \theta}{\partial n}\\
  && && &&   \left(\frac{u^{2}}{a^{2}}  - 1\right) \frac{1}{u}\frac{\partial u}{\partial s}  &=        \frac{\partial \theta}{\partial n}\\
\end{align*}$$

We've got the [[Mach number]] def in there now:
$$\begin{align*}
\left(\frac{u^{2}}{a^{2}}  - 1\right) \frac{1}{u}\frac{\partial u}{\partial s}  &=        \frac{\partial \theta}{\partial n} &&\to &\left(M^{2}  - 1\right) \frac{1}{u}\frac{\partial u}{\partial s}  &=        \frac{\partial \theta}{\partial n} 
\end{align*}$$

 


I need an equation relating angle change and velocity change.... oh [[Prandtl–Meyer expansion fan#^77e61b]], this can be used with the [[Mach cone|Mach angle]] equation to get something:

$$\begin{align*}
&& \tan \mu &= \frac{1}{\sqrt{M^{2} -1}}  \\
&& \theta_{pm} &= \nu\: (\neq v) \\
\frac{ d\theta_{pm}}{\sqrt{M^{2} - 1}} &=   \frac{du}{u} &&\to &  d\nu \tan \mu &=   \frac{du}{u}
\end{align*}$$

Now this can be used on the $d\theta/dn$ equation:

$$\begin{align*}
\tan \mu &= \frac{1}{\sqrt{M^{2} -1}}&&\to& \frac{1}{\tan^{2} \mu} &= M^{2} -1   \\
&& && \text{sub}&\downarrow&&& \partial\nu \tan \mu &=   \frac{\partial u}{u}\\
&&  \left(M^{2}  - 1\right) \frac{1}{u}\frac{\partial u}{\partial s} &=        \frac{\partial \theta}{\partial n}  & &\to &  \frac{1}{\tan^{2} \mu} \frac{\partial u}{u}\frac{1}{\partial s}   &=        \frac{\partial \theta}{\partial n}  &&\to& \frac{1}{\tan^{2} \mu} \partial\nu \tan \mu\frac{1}{\partial s}   &=        \frac{\partial \theta}{\partial n}\\
&&&&&&&&&&   \frac{1}{\tan  \mu} \frac{\partial\nu}{\partial s}   &=        \frac{\partial \theta}{\partial n}\\ 
\end{align*}$$

Finally we can now utilise the vortisity equation, lets assume [[irrotational and incompressible flow|irrotational flow]] and use the previous equation to get another equation with the same inputs:

$$\begin{align*}
&&&&&& \partial\nu \tan \mu &=   \frac{\partial u}{u}\\
0=\omega &=u \frac{\partial \theta}{\partial s} - \frac{\partial u}{\partial n} & &\to & 0&=  \frac{\partial \theta}{\partial s} - \frac{\partial u}{u}\frac{1}{\partial n} & &\to & 0&=  \frac{\partial \theta}{\partial s} -  \tan \mu\frac{\partial\nu }{\partial n}\\ \\
& & &  & \frac{1}{\tan  \mu} \frac{\partial\nu}{\partial s}   &=        \frac{\partial \theta}{\partial n} & &\to & 0   &=   \frac{\partial\nu}{\partial s}-\tan  \mu  \frac{\partial \theta}{\partial n} \\\\

\end{align*}$$

Boom we now a set of simultaneous equations which can be used to describe flow characteristics in a supersonic flow!

#### Meaning

To make math simpler, we convert em into matrix form:

$$\begin{align*}
0&= \frac{\partial}{\partial s} \begin{pmatrix} \nu \\ \theta \end{pmatrix} + \begin{pmatrix} 0  & -\tan\mu \\ -\tan\mu   & 0\end{pmatrix} \frac{\partial}{\partial n} \begin{pmatrix} \nu \\ \theta \end{pmatrix} & \to && 0&= \frac{\partial\bf{Q}}{\partial s}   + \bf{A} \frac{\partial \bf{Q}}{\partial n}  
\end{align*}$$



Now to evaluate the physical meaning behind this equation:
- $\bf{Q}$ represents the [[Prandtl–Meyer expansion fan|Prandtl-Meyer function]] and the [[Prandtl–Meyer expansion fan|turning angle]], so it is a representation of the angle of flow and the expansion wave angle
- $\bf{M}$ is a matrix representing the [[Mach cone|Mach angle]], which going back to the [[Mach cone#Supersonic]] can be seen to reflect how information propagates downstream, with the angle being a pure function of Mach number
- $\frac{\partial}{\partial s}$ is rate of change along the streamline (how something changes downstream)
- $\frac{\partial}{\partial n}$ is rate of change normal to the streamline (how something changes perpendicular)

Overall then, this equation relates how key angles in the flow change ($\bf{Q}$) in both the normal and tangential directions, with that relationship being characterised by [[Mach cone|Mach angle]] ($\bf{A}$). Which makes sense since mach angle is a characterisation of the ratio between information propagation in the tangential and normal directions. (Recall in simple supersonic flow, information can't back propagate)


