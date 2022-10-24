---
aliases: [""]
tags: []
---

## Electrically propelled systems

### Description

Electrical propulsion systems use electrical power to accelerate the propellant gas out of the rocket nozzle. Electrically propelled systems tend to have very high [[specific impulse]], even multiple times higher than traditional [[bi propellant systems]], the trade off is they require large amounts of power as well as are quite low thrust (thrust being mainly limited by electricity generation).
Something else worth noting is although for more traditional propellant systems the burn time is negligible compared to orbital period such that it can be approximated by an impulse, since electrically propelled systems might burn for weeks, months even years this assumption is often not applicable.

### Maths

When working with electrically propelled systems the importance of the effect of the power plant mass should be considered, a larger power plant of course generates more power allowing for a greater thrust but also increases the mass ([[phat generator|obviously]]).

Let's define a set of equations to describe the properties of the spacecraft and it's subsystems:
- Here $\beta$ is the specific power of the plant (Watts per kg) $\beta=W/M_W$, this measures the power to generator weight efficiency.
- The initial mass of the vehicle $M_{0}$ can be described interms of it's components $M_{p}=$ payload mass, $M_W=$ power plant mass, $M_{e}=$ propellant mass; hence $M_{0}=M_W+M_e+M_p$.
- The efficiency of the power generated to the KE given to propellant can be described as $W_{jet}=\eta W$ where $eta$ is the efficiency of energy conversion.
- The rate of mass burn (assuming constant) $\sigma=M_{e}/t_{b}$ where $t_{b}=$ time taken to burn fuel.

Now by combining these equations can get a definition of potential thrust:

$$\begin{align*}
W_{jet} &= \eta W & W &= \beta M_{W}\\
\sigma \frac{1}{2} V_{ex}^{2} &= \eta \beta M_{W}\\
 \frac{\sigma V_{ex}^{2} }{2 \eta} &= \beta M_{W} & \sigma&=\frac{M_{e}}{t_{b}}\\
\frac{ M_{e} V_{ex}^{2} }{2 \eta t_{b} \beta } &= M_{W}
\end{align*}$$

Subbing this into the equation of $M_{0}$ gives:
$$\begin{align*}
M_{0}&=M_{W}+M_{e}+M_{p} &  \frac{ M_{e} V_{ex}^{2} }{2 \eta t_{b} \beta } &= M_{W}\\
&= \frac{ M_{e} V_{ex}^{2} }{2 \eta t_{b} \beta }+M_{e}+M_{p} \\
M_{0} - M_{p} &= \left(\frac{  V_{ex}^{2} }{2 \eta t_{b} \beta }+1\right) M_{e} \\
\frac{M_{0} - M_{p}}{\left(\frac{  V_{ex}^{2} }{2 \eta t_{b} \beta }+1\right)} &=  M_{e} 
\end{align*}$$
Subbing into [[the basic rocket equation|the rocket equation]] gives:
$$\begin{align*}
\Delta V &= V_{ex} \ln\left( \frac{M_{0}}{M_{e}} \right) & M_{e} &= \frac{M_{0} - M_{p}}{\left(\frac{  V_{ex}^{2} }{2 \eta t_{b} \beta }+1\right)} \\
\Delta V &= V_{ex} \ln\left( \frac{M_{0}}{\frac{M_{0} - M_{p}}{\left(\frac{  V_{ex}^{2} }{2 \eta t_{b} \beta }+1\right)}} \right)   \\
\Delta V &= V_{ex} \ln\left( \frac{ \frac{  V_{ex}^{2} }{2 \eta t_{b} \beta }+1 }{1  - \frac{M_{p}}{M_{0}} } \right)   \\
&
\end{align*}$$
This form's not very useful to read so we'll introduce this variable "characteristic velocity" $V_{c}=\sqrt{2\eta \beta t_{b}}$:
$$\begin{align*}
\Delta V &= V_{ex} \ln\left( \frac{ \frac{ M_{e} V_{ex}^{2} }{2 \eta t_{b} \beta }+M_{e}+M_{p} }{ M_{e} } \right) & M_{0}&=\frac{ M_{e} V_{ex}^{2} }{2 \eta t_{b} \beta }+M_{e}+M_{p}\\
  &= V_{ex} \ln\left( \frac{ \frac{ M_{e} V_{ex}^{2} }{V_{c}^{2} }+M_{e}+M_{p} }{ M_{e} } \right)\\
  &= V_{ex} \ln\left( \frac{  V_{ex}^{2} }{V_{c}^{2} }+1+ \frac{M_{p}}{M_{e}}   \right)\\
\end{align*}$$