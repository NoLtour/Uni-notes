---
aliases: [""]
tags: []
---

## Battery and array sizing assessment order
### Intro
When considering the hardware required to manage the power of a vehicle the order (RE WRITE)

### Example

> Estimate the battery and array size for a LEO spacecraft in a 800 km altitude circular orbit, given an average power requirement for payload and subsystems of 1 kW over a mission lifetime of 2 years.

First it is necessary to determine the time spent in sunlight vs time spent in the shadow of the orbited celestial body.
![[Pasted image 20221115124347.png]]
Since this is a circular orbit we know that the radial velocity is constant hence time spent in eclipse is simply the orbital period multiplied by the fraction of angle of the eclipse region over 360:

$$\begin{align*}
t_{e} &= \tau \frac{180\degree-2\alpha}{360\degree} 
\end{align*}$$
For a elliptical orbit you'd use the equations from [[Mission analysis overview|this page]]. Time spent in the sun is obviously just orbital period minus the time spent in the eclipse:
$$\begin{align*}
t_{s} &= \tau - t_{e}
\end{align*}$$
From this the total power required for the dark region vs the excess power generation required to charge the batteries for this region can be easily found.