---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Von mises yield criterion
### Intro
It is the more ((((([[the other one is bad|based]]))))) version of the bitch ass [[Tersca yield criterion]]. That being the official technical language that is used when comparing the two approaches to finding yield stress.

Note that the [[Tersca yield criterion#^3eb6a8|same restriction applies]].

Read [[#Theory]] before [[#Useful bit]].
### Useful bit
#### Equation
For general use in 3D:

> ### $$ \sigma_{RMS\:x'y'} = \frac{1}{2\sqrt{3}} \sqrt{ (\sigma_{I}-\sigma_{II})^{2} + (\sigma_{I}-\sigma_{III})^{2} + (\sigma_{II}-\sigma_{III})^{2} } $$ 
>> where:
>> $\sigma_{RMS\:x'y'}=$ The maximum shear stress
>> $\sigma_{I},\sigma_{II},\sigma_{III}=$ are [[points of intrest on mohrs circle|principal stresses]] in $x',y',z'$

For plane stress it can be simplified to:

> ### $$ \sigma_{max\:x'y'} = \sqrt{ \sigma_{I}^{2} + \sigma_{II}^{2} - \sigma_{I}\sigma_{II} } $$
> ### $$ \sigma_{max\:x'y'} = \sqrt{ \sigma_{xx}^{2} + \sigma_{yy}^{2} + 3\sigma_{xy}^{2} - \sigma_{xx}\sigma_{yy} } $$ 
>> where:
>> $\sigma_{RMS\:x'y'}=$ The maximum shear stress
>> $\sigma_{I},\sigma_{II} =$ are [[points of intrest on mohrs circle|principal stresses]] in $x',y'$

#### Graph (plane loading)
Plotted we can compare it to [[Tersca yield criterion#Graph uniaxle loading]] and see that this one is basically just an ellipse intersepting the corners of the other:
![[Pasted image 20220318140822.png]]
In experiments this theory also tends to be more accurate, though it is less conservative.

### Theory
That guy:
![[Pasted image 20220318135000.png]]
Predics that yielding is determined by the absolute maximum shear stress. Basically a root mean square approach:
$$ \sigma_{RMS\:x'y'} = \sqrt{ \frac{\left(\frac{\sigma_{I}-\sigma_{II}}{2}\right)^{2} + \left(\frac{\sigma_{I}-\sigma_{III}}{2}\right)^{2} + \left(\frac{\sigma_{II}-\sigma_{III}}{2}\right)^{2} }{3} } $$