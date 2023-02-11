---
aliases: ["miners law of cumulative damage"]
tags: []
---

## Miners rule
### Intro
It's obvious that the super clean sinosodial curves are not representatibe of typical loading conditions, unless we're dealing with some sort of really specific rotating motion thing the stress over time will probably be something like:
![[Pasted image 20230211142456.png]]

Considering all the maths we've done so far only applies to single frequency+amplitude cases it would appear all of the maths was useless.... introducing miners rule (the title, and the thing that solves this issue)!

### Thingy

So miners rule is essentially you look at all the stress states that will occur and use the equations derived so far to calculate what fraction of the design life will be lost in that stress occilation. Then you can just keep adding these life fractions and eventially they will sum to 1 at which point the materials broken. Of course practically we don't measure every bit of force on the material then add it to some total (would take 10^5+ calculations lol) instead we'd get estimates for what fraction of the stresses belong to different frequencys, amplitudes and [[mean stress]]' then use that to estimate how many average cycles it takes to reach failure.

I can already soo how much of a massive bitch this will be...

> ### $$\begin{align*} \sum\limits \frac{n_{i}}{N_{i}}  &= F   \end{align*}$$
>> where:
>> $n_{i}=$ the number of cycles experienced for a specific cycle type
>> $N_{i}=$ the [[fatigue life (material fatigue)|fatigue life]] measured for that specific cycle type
>> $F=$ the total fraction of lift experienced, once $F=1$ failure should occur

