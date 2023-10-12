---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Discharge coefficient
This is a coefficient that represents the ratio between the actual and theoretical mass flow rate (according to [[Bernouillis equation]]), it can be used to represent frictional losses in pipes:

> ### $$ C_{d} = \frac{T_{e}}{T_{t}} $$ 
>> where:
>> $C_{d}=$ [[discharge coefficient]] 
>> $T_{e}=$ experimental mass flow rate
>> $T_{t}=$ theoretical mass flow rate (no friction)

To apply it in a venturi nozzle:
![[Pasted image 20220518144215.png]]

This can be subbed directly into the [[Bernouillis equation]] if you rearrange it for flow rate:

> ### $$ Q_{e} = C_{d} \sqrt{ 2 \frac{ g(h_{2} - h_{1}) + \frac{1}{\rho} ( P_{2} - P_{1} ) }{ \left(\frac{1}{A_{1}^{2}} - \frac{1}{A_{2}^{2}}\right) } } $$ 
> ### $$\frac{Q_{e}^{2}}{2 C_{d}^{2}} \left( \frac{1}{A_{1}^{2}} - \frac{1}{A_{2}^{2}}\right)  +  g(h_{1} - h_{2})  + \frac{P_{1} - P_{2}}{\rho} =0 $$
>> where:
>> $C_{d}=$ [[discharge coefficient]] 
>> $Q_{e}=$ experimental volumetric flow rate
>> $A=$ cross sectional area
>> $P=$ pressure
>> $\rho=$ fluid density (constant)
>> $h=$ height from some reference
>> $X_{1}=$ variable associated with upstream location (flow source)
>> $X_{2}=$ variable associated with downstream location (point of application of $Q_{e}$)
