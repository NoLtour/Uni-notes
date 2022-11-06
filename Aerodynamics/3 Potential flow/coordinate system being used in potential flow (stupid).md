---
aliases: ["euler equations for potential flow syntax","irrotational flow for potential flow syntax","velocity potenial for potential flow syntax","stream function for potential flow syntax"]
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
Since none of these equations are new just a change in the format used for the axis labels I'm not putting exhaustive definitions of the variables below each equation. If you need to know the variable defs just look at the page they where converted from.

#### [[euler equations for inviscid and incompressible flow|Euler equations]]

> ### $$ \frac{\delta u}{\delta x} + \frac{\delta w}{\delta z} = 0 $$
> ### $$ u \frac{\delta u}{\delta x} + w \frac{\delta u}{\delta z} = \frac{1}{\rho} \frac{\delta p}{\delta x} $$
> ### $$ u \frac{\delta w}{\delta x} + w \frac{\delta w}{\delta z} = \frac{1}{\rho} \frac{\delta p}{\delta z} $$

#### [[curl of a vector|Irrotational flow]] 

Since we are working in 2D the only direction of curl that matters is in the $y$ direction hence:

> ### $$ \left(\frac{\delta u}{\delta z} - \frac{\delta w}{\delta x }\right) \hat{e}_{y} $$

Of course if this equals zero then we know the flow is irrotational, hence for irrotational flow:

> ### $$ \frac{\delta u}{\delta z} = \frac{\delta w}{\delta x } $$

#### Velocity potential and stream function
The [[velocity potential]] in cartesian:

> ### $$ u = \frac{\delta \phi}{\delta x} $$
> ### $$ w = \frac{\delta \phi}{\delta z} $$

The velocity potential in polar coordinates:
> ### $$ V_{r} = \frac{\delta \phi}{\delta r} $$
> ### $$ V_{\theta} = \frac{1}{r} \frac{\delta \phi}{\delta \theta} $$

The [[stream function (2D)|stream function]] in cartesian:
> ### $$ u = \frac{\delta \psi}{\delta z} $$
> ### $$ w = -\frac{\delta \psi}{\delta x} $$


The [[stream function (2D)|stream function]] in polar:
> ### $$ V_{r} = \frac{1}{r} \frac{\delta \psi}{\delta \theta} $$
> ### $$ V_{\theta} = -\frac{\delta \psi}{\delta r} $$

#### [[laplace equation for flow|Laplace equations]]

For [[mass conservation and velocity potential|incompressible flow]]:

> ### $$  \frac{\delta^{2} \phi}{\delta x^{2} } + \frac{\delta^{2} \phi}{\delta z^{2} } = 0$$

For [[laplace equation for flow|irrotational flow]]:

> ### $$  \frac{\delta^{2} \psi}{\delta x^{2} } + \frac{\delta^{2} \psi}{\delta z^{2} } = 0$$
 