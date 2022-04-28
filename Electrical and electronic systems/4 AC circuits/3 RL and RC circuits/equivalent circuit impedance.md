---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### Expalin
## Equivalent circuit impedance
### Intro
Basically just like [[simplifieing simple circuits|Thevinins theorem]] (god I hate that name [[I do not know why I just hate saying it|so much]])

### Meath
#### Parallel
You can prove this quite easily so I'm not going to here, when working with multiple components in parallel you can basically just sum the [[impedance]] of each component in the same way you sum for [[resistors in parallel]]:
> ### $$ Z_{T} = \frac{1}{\sum\limits \frac{1}{Z_{i}}} = \frac{1}{\frac{1}{Z_{1}} + \frac{1}{Z_{2}} + ... + \frac{1}{Z_{n}}} $$ 
>> where:
>> ![[Pasted image 20220428153239.png]]
>> $Z_{T}=$ equivalent [[impedance]]
>> $Z_{i}=$ [[impedance]] of a component in parallel

#### Series
Just like the parallel thing it's equivalent to what you do for [[resistors in series]]:
> ### $$ Z_{T} = \sum\limits Z_{i} = Z_{1} + Z_{2} + ... + Z_{n} $$ 
>> where:
>> ![[Pasted image 20220428153622.png]]
>> $Z_{T}=$ equivalent [[impedance]]
>> $Z_{i}=$ [[impedance]] of a component in series