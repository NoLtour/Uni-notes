---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Moment over a section of beam cross section
### Theory
Look the method is basically just what we did in [[force over a section of beam cross section]], but since it's a moment not a force:
![[Pasted image 20211108131924.png]]

We also multiply the force of a given point by it's distance away from the [[neutral surface and neutral axis|neutral axis]]:
$$ \begin{align*}
M =& \int \int F_{yx}y \cdot dy\cdot dz &\\
=& \frac{E}{R} \int \int yy \cdot dy\cdot dz\\
=& \frac{E}{R} \int \int y^{2} \cdot dy\cdot dz
\end{align*} $$
Giving us the anticlockwise moment, pog!

![[second moment of area]]