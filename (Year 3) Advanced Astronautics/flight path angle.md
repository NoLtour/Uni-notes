---
aliases: [""]
tags: []
---

## Flight path angle ($\gamma$)

This is the angle between the local horizon and the velocity vector. Note that the local horizon is just perpendicular to the direction to the [[barycenter]]. In a circular orbit the flight path angle would therefor always be zero.

![[Pasted image 20231216002535.png]]

It's pretty simple to define mathematically, though finding the velocities requires derivation:

> ### $$\begin{align*} \tan \gamma  &= \frac{v_{r}}{v_{\perp}}  \end{align*}$$
> ### $$\begin{align*}  v_{r} &= \frac{ \mu  }{ h }  e \sin\theta &&& v_{\perp} &= \frac{\mu}{h}(1+e\cos\theta) &&& \vec{h} &= \vec{r} \times \vec{v}_{\perp}  \end{align*}$$
>> where:
>> $\gamma=$ [[flight path angle]]
>> $v_{\perp}=$ velocity component normal to horizon
>> $v_{r}=$ velocity component perpendicular to horizon
>> $h=$ [[specific orbital moment of momentum|orbital angular momentum]] magnitude
>> $\mu=$ [[standard gravitational parameter]]
>> $\theta=$ [[orbital precession]]
>> $e=$ [[eccentricity vector|eccentricity]]

This set of equation holds for any orbit, including both [[orbit categories by eccentricity|elliptical]] and [[orbit categories by eccentricity|hyperbolic orbit]]s.

### Derivation of velocities

Making use of the [[specific orbital moment of momentum|orbital angular momentum]]:

$$\begin{align*}
&& \vec{v} &= \vec{v}_{r} + \vec{v}_{\perp} &&& \vec{v}_{r}\times\vec{r}&= 0 \\
\vec{h} &= \vec{r} \times \vec{v} &&\to& \vec{h} &= \vec{r} \times (\vec{v}_{r} + \vec{v}_{\perp})  &&\to&  \vec{h} &= \vec{r} \times \vec{v}_{\perp} 
\end{align*}$$

Then from the fundamental definition of [[specific orbital moment of momentum|orbital angular momentum]] we can intuitively derive a second expression (additionally we use from [[orbital path in ellipse form]]):

$$\begin{align*} 
&&&&&& r &=  \frac{h^{2}}{\mu(1+e\cos\theta)}\\
h &= r^{2} \dot{\theta} &&\to& h &= r v_{\perp} &&\to& \frac{\mu}{h}(1+e\cos\theta) &= v_{\perp}
\end{align*}$$

Finding $v_{r}$ is easy:

$$\begin{align*}
 &&&&&&\frac{h}{r^{2}}&= \dot{\theta}&&&r &=  \frac{h^{2}}{\mu(1+e\cos\theta)} \\
 \frac{d}{dt} r &= \frac{d}{dt}\frac{h^{2}}{\mu(1+e\cos\theta)}  &&\to& v_{r} &= \frac{h^{2}}{\mu} \frac{\dot\theta e \sin\theta }{(1+e\cos\theta)^{2}} &&\to&
 v_{r} &= \frac{h^{3}}{\mu r^{2}} \frac{ e \sin\theta }{(1+e\cos\theta)^{2}} &&\to&
 v_{r} &= \frac{ \mu  }{ h }  e \sin\theta
\end{align*}$$
