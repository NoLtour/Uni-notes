---
aliases: ["RMS for AC power","root mean squared current","root mean squared voltage"]
tags: ["Question","QFormat3"]
---

#### Whats the method for
## Calculating power of an AC circuit
For when you deal with more complex idea's of power refer to [[apparent, reactive and real power]].

### Circuit
I recommend only using this equation for validation, since I don't think it'll give marks in the exam [[UNFINISHED STUFF]] (validate):
![[Pasted image 20220509161618.png]]
> ### $$ P_{mean} = \frac{1}{2} \frac{V_{p}^{2}R_{T}}{R_{T}^{2} + D_{T}^{2}} $$ 
>> where:
>> $Z_{T}= R_{T} + jD_{T}$ 
>> $V_{p}=$ peak voltage
>> $P_{mean}=$ mean [[apparent, reactive and real power|real power]]
>> $V_{in} = V_{p} \cos (\omega t)$

### RMS
> ### $$ V_{rms} = \frac{V_{P}}{\sqrt{2}} $$ 
>> where:
>> $V_{rms}=$ root mean squared voltage 
>> $V_{P}=$ peak voltage


> ### $$ I_{rms} = \frac{I_{P}}{\sqrt{2}} $$ 
>> where:
>> $I_{rms}=$ root mean squared current 
>> $I_{P}=$ peak current

Then mean power will be:
> ### $$ P_{mean} = \frac{1}{T} \int^{T}_{0} P dt $$ 
>> where:
>> $P_{mean}=$ mean power 
>> $P=$ instantanious power
>> $T=$ some arbitrary large time value

If we take a sin AC wave then we can use rms:
> ### $$ P_{mean} = \frac{V_{p}^{2}}{2R} = \frac{V_{rms}^{2}}{R} = I_{rms} V_{rms} $$ 
>> where:
>> $P_{mean}=$ mean power
>> $V_{rms}=$ [[calculating power of an AC circuit|root mean squared voltage]]
>> $I_{rms}=$ [[calculating power of an AC circuit|root mean squared current]]
>> $R=$ resistance
>> $V_{p}=$ peak AC voltage 

### Heres the theory
![[Pasted image 20220218170016.png]]
