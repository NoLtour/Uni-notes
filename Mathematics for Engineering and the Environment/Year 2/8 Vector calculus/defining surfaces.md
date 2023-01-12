---
aliases: ["surface"]
tags: []
---

## Defining surfaces

### Intro

There are 3 ways to describe a surface (3D space):
1) The graph of a function of 2 variables $z=f(x,y)$
2) A level surface of 3 variables $F(x,y,z)=c$
3) A parameterised surface $(s,t) \to ( x(s,t), y(s,t), z(s,t) )$   

Each representation method has it's own pro's and cons when manipulating, for this course we will generally be using (3).

### Parameterised surface

Basically what this involves is creating a 2D grid on which position is defined using some new variable, say $s,t$ and then mapping that grid onto a 3D space by describing position in terms of those new variables:

![[Pasted image 20221227235232.png]]

By making $s$ and $t$ be perpendicular we can take [[derivative symbols|partial derivatives]] since the other will be constant, this becomes [[which is why we use representation method 3|REALLY]] useful when we start applying all the fucky [[Vector calculus Overview|vector shit]] we've learned so far to em.

> ### $$\begin{align*} \vec{r}(s,t)  &= f_{x}(s,t)\:\hat{i} + f_{y}(s,t)\:\hat{j} + f_{z}(s,t)\:\hat{k}  \end{align*}$$
> ### $$ \frac{\delta \vec{r}}{\delta s} \cdot \frac{\delta \vec{r}}{\delta t} = 0 $$
> ### $$ \frac{\delta \vec{r}}{\delta s} \times \frac{\delta \vec{r}}{\delta t} = \vec{n} $$
>> where:
>> $\vec{r}(s,t)=$ the parameterised surface
>> $f_{x},f_{y},f_{z}=$ functions defining position in 3D space
>> $s,t=$ variables describing position on 2D surface, are at right angles to each other (independent) 
>> $\cdot=$ [[dot product (vectors)|dot product]]
>> $\times=$ [[cross product (vectors)|cross product]]
>> $\vec n=$ normal vector to the surface at some point

Since we know that along the surface $s$ and $t$ are independent, we can take the derivative of $\vec r$ with respect to $s$ and $t$ to get the vectors describing their directions in 3D space which we know to be perpendicular to eachother so the identities of [[dot product (vectors)|dot product]] and [[cross product (vectors)|cross product]] follow intuitively.

#### Example cylinder
![[Pasted image 20221227235701.png]]

### Example sphere
![[Pasted image 20221227235725.png]]
