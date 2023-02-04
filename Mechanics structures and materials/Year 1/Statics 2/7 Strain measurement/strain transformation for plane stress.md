---
aliases: ["mohrs circle (strain)"]
tags: ["Question","QFormat3"]
---

#### What are the equations for
## Strain transformation for plane stress
### Strain transformation equations
So you know what we did for [[stress transformation for plane stress]], this is that, like 1:1, the derivation method is litterally the same so if you want the proof to these just look at [[stress transformation for plane stress#Proof]]:

![[Pasted image 20220307105608.png]]

> ### $$ \varepsilon_{x'x'} = \varepsilon_{yy} \sin^{2}\theta + \varepsilon_{xx} \cos^{2}\theta + 2\varepsilon_{xy}\sin\theta \cos\theta $$ 
> ### $$ \varepsilon_{x'x'} = \varepsilon_{yy} \sin^{2}\theta + \varepsilon_{xx} \cos^{2}\theta + \varepsilon_{xy} \sin2\theta $$ 
>> where:
>> $\varepsilon_{x'x'}=$ normal strain on slice 
>> $\theta=$ angle of slice
>> $\varepsilon=$ strains

^aaf81e


> ### $$ \varepsilon_{x'y'} = (\varepsilon_{yy} -\varepsilon_{xx})\cos\theta \sin\theta  + \varepsilon_{xy}(\cos^{2}\theta- \sin^{2}\theta ) $$ 
> ### $$ \varepsilon_{x'y'} = (\varepsilon_{yy} -\varepsilon_{xx}) \frac{\sin2\theta}{2}  + \varepsilon_{xy}(\cos^{2}\theta- \sin^{2}\theta ) $$ 
>> where:
>> $\varepsilon_{x'y'}=$ shear strain along slice 
>> $\theta=$ angle of slice
>> $\varepsilon=$ strains


### Mohrs circle
Since [[mohrs circle]] is derived from those equations it's kinda obvious but yeah, that is also exactly the same but with strain instead of stress.... 
