---
aliases: [""]
tags: []
---

## Dirac theta function

These are similar to [[heaviside function]] except instead of going to zero under certain conditions they go to $\infty$ at one point, mathematicians [[major coping|cope]] hard if you say they equal infinity but since that's basically the case Ima just say skill issue and define them as:

> ## $$ \int^{\infty}_{-\infty} \delta(x-a) K \cdot dx = K $$
> ## $$ \int^{\infty}_{-\infty} \delta(x-a) f(x) \cdot dx = f(a) $$
> ## $$ \int^{A}_{B} \delta(x-a) K \cdot dx = 0 \:\:\:\:\:\text{if }{a>A\text{ or }a<B}   $$
> ## $$ \delta(x-a) \approx \begin{dcases}0, &x\neq a\\ \infty,&x=a \end{dcases} $$ 
>> where:
>> $H(x)=$ [[heaviside function]]
>> $x=$ independent variable

The above can clearly be used for defining impulses.

