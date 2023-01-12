---
aliases: ["mean angle of attack","mean no lift angle"]
tags: []
---

## Accounting for wing twist

The use of [[geometric twist]] and [[aerodynamic twist]] was discussed in previous sections ([[wing planform for eliptic lift distrobution#Without using elliptic planform]]) but the actual relationships wheren't defined (that's where this page comes in).

The important part is that the overall effect of twisting on the wings preformance is that $\alpha$ (and things like $\alpha_{L=0}$) get's replaced with mean AOA $\bar{\alpha}$ which is the average along with span using the following:

> ### $$\begin{align*} \bar\alpha  &=  \frac{1}{S} \int^{\frac{b}{2}}_{- \frac{b}{2}} \alpha(y) \: c(y) \: dy \end{align*}$$
> ### $$\begin{align*} \bar\alpha_{L=0}  &=  \frac{1}{S} \int^{\frac{b}{2}}_{- \frac{b}{2}} \alpha_{L=0}(y) \: c(y) \: dy \end{align*}$$
> ### $$ C_{L} = a(\bar\alpha - \bar{\alpha}_{L=0}) $$
>> where:
>> $\alpha=$ [[angle of attack|AOA]] at some point along the span
>> $\bar\alpha=$ mean [[angle of attack|AOA]]
>> $\alpha_{L=0}=$ no lift angle at some point along the span
>> $\bar\alpha_{L=0}=$ mean no lift angle
>> $c=$ chord length at some point along the wing
>> $S=$ [[Wing plan area]]
>> $y=$ position along the wing span
>> $b=$ [[Wing span]]
