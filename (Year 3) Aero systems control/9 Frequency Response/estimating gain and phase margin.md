---
aliases: [""]
tags: []
---

## Estimating gain and phase margin

### Intro

This is pretty much just doing [[complex bode plots]] but with extra effort put into doing it accurately so you can measure the values. It is of course possible to find them mathematically, but the phase is a [[scientific term for pain in the ass|bitch]] to work with, since you've got to deal with [[quadrant disambiguation]].

### Example 1

Take the following:

$$\begin{align*}
G_{c}GH &= \frac{0.325}{s(s+1)(0.5+1)} & &\to&   0.325\frac{1}{s } \frac{1}{(s+1)} \frac{1}{(0.5s+1)}
\end{align*}$$

$$\begin{align*}
\text{Gain magnitude:}&&20\log_{10}0.325 &\approx -9.8 \\
\text{lag 1 freq:}&&  \frac{1}{1}&= 1 \\
\text{lag 2 freq:}&&  \frac{1}{0.5}&= 2 \\
\end{align*}$$

$$\begin{align*} 
\begin{matrix}
             & K && integrator && S_{lag\:1} && S_{lag\:2} \\
\phi_{init}= & 0\degree &+& -90\degree &+& 0\degree &+& 0\degree & =-90\degree\\
\phi_{final}= & 0\degree &+& -90\degree &+& -90\degree &+& -90\degree & =-270\degree\\\\

M_{init}= & -9.8 &+& \infty &+& 0 &+& 0 & =\infty\\
M_{final}= & -9.8 &+& -\infty &+& -\infty &+& -\infty & = -3\infty
\end{matrix}\\
\end{align*}$$

We can actually skip drawing each contribution individually, start from some known point then define gradient's around it. Here we can see that the lag's actually occur after $10^{0}=1$, then since the integrator gives no contribution there it will just be determined by $K$. 
Next we just work outwards from that point. Then the phase plots easy, we can start from -90 on the left and work towards the right.

![[Pasted image 20231209195238.png]]
Note that this way of determining everything possible before sketching is actually more accurate than drawing all the contributing graphs, but is not easy to do without practice.

From this the [[gain and phase margin|gain margin]] can be found and the [[gain and phase margin|phase margin]]:
$$\begin{align*}
GM  &= -M( \omega_{\phi=-180} ) &\to&& GM &\approx 20\:dB \\
\phi_{M}  &= \phi( \omega_{M=0} ) -- 180\degree &\to&& \phi_{M} &\approx 60\degree
\end{align*}$$

Note that the real value's are different, $GM=20dB$ and $\phi_{M}=63\degree$. But the sketch is actually not so wrong.

![[Pasted image 20231209195551.png]]

### Effect of varying values

![[Pasted image 20231209194335.png]]

In this plot, we have the function:

$$\begin{align*}
G_{c}GH &= \frac{K}{s(s+1)(0.5+1)} & &\to&  K\frac{1}{s } \frac{1}{(s+1)} \frac{1}{(0.5s+1)}
\end{align*}$$

As you expect by increasing the value of gain $K$:
- The gain plot shifts up by the log difference of the K's
- There is no change in phase as gain has no phase contribution

But the effect on stability is slightly more complicated. Not that hard to figure out looking at the sketch though:
- Gain increase leads to $M=0$ occurring later, which in this case since phase is decreasing leads to a lower phase margin
- Phase is unchanged so $\phi=-180$ occurs at the same time, but obviously the gain shift means gains higher at that point... hence gain margin is lower

This suggests that increasing gain $K$ leads to a less stable system! Note that this is somewhat dependent on the components of the system though!

If you increase gain, the [[gain and phase margin|gain margin]] will decease, but that's not always true for [[gain and phase margin|phase margin]].
