---
aliases: [""]
tags: []
---

## Ackeret theory

### Equation

> ### $$\begin{align*} C_{p} &=   \frac{2\theta}{\sqrt{ M^{2}_{\infty} - 1}}  \end{align*}$$
>> where:
>> $\theta=$ streamline angle
>> $M_{\infty}=$ freestream Mach number
>> $C_{p}=$ [[linearized compressible flow|linearized pressure coefficient]]
>> ![[Pasted image 20231123233716.png]]

So this equation is to be used when trying to find pressure in a supersonic flow, note it should be used in range $1.2<M<5$. Obviously it relies on all assumptions in [[linearized compressible flow]].

### Proof

#### Characteristic lines

Why do we need this anyway? Let's just use the [[Prandtl-Glauert transformation]]!

$$\begin{align*}
\beta &= \sqrt{1 - M^{2}_{\infty}} & &\to & \beta &= \sqrt{1 - (M^{2}_{\infty}>1)} & &\to & \beta &= \sqrt{-1 (\:...)}
\end{align*}$$

Oh.... that's why.

K let's attempt to apply some new thing, assume that the velocity potential is a function of only $\eta$, which is constant along straight lines:

$$\begin{align*}
 & & \lambda &= \sqrt{ M^{2}_{\infty} - 1} \\
 & & \phi &= \phi(\eta) &&& \frac{\partial \eta }{\partial y}&=  -\lambda  \\
 & & \eta &= x - \lambda y &&& \frac{\partial \eta }{\partial x}&=  1 \\ 

u' &=  \frac{\partial \phi}{\partial x} & &\to & u' &= \frac{\partial \phi}{\partial \eta} \frac{\partial \eta}{\partial x} & &\to & u' &= \frac{\partial \phi}{\partial \eta}  &&\searrow&

\\ 

v' &=  \frac{\partial \phi}{\partial y} & &\to & v' &= \frac{\partial \phi}{\partial \eta} \frac{\partial \eta}{\partial y} & &\to & v' &= -\frac{\partial \phi}{\partial \eta}\lambda  
& &\to& u' &= - \frac{v'}{\lambda}\\\\\\

& & & & \frac{\partial^{2} \phi}{\partial x^{2} } &=  \frac{\partial }{\partial \eta} \left(\frac{\partial \phi}{\partial \eta} \frac{\partial \eta}{\partial x}\right) & 
&\to & \frac{\partial^{2} \phi}{\partial x^{2} } &=    \frac{\partial^{2} \phi}{\partial \eta^{2}}   &&\searrow&

\\ 


& & & & \frac{\partial^{2} \phi}{\partial y^{2} } &=   \frac{\partial }{\partial \eta}  \left(\frac{\partial \phi}{\partial \eta} \frac{\partial \eta}{\partial y}\right) & 
&\to & \frac{\partial^{2} \phi}{\partial y^{2} } &=   \lambda^{2}   \frac{\partial^{2} \phi}{\partial \eta^{2}}   &&\to& \lambda^{2} \frac{\partial^{2} \phi}{\partial x^{2} } &= \frac{\partial^{2} \phi}{\partial y^{2} }

\end{align*}$$

This result is consistent with [[linearized compressible flow|linearized velocity potential equation]]:

$$\begin{align*}
 0  &=   (1-M_{\infty}^{2})  \frac{\partial^{2} \phi}{\partial x^{2}} + \frac{\partial^{2} \phi}{\partial y^{2}}
\end{align*}$$

What this result means is that $\phi$ is constant along particular lines (characteristic lines) of the gradient $\frac{1}{\lambda}$:

$$\begin{align*}
y &= \frac{x}{\lambda} + c & &\to & \frac{dy}{dx} &= \frac{1}{\sqrt{ M^{2}_{\infty} - 1}} 
\end{align*}$$

Note that this equation matches the one for [[Mach cone|Mach angle]]:

$$\begin{align*}
 \tan \mu  &=  \frac{1}{\sqrt{M^{2} -1 }} = \frac{dy}{dx}
\end{align*}$$

Which is saying that a wave of form $f(\eta)$ has consistent solutions along that.

#### Surface boundary condition

![[Pasted image 20231123230910.png]]

Take a streamline with a shallow angle $\theta$. We can use it's $y$ velocity to find [[linearized compressible flow|linearized pressure coefficient]]:

$$\begin{align*}
&& u' &= - \frac{v'}{\lambda}& && \tan \theta= \frac{v'}{U_{\infty}} &\approx\theta && & \lambda &= \sqrt{ M^{2}_{\infty} - 1}\\
 C_{p} &= -2 \frac{u'}{U_{\infty}} & &\to &  C_{p} &=   \frac{2}{\lambda} \frac{v'}{U_{\infty}}   & &\to &  C_{p} &=   \frac{2}{\lambda}\theta  & &\to &  C_{p} &=   \frac{2\theta}{\sqrt{ M^{2}_{\infty} - 1}}
\end{align*}$$

I have no clue why this works ngl, since It's derived from something thats constant along those mach lines?? And streamlines arn't???

### Example

![[Pasted image 20231123232312.png]]

![[Pasted image 20231123232411.png]]
