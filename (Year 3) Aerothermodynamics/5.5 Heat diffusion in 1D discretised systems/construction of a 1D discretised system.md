---
aliases: [""]
tags: []
---

## Construction of a 1D discretised system

### Problem setup

This implementation is just an introduction into the steps involved, it's not useful.

First we get the 1D [[general heat transfer equation]]:

$$\begin{align*}
\frac{1}{\alpha} \frac{\partial T}{\partial t}&=   \nabla^{2} T + \frac{g}{k} &&\to& 
\frac{1}{\alpha} \frac{\partial T}{\partial t}&=   \frac{\partial^{2} T}{\partial x^{2}} + \frac{g}{k} 
\end{align*}$$

Here we will be constructing a steady state system, our assumed conditions are:

- Constant temperature: $\frac{d}{dt} T(0,t)=0$
- No internal heating: $g=0$
- In a steady state 1D system, heat flux is equal everywhere: $-k \frac{\partial T}{\partial x} = \dot{q}_{x} =\text{constant}$
- At the boundaries there is [[forced convection]]: $-k \left.\frac{\partial T}{\partial x}\right|_{x=0,L} = \text{convection}$

### Discretisation

The system is discrete, so it can be thought of as a 1D line of 1D cells like so:

![[Pasted image 20231213115839.png]]

When discretising the temp gradient we take it as the midpoint between two cells $i+ \frac{1}{2}k$ so:

$$\begin{align*}
\left.\frac{\partial T}{\partial x}\right|_{x= i- \frac{1}{2}} &\approx \frac{T_{i}-T_{i-1}}{\Delta x} &&&
\left.\frac{\partial T}{\partial x}\right|_{x= i+ \frac{1}{2}} &\approx \frac{T_{i+1}-T_{i}}{\Delta x} 
\end{align*}$$

In this case, since the gradient is constant everywhere this isn't even an approximation it's exact. Which will be reflected in the solution.

This can be further broken down to get the double derivative:

$$\begin{align*}
\left.\frac{\partial^{2} T}{\partial x^{2}}\right|_{x= i} &\approx \frac{\left.\frac{\partial T}{\partial x}\right|_{x= i+ \frac{1}{2}} - \left.\frac{\partial T}{\partial x}\right|_{x= i- \frac{1}{2}}}{\Delta x} &&\to&
\left.\frac{\partial^{2} T}{\partial x^{2}}\right|_{x= i} &\approx \frac{   \frac{T_{i+1}-T_{i}}{\Delta x} - \frac{T_{i}-T_{i-1}}{\Delta x}  }{\Delta x} &&\to&
\left.\frac{\partial^{2} T}{\partial x^{2}}\right|_{x= i} &\approx \frac{   T_{i+1} + T_{i-1} -2T_{i}     }{(\Delta x)^{2}} 
\end{align*}$$

### Boundary conditions

The left and right wall temps are $T_{l}$ and $T_{r}$, taking the double derivative equation a equation for the wall's relation to nearby cells can be easily defined:

$$\begin{align*}
0=\left.\frac{\partial^{2} T}{\partial x^{2}}\right|_{x= i} &= \frac{   T_{i+1} + T_{i-1} -2T_{i}     }{(\Delta x)^{2}} &&\to& 
\begin{aligned} 
0 &= \frac{   T_{2} + T_{l} -2T_{1}     }{(\Delta x)^{2}}  &&\to& -T_{0} &=   T_{2} - 2T_{1}  \\
0 &= \frac{   T_{L-2} + T_{r} -2T_{L-1}     }{(\Delta x)^{2}}  &&\to& -T_{L} &=   T_{L-2} - 2T_{L-1}   \\
0&= \frac{   T_{i+1} + T_{i-1} -2T_{i}     }{(\Delta x)^{2}} &&\to& 0 &=  T_{i-1}-2T_{i} + T_{i+1}  
\end{aligned}

\end{align*}$$

Then for heat transfer at the wall, boundaries smush our normal equation so instead of working in half steps we work in quarter steps, then sub in the surface [[thermal boundary layer|convection]]:

$$\begin{align*}
0=\left.\frac{\partial^{2} T}{\partial x^{2}}\right|_{x=i} &\approx \frac{\left.\frac{\partial T}{\partial x}\right|_{x= i+ \frac{1}{4}} - \left.\frac{\partial T}{\partial x}\right|_{x= i- \frac{1}{4}}}{0.5\Delta x} &&\to&
0&=  \frac{\left.\frac{\partial T}{\partial x}\right|_{x= \frac{1}{2}} - \left.\frac{\partial T}{\partial x}\right|_{x= 0}}{0.5\Delta x} &&\to&
0&=  \frac{ \frac{T_{1}-T_{0}}{\Delta x} - \left( -\frac{h}{k} [T_{\infty,l} - T_{0}] \right) }{0.5\Delta x} &&\to& 
T_{1} - \left(1 + \frac{h\Delta x}{k}\right) T_{0} &=   \frac{h\Delta x}{k} T_{\infty,l}
\end{align*}$$

A similar thing can be done to get the other side:

$$\begin{align*}
T_{L-1} - \left(1 + \frac{h\Delta x}{k}\right) T_{L} &= - \frac{h\Delta x}{k} T_{\infty,r}
\end{align*}$$

### Matrix construction

Making use of all of these equations, it becomes possible to construct a matrix:

$$\begin{align*}
 \begin{pmatrix} 
-\left(1 + \frac{h\Delta x}{k}\right) & 1 & 0 & ... & 0 & 0 & 0 \\ 
1 & -2 & 1 & ... & 0 & 0 & 0 \\
0 & 1 & -2 & ... & 0 & 0 & 0 \\
 ... & ... & ... & ... & ... & ... & ... \\
0 & 0 & 0 & ... & 1 & -2 & 1 \\
0 & 0 & 0 & ... &-2 & 1  & 0\\
0 & 0 & 0 & ... & 0 & 1 &  -\left(1 + \frac{h\Delta x}{k}\right) \\
 \end{pmatrix}  
 
 \begin{pmatrix}  T_{0} \\ T_{1} \\ T_{2} \\ ... \\ T_{L-2} \\ T_{L-1} \\ T_{L} \end{pmatrix} &=  
 \begin{pmatrix}   \frac{h\Delta x}{k} T_{\infty,l} \\ 0 \\ 0 \\ ... \\ 0 \\ 0 \\  \frac{h\Delta x}{k} T_{\infty,r}  \end{pmatrix}
\end{align*}$$

This can then be solved! Though doing so in this case would just result in a straight line between $T_{0}$ and $T_{1}$.
