---
aliases: ["Goodman equation"]
tags: []
---

## Mean stress effect

### Idea

Ok so far we've mostly been dealing with relating [[fatigue life (material fatigue)|cycles to failure]] to [[stress range]]/[[strain range]], so clearly you can just put any material through cyclic loading with a huuuuuge stress but as long as the stress range is small everything will be fine right? The answer is clearly no, that is dumb and not how materials work. Mean stress will clearly have some effect (we know that things like [[creep (materials)|creep]] exist as well as [[yield strength|yield]] which occurs regardless of stress range). e

![[Pasted image 20230211122851.png]]

Not going into detail but the effect of mean stress on [[fatigue life (material fatigue)|cycles to failure]] is something like the following:

![[Pasted image 20230211122924.png]]

### Goodman equation

Note that the curve is [[you know something is wrong when you describe fucking maths like this|sexy]], and looks like it can probably be linked to some equally sexy equation... well it can! Introducing the [[mean stress effect|Goodman equation]], (note that he was in fact more of a [[I am a very funny and origional person|neutral man]]):

> ### $$\begin{align*} \sigma_{a}  &= \sigma_{a0} \left( 1 - \frac{\sigma_{m}}{\sigma_{ts}} \right)  \end{align*}$$
>> where:
>> $\sigma_{a}=$ [[stress amplitude]]
>> $\sigma_{m}=$ [[mean stress]]
>> $\sigma_{ts}=$ [[ultimate tensile strength]]
>> $\sigma_{a0}=$ the baseline [[stress amplitude]] for when $\sigma_{m}=0$

In effect this equation is relating [[stress amplitude]] and [[mean stress]] for which a material will experience the same cycles to failure.

The equation itself assumes that [[mean stress]] and [[stress amplitude]] have a linear relationship at some [[fatigue life (material fatigue)|cycles to failure]] which is consistantish with real life. (as with all thing's in materials only ish)