---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Pressure loss in a laminar flow pipe
### Equation

> ### $$  \Delta p = \frac{32\mu LU}{D^{2}} $$ 
>> where:
>> $\Delta p=$ pressure loss
>> $\mu=$ [[viscosity]] 
>> $L=$ length of pipe
>> $D=$ diameter of pipe
>> $U=$ flow velocity
 
### Derivation
Basically take the [[pressure loss darcy weisbach equation]] and sub in the equation for [[darcy-weisbach friction factor]] with [[Reynolds number]] equation.

$$\begin{align*}
\Delta p &= f_{D} \frac{L}{D} \frac{\rho U^{2}}{2} & f_{D} &= \frac{64}{Re} & Re &= \frac{\rho U D}{\mu} \\
&&  f_{D} &= \frac{64\mu}{\rho U D}\\
&= \frac{64\mu}{\rho U D} \frac{L}{D} \frac{\rho U^{2}}{2}\\
&= \frac{32\mu LU}{D^{2}}
\end{align*}$$
