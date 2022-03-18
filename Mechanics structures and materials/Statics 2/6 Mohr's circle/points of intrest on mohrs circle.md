---
aliases: ["principal stress","principal stresses"]
tags: ["Question","QFormat3"]
---

#### What are the
## Points of intrest on mohrs circle

It's quite intuitive to see where the maximums occur on [[mohrs circle]], but some of these points have names and we can also get neat expressions for them:

![[Pasted image 20220301230818.png]]

The points where the circle intercept the stress axis are known as the [[points of intrest on mohrs circle|principal stresses]] where $\sigma_{I}$ is the max normal stress and $\sigma_{II}$ is the min normal stress. It should be noted that depending on the position of average stress (centre of circle) that the min normal stress and max stress can be negative or positive indicating compression and tension.

These stresses can be expressed mathamatically using:
> ### $$ \sigma_{I} = \sigma_{average} + R $$
> ### $$ \sigma_{II} = \sigma_{average} - R $$ 
>> where:
>> $R=\sqrt{\left(\frac{\sigma_{xx}-\sigma_{yy}}{2}\right)^{2} + \sigma_{xy}^{2}}$ 
>> $\sigma_{average}= \frac{\sigma_{xx} + \sigma_{yy}}{2}$
>> $\sigma_{I}=$  max normal stress
>> $\sigma_{II}=$  min normal stress
>> (further variable elaboration can be found in [[mohrs circle#^1da227]])

You can also see that the max shear stress occurs at:
> ### $$ \sigma_{x`y`\:max} = \pm \frac{\sigma_{I}-\sigma_{II}}{2} = \pm R  $$ 
>> where:
>> $\sigma_{x`y`\:max}=$ max shear stresses ($\pm$)
>> $\sigma_{I},\sigma_{II}=$ [[points of intrest on mohrs circle|principal stresses]]
>> $R=\sqrt{\left(\frac{\sigma_{xx}-\sigma_{yy}}{2}\right)^{2} + \sigma_{xy}^{2}}$ 
>> (further variable elaboration can be found in [[mohrs circle#^1da227]])

^765894
