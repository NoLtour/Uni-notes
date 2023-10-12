---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How do you find
## Longitudinal strain in a beam
#### Important definitions
First we need a refrence point for this we use the [[neutral surface and neutral axis|neutral axis]]:
![[neutral surface and neutral axis]]

We will work under the same assumptions as from [[deformation due to bending in beams#Assumptions]].

### Ma(e)th
![[Pasted image 20211108095704.png]]

If we get a general equation for [[Strain|strain]] ($\epsilon_{xx}$) on the surface A' B':
$$ \epsilon_{xx} = \frac{A'B'-AB}{AB} $$ ^234340

Here $AB$ represents the origional dimentions of the beam so since the [[neutral surface and neutral axis|neutral surface]] is equivilent and equal:
$$ \begin{align*}
AB = A_0'B_0' = Rd\theta
\end{align*} $$
also:
$$ A'B' = (R+y)d\theta $$
Note that $Rd\theta$ uses radians, and subbing back into the strain equation:

$$ \begin{align*}
\epsilon_{xx} &= \frac{(R+y)d\theta-Rd\theta}{Rd\theta}\\
&= \frac{(R+y)-R}{R}\\
&= \frac{y}{R}
\end{align*} $$

#### Implications
> ### $$ \epsilon_{xx} = \frac{y}{R} $$
>> where:
>> $\epsilon_{xx}=$ Longitudinal strain
>> $y=$ Verticle distance from [[neutral surface and neutral axis|neutral surface]]
>> $R=$ Radius of the circle arc representing the beam
^a731ed

What this tells us is that strain varies linearly with distance away from the neutral surface.
