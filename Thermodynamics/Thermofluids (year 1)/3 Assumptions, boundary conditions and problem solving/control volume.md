---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is a
## Control volume
### Defenition
A control volume is a fixed region in space chosen for the thermodynamic study of mass and energy balances for flowing systems. The boundary of the control volume may be a real or imaginary envelope. The control surface is the boundary of the control volume.

![[Pasted image 20220512153625.png]]

At steady state, a control volume can be thought of as an arbitrary volume in which the mass of the continuum remains constant. As a continuum moves through the control volume, the mass entering the control volume is equal to the mass leaving the control volume.

Unlike a [[system (thermodynamics)|system]] which has no mass transfer across it's [[system boundary]].

### Momentum conservation

To find the net force acting on a control volume it's just conservation of momentum + normal pressure on the control volume boundary. 

> ### $$\begin{align*} \vec{F}  = \sum\limits \vec{P}_{n} A_{n} + \sum\limits_{\text{in}} \vec{V}_{n} \dot{m}_{n}   - \sum\limits_{\text{out}} \vec{V}_{n} \dot{m}_{n}   \end{align*}$$
>> where:
>> $\vec{V}_{n} \dot{m}_{n}=$ the momentum of the mass flow of some input/output from the control volume
>> $\vec{F}=$ resultant force acting on the control volume (usually your solving for this)
>> $\vec{P}_{n} A_{n}=$ Pressure over area acting over a side of the control volume
