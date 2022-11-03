---
aliases: [""]
tags: []
---

## Noteable properties of Laplace transforms

These are just some noteable results that are somewhat useful and don't really fit anywhere.

The following is essentially just "if you have a derivative that is taken for a variable independent of $x$ and $s$ then it can be taken out" which is kinda obvious but should also not be forgotten.

> ## $$ \mathcal{L}\left[ \frac{\delta}{\delta A} f(x) \right] = \frac{\delta}{\delta a} \tilde{f}(s) $$ 
>> where:
>> $\mathcal{L}[...]=$ [[Laplace transform]] function
>> $\tilde{f}(s)=$ [[Laplace transform]] of $f(x)$
>> $s=$ frequency, independent variable of [[Laplace transform]]
>> $f(x)=$ some function of $x$
>> $x=$ independent variable of function being transformed
>> $A=$ some variable independent of $x$ and $s$

Then there is this [[it is not that bad to be fair|eldritch horror]], apparently can be useful for some inversion problems? It's not that confusing but it does look strange.

> ## $$ \mathcal{L} \left[\int^{x}_{0} f(z) \cdot dz \right] = \frac{1}{s} \mathcal{L}[f(x)] = \frac{1}{s}\tilde{f}(s) $$ 
>> where: 
>> $\mathcal{L}[...]=$ [[Laplace transform]] function
>> $\tilde{f}(s)=$ [[Laplace transform]] of $f(x)$
>> $s=$ frequency, independent variable of [[Laplace transform]]
>> $f(x)=$ some function of $x$
>> $x=$ independent variable of function being transformed
>> $z=$ some variable independent of $x$ and $s$
