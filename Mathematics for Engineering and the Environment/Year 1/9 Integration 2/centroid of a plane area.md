---
aliases: ["integration to find the center of a laminar","centre of area of a graph","centroid of a curve","cetnre of a curve","centroid"]
tags: ["Question","QFormat3"]
---

#### How can we find the
## Centroid of a plane area
### General case
Given that a 2D shape is defined as the area between two curves between two limits:
![[Pasted image 20211223105935.png]]
It's possible to find the center of this shape using:
> ### $$ \bar{y} = \frac{1}{2A} \int^{b}_a \left( [f(x)]^{2} - [g(x)]^{2} \right)  \cdot dx $$ 
>> where:
>> $A= \int^{b}_a [f(x)-g(x)]\cdot dx$ 
>> $\bar{y} =$ center of y
>> $a,b=$ limits
>> $f(x),g(x)=$  functions that define the curve
>> $f(x) \geq g(x)$

> ### $$ \bar{x} = \frac{1}{A} \int^{b}_a x[ f(x) - g(x) ] \cdot dx $$
>> where:
>> $A= \int^{b}_a [f(x)-g(x)]\cdot dx$ 
>> $\bar{x} =$ center of x
>> $a,b=$ limits
>> $f(x),g(x)=$  functions that define the curve
>> $f(x) \geq g(x)$

### Along the x axis
If we let $g(x)=0$ (so it's just between $f(x)$ and the x axis):

> ### $$ \bar{y} = \frac{1}{2A} \int^{b}_a  [f(x)]^{2}  \cdot dx $$ 
>> where:
>> $A= \int^{b}_a f(x)\cdot dx$ 
>> $\bar{y} =$ center of y
>> $a,b=$ limits
>> $f(x)=$  function that defines the curve


> ### $$ \bar{x} = \frac{1}{A} \int^{b}_a xf(x) \cdot dx $$
>> where:
>> $A= \int^{b}_a f(x)\cdot dx$ 
>> $\bar{x} =$ center of x
>> $a,b=$ limits
>> $f(x)=$  function that defines the curve