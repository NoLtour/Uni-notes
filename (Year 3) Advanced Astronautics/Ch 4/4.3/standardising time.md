---
aliases:
  - calendar year
  - tropical year
  - sidereal year
  - UTC
  - TAI
tags:
---

## Standardising time

We've come a long way in standardising seconds, which are now defined by atomic clocks. But what's the answer to a simple question: how many seconds are in a year?

Turns out that's a real pain in the ass to answer, since we have lots of definitions of what a year is:
- Calendar year, 365 or 366 days, depending on the year
- Tropical year, time between consecutive [[static reference frames|vernal equinox]]'s
- Sidereal year, Earth's orbital period around the sun

These differences in definition are caused by 2 facts:
- The rotation of the Earth is not fully synchronized with tropical years by an integer ratio
- The exact orbit and rotation of the Earth fluctuate slightly

### Practical

#### Civil time (UTC)

This is what get's returned when you do most "getTime" functions in programs, and is what your computer's clock says. It is constantly slightly adjusted with leap seconds inserted all over the place:

![[Pasted image 20231216131912.png]]

This plot shows the difference between civil time and universal time (defined by Earths rotation), the insertion of leap seconds is all over the place and a real pain in the ass to keep track of. Which is why pretty much all time conversions use library's, since implementing it manually is a real pain in the ass.

#### International atomic time

This is basically just counting up from some reference (synced with UTC in 1958) in seconds using atomic clocks, as of 2020 it has a 37 second difference from UTC. For precise applications we use this for finding the change in seconds between two times.

#### Sidereal year

This is the period of the Earths orbit around the sun, it is equal to:

> ### $$\begin{align*} \text{Year}_\text{sidereal} &= 365.256363004 \: \text{SI-days}  \end{align*}$$

Compared to a tropical year, it is 20 min's longer. This is most useful for orbital mechanics, such as calculating the period of a geo satellite.

This is actually a bit more complex than it would seem:
- The number of inertial rotations of the Earth per full orbit around the sun: $N_{i} = \frac{P_{i}}{p_{i}}= 366.256363004$
- The number of sun facing rotations (days): $N_{r} = N_{i} - 1 = \frac{P_{i}}{p_{r}}=365.256363004$

($P_{i}=$ period for a [[standardising time|sidereal year]], $p_{i}=$ Earths rotation period in inertial frame, $p_{r}=$ Earth's day/night cycle an SI-day)

Since the Earth rotates as it moves around the sun there is a difference between the rotations in an inertial frame and the number of day/night cycles.

So if we want the period for a geo sat, we need to find $p$, which isn't so hard:

$$\begin{align*}
&&&& N_{i} &= \frac{P_{i}}{p_{i}}\\
N_{r} &=  \frac{P_{i}}{p_{r}} &&\to& N_{r}p_{r} &= P_{i}\\
&& N_{i} - 1 &=  \frac{P_{i}}{p_{r}} &&\to& \frac{N_{r}p_{r}}{p_{i}} - 1 &=  \frac{N_{r}p_{r}}{p_{r}} &&\to& \frac{N_{r}p_{r}}{N_{r} +1}   &=  p_{i} =23.9345\:\text{hours}
\end{align*}$$


