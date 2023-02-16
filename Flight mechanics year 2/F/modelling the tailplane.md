---
aliases: ["tail plane AOA","tail plane setting angle"]
tags: []
---

## Modelling the tailplane

### Angle of attack


![[Pasted image 20230215203511.png]]

First note that for a tailplane it's AOA is different to the main wing AOA:

> ### $$\begin{align*} \alpha_{T}  &= \alpha + \alpha_{S}  \end{align*}$$
>> where:
>> $\alpha_{T}=$ tail plane AOA
>> $\alpha=$ AOA
>> $\alpha_{S}=$ tail plane setting angle

But of course there is the effect of the main wings [[downwash for stability analysis|downwash]], here we represent (main wing) downwash angle with $\varepsilon$:
![[Pasted image 20230215204452.png]]

> ### $$\begin{align*} \alpha_{T_{eff}}  &= \alpha_{T} - \varepsilon - \varepsilon_{T}  \end{align*}$$
> ### $$\begin{align*} \alpha_{T_{eff}}  &= (\alpha +  \alpha_{S}) - \varepsilon_{\alpha}(\alpha - \alpha_{0}) - \frac{C_{L_{T}}}{\pi A_{T} e_{T}}  \end{align*}$$
>> where:
>> $\alpha_{T}=$ tail plane AOA
>> $\alpha=$ AOA
>> $\alpha_{S}=$ tail plane setting angle
>> $\alpha_{T_{eff}}=$   effective angle of attack of tailplane
>> $\varepsilon_{T}=$ tailplane induced downwash angle
>> $\varepsilon=$  downwash from main wing on tail
>> $\varepsilon_{\alpha}= \frac{d\varepsilon}{d\alpha}=$ downwash from main wing with AOA
>> $\alpha_{0}=$ zero lift angle main wing
>> $C_{L_{T}}=$ Lift coefficient of tail
>> $A_{T}=$ [[wing aspect ratio|aspect ratio]] of tail
>> $e_{T}=$ [[Oswald efficiency factor]] of tail

### Lift equation

> ### $$\begin{align*} C_{L_{T}}  &= a_{1} \alpha_{T_{eff}} + a_{2} \eta   \end{align*}$$
>> where:
>> $=$ 
>> $=$
>> $=$
