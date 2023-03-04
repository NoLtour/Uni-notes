---
aliases: [""]
tags: []
---

## Comparison of axial and shear stress

When designing structures the main thing that matters is max stress, so here's the question what's higher shear stress or axial stress?

From [[engineer's bending theory]] we know that max axial stress occurs at $\sigma_{xx,max}= \frac{M_{zz}y_{max}}{I_{zz}}$ and from [[shear force in a arbitrary symmetric cross section]] we know that (for a square section) max stress can be expressed as $1.5 \frac{Q_{yy}}{th} = \tau_{xy,max}$ so take the following case:

![[Pasted image 20230304095526.png]]

Here it is clear that the moments force $M=LF$ and the shear force is $Q_{yy}=F$ so subbing that in:

$$\begin{align*}
\sigma_{xx,max}&=  \frac{M_{zz}y_{max}}{I_{zz}} && & \tau_{xy,max} &= \frac{3}{2} \frac{Q_{yy}}{th} \\
 &=  \frac{FL \frac{h}{2}}{\frac{th^{3}}{12}} &&&  &= \frac{3}{2} \frac{F}{th} \\
 &=  \frac{6 FL }{th^{2}}  \\
&& \frac{\sigma_{xx,max}}{\tau_{xy,max}} &= \frac{\frac{6 FL }{th^{2}}}{\frac{3}{2} \frac{F}{th}}\\
&& &= \frac{4 L}{   h }
\end{align*}$$
From this it becomes clear that if w
