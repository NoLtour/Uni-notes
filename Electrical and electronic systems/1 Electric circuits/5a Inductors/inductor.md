---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is an
## Inductor

This is a passive two terminal electrical component that stores energy in a magnetic field when an electric current is flowing through it. An inductor is generally an insulated witre wound into a coil.

Inductors generally stabalise current, this is because the magnetic field created "matches" the current flowing through it. So to change the current you need to apply a pd accross the inductor; [[inductor#^52f189|the pd is proportional to the rate of change of current]]. This applys to both increaseing and decreasing the current.

Inductors can be thought of as components that resist changes in [[electric current|current]].

![[Pasted image 20211107100602.png]]

### [[methath|Math]]

The [[magnetic flux]] in a coil can be found using:
> ### $$ N \varphi = Li $$ 
>> where:
>> $N=$ number of turns 
>> $\varphi=$ phase angle? (WHY DON'T PEOPLE LABEL EQUATIONS FFS)
>> $L=$ [[inductance]]
>> $i=$ current
Basically saying that the flux in a coil is proportional to the current flowing. (The first equation dosn't need to be remembered)

> ### $$ V = L \frac{di}{dt} $$ 
>> where:
>> $V=$ [[potential difference]] accross inductor
>> $L=$ Number of turns
>> $\frac{di}{dt}=$ rate of change of current

^52f189

This can be integrated to get:
> ### $$ I = \frac{V_{s}}{R} \left(1-e^{-\frac{tR}{L}}\right) $$ 
> ### $$ V_{L} = V_{s} e^{-\frac{tR}{L}} $$ 
>> where:
>> The inductor has a constant DC source and a purely resistive load
>> $=$ 
>> $=$
>> $=$

### Example
>> Plot the voltage across the inductor vs time for the following circuit:
>> ![[Pasted image 20211107102808.png]]
> 
> Its in series so we know $I=I_R=I_L$
> At t=0, I=0 sp according to [[Ohms law]] $V_R = 0$ 
> so $V_L=6-0=6$
> 
> using [[inductor#^52f189| this equation]]:
> ![[Pasted image 20211107103213.png]]
