---
aliases: [""]
tags: []
---

## GEO post-mission disposal
### Intro
As outlined by [[IDAC]], we need to remove satellites from GEO. This region has REALLY heavy enforcement of that, since there is only 1 [[obit selection|geostationary orbit]], a single collision could make that entire incredibly useful region [[just like me fr fr|useless]]!

We have a few option's for disposal:
- Blow it up
- Get it to re-enter and burn up
- Move it out the way

Can you guess which one is cheap(ish) and not a terrible idea? It's move it out the way slightly, basically we just use enough fuel to get it out of the [[protected orbital regions|protected GEO orbital region]].

### Valid graveyard orbit
[[IDAC]] guidelines state that two conditions should be fulfilled to achieve a reasonable GEO graveyard orbit:

> ### $$\begin{align*} \Delta H  &\geq 235\times10^{3}\:m + 10^{6}C_{R}\frac{A}{m} &&\text{and}& e&\leq 0.003\end{align*}$$
> ### $$\begin{align*} \Delta H  &\geq 235 \:km + 10^{3} C_{R}\frac{A}{m} &&\text{and}& e&\leq 0.003\end{align*}$$
> ### $$\begin{align*} r_{p} &= a_{geo} + \Delta H  &&& r_{a} &= r_{p} \frac{1+e}{1-e} \end{align*}$$
>> where:
>> $\Delta H=$ The perigee increase from circular geostationary orbit to comply with [[IDAC]]
>> $a_{geo}=$ The [[orbital semi-major axis|semi-major axis]] of the geostationary satellite
>> $C_{R}=$ solar radiation pressure coefficient
>> $\frac{A}{m}=$ Cross sectional area to dry mass ration
>> $e=$ [[ellipse (year 2)|eccentricity]]

That [[orbital eccentricity]] is there to ensure they circularise their orbit, no point in raising the [[perigee and apogee|perigee]] if the [[perigee and apogee|apogee]] still intercepted GEO.

The $C_{R}$ bit is to counter the effects of [[space drag]].

![[Pasted image 20231109160411.png]]

### Calculating
To perform a transfer from GEO to graveyard we'll obviously require a [[impulsive orbital transfers|Hohmann transfer]].

![[impulsive orbital transfers#Transfer between non intersecting orbits|Hohmann transfer]]