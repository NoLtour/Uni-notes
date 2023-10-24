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

It's not so much harder when considering supersonic flows, pretty much we just need to take the [[stagnation pressure]] from after a normal shock, we'll assume $p$ is known from altitude tables or something. So in summery the input's we've got are $P_{02}$ and $P_{1}$, we've got lots of equations given as pressure ratio's, so lets express our pressures as a ratio:

$$\begin{align*}
\frac{P_{02}}{P_{1}} &= \frac{P_{2}}{P_{1}} \frac{P_{02}}{P_{2}}
\end{align*}$$



Whipping out the [[normal shock properties equations]] we can get $\frac{P_{2}}{P_{1}}$, then we can simply get $\frac{P_{02}}{P_{2}}$ from [[supersonic flow properties equations]]:

$$\begin{align*}
 \frac{P_{2}}{P_{1}} &= \frac{2\gamma M_{1}^{2} - (\gamma - 1)}{\gamma+1} & \frac{P_{02}}{P_{2}} &= \left(1 + \frac{\gamma-1}{2} M_{2}^{2}\right)^\frac{\gamma}{\gamma-1}
\end{align*}$$
Hence: $$\begin{align*} \frac{P_{02}}{P_{1}} &= \frac{P_{2}}{P_{1}} \frac{P_{02}}{P_{2}}  = \left[1 + \frac{2\gamma(M_{1}^{2}-1)}{\gamma+1}\right] \left[1 + \frac{\gamma-1}{2}M^{2}_{2}\right]^\frac{\gamma}{\gamma-1} \end{align*}$$
Then $M_{2}$ can be found from $M_{1}$, once again [[normal shock properties equations]]:

$$\begin{align*}
&&M_{2}^{2}  &= \frac{(\gamma - 1) M_{1}^{2} + 2}{2\gamma M_{1}^{2} - (\gamma - 1)}\\
\frac{P_{02}}{P_{1}} &=   \left[1 + \frac{2\gamma(M_{1}^{2}-1)}{\gamma+1}\right] \left[1 + \frac{\gamma-1}{2}M^{2}_{2}\right]^{\frac{\gamma}{\gamma-1}}& &\to & \frac{P_{02}}{P_{1}} &=   \left[1 + \frac{2\gamma(M_{1}^{2}-1)}{\gamma+1}\right] \left[1 + \frac{\gamma-1}{2}\frac{(\gamma - 1) M_{1}^{2} + 2}{2\gamma M_{1}^{2} - (\gamma - 1)}\right]^\frac{\gamma}{\gamma-1}
\end{align*}$$

You'll have to take my word for it, but simplifying that abomination will eventually give you:

$$\begin{align*}
\frac{P_{02}}{P_{1}} &= \left[ \frac{(\gamma+1)^{\gamma+1} \left(\frac{M_{1}^{2}}{2}\right)^{\gamma} }{2\gamma M_{1}^{2} - (\gamma - 1)} \right]^{\frac{1}{\gamma-1}}
\end{align*}$$

Ok now [[lmao that aint happening ever|good luck rearranging for M]], at which point you can times by $a$ and get airspeed... This complexity is why you should give up and just use the normal shock tables! (This is the method in exams lmao)
