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

> ### $$\begin{align*} \sigma_{xx}  &= \frac{ (M_{zz} I_{yy} - M_{yy} I_{yz}) y  + (M_{yy} I _{zz} - M_{zz} I_{yz}) z }{I_{yy} I_{zz} - I_{yz}^{2}}  \end{align*}$$
> ### $$\begin{align*} I_{zz} &= \int_{A} y^{2} \: dA &  I_{yy} &= \int_{A} x^{2} \: dA &  I_{yz} &= \int_{A} xy \: dA &  \end{align*}$$
> ### $$\begin{align*} M_{zz} &= \frac{EI_{zz}}{R_{y}} + \frac{EI_{yz}}{R_{z}} &  M_{yy} &= \frac{EI_{yy}}{R_{z}} + \frac{EI_{yz}}{R_{y}} \end{align*}$$
>> where:
>> $M_{zz},M_{yy}=$ bending moments acting in xz and xy planes respectively
>> $I_{yy}, I_{zz}=$ [[second moment of area|2nd moment of area]]
>> $I_{yz}=$ second moment of area along yz?
>> $\sigma_{xx}=$ axial stress at some point on the beam cross section
>> $R_{y},R_{z}=$ [[Deflection in beams notes|radius of beam delfection]] in 
>> ![[Pasted image 20230219124240.png]]

Note sometimes $I_{z}$ will be used instead of $I_{zz}$ for [[second moment of area]] in the lecture notes, I'm using the same notation that was used last year. (same for $M_{zz}$ and $M_{z}$)

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