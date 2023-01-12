---
aliases: ["lift drependent coefficient","vortex drag coefficient"]
tags: ["Question","QFormat3","SESA1015"]
---

#### What causes the
## Induced drag coefficient
### Main bit
This is caused from the downwash the wing uses to produce lift, it increases in proportion to the square of the [[lift coefficient]] with a relationship of:

> $$ C_{Di} = k C_L^{2} $$ 
>> where:
>> $C_{Di} =$ induced drag coefficient
>> $k =$ a constant
>> $C_L =$ [[lift coefficient]]

^4d0b00

([[you use this a supprising amount]] so remember it)

### The $K$ and the $k$

The constant $k$ from above can be calculated using:

> $$ k = \frac{K}{\pi A} $$ 
>> where:
>> $k =$ a constant from [[induced drag coefficient#^4d0b00|this equation]]
>> $K =$ another constant
>> $A =$ [[wing aspect ratio]]

^438b96

This new constant $K$ depends on the planform shape of the wing. For elliptic wings (These have the lowest induced drag of all planforms) the value of $K$ is exactly 1. ^fce277

### Implications

We can rewrite the equation to show how aspect ratio effects induced drag:

$$ k = \frac{K}{\pi A} $$ 

$$ C_{Di} = k C_L^{2} $$ 

 $$ A = \frac{b}{\bar{c}} $$ 
 
 Can be combined:
 
 $$ \begin{align*}
C_{Di} &= \dfrac{K}{\pi A} C_L^{2}\\
C_{Di} &= \dfrac{K C_L^{2}}{\pi \dfrac{b}{\bar{c}} } \\
C_{Di} &= \dfrac{K \bar{c}}{\pi b } C_L^{2}
\end{align*} $$
 
> where:
> $b =$ [[Wing span]]
> $\bar{c} =$ [[Mean chord]]

$$C_{Di} = \dfrac{K \bar{c}}{\pi b }C_L^{2}$$

Tells us that you can minimise induced drag with long slender wings.