---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe
## Calculus with vectors
### Useful stuff
Yum [[integration]], [[differentiation]] and [[Scalars and vectors|vectors]]...

Ok looks like it's basically the same as normal but you do the thing to each part of the stuff (clear?):

> ### $$ \frac{d}{dt} [ \underline{u}(t) + \underline{v}(t) ] = \frac{d\underline{u}}{dt} + \frac{d\underline{v}}{dt}  $$ 
>> where:
>> $\underline{v},\underline{u}=$ are vector funtions

This ^ one is basically what I said above, you can integrate/differentiate each part independently then add it back together... like in the example at the bottom. This one also works for [[integration]] with vectors.

> ### $$ \frac{d}{dt} [ f(t) \underline{v}(t) ] = \frac{df}{dt} \underline{v} + f \frac{d\underline{v}}{dt}  $$ 
>> where:
>> $\underline{v}=$ vector funtion
>> $f=$ scalar funtion

> ### $$ \frac{d}{dt} [ \underline{u}(t) \times \underline{v}(t) ] = \frac{d\underline{u}}{dt} \times \underline{v} + \underline{u} \times \frac{d\underline{v}}{dt}  $$ 
>> where:
>> $\underline{v},\underline{u}=$ are vector funtions
>> Since [[cross product (vectors)|cross product]] is used, order matters!


> ### $$ \frac{d}{dt} [ \underline{u}(t) \cdot \underline{v}(t) ] = \frac{d\underline{u}}{dt} \cdot \underline{v} + \underline{u} \cdot \frac{d\underline{v}}{dt}  $$ 
>> where:
>> $\underline{v},\underline{u}=$ are vector funtions
>> [[dot product (vectors)|dot product]] used

### Example (hopefully also usefull stuff)
> Differentiate:
> $$ \underline{r} = \underline{i} \sin t + \underline{j} \cos t $$

$$\begin{align*}
\underline{r} &= \underline{i} \sin t + \underline{j} \cos t \\
\frac{d\underline{r}}{dt} &= (\frac{d}{dt} \underline{i} \sin t) + \frac{d}{dt} (\underline{j} \cos t) \\
\frac{d\underline{r}}{dt} &= \underline{i} \cos t -\underline{j} \sin t \\
\end{align*}$$

Basically what I said, just differentiate them independently and add em back together.