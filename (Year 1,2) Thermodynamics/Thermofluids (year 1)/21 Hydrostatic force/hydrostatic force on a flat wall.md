---
aliases: ["centre of force on a flat wall"]
tags: ["Question","QFormat3"]
---

#### How can you calculate
## Hydrostatic force on a flat wall

### Equation (taking $\rho,g,\theta,w$ as constants)
For versions of the equation that don't take these as constants, use the equations in [[hydrostatic force on a flat wall#Proof]] before integration.

Things are based of this image:
![[Pasted image 20220501061443.png]]
#### Centre pos

Assuming constant density, gravity, angle and width:
> ### $$ H_{CP} = \frac{2}{3} \frac{H_{B}^{3} - H_{T}^{3}}{H_{B}^{2} - H_{T}^{2} } $$
>> where: 
>> Vars from [[Pasted image 20220501061443.png|refrence image]]
>> $H_{CP}=$ position of centre of pressure
>> $H_T=$ position of top of surface
>> $H_B=$ position of bottom of surface 

Assuming the top of the surface reaches fluid level (and uses the assumptions above):

> ### $$ H_{CP} = \frac{2}{3} H_{B} $$
>> where: 
>> Vars from [[Pasted image 20220501061443.png|refrence image]]
>> $H_{CP}=$ position of centre of pressure
>> $H_T=0$ 
>> $H_B=$ position of bottom of surface 

#### Magnitude

Assuming constant density, gravity, angle and width:
> ### $$ F_{total} = \frac{\rho w g}{\sin\theta} \frac{ H_{B}^{2} - H_{T}^{2} }{2}$$ 
>> where: [[UNFINISHED STUFF]] check eq
>> Vars from [[Pasted image 20220501061443.png|refrence image]]
>> $F_{total}=$ total hydrostatic force acting on the surface (normal to it)
>> $g=$ gravity
>> $\rho=$ fluid density
>> $w=$ wall width
>> $H_{T}=$ height of top of area below surface
>> $H_{B}=$ height of bottom of area below surface
>> $\theta=$ angle of wall

### Proof
![[Pasted image 20220501061443.png]]
#### Force magnitude
$$\begin{align*}
dF &= p \cdot \frac{wdh}{\sin\theta} & p &= \rho gh\\
\int^{F_{all}}_{F_{above}} 1\cdot dF &= \int^{H_{B}}_{H_{T}} \frac{\rho w g}{\sin\theta} h \cdot dh \\
assume:\:&\theta,w,\rho,g\:are\;constant\\
F_{total} &= \frac{\rho w g}{\sin\theta} \frac{ H_{B}^{2} - H_{T}^{2} }{2}
\end{align*}$$

#### Centre of pressure
Modify the equation to calculate bending moments above and below some point $H_{CP}$:
$$\begin{align*}
0 &= \int^{H_{T}}_{H_{CP}} (H_{CP} - h) \frac{hwp}{\sin\theta} \cdot dh + \int^{H_{CP}}_{H_{B}} (H_{CP} - h) hwp \sin\theta \cdot dh\\
 &= \int^{H_{T}}_{H_{B}} (H_{CP} - h) \frac{hwp}{\sin\theta} \cdot dh\\
&=  \left[ \frac{H_{CP}h^{2}}{2} - \frac{h^{3}}{3} \right]^{H_{T}}_{H_{B}}  \frac{wp}{\sin\theta}\\
&= \frac{H_{CP}H_{T}^{2}}{2} - \frac{H_{CP}H_{B}^{2}}{2} - \frac{H_{T}^{3}}{3} + \frac{H_{B}^{3}}{3}\\
\frac{2}{3} \frac{H_{B}^{3} - H_{T}^{3}}{H_{B}^{2} - H_{T}^{2} } &= H_{CP}
\end{align*}$$