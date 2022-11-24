---
aliases: ["free space loss","equivalent isotropic radiated power","EIRP","gain noise ratio"]
tags: []
---

## Calculating communication link strength
### Equation
To calculate the strength of a received signal we need to know the receiver's area, the transmitters [[antenna gain|gain]] and the distance between them:
![[Pasted image 20221123233952.png]]

> ### $$ \frac{C}{N_{0}}  = P_{T}G_{T} \left(\frac{ G_{R} }{k_{B}T_{R}} \right)\left(\frac{ 1 }{ L_{FS} L_{A} }  \right) $$ 
> ### $$ L_{FS}  = \left(\frac{4\pi\rho}{\lambda}\right)^{2} $$ 
>> where:
>> $C=$ carrier power
>> $P_{T}=$ signal power transmitted
>> $G_T =$ transmitter [[antenna gain|gain]]
>> $G_R =$ receiver [[antenna gain|gain]]
>> $T_{R}=$ [[communications signal noise#^a7d099|transmitter equivalent noise temp]]
>> $L_{FS}=$ free space loss
>> $\lambda=$ operating wavelength
>> $\rho=$ distance between transmitter and receiver ([[emphesis on it being a stupid symbol|with a stupid symbol]])
>> $N_{0}=$ [[communications signal noise|noise density]]
>> $k_{B}=$ [[Boltzmann constant]]

The [[the decibel|dB]] form of this equation is:
> ### $$\begin{align*}  10\log_{10}\left( \frac{C}{N_{0}} \right) &= 10\left[\log_{10}( P_{T} G_{T} ) + \log_{10}\left( \frac{G_{R}}{T_{R}} \right) - \log_{10} (L_{A}k_{B}) \right] - 20 \log_{10}\left( \frac{4\pi\rho}{\lambda} \right) \end{align*}$$
> ![[Pasted image 20221124001943.png]]

### Notable related quanitities

#### Equivalent isotropic radiated power (EIRP)
If the transmitter were replaced by an isotropic radiator, the EIRP would be the power required by the isotropic radiator to achieve the same power flux at the receiver as the original transmitter.

> ### $$\begin{align*} EIRP &= P_{T}G_{T}  \end{align*}$$

#### Receiver $G/T$ ratio

This is a measure of the sensitivity of the receiver – it can be shown to be directly proportional to the $C/N_0$ ratio:
$$ \frac{G_{R}}{T_{R}} \propto \frac{C}{N_{0}} $$

### Equation derivation
We can get the transmitted signels power flux by using the equation of a [[isotropic and high gain antenna|isotropic antenna]] transmission at distance $\rho$ and multiplying it by the [[antenna gain|gain]] of the trasnmitter:
$$\begin{align*}
\phi_{isotropic} &= \frac{P_{T}}{4\pi\rho^{2}} & &\to & \phi &= \frac{P_{T} G_{T}}{4\pi\rho^{2}}
\end{align*}$$
(The equation for isotropic transmitters just power/area of sphere, also [[like it is such a bad choice of symbol but I want to be consistant with the slides|wtf]] is $\rho$ being used for distance)

Then we can multiply the flux by the effective receiver area $A_{Reff}$ to get the power received:

$$ P_{R} = \frac{ P_{T} G_{T}}{4\pi\rho^{2}} A_{reff}  $$

This can be expanded further by subbing in the equation for effective area, which is the same as [[antenna gain#^f6b5c0|this equation]] resulting in:

$$\begin{align*}
P_{R} &=  \frac{ P_{T} G_{T}}{4\pi\rho^{2}} \left( \frac{G_{R}\lambda^{2}}{4\pi} \right)\\
&& L_{FS} &= \left(\frac{4\pi\rho}{\lambda}\right)^{2}\\
P_{R} &=  \frac{ P_{T} G_{T}G_{R}}{ L_{FS} }   \\
\end{align*}$$
Here $L_{FS}$ is a convenient term that can be used to represent the loss from travel, known as free space loss. But so far we have assumed no other soruces of interference, if we assume there are losses due to atmospheric absorbtion, precipitation, circuit losses ect then represent them using $L_{A}$:
$$ P_{R}  =  \frac{ P_{T} G_{T}G_{R}}{ L_{FS} L_{A} } $$
But it keeps going! We can account for the effect of [[communications signal noise|noise]] by using the equation of [[communications signal noise#Noise density ($N_{0}$)|noise density]]:
$$ \frac{P_{R}}{N_{0}}  =  \frac{ P_{T} G_{T}G_{R}}{ L_{FS} L_{A} } \frac{1}{k_{B}T_{R}} $$

Also for we replace $P_{R}$ with carrier power ($P_{R}\equiv C$) since the power of the received signal is literally the same as the power of the carrier wave that is received, [[really cramming it all in there huh|finally]] we are done:
$$ \frac{C}{N_{0}}  = P_{T}G_{T} \left(\frac{ G_{R} }{k_{B}T_{R}} \right)\left(\frac{ 1 }{ L_{FS} L_{A} }  \right) $$ 
