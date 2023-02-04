---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How can we calculate
## Stresses in a cylindrical pressure vessel
### Equations
#### $\sigma_{yy}$
![[Pasted image 20220206130233.png]]

> ### $$ \sigma_{yy}= \frac{pR}{t} $$ 
>> where:
>> $\sigma_{yy}=$ stress 
>> $p=$ pressure
>> $R=$ Radius of vessel
>> $t=$ vessel wall thickness
>> $\frac{t}{R}\leq 0.1$

#### $\sigma_{xx}$
![[Pasted image 20220206130831.png]]

> ### $$ \sigma_{xx} = \frac{p R}{2 t} $$ 
>> where:
>> $\sigma_{xx}=$ stress 
>> $p=$ pressure
>> $R=$ Radius of vessel
>> $t=$ vessel wall thickness
>> $\frac{t}{R}\leq 0.1$

### Proof
For these we will be using [[thin walled pressure vessel assumptions]].

#### $\sigma_{yy}$

First we split the cylinder into two halfs:

![[Pasted image 20220206130233.png]]

For equilibrium we know that: $pA_{outside}=\sigma_{yy}A_{inside}$:
$$\begin{align*}
pA_{outside}&=\sigma_{yy}A_{inside}\\
p(2RL) &= \sigma_{yy} (2tL)\\
\frac{p2RL}{2tL} &= \sigma_{yy}\\
\sigma_{yy}&= \frac{pR}{t}
\end{align*}$$


#### $\sigma_{xx}$
![[Pasted image 20220206130831.png]]

$$\begin{align*}
p(\pi R^{2}) &= \sigma_{xx}(2\pi Rt)\\
\frac{p\pi R^{2}}{2 \pi Rt}&=\sigma_{xx}\\
\sigma_{xx} &= \frac{p R}{2 t} 
\end{align*}$$

^b3611c
