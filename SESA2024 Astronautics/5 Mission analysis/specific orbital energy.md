---
aliases: ["orbital energy"]
tags: []
---

## Specific orbital energy
### Equation

#### General equation

> ### $$ \varepsilon = \frac{KE+PE}{m} $$ 
> ### $$ \varepsilon =  -\frac{ \mu  }{ r_{a}  +  r_{p}  } = - \frac{\mu}{2a} $$
> ### $$ \varepsilon = \frac{V^{2}}{2} - \frac{\mu}{r}  $$
> ### $$ V = \sqrt{2\mu\left( \frac{1}{r} - \frac{1}{r_{a} + r_{p}} \right)} = \sqrt{ \mu\left( \frac{2}{r} - \frac{1}{a} \right)} $$
>> where:
>> $\varepsilon= \frac{K}{m} =$ [[specific orbital energy]]
>> $\mu=GM=$ [[universal constant of gravitation|gravitational constant]] times mass of orbited body
>> $r_{a}=$ radius of [[perigee and apogee|apogee]]
>> $r_{p}=$ radius of [[perigee and apogee|perigee]]
>> $r=$ the radius at some point in the orbit
>> $V=$ the velocity at some point in the orbit
>> $m=$ mass of satellite
>> $a=$ [[orbital semi-major axis|semi-major axis]]
>> $K=KE+PE=$ sum of energy's in the orbit, which is of course constant of a set orbit

#### Circular case
The equation greatly simplifies in the case that the radius is constant (aka a circular orbit):
> ### $$ r = a $$ 
> ### $$ V = \sqrt{\frac{\mu}{r}} = \sqrt{\frac{\mu}{a}} $$ 
>> where: 
>> $r=$ the radius at some point in the orbit
>> $V=$ the velocity at some point in the orbit 
>> $a=$ [[orbital semi-major axis|semi-major axis]] 

### Derivation
We can easily derive a relationship for satellite height and velocity using the fact that energy is conserved:
$$\begin{align*}
K &= \frac{1}{2}mV^{2} + \int^{r}_{0} \frac{GMm}{r^{2}} \cdot dr\\
&= \frac{1}{2}mV^{2} - \frac{GMm}{r} & \mu &= GM \\
\frac{K}{m} &= \frac{V^{2}}{2} - \frac{\mu}{r} \\ 
\end{align*}$$

Then we know that [[specific orbital moment of momentum|orbital angular momentum]] is conserved : 
$$\begin{align*}
\underline{h}  &= \underline{r} \times \underline{V}\\
&& &h\text{ is a constant}\\
 \frac{V_{a}}{V_{p}} &= \frac{r_{p}}{r_{a}} 
\end{align*}$$
Here $r_{a}$ is radius at [[perigee and apogee|apogee]] and $r_{p}$ is radius at [[perigee and apogee|perigee]]. Since $\underline{r}$ and $\underline{V}$ is a vector, by picking opposite points on the ellipse it becomes possible to simplify the relationship as seen above.
![[Pasted image 20221107101931.png]]
Hence combining these:
$$\begin{align*}
\frac{K}{m} + \frac{\mu}{r } &= \frac{V ^{2}}{2}   \\
 \frac{\frac{K}{m} + \frac{\mu}{r_{a} }}{\frac{K}{m} + \frac{\mu}{r_{p} }} &= \frac{\frac{V_{a} ^{2}}{2}}{\frac{V_{b} ^{2}}{2}} & \frac{V_{a}}{V_{p}} &= \frac{r_{p}}{r_{a}} \\
 &= \frac{ r_{p} ^{2} }{ r_{a} ^{2} } \\
 \frac{K}{m} + \frac{\mu}{r_{a} } &= \frac{K  r_{p} ^{2}}{m r_{a} ^{2}} + \frac{\mu r_{p}  }{r_{a}^2 }  \\
 \frac{K}{m}\left(1 - \frac{   r_{p} ^{2}}{  r_{a} ^{2}}\right) &=  \frac{\mu}{r_{a} }\left(  \frac{r_{p}}{r_{a}} - 1 \right)\\
 \frac{K}{m} &= \frac{ \mu (   r_{p} - r_{a} )}{\left(r_{a}^{2} -  r_{p} ^{2} \right)}\\
 &=  \frac{ \mu (   r_{p} - r_{a} )}{ (r_{a}  -  r_{p} )(r_{a}  +  r_{p} )}\\
 &=  -\frac{ \mu  }{ r_{a}  +  r_{p}  }\\

\end{align*}$$
This final form can clearly be converted into $\frac{K}{m}=- \frac{\mu}{2a}$ using the clear fact that $2a=r_{a}+r_{p}$.