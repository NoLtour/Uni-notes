---
aliases: ["effect of current/voltage draw on solar efficiency","effect of temperature on solar efficiency","effect of sun angle on solar efficiency","effect of radiation degredation on solar efficiency"]
tags: []
---

## Maximising solar power out
### Example cell material characterisitics
[[real shocker here huh|As you'd expect]] the choice of cell material greatly effects pretty much all properties of a solar cell:
![[Pasted image 20221123130431.png]]
So material selection can vary greatly depending on environmental conditions and payload power requirements.

### Effect of conditions
#### Current/Voltage draw
Turns out that the power output of a solar cell actually changes depending on the voltage/current across it:
![[Pasted image 20221123124727.png]]

For a typical silicon cell operating at 30C with [[solar flux]] ~$1400W/m^{2}$ it'll have:
- Open circuit voltage $V_{oc}\approx 0.55V$
- Short circuit current $I_{sc}\approx 35mA/cm^{2}$
- Open circuit voltage $P_{max}\approx 14mW/cm^{2}$

To achieve maximum power output there will usually be a power management system which ensures the voltage/current across the cell maximises power. In the case where it is not operating at maximum efficiency the extra energy is lost as heat, for situations of excess power this is sometimes done intentionally.

#### Temperature effect
The IV curve changes depending on temperature:
![[Pasted image 20221123125229.png]]

But basically it boils down to, a higher temperature reduces power out so you want as low a temperature as possible. 

#### Sun angle effect
Of course if you angle the panel less light actually hits it, but that is not the only thing reducing efficiency when off angle; the greater incidence angle leads to additional energy losses even for the reduced amount of light that reaches the cell:
![[Pasted image 20221123125605.png]]
This can be approximated using $\cos$.

#### Radiation
Exposure to radiation damages the cell reducing it's efficiency, of course in space the amount of high energy radiation hitting the cell is much greater than on earth so it's a much bigger issue for satellites:

![[Pasted image 20221123125909.png]]

(General beggining of live vs end of life I/V curves for some solar cell)

Reducing effect of radiation:
- Increase thickness of protective glass
- Use N-type semiconductor on exposed parts to reduce damage

Using information about the environment conditions for the course of the mission and the behaviour of the material it is possible to get resonable estimates for most end of life conditions for the solar cells as a consequence of radiation damage.