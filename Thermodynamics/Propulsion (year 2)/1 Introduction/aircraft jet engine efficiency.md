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


Now the KE used in the air through the engine is simple enough to find, just KE of air out minus KE of air in:

$$\begin{align*}
KE_{in} &= \frac{1}{2} V_{\infty}^{2} \dot{m}_{a} & KE_{exit} &= \frac{1}{2} V_{jet}^{2} \dot{m}_{a}(1+f)
\end{align*}$$
$$\begin{align*}
\dot{W}_{jet} &= KE_{exit} - KE_{in}\\
&=  \frac{1}{2} V_{jet}^{2} \dot{m}_{a}(1+f) - \frac{1}{2} V_{\infty}^{2} \dot{m}_{a}\\
&= \frac{1}{2} \dot{m}_{a} [ (1+f) V_{jet}^{2} - V_{\infty}^{2} ]
\end{align*}$$



Now we can sub back to get propulsive efficiency:

$$\begin{align*}
\eta_{P} &= \frac{\dot{W}_{aircraft}}{\dot{W}_{jet}} & \to& & \eta_{P} &= \frac{V_{\infty} \dot{m}_{a}[(1+f) V_{jet} - V_{\infty}] + V_{\infty} A_{j} (P_{j}-P_{a}) }{\frac{1}{2} \dot{m}_{a} [ (1+f) V_{jet}^{2} - V_{\infty}^{2} ]} 
\end{align*}$$

Now that looks disgusting, and it is ([[math vomit is great|yay]])! So we take the ever present engineering approach of "what can I cut out to make my life easyer?" and the answer is 2 things:
- We know that for a not shit jet engine the amount of fuel relative to the amount of air is tiny, so $f<<1$ and hence $f+1\approx1$
- Secondly for a non shit 
