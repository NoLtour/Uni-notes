---
aliases: [""]
tags: []
---

## Parallel axis theorem and other example
### Question
![[Pasted image 20211115101426.png]]

#### Using the [[parallel axis theorem]]
First you split it into bits:
![[Pasted image 20211115101452.png]]

For the $I_{zz}$ of all of these we can just use [[standard results for second moment of area]]

For area (1):
> $$\begin{align*}
I_{zz} &= \frac{bd^{3}}{12}\\
&= \frac{(5)(90)^{3}}{12}\\
&= 303750
\end{align*}$$

For area (2) and (3):
> $$\begin{align*}
I_{zz} &= \frac{bd^{3}}{12} + h^{2}A\\
&= \frac{(60)(5)^{3}}{12} + (47.5)^{2}(60\cdot 5)\\
&= 677500
\end{align*}$$

Combining them:
> $$\begin{align*}
   I_{zz} &= 303750 + 2(677500)\\
&= 1658750 mm^{4} 
\end{align*}$$

#### The [[based method for finding second moment|__based__ method]] 
