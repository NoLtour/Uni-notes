---
aliases: ["tail plane AOA","tail plane setting angle","floating tendency","restoring tendency","tail hinge moment equation"]
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

We know that there will be 3 things influencing the lift of the tail:
- The main wings downwash
- The static profile of the tailplane
- The elevators angle
- The trim tabs angle

Since the main wing downwash and static profile of the tail plane are both just linear functions of AOA (in our model) we can combine them into $a_{1} \alpha_{T_{eff}}$, the others we can just give linear models. Then add em up and we get total tail lift:

> ### $$\begin{align*} C_{L_{T}}  &= a_{1} \alpha_{T_{eff}} + a_{2} \eta + a_{3}\beta  \end{align*}$$
> ### $$\begin{align*} a_{1} &= \frac{dC_{L_{T}}}{d\alpha_{T_{eff}}} &  a_{2} &= \frac{dC_{L_{T}}}{d\eta} &  a_{3} &= \frac{dC_{L_{T}}}{d\beta}  \end{align*}$$
>> where:
>> $\alpha_{T_{eff}}=$   effective angle of attack of tailplane
>> $\eta=$ elevator angle
>> $\beta=$ trim tab angle relative to elevator
>> $C_{L_{T}}=$ Lift coefficient of tail
>> $a_{1}=$ Coeffient describing tail lift change with AOA change
>> $a_{2}=$ Coefficient describing tail lift change with elevator change
>> $a_{3}=$ Coefficient descibing tail lift change with trim angle change

### Hinge moment equation

This is the exact same approach as was taken for the tails lift equation, we know moments will be some function of all those angles and turns out a linear model works well enough so we just go with that and add em up:

> ### $$\begin{align*} C_{M_{H}}  &= b_{1} \alpha_{T_{eff}} + b_{2} \eta + b_{3}\beta  \end{align*}$$
> ### $$\begin{align*} b_{1} &= \frac{dC_{M_{H}}}{d\alpha_{T_{eff}}} &  b_{2} &= \frac{dC_{M_{H}}}{d\eta} &  b_{3} &= \frac{dC_{M_{H}}}{d\beta}  \end{align*}$$
>> where:
>> $\alpha_{T_{eff}}=$   effective angle of attack of tailplane
>> $\eta=$ elevator angle
>> $\beta=$ trim tab angle relative to elevator
>> $C_{M_{H}}=$ Hinge moment acting on elevator
>> $b_{1}=$ [[modelling the tailplane|floating tendency]]
>> $b_{2}=$  [[modelling the tailplane|restoring tendency]]
>> $b_{3}=$  change in hinge moment with trim angle
>> ![[Pasted image 20230216103607.png]]

If you imagine the tailplanes motion in the event that the only rigid joint is the trim tab one, then you can see that when you deflect the trim tab the elevator will pivot such that the moments around the elevator hinge become zero:

![[Pasted image 20230216104037.png]]

This is where the names [[modelling the tailplane|restoring tendency]] and [[modelling the tailplane|floating tendency]] come from, they describe the tendency of these systems to move in particular ways:
- [[modelling the tailplane|Floating tendency]], the effect causing the elevator to be deflected by the effects of overall attitude and the main wing.
- [[modelling the tailplane|Restoring tendency]], the effect from the elevator that will cause some equilibrium to be reached.
- $b_{3}$, the pilots input into the trim tab to passively control the elevators angle.

Note that the [[components of a tailplane|horn balance]] actually exists to control [[modelling the tailplane|restoring tendency]].
