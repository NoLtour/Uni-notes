---
aliases: ["stick fixed","stick free"]
tags: []
---

## Stick fixed and stick free flight

### Defs
Well the definitions really ez, so the pilot has a stick (the control rod for the [[components of a tailplane|tailplane elevator]]):
- If he holds the stick in place it is [[stick fixed and stick free flight|stick fixed]] (he manually holds the elevator at a certain deflection)
- If he doesn't hold the stick it is [[stick fixed and stick free flight|stick free]] (the elevator will naturally go to it's equilibrium position)

### Consequences

#### Stick fixed
This can be quite easily described in math terms using the [[modelling the tailplane|tail hinge moment equation]]. [[stick fixed and stick free flight|Stick fixed]], $C_{M_{H}} \neq 0$ because it's equilibrium is being forced by pilot input:

![[Pasted image 20230216105427.png]]

We can also assume that $\beta=0$ because there is no point in the pilot using the trim tab if he is going to manually hold the elevator. Problem is controlling the tail like this is lots of effort on the pilots side so for thing's like cruse generally [[stick fixed and stick free flight|stick free]] is used instead.

### Stick free
In [[stick fixed and stick free flight|Stick free]], $C_{M_{H}}=0$ because the elevator is free to drift to equilibrium:

![[Pasted image 20230216105654.png]]

This will generally be used in cruse because then the pilot doesn't need to actively do shite, generally in these cases $\beta\neq 0$ but that isn't necessarily true. For the stick free case we can use [[modelling the tailplane#Hinge moment equation]] to figure out what's needed to reach this equilibrium.

#### Solving stick free problems

Often in these cases you will need to find $\eta$ given some trim tab angle $\beta$, this can be done using the [[modelling the tailplane#Hinge moment equation]] and the tail lift coefficient [[modelling the tailplane#Lift equation]]:
$$\begin{align*}
C_{M_{H}}  &= b_{1} \alpha_{T_{eff}} + b_{2} \eta + b_{3}\beta & C_{L_{T}}  &= a_{1} \alpha_{T_{eff}} + a_{2} \eta + a_{3}\beta\\&\text{let: }C_{M_{H}}=0\\
  \frac{- b_{3}\beta - b_{1} \alpha_{T_{eff}}}{b_{2}} &=   \eta   \\
  && C_{L_{T}}  &= a_{1} \alpha_{T_{eff}} + a_{2} \frac{ b_{3}\beta + b_{1} \alpha_{T_{eff}}}{-b_{2}} + a_{3}\beta\\
  &&   &= \left(a_{1} - a_{2} \frac{b_{1}}{b_{2}}\right) \alpha_{T_{eff}} + \left( a_{3} - a_{2} \frac{b_{3}}{b_{2}} \right) \beta\\
  &&  &= \bar{a_{1}} \alpha_{T_{eff}} + \bar{a_{3}} \beta
\end{align*}$$

So that's a convenient equation:

> ### $$\begin{align*} \eta&= - \frac{ b_{3}\beta + b_{1} \alpha_{T_{eff}}}{b_{2}}  \end{align*}$$
> ### $$\begin{align*} C_{L_{T}}  &=  \bar{a_{1}} \alpha_{T_{eff}} + \bar{a_{3}} \beta \end{align*}$$
> ### $$\begin{align*}  \bar{a_{1}} &=  a_{1} - a_{2} \frac{b_{1}}{b_{2}} & \bar{a_{3}} &=    a_{3} - a_{2} \frac{b_{3}}{b_{2}}  \end{align*}$$
>> where:
>> $\alpha_{T_{eff}}=$   effective angle of attack of tailplane
>> $\eta=$ elevator angle
>> $\beta=$ trim tab angle relative to elevator
>> $C_{M_{H}}=$ Hinge moment acting on elevator
>> $b_{1}=$ [[modelling the tailplane|floating tendency]]
>> $b_{2}=$  [[modelling the tailplane|restoring tendency]]
>> $b_{3}=$  change in hinge moment with trim angle
>> $C_{L_{T}}=$ Lift coefficient of tail
>> $a_{1}=$ Coeffient describing tail lift change with AOA change
>> $a_{2}=$ Coefficient describing tail lift change with elevator change
>> $a_{3}=$ Coefficient descibing tail lift change with trim angle change


