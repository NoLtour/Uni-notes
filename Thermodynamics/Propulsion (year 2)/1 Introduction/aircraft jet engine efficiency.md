---
aliases: ["propulsive efficiency","thermal efficiency"]
tags: []
---

## Aircraft jet engine efficiency

### Intro

Ok so we can define overall efficiency as the propulsive efficiency (a measure of how well an engine can convert the kinetic energy into displacement work) of the engine multiplied by the thermal efficiency (how well an engine can convert heat into kinetic energy) of the engine:

$$\begin{align*}
\eta_{O} &= \eta_{P} \times \eta_{th}
\end{align*}$$

This doesn't really tell us much though, so lets get some equations for propulsive and thermal efficiency!

### Propulsive efficiency

So this is how efficient we use our KE, so it's just the power of the engine divided by the total KE imparted into the environment by the engine:

$$\begin{align*}
\eta_{P} &= \frac{\dot{W}_{aircraft}}{\dot{W}_{jet}}
\end{align*}$$

The equation for engine power is easy enough, just simple thrust multiplied by velocity of the vehicle. We know the velocity of the vehicle is just $V_{\infty}$ and thrust is [[momentum conservation applied to a jet engine|thrust of a jet engine]] so combining this:

$$\begin{align*}
\dot{W}_{aircraft} &= V_{\infty} \times F & F  &= \dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] + A_{j}(P_{j}-P_{a})\\
&= V_{\infty} \dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] + V_{\infty} A_{j} (P_{j}-P_{a}) 
\end{align*}$$
