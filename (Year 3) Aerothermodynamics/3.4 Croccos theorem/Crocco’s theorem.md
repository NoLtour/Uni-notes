---
aliases:
  - Euler n-equation
tags:
---

## Crocco’s theorem

> ### $$\begin{align*} T \frac{dS}{dn} &= \frac{dh_{0}}{dn} +u \omega  \end{align*}$$
>> where:
>> $S=$ [[specific properties (thermodynamics)|specific]] entropy
>> $h_{0}=$ [[specific properties (thermodynamics)|specific]] [[stagnation points in a compressible flow|stagnation enthalpy]]
>> $n=$ position normal to the streamline
>> $u=$ velocity along streamline
>> $\omega=$ [[curl of a vector|vorticity]]

What this equation means is that If stagnation enthalpy is constant everywhere and the flow is irrotational and steady, then the entropy is constant everywhere ([[homentropic flow]]).

### Derivation
#### Euler n-equation

In the previous section we derived the [[irrotational, homentropic, supersonic flow#homentropic flow Homentropic flow|Euler p-equation]]. The method for deriving the Euler n-equation is pretty similar.


![[Pasted image 20231112163540.png]]

Momentum flux is simply:

$$\begin{align*}
\text{n-momentum}_{out} - \text{n-momentum}_{in} &= \text{net applied force} \\
\dot{m} \left[ u \frac{\partial \theta}{\partial s} \Delta s \right] - 0 &=- \frac{\partial p}{\partial n} \Delta n \: \Delta s  
\end{align*}$$

Fun things can then be done by rearranging and subbing in the mass equation as well as the R relation [[irrotational, homentropic, supersonic flow#Deriving relations]]:

$$\begin{align*}
&& \dot{m } &= \rho u \Delta n &&&&&&& \frac{1}{R} &= \frac{\partial\theta}{\partial s}\\
\dot{m} \left[ u \frac{\partial \theta}{\partial s} \Delta s \right] - 0 &= -\frac{\partial p}{\partial n} \Delta n \: \Delta s & &\to & \rho u \Delta n \left[ u \frac{\partial \theta}{\partial s} \Delta s \right]  &= -\frac{\partial p}{\partial n} \Delta n \: \Delta s  & &\to & \rho   u^{2} \frac{\partial \theta}{\partial s}   &= -\frac{\partial p}{\partial n}   & &\to &    \frac{\rho u^{2}}{R}  &= -\frac{\partial p}{\partial n}  
\end{align*}$$

#### Crocco’s theorem

This relationship essentially states that a normal pressure gradient will cause the streamline to curve, which makes sense.
 
Taking [[Gibbs' equation]] and [[stagnation points in a compressible flow|stagnation enthalpy]] (note that $S$ is [[specific properties (thermodynamics)|specific]] entropy):

$$\begin{align*}
h_{0} - \frac{1}{2}u^{2}&= h  &&\to& d h_{0} - u\:du &= dh &&&&&&&\rho   u^{2} \frac{\partial \theta}{\partial s}   &= -\frac{\partial p}{\partial n}   \\
&& TdS &= dh - \frac{dp}{\rho} & &\to & TdS &= dh_{0} - u\: du - \frac{dp}{\rho} & &\to & T \frac{dS}{dn} &= \frac{dh_{0}}{dn} - \left(u\: \frac{du}{dn} + \frac{dp}{dn} \frac{1}{\rho} \right) & &\to & T \frac{dS}{dn} &= \frac{dh_{0}}{dn} - \left(u\: \frac{du}{dn} - u^{2} \frac{\partial \theta}{\partial s} \right)
\end{align*}$$

Recalling the equation for vorticity from [[irrotational, homentropic, supersonic flow#Vorticity]]:

$$\begin{align*}
&& \omega &=u \frac{d \theta}{d s} - \frac{d u}{d n}\\
T \frac{dS}{dn} &= \frac{dh_{0}}{dn} - \left(u\: \frac{du}{dn} - u^{2} \frac{d \theta}{d s} \right) &&\to& T \frac{dS}{dn} &= \frac{dh_{0}}{dn} - \left(u\: \frac{du}{dn} - u \omega  - u \frac{du}{dn} \right)&&\to& T \frac{dS}{dn} &= \frac{dh_{0}}{dn} +u \omega    \\ 
\end{align*}$$

This is [[Crocco’s theorem]], it describes entropy change normal to a streamline. 

