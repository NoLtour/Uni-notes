---
aliases: ["choked flow","critical area","converging diverging nozzle"]
tags: []
---

## Converging diverging nozzles

(Should have been in [[Propulsion overview]])

### Supersonic [[my use of technical terms is legendary|fuckary]]

The main reason why supersonic flows are so useful is this equation:

> ### $$\begin{align*} \frac{dA}{A}  &= (M^{2} - 1) \frac{dV}{V} \end{align*}$$
> ### $$\begin{align*} \frac{dA}{dx}  &= \frac{dV}{dx} \frac{A}{V}(M^{2}-1) \end{align*}$$
>> where:
>> $A=$ cross sectional area
>> $M=$ Mach number
>> $V=$ Velocity
>> $x=$ position along nozzle

So if we break down the implications of the equation when Mach is less than 1, it tells us that for subsonic flows velocity decreases with area increase. This is consistent with everything studied in year 1 and 2.

But the moment Mach number exceeds 1 we get something truly insane, increased area leads to increasing flow speed. This process gives us a mechanism to convert pressure and temperature into velocity which is an incredibly useful form of energy! Opening up a huge realm of [[hell yeah fuck entropy|possibilities]], a critical one being the converging diverging nozzle.

![[Pasted image 20231027182738.png]]

### The nozzle

![[Pasted image 20230402145155.png]]

- If the conditions of the nozzle are such that the flow can reach Mach 1 at or before the throat then the flow will be choked AT the throat (where it is at mach 1)
- This is because a subsonic flow will accelerate in a converging nozzle
- When it exceeds Mach 1 it will become a supersonic flow, hence it will decelerate in a converging nozzle... making it subsonic
- It can be seen that regardless of ability to reach supersonic flow before the throat it will be stuck at Mach 1 for the duration of the converging region.

A direct consequence of this is "choked flow", since the maximum Mach number achievable in the throat is 1 this places a hard limit on mass throughput, such that:
$$\begin{align*}
\dot{m} &= A \rho V & &\to & \dot{m} &= A \rho M \sqrt{ \gamma R T}& \dot{m} &= A \rho \sqrt{ \gamma R T}
\end{align*}$$

Looking at this equation we can see that the ONLY way to increase throughput is increasing:
- Cross section
- Temperature
- Density

This also implies that downstream conditions doesn't effect throughput (so long as Mach 1 is reached), which makes sense when you consider that information cannot back propagate in a supersonic flow.

#### Choked flow equation

Taking that working and doing further magic will yield:

> ### $$\begin{align*} \frac{A}{A*}  &= \frac{1}{M} \left[ \frac{2}{\gamma+1} \left(1+ \frac{\gamma-1}{2} M^{2}\right) \right]^{\frac{\gamma+1}{2(\gamma-1)}} \end{align*}$$
>> where:
>> $A=$ Area at some point
>> $A*=$ critical area (area at nozzle throat)
>> $M=$ Mach number at some point
>> $\gamma=$ [[specific heat ratio]]

Plotting this equation would result in:
![[Pasted image 20231027184327.png]]

Which makes sense:
- At 1,1 Mach number is 1 (as expected at the throat) and area is the critical area
- For any area there are 2 possible Mach numbers, one corresponding to a subsonic and one to a supersonic regime. Expected considering the nature of a converging diverging nozzle.

Note there is also the [[mass flowrate through a choked nozzle]].

#### Pressure change

As discussed previously, we sacrifice pressure and temperature for velocity. When charted it looks like:

![[Pasted image 20231027184547.png]]

