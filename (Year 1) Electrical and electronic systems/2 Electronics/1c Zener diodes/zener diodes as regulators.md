---
aliases: ["zener diodes as limiters"]
tags: ["Question","QFormat3"]
---

#### How can we use
## Zener diodes as regulators
![[Pasted image 20211219100304.png]]

If we think back to [[Kirchov's voltage law]], and how [[zener diodes]] have a maximum voltage they cannot exceed. Then $V_Z$ cannot exceed the max voltage across the [[zener diodes|zener diode]], making it very useful as a voltage regulator.

The resistor $R_S$ will regulate the current, which regulates the current for $R_L$ protecting it from excessive currents as well. We can easily calculate the value of $R_S$ for a particular required diode current and particular load current.

> ### $$ R_S = \frac{V_{in}-V_{Z}}{I_{load}+I_Z} $$ 
>> where:
>> $R_S=$ Required resistance 
>> $V_{in}=$ Input voltage
>> $V_Z=$ voltage across $R_L$ (same as across diode)
>> $I_{load}=$ Load current (current through $R_L$)
>> $I_Z=$ Current through diode (usually about 5mA)