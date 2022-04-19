---
aliases: ["operational amplifiers"]
tags: ["Question","QFormat3"]
---

#### What is a
## Operational amplifier
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

Basically what this means is that the output is proportional to the difference between $V_{+}$ and $V_{-}$ multiplied by the amplification factor but then capped between the supply voltages. Since the amplification factor is often measured in the millions tiny differences in the inputs will usually just resault in a value equivilent to $V_{cc}^{+}-1$ or