---
aliases: ["perifocal frame"]
tags: []
---

## Perifocal coordinate frame

We've already seen this quite a lot, it's simply where the [[barycenter]] is taken as the centre, with the x axis aligning with the [[perigee and apogee|periapsis]] and then the y axis aligning with the $\vec{r}$ when $\theta=90\degree$:

![[Pasted image 20231216122302.png]]

The value's can be derived to be the following:

> ### $$\begin{align*} \text{general case: }&& \vec{r}  &= (r \cos\theta ) \hat{p} + (r\sin\theta)\hat{q} & &&\vec{v}&= \dot{\vec{r}}  \end{align*}$$
> ### $$\begin{align*} \text{elliptic orbit: }&& \vec{v}&= \dot{\vec{r}}= \frac{\mu}{h} ((-\sin\theta)\hat{p} + (e+\cos\theta)\hat{q}) \end{align*}$$
>> where:
>> $\hat{q}=$ y axis unit vector
>> $\hat{p}=$ x axis unit vector
>> $\vec{r}=$ position vector
>> $r=|r|=$ radius
>> $\theta=$ [[orbital elements and alignment|true anomaly]]
>> $h=$ [[specific orbital moment of momentum|specific orbital angular momentum]]
>> $\mu=$ [[standard gravitational parameter]]

Although very useful when working in a orbit, by itself it contains no information about how it's related to the real world. For this we need to define the plane this lies in using some real world reference.
