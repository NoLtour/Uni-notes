---
aliases: 
tags:
---

## Time integral for orbital motion

### Getting time from [[orbital elements and alignment|true anomaly]]

To get time back into the orbital motion equations, we make use of:

$$\begin{align*}
\frac{d\theta}{dt} &=  \frac{h}{r^{2}} &&\to& \int^{t}_{t_{0}} dt &= \int^{\theta}_{\theta_{0}} \frac{h}{r^{2}}d\theta 
\end{align*}$$

From that point we can derive a useful set of equations for each [[orbit categories by eccentricity|orbit type]] by subbing in the relevant relations, not going to proof it here though. 

> ### $$\begin{align*} (e<1)\text{ elliptic case: }& & t &=  \frac{h^{3}}{\mu^{2} (1-e^{2} )^{\frac{3}{2}}} \left( 2 \arctan\left( \sqrt\frac{1-e}{1+e} \tan \frac{\theta}{2} \right) - \frac{e\sqrt{1-e^{2}} \sin\theta}{1+e\cos\theta} \right) \\\\ (e=1)\text{ parabolic case: }& & t &=  \frac{h^{3}}{\mu^{2}  } \left(\frac{1}{2}\tan \frac{\theta}{2} + \frac{1}{6} \tan^{3} \frac{\theta}{2} \right) \\\\(e>1)\text{ hyperbolic case: }& & t &=  \frac{h^{3}}{\mu^{2} (e^{2} - 1)} \left( \frac{e\sin\theta}{1+e \cos\theta} - \frac{1}{\sqrt{e^{2}-1}} \ln\left(\frac{\sqrt{e+1}+\sqrt{e-1}\tan \frac{\theta}{2} }{\sqrt{e+1}-\sqrt{e-1}\tan \frac{\theta}{2} }\right) \right) \end{align*}$$
>> where:
>> $t=$ time
>> $\theta=$ [[orbital elements and alignment|true anomaly]]
>> $h=$ [[specific orbital moment of momentum|orbital angular momentum]]
>> $\mu=$ [[standard gravitational parameter]]

Now solving these to get $\theta$ in terms of $t$ is [[I mean why not give it a go|non-trivial]], so if you need to solve em backwards I'd suggest using some numerical solver... or just read the next section.

