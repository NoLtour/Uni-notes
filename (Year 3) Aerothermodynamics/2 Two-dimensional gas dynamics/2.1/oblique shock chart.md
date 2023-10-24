---
aliases: ["oblique shock properties","strong solution","weak solution"]
tags: []
---

## Oblique shock chart
### Description
If we chart the equations found in [[oblique shock equations]], we'll get the [[oblique shock chart]] ([[ok I will double kill myself|shocking]]).

![[Pasted image 20231024175130.png]]

Lot's of interesting properties of [[oblique shocks]] can be gathered from this chart:
- There is generally ($\theta<\theta_{max}$) 2 solutions for any valid [[oblique shock angles|turning angle]]
- At zero [[oblique shock angles|turning angle]] they have a [[normal shock properties equations|normal shock]] solution as well as some $\beta\neq90\degree$ solution. 
- All Mach numbers have a [[normal shock properties equations|normal shock]] solution at an appropriate turning angle, which makes sense
- The maximum turning angle is $45\degree$ with higher Mach numbers tending towards this value
- There exists a maximum possible turning angle for any mach number $\theta_{max}$

### Technical stuff

![[Pasted image 20231024185257.png]]

Lot's to break down in this more detailed chart.
- The dotted blue line separates the solutions where $M_{2}$ is less than 1 (above) from where it is greater than one (supersonic, and blow)
- The red line shows where $\theta_{max}$ occurs for each $M_1$, above it is where [[oblique shock chart|strong solutions]] occur and below is where [[oblique shock chart|weak solutions]] occur
- Looking at the 2 lines, we can see that all [[oblique shock chart|strong solutions]] are subsonic, but only almost all [[oblique shock chart|weak solutions]] are subsonic

In this course we only deal with [[oblique shock chart|weak solutions]], and in real life most [[oblique shocks]] are weak.

The equations for where $\theta=0$ are the following:

> ### $$$$
> ### $$\begin{align*} \text{At }\theta=0\degree:&&  \beta &= \arcsin \frac{1}{M_{1}} \:\:\text{or}\:\: \beta = 90\degree \end{align*}$$
>> where:
>> $\theta=$ [[oblique shock angles|shock angle]]
>> $\beta=$ [[oblique shock angles|flow turning angle]]
>> $M_{1}=$ [[Mach number]] before [[oblique shocks|oblique shock]]

Note that often a [[oblique shock chart]] (like the one above) can be used to calculate $\theta$ instead of using the [[oblique shock equations]], alternatively make use of On-line shock calculator: https://devenport.aoe.vt.edu/aoe3114/calc.html