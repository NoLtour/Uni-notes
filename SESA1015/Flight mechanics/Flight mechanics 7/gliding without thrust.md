---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can you model
## Gliding without thrust

![[Pasted image 20211123174004.png]]

We can model [[angle of attack]] as $\theta$ then work with that to define useful relationships

#### Angle of attack
We can get a descent approximation of angle of attack from the [[lift to drag ratio]] using the method below:
$$\begin{align*}
   & & L &= W \cos \theta & D = W\sin\theta\\
\frac{D}{L} &= \frac{W\sin\theta}{W \cos \theta}\\
&= \tan \theta\\
\therefore \frac{D}{L}&\approx \theta \:\:\:small\:angle\:approx
\end{align*}$$

Also see [[minimum glide angle]].

#### Rate of descent
We can get a descent approximation of rate of descent using small angle formula:
$$\begin{align*}
   - \frac{dh}{dt} &= -h\\
&= V\sin\theta \approx V\theta \\
&= V \frac{D}{W} 
\end{align*}$$

Also see [[minimum rate of descent]].