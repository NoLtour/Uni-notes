---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What
## Calculating limits on preformance for a co-ordinated turn

Our course is pointless, the internet found a better method of flight [[watching this]].

### Introduction

We have this useful boi that we calculated previously:
![[calculating lift in a co-ordinated turn#^6e5848]]

We know each of these values have limitations, things like max lift coefficient, [[stalling speed]], even [[yield strength|yield stress]] and limitations on the forces the aircraft can experience. So lets rearrange our lift equation to analyse how these limitations effect our flight.

### Radius rearrangement
#### Math

$$\begin{align*}
 L &= W \sqrt{ 1 + \left(\frac{V^{2}}{gR}\right)^{2} }\\
\frac{L^{2}}{W^{2}} - 1 &= \left(\frac{V^{2}}{gR}\right)^{2}\\
\frac{g}{V^{2}} \sqrt{\frac{L^{2}}{W^{2}} - 1} &= \frac{1}{R}\\
\therefore R &= \frac{V^{2}}{g\sqrt{\frac{L^{2}}{W^{2}} - 1}}
\end{align*}$$

You can also express this interms of bank angle and speed, (the equations used here are from [[modeling a co-ordinated turn]]):

$$\begin{align*}
  L sin\phi  &= \frac{W}{g} \frac{V^{2}}{R}\\
 R   &= \frac{WV^{2}}{Lg \cdot sin\phi} & L\cos\phi = W \\\\
&= \frac{L\cos\phi\cdot V^{2}}{Lg \cdot sin\phi}\\
&= \frac{ V^{2}}{g \cdot tan\phi}
\end{align*}$$

As we can see, by increasing the [[bank angle]] we can decrease the radius of turning.

### The limit part
So if we want to find the minimum radius that the aircraft can turn, we need to get:
- Lift to a maximum
- [[load factor]] to a maximum
- [[bank angle]] to a maximum
- g to a somethingum. Yes what I'm saying is control gravity. [[ccccope|COPE]]

Each of these things have effective limits related to what the plane is resonably capible of, which I'm describing below.

![[limit on the load factor during a co-ordinated turn#Limit on the load factor during a co-ordinated turn]]

![[limit on the lift during a co-ordinated turn#Limit on the lift during a co-ordinated turn]]

#### Charting this info
Now we can define different limits on $R_{min}$ we can chart it:
![[Pasted image 20211129213223.png]]
Here the domain of flight is the region where the plane will remain flying in the desired manor.
You can also see a $V_{max}$ this is the [[design speed]] of the aircraft.

There are various implications of this chart:
- Max maneuverability occurs where the stall limit and load factor limit intercept (assuming that this is within the domain of flight, idk there might be an extreme aircraft with some weird chart)
- Stall limit increases with altitude, $R_{min}$ also increases hence at higher altitudes you are less maneuverable

#### A few more limits

![[limit on the thrust during a co-ordinated turn]]