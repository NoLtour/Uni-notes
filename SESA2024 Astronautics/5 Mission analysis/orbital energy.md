---
aliases: [""]
tags: []
---

## Orbital energy

We can easily derive a relationship for satellite height and velocity using the fact that energy is conserved:
$$\begin{align*}
K &= \frac{1}{2}mV^{2} + \int^{r}_{0} \frac{GMm}{r^{2}} \cdot dr\\
&= \frac{1}{2}mV^{2} - \frac{GMm}{r} & \mu &= GM \\
\frac{K}{m} &= \frac{V^{2}}{2} - \frac{\mu}{r} \\
&& &\frac{K}{m}\text{ is a constant}\\
\frac{V_{p}^{2}}{2} - \frac{\mu}{r_{p}}  &= \frac{V_{a}^{2}}{2} - \frac{\mu}{r_{a}} 
\end{align*}$$

Here $r_{a}$ is radius at [[perigee and apogee|apogee]] and $r_{p}$ is radius at [[perigee and apogee|perigee]]:
![[Pasted image 20221107101931.png]]
Then we know that [[specific orbital moment of momentum|orbital angular momentum]] is conserved : 
$$\begin{align*}
h  &= rV\\
&& &h\text{ is a constant}\\
 \frac{V_{a}}{V_{p}} &= \frac{r_{p}}{r_{a}} 
\end{align*}$$
Hence combining these:
$$\begin{align*}
\frac{K}{m} + \frac{\mu}{r } &= \frac{V ^{2}}{2}   \\
 \frac{\frac{K}{m} + \frac{\mu}{r_{a} }}{\frac{K}{m} + \frac{\mu}{r_{p} }} &= \frac{\frac{V_{a} ^{2}}{2}}{\frac{V_{b} ^{2}}{2}} & \frac{V_{a}}{V_{p}} &= \frac{r_{p}}{r_{a}} \\
 &= \frac{ r_{p} ^{2} }{ r_{a} ^{2} } \\
 \frac{K}{m} + \frac{\mu}{r_{a} } &= \frac{K  r_{p} ^{2}}{m r_{a} ^{2}} + \frac{\mu r_{p}  }{r_{a} }  \\
 \frac{K}{m}\left(1 - \frac{   r_{p} ^{2}}{  r_{a} ^{2}}\right) &=   \frac{\mu r_{p}  }{r_{a} } - \frac{\mu}{r_{a} } 
\end{align*}$$
