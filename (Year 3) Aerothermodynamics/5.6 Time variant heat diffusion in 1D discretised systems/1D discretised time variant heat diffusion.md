---
aliases:
  - Fourier number
tags:
---

## 1D discretised time variant heat diffusion

Well we've new got to discretise in 2 axis: the time and space dimensions. Visualised we can imagine that our 1D system is represented in 2D:

![[Pasted image 20231214110819.png]]

With one axis being time and the other being space. We get the 1D [[general heat transfer equation]], note that $g=0$ (excluding the borders):

$$\begin{align*}
&&&&&&\text{Discr}&\text{etised}\\
\frac{1}{\alpha} \frac{\partial T}{\partial t}&=   \nabla^{2} T + \frac{g}{k} &&\to& 
\frac{1}{\alpha} \frac{\partial T}{\partial t}&=   \frac{\partial^{2} T}{\partial x^{2}} &&\to& 
\frac{1}{\alpha} \frac{T_{n+1,i} - T_{n,i}}{\Delta t}&=   \frac{T_{n,i+1}-2T_{n,i}+T_{n,i-1}}{(\Delta x)^{2}}
\end{align*}$$

Then we use an identity the [[1D discretised time variant heat diffusion|Fourier number]]:

$$\begin{align*}
F &= \frac{\Delta t}{\Delta x^{2}}\alpha\\
\frac{1}{\alpha} \frac{T_{n+1,i} - T_{n,i}}{\Delta t}&=   \frac{T_{n,i+1}-2T_{n,i}+T_{n,i-1}}{(\Delta x)^{2}} &&\to
& T_{n+1,i} - T_{n,i}&=  F (T_{n,i+1}-2T_{n,i}+T_{n,i-1} ) &&\to
& T_{n+1,i} &=  F (T_{n,i+1}+T_{n,i-1} ) + T_{n,i}(1-2F)
\end{align*}$$

The boundary conditions will assume [[forced convection]], so we can sub that into the discretised [[general heat transfer equation|heat transfer equation]]:

$$\begin{align*}
\frac{1}{\alpha} \frac{\partial T}{\partial t}=\left.\frac{\partial^{2} T}{\partial x^{2}}\right|_{x=i} &\approx \frac{\left.\frac{\partial T}{\partial x}\right|_{x= i+ \frac{1}{4}} - \left.\frac{\partial T}{\partial x}\right|_{x= i- \frac{1}{4}}}{0.5\Delta x} &&\to&
\frac{1}{\alpha} \frac{\partial T}{\partial t}&=  \frac{\left.\frac{\partial T}{\partial x}\right|_{x= \frac{1}{2}} - \left.\frac{\partial T}{\partial x}\right|_{x= 0}}{0.5\Delta x} &&\to&
\frac{1}{\alpha} \frac{T_{n+1,0} - T_{n,0} }{\Delta t} &=  \frac{ \frac{T_{n,1}-T_{n,0}}{\Delta x} - \left( -\frac{h}{k} [T_{\infty l} - T_{n,0}] \right) }{0.5\Delta x} 
\end{align*}$$

This can then be simplified:

$$\begin{align*}
\frac{1}{\alpha} \frac{T_{n+1,0} - T_{n,0} }{\Delta t} &=  \frac{ \frac{T_{n,1}-T_{n,0}}{\Delta x} - \left( -\frac{h}{k} [T_{\infty l} - T_{n,0}] \right) }{0.5\Delta x} &&\to&

 T_{n+1,0} - T_{n,0}  &= \alpha \frac{\Delta t}{\Delta x^{2}} \frac{  T_{n,1}-T_{n,0}  - \Delta x\left( -\frac{h}{k} [T_{\infty l} - T_{n,0}] \right) }{0.5 }   &&\to&

T_{n+1,0}  &= T_{n,0}+2F \left[  T_{n,1}-T_{n,0} + \left( \frac{h\:\Delta x}{k} [T_{\infty l} - T_{n,0}] \right)   \right] 
\end{align*}$$

Which can be even further rearranged into:

$$\begin{align*}
T_{n+1,0}  &= T_{n,0}+2F \left[  T_{n,1}-T_{n,0} + \left( \frac{h\:\Delta x}{k} [T_{\infty l} - T_{n,0}] \right)   \right] &&\to& 

T_{n+1,0}  &= T_{n,0}\left[1-2F\left(1+ \frac{h\:\Delta x}{k}\right)\right] +2F \left[  T_{n,1} +   \frac{h\:\Delta x}{k} T_{\infty l}      \right] 
\end{align*}$$

The other boundary condition will be similar:

$$\begin{align*}
T_{n+1,L}  &= T_{n,L}\left[1-2F\left(1+ \frac{h\:\Delta x}{k}\right)\right] +2F \left[  T_{n,L-1} +   \frac{h\:\Delta x}{k} T_{\infty r}      \right] 
\end{align*}$$

This can then be used to construct the matrix, for incrementing one timestep and then solved.

![[Pasted image 20231214120516.png]]
