---
aliases: [""]
tags: []
---

## Pitot tube in supersonic flow

We've done the [[pitot-static tube|pitot tube]] problem with non-compressible flows previously, but how is it done with a supersonic flow?

### Compressible flow

If we assume [[isentropic process|isentropic]] behaviour, we can use the [[supersonic flow properties equations]] for pressure:

$$\begin{align*}
\frac{p_{0}}{p} &= \left(1 + \frac{\gamma-1}{2} Ma^{2}\right)^{\frac{\gamma}{\gamma-1}}& &\to &

 \sqrt{\frac{2}{\gamma-1} \left(\frac{p_{0}}{p}^{\frac{\gamma-1}{\gamma}}- 1\right)}   &=  \text{Ma}
\end{align*}$$

Then subbing in the definition of [[Mach number]] and [[speed of sound]]:

$$\begin{align*}

&& a &= \sqrt{\gamma R T} \\
a\sqrt{\frac{2}{\gamma-1} \left(\frac{p_{0}}{p}^{\frac{\gamma-1}{\gamma}}- 1\right)}   &= a  \text{Ma} = V & &\to & \sqrt{\frac{2\gamma R T}{\gamma-1} \left(\frac{p_{0}}{p}^{\frac{\gamma-1}{\gamma}}- 1\right)}   &=  V
\end{align*}$$

Here a value of $T$ would likely be gathered from a sensor or estimated using [[International Standard Atmosphere|ISA tables]].

### Supersonic flows


