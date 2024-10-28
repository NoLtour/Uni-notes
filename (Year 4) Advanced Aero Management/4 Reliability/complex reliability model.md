---
aliases:
  - reliability model
  - series reliability model
  - parallel reliability model
  - m-out-of-n redundancy model
tags:
---

## Complex reliability model

### Requirements for model construction

Reasonably credible reliability predictions can be made if:
- The system is similar to systems developed, built and used previously
-  The new system does not involve significant technological risk

Credible predictions must be made if:
- The system will be manufactured in large quantities, or is very complex, or will be used for a long time, or a combination of these
- There is a strong commitment to the achievement of the reliability predicted (human lives at risk, high failure cost, market requirements)

If we make an aircraft from existing components, even though the thing's quite complex we can probably get a resonable idea of it's failure characteristics. However if we start going for some radical new design, or use untested components reliability models may require bounds so conservative we can't get much useful from them.

#### Series Reliability Model

This is where two independent events occur in series, with the failure of one blocking the path. Effectively it means (A) and (B) need to both work for the system to work.

![[Pasted image 20241024110240.png]]

Put mathamatically, the reliability of the system is:

> ### $$\begin{align*} R_{SYS}  &=  \prod^{n}_{i=1} R_{i} \end{align*}$$
>> where:
>> $R_{SYS}=$ [[reliability function]] of the series system
>> $R_{i}=$ [[reliability function]] of the independent events in series

#### Parallel Reliability Model

Ok, so what about redundancy? What if it takes more than one component to fail for the system to fail?

This is where the independent events are in parallel, so long as one of the parallel paths doesn't fail, the system doesn't.

![[Pasted image 20241024110707.png]]

> ### $$\begin{align*} R_{SYS}  &= 1- \prod^{n}_{i=1} (1-R_{i}) \\&= 1- \prod^{n}_{i=1} F_{i}  \end{align*}$$
>> where:
>> $R_{SYS}=$ [[reliability function]] of the parallel system
>> $R_{i}=$ [[reliability function]] of the independent events in parallel
>> $F_{i}=$ [[cumulative distribution function]] of the independent events in parallel

#### Constant hazard rate components

If the system has a constant [[hazard function|hazard rate]], then it is an [[continuous distribution functions#Exponential Distribution|exponential distribution]]. Hence it's [[cumulative distribution function|CDF]] and [[reliability function]] will be:

$$\begin{align*}
F(t) &= 1 - e^{-\lambda t} &&\to& R(t) &= e^{-\lambda t}
\end{align*}$$

When the question states "x failures per y units time", that means the hazard rate is constant! So use these. 

For instance if we consider a [[complex reliability model|series reliability model]] with a two different components with [[hazard function|hazard rate]]s of $\lambda_{1}$ and $\lambda_{2}$ respectively, the systems reliability function becomes:

$$\begin{align*}
&& R_{i}(t) &= e^{-\lambda_{i} t}\\
R_{SYS}  &=  \prod^{n}_{i=1} R_{i} &&\to& R_{SYS}  &= e^{-\lambda_{1} t} e^{-\lambda_{2} t} \\ &&&&&= e^{-(\lambda_{1}+\lambda_{2}) t}
\end{align*}$$

#### m-out-of-n redundancy model

Some systems have redundancy, but will fail unless n are still operating. For instance a system that has 4 motors, but needs atleast 2 to continue working for it to still function. These are called [[complex reliability model|m-out-of-n redundancy systems]], they can be put as:

> ### $$\begin{align*} R_{SYS}  &=  1-\sum\limits^{m-1}_{i=0} \begin{pmatrix} n\\i \end{pmatrix} R^{i} (1-R)^{n-1} \end{align*}$$
>> where:
>> $R_{SYS}=$ [[reliability function]] of system
>> $R=$ independent [[reliability function]] of the component being repeated (must be same for all)
>> 
>> [[binomial coefficient]] is used here

In a diagram these would look like:

![[Pasted image 20241024112449.png]]
### Examples
![[Pasted image 20241024111038.png]]
![[Pasted image 20241024111052.png]]


![[Pasted image 20241024112537.png]]![[Pasted image 20241024112549.png]]
