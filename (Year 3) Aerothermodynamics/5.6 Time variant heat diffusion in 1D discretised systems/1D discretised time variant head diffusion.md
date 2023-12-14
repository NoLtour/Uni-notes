---
aliases:
  - Fourier number
tags:
---

## 1D discretised time variant head diffusion

Well we've new got to discretise in 2 axis: the time and space dimensions. Visualised we can imagine that our 1D system is represented in 2D:

![[Pasted image 20231213153246.png]]

With one axis being time and the other being space. We get the 1D [[general heat transfer equation]], note that $g=0$ (excluding the borders):

$$\begin{align*}
&&&&&&\text{Discr}&\text{etised}\\
\frac{1}{\alpha} \frac{\partial T}{\partial t}&=   \nabla^{2} T + \frac{g}{k} &&\to& 
\frac{1}{\alpha} \frac{\partial T}{\partial t}&=   \frac{\partial^{2} T}{\partial x^{2}} &&\to& 
\frac{1}{\alpha} \frac{T_{n+1,i} - T_{n,i}}{\Delta t}&=   \frac{T_{n,i+1}-2T_{n,i}+T_{n,i-1}}{(\Delta x)^{2}}
\end{align*}$$

Then we use an identity the [[1D discretised time variant head diffusion|Fourier number]]:

$$\begin{align*}
F &= \frac{\Delta t}{\Delta x^{2}}\alpha\\
\frac{1}{\alpha} \frac{T_{n+1,i} - T_{n,i}}{\Delta t}&=   \frac{T_{n,i+1}-2T_{n,i}+T_{n,i-1}}{(\Delta x)^{2}} &&\to
& T_{n+1,i} - T_{n,i}&=  F (T_{n,i+1}-2T_{n,i}+T_{n,i-1} )
\end{align*}$$

The boundary conditions are taken as constant temperature where $T_{n,0}=T_{l}$ and $T_{n,L}=T_{r}$

