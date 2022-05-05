---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the method for
## Measuring shear strain
### Useful bits
So we know that the [[practical real world method for measuring strain]] of using a [[strain guage]] can only measure compression/tension but not torsion. So we use multiple [[strain guage|strain guages]] at different angles and then slap that with some rearranged form of the [[strain transformation for plane stress#^aaf81e]] equation and can calculate torsion.

Looks like we are supposed to derive this manually for each [[strain guage rosette]] configuration, but that's dumb when a general form is possible:

![[Pasted image 20220307113750.png]]

> ### $$ \varepsilon_{yy} = \frac{ (\varepsilon_{B} - \varepsilon_{xx}\cos^{2}\theta)\sin 2\alpha - (\varepsilon_{C} - \varepsilon_{xx}\cos^{2}\alpha) \sin 2\theta }{ \sin^{2}\theta \sin 2\alpha - \sin^{2}\alpha \sin 2\theta } $$ 
> ### $$ \varepsilon_{yy} = \frac{\varepsilon_{B} - \varepsilon_{xx} \cos^{2}\theta - \varepsilon_{xy} \sin 2\theta}{\sin^{2}\theta}  = \frac{\varepsilon_{C} - \varepsilon_{xx} \cos^{2}\alpha - \varepsilon_{xy} \sin 2\alpha}{\sin^{2}\alpha} $$
> ### $$ \varepsilon_{xy} = \frac{ ( \varepsilon_{B} - \varepsilon_{xx} \cos^{2}\theta ) \sin^{2}\alpha - ( \varepsilon_{C} - \varepsilon_{xx} \cos^{2}\alpha )\sin^{2}\theta }{ \sin^{2}\alpha \sin 2\theta  - \sin^{2} \theta \sin 2\alpha  } $$
> ### $$ \varepsilon_{xy}  = \frac{\varepsilon_{B} - \varepsilon_{xx} \cos^{2}\theta  -\varepsilon_{yy} \sin^{2}\theta}{\sin 2\theta} = \frac{\varepsilon_{C} - \varepsilon_{xx} \cos^{2}\alpha-\varepsilon_{yy} \sin^{2}\alpha  }{\sin 2\alpha} $$
>> where:
>> $\varepsilon_{xx}=$ strain in $xx$
>> $\varepsilon_{yy}=$ strain in $yy$
>> $\varepsilon_{xy}=$ shear strain in $xy$
>> $\varepsilon_{B},\varepsilon_{C}=$ some strain 
>> $\theta=$ anticlockwise angle between $\varepsilon_{B}$ and $\varepsilon_{xx}$
>> $\alpha=$ anticlockwise angle between $\varepsilon_{C}$ and $\varepsilon_{xx}$  

#### Specific

### Equation proof
Ok I'm not doing this in latex fuck that, so you get to see it in one note (less clean but like so much effort to latex it):
![[Pasted image 20220307110728.png]]

![[Pasted image 20220307110800.png]]