---
aliases: [""]
tags: []
---

## Distance on a sphere

### Equation

Note that for the following [[quadrant disambiguation]] is not a concern as the trig functions return the smallest values.

> ### $$\begin{align*} \frac{d}{R_{E}} = \delta &=\arccos[ \sin (\phi_{2})\: \sin (\phi_{1}) + \cos (\phi_{2}) \:\cos \phi_{1}) \:\cos (\lambda_{2} - \lambda_{1})]  \end{align*}$$
> ### $$\begin{align*} \sin^{2} \left(\frac{\delta}{2}\right) &= \sin \left(\frac{\phi_{2}-\phi_{1}}{2}\right) + \cos\phi_{1} \cos \phi_{2}  \sin^{2} \left(\frac{\lambda_{2}-\lambda_{1}}{2}\right)  \end{align*}$$
>> where:
>> $\phi=$ [[latitude]]
>> $\lambda=$ [[longitude]]
>> $\delta=$ separation on unit sphere
>> $r=$ separation on Earth
>> $R_{E}=$ Earth's radius

The second formula is a more numerically stable form of the equation, as it doesn't accumulate as much error when given small numbers. Which can be a problem when implementing this in a comupter.

### Derivation

The shortest distance between two point's is a straight line, well we're in luck since that does hold for spherical geometry as well! Though specifically it's the shorter of the two solutions, since the straight line can go either way around the earth.

Still it's not so easy to calculate, but an expression can be derived making use of the longitude of the two points ($\lambda_{1},\lambda_{2}$) and the latitudes ($\phi_{1},\phi_{2}$)

![[Pasted image 20231215131320.png]]

First drawing the problem:

![[Pasted image 20231215134412.png]]

Then we can extract a triangle for our point of interest:

![[Pasted image 20231215134449.png]]

Making use of [[spherical triangles|spherical cosine rules]]:

$$\begin{align*}
 \cos a &= \cos b\: \cos c + \sin b \:\sin c \:\cos A &&\to&  \cos \delta &= \cos (90-\phi_{2})\: \cos (90-\phi_{1}) + \sin (90-\phi_{2}) \:\sin (90-\phi_{1}) \:\cos (\lambda_{2} - \lambda_{1})
\end{align*}$$

Recalling basic trig relations, this can be greatly simplified:

$$\begin{align*}
&& \cos (90-x) &= \sin x\\
&& \sin (90-x) &= \cos x\\
\cos \delta &= \cos (90-\phi_{2})\: \cos (90-\phi_{1}) + \sin (90-\phi_{2}) \:\sin (90-\phi_{1}) \:\cos (\lambda_{2} - \lambda_{1}) &&\to &
 \delta &=\arccos[ \sin (\phi_{2})\: \sin (\phi_{1}) + \cos (\phi_{2}) \:\cos \phi_{1}) \:\cos (\lambda_{2} - \lambda_{1})]
\end{align*}$$

Note that this $\delta$ is an arclength on the unit circle, so for Earth scale you need to multiply by Earth's radius.
