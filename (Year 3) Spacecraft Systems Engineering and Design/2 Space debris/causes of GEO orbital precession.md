---
aliases: ["quantifying the main causes of GEO orbital precession"]
tags: []
---

## Causes of GEO [[orbital precession]]

Here we will be quantifying the main causes of GEO [[orbital precession]].

### Quantification

#### Impact of lunar-solar gravity

It can be approximated using:

> ### $$\begin{align*} \frac{de}{dt} &=  K_{1} e\sqrt{1-e^{2}} [0.089\sin(2\omega + \Omega) - 0.158\sin(2(\omega + \Omega)) - 0.1842\sin(2\omega)] \end{align*}$$
>> where:
>> $K_{1}=$ is a constant ~$1\times10^{-10}$
>> $\omega=$ [[argument of perigee]]
>> $\Omega=$ [[orbital right ascension|right ascension of the ascending node]]
>> $e=$ [[orbital eccentricity]]
>> $t=$ time (seconds?)

The key take away is that the influence of the sun and moons gravity on [[orbital eccentricity]] $\frac{de}{dt}$ is a function of the objects eccentricity and position in orbit around the Earth and sun. 

With eccentricity playing the largest role in this type of orbital drift:
![[Pasted image 20231108184913.png]]

#### Solar radiation pressure
The long-term effects of solar radiation pressure on the eccentricity can be approximated using:

> ### $$\begin{align*} \frac{de}{dt}  &= -K_{2} a^{2}\sqrt{1- e^{2}} \sin(\lambda_{sun} - omega - Omega)  \end{align*}$$
>> where:
>> $K_{2}=$ is a constant ~$1\times10^{-10}$
>> $\omega=$ [[argument of perigee]]
>> $\Omega=$ [[orbital right ascension|right ascension of the ascending node]]
>> $a=$ [[orbital semi-major axis|semi-major axis]]
>> $e=$ [[orbital eccentricity]]
>> $t=$ time (seconds?)

![[Pasted image 20231108190931.png]]

### Takeaways

The changes due to solar radiation pressure perturbations are likely to be greater in amplitude than the changes due to luni-solar perturbations (especially for high $C_{R}$ and area to mass ratio's).

So [[orbital precession]] minimisation requires a high [[ellipse|eccentricity]], aka we target $e=0.0003$ since that's the max [[IDAC]] allows.

#### Other trade off
Eccentricity also effects the orbital volume of space the spacecraft will occupy, higher eccentricity reduces collision chance.
