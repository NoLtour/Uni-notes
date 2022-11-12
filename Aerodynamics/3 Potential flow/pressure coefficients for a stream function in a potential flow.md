---
aliases: [""]
tags: []
---

## Pressure coefficients for a stream function in a potential flow

### Theory

It's quite easy just take the equation for [[pressure coefficient when there is no freestream|pressure coefficient]] and then use the same sort of method we did for finding [[defining the geometry of an object in a flow#Finding thickness|thickness of a object in freestream]] from it's streamfunction, but for the pressure coefficient:

![[pressure coefficient when there is no freestream#^6ace8a]]

### Example

> [[Flow past a circular cylinder]], find the pressure coefficients at the maximum and minimum points of velocity on the surface of cylinder with radius $R=\sqrt{\frac{k}{2\pi U_{\infty}}}$, then find the coefficients of pressure at these points and where $C_{p}=0$

$$ \psi(r,\theta) = U_{\infty}r\sin(\theta)\left(1- \frac{R^{2}}{r^{2}}\right) $$
$$\begin{align*}
V_{r}&=  \frac{1}{r} \frac{\delta\psi}{\delta\theta} & V_{\theta} &= -\frac{\delta\psi}{\delta r} \\
&\text{online calculator...}\\
&= \frac{1}{r} U_{\infty}\cos\theta \left(1- \frac{R^{2}}{r^{2}}\right) & &= -U_{\infty} \sin\theta \left(1 + \frac{R^{2}}{r^{2}}\right)
\end{align*}$$
Then letting $r=R$:
$$\begin{align*}
V_{r} &= 0& V_{\theta} &= -2U_{\infty} \sin\theta
\end{align*}$$
We can tell just by looking that a stagnation point will exist at $\theta=0,\pi,2\pi,3\pi...$ which for us is just $\theta=0,\pi$ and that the maximum vel will occur at $\theta= \frac{\pi}{2},-\frac{\pi}{2}$ such that $|V|=2U_{\infty}$ which looks like:
![[Pasted image 20221112123716.png]]
This result also lines up with the computational analysis in [[determining stagnation point computationally]] (since [[Flow past a circular cylinder]] was used there as the example too) stagnation points are marked red:
![[Pasted image 20221112124242.png]]
Next to find pressure coefficient:
$$ C_{p} = 1-\frac{  V_{\theta}^{2} + V_{r}^{2}  }{ V^{2}_{ref} }  $$ $$\begin{align*}
 C_{p} &=  1-\frac{  V_{\theta}^{2} + V_{r}^{2}  }{ V^{2}_{ref} }  & V_{r}&= \frac{1}{r} U_{\infty}\cos\theta \left(1- \frac{R^{2}}{r^{2}}\right) & V_{\theta} &= -U_{\infty} \sin\theta \left(1 + \frac{R^{2}}{r^{2}}\right)\\
 &=  1-\frac{  V_{\theta}^{2} + V_{r}^{2}  }{ V^{2}_{ref} }
\end{align*}$$
