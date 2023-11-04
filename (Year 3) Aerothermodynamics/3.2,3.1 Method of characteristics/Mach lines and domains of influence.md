---
aliases:
  - Mach lines
  - domains of influence
  - domains of dependence
  - characteristic lines
tags:
---

## Mach lines and domains of influence

#### Mach lines/Characteristic lines

So looking back at what we described in [[irrotational, homentropic, supersonic flow#Meaning]], it's apparent that the region of downstream information propagation can be drawn if [[Mach cone|Mach angle]] is known:

![[Pasted image 20231104162902.png]]

If we want to remain in the purely mathematical domain, we may want to express $\bf{A}$ as an [[eigenvalues and eigenvectors|eigenvalue]] for convenient use in equations, doing so yields:

$$\begin{align*}
&&\bf{A} &= \begin{pmatrix} 0  & -\tan\mu \\ -\tan\mu   & 0\end{pmatrix}\\
\det(\bf{A} - \bf{I}\lambda)&=0 &&\to & \lambda &= \pm \tan \mu
\end{align*}$$

Which shows that the slope of [[Mach lines and domains of influence|Mach lines]] (how info propagates) are just the eigenvalues, with positive and negative values demonstrating the symmetry.

#### Domains of influence and dependence

![[Pasted image 20231104161831.png]]

It follows from the idea of a [[Mach lines and domains of influence|domains of influence]] that a [[Mach lines and domains of influence|domains of dependence]] must also exist. Though it should also be stated that since $M$ can change in a flow the above diagram is only accurate on a small scale, the lines separating domains would curve in a large Mach variant flow.

#### Summery

> ### $$\begin{align*}  0&=  \frac{\partial \theta}{\partial s} -  \tan \mu\frac{\partial\nu }{\partial n} \end{align*}$$
> ### $$\begin{align*}  0  &=   \frac{\partial\nu}{\partial s}-\tan  \mu  \frac{\partial \theta}{\partial n}  \end{align*}$$
> ### $$\begin{align*} 0&= \frac{\partial}{\partial s} \begin{pmatrix} \nu \\ \theta \end{pmatrix} + \begin{pmatrix} 0  & -\tan\mu \\ -\tan\mu   & 0\end{pmatrix} \frac{\partial}{\partial n} \begin{pmatrix} \nu \\ \theta \end{pmatrix} & \to && 0&= \frac{\partial\bf{Q}}{\partial s}   + \bf{A} \frac{\partial \bf{Q}}{\partial n}    \end{align*}$$
> ### $$\begin{align*} \bf{Q}&= \begin{pmatrix} \nu \\ \theta \end{pmatrix}& \bf{A}&= \begin{pmatrix} 0  & -\tan\mu \\ -\tan\mu   & 0\end{pmatrix} & \lambda &= \pm \tan \mu \end{align*}$$
>> where:
>> $\theta=$ [[Prandtl–Meyer expansion fan|turning angle]]
>> $\nu=$ [[Prandtl–Meyer expansion fan|Prandtl-Meyer function]]
>> $\frac{\partial n}{\partial s}=$ streamline "expansion" with distance along streamline
>> $s=$ distance along streamline
>> $\mu=$ [[Mach cone|Mach angle]]
>> $\lambda=$ [[eigenvalues and eigenvectors|Eigenvalues]] of $\bf{A}$
>> 
>> $\mathbf{Q}=$ represents the [[Prandtl–Meyer expansion fan|Prandtl-Meyer function]] and the [[Prandtl–Meyer expansion fan|turning angle]], so it is a representation of the angle of flow and the expansion wave angle. It characterises flow property change.
>> $\mathbf{A}=$ is a matrix representing the [[Mach cone|Mach angle]], which going back to the [[Mach cone#Supersonic]] can be seen to reflect how information propagates downstream, with the angle being a pure function of Mach number
>> 
>> ![[Pasted image 20231104162902.png]]
