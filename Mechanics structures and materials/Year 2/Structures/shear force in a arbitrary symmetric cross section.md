---
aliases: [""]
tags: []
---

## Shear force in a arbitrary symmetric cross section

### Equation




### Proof

Ok so lets take a lil slice from a big beam, which is $x$ away from some refrence and $\delta x$ long:
![[Pasted image 20230303203200.png]]

The total shear acting on the upper surface of this element will be equal to the shear stress times the area on the top:
![[Pasted image 20230303203315.png]]

Giving the equation:
$$\begin{align*}
Q_{yx} &= \tau_{yx} t \: \delta x
\end{align*}$$
Where $t$ is thickness.

Then consider the forces acting on this section, you've got the shear force along the top and then the tensile/compressive stress acting on each side:

![[Pasted image 20230303203512.png]]

For this thing to be in equilibrium (only considering $x$ direction) we'll need these forces to sum to zero:

$$\begin{align*}
Q_{yx} &= \sigma_{xx}(x+\delta x) \: \delta A - \sigma_{xx}(x) \: \delta A\\
\tau_{yx} t \: \delta x &= \sigma_{xx}(x+\delta x) \: \delta A - \sigma_{xx}(x) \: \delta A\\
\end{align*}$$

