---
aliases: [""]
tags: []
---

## Rotating [[perifocal coordinate frame]] to reference frame

It was described in [[orbital elements and alignment]] how to do this, but it can be expressed as a vector:

> ### $$\begin{align*} Q_{p \to r}=Q_{\text{perifocal} \to \text{reference}} &=  \begin{pmatrix} \cos(\Omega)\cos(\omega)- \cos(i)\sin(\Omega)\sin(\omega) & -\cos(\Omega)\cos(\omega)- \cos(i)\cos(\omega)\sin(\Omega)& \sin(\Omega)\sin(i)\\\cos(\omega)\sin(\Omega)+ \cos(\Omega)\cos(i)\sin(\omega) & \cos(\Omega)\cos(i)\cos(\omega)- \sin(\Omega)\sin(\omega)& -\cos(\Omega)\sin(i)\\\sin(i)\sin(\omega)& \cos(\omega)\sin(i)& \cos i \end{pmatrix}  \end{align*}$$
> ### $$\begin{align*} Q_{\text{perifocal} \to \text{reference}}^{T} &= Q_{\text{reference} \to \text{perifocal}}\\\begin{pmatrix} \cos(\Omega)\cos(\omega)- \cos(i)\sin(\Omega)\sin(\omega) & \cos(\omega)\sin(\Omega)+ \cos(\Omega)\cos(i)\sin(\omega) &\sin(i)\sin(\omega)\\ -\cos(\Omega)\cos(\omega)- \cos(i)\cos(\omega)\sin(\Omega) & \cos(\Omega)\cos(i)\cos(\omega)- \sin(\Omega)\sin(\omega)& \cos(\omega)\sin(i)\\  \sin(\Omega)\sin(i)& -\cos(\Omega)\sin(i)  & \cos i \end{pmatrix}  &= Q_{r\to p} \end{align*}$$

> ### $$\begin{align*}  Q_{p \to r}\begin{pmatrix}  r \cos\theta \\  r\sin\theta \\ 0\end{pmatrix}  &=  \vec{r}_{ref\:frame}(r,\theta) \end{align*}$$
> ### $$\begin{align*} \frac{\mu}{h} Q_{p \to r}\begin{pmatrix}  - \sin\theta \\  e+\cos\theta \\ 0\end{pmatrix}  &=  \vec{v}_{ref\:frame}(r,\theta) \end{align*}$$
>> where:
>> $\omega=$ [[orbital elements and alignment|argument of periapsis]]
>> $\Omega=$ [[orbital elements and alignment|longitude of the ascending node]]
>> $i=$ [[orbital elements and alignment|inclination]]
>> $r=$ radial separation
>> $\theta=$ [[orbital elements and alignment|true anomaly]]
>> Noting use of [[transposed matrix|transpose]]

Using these equations, we can describe the motion of the satellite in 3D!


