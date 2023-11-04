---
aliases: ["emittance","emissivity"]
tags: []
---

## Real body emission

Real object's don't behave the same way as [[black and grey bodies|black bodies]] so of course [[black body emission]] equations aren't directly applicable, but like most things in engineering we fix that fact by just shoving a empirical constant in there ([[It is funny how common this is|lol]]).
The constant slapped in there is called emittance.

> ### $$\begin{align*} \varepsilon  &\equiv \frac{q(T)}{q_{BB}(T)}   \end{align*}$$
> ### $$\begin{align*} q(T) &=  \varepsilon \:q_{BB}(T)  \\&=  \varepsilon \sigma T^{4} \end{align*}$$
>> where:
>> $\varepsilon=$ [[real body emission|emittance]], it's the ratio between [[black body emission|total black body emission]] and the actual emission of a material.
>> $q=$ the actual total emission of a material
>> $q_{BB}=$ [[black body emission|total black body emission]]
>> $T=$ temperature of black body
>> $\sigma=$ [[Stefan-Boltzmann constant]]
>
>(btw this is emission per unit area if that wasn't obvious)

