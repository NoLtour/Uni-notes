---
aliases: [""]
tags: []
---

## Shortcuts for the fourier series

### Intro

![[defining the fourier series#^3f0fc8]]

If we look at the equation that actually defines the [[Fourier Series Overview|Fourier series]] we can tell that:
- $a_{0}$ is responsible for the vertical shift ($a_{0}=0$ means the area above and below the x axis are equal since everything else is constructed from $\sin$ and $\cos$ functions).
- $a_{n}$ creates graphs which are symetric about the y axis (aka purely $\cos$ based functions will be [[even function]]s).
- $b_{n}$ creates graphs which are clearly [[odd function]]s (if made solely out of sin functions).

### Simplifications for [[odd function]]s

Since it's clear for [[odd function]]s there is no $\cos$ we can just take $a_{n}=0$ also $a_{0}=0$, further when finding $b_{m}$ we know that we will be integrating the result of multiplying two [[odd function]]s ($\sin$ and $f(x)$) which according to [[relationships with odd and even functions]] will produce an [[even function]], hence we can apply [[even function]] identities to it.

> ### $$ f(x) = \sum\limits^{\infty}_{n=1}\left[   b_{n} \sin \left(\frac{n\pi}{L} x\right) \right] $$  
> ### $$ b_{m} = \frac{2}{L} \int^{L}_{0} f(x) \sin\left(\frac{n\pi}{L} x\right) \cdot dx $$  
>> where:
>> $f(x)=f(x+2L)=$ a periodic function (it repeats perfectly every $2L$)
>> $a_{0}=0$  
>> $b_{n}=$ the $n$th constant related to $\sin$  
>> $a_{n}=0$
>> $L=$ half the period of the function

### Simplifications for [[even function]]s

Since it's clear for [[even function]]s there is no $\sin$ we can just take $b_{n}=0$ further we know that for an [[even function]] $\int^{A}_{-A} f_{e}(x) \cdot dx = 2 \int^{A}_{0} f_{e}(x) \cdot dx$ this allows further simplification.

> ### $$ f(x) = \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \cos \left( \frac{n\pi}{L} x \right)  \right] $$ 
> ### $$ a_{m} = \frac{2}{L} \int^{L}_{0} f(x) \cos\left(\frac{n\pi}{L} x\right) \cdot dx $$  
> ### $$ a_{0} = \frac{2}{L} \int^{L}_{0} f(x) \cdot dx $$
>> where:
>> $a_{m}=$ often expands to a function defining the $n$th $a$ constant in terms of $m$.
>> $b_{m}=0$
>> $f(x)=f(x+2L)=$ a periodic function (it repeats perfectly every $2L$)
>> $L=$ half the period of the function 

### Further implications

When solving for the identities of $a_{0}$, $a_{n}$ and $b_{n}$ it becomes possible to simplify complex functions by removing components that will clearly solve to zero and not contribute anything to the final solution.

### Example: Tent function

> Find the [[Fourier Series Overview|Fourier series]] for:
> ![[Pasted image 20221011163613.png]]

From the graph we can clearly see that the function is $f(x)=|x|$ in the range $-\pi\leq x \leq \pi$ repeating every $2\pi$. 

Simply by looking at the function it's obvious that this is a [[even function]] hence $b_n=0$, so all that needs to be calculated is $a_{0}$ and $b_{n}$. 


