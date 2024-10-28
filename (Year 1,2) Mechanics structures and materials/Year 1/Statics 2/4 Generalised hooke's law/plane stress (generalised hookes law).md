---
aliases: ["plane stress","plane strain","plane stress equations","plane stain equations"]
tags: ["Question","QFormat3"]
---

#### Describe
## Plane stress (generalised hookes law)
So in the past we discussed [[poisson's ratio]] and we have been mostly solving problems with loads in one diection, but when working in 3D or even 2D there are often stresses and strains being externally applied in multiple directions, so the [[poisson's ratio]] needs to be used to calculate how all these different stresses interact and overlap. So it is important to keep in mind that these equations need to be used instead of there simpler older counterparts when considering multi directional strain situations!

![[Pasted image 20220220111356.png]]

In a situation of plane stress we assume $\sigma_{zz}=0$ but that does not mean that $\varepsilon_{zz}=0$, such a state is known as [[plane stress (generalised hookes law)|plane stress]] using this we can derive the following formula for strains:

### Strain equations

#### Axial Strain

> ### $$ \varepsilon_{xx} = \frac{1}{E} (\sigma_{xx} - \nu \sigma_{yy} ) $$ 
> ### $$ \varepsilon_{yy} = \frac{1}{E} (\sigma_{yy} - \nu \sigma_{xx} ) $$ 
> ### $$ \varepsilon_{zz} = -\frac{\nu}{E} (\sigma_{xx} + \sigma_{yy} ) $$ 
>> where:
>> $E=$ [[Youngs modulus]]
>> $\varepsilon=$ strain in some axis
>> $\sigma_{xx}=$ stress in xx
>> $\sigma_{yy}=$ stress in yy
>> $\sigma_{zz}=0=$ stress in zz
>> $\nu=$ [[poisson's ratio]]

#### [[local shear strain|shear strain]]

![[Pasted image 20220220112430.png]]

> ### $$ \varepsilon_{xy} = \frac{1+\nu}{E} (\sigma_{xy}) $$ 
>> where:
>> $E=$ [[Youngs modulus]]
>> $\varepsilon_{xy}=$ shear strain in xy
>> $\sigma_{xx}=$ shear stress in xy
>> $\nu=$ [[poisson's ratio]]

### Stress equations
With lots of subbing in and rearranging you can get the following stress equations from the strain ones:

#### Axial Stress

> ### $$ \sigma_{xx} = \frac{E}{1-\nu^{2}} ( \varepsilon_{xx} + \nu \varepsilon_{yy} ) $$ 
> ### $$ \sigma_{yy} = \frac{E}{1-\nu^{2}} ( \varepsilon_{yy} + \nu \varepsilon_{xx} ) $$ 
> ### $$ \sigma_{zz} = 0 $$
>> where:
>> $\sigma=$ stress in some axis
>> $E=$ [[Youngs modulus]]
>> $\nu=$ [[poisson's ratio]]
>> $\varepsilon_{xx}=$ strain in x
>> $\varepsilon_{yy}=$ strain in y
>> $\sigma_{zz}=0$  (because that is [[I am concerned if you didn't realise that|literally the point]] of this page, have you not been paying attention?)

#### Shear stress

> ### $$ \sigma_{xy} = \frac{E}{1+\nu} \varepsilon_{xy} $$ 
>> where:
>> $\sigma_{xy}=$ shear stress in xy
>> $E=$ [[Youngs modulus]]
>> $\nu=$ [[poisson's ratio]]
>> $\varepsilon_{xy}=$ shear strain in xy