---
aliases:
  - circular orbit
  - elliptical orbit
  - parabolic orbit
  - hyperbolic orbit
  - escape velocity of hyperbolic orbit
tags:
---

## Orbit categories by eccentricity

So far we've covered circular and elliptical orbits, but if you keep pushing that $V$ term eventually you reach escape velocity, at which point $e\geq1$.

The shape's for each eccentricity can be shown in the following diagram:

![[Kegelschnitt-schar-s-4249920552.png]]

Another way of considering these is interms of energy debt, hyperbolic orbits have excess energy while elliptical and below are in energy debt (trapped inside a gravity well).

#### Types

##### Circular orbit ($e=0$)

Classical circular orbit, here the [[ellipse (year 2)|semi-major axis]] equals the [[ellipse (year 2)|semi-minor axis]]. They are really easy and convenient to work with.

In real life no orbit is perfectly circular, but it's a good enough approximation for really really low eccentricity orbits.

##### Elliptical orbit ($0<e<1$)

[[if this is the case please drop this course|idk, never heard of it]]

##### Parabolic orbit ($e=1$)

Just like circular orbits, these are theoretical as no real orbit has an exact $e=1$, they are special as their terminal exit velocity is zero ($V_{\infty}=0$).

![[Pasted image 20231215200624.png]]

##### Hyperbolic orbit ($e>1$)

These have asymptotes which area approached as $V\to V_{\infty}$, they also have a mirrored copy about the centre, but that's more just a fragment left over from the maths than a real thing we care about.

![[Pasted image 20231215200610.png]]

> ![[Pasted image 20231216010807.png]]
> ### $$\begin{align*} r(\theta)  &= \frac{p}{1+e\cos(\theta)}  &&& r_{p} &= \frac{p}{1+e} &&& a &= \frac{p}{1-e^{2}}<0 &&& \varepsilon>0 \end{align*}$$
> ### $$\begin{align*} v_{\infty} &= \sqrt{- \frac{\mu}{a}}>0 &&& \theta_{\infty} &= \arccos\left( -\frac{1}{e} \right) &&& \delta &= 2 \arcsin\left(\frac{1}{e}\right) \end{align*}$$
>> where:
>> $e=$ [[ellipse (year 2)|eccentricity]]
>> $p=$ [[perigee and apogee|perigee]]
>> $\theta=$ [[orbital true anomaly]]
>> $r=$ separation
>> $a=$ [[ellipse (year 2)|semi-major axis]], note for the hyperbolic case it's more just a useful number than something that actually exists
>> $v_{\infty}=$ escape velocity
>> $\varepsilon=$ [[specific orbital energy|orbital energy]]


