---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Min drag speed in steady level flight
Using the equations from [[calculating minimum drag]]:

> $$V_{MD} = \sqrt[4]\frac{B'}{A'}$$ 
>> where:
>> $V_{MD}=$  Minimum drag speed
>> $A'=$ constant
>> $B'=$ constant
>> (They are only constants in steady flight)

^ee6a75

Subbing in for A and B:

$$ \begin{align*}
V_{MD} &= \sqrt[4]{  \frac{ \frac{2 K}{ \pi A} \cdot \frac{ W^{2}}{ \rho S } }{ \frac{1}{2}\rho S C_{Do} }   }\\
&= \sqrt[4]{ \frac{4 K}{ \pi A} \cdot \frac{ { W^{2}} }{ \rho^{2} S^{2} C_{Do} }   }\\
&= \sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{ \frac{4 K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   }
\end{align*} $$

> $$ V_{MD} = \sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{ \frac{4 K}{ \pi A} \cdot \frac{ 1 }{ C_{Do} }   }= \sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{  \frac{ 4k }{ C_{Do} }   } $$

^c26ec7

(Not 100% if this equation is right since I made it)

Intrestingly it shows your minimum drag speed decreases at higher density, hence the speed at min drag increases with altitude.

