---
aliases: [""]
tags: []
---

## Criticality importance measure

This is a measure of how fucked you are because of a specific component, it allows you to asses:
1) Is this component critical to the system
2) Chance it has already failed at time $t$

If the answer to both of those ends up being high, then the measures very high and your fucked.

> ### $$\begin{align*} I^{i}_{CR} &= I^{i}_{B}(t) \times \frac{q_{i}(t)}{G(q(t))}  =  \frac{\partial G(q(t)) }{\partial q_{i}(t)}\times \frac{q_{i}(t)}{G(q(t))} \\&=  \frac{[G(1_{i} ,q) - G(0_{i},q)]\times q_{i}(t)}{G(q(t))} \end{align*}$$
>> where using [[importance metrics notation]]:
>> $P(X_{i}=0)=q_{i}=$  The probability that the $i_{th}$ component is not working
>> $q=$ The set describing the probability of the components of the system not working
>> $G=$ the [[importance metrics notation|system unreliability function]]
>> $G(0_{i}, q)=$ The system unavailability when component $i$ is working
>> $G(1_{i}, q)=$ The system unavailability when component $i$ is not working
>> $I^{i}_{B}(t)=$ The [[Birnbaum importance measure]] for component $i$
>> $I^{i}_{CR}=$ The [[probability convention for advanced management|conditional probability]] that at time $t$ component $i$ is both critical to the system functioning AND has already failed

### Example
![[Pasted image 20241031102023.png]]
![[Pasted image 20241031102031.png]]
![[Pasted image 20241031102042.png]]
