---
aliases: ["Planks law","Wiens displacement law","total black body emission"]
tags: []
---

## Blackbody emission

### Planks law

All thing's radiate thermal radiation when above absolute zero, but generally modelling it is hard. For a[[black and grey bodies|black body]] the equations relatively simple though:

> ### $$\begin{align*} q_{\lambda}  &= \frac{2 \pi h c^{2}}{\lambda^{5} \left( e^{\frac{ch}{k\lambda T}} - 1 \right)}  \end{align*}$$
>> where:
>> $q_{\lambda}=$ [[blackbody emission]] (at wavelength $\lambda$), units $Wm^{-3}$
>> $h=$ [[Plank constant]]
>> $k=$ [[Boltzmann constant]]
>> $c=$ [[speed of light]]
>> $\lambda=$ wavelength being emitted units $m$

### Wiens displacement law


By plotting the equation from planks law we get a graph like the following:

![[Pasted image 20221230162613.png]]

Can see clearly that the emission increases with temperature, as you'd expect. If you look at the peak emission $q_{\lambda\:max}$ it occurs at lower wavelengths as temperature increases, call this peak emission wavelength $\lambda_{max}$. Wiens displacement law is simply an equation derived which relates $\lambda_{max}$ and temperature for a [[black and grey bodies|blackbody]]:

> ### $$\begin{align*} \lambda_{max} T  &= 2.898\times 10^{3} && (\mu m \: K) \\ \lambda_{max} T  &= 2.898 &&(m \: K)  \end{align*}$$
>> where:
>> $\lambda_{max}=$ the wavelength of highest [[blackbody emission]] for the given temperature
>> $T=$ the temperature of the black body

#### Application

Although real object's aren't black bodies they can often be approximated as such. For example:

> Earth's emission spectrum peaks at $\lambda=10\:\mu m$, estimate earth's surface temperature.

$$\begin{align*}
\lambda_{max} T  &= 2.898\times 10^{3} & &\to & T  &= \frac{2.898\times 10^{3}}{\lambda_{max}}\\
&&&& T_{earth} &\approx \frac{2.898\times 10^{3}}{10} = 289.8K
\end{align*}$$

Once you get a value of the temperature of an object you can then go back to [[blackbody emission|Planks law]] and create a reasonably accurate emission spectrum for the object!

### Total emission

To get total emission we just integrate using:

$$\begin{align*}
q_{BB} &= \int^{\infty}_{0} q_{\lambda} \: d\lambda\\
&=  \int^{\infty}_{0} \frac{2 \pi h c^{2}}{\lambda^{5} \left( e^{\frac{ch}{k\lambda T}} - 1 \right)} \: d\lambda\\
&...\\
q_{BB}&= \sigma T^{4}
\end{align*}$$

This is known as the Stefan-Boltzmann equation, where $\sigma$ is a constant:

> ### $$\begin{align*}  q_{BB}&= \sigma T^{4}  \end{align*}$$
>> where:
>> $q_{BB}=$ Total thermal radiation emission per unit area from a black body, units $Wm^{-2}$
>> $T=$ temperature of black body
>> $\sigma=$ [[Stefan-Boltzmann constant]]

