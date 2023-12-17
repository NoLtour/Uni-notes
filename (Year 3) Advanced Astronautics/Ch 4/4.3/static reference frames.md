---
aliases:
  - vernal equinox
tags:
---

## Static reference frames

### Intro

For a static reference frame we need to fix both the centre point and the axis, to do this:
- We choose the centre point as the dominant gravity well (often the Sun or the body you're orbiting, or their [[barycenter]])
- We align the axis with something that "doesn't" change

The sun is the obvious choice for the origin, but aligning the axis is a bit more complex.

### Origin alignment

As stated previously, we generally make use of the dominant gravity well's [[barycenter]] as our origin. For Earth orbit's this actually results in an [[inertial frame of reference|inertial frame]][[well a near inertial frame|*]] even though the sun exists. The reason this is the case is that both the Earth and a near Earth satellite experience the "same" attraction from the sun, or at least a force vector so negligibly different that it's irrelevant. 

$$\begin{align*}
&& \vec{g} &= \frac{\mu}{\vec{r}|\vec{r}|}\\
\vec{r}_{Earth} &\approx \vec{r}_{SC} &&\to& \vec{a}_{Earth} &\approx \vec{a}_{SC}
\end{align*}$$
This applies to any case where one gravity well is extremely dominant, of course as you leave LEO this assumption becomes less and less valid.

![[Pasted image 20231216123935.png]]


### Axis alignment

#### Vernal equinox ($x$ axis)

Classically the $x$ axis has been aligned with the vernal equinox. The vernal equinox is a celestial event that occurs around March 20th each year when the Sun crosses the celestial equator from south to north. It marks the beginning of spring in the Northern Hemisphere and autumn in the Southern Hemisphere, with day and night approximately of equal length worldwide.

![[Pasted image 20231216114847.png]]

This is actually a pretty good choice, as it's practical to measure globally and "static". Problem is, it's not actually static. The wobble of the Earth means the vernal equinox changes over millennia.

#### Earth's angular momentum vector 

Obviously this is just the normal vector to the Earth's plane of motion, variation is minute so it's a pretty static reference.

#### Earth's spin axis

This is not really that static on a solar scale, it wobbles. Useful for Earth orbiting calculations but limited utility outside of that.

#### Quasar locations

Modern approaches make use of Quasars, they are so far away but also convenient to measure. This means by using them as reference point's we can define a very static axis!
