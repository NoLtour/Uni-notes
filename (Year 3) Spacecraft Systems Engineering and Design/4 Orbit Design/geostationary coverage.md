---
aliases: ["GEO coverage"]
tags: []
---

## Geostationary coverage

![[obit selection#Geostationary orbit|geostationary orbit]]

### Coverage

Since GEO is be definition in plane with the equator, it can't cover the poles:

![[05-Geostationary-Sat-Ani-4077262913.gif]]

The coverage will of course be lower than the theoretical $\theta_{max}$ due to operational elevation angles being non zero ([[calculating orbital coverage]]). Further reducing the coverage.

In most cases this isn't such a huge issue though, since most people don't live in/near the poles.

The maximum latitude that geo can practically cover is about $70\degree$, beyond which the spacecraft elevation drops below $10\degree$ and connection becomes difficult.

#### Equatorial total coverage

We can calculate the minimum number of satellites needed for total coverage of the equator. From [[calculating orbital coverage]] we can get coverage diameter, dividing that by the earth's circumference gives the required count:



$$\begin{align*} 
\cos \alpha   &= \frac{R_{E}\cos E}{R_{E}+H} - E  &&\to&
 \alpha   &= \arccos \left(\frac{R_{E}\cos E}{R_{E}+H} - E \right)\\
 && B &= 2 \alpha R_{E} &&\to& B &= 2 \arccos \left(\frac{R_{E}\cos E}{R_{E}+H} - E \right) R_{E}
\end{align*}$$

If we assume a reasonable value of $E=10\degree$ then:

$$\begin{align*}
B=2R_{E}\arccos \left(\frac{R_{E}\cos E}{R_{E}+H} - E \right) &= 15903\:km
\end{align*}$$

Then number can be trivially calculated:

$$\begin{align*}
\text{int}\left(\frac{2\pi R_{E}}{B}\right)+1 &= N=3
\end{align*}$$
