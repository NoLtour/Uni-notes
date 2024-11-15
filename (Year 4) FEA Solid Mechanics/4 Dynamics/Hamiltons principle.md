---
aliases:
  - Hamilton's principle
  - Lagrangian of the system
tags:
---

## Hamilton's principle

In statics we knew that forces summed to zero, but in dynamics we deal with force imbalances, hence acceleration and velocity. Instead of [[principle of minimum total potential energy|PMTPE]] we apply Hamilton's principle.

[[Hamiltons principle|Hamilton's principle]] assumes a [[conservative system]], it's basis is the "Lagrangian of the system":

> ### $$\begin{align*} L  &= T - U  \end{align*}$$
>> where:
>> $L=$ [[Hamiltons principle|Lagrangian of the system]]
>> $T=$ Kinetic energy
>> $U=$ Stored potential energy of the system

We use [[Hamiltons principle|Hamilton's principle]] to find where gradient with respect to $q$ of the [[Hamiltons principle|Lagrangian of the system]] integrated with respect to $t$ is zero:

> ### $$\begin{align*} S(q) &= \int^{t_{2}}_{t_{1}} L(\:q(t), \:\dot{q}(t),\: t\:)\cdot dt &&& \partial S(q)&= 0  &&& \frac{d}{dt} \left(\frac{\partial L}{\partial \dot{q}}\right) - \frac{\partial L}{\partial q} &=  0 \end{align*}$$
>> where:
>> $S=$ The action, it's a [[functional]]
>> $t_{2},t_{1}=$ The bounds of time
>> $L=$ [[Hamiltons principle|Lagrangian of the system]]
>> $q=$ the state of nodes of the system
>> $\dot{q}=$ rate of change of nodes of the system

Although that sounds confusing, effectively what it means is that if we search the possible state space showing all the possible $q$'s and the paths between them (following time) then the path that is stationary under small variations of $q$ is the real one. 

![[Pasted image 20241112111611.png]]


