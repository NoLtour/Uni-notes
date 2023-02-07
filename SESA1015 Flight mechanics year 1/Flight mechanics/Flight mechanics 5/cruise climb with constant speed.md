---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Cruise climb with constant speed for a jet
#### Introduction
So we already know [[cruise pattern|the problem]] that [[cruise pattern|cruise climb technique]] is trying to solve.

So using the [[lift equation]] we know: $L=\frac{1}{2}\rho V^{2}SC_L$

To keep lift equal to weight as the fuel is burned we therefore must change one of the following:
- $\rho$
- $V$
- $C_L$

The technique we are focusing on here is going to assume that true airspeed and angle of attack are constant [[effect of angle on lift coefficient|(because lift coefficient's a function of angle of attack)]].

#### Calculating changes required
If $C_L$ is constant then:
$$\begin{align*}
   \frac{L}{D} &= \frac{C_L}{D_D}\\
&= \dfrac{C_L}{C_{D0} + \dfrac{KC_L^{2}}{\pi A} } 
\end{align*}$$
hence $\frac{C_L}{C_{D0} + \frac{KC_L^{2}}{\pi A} }$ will also be constant. ([[Drag coefficient|where we got the equation from]])

Now since we know that $L/D$ is constant and that $V$ is constant we can use the [[Breguet range equation (jets)]]: $R = \frac{1}{s} \frac{VL}{D} \ln\left(1+\frac{W_f}{W_s}\right)$

In the stratosphere the temperature is assumed to be constant and the thrust ($T$) of a turbo-jet engine at a fixed throttle is assumed to be proportional to the [[relative density (planes)|relative density]] ($\sigma$):
$$\begin{align*}
   T &= k\sigma\\
\therefore \frac{T_1}{T_2}&=\frac{\sigma_1}{\sigma_2} 
\end{align*}$$

Now consider that during flight the weight of fuel decreases, but total weight still equals lift. Since V and $C_L$ are constant then:
1) total weight decreases
2) height increases
3) relative density decreases
4) thrust decrease and drag decrease
6) the aircraft continues to fly at a constant speed

This pattern is the [[cruise pattern|cruise climb technique]], and this one is very common for most long haul airlines.

We can relate these values and how they change using the [[lift equation]].
$$\begin{align*}
   L&=\frac{1}{2}\rho V^{2}SC_L\\
&= W & \rho&=\sigma \rho_0 \\
\therefore W&=\frac{1}{2}(\sigma \rho_0) V^{2}SC_L
\end{align*}$$

