---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Griffith approach
### Theory
This is the work of a mad lad from [[world war one]], basically he took a thermodynamic approach to why the fracture stress of a material and theoretical stress for breaking atomic bonds varied so much.

It works along the lines of:
- Cracks in materials exist due to imperfections during material creation, these cracks reduce the materials strength.
- Cracks have a surface energy ($U_S$), which is the total amount of energy that can be stored within a given crack. ($U_S$ resists crack growth)
- Cracks have a stored strain energy ($U_E$), which is the total energy of the stress acting through it. ($U_E$ drives crack growth)

Cracks behaviour under expansion:
- When the strain energy is large enough it causes the crack to grow
- Crack growth increases surface energy, allowing it to handle greater strain energys
- Rate of surface energy increase is linear but strain energy is exponenetial
- So at some point crack length increases strain energy more than surface energy
- This leads to rapid crack growth at this point, which leads to fracture

![[Pasted image 20211125132835.png]]

### Math time

![[calculating surface energy in a crack]]

![[calculating stored strain energy in a crack]]

Although surface energy starts with a faster growth rate than strain energy at some point there rates of change will be equal:

$$\begin{align*}
  && U_S &= 4a\gamma & U_E &= \frac{(\sigma_0)^{2} \pi a^2 }{E}\\
 \frac{dU_S}{da} &= \frac{dU_E}{da} & \frac{dU_S}{da} &= 4\gamma & \frac{dU_E}{da} &= \frac{(\sigma_f)^{2} \pi 2a }{E}\\
4\gamma &= \frac{(\sigma_f)^{2} \pi 2a }{E}\\
\sqrt\frac{E4\gamma}{\pi 2a} &= \sigma_f\\
\sqrt\frac{2E\gamma}{\pi a} &= \sigma_f
\end{align*}$$

![[Griffith approach for critical stress]]