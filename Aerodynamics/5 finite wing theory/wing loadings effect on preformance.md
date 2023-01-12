---
aliases: [""]
tags: []
---

## Wing loadings effect on preformance

If we take the equation for induced drag in steady level flight then sub in the equations for [[wing aspect ratio|aspect ratio]] and lift coefficient:
$$\begin{align*}
D_{i} &= \frac{1}{2} \rho V_{\infty}^{2} S C_{Di} & C_{Di} &= \frac{C_{L}^{2}}{\pi e A} & C_{L} &= \frac{W}{\frac{1}{2}\rho V_{\infty}^{2} S} & S &=  \frac{b^{2}}{A}
\end{align*}$$

$$\begin{align*}
D_{i} &= \frac{1}{2} \rho V_{\infty}^{2} S C_{Di}\\
&= \frac{1}{2} \rho V_{\infty}^{2} \frac{b^{2}}{A} \frac{\left( \frac{W}{\frac{1}{2}\rho V_{\infty}^{2} \frac{b^{2}}{A}} \right)^{2}}{\pi e A}\\
&...\\
D_{i} &= \frac{2}{\pi e \rho V_{\infty}^{2}} \left( \frac{W}{b} \right)^{2}
\end{align*}$$

In this equation $\frac{W}{b}$ is [[wing loading]], which suggests that by reducing wing loading we can reduce induced drag. This can be seen when super high efficiency vehicles distrobute the mass of the vehicle across the wing instead of having most of it in a single fusalage:

![[Pasted image 20221222145525.png]]
