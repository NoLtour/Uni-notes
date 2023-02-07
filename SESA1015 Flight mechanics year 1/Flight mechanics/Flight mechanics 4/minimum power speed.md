---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Minimum power speed
Power is the rate of doing work, we know that $P=Fv$ so applieing that to drag knowing that drag = thrust:

![[calculating minimum drag#^fb4ad2]]

$$ \begin{align*}
P &= DV \\
&= ( A'V^{2} + \frac{B'}{V^{2}} )V\\
&= A'V^{3} + \frac{B'}{V}\\
\frac{dP}{dV} &= 3A'V^{2} - \frac{B'}{V^2}\\
& & \frac{dP}{dV} &= 0\\
0&=3A'V^{2} - \frac{B'}{V^2}\\
\frac{B'}{V^2}&=3A'V^{2} \\
\frac{B'}{3A'}&=V^{4}\\
V&=\sqrt[4]\frac{B'}{3A'}
\end{align*} $$

If we refer to [[min drag speed in steady level flight]]:

$$ \begin{align*}
V_{MP} &=\sqrt[4]\frac{B'}{A'} \cdot \sqrt[4] \frac{1}{3}\\
V_{MP} &= V_{MD} \cdot \sqrt[4] \frac{1}{3} \approx V_{MD} \cdot 0.76
\end{align*} $$

So:
> $$ V_{MP} = V_{MD} \cdot \sqrt[4] \frac{1}{3} \approx V_{MD} \cdot 0.76 \:\:\:or\:\:\:V_{MP} = \sqrt{ \frac{W}{\rho S} } \cdot \sqrt[4]{  \frac{ 4k }{ C_{Do} }   } \cdot \sqrt[4] \frac{1}{3} $$ 
>> where:
>> $V_{MP}=$ Speed at minimum power
>> $V_{MD}=$ [[min drag speed in steady level flight]]

^6d5ee2

Hence the min power speed is less than the min drag speed.

### Relationships at min power speed
![[Pasted image 20220511185433.png]]
At the minimum power speed all the following are true:

#### Induced drag and form drag

This relationship is proved [[relating induced drag and form drag at minimum power speed]]

> ### $$ C_{Di} = k C_L^{2} = 3 C_{Do} \:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\:\: C_D = 4 C_{Do} = \frac{4}{3}C_{Di} $$ 
>> where:
>> $C_{Do}=$ [[form drag coefficient]]
>> $k=$ [[induced drag coefficient#^438b96|constant related to wing shape]]
>> $C_L=$ [[lift coefficient]]

^0cb1a3

#### Coefficient of lift

This relationship is proved [[relating induced drag and form drag at minimum power speed#^dfc8e1]]

> ### $$ C_L = \frac{ \sqrt{ 3 C_{Do} }}{ \sqrt{ k }   } $$ 
>> where:
>> $=$ 
>> $=$
>> $=$

#### Lift to drag ratio

This relationship is proved [[lift to drag ratio at minimum power speed]]

> ### $$ \frac{L}{D}_{minP} = \frac{C_L}{4C_{Do}} = \frac{3}{4kC_L  } = \frac{1}{4} \sqrt\frac{3}{k C_{Do}  } $$ 
>> where:
>> $\frac{L}{D}_{minP}=$ [[lift to drag ratio]] at min power
>> $C_{Do}=$ [[form drag coefficient]]
>> $k=$ [[induced drag coefficient#^438b96|constant related to wing shape]]
>> $C_L=$ [[lift coefficient]]
