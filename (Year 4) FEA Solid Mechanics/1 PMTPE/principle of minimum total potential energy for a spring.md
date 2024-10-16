---
aliases: [""]
tags: []
---

## Principle of minimum total potential energy for a spring

### One spring

Take the following spring, with displacement of the tip $q$:

![[Pasted image 20241008162414.png]]

[[principle of minimum total potential energy|PMTPE]] would start by describing it's strain energy ($U$) and potential energy ($V$):

$$\begin{align*}
U &= \frac{1}{2} kq^{2} &&& V &= -W=-Fq\\
\end{align*}$$

Here strain energy makes sense, it's just the energy actually mechanically available in the spring (in dynamics we called it [[conservative force|potential energy]], needlessly confusing). Potential energy ($V$) is the instantaneous work done equation.

$$\begin{align*}
&&&&&&\text{turn}&\text{ing point}\\
\Pi &= U+V &&\to& \Pi&= \frac{1}{2} kq^{2} - Fq &&\to&
\frac{\partial \Pi}{\partial q} &= \frac{1}{2} 2 kq - F =0&&\to& F=kq
\end{align*}$$

The result is exactly what we expect! $F=kq$ is the relationship between a simple springs force and extension.

### Two springs

![[Pasted image 20241008165234.png]]

Ok so that was ez, what about 2 springs though? 

$$\begin{align*}
U&= \frac{1}{2}k_{1} q_{1}^{2} + \frac{1}{2} k_{2} (q_{2}-q_{1})^{2} &&& V &= -F_{1} q_{1} - F_{2}q_{2}  
\end{align*}$$

$$\begin{align*}
\Pi &=\frac{1}{2}k_{1} q_{1}^{2} + \frac{1}{2} k_{2} (q_{2}-q_{1})^{2}  -F_{1} q_{1} - F_{2}q_{2}   
\end{align*}$$
Then do the minimisation, we need to do so for both:

$$\begin{align*}
0=\frac{\partial\Pi}{\partial q_{1}} &=\frac{1}{2}(2k_{1} q_{1}  +  k_{2} (-2q_{2}+2q_{1}))  -F_{1}  &&\to& 
F_{1} &= q_{1}(k_{1} + k_{2} ) - q_{2} k_{2} \\

0 =\frac{\partial\Pi}{\partial q_{2}} &= \frac{1}{2} k_{2} (2q_{2}-2q_{1}) - F_{2} &&\to&
F_{2} &=  -q_{1}k_{2}+q_{2}k_{2}
\end{align*}$$

Now if we write that into a matrix form, we can solve for $F$ but also (more usefully) $q$:

$$\begin{align*}
\begin{pmatrix} F_{1} \\ F_{2} \end{pmatrix} &= \begin{pmatrix}k_{1} + k_{2} & -k_{2} \\ -k_{2} & k_{2} \end{pmatrix} \begin{pmatrix} q_{1} \\ q_{2} \end{pmatrix} &&\to&

 \begin{pmatrix}k_{1} + k_{2} & -k_{2} \\ -k_{2} & k_{2} \end{pmatrix}^{-1} \begin{pmatrix} F_{1} \\ F_{2} \end{pmatrix} &=  \begin{pmatrix} q_{1} \\ q_{2} \end{pmatrix}
\end{align*}$$

It's not so hard to invert this matrix and keep it all analytical... but cba rn lol. 

We can see that this method works, and theoretically could be scaled further. Thing is, doing all these steps is already long, and will only become longer...
