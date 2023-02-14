---
aliases: ["isentropic efficiency of a compressor"]
tags: []
---

## Isentropic efficiency
### Justification of lazyness
You know how we've been modelling lots of processes as ideal [[isentropic process|isentropic]] processes to clean up the maths? Well instead of doing a proper job and developing theory further to account for real world shite why not just take the tried and tested [[nerds try and figure out the truth of the universe we just need things to work lol|engineering approach]]... slapping in a constant to correct for error? Introducing: "Isentropic efficiency factor".

K so lets look at some [[TS diagram]]s to get an idea of what I mean, so the dotted line is realisting the black one is ideal:

![[Pasted image 20230213234517.png]]

See how irl [[entropy]] increases, we don't have a [[reversible and irreversible processes|reversible process]]. That is where slapping a constant in works.

### The slapping in variable ($\eta_{c}$), the compressor

> ### $$\begin{align*} \eta_{c}  &= \frac{\text{isentropic work input}}{\text{actual work input}} = \frac{w_{c,s}}{w_{c}} \end{align*}$$
> ### $$\begin{align*}\text{generic:}&& \eta_{c}  &= \frac{\text{isentropic work input}}{\text{actual work input}} = \frac{w_{c,s}}{w_{c}}\\\text{perfect gas:}&& \eta_{c}  &= \frac{T_{2,s}-T_{1}}{T_{2}-T_{1}} \end{align*}$$
>> where:
>> $\eta_{c}=$ [[isentropic efficiency|isentropic efficiency of a compressor]]
>> $w_{c,s}=$ real work input
>> $w_{c}=$ ideal work input
>> $T_{1}=$ temp into compressor
>> $T_{2}=$ ideal temp out of compressor (assuming [[isentropic process|isentropic]])
>> $T_{2,s}=$ real temp out

### The slapping in variable ($\eta_{t}$), the turbine

> ### $$\begin{align*}\text{generic:}&& \eta_{t}  &= \frac{\text{ actual work output}}{\text{isentropic work output}} = \frac{w_{t}}{w_{t,s}}\\\text{perfect gas:}&& \eta_{t}  &= \frac{T_{1}-T_{2}}{T_{1}-T_{2,s}} \end{align*}$$
>> where:
>> $\eta_{t}=$ [[isentropic efficiency|isentropic efficiency of a compressor]]
>> $w_{t,s}=$ real work output
>> $w_{t}=$ ideal work output
>> $T_{1}=$ temp into turbine
>> $T_{2}=$ ideal temp out of turbine (assuming [[isentropic process|isentropic]])
>> $T_{2,s}=$ real temp out

These equations can be used with [[SFEE simplifications for propulsion application]] to do calculations involving turbines.