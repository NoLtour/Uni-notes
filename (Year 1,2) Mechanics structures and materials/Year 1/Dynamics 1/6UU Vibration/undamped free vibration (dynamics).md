---
aliases: ["natural frequency"]
tags: ["Question","QFormat3"]
---

#### What is
## Undamped free vibration (dynamics)
### Important bits
Also defined [[free vibrations|here]]. This is a special case of oscillation in dynamics where the sum of kinetic energy and elastic energy is conserverd. 

> ### $$ x=A\cos \left(t\sqrt{\frac{k}{m}}\right) + B\sin \left(t\sqrt{\frac{k}{m}}\right) $$ 
>> where:
>> $x=$ displacement
>> $t=$ time
>> $A,B=$ constants that need to be found
>> $k=$ [[spring constant]] 
>> $m=$ mass of particle

To find the values of A and B you need to be given some combination of initial conditions like time, velocity, displacement ect.

#### Natural frequency (undamped)

The natural frequency is equivilent to:
> ### $$ \omega = \sqrt{\frac{k}{m}} $$
> ### $$ f = \frac{1}{2\pi} \sqrt{\frac{k}{m}} $$ 
>> where:
>> $\omega=$ natural frequency (rad)
>> $f=$ natural frequency (Hz)
>> $k=$ [[spring constant]]
>> $m=$ mass of thing

### Maths
So basically if we take this eqaution:
![[modeling vibration (not driven)#^9328aa]]

Then set $c=0$ we get $0=m \frac{d^{2}x}{dt^{2}}+ kx$, then if we apply [[solving linear homogeneous constant-coefficient equations]]:

$$\begin{align*}
s^{2}m + k &= 0\\
s &= \sqrt\frac{-k}{m} \\
&= i\sqrt{\frac{k}{m}}
\end{align*}$$

Since we got a [[complex numbers|complex number]] we use the form $x=e^{at} (A\cos bt + B\sin bt)$ where $a=0$ and $b=\sqrt{\frac{k}{m}}$ getting:
$$\begin{align*}
x=A\cos \left(t\sqrt{\frac{k}{m}}\right) + B\sin \left(t\sqrt{\frac{k}{m}}\right)
\end{align*}$$