---
aliases: ["gain"]
tags: []
---

## Antenna gain
### Description
In a transmitting antenna, the gain describes how well the antenna converts input power into radio waves headed in a specified direction. 
In a receiving antenna, the gain describes how well the antenna converts radio waves arriving from a specified direction into electrical power. 
When no direction is specified, gain is understood to refer to the peak value of the gain.

#### Numerical value

> ### $$ G = \frac{\text{maximum power flux}}{\text{power flux of an isotropic radiator}} $$ 
> ### $$ G = \frac{4\pi A_{eff}}{\lambda^{2}} = \frac{4\pi A}{\lambda^{2}} \eta $$ 
>> where:
>> $G=$ [[antenna gain]]
>> $\lambda=$ operating wavelength of dish
>> $A_{eff}=$ [[effective and projected aperture area|effective aperture area]]
>> $A=$ [[effective and projected aperture area|projected aperture area]]
>> $eta=$ [[effective and projected aperture area|aperture efficiency]] (generally in the range $0.4\to0.8$)

^f6b5c0

For a parabolic antenna of diameter $D$ the equation becomes:
> ### $$ G = \eta \left(\frac{\pi D}{\lambda}\right)^{2} $$
If not given you can usually approximate $\eta$ as about $\eta\approx0.65$

### Maximising gain
If your transmitting in all directions equally ([[isotropic and high gain antenna|isotropic antenna]]) then clearly as you get away from the transmission point the signal strength decrease by distance squared since that signal is covering a the surface of a 2D sphere. 
To increase gain you therefore just concentrate the signal in a single direction instead, aka a [[isotropic and high gain antenna|high gain antenna]]. The more the transmission is concentrated in a single direction the higher the gain. Of course the trade off is the transmitter needs to have increased pointing precision the more concentrated the transmission direction is.
