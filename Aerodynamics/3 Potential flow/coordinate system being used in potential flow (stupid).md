---
aliases: ["euler equations for potential flow syntax","irrotational flow for potential flow syntax"]
tags: []
---

## Coordinate system being used in potential flow
### Change
For the [[Potential flow Overview|potential flow notes]] we will be using this really stupid convention for coordinates instead of what we usually have. Why you ask? Because people of the [[I really hate this sort of thing with an unreasonable passion|past are stupid]] and inconsonant and no one has fixed it because changing the conventions too hard.

![[Pasted image 20221106101718.png]]

Essentially the change is that instead of using $y$ as the vertical direction, we use $z$ as the vertical and $y$ as the span wise.

### Consequential equations
Now all the equations we defined such as [[euler equations for inviscid and incompressible flow|euler equations]] are now inconsistent with the new coordinates so need to be adjusted (fucking cringe) where:
- $y\to z$
- $z \to y$
- $v \to w$
- $w \to v$

Note that $w$ is equivalent to $V_{z}$.

#### [[euler equations for inviscid and incompressible flow|Euler equations]]

> ### $$ \frac{\delta u}{\delta x} + \frac{\delta w}{\delta z} = 0 $$
> ### $$ u \frac{\delta u}{\delta x} + w \frac{\delta u}{\delta z} = \frac{1}{\rho} \frac{\delta p}{\delta x} $$
> ### $$ u \frac{\delta w}{\delta x} + w \frac{\delta w}{\delta z} = \frac{1}{\rho} \frac{\delta p}{\delta z} $$

#### [[curl of a vector|Irrotational flow]] 

Since we are working in 2D the only direction of curl that matters is in the $y$ direction hence:

> ### $$ \left(\frac{\delta u}{\delta z} - \frac{\delta w}{\delta x }\right) \hat{e}_{y} $$

Of course if this equals zero then we know the flow is irrotational, hence for irrotational flow:

> ### $$ \frac{\delta u}{\delta z} = \frac{\delta w}{\delta x } $$

#### Velocity potential and streamfunction

