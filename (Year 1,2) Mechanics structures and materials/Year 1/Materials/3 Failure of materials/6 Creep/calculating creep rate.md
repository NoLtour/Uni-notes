---
aliases: ["creep rate"]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Calculating [[creep (materials)|creep]] rate ($\dot{\epsilon}$)
We know creep is a diffusion based mechanism so we can use [[temperatures effect on diffusion|diffusion equations to model it]]

![[Pasted image 20211203154515.png]]

> ### $$ \dot{\epsilon} = K_2 \sigma^{n} (exp)^{-\frac{Q_c}{R_u T}} $$ 
>> where:
>> $\dot{\epsilon}= \frac{d\epsilon}{dt}=$ [[calculating creep rate|creep rate]] 
>> $Q_c=$ activation energy for creep
>> $T=$ temperature
>> $n=$ the stress exponent, it is dependent on the mechanism
>> $K_2=$ a material constant
>> $R_u=$ [[universal gas constant]] (I think)

##### [[holy shit I'm stupid|Determining]] $n$

$n$ is basically determined by the type of diffusion eg:
- Stress-induced vacancy diffusion
-  Grain boundary diffusion
-  dislocation motion
-  grain boundary sliding 

It also includes any mechanisms that include bulk diffusion of atoms to relieve stresses, Diffusion to assist Dn. Motion and g.b. diffusion allowing g.b. sliding

Also there is a meme hidden in this page, see if you can find it.