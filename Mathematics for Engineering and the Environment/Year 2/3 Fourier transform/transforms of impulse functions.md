---
aliases: ["Laplace transform of heaviside function","heaviside function Laplace transform","second shift theorem"]
tags: []
---

## Transforms of impulse functions
If we take the [[heaviside function]] and the [[dirac theta function]] we can do some [[insanity|funky]] stuff using [[Laplace transform]] to get useful identities.

### Laplace transform of [[heaviside function]]

> ### $$ \mathcal{L}[ H(x-a) ] = \frac{e^{-as}}{s} $$ 
> ### $$\therefore \mathcal{L }^{-1}\left[ \frac{e^{-as}}{s} \right] = H(x-a) $$ 
>> requires:
>> Re$(s)>0$
>
>> where:
>> $\mathcal{L}[..]=$ [[Laplace transform]]
>> $H(...)=$ [[heaviside function]]

### Second shift theorem

This 

> ### $$ \mathcal{L}[ f(x)H(x-a) ] = e^{-as} \mathcal{L}[f(x+a)] $$ 
> ### $$ \mathcal{L}[ f(x-a)H(x-a) ] = e^{-as} \mathcal{L}[f(x)] = e^{-as} \tilde{f}(s) $$ 
>> where:
>> $\mathcal{L}[..]=$ [[Laplace transform]]
>> $H(...)=$ [[heaviside function]]
