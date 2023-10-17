---
aliases: [""]
tags: []
---

## Effect of temperature on solar panel output

### Current, voltage effect

![[Pasted image 20231016083024.png]]

It can be seen that increasing temperature has a significant effect on both the current and voltage out of a solar cell. Where increasing temperatures:
- Significantly decrease voltage output
- Slightly increase current output
- Decrease potential max power

This can be modelled using the following:

> ### $$\begin{align*} I_{sc}  &= I_{0} + \alpha \Delta T  \end{align*}$$
> ### $$\begin{align*} V_{oc}  &= V_{0} + \beta \Delta T  \end{align*}$$
>> where:
>> $I_{sc}=$ [[solar cell terms|cell short circuit current]] at target temp
>> $V_{oc}=$ [[solar cell terms|cell open circuit voltage]] at target temp
>> $I_{0}=$ [[solar cell terms|cell short circuit current]] at reference temp
>> $V_{0}=$ [[solar cell terms|cell open circuit voltage]] at reference temp
>> $\alpha=$ temperature coefficient for current
>> $\beta=$ temperature coefficient for voltage
>> $\Delta T=$ difference from reference to target temp

Generally $\alpha$ and $\beta$ are given by the manufacturer, a common reference temperature is 21C

### Power

![[Pasted image 20231016084317.png]]

As discussed previously power output decreases with higher temps, this also means that by cooling your cells power output can be increased. This becomes a difficult balancing act as more incident light correspondingly means more subsequent heating. 

### Relationship with eclipses

The increased power output at low temps can lead to a useful effect:

![[Pasted image 20231016084636.png]]

As a spacecraft enters an eclipse it experiences a drop in temperature as the heating effects of the sun are eliminated. This means that once the craft exits the eclipse it experiences above typical power output aiding it in recharging it's batteries quickly.

