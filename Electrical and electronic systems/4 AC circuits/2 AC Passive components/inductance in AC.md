---
aliases: ["inductive impedance"]
tags: ["Question","QFormat3"]
---

#### How do we deal with
## Inductance in AC
### Equation bit
#### Inductive [[impedance]] ($Z_{L}$)

> ### $$ Z_{L} = j \omega L $$ 
>> where:
>> $Z_{L}=$ [[inductance in AC|inductive reactance]] 
>> $j=\sqrt{-1}$ 
>> $\omega=$ [[AC angular frequency]]
>> $L=$ [[inductance]]

^ffad83

#### For a pure circuit
![[Pasted image 20220428112758.png]]

What you will notice is that inductance is offset by 90 degrees:

> ### $$ V = -L I_{p} \omega\sin(\omega t + \phi ) = L I_{p} \omega \cos( \omega t + \phi + 90 \degree ) $$ 
> ### $$ V = I \times j \omega L  $$
> ### $$ V = \omega L (I_{p} \angle 90) $$
>> where:
>> $V=$ Potential difference across component
>> $I_{p}=$ peak current
>> $L=$ [[inductance]]
>> $\omega=$ [[AC angular frequency]]
>> $t=$ time
>> $\phi=$ time offset
>> $j=\sqrt{-1}$
>> $\angle$ is from [[phasor representation]]

![[Pasted image 20220428110539.png]]

The effect of inductance in AC is proportional to angular frequency, so at high frequencies inductance becomes a large factor. It's also 90 degrees out of phase of [[resistance in AC|resistor impedance]] so yeah, funky.

### Theory
We know the equation for [[complex numbers for representing AC|AC with complex numbers]] and [[inductor#^52f189|an inductor]] so:

$$\begin{align*}
 V &= L \frac{di}{dt} & i &= I_{p}\cos(\omega t + \phi )\\
&= L \frac{dI_{p}\cos(\omega t + \phi )}{dt}\\
&= L \frac{d}{dt}I_{p}\cos(\omega t + \phi )\\
&= -L I_{p} \omega\sin(\omega t + \phi )\\
\end{align*}$$
