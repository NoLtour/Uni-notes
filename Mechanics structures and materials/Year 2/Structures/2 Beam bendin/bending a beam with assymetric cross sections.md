---
aliases: ["bending a beam with asymmetric cross sections"]
tags: []
---

## Bending a beam with [[grow up|ass]]ymetric cross sections
### Intro
![[Pasted image 20230219120816.png]]

When a beam is under bending moment $M_{z}$ (parallel to z axis), it deflects in both x-y and x-z planes. This also has the consequence that unlike with symetric beams where max stress occurs at the upper and lower points this may not be the case in a asymmetric beam.

Note: Positive $M_{z}$ creates positive stress in the positive side of the beam in the yz plane. Therefore, the shown $M-z$ above is negative. ([[deformation due to bending in beams|notation for moments on a beam]])

### Modelling it

#### Final equation

> ### $$\begin{align*} \sigma_{xx}  &= \frac{ (M_{z} I_{y} - M_{y} I_{yz}) y  + (M_{y} I _{z} - M_{z} I_{yz}) z }{I_{y} I_{z} - I_{yz}^{2}}  \end{align*}$$
>> where:
>> $M_{z},M_{y}=$ bending moments acting in xz and xy planes repectively
>> $I_{y}, I_{z}=$ [[moment of area]]
>> $=$

#### Proof (unfinished)
##### Method
We already know how to model beam bending stuff from year 1, but what happens if we have moments acting in multiple directions instead of just one plane?

![[Pasted image 20230219121827.png]]

Then we can use superposition by analysing moments and bending in the xy and xz planes and adding em to find the total deformation:
![[Pasted image 20230219122005.png]]

##### XY plane
Ok so lets isolate the moments in the xy plane:
![[Pasted image 20230219122133.png]]

Then we'll need to do some good ol curvature analysis (year 1 stuff), using the following equations:
- [[Bending of beams notes]]