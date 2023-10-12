---
aliases: ["cross product","perpendicular vector"]
tags: ["Question","QFormat3"]
---

#### What is
## Cross product (vectors)

The cross product is the vector perpendicular to two given vectors times some other stuff:

![[Pasted image 20220225110553.png]]

Note that the order matters $\underline{a} \times \underline{b} \neq \underline{b} \times \underline{a}$

> ### $$ \underline{a} \times \underline{b} = (\sin(\theta) \times |\underline{a}| \times |\underline{b}|) \hat{\underline{n}} $$ 
> ### $$ \hat{\underline{n}} = \frac{\underline{a} \times \underline{b}}{\sin(\theta) \times |\underline{a}| \times |\underline{b}|} $$ 
>> where:
>> $\underline{a}, \underline{b}=$ some [[Scalars and vectors|vectors]]
>> $\hat{\underline{n}}=$ the [[unit vector]] perpendicular to $\underline{a}, \underline{b}$
>> $\theta=$ the angle between $\underline{a}, \underline{b}$

Now getting the vector for $\underline{n}$ is a pain in the ass. 
So instead you can calculate the [[cross product (vectors)|cross product]] using the [[determinant]]s in a simular way to how it's done in [[finding the determinant of a 3x3 matrix]]:
![[Pasted image 20220225112254.png]]

So here is the version for a 3D vector:
> ### $$ \underline{a} \times \underline{b} = \begin{pmatrix} a_{i} \\ a_{j} \\ a_{k} \end{pmatrix} \times \begin{pmatrix} b_{i} \\ b_{j} \\ b_{k} \end{pmatrix} = \begin{pmatrix} a_{j} b_{k} - a_{k} b_{j} \\ a_{k} b_{i} - a_{i} b_{k} \\ a_{i} b_{j} - a_{j} b_{i} \end{pmatrix} $$ 
>> where:
>> $\underline{a}, \underline{b}=$ some [[Scalars and vectors|vectors]]