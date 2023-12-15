---
aliases: ["orbital coverage calculation variables"]
tags: []
---

## Calculating orbital coverage

Fundamental geometric relationships limit where on the surface of a sphere a point above that sphere can see, these relations can be easily derived:

> ![[Pasted image 20231201222915.png]]
> ![[Pasted image 20231201223027.png]]
> ### $$\begin{align*} E &= \frac{\pi}{2} -\theta  - \alpha  \end{align*}$$
> ### $$\begin{align*} R &= \frac{R_{E}\sin\alpha}{\sin \left( \frac{\pi}{2} - E - \alpha\right) }  \end{align*}$$
> ### $$\begin{align*} \cos\alpha_{max} &= \frac{R_{E}}{R_{E+H}} \end{align*}$$
> ### $$\begin{align*} \cos \alpha   &= \frac{R_{E}\cos E}{R_{E}+H} - E \end{align*}$$
> ### $$\begin{align*} B &= 2 \alpha R_{E}\end{align*}$$
>> where:
>> $H=$ orbital height 
>> $\theta=$ half antenna beam width
>> $\theta_{max}=$ half antenna beam width if $E=0$
>> $\beta=$ coverage area diameter
>> $\alpha=$ coverage angle
>> $\alpha_{max}=$ coverage angle if $E=0$
>> $E=$ spacecraft elevation angle at edge of coverage
>> $R=$ slant range at edge of coverage area
>> $R_{E}=$ earth radius

The reason we have a difference between the actual coverage and the max coverage is clearly $E$, this represents the "minimum slant" before we can usefully do stuff. For a transmitter and reviever it would be a combination of:
- Minimum slant needed to see the sky without obstructions (could be difficult if surrounded by tall structures)
- Signal density losses due to slope of the planet (normal component of signal reduces with larger $\theta$)
- Atmospheric effects, larger angle means longer in atmosphere travel and signal dissipation
