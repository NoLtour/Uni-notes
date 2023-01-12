---
aliases: ["active thermal control","passive thermal control"]
tags: []
---

## Active and passive thermal control

### Intro

There are 2 types of thermal control:
- Passive thermal control, no mechanical/electrical devices needed to change the temperature, material choice regulates the temperature
- Active thermal control, not passive (some mechanical/electrical stuff is [[I hope when you read this it is a abnoctously loud autistic sound mentally|ACTIVELY]] doing something).

Thing is passive control is hella based, since:
- Simple without moving parts, more reliable.
- Cheaper.
- No power requirements.
- Generally lighter.

Problem is passive has issues in variable thermal requirement conditions and also has limitations under extreme design requirements (environmental/payload). So generally what happens especially for large vehicles is we make as much use of passive thermal regulation as possible such that minimal active thermal control is needed.

### Achieving passive thermal control

If we look back at the [[spacecraft heat balance#^7c6936|equation from heat balance]]:

$$\begin{align*} \sigma T^{4} &= q_{S} \frac{\alpha_{S}}{\varepsilon} \left( \frac{A_{S}^{proj}}{A_{surf}} + a \frac{A^{proj}_{E}}{A_{surf}} \cos(\phi)\:\beta F \right) + q_{E} \frac{A_{E}^{proj}}{A_{surf}} F + \frac{P}{\varepsilon A_{surf}} \end{align*}$$

In the event that the the heating caused by components and the heating due to the orbited bodies thermal emissions are much lower than the heating due to the sun we can reasonably accurately approximate the above thermal balance equation too:

$$\begin{align*}
q_{E} &<< q_{S} & \text{and}& & P &<< q_{S} 
\end{align*}$$

$$\begin{align*}
T &= f\left( \frac{\alpha_{S}}{\varepsilon} \right)
\end{align*}$$

The conditions above are generally true for most spacecraft. Hence the equation produced which states that under such conditions the temperature of the craft is some function of solar [[total radiation absorption transmittance and reflectance|absorptance]] over [[real body emission|emittance]].

By carefully selecting the materials on the outside we can get desirable passive thermal regulation.
![[Pasted image 20221230185124.png]]

Something that also needs to be kept in mind when designing a spacecraft is the degradation of the materials over time due to environmental influences (mainly radiation). Typically the overall effect of this degradation is $T$ dropping over the missions lifespan.

Use of insulation and geometry are also critical especially when different sections of the vehicle have different thermal requirements.


