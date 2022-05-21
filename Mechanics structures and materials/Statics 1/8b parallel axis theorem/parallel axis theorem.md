---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Parallel axis theorem
An example can be found at [[parallel axis theorem and other example#Using the parallel axis theorem]]
### Equation

> ### $$ I_{z'z'} = I_{zz} + Ab^{2} $$ 
>> where:
>> $I_{z'z'}=$ [[second moment of area]] around z'
>> $I_{zz}=$ [[second moment of area]]
>> $A=$ Area of shape
>> $b=$ Separation between center line of shape and [[neutral surface and neutral axis|neutral axis]]
>> ![[Pasted image 20220521103931.png]]


### Setup
Suppose you want to use on of the [[standard results for second moment of area]] for a shape that isn't on the [[neutral surface and neutral axis|neutral axis]]:

![[Pasted image 20220521103931.png]]

But instead it's centres now off.

These *parallel axis* are meant to be used instead, see where this is going?

### Maths
$$\begin{align*}
   I_{z'z'} &= \int \int (y+b)^{2} \cdot dydz\\
&= \int \int   y^{2}+2by+b^{2}   \cdot dydz\\
&= \int \int   y^{2}   \cdot dydz + 2b \int \int  y  \cdot dydz + b^{2}\int \int 1 \cdot dydz\\
& & 0 &= \int \int  y  \cdot dydz& Area &= \int \int 1 \cdot dydz\\
&= \int \int   y^{2}   \cdot dydz + 2b\cdot 0+ b^{2}\cdot A\\
&= \int \int   y^{2}   \cdot dydz + Ab^{2}
\end{align*}$$

### Implications
$I_{z'z'} = I_{zz} + Ab^{2}$ So you can increase the value of $Ab^{2}$ to increase the $I_{z'z'}$ and since we know that $\sigma = \frac{My}{I_{z'z'}}$ (from [[engineer's bending theory]]), we can drastically decrease the stress for the same quantity of material by spacing it out:

- Hence a hollow cylinder is much stronger than it's equivalent massed solid one
- Hence an I beam is much stronger than a solid square beam for its equivalent massed one

![[Pasted image 20211115103138.png]]

Allowing for lighter and stronger structures. (which matters when your on an aero course huh, I know shocking)

#### Example of excellent engineering:
![[pussymobile.jpg]]