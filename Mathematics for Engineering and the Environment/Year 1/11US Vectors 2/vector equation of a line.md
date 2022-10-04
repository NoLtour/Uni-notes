---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Vector equation of a line

Basically this is defining a vector that goes from a origin point to any point on a line through two points:

![[Pasted image 20220225172745.png]]

(An equation for getting point P (defined using $\underline{r}$) using $\underline{a}$ and $\underline{b}$)

This uses basic [[Addition of vectors|vector addition]], since $\underline{a}$ and $\underline{b}$ originate from the same point:
$$\begin{align*}
\vec{BA} &= \underline{a} - \underline{b} & \vec{OB} &= \underline{b} & \vec{OP} = \underline{r} &= \vec{OB} + \vec{BP} \\
\vec{BP} &= t(\underline{a} - \underline{b})\\
& & & & &= \underline{b} + t(\underline{a} - \underline{b})\\
& & & & &=\underline{a} t + \underline{b}(1 - t) \\
\end{align*}$$

We can further define the vector parrallel to the line as $\underline{c}$ to get $\underline{r} = \underline{a} + t\underline{c}$ then if we get this into [[Cartesian coordinates|cartesian]] form:

> ### $$ \frac{x-a_{1}}{c_{1}} = \frac{y-a_{2}}{c_{2}} = \frac{z-a_{3}}{c_{3}} $$ 
> ### $$\underline{r}=\underline{a}+t\underline{c} $$
> ### $$ \begin{pmatrix} x \\ y \\ z \end{pmatrix} = \begin{pmatrix} a_{1}  \\ a_2 \\ a_3 \end{pmatrix} + t\begin{pmatrix}c_1 \\ c_2 \\ c_3\end{pmatrix} $$
>> where:
>> $\underline{r}=$ a vector function defining the line
>> $\underline{c}=$ a vector defining the gradient of the line
>> $\underline{a}=$ a vector defining the point on the line where $t=0$
>> $t=$ some scalar used to vary position