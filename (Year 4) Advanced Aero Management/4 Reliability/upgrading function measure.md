---
aliases:
  - upgrading function
tags:
---

## Upgrading function measure

This is a function specifically for use with systems constructed from [[continuous distribution functions|exponential distribution]]s, it measures how much gain we get from reducing the failure rate ([[hazard function|hazard rate]]) of component $i$:

> ### $$\begin{align*} I^{i}_{UF}(t)  &= \frac{\lambda_{i}}{G(q(t))} \times \frac{\partial G(q(t))}{\partial\lambda_{i}} \end{align*}$$
>> where using [[importance metrics notation]]:
>> $P(X_{i}=0)=q_{i}=$  The probability that the $i_{th}$ component is not working
>> $q=$ The set describing the probability of the components of the system not working
>> $G=$ the [[importance metrics notation|system unreliability function]]
>> $I^{i}_{UF}(t)=$ The fractional reduction in the probability of system failure when the $i_{th}$ components [[hazard function|hazard rate]] is reduced

As suggested by the name, this functions useful for determining where most benefit from upgrades can be found.


### Example 1 - Series

![[Pasted image 20241031102546.png]]
![[Pasted image 20241031102555.png]]
![[Pasted image 20241031102604.png]]
![[Pasted image 20241031102622.png]]


### Example 1 - 2-out-of-3

![[Pasted image 20241031102735.png]]
![[Pasted image 20241031102743.png]]
![[Pasted image 20241031102802.png]]