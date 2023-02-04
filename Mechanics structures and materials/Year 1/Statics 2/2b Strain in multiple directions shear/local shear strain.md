---
aliases: ["shear strain"]
tags: ["Question","QFormat3"]
---

#### What is
## Local shear strain
### Useful bit
![[Pasted image 20220213104635.png]]

> ### $$ \gamma_{xy} = \alpha + \beta = \frac{du_{x}}{dy} + \frac{du_{y}}{dx} $$ 
>> where:
>> $\gamma_{xy}=$ [[shear strain]] 
>> $\alpha,\beta$ are small

Negative [[shear strain]] corresponds to an increase in the angle between x+ and y+ while a positive corresponds to a decrease.

It is _important_ to note that $\varepsilon_{xy}\neq \gamma_{xy}$ and is instead defined in the following:

![[Pasted image 20220213105822.png]]

> ### $$ \varepsilon_{xy} = \frac{1}{2} \gamma{xy} = \frac{1}{2}\left(\frac{du_{x}}{dy} + \frac{du_{y}}{dx}\right) $$ 
>> where:
>> $\varepsilon_{xy}=$ angular deformation of each face symmetric with respect to the diagonal 
>> $\gamma_{xy}=$ [[shear strain]] 

### Explenation
Basically the same as [[local strain]] but considering [[shear strain]] instead:
![[Pasted image 20220213104133.png]]

We can generate the following equation for finding the gradient for the case above:
$$ \frac{du_{x}}{dy} = \frac{u_{x\:top}-u_{x\:bottom}}{dy} $$

Now if we consider what this looks like for a small material element with initial dimensions $dx$ and $dy$, where the object is free to rotate:

![[Pasted image 20220213104635.png]]

Which if we take small angle approximations becomes:

$$ \gamma_{xy} = \alpha + \beta = \frac{du_{x}}{dy} + \frac{du_{y}}{dx} $$

It should be noted that shear strain is essentially a measure of the change in angle between the x and y sides from 90 degrees, so sign matters:

![[Pasted image 20220213105020.png]]

While:
![[Pasted image 20220213105130.png]]