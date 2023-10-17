---
aliases: ["Kelly cosine"]
tags: []
---

## Effect of angle on solar panel output

Previously in [[maximising solar power out#Sun angle effect]] we demonstrated that $\cos$ provides a descent approximation of current drop with cell output. This approximation only works well in the range of 0 to 50 degrees:

![[Pasted image 20231016082515.png]]

To achieve greater accuracy a Kelly cosine should be used:
- Beyond $85\degree$ no power is produced
- Beyond $50\degree$ a standard $\cos$ approximation becomes impractical

> ### $$\begin{align*} I_{s}  &= I_{0} \{text{KellyCos}}(\theta)  \end{align*}$$
>> where:
>> $I_{s}=$ Current at current angle
>> $I_{0}=$ Reference current when cell is normal to the sun ($\theta=0$)
>> $\theta=$ Angle between cell normal and incident light