---
aliases:
  - linearized energy equation
  - linearized velocity potential equation
  - linearized pressure coefficient
tags:
---

## Linearized compressible flow
 

> ### $$\begin{align*}   \\a_{\infty}^{2} &= a^{2} + ( \gamma-1)    u' U_{\infty}  \end{align*}$$
> ### $$\begin{align*}   0  &=   (1-M_{\infty}^{2})  \frac{\partial^{2} \phi}{\partial x^{2}} + \frac{\partial^{2} \phi}{\partial y^{2}}  \end{align*}$$
> ### $$\begin{align*}  C_{p} &= -2 \frac{u'}{U_{\infty}}   \end{align*}$$
>> where:
>> $X_{\infty}=$ free stream property
>> $X=$ point property
>> $a=$ [[speed of sound]]
>> $M=$ [[Mach number]]
>> $u'=\frac{\partial\phi}{\partial x}=$ velocity perturbation in $x$
>> $U_{\infty}=$ free stream velocity
>> $\gamma=$ [[specific heat ratio]]
>> $\phi=$ [[velocity potential]]
>> $C_{p}=$ linearized [[pressure coefficient]]
>
>> assumptions:
>> - Perfect gas
>> - Irrotational
>> - Inviscid
>> - Steady
>> - 2D
>> - Small velocity perturbation $u',v'<<U_{\infty}$ such that high order terms are negligible

Some key observations are:
- The velocity potential reduces to previously derived [[laplace equation for flow|Laplace equation]] if flow is incompressible ($M_{\infty} \to 0$)
- Equation will clearly have strange results near Mach 1 (invalid $0.8<M<1.2$)
- Not applicable for extreme Mach's $M_{\infty}>5$ (hypersonic flow)

### Proof

#### Energy equation

Then the [[supersonic flow properties equations|energy equation]] can be linearized, first we get it into a more useful form:

$$\begin{align*}
 && a &= \sqrt {TR\gamma }&&& a^{2} M^{2} &= u^{2} + v^{2} \\
T_{0} &= T \left(1 + \frac{\gamma-1}{2} M^{2} \right) & &\to & a_{0}^{2} &= a^{2} \left(1 + \frac{\gamma-1}{2} M^{2} \right)& &\to & a_{0}^{2} &= a^{2} +  \frac{\gamma-1}{2} (u^{2} + v^{2}) 
\end{align*}$$

Now to linearize, we state the following:

$$\begin{align*}
u &= U_{\infty} + u', &&\text{where: }u', v' <<U_{\infty}\\
v &= 0 + v'
\end{align*}$$

Subbing into the energy equation:

