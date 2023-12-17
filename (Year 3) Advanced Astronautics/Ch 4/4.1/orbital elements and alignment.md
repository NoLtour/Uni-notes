---
aliases:
  - true anomaly
  - orbital alignment
  - inclination
  - longitude of the ascending node
  - argument of periapsis
tags:
---

## Orbital elements and alignment

### Intro

It is actually possible to completely define an orbit's shape and orientation in 3D space using:
- [[orbital semi-major axis|semi-major axis]]
- [[eccentricity vector|eccentricity]]
- [[orbital elements and alignment|inclination]]
- [[ascending node]]
- [[perigee and apogee|periapsis]]

This is demonstrated in the following content.

### Orbit shape

> ![[Pasted image 20231215162303.png]]
> ### $$ e \geq 0 $$
>> where:
>> $f=$ true anomaly, angle from perigee to current spacecraft about the focus
>> $r=$ distance from [[barycenter]]
>> $a=$ [[orbital semi-major axis|semi-major axis]]
>> $b=$ [[ellipse (year 2)|semi-minor axis]]
>> $e=$ [[ellipse (year 2)|eccentricity]]

### Alignment

> ### ![[Pasted image 20231216160501.png]]
> ### $$\begin{align*} &0\degree\leq i \leq 180\degree &&&  &0\degree\leq \Omega \leq 360\degree  &&&  &0\degree\leq \omega \leq 360\degree  \end{align*}$$
>> where:
>> The reference direction is used to define where on the plane of reference we take the ascending node angle from
>> The ascending node is the point where the orbit intercepts with the plane of reference
>> $i=$ inclination, the angle between the orbital plane and the reference plane
>> $\Omega=$ longitude of the ascending node, this is the anticlockwise angle from the reference direction to the ascending node
>> $\omega=$ argument of periapsis, the angle between the ascending node and the [[perigee and apogee|periapsis]]
>> 
>> The order to define an orbit is:
>> $$\begin{align*} && \Omega=\text{Long of }&\text{ascending node}& && i=\text{in}&\text{clenation}& && \omega=\text{arg of }&\text{periapsis} \\&\text{refrerence direction} &&\to& &\text{ascending node} &&\to& &\text{inclined plane about ascending node}  &&\to& &\text{final periapsis} \end{align*}$$
>> ![[2023-12-16 16-46-42.mp4]]

With these defined we can describe the position of a orbit relative to some axis in 3D space.

Frustratingly previous years define these values in a highly specific context, which makes it confusing. These definitions are generalised. 
