---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Tersca yield criterion
### Equation

> ### $$ \sigma_{max\:x'y'} = \frac{1}{2} \max( |\sigma_{I} - \sigma_{II}|, |\sigma_{I}-\sigma_{III}|, |\sigma_{II} - \sigma_{III}| ) $$ 
>> where:
>> $\sigma_{max\:x'y'}=$ The maximum shear stress in 3D
>> $\sigma_{I},\sigma_{II},\sigma_{III}=$ are [[points of intrest on mohrs circle|principal stresses]] in $x',y',z'$

If we assume a state of plane stress (where $\sigma_{III}= 0$) it can be written more simply as:

> ### $$ \sigma_{max\:x'y'} = \frac{1}{2} \max( |\sigma_{I} - \sigma_{II}|, |\sigma_{I}|, |\sigma_{II} - \sigma_{III}| ) $$ 
>> where:
>> $\sigma_{max\:x'y'}=$ The maximum shear stress in 3D
>> $\sigma_{I},\sigma_{II}=$ are [[points of intrest on mohrs circle|principal stresses]] in $x',y',z'$


### Theory
So you know how in [[ductile material failure appearance|ductile failure]] you get a sheared cup cone failure, well basically this lad:
![[Pasted image 20220318132137.png]]
Had the idea that what actually causes fracture is maximum shear. So going back to [[mohrs circle]] we can find maximum shear and when that reaches a maximum fracture should occur:
![[points of intrest on mohrs circle#^765894]]

But to apply this in 3D we will need to apply [[mohrs circle]] to the other 2 planes as well to get $\sigma_{III}$, $\sigma_{II}$ and $\sigma_{I}$:
![[Pasted image 20220318132611.png]]
Then we can use the same equation linked above to get max shear in each of those directions and then the maximum of all of those will be the absolute max shear:
$$ \sigma_{max\:x'y'} = \frac{1}{2} \max( |\sigma_{I} - \sigma_{II}|, |\sigma_{I}-\sigma_{III}|, |\sigma_{II} - \sigma_{III}| ) $$
If you are confused where $\sigma_{III}$ comes from note that $\sigma_{I}$ is just the max stress in $x'$ then $\sigma_{II}$ is just the max stress in $y'$ so $\sigma_{n}$ is just a way of expressing max force in some axis (after [[strain transformation for plane stress|strain transformation]]) so $\sigma_{III}$ is max stress in $z'$.