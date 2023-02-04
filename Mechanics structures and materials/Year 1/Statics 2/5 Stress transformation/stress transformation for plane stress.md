---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe
## Stress transformation for plane stress
### Equation
![[Pasted image 20220221135947.png]]

> ### $$ \sigma_{x'x'} = \sigma_{yy} \sin^{2}\theta + \sigma_{xx} \cos^{2}\theta + 2\sigma_{xy}\sin\theta \cos\theta $$ 
> ### $$ \sigma_{x'x'} = \sigma_{yy} \sin^{2}\theta + \sigma_{xx} \cos^{2}\theta + \sigma_{xy} \sin2\theta $$ 
>> where:
>> $\sigma_{x'x'}=$ normal stress on slice 
>> $\theta=$ angle of slice
>> $\sigma=$ stresses

^52d731

> ### $$ \sigma_{x'y'} = (\sigma_{yy} -\sigma_{xx})\cos\theta \sin\theta  + \sigma_{xy}(\cos^{2}\theta- \sin^{2}\theta ) $$ 
> ### $$ \sigma_{x'y'} = (\sigma_{yy} -\sigma_{xx}) \frac{\sin2\theta}{2}  + \sigma_{xy}(\cos^{2}\theta- \sin^{2}\theta ) $$ 
>> where:
>> $\sigma_{x'y'}=$ shear stress along slice 
>> $\theta=$ angle of slice
>> $\sigma=$ stresses

^b65568

#### Implications

Note much of [[stress transformation for uniaxle loading#Implications]] applies here, basically this is that but worse since it's likely some of the orientations will actually have higher normal stress values than any of the input values... so fun.

### Proof
Basically the same as [[stress transformation for uniaxle loading#Proof]] but now in 2D. (so [[something something skill issue|harder]])

Since we have multiple forces acting in each axis we need to account for all their components effect on forces acting on rotated planes:
![[Pasted image 20220221134050.png]]

But we can change our diagram to represent an equivalent pressure in a way that's less overwhelming:
![[Pasted image 20220221134202.png]]

As before we can use pressure times area to get force and then equilibrium conditions to get equations defining the stress on/along the plane we are intrested in:
$$\begin{align*}
A_{y} &= A & A_{x} &= A\tan\theta & A_{H} &= \frac{A}{\cos\theta} 
\end{align*}$$
For cancelling terms later it will be convenient to define the area of the faces interms of a single area $A$, now to get our force equilibrium equations along the normal/tangent of the cut face and solve:
$$\begin{align*}
\sigma_{x'x'} A_{H} &= A_{y}( \sigma_{xx} \cos\theta + \sigma_{xy}\sin\theta ) + A_{x}( \sigma_{yy} \sin\theta + \sigma_{xy} \cos\theta ) &
\sigma_{x'y'} A_{H} &= A_{y}( \sigma_{xx} \sin\theta + \sigma_{xy}\cos\theta ) + A_{x}( \sigma_{yy} \cos\theta + \sigma_{xy} \sin\theta ) \\

\sigma_{x'x'} \frac{A}{\cos\theta} &= A( \sigma_{xx} \cos\theta + \sigma_{xy}\sin\theta ) + A\tan\theta( \sigma_{yy} \sin\theta + \sigma_{xy} \cos\theta ) &
\sigma_{x'y'} \frac{A}{\cos\theta} &= A( - \sigma_{xx} \sin\theta + \sigma_{xy}\cos\theta ) + A\tan\theta( \sigma_{yy} \cos\theta - \sigma_{xy} \sin\theta ) \\

\sigma_{x'x'} \frac{1}{\cos\theta} &=  \sigma_{xx} \cos\theta + \sigma_{xy}\sin\theta  + \tan\theta( \sigma_{yy} \sin\theta + \sigma_{xy} \cos\theta ) &
\sigma_{x'y'} \frac{1}{\cos\theta} &= -\sigma_{xx} \sin\theta + \sigma_{xy}\cos\theta  + \tan\theta( \sigma_{yy} \cos\theta - \sigma_{xy} \sin\theta ) \\

\sigma_{x'x'} &=  \sigma_{xx} \cos^{2}\theta + \sigma_{xy}\sin\theta \cos\theta  + \sigma_{yy} \sin^{2}\theta + \sigma_{xy} \cos\theta \sin\theta &
\sigma_{x'y'} &= -\sigma_{xx} \cos\theta \sin\theta + \sigma_{xy}\cos^{2}\theta  + \sigma_{yy} \sin\theta \cos\theta - \sigma_{xy} \sin^{2}\theta  \\

 &=  \sigma_{yy} \sin^{2}\theta + \sigma_{xx} \cos^{2}\theta + 2\sigma_{xy}\sin\theta \cos\theta  &
 &= (\sigma_{yy} -\sigma_{xx})\cos\theta \sin\theta  + \sigma_{xy}(\cos^{2}\theta- \sin^{2}\theta )    \\

\end{align*}$$