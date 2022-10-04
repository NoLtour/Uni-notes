---
aliases: ["resistor impedance"]
tags: ["Question","QFormat3"]
---

#### How do we deal with
## Resistance in AC
### Equation
#### Impedance component
> ### $$ Z_{R} = R + 0j = R $$ 
>> where:
>> $Z_{R}=$ [[resistance in AC|resistor impedance]]
>> $R=$ [[resistance]]
>> Component follows [[Ohms law]]

^40f307

#### Standalone circuit
If you have a circuit where the only components are an AC source and a ohmic resistor:

![[Pasted image 20220428112311.png]]

Then since its impedance is $Z=Z_{R}=R$ it's voltage and current will be in phase which can be seen by subbing into the [[impedance#^bd1cda|equation for impedance]]:
> ### $$ V = I_{p} \cos(\omega t + \phi) R $$ 
>> where:
>> $V=$ potential difference across component
>> $I_{p}=$ peak current
>> $\omega=$ [[AC angular frequency]]
>> $R=$ [[resistance]]
>> $t=$ time
>> $\phi=$ time offset

### Theory
For an ohmic resistor it's behaviour is completely defined using [[Ohms law]]:
![[Ohms law#^cfccff]]

When dealing with resistance current and voltage are in phase:
![[Pasted image 20220428102024.png]]

### Example
![[Pasted image 20220428104729.png]]