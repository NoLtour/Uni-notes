---
aliases: [""]
tags: []
---

## Thermodynamics radiation absorption example

![[Pasted image 20231211224833.png]]

Using [[total radiation absorption transmittance and reflectance|absorptance]] and cross section of the sphere, we can assume the spacecraft to be in thermal equilibrium, noting that for aluminium $\varepsilon=0.04$:

$$\begin{align*}
&&\dot{Q}_{in} &= \alpha \dot{q}_{sun} A_{cross}=\alpha \dot{q}_{sun} \pi r^{2}\\
&&\dot{Q}_{out} &= \varepsilon \sigma T^{4} A_{total} =\varepsilon \sigma T^{4} \pi 4r^{2}  \\
\dot{Q}_{in} &= \dot{Q}_{out} &&\to& \alpha \dot{q}_{sun} \pi r^{2}&= \varepsilon \sigma T^{4} \pi 4r^{2}  
 &&\to&  \left(\frac{ \alpha\dot{q}_{sun}}{4 \varepsilon  \sigma}\right)^{\frac{1}{4}} &=   T=459.7K
\end{align*}$$

[[Stefan-Boltzmann constant]] is used.
