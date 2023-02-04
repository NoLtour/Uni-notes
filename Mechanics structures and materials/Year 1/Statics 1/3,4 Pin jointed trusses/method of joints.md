---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Method of joints

1) First you consider the truss as a single body and calculate what [[External forces]] are needed to keep it in eqaulibrium
2) You consider the horizontal and verticle force equalibrium at each joint in the [[pin jointed truss model]], and figure out the forces acting on the surrounding bars which produces this resault. Generally it is easyer to start by analysing pins with as few unknowns as possible.
3) Pog your done m8

### Example
Find the tensions in $\vec{BC}$, $\vec{AB}$ and $\vec{AC}$.

![[Pasted image 20211022212948.png]]

1) Calculate missing reactions
> Horizontal equilibrium:
>> $$ H_A + H_B = 0 $$
>
> Vertical equilibrium:
>> $$ V_B + 200 = 0 $$
>> $$ V_B = -200 $$
>
> Moments equilibrium (about B):
>> $$ \begin{align*}
5H_A &= 10*200\\
H_A &= 400
\end{align*} $$
>
> Using all the equations together:
>> $$\begin{align*}
H_A &= -H_B\\
H_B &= -400
\end{align*}$$

2) Work out forces at each joint
> ![[Pasted image 20211022214031.png]]
> $\theta = 26.565\degree$
> Using the same ideas of horizontal and vertical equalibrium:
>> $$ \begin{align*}
F_{BC} \cos(\theta) + F_{AC} &= 0\\\\
200 + F_{BC}\sin(\theta) &= 0\\
F_{BC} &= \frac{-200}{\sin(\theta)} \\&= -447.213\\\\
F_{AC}&= - F_{BC} \cos(\theta) \\&= 400
\end{align*} $$
>
> Now you compute B and find that $\vec{BA}=0$ (cba rn)

Finally you have:
![[Pasted image 20211022214705.png]]