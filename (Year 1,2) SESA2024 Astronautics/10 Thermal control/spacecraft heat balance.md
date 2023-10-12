---
aliases: ["heating due to direct solar radiation","direct solar radiation","heating due to albedo of significant nearby objects","heating due to nearby object thermal emission","spacecraft thermal emission","heating due to components"]
tags: []
---

## Spacecraft heat balance

### Thermal balance equation

For a real spacecraft the heat balance would have to be calculated on a small area scale since things like [[total radiation absorption transmittance and reflectance|absorptance]], [[real body emission|emittance]] ect vary based on the material which is not constant at different points on the craft. However if we choose to just assume these measures are uniform across the craft as well as tones of others we can use the following balance equation:

> ### $$\begin{align*} Q_{SC}  &= Q_{S} + Q_{a} + Q_{E} + Q_{dis}  \end{align*}$$
>> where:
>> $Q_{SC}=$ [[spacecraft heat balance#Spacecraft thermal emission|spacecraft thermal emission]]
>> $Q_{S}=$ [[spacecraft heat balance#Direct solar radiation|heating from direct solar radiation]]
>> $Q_{a}=$ [[spacecraft heat balance#Albedo of significant nearby objects|heating due to albedo of significant nearby objects]]
>> $Q_{E}=$ [[spacecraft heat balance#Thermal emission of significant nearby objects|heating due to nearby object thermal emission]]
>> $Q_{dis}=$ [[spacecraft heat balance#Components|heating due to components]]

For the above if you still want to use it for a spacecraft with varying things like [[real body emission|emittance]] then you'll need to calculate surface average emittance, the same goes for things like [[total radiation absorption transmittance and reflectance|absorptance]].

By expanding this equation we can get the following forms:

> ### $$\begin{align*} \varepsilon \sigma T^{4} A_{surf}  &= q_{S}\: \alpha_{S}\: A_{S}^{proj} + a\: q_{S} \: \alpha_{S}\: A_{E}^{proj} \: \cos (\phi) \: \beta F +  q_{E} \: \varepsilon \: A_{E}^{proj} \: F + P  \end{align*}$$
> ### $$\begin{align*} \sigma T^{4} &= q_{S} \frac{\alpha_{S}}{\varepsilon} \left( \frac{A_{S}^{proj}}{A_{surf}} + a \frac{A^{proj}_{E}}{A_{surf}} \cos(\phi)\:\beta F \right) + q_{E} \frac{A_{E}^{proj}}{A_{surf}} F + \frac{P}{\varepsilon A_{surf}} \end{align*}$$
>> where: 
>> $\sigma=$ [[Stefan-Boltzmann constant]]
>> $a=$ albedo of object, for earth $=0.34$
>> $q_{S}=$ power per unit area of heating from the sun, near the earth $\approx 1350\:Wm^{-2}$
>> $q_{E}=$ thermal emission of planet due to it's temperature, the earth has a $q_{E}=240\:Wm^{-2}$ 
>> $A_{E}^{proj}=$ projected area of spacecraft relative to planet 
>> $A_{S}^{proj}=$ The projected area of the spacecraft relative to the sun (changes with vehicle orientation)
>> $A_{surf}=$ surface area of spacecraft
>> $P=$ power of heating due to components 
>> $T=$ temperature of spacecraft
>> $\phi=$ angle between the sun vector of the planet and the vector towards the vehicle
>> $\beta=\begin{dcases} 1, & -90\degree < \phi < 90\degree \\ 0, &\text{else} \end{dcases}=$  This is essentially a logic function to switch $Q_{a}$ to zero in the event the spacecraft is no longer in front of the planet (aka in eclipse)
>> $\alpha_{S}=$ [[total radiation absorption transmittance and reflectance|solar absorptance]] for the material
>> $\alpha=$ [[total radiation absorption transmittance and reflectance|absorptance]] of spacecraft
>> $\varepsilon=$  [[real body emission|emittance]]
>> $F=\left(\frac{R_{E}}{R_{orb}}\right)^{2}=$ a variable describing intensity reduction due to inverse square law
>> $R_E =$ radius of planet (I THINK, NOT SURE)
>> $R_{orb} =$ separation between craft and surface? (I THINK, NOT SURE) 
>> 
>> Note this form of the equation is assuming that the spacecraft is in orbit of earth and has an operating temperature around $290K$

^7c6936

### Heat inputs and outputs

#### Direct solar radiation

This is the heating caused directly by the radiation from the sun hitting the spacecraft. The equation's pretty obvious, multiply the area facing the sun by the solar power per area and then by [[total radiation absorption transmittance and reflectance|absorptance]] to get total solar radiation heating:

> ### $$\begin{align*} Q_{S}  &= q_{S}\: \alpha_{S}\: A_{S}^{proj}  \end{align*}$$
>> where:
>> $Q_{S}=$ Direct solar radiation
>> $q_{S}=$ power per unit area of heating from the sun, near the earth $\approx 1350\:Wm^{-2}$
>> $A_{S}^{proj}=$ The projected area of the spacecraft relative to the sun (changes with vehicle orientation)
>> $\alpha_{S}=$ [[total radiation absorption transmittance and reflectance|solar absorptance]] for the material

#### Albedo of significant nearby objects

This is the heating caused by the radiation reflected off nearby significant bodies, most often we're talking about the earth's albedo.

> ### $$\begin{align*} Q_{a}  &= a\: q_{S} \: \alpha_{S}\: A_{E}^{proj} \: \cos (\phi) \: \beta F  \end{align*}$$
>  ### $$\begin{align*} F &= \left(\frac{R_{E}}{R_{orb}}\right)^{2}  \end{align*}$$
>> where:
>> $Q_{a}=$ Heating due to albedo
>> $a=$ albedo of object, for earth $=0.34$
>> $q_{S}=$ power per unit area of heating from the sun, near the earth $\approx 1350\:Wm^{-2}$
>> $\alpha_{S}=$ [[total radiation absorption transmittance and reflectance|solar absorptance]] for the material
>> $A_{E}^{proj}=$ projected area of spacecraft relative to object
>> $\phi=$ angle between the sun vector of the object and the vector towards the vehicle
>> $\beta=\begin{dcases} 1, & -90\degree < \phi < 90\degree \\ 0, &\text{else} \end{dcases}=$  This is essentially a logic function to switch $Q_{a}$ to zero in the event the spacecraft is no longer in front of the planet (aka in eclipse)
>> $F=\left(\frac{R_{E}}{R_{orb}}\right)^{2}=$ a variable describing intensity reduction due to inverse square law
>> $R_E =$ radius of body (I THINK, NOT SURE)
>> $R_{orb} =$ separation between craft and surface? (I THINK, NOT SURE)
>> 
>
>![[Pasted image 20221230172501.png]]

Note that this equation is very much a approximation, for instance $\beta$ clearly only works for small orbits and does not account for the effect of atmospheric light scattering.

#### Thermal emission of significant nearby objects

This is the heat that was radiated by significant nearby hot objects that was absorbed by the spacecraft.

> ### $$\begin{align*}\text{general case:}&& Q_{E}  &= q_{E} \: \alpha \: A_{E}^{proj} \: F\\\\\text{Earth(ish) case:}&& Q_{E}  &= q_{E} \: \varepsilon \: A_{E}^{proj} \: F \end{align*}$$
>> where:
>> $q_{E}=$ thermal emission of object due to it's temperature, the earth has a $q_{E}=240\:Wm^{-2}$
>> $\alpha=$ [[total radiation absorption transmittance and reflectance|absorptance]] of spacecraft
>> $\varepsilon=$  [[real body emission|emittance]]
>> $A_{E}^{proj}=$ projected area of spacecraft relative to object
>> $F=\left(\frac{R_{E}}{R_{orb}}\right)^{2}=$ a variable describing intensity reduction due to inverse square law
>> $R_E =$ radius of body (I THINK, NOT SURE)
>> $R_{orb} =$ separation between craft and surface? (I THINK, NOT SURE)
>
>Note on earth(ish): Since typical spacecraft operational temperature is about 290K which is similar to the earths temperature we can apply [[finish this link|Kirchoff's Law]], which means that for typical spacecraft in orbit of earth $\alpha=\varepsilon$ 

#### Components

This is the heat produced by the components of the spacecraft. There isn't an equation for this since it's really dependent of spacecraft configuration, the symbol is $Q_{dis}$. Guess we can do:

> ### $$\begin{align*} Q_{dis}  &= P  \end{align*}$$
>> where:
>> $Q_{dis}=$ heating due to components
>> $P=$ power of heating due to components
>> 
>> I present to you the most [[really just so pointless like why|pointless equation]] in the universe! Why dies this exist? Who knows!

#### Spacecraft thermal emission

The only way we actually cool down the fucking thing, the radiation emission of the body:

> ### $$\begin{align*} Q_{SC}  &= \varepsilon \sigma T^{4} A_{surf}  \end{align*}$$
>> where:
>> $Q_{SC}=$ heat emitted as radiation
>> $\varepsilon=$  [[real body emission|emittance]]
>> $T=$ temperature of spacecraft
>> $\sigma=$ [[Stefan-Boltzmann constant]]
>> $A_{surf}=$ surface area