$$\begin{align*}
& & &\text {sub} &&&&&&&\text{small }&\text{terms}  \\
a_{0}^{2} &= a^{2} +  \frac{\gamma-1}{2} (u^{2} + v^{2})  &  &\to & a_{0}^{2} &= a^{2} +  \frac{\gamma-1}{2} ((U_{\infty} + u')^{2} + v'^{2}) &  &\to & a_{0}^{2} &= a^{2} +  \frac{\gamma-1}{2} (U_{\infty}^{2} + 2u' U_{\infty} + u'^{2} + v'^{2}) & &\to & a_{0}^{2} &= a^{2} +  \frac{\gamma-1}{2} (U_{\infty} + 2u' U_{\infty})
\end{align*}$$

Then equating it to the free stream equation we can get something useful:

$$\begin{align*}
a_{\infty}^{2} +  \frac{\gamma-1}{2} (U_{\infty}  ) &= a^{2} +  \frac{\gamma-1}{2} (U_{\infty} + 2u' U_{\infty}) & &\to & a_{\infty}^{2} &= a^{2} + ( \gamma-1)    u' U_{\infty} 
\end{align*}$$

This is the linearized energy equation.

#### Velocity potential equation

Going to skip unneeded working, a critical first simplification is taking the steady flow Euler equations and assume that the flow is [[irrotational and incompressible flow|irrotational]]:

$$\begin{align*}
&& \nabla\times(\nabla \phi) &= 0 \\
\frac{\partial}{\partial x}  \begin{pmatrix} \rho u  \\ \rho u^{2} + p \\ \rho u v \\ \rho u H \end{pmatrix} + \frac{\partial}{\partial y}  \begin{pmatrix} \rho v  \\ \rho u v \\ \rho v^{2} + p \\ \rho v H \end{pmatrix} &= 0 & &\to & ... & &\to && u^{2} \frac{\partial u}{\partial x} + uv \frac{\partial u}{\partial y} + uv \frac{\partial v}{\partial x} + v^{2} \frac{\partial v}{\partial y} &= a^{2} \left( \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} \right)
\end{align*}$$

This equation can be rewritten interms of small perturbations using the previous:

$$\begin{align*}
u &= U_{\infty} + u', &&\text{where: }u', v' <<U_{\infty}\\
v &= 0 + v'
\end{align*}$$

So subbing in these, plus the previously derived linear energy equation:

$$\begin{align*}
&&&&&&\text{small terms}&\text{, simplify}\\
u^{2} \frac{\partial u}{\partial x} + uv \frac{\partial u}{\partial y} + uv \frac{\partial v}{\partial x} + v^{2} \frac{\partial v}{\partial y} &= a^{2} \left( \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} \right) & & \to & (U_{\infty} + u')^{2} \frac{\partial u'}{\partial x} + (U_{\infty} + u')v' \frac{\partial u'}{\partial y} + (U_{\infty} + u')v' \frac{\partial v'}{\partial x} + v'^{2} \frac{\partial v'}{\partial y} &= (a_{\infty}^{2}- ( \gamma-1)    u' U_{\infty} ) \left( \frac{\partial u'}{\partial x} + \frac{\partial v'}{\partial y} \right) & & \to & 
 U_{\infty}   ^{2} \frac{\partial u'}{\partial x}   &= a^{2}_{\infty} \left( \frac{\partial u'}{\partial x} + \frac{\partial v'}{\partial y} \right)
\end{align*}$$

Something to note is that $U_{\infty}$ is a constant, hence why $\frac{\partial U_{\infty}}{\partial x,\:y}=0$.  

Now using definitions of velocity potential:
$$\begin{align*}
&& u' &= \frac{\partial\phi}{\partial x}\\
&& v' &= \frac{\partial\phi}{\partial y}\\
U_{\infty}   ^{2} \frac{\partial u'}{\partial x}   &= a^{2}_{\infty} \left( \frac{\partial u'}{\partial x} + \frac{\partial v'}{\partial y} \right) & &\to & M_{\infty}   ^{2} \frac{\partial^{2} \phi}{\partial x^{2}}   &=   \left( \frac{\partial^{2} \phi}{\partial x^{2}} + \frac{\partial^{2} \phi}{\partial y^{2}} \right)
 & &\to &    0  &=   (1-M_{\infty}^{2})  \frac{\partial^{2} \phi}{\partial x^{2}} + \frac{\partial^{2} \phi}{\partial y^{2}} 
\end{align*}$$

This is the linearized velocity potential equation.

#### Pressure coefficient

From the [[isentropic flow equations]]

$$\begin{align*}
 && a &= \sqrt {TR\gamma }&&& a_{\infty}^{2} &= a^{2} + ( \gamma-1)    u' U_{\infty}\\
\frac{p}{p_{\infty}} &= \left(\frac{T}{T_{\infty}}\right)^{\frac{\gamma}{\gamma-1}}  & &\to & \frac{p}{p_{\infty}} &= \left(\frac{a^{2}}{a^{2}_{\infty}}\right)^{\frac{\gamma}{\gamma-1}}  & &\to & \frac{p}{p_{\infty}} &= \left(\frac{a^{2} - ( \gamma-1)    u' U_{\infty} }{ a^{2}   }\right)^{\frac{\gamma}{\gamma-1}}  & &\to & 
\frac{p}{p_{\infty}} &=  \left( 1 -( \gamma-1) M^{2}_{\infty} \frac{      u' }{ U_{\infty} }\right)^{\frac{\gamma}{\gamma-1}} 
\end{align*}$$

Expanding this using [[Taylor series]] produces:

$$\begin{align*}
&& &\text{Taylor}&& &\text{high}&\text{ order terms} \\
\frac{p}{p_{\infty}} &=  \left( 1 -( \gamma-1) M^{2}_{\infty} \frac{      u' }{ U_{\infty} }\right)^{\frac{\gamma}{\gamma-1}} & &\to & \frac{p}{p_{\infty}} &= 1 - \gamma M^{2}_{\infty} \frac{u'}{U_{\infty}} + \:...  & &\to & \frac{p}{p_{\infty}} &= 1 - \gamma M^{2}_{\infty} \frac{u'}{U_{\infty}}  
\end{align*}$$

This is quite simple now, just sub into the [[pressure coefficient]] equation:

$$\begin{align*} 
&&\frac{p}{p_{\infty}}&=  1 - \gamma M^{2}_{\infty} \frac{u'}{U_{\infty}}\\
C_{p} &= \frac{2}{\gamma M^{2}_{\infty}} \left(\frac{p}{p_{\infty}} - 1\right) & &\to & C_{p} &= -2 \frac{u'}{U_{\infty}}  
\end{align*}$$

This is the linearized pressure coefficient equation!
