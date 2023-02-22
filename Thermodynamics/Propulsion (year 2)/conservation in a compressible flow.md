---
aliases: ["equations of conservation in a compressible flow"]
tags: []
---

## Conservation in a compressible flow

K there is some complex shite in the notes, but since it's a derivation with complex unexplained equations I'm not bothering (we don't need to know it anyway). The gist is that after applying a few assumptions we will get:

> ### $$\begin{align*} \text{Mass conservation:}&&\frac{d}{dx} (\rho U) &= 0\\\\ \text{Momentum conservation:}&&U \frac{dU}{dx} + \frac{1}{\rho} \frac{dP}{dx} &= 0\\\\ \text{Energy conservation:}&&\frac{dh}{dx} + U \frac{dU}{dx} &= 0\\\\ \text{Equation of state:}&&P &= \rho R T \end{align*}$$
>> where:
>> $U=$ velocity
>> $\rho=$ fluid density (not constant)
>> $x=$ position
>> $h=$ specific [[enthalpy]]
>> $R=$ [[individual gas constant|specific gas constant]]
>> $T=$ fluid temperature
>> $P=$ pressure
>
>> assumptions:
>> - One dimensional flow
>> - [[steady flow|Steady flow]]
>> - [[inviscid flow|Inviscid flow]]
>> - No thermal diffusion (no change in heat distrobution)
>> - No viscous heating (from [[inviscid flow]])

Although 1D equations seem kinda worthless, we can do what is essentially [[Bernouillis equation]] with extra steps, to get a better [[Bernouillis equation]].