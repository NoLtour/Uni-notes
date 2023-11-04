---
aliases: [""]
tags: []
---

## KEYWORDS environment characteristics

A bunch of the setup of the environment is simular to what  we did in [[Aerodynamics overview|the Aerodynamics module]], here we'll start by taking a [[control volume]] between two [[streamlines]] in [[n-t diagram|n-t space]]:

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

####


![[Pasted image 20231103194300.png]]

Since we are dealing with a [[control volume]] we have the equation of momentum conservation, it can be put into our context (the momentum and pressure flux above):

$$\begin{align*} 
&& && && \dot{m}&= \rho u \Delta n \\
\vec{F}  &=  \sum\limits \vec{P}_{n} A_{n} + \sum\limits_{\text{in}} \vec{V}_{n} \dot{m}_{n}   - \sum\limits_{\text{out}} \vec{V}_{n} \dot{m}_{n}  & &\to & \dot{m} \left( u+\frac{\partial u}{\partial s}\right) - \dot{m} u &= - \left(\frac{\partial p }{\partial s}\Delta s\right) \Delta n  & &\to & \rho u \Delta n \: \left( u+\frac{\partial u}{\partial s}\right) -  \rho u \Delta n \: u &= - \left(\frac{\partial p }{\partial s}\Delta s\right) \Delta n  \end{align*}$$

Expanding this out and removing higher order terms, then rearranging yields:

$$\begin{align*}
\rho u \Delta n \: \left( u+\frac{\partial u}{\partial s}\right) -  \rho u \Delta n \: u &= - \left(\frac{\partial p }{\partial s}\Delta s\right) \Delta n  & &\to & \rho u \frac{\partial u}{\partial s} &= - \frac{\partial p}{\partial s}
\end{align*}$$


