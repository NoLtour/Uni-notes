---
aliases: [""]
tags: ["Question","QFormat3","SESA1015"]
---

#### What is the
## Aerodynamic centre
### General definition
This is defined as the reference axis position about which the pitching moment coefficient does not  vary with angle of attack. In maths terms:
$$ \frac{dM_{AC}}{d\alpha}=0 $$
In other terms:
The Aerodynamic center is the point at which the pitching moment coefficient for the airfoil does not vary with lift coefficient (i.e. angle of attack), making analysis simpler.

The lift and drag forces can be applied at a single point (the [[centre of pressure]]), about which they exert zero torque, but this is impractical for analysis as the [[centre of pressure]]'s location varies greatly with angle of attack. So this is why the aerodynamic centre is used.

If we refer to [[measuring pitching moments on a plane]], keeping that in mind a graphical representation of the aerodynamic centre is shown below:
![[Pasted image 20211025212324.png]]

### Maths
![[Pasted image 20211021205317.png]]
Taking moments about the centre of gravity:
$$ M_{CG} = M_0 + x_{AC}L $$

Then if we divide by $\frac{1}{2}\rho V^{2}Sc$ and use $C_m = C_{mo}-hC_L$ (from [[Effect of angle of attack on the moment coefficient#^cfc8b1]]):

> $$ C_{M_{CG}} = C_{M_0} \dfrac{x_{AC}}{c}C_L = C_{m_0} - hC_L $$ 
>> where:
>> $C_{M_{CG}} =$  moment coefficient around the centre of gravity
>> $x_{AC} =$ distance between aerodynamic centre and centre of gravity
>> $C_{m_0} =$ ?!?
>> $c =$ [[Mean chord|Mean aerodynamic chord]]
>> $C_L =$ [[lift coefficient]]
>> $h =$ a constant

hence:
> $$ \frac{x_{AC}}{c}= \frac{dC_{M_{CG}}}{dC_L}=-h $$ 

Since $h$ is a constant this proves aerodynamic centre is at a fixed position,
