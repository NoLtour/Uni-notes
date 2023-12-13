---
aliases: ["heat transfer equation"]
tags: []
---

## General heat transfer equation

### Equation

The following is the general case, can be converted to 1D, 2D and 3D depending on the expansion of [[the Laplacian]] (or 4D if you [[we do not do theoretical shit here|are insane]]). 

> ### $$\begin{align*} \frac{1}{\alpha} \frac{\partial T}{\partial t}&=   \nabla^{2} T + \frac{g}{k}  \end{align*}$$
> ### $$ \frac{k}{\rho c_{p}} = \alpha $$
>> where:
>> $k=$ [[material thermal conductivity]]
>> $g=$ source strength (heat input/output per unit length^dimensions)
>> $T=$ temp
>> $\nabla^{2}=$ [[the Laplacian]]
>> $\rho=$ material density
>> $c_{p}=$ [[constant pressure specific heat]]
 

### Proof
![[Pasted image 20231213110259.png]]

The per cell heat equation is quite easy to derive, it has 3 components:
$$\begin{align*}
\text{Heat x flux:}& &&& \text{Heat y flux:}& &&& \text{Heat gen:}&  \\
\dot{q}_{x\:flux} &= \delta y \times (\dot{q}_{x} - \dot{q}_{x+\delta x})  
&&&  \dot{q}_{y\:flux} &= \delta x \times (\dot{q}_{y} - \dot{q}_{y+\delta y})  
&&&  \dot{q}_{gen} &= g \delta x  \:\delta y
\end{align*}$$

The total per cell would just be these summed:
$$\begin{align*}
\dot{q}_{total} &=  \delta y (\dot{q}_{x} - \dot{q}_{x+\delta x}) + \delta x  (\dot{q}_{y} - \dot{q}_{y+\delta y})  +g \delta x  \:\delta y
\end{align*}$$

Another way to describe $\dot{q}_{total}$ is as the temp change per second of that area of mass:
$$\begin{align*}
\dot{q}_{total}  &= \rho c_{p} \frac{\partial T}{\partial t} \delta x\:\delta y &&\to& \rho c_{p} \frac{\partial T}{\partial t} \delta x\:\delta y&=  \delta y (\dot{q}_{x} - \dot{q}_{x+\delta x}) + \delta x  (\dot{q}_{y} - \dot{q}_{y+\delta y})  +g \delta x  \:\delta y
 &&\to& \rho c_{p} \frac{\partial T}{\partial t}&=   \frac{\dot{q}_{x} - \dot{q}_{x+\delta x}}{\delta x} +\frac{\dot{q}_{y} - \dot{q}_{y+\delta y}}{\delta y}  +g
  &&\to& \rho c_{p} \frac{\partial T}{\partial t}&=  - \frac{\delta\dot{q}_{x} }{\delta x} -\frac{\delta \dot{q}_{y} }{\delta y}  +g \\
\end{align*}$$

Then making use of [[fundamental heat conduction (thermodynamics)|Fourier's law]] (general into 2D case):

$$\begin{align*}
 \dot{\vec{q}}  &= -k \nabla T & &\to &  
 \begin{pmatrix} \dot{q}_{x}\\\dot{q}_{y} \end{pmatrix} &= -k \begin{pmatrix} \frac{\partial T}{\partial x}\\\frac{\partial T}{\partial y} \end{pmatrix}& &\to &  
\begin{aligned}  \dot{q}_{x} &= -k  \frac{\partial T}{\partial x}\\ 
\dot{q}_{y} &= -k \frac{\partial T}{\partial y} \end{aligned}
\end{align*}$$

Using these:
$$\begin{align*}
\rho c_{p} \frac{\partial T}{\partial t}&=   -\frac{\partial\dot{q}_{x} }{\partial x} -\frac{\partial \dot{q}_{y} }{\partial y}  +g 
&&\to & \rho c_{p} \frac{\partial T}{\partial t}&=   k\left(\frac{\partial^{2} T }{\partial x^{2}} +\frac{\partial^{2} T }{\partial y^{2}}\right)  +g
&&\to &  \frac{1}{\alpha} \frac{\partial T}{\partial t}&=   \nabla^{2} T + \frac{g}{k}\\

\end{align*}$$

Note the use of [[the Laplacian]].

