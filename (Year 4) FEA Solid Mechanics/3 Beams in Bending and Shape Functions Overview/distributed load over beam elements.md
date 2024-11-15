---
aliases: [""]
tags: []
---

## Distributed load over beam elements

Take the following scenario, what is the [[stiffness matrix]] and force vector?

![[Pasted image 20241111170333.png]]

The stiffness matrix is easy, we can just rip it from [[beam elements in pure bending]]. The force vector is harder to identify, if we recall [[distributed forces in PMTPE]] we will need our potential energy equation:

$$\begin{align*}
V &= -W &&\to&V&=  -\int^{L_{E}}_{x=0} p_{0} \:w(x) \: dx 
\end{align*}$$

Recalling [[beam elements in pure bending]], the definition of $w(x)$ is the [[beam elements in pure bending|hermite cubics]] 
$$\begin{align*}
&&w(x) &= f_{1}(x) q_{1} + f_{2}(x) q_{2}+ f_{3}(x) q_{3}+ f_{4}(x) q_{4}\\
V&=  -\int^{L_{E}}_{x=0} p_{0} \:w(x) \: dx  &&\to&  V&=  -q_{1}\left(\int^{L_{E}}_{x=0} p_{0} \:f_{1}(x) \: dx \right)  -q_{2}\left(\int^{L_{E}}_{x=0} p_{0} \:f_{2}(x) \: dx \right)  -q_{2}\left(\int^{L_{E}}_{x=0} p_{0} \:f_{2}(x) \: dx \right)  -q_{2}\left(\int^{L_{E}}_{x=0} p_{0} \:f_{2}(x) \: dx \right)
\end{align*}$$

In the event that $p_{0}$ is uniform we can simplify that expression into:

$$\begin{align*}
V &= \:... &&\to& V&=  p_{0}\left[-q_{1}\left(\int^{L_{E}}_{x=0}  \:f_{1}(x) \: dx \right)  -q_{2}\left(\int^{L_{E}}_{x=0} \:f_{2}(x) \: dx \right)  -q_{2}\left(\int^{L_{E}}_{x=0}  \:f_{2}(x) \: dx \right)  -q_{2}\left(\int^{L_{E}}_{x=0}  \:f_{2}(x) \: dx \right)\right] &&\to& 
V &= \begin{pmatrix} p_{0}\int^{L_{E}}_{x=0}  \:f_{2}(x) \: dx\\ p_{0}\int^{L_{E}}_{x=0}  \:f_{3}(x) \: dx\\ p_{0}\int^{L_{E}}_{x=0}  \:f_{1}(x) \: dx\\ p_{0}\int^{L_{E}}_{x=0}  \:f_{4}(x) \: dx \end{pmatrix}^{T} \begin{pmatrix} q_{1} \\ q_{2} \\ q_{3} \\ q_{4} \end{pmatrix} 
\end{align*}$$

Finally we can identify the other forces that are acting, they'll be: moment reaction, force reaction, applied external moment:

$$\begin{align*}
V_{other} &= \begin{pmatrix} R \\ M \\ 0 \\ -M \end{pmatrix}^{T} \begin{pmatrix} q_{1} \\ q_{2} \\ q_{3} \\ q_{4} \end{pmatrix} 
\end{align*}$$

So combining it we get:

![[Pasted image 20241111171548.png]]


