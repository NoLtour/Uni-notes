---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Phasor representation
### Intro
It is not very convenient to handle equation or waveforms for alternating quantities. An alternating quantity (current or voltage) is a vector quantity. Since the instantaneous values are continuously changing, it must be represented by a rotating vector or phasor. A vector is a phasor that is rotating at a constant angular velocity. The image shows that sinusoidal voltage or current can be represented by a Phasor Representation diagram.

![[Pasted image 20220428100034.png]]

Phaser representation is just a fancy way of saying "we represent AC with a rotating vector":
![[complex numbers for representing AC#^ec50da]]

### Convention
> ### $$ a ( \cos \theta + j\sin \theta ) = a \angle \theta $$ 
>> where:
>> $a=$ magnitude
>> $\theta=$ angle
>> $j=\sqrt{-1}$

### Representing voltage and current
We represent the root mean square voltage when working with phasor voltage:
![[Pasted image 20220509110434.png]]

The same goes for current, we generally represent root mean square current.

### Representing [[impedance]]
> ### $$ Z = R + jD = \sqrt{R^{2} + D^{2}} \angle \arctan \left( \frac{D}{R} \right) $$ 
>> where:
>> $Z=$ [[impedance]] 
>> $R=$ resistance
>> $D=$ [[electrical reactance|reactance]]