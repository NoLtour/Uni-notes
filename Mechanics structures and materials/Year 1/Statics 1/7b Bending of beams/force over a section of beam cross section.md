---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Force over a section of beam cross section
### Theory

![[Pasted image 20211108124349.png]]

We can see that the section has area $dy \cdot dz$ and force due to $\sigma_{xx}$ so force is:
$$ F = \sigma_{xx}(dy\cdot dz) $$
But getting the force of a neglibible sized points kinda useless (shock), now if only there was some method... something that could find the area enclosed by a graph, if only that existed. It would be amazing.
Well guess what, it's called calculus and you already knew that, remember when you [[kekekkw|asked your teacher]] "but when will I use this?" well now (bitch).

### Math
I'm going to use [[youngs modulus]] and [[longitudinal strain in a beam#Implications]].

$$ \begin{align*}
F =& \int \int \sigma_{xx}\cdot dy\cdot dz & \sigma_{xx} =& \frac{Ey}{R}\\
F =& \int \int \frac{Ey}{R} \cdot dy\cdot dz\\
F =& \frac{E}{R} \int \int y \cdot dy\cdot dz
\end{align*} $$

Also note that $\int \int y \cdot dy\cdot dz$ is known as the [[first moment of area]].

#### Force equilibrium
But we know that the total force acting on the cross section must be 0 because it's in equalibrium:
$$ \begin{align*}
F =& \frac{E}{R} \int \int y \cdot dy\cdot dz\\
 =& 0
\end{align*} $$
Further $\frac{E}{R} \neq 0$ because E is [[modulus of elasticity]] and R is the radius of the circle that the beam's being modelled ([[deformation due to bending in beams#Assumptions|look here if confused]]). So that means that we can simplify to:
$$ \begin{align*}
0 =& \int \int y \cdot dy\cdot dz\\
\end{align*} $$

### Implications
#### [[neutral axis position|Neutral axis position]]

If we think about what:
$$ \begin{align*}
0 =& \int \int y \cdot dy\cdot dz\\
\end{align*} $$
Actually means, it is where the total area above a line on the cross section equals the total area below. Since we know this line to be defined as the [[neutral surface and neutral axis|neutral axis]], we can extend the definition of the neutral axis to be a line that passes through a beam cross sections centre of area.

![[Pasted image 20211108131114.png]]