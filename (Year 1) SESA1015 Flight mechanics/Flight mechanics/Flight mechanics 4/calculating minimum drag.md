---
aliases: ["minimum drag"]
tags: ["Question","QFormat3"]
---

#### How would you go about
## Calculating minimum drag
### Conditions
We can work under the same assumptions from [[steady flight and true airspeed#Conditions]].

### Calculations
We know that drag can be found using:
![[Drag equation#^33fc8d]]

Subbing in for $C_D$ with:
[[drag coefficient#^e6ae2f]]

Then subbing in $C_{Di}$ with:
[[induced drag coefficient#^4d0b00]]
[[induced drag coefficient#^438b96]]

$C_{Di} = \dfrac{K}{\pi A} C_L^{2}$

We get:
$$\begin{align*}
D =& \frac{1}{2}\rho V^{2}S (C_{Do} + C_{Di})\\
=& \frac{1}{2}\rho V^{2}S (C_{Do} + \dfrac{K}{\pi A} C_L^{2})
\end{align*} $$

Then using [[lift equation#^{1f2714]] rearranged to: $\dfrac{2L}{\rho V^{2}S} =  C_L$

$$ \begin{align*}
D =& \frac{1}{2}\rho V^{2}S (C_{Do} + \dfrac{K}{\pi A} \cdot (\dfrac{2L}{\rho V^{2}S})^{2})\\
=&  \frac{1}{2}\rho V^{2}S C_{Do} + \frac{1}{2}\rho V^{2}S \dfrac{K}{\pi A} \cdot \dfrac{4L^{2}}{\rho^{2} V^{4}S^{2}}\\
=& \frac{1}{2}\rho V^{2}S C_{Do} + \frac{\rho V^{2} S K 4L^{2}}{2 \pi A \rho^{2} V^{4}S^{2}} & W&=L\\
=& \frac{1}{2}\rho V^{2}S C_{Do} + \frac{2 K W^{2}}{ \rho \pi A V^{2}S }\\
=& \frac{1}{2}\rho V^{2}S C_{Do} + \frac{2 K}{ \pi A} \cdot \frac{ W^{2}}{ \rho S V^{2} }
\end{align*} $$



#### Final equation for drag

Hence focusing on speed:

> $$ D = A'V^{2} + \frac{B'}{V^{2}} $$ 
>> where:
>> $D=$ Drag 
>> $V=$ [[True airspeed]]
>> $A'=$ A constant $=\frac{1}{2}\rho S C_{Do}$
>> $B'=$ A constant $=\frac{2 K}{ \pi A} \cdot \frac{ W^{2}}{ \rho S }$
>> (They are only constants in steady flight)

^fb4ad2

### Implications
![[Pasted image 20211101214128.png]]
This equation $D = A'V^{2} + \frac{B'}{V^{2}}$ implies that there are 2 possible speeds for any given drag/thrust, this is true to an extent but in reality many of the slower speeds become impossible when [[stalling speed]] is considered.

It should also be noted that min drag occurs when [[profile drag coefficient|profile drag]] = [[induced drag coefficient|induced drag]].

#### Calculating minimum drag
Finally, now just use [[MEE Differentiation 1|Differentiation]]:

$$ \begin{align*}
\frac{dD}{dV} &= 2A'V - 2\frac{B'}{V^{3}}\\
& & let\: \frac{dD}{dV} &= 0\\
0 &=2A'V - 2\frac{B'}{V^{3}}\\
2\frac{B'}{V^{3}} &= 2A'V\\
\frac{B'}{A'}&=V^{4}\\
\sqrt[4]\frac{B'}{A'}&=V
\end{align*} $$

### Min drag equations
![[min drag speed in steady level flight]]

![[min drag lift coefficient in steady level flight]]

![[min drag in steady level flight]]

![[max lift to drag ratio]]

![[minimum power speed]]

