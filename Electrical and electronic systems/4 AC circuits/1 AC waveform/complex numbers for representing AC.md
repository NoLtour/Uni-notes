---
aliases: ["AC with complex numbers"]
tags: ["Question","QFormat3"]
---

#### How can we use
## Complex numbers for representing AC
### Intro
So [[complex numbers]] are actually ideal for this, especially when dealing with sinasoidal waveforms, take the following equation:
![[representing complex numbers using angle and magnitude#^c3da45]]
Then by focusing on the real component we get a convenient way to represent the current voltage of some [[alternating current|AC]] source:
![[Pasted image 20220306132906.png]]

### Equations

So a equation that represents the current voltage of some sinasodal AC source can be written as:

> ### $$ V = V_{p}(\cos(\omega t + \phi ) + j\sin(\omega t + \phi )) = V_{p} e^{j(\omega t + \phi )} $$ 
> ### $$ Re: V = V_{p}\cos(\omega t + \phi ) = Re: V_{p} e^{j(\omega t + \phi )}  $$
>> where:
>> $V=$ current voltage 
>> $V_{p}=$ peak voltage
>> $\omega=$ [[AC angular frequency|angular frequency]]
>> $\phi=$ offset
>> $t=$ time
>> $j=\sqrt{-1}=$ [[complex numbers#^60fc2b|a cringy alternative to using i]] also [[the j|this]]

^ec50da

Of course the same thing goes for $I$:

> ### $$ I = I_{p}(\cos(\omega t + \phi ) $$ 
>> where:
>> $I=$ current current (ehehhe)
>> $I_{p}=$ peak current
>> $\omega=$ [[AC angular frequency|angular frequency]]
>> $\phi=$ offset
>> $t=$ time
>> Current and voltage are known to be in phase

