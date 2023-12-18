---
aliases:
  - mean motion
  - Kepler's equation
  - mean anomaly
  - eccentric anomaly
tags:
---
 

## Getting true anomaly from time for elliptic orbits (Kepler’s equation)

Through careful rearrangement of [[time integral for orbital motion]], it becomes possible to derive a form of the equation that can be used to get true anomaly! (This is specifically for the [[orbit categories by eccentricity|elliptical case]])

> ### $$\begin{align*} \frac{\mu^{2}}{h^{3}}(1-e^{2})^{\frac{3}{2}} t  &= 2\arctan\left( \sqrt{\frac{1-e}{1+e}} \tan \frac{\theta}{2} \right) - \frac{e\sqrt{1-e^{2}}\sin\theta}{1+e\cos\theta} \\ M_{e} &= E - e\sin E \end{align*}$$
> ### $$\begin{align*} M_{e}&= \frac{\mu^{2}}{h^{3}}(1-e^{2})^{\frac{3}{2}} t &&& E&=  2\arctan\left( \sqrt{\frac{1-e}{1+e}} \tan \frac{\theta}{2} \right) &&&  e\sin E&=  \frac{e\sqrt{1-e^{2}}\sin\theta}{1+e\cos\theta} \\\\ M_{e} &= \frac{2\pi}{T} t =nt &&& \tan \frac{E}{2} &= \sqrt{ \frac{1-e}{1+e} } \tan \frac{\theta}{2} \end{align*}$$
>> where:
>> $T=$ [[keplers laws of orbital motion#Kepler's 3rd law|orbital period]]
>> $t=$ time
>> $\theta=$ [[orbital elements and alignment|true anomaly]]
>> $h=$ [[specific orbital moment of momentum|orbital angular momentum]]
>> $\mu=$ [[standard gravitational parameter]]
>> $n= \frac{2\pi}{T}=$ [[time integral for orbital motion|mean motion]]
>> $M_{e}=$ [[time integral for orbital motion|mean anomaly]]
>> $E=$ [[time integral for orbital motion|eccentric anomaly]]
>
>> Note that is is critical to keep [[quadrant disambiguation]] in mind when working with these equations!

It is far more convenient to work with this form of the equation then translate back into $\theta$! 

As for the actual geometric meaning of the translation, what's effectively being done is translating the elliptical form into an "equivalent" circular form:

![[Pasted image 20231217120643.png]]

#### Quadrant ambiguity $\left(E=  2\arctan\left( \sqrt{\frac{1-e}{1+e}} \tan \frac{\theta}{2} \right)\right)$

Consider the form of the equation of [[time integral for orbital motion|eccentric anomaly]], does it suffer from [[quadrant disambiguation]]? 

![[Pasted image 20231217122146.png]]
![[Pasted image 20231217121723.png]]

For all value's of $E$ and $\theta$ there is a unique solution! So this is easy to handle and doesn't require special consideration. The only thing that must be considered is that most calculators return value's between $- \frac{\pi}{2}\to \frac{\pi}{2}$ but for orbital mechanics notation dictates $0\to 2\pi$, so it should be translated when appropriate.

#### Quadrant ambiguity $\left(e\sin E =  \frac{e\sqrt{1-e^{2}}\sin\theta}{1+e\cos\theta}\right)$

Consider this form of the equation of [[time integral for orbital motion|eccentric anomaly]], does it suffer from [[quadrant disambiguation]]? 

![[Pasted image 20231217122031.png]]

When plotted we can see that $cos$ will not return a unique inverse, the same obviously also applies to $\sin$. So when considering this part of the equation consideration of the real world implications can be used to aid [[quadrant disambiguation]].
