---
aliases:
  - system unreliability function
tags:
---

## Importance metrics notation

Here is a bunch of definitions we use when working with importance metrics.

> ### $$\begin{align*} X  &= \begin{pmatrix} X_{1} & X_{2} & ... & X_{n} \end{pmatrix} &&& X_{i} &= \begin{cases} 0 & \text{Component has failed}\\1 & \text{Component is working} \end{cases} \end{align*}$$
> ### $$\begin{align*} q  &= \begin{pmatrix} q_{1} & q_{2} & ... & q_{n} \end{pmatrix} &&& P(X_{i}=0) &= q_{i} \end{align*}$$
> ### $$\begin{align*} \phi(X) &= \begin{cases} 0 & \text{System has failed}\\1 & \text{System is working} \end{cases} \end{align*}$$
> ### $$\begin{align*} G(q) &= 1 - P(\phi(X)=1) &&& G(0_{i}, q) &&& G(1_{i}, q) \end{align*}$$
>> where:
>> $X=$ The state of the components of a system
>> $X_{i}=$ The state of the $i_{th}$ component of the system
>> $P(X_{i}=0)=q_{i}=$  The probability that the $i_{th}$ component is not working
>> $q=$ The set describing the probability of the components of the system not working
>> $\phi(X)=$ The overall state of the system, whether it's failed or not. Dependent on the set of $X$
>> $G=$ the [[complex reliability model|system]]s un[[reliability function]]
>> $G(0_{i}, q)=$ The system unavailability when component $i$ is working
>> $G(1_{i}, q)=$ The system unavailability when component $i$ is not working


