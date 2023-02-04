---
aliases: ["superposition method"]
tags: ["Question","QFormat3"]
---

#### How
## Solving statically indeterminate beams with superposition method
Essentially what this involves is using [[deflection of beams standard resaults]] for [[solving statically indeterminate beams]], by supperimposing standard resaults to get the overall deflection and skip a few steps.

### Example

![[Pasted image 20211129132209.png]]

We just need to superimose [[deflection of beams standard resaults#Uniformly distrobuted load]] and [[deflection of beams standard resaults#Point load]] after rearranging them into the correct format:

$$\begin{align*}
v(L) &= 0 \\
   0 &= \frac{1}{8} \frac{wL^{4}}{EI} + \frac{1}{3} \frac{FL^{3}}{EI} \\
\frac{1}{3} \frac{FL^{3}}{EI} &=- \frac{1}{8} \frac{wL^{4}}{EI}\\
\frac{1}{3} F &= -\frac{1}{8} wL\\
F &= -\frac{3}{8} wL
\end{align*}$$
We know that here $F$ is in the opposite direction as $R$ so $F=-R$ and:
$$\begin{align*}
   R &= \frac{3}{8} wL
\end{align*}$$

This is the same example as the [[solving statically indeterminate beams with double integration method|double integration method]], but as you can see much faster.