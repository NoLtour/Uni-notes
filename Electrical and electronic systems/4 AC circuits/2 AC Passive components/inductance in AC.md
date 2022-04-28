---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### How do we deal with
## Inductance in AC
### Equation bit
What you will notice is that inductance is offset by 90 degrees:

> ### $$ V = -L I_{p} \omega\sin(\omega t + \phi ) = L I_{p} \omega \cos( \omega t + \phi + 90 \degree ) $$ 
> ### $$ V = I \times j \omega L \;\;\;\;\{\phi=0\} $$
> ### $$ V = \omega L (I_{p} \angle 90)  \;\;\;\;\{\phi=0\} $$
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

### Theory
We know the equation for [[complex numbers for representing AC|AC with complex numbers]] and [[inductor#^52f189|an inductor]] so:

$$\begin{align*}
 V &= L \frac{di}{dt} & i &= I_{p}\cos(\omega t + \phi )\\
&= L \frac{dI_{p}\cos(\omega t + \phi )}{dt}\\
&= L \frac{d}{dt}I_{p}\cos(\omega t + \phi )\\
&= -L I_{p} \omega\sin(\omega t + \phi )\\
\end{align*}$$
