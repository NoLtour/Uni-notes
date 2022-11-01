---
aliases: [""]
tags: []
---

## Local wall shear stress ($\tau_{w}$)

This is simply the shear stress at the wall between the fluid and the solid.

![[Pasted image 20221029202527.png]]

It can be integrated to get [[skin drag]]:

> ## $$ D' = \int^{x}_{0} \tau_{w} dx $$ 
> ## $$ \tau_{w} = \frac{dD'}{dx} $$
> ## $$ \tau_{w} = \mu \left. \frac{du}{dy} \right|_{y=0} $$
>> where:
>> $D'(x)=$ total [[skin drag|viscous drag]] caused up to that point as a function of $x$ 
>> $x=$ position on object 
>> $\tau_{w}=$ [[local wall shear stress]]
>> $\mu=$ [[viscosity]]
>> $y=$ normal distance from surface
>> $u=$ tangential velocity of fluid to surface
>> This is in 2D

^803cc0

