---
aliases: ["system controllability","pole placement","moving closed-loop poles"]
tags: []
---

## State space system controllability

### Controllability

This is the ability of an external input or inputs to move the internal state of a system from any initial state to any final state in a finite time interval.
In [[I need some shitposting|other words]], can you manoeuvre the spacecraft in any direction using a limited number of thrusters.


> $\:$
> ### $$\begin{align*} \text{Controllable if:}&&&&\text{rank}(\bf{\mathcal{C}})  &= n   \end{align*}$$
> ### $$\begin{align*} \bf{\mathcal{C}} &= \begin{bmatrix}  \bf{C} & \bf{C}\bf{A} & \bf{C}\bf{A}^{2} & ... & \bf{C}\bf{A}^{n-1}  \end{bmatrix}  \end{align*}$$
>> where:
>> $\bf{A}=$ [[state space form|state matrix]]
>> $\bf{C}=$ [[state space form|output matrix]]
>> $\bf{\mathcal{C}}=$ 
>> $n=$ 
>> uses [[matrix rank|rank of a matrix]]

If a system is controllable, then we can move the closed-loop poles to any desired position.

### Pole placement

Starting with a [[state space form]] equation:

$$\begin{align*}
& &\text{Assume: } \bf{u} &= -\bf{K}\bf{x}\\
\dot{\bf{x}}  &= \bf{A}\bf{x} + \bf{B}\bf{u} & &\to & \dot{\bf{x}}  &= \bf{A}\bf{x} - \bf{B}\bf{K}\bf{x} & &\to & \dot{\bf{x}}  &= \bf{x}(\bf{A} - \bf{B}\bf{K})
\end{align*}$$

The [[system transfer function feature definitions|poles]] of the [[control system loop types|closed-loop system]] are clearly the [[eigenvalues and eigenvectors|eigenvalues]] of $\bf{A} - \bf{B}\bf{K}$, so we can set the [[system transfer function feature definitions|poles]] by manipulating $\bf{K}$.

#### Example

I'm gunna do a [[if the slides are good enough I use|lazy]]

![[Pasted image 20231111110813.png]]