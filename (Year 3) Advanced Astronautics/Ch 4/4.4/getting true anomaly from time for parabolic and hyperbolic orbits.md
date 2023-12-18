---
aliases:
  - Barker's equation 
  - parabolic eccentric anomaly
  - parabolic mean anomaly
  - hyperbolic eccentric anomaly
  - hyperbolic mean anomaly
  - hyperbolic Kepler's equation 
tags:
---

## Getting true anomaly from time for parabolic orbits

In a similar fashion to [[getting true anomaly from time for elliptic orbits]] we can do so for [[orbit categories by eccentricity|parabolic orbits]]:

> ### $$\begin{align*}  M_{p} &=  \frac{1}{2} B + \frac{1}{6} B^{3} \end{align*}$$
> ### $$\begin{align*} M_{p}&= \frac{\mu^{2}}{h^{3}} t  &&& B &= \tan \frac{\theta}{2} \end{align*}$$
>> where:
>> $t=$ time
>> $\theta=$ [[orbital elements and alignment|true anomaly]]
>> $h=$ [[specific orbital moment of momentum|orbital angular momentum]]
>> $\mu=$ [[standard gravitational parameter]]
>> $M_{p}=$ [[getting true anomaly from time for parabolic and hyperbolic orbits|parabolic mean anomaly]]
>> $E=$ [[getting true anomaly from time for parabolic and hyperbolic orbits|parabolic eccentric anomaly]]

## Getting true anomaly from time for hyperbolic orbits

In a similar fashion to [[getting true anomaly from time for elliptic orbits]] we can do so for [[orbit categories by eccentricity|hyperbolic orbits]]:

> ### $$\begin{align*}  M_{h} &=  e\sinh F - F \end{align*}$$
> ### $$\begin{align*} M_{h} &= \frac{\mu^{2}}{h^{3}}(e^{2} -1)^{\frac{3}{2}} t &&& \tanh \frac{F}{2} &= \sqrt{\frac{e-1}{e+1}} \tan \frac{\theta}{2} \\ &= t\sqrt{\frac{\mu}{-a^{3}} } \end{align*}$$
>> where:
>> $t=$ time
>> $\theta=$ [[orbital elements and alignment|true anomaly]]
>> $a=$ [[orbital semi-major axis|semi-major axis]] (same equation, different meaning in [[orbit categories by eccentricity|hyperbolic case]])
>> $\mu=$ [[standard gravitational parameter]]
>> $M_{h}=$ [[getting true anomaly from time for parabolic and hyperbolic orbits|hyperbolic mean anomaly]]
>> $F=$ [[getting true anomaly from time for parabolic and hyperbolic orbits|hyperbolic eccentric anomaly]]

Something great about this equation is there is no issues surrounding angle disambiguation, since both $\sinh$, $\tan \frac{\theta}{2}$ and $\tanh$ all have unique solutions in their range!
