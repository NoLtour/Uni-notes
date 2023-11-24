---
aliases: [""]
tags: []
---

## Prandtl-Glauert transformation

### Equations

> ### $$\begin{align*} 0  &= \frac{\partial^{2} \phi_{0} }{\partial x_{0}^{2}}  + \frac{\partial^{2} \phi_{0} }{\partial y_{0}^{2}}  \end{align*}$$
> ### $$\begin{align*}   C_{p0} &= -2 \frac{u_{0}'}{U_{\infty}}   \end{align*}$$
> ### $$\begin{align*}  & & \beta &= \sqrt{1 - M^{2}_{\infty}} & \phi_{0} &= \beta \phi & x_{0} &= x & y_{0} &= \beta y &  C_{p} &=  \frac{C_{p0}}{\sqrt{1-M_{\infty}^{2}}}   \end{align*}$$



>> where:
>> $\beta=$ a constant for applying the transform 
>> $\phi_{0}=$ transformed [[velocity potential]]
>> $C_{p0}=$ transformed [[linearized compressible flow|linearized pressure coefficient]]
>
>Note assumptions from [[linearized compressible flow]] apply

Allows __incompressible results to be used in the compressible flow regime__. These results can then be transformed back into real space, with emphasis on important properties such as [[pressure coefficient]]. 

This then means that key features such as lift and drag can be determined.

Something to note is that this transform is made to work in the __subsonic regime__ where $~M_{\infty}<0.8$!

### Proof

#### Velocity potential transform

Starting with the [[linearized compressible flow|linearized velocity potential equation]], we can perform a transform using a substitution of the following definition:

$$\begin{align*}
 & & \beta &= \sqrt{1 - M^{2}_{\infty}} \\
 & & \phi_{0} &= \beta \phi \\
 & & x_{0} &= x \\
 & & y_{0} &= \beta y \\
0  &=   (1-M_{\infty}^{2})  \frac{\partial^{2} \phi}{\partial x^{2}} + \frac{\partial^{2} \phi}{\partial y^{2}} & &\to & 0  &=   (1-1+\beta^{2})  \frac{\partial^{2} \left(\frac{\phi_{0}}{\beta}\right) }{\partial x_{0}^{2}} + \frac{\partial^{2} \left(\frac{\phi_{0}}{\beta}\right)}{\partial \left(\frac{y_{0}}{\beta}\right)^{2}}
& &\to & 0  &=    \beta^{2}   \frac{\partial^{2} \phi_{0} }{\partial x_{0}^{2}} \frac{1}{\beta^{2}}+ \frac{\partial^{2} \phi_{0} }{\partial y_{0}^{2}} \frac{\beta^{2}}{\beta^{2}}
& &\to & 0  &= \frac{\partial^{2} \phi_{0} }{\partial x_{0}^{2}}  + \frac{\partial^{2} \phi_{0} }{\partial y_{0}^{2}} 
\end{align*}$$

This is basically [[laplace equation for flow|Laplace equation]], which means it's not a massive pain in the ass to work with.

#### Pressure coefficient transform

Starting with the [[linearized compressible flow|linearized pressure coefficient]], we can perform a transform using a substitution of the following definition:

$$\begin{align*}
 & & \beta &= \sqrt{1 - M^{2}_{\infty}} \\
 & & \phi_{0} &= \beta \phi \\
 & & x_{0} &= x \\
 & & y_{0} &= \beta y \\
 && u' &= \frac{\partial\phi}{\partial x}= \frac{1}{\beta} \frac{\partial\phi_{0}}{\partial x} &&& C_{p0} &= -2 \frac{u_{0}'}{U_{\infty}}  \\
 C_{p} &= -2 \frac{u'}{U_{\infty}} & &\to & 
  C_{p} &= -  \frac{2}{U_{\infty}\beta} \frac{\partial\phi_{0}}{\partial x} & &\to & 
  C_{p} &=  \frac{C_{p0}}{\beta}   & &\to & 
  C_{p} &=  \frac{C_{p0}}{\sqrt{1-M_{\infty}^{2}}}  
\end{align*}$$

This allows us to get the actual pressure coefficient from working with transformed velocity potentials.
