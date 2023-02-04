---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Calculating the deflection of a beam
### Useful bits
We use the same assumptions as those from [[deformation due to bending in beams#Assumptions]] which are also used for [[engineer's bending theory]].

When we measure deflection we take it in respect to the origional strait beam's position, with downwards deflections being negative.

> ### $$ M = -EI \frac{d^{2}v}{dx^{2}} $$ 
> ### $$ v = -\frac{1}{EI} \left(\int \left(\int M \cdot dx\right) \cdot dx\right)$$
>> where:
>> $M=$ Moment 
>> $E=$ [[youngs modulus]]
>> $I=$ [[second moment of area]] 
>> $v=$ Displacement from strait position
>> $x=$ Distance along the beam

### Proof
Since we are modelling under the same assumptions as those for [[engineer's bending theory]], we can assume the distance to the [[neutral surface and neutral axis|neutral axis]] of the beam is $R$:

![[Pasted image 20211122105413.png]]

This also means we can define deflection ($v$) as a function of $x$ hence $v(x)$.

Ok so since we are modelling the beam as a circular arc, it can be drawn as the following:
![[Pasted image 20211122110014.png]]

Since the circular arc is assumed to be very large, we can say that $ds \approx dx$.
We also know that $\tan \theta = \frac{dv}{dx} \approx \theta$.
And since $ds$ is the base of a right angled triangle $ds\approx R d\theta$

$$\begin{align*}
   && \frac{dv}{dx} &= \theta & ds &= dx & ds &= R d\theta\\
&& \frac{d^{2}v}{dx^{2}} &= d\theta & & & \frac{1}{R} &= \frac{d\theta}{ds} \\
\frac{1}{R} &= \pm \frac{d\theta}{ds} = \pm \frac{d^{2}v}{dx^{2}}\\
\end{align*}$$
(to be honest I'm not really sure how we get that? This is what the notes say and they don't really explain so that's just great huh)
The sign depends on convention used.

We can recall from [[engineer's bending theory]] that:
![[engineer's bending theory#^6fb9ef]]

We can use this with the equation we worked out previously:

$$\begin{align*}
    \frac{1}{R} &= \frac{M}{EI} & \frac{1}{R} &= -\frac{d^{2}v}{dx^{2}}\\
-\frac{d^{2}v}{dx^{2}} &= \frac{M}{EI}\\
\therefore M &= -EI \frac{d^{2}v}{dx^{2}}
\end{align*}$$

#### Integration time
This equation isn't all that useful, so we use [[MEE Intergration 1|Intergration]], yay!

$$\begin{align*}
  M &= -EI \frac{d^{2}v}{dx^{2}}\\
-\frac{1}{EI}\int M \cdot dx &= \frac{dv}{dx} \\
-\frac{1}{EI} \left(\int \left(\int M \cdot dx\right) \cdot dx\right) &= v
\end{align*}$$

Note that as a resault of the integration you will get 2 constants added as $+ax+b$.