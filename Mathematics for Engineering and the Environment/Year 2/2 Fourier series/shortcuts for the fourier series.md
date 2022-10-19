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

> ### $$ f(x) = \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \cos \left( \frac{n\pi}{L} x \right)  \right] $$ 
> ### $$ a_{m} = \frac{1}{L} \int^{R_{1}}_{R_{2}} f(x) \cos\left(\frac{n\pi}{L} x\right) \cdot dx $$  
> ### $$ a_{0} = \frac{1}{L} \int^{R_{1}}_{R_{2}} f(x) \cdot dx $$
>> where:
>> $a_{m}=$ often expands to a function defining the $n$th $a$ constant in terms of $m$.
>> $b_{m}=0$
>> $f(x)=f(x+2L)=$ a periodic function (it repeats perfectly every $2L$)
>> $L=$ half the period of the function
>> $R_{1},R_{2}=$ a region the functions defined over, often this is just $R_{1}=L$ and $R_{2}=-L$

Hence from this it becomes obvious that:
- If a function is a [[odd function]] then in its [[Fourier Series Overview|fourier series]] $a_{n}=0$ and $a_{0}=0$.
- If a function is a [[even function]] then in its [[Fourier Series Overview|fourier series]] $b_{n}=0$.
- If a function has equal area's above and below the x axis then $a_{0}=0$.

When solving for the identities of $a_{0}$, $a_{n}$ and $b_{n}$ it becomes possible to simplify complex functions by removing components that will clearly solve to zero and not contribute anything to the final solution.

### Example: Tent function

> Find the [[Fourier Series Overview|Fourier series]] for:
> ![[Pasted image 20221011163613.png]]

From the graph we can clearly see that the function is $f(x)=|x|$ in the range $-\pi\leq x \leq \pi$ repeating every $2\pi$. 

Simply by looking at the function it's obvious that this is a [[even function]] hence $b_n=0$, so all that needs to be calculated is $a_{0}$ and $b_{n}$. 


