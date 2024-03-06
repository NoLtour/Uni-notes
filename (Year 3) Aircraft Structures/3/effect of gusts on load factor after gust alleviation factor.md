---
aliases: ["gust alleviation factor"]
tags: []
---

## Effect of gusts on load factor after gust alleviation factor

The model described in [[effect of gusts on load factor]] is incomplete, it doesn't capture the fact that changes in loads due to gusts are not instantaneous. To fix this we can do what [[mathamaticians can cope and seeth|engineers always do]]: slap a empirical coefficient in there to fix things.

> ### $$\begin{align*} n &= 1 + \frac{1}{2} \rho  F\frac{UV}{W} \left(S\frac{dC_{L}}{d\alpha} +   S_{T} \frac{dC_{LT}}{d\alpha} \right) \end{align*}$$
> ### $$\begin{align*} F &= \frac{0.88\mu_{g}}{5.3+\mu_{g}} &&& \mu_{g} &= \frac{2W}{\rho g \bar{c} S a_{1}}  \end{align*}$$
>> where:
>> $F=$ [[effect of gusts on load factor after gust alleviation factor|gust alleviation factor]]
>> $n=$ [[load factor]]
>> $W=$ Weight
>> $\rho=$ atmospheric density
>> $S=$  main [[Wing plan area]]
>> $S_{T}=$  tail [[Wing plan area]]
>> $C_{L}=$ lift coefficient
>> $C_{LT}=$ tail lift coefficient 
>> $U=$ upward gust velocity
>> $V=$ airspeed
>> $a_{1}=$ [[modelling the tailplane|coefficient relating to tailplane I think]] (it's not specified what this is so I have no idea, just $a_{1}$ in the notes)
 

