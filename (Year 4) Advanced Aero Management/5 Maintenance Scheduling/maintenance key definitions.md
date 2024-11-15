---
aliases:
  - mean time to failure
  - MTTF
  - repairable system
  - system availability
  - availability
tags:
---

## Maintenance key definitions

#### Mean time to failure

The definition is quite self explanatory:

> ### $$\begin{align*} \text{MTTF} =E[T] &= \int^{\infty}_{0} t \: f(t) \cdot dt \\&= \int^{\infty}_{0} R(t) \cdot dt  \end{align*}$$
>> where:
>> $\text{MTTF}=E[T]=$ mean time to failure, the average time taken for a component to fail after instillation
>> $f(t)=$ the [[probability density function|PDF]] of the component
>> $R(t)=$ the [[reliability function]] of the component

#### Repairable systems

We’ve defined a repairable system as one which is repaired upon failure, this definition includes large and complex systems e.g: aircraft, cars, mainframes, telephone networks etc.

#### Availability

This is critical to maintenance analysis, it's the time that the system is actually performing the job it's supposed to. If the system's down for scheduled maintenance we're loosing availability, but we will loose more availability if we have to scramble to perform unplanned repairs due to a component failure. 

