---
aliases: [""]
tags: []
---

## Streamline curvature and pressure

### The equations

If instead of using a Cartesian coordinate system we use one defined in terms of a streamline, where $s$ is tangent along the streamline and $n$ is normal to the streamline. Doing this [[momentum balance in inviscid incompressible flow#^da19ae|these equations]] become:

#### Equation along streamline

> ### $$ \rho V_{s} \frac{\delta V_{s}}{\delta s} = - \frac{\delta p}{\delta s} $$ 
>> where:
>> $V_{s}=$ velocity tangent to streamline 
>> $s=$ position along streamline
>> $p=$ pressure
>> $\rho=$ density

(Note that this equation actually integrates into the [[Bernouillis equation]], without accounting for height changes of course)

#### Equation normal to streamline

> ### $$ \rho \frac{V_{s}^{2}}{r} = \frac{\delta p}{\delta n } $$ 
>> where:
>> $V_{s}=$ velocity tangent to streamline 
>> $n=$ position normal to streamline
>> $r=$ [[radius of curvature]]
>> $p=$ pressure
>> $\rho=$ density

Something to note is that by definition of [[streamlines|streamline]] $V_{n}=0$. (streamlines are literally lines of velocity vectors)

### Implications

Note that this equation is literally the same as [[centrifugal force equation|centrifugal force]]:
$$ \frac{\rho V_{s}^{2}}{r} = \frac{\delta p}{\delta n } $$ 

This relationship implies that surface curvature (or curvature of the streamline) is directly linked to the pressure gradient:
![[Pasted image 20221017185113.png]]
Such that:
- For a convex surface, the pressure will be lower than freestream.
- For a concave surface, the pressure will be higher than freestream.

Now consider a airfoil:

