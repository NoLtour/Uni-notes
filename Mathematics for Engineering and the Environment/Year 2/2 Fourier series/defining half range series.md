---
aliases: [""]
tags: []
---

## Defining half range series
### Intro
It's possible to be given a function where you only know it's definition for half the range ($0\leq x < L$) in this situation there are 3 different [[defining the fourier series|fourier series]] representations:
![[Pasted image 20221019144811.png]]

### Case: Periodic extension
In this case we simply use the half range as it's range


#### Example
> Given the function $g(x)$ over the half range $0\leq x < \pi$ what is it's fourier series

We find the period, which in this case is $\pi$, hence it's half period $L=\frac{\pi}{2}$ so looking at [[defining the fourier series#^918760|these equations]]:
  $$ g(x) = \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \cos \left( 2nx \right) + b_{n} \sin \left(2nx\right) \right] $$ 
 $$ a_{m} = \frac{2}{\pi} \int^{\pi}_{0} g(x) \cos\left(2n x\right) \cdot dx $$ 
 $$ b_{m} = \frac{2}{\pi} \int^{\pi}_{0} g(x) \sin\left(2n x\right) \cdot dx $$ 
 $$ a_{0} = \frac{2}{\pi} \int^{\pi}_{0} g(x) \cdot dx $$