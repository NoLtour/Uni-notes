---
aliases: ["MIE"]
tags: []
---

## Momentum integral equation for a flat plate

![[Pasted image 20221029202811.png]]

From [[viscous drag coefficient]]:
$$\begin{align*}
C_{F} = \frac{\left. D' \right|_{x=L}}{\frac{1}{2}\rho  U_{\infty}^{2} L} &= \frac{ 2}{L}(\left. \theta \right|_{x=L}  )\\
\left. D' \right|_{x=L} &=\rho  U_{\infty}^{2} (\left. \theta \right|_{x=L}  )\\
D'(x) &=\rho  U_{\infty}^{2}  \theta(x)  \\
\end{align*}$$
Combining this with the equation defining [[local wall shear stress]]:
$$\begin{align*}
\tau_{w} &= \frac{dD'}{dx} & D' &=\rho  U_{\infty}^{2}  \theta\\
 &= \rho  U_{\infty}^{2} \frac{d\theta}{dx}\\
\frac{\tau_{w}}{\rho  U_{\infty}^{2} } &= \frac{d\theta}{dx}\\
\end{align*}$$