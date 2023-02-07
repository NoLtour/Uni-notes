---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you model
## Steady climbing flight

The forces acting on an aircraft in steady climbing flight are shown here:
![[Pasted image 20211124105215.png]]

Where:
- $\theta=$ [[climb angle]]
- $\gamma=$ [[thrust vector angle]]

You can write the equibilbrium equations as:

$$\begin{align*}
  & & L+T\sin \gamma &= W \cos \theta & T\cos\gamma-D&=W\sin\theta\\
\frac{dh}{dt} &= V\sin \theta & & & \frac{T\cos\gamma-D}{W}&=\sin\theta\\
&= V \frac{T\cos\gamma-D}{W}
\end{align*}$$

^ea3763

Note that at a [[thrust vector angle]] of zero, this equation is known as the [[specific excess thrust]]. We can also find the climb angle from [[specific excess thrust]] for small angles of $\theta$ (note that we are assuming that $W=L$ although $W=Lcos\theta$ because $\cos\theta \approx 1$):

$$\begin{align*}
\frac{dh}{dt} &= V \frac{T\cos\gamma-D}{W} & \frac{dh}{dt} &= V\sin\theta\\
V\sin\theta &= V \frac{T\cos\gamma-D}{W}\\
\therefore \theta &= \sin^{-1}\left(\frac{T\cos\gamma-D}{W}\right)
\end{align*}$$

Note that this equation only works for slow rates of ascent and very shallow angles as it assumes that $\rho$ and such are constant, so it's not very useful outside of approximation.