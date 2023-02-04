---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Calculating the pressure of a gas molecule
#### Into
I reiterate, boyles law ect = trash. Just use the one we are about to make (I really don't know why we learn about obsolete equations, too many names to remember).

### Modelling a molecule of gas

First lets take a molecule of gas in a box with sides of length $L$.

![[Pasted image 20211112082420.png]]

When it hits a wall it bounces off with an equal but negative momentum so:

momentum before + momentum change = momentum after

$$\begin{align*}
   m_a u_x + -2 m_a u_x &= - m_a u_x\\
 \therefore momentum\:excerted\:on\:wall=2m_a u_x&  
\end{align*}$$

Now we have the momentum excerted on the wall during one collision but we need to know the number of collisions per second with this specific wall. The number of collisions per second with this wall will be:
$$\begin{align*}
   u_x &= \frac{2L}{t}\\
t &= \frac{2L}{u_x} 
\end{align*}$$

Recalling $F=\frac{mv-mu}{t}$:
$$\begin{align*}
   F &= \frac{2m_au_x}{\frac{2L}{u_x} } \\
&= \frac{m_au_x^{2}}{L}
\end{align*}$$

We also know $p = \frac{F}{A}$:
$$\begin{align*}
   p &= \frac{\frac{m_au_x^{2}}{L}}{L^{2}}\\
&= \frac{m_au_x^{2}}{L^{3}}\\
&=\frac{m_au_x^{2}}{V}
\end{align*}$$

In reallity the particle is moving in 3D, and $u \frac{1}{\sqrt{3}}=u_x$ (think about it interms of components of a 3D vector):
$$\begin{align*}
   p &= \frac{m_a(u \frac{1}{\sqrt{3}})^{2}}{V}\\
&= \frac{m_a \bar{u^{2}} }{3V}
\end{align*}$$

There are also N number of particles so total pressure is:
$$\begin{align*}
   p &= \frac{N m_a \bar{u^{2}} }{3V}\\
pV &= \frac{N m_a \bar{u^{2}} }{3}\\
&= \frac{2N}{3} (\frac{1}{2}  m_a \bar{u^{2}} )\\
\therefore\:pV&=\frac{2N}{3}KE_{particle}
\end{align*}$$

#### Finally giving

> ### $$ pV=\frac{2N}{3}KE_{particle} $$ 
>> where:
>> $p=$ Pressure excerted on walls
>> $V=$ Volume of container
>> $N=$ Number of gas particles
>> $KE_{particle}=$ KE of a single particle

^3c65ed

This equation isn't super useful but we can refine it into [[pressure, volume and temperatures relationship in an idea gas|something useful once we consider temperitures relation to particle KE]].