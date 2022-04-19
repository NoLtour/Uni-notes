---
aliases: ["operational amplifiers","op amp", "op amps"]
tags: ["Question","QFormat3"]
---

#### What is a
## Operational amplifier
### Basic function
These are components that take two inputs and outputs a value equivilent to:
> ### $$ V_{out} = ( V_{+} - V_{-}) \times A_{OL} $$ 
>> where:
>> $V^{+}_{cc} - k > V_{out} > V^{-}_{cc} + k$ 
>> $V_{out}=$ voltage at inverting input
>> $V_{+}=$ voltage at non inverting input
>> $V^{+}_{cc} , V^{-}_{cc}=$ supply voltages
>> $k=$ minimum difference between output voltage and supplys
>> $A_{OL}=$ amplification factor

The layout can be seen on the following diagram.

![[Pasted image 20220419142120.png]]

### Generating square waves

Basically what this means is that the output is proportional to the difference between $V_{+}$ and $V_{-}$ multiplied by the amplification factor but then capped between the supply voltages. Since the amplification factor is often measured in the millions tiny differences in the inputs will usually just resault in a value equivilent to $V_{cc}^{+}-1$ or $V_{cc}^{-}+1$ hence you get a square wave:
![[Pasted image 20220419142522.png]]
As you can see the exact value of $A_{OL}$ doesn't really matter since any super high value gets basically the same output. Also in the example above if you flip the two inputs then the square wave would be 180 degrees out of phase with the input (because the input would be in the inverting input (hence the name)).

Of couse the square waves transition between $V_{max}$ and $V_{min}$ isn't actually instantanious, but it's so sudden it approximates extreemly well as a square wave.

