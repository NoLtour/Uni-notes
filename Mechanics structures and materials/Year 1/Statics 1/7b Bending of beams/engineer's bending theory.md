---
aliases: ["how the thing does stuff when the thing is applied over a thing (thats the technical term)"]
tags: ["Question","QFormat3"]
---

#### What is
## Engineer's bending theory
### The equation you care about

Also note that this equation is only true for pure bending (when shear force is zero), but it still acts as a resonably accurate approximation even when this isn't the case, so you can still use it when there is a shear force.

> ### $$ \frac{M}{I} = \frac{\sigma_{xx}}{y} = \frac{E}{R} $$
>  ### $$ \sigma_{xx} = \frac{My}{I} $$
>> where:
>> $M=$ anticlockwise moment about the [[neutral surface and neutral axis|neutral axis]]  
>> $I_{zz}=I=\int \int y^{2} \cdot dy\cdot dz=$ The resistance to bending due to the geometry of the beams cross section
>> $\sigma_{xx}=$ stress
>> $y=$ displacement from [[neutral surface and neutral axis|neutral axis]]
>> $E=$ [[modulus of elasticity]]
>> $R=$ Radius of circle

^6fb9ef

### Prooving this madness
We have made some progress in how stress/straing is applied on a material at different points using [[strains effects on cross section of a beam]], but this dosn't really work if we want to find stress over a given area:
![[Pasted image 20211108122435.png]]
So if any of that confused you, well you are about to [[experience pain|suffer]], god that embed is disgusting (click on it pussy).

#### Integration solves all problems
![[force over a section of beam cross section]]

![[moment over a section of beam cross section]]
