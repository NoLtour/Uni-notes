---
aliases: ["virtual origin"]
tags: []
---

## Transition
We know from [[approximating a laminar BL profile]] and [[approximating a turbulent BL profile]] methods for modelling flow:
![[Pasted image 20221101220722.png]]
But the transition between the two cannot be as easily modelled, generally this transition region takes place somewhere between 300k to 1M [[Reynolds number]]. The question is how can we calculate drag while accounting for this region? The answer is that it is much easier than you'd think.

![[Pasted image 20221101233321.png]]

We know that [[momentum thickness and viscous drag|momentum thickness is directly proportional to viscous drag]], of course if we can find the momentum thickness at the end of the turbulent boundary layer we can easily find drag. That is where $x_{0}$ comes in, as can be seen above this "[[calculating drag across a plate with a transition region|virtual origin]]" of the turbulent region marks where the turbulent boundary layer would start from if you trace it's shape forward; hence if you can find length $x_{0}\to c$ then a turbulent layer of that length has viscous drag equal to the current plate.
So if we can find $x_{0}$ we can find the [[boundary layer momentum thickness|momentum thickness]] and then drag. Since we know that at the transition location $x_{T}$ the laminar and turbulent momentum thicknesses are equal:
$$\begin{align*}
\frac{\theta_{lam}}{x} &= \frac{0.664}{\sqrt{Re_{x}}} & \frac{\theta_{turb}}{x} &= \frac{0.037}{({Re_{x}})^{\frac{1}{5}}}
\end{align*}$$
(equations from [[approximating a laminar BL profile|here]] and [[approximating a turbulent BL profile|here]])

We know that for $\theta_{lam}$ when $x=x_{T}$ it is equal to $\theta_{lam}$ at $x=x_{T}-x_{0}$ substituting in:


$$\begin{align*}
\frac{\theta_{lam}}{x_{T}} &= \frac{0.664}{\sqrt{Re_{x_{T}}}} &&& \frac{\theta_{turb}}{x_{T}-x_{0}} &= \frac{0.037}{({Re_{x_{T}-x_{0}}})^{\frac{1}{5}}}\\
 \theta_{lam}  &= \frac{0.664x_{T}}{\sqrt{ \frac{U_{\infty} x_{T}}{ \nu } } } && &  \theta_{turb} &= \frac{0.037(x_{T}-x_{0})}{\left(  \frac{U_{\infty} (x_{T}-x_{0})}{ \nu }  \right)^{\frac{1}{5}}}\\
 && \frac{0.664x_{T}}{\sqrt{ \frac{U_{\infty} x_{T}}{ \nu } } } &= \frac{0.037(x_{T}-x_{0})}{\left(  \frac{U_{\infty} (x_{T}-x_{0})}{ \nu }  \right)^{\frac{1}{5}}}
\end{align*}$$

Something that can be quickly found is that this equation is really hard to solve [[numerical and analytical solutions|analytically]], so instead we use computers and a root finding algorithm to figure it out. Alternatively under specific conditions the following approximation can be applied:

> ## $$ x_{0} \approx x_{T} \left(1-\frac{38}{Re_{x^{T}}^{\frac{3}{8}}}\right) $$ 
>> where:
>> $x_{0}=$ virtual origin of boundary layer
>> $Re_{x^{T}}=$ [[Reynolds number]] at $x_{T}$
>> $x_{T}=$ 