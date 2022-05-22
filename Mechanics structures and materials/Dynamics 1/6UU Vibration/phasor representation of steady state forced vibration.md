---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Describe
## Phasor representation of steady state forced vibration
### Intro
Yes this is the same thing as [[phasor representation]] covered in AC, but instead we use it for oscillating systems. We use the following format when representing [[phasor representation|phasors]]:
![[phasor representation#^93ff19]]

### Phasors for vibration
Basically phasors are used to relate a input (driving force) to the oscillation:
![[Pasted image 20220522184420.png]]

As long as the frequency of the input is a single constant value then you can represent the relationship between the driving force and output displacement as a frequency response function of the form $\frac{X}{F}$, in steady state this value is constant and represents the transformation that maps the input force onto the displacement as can be seen below:
![[Pasted image 20220522184721.png]]

> ### $$ x(t) = Re: (Xe^{j\omega t}) $$ 
> ### $$ X = |X|e^{j\phi} = |X|\angle \phi $$
> ### $$$$
> ### $$ f(t) = F\times Re: ( e^{j\omega t} ) $$
> ### $$ F = Re: F $$
>> where:
>> $x(t)=$ the function that describes displacement relative to time
>> $f(t)=$ the function that describes driving force relative to time
>> $F=$ amplitude of driving force (completely real)
>> $X=$ complex number representing displacement (displacement [[phasor representation|phasor]])

In a system with some oscillating mass such as the following:
![[Pasted image 20220522185212.png]]

We can sum up the forces on the free body diagram:
$$\begin{align*}
m \ddot{x} + c\dot{x} + kx &= Fe^{j\omega t}
\end{align*}$$
Since it's a steady state we can also assume that $x(t) = Xe^{j\omega t}$:
$$\begin{align*}
x &= Xe^{j\omega t} \\
\dot{x} &= j\omega Xe^{j\omega t} \\
\ddot{x} &= -\omega^{2}Xe^{j\omega t} & m \ddot{x} + c\dot{x} + kx &= Fe^{j\omega t}\\
& & -m\omega^{2}Xe^{j\omega t} + c j\omega Xe^{j\omega t} + kXe^{j\omega t} &= Fe^{j\omega t} \\
& & (-m\omega^{2} + c j\omega  + k) X &= F \\
& &  \frac{X}{F} &= \frac{1}{-\omega^{2}m + j \omega c + k} \\
\end{align*}$$

Hence we have a function describing the relationship between a driven damped oscillator and displacement:

> ### $$ \frac{X}{F} = \frac{1}{-\omega^{2}m + j \omega c + k} $$ 
>> where:
>> $X=$ Displacement [[phasor representation|phasor]]
>> $F=$ Force amplitude
>> $m=$ mass of oscillating object
>> $c=$ [[damping coefficient]]
>> $k=$ [[spring constant]]
>> $j=\sqrt{-1}$

^c82636

This is the general form of the equation but in most use cases a single value dominates the equation so the equation gets simplified.

### Stiffness, damping and mass controlled oscillation

![[stiffness, damping and mass controlled oscillation#Stiffness damping and mass controlled oscillation]]
