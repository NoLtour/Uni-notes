---
aliases: ["fourier periodic extention","fourier even extention","fourier odd extention"]
tags: []
---

## Defining half range series
### Intro
It's possible to be given a function where you only know it's definition for half the range ($0\leq x < L$) in this situation there are 3 different [[defining the fourier series|fourier series]] representations:
![[Pasted image 20221019144811.png]]

### Case: Periodic extension
In this case we simply use the half range as it's range, aka $0\leq x < L$.

![[Pasted image 20221019150659.png]]

#### Example
> Given the function $g(x)$ over the half range $0\leq x < \pi$ what is it's fourier series (using a periodic extension)

We find the period, which in this case is $\pi$, hence it's half period $L=\frac{\pi}{2}$ so looking at [[defining the fourier series#^918760|these equations]]:
  $$ g(x) = \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \cos \left( 2nx \right) + b_{n} \sin \left(2nx\right) \right] $$ 
 $$ a_{m} = \frac{2}{\pi} \int^{\pi}_{0} g(x) \cos\left(2n x\right) \cdot dx $$ 
 $$ b_{m} = \frac{2}{\pi} \int^{\pi}_{0} g(x) \sin\left(2n x\right) \cdot dx $$ 
 $$ a_{0} = \frac{2}{\pi} \int^{\pi}_{0} g(x) \cdot dx $$

Then it's just the case of solving for the constants.

### Case: Even extension
We take $f_{ext}(x)=f_{orig}(|x|)$ then extend the range to $-L\leq x < L$. Since we're taking the function as an [[even function]] we can use the [[shortcuts for the fourier series]] that apply to even functions ($b_{n}=0$).

![[Pasted image 20221019150710.png]]

#### Example
> Given the function $g(x)$ over the half range $0\leq x < \pi$ what is it's fourier series (using a even extension)

We find the period, which in this case is $2\pi$, hence it's half period $L=\pi$ so looking at [[defining the fourier series#^918760|these equations]] and the [[shortcuts for the fourier series]] since this is an even function:
$$ g(x) = \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ a_{n} \cos \left( \frac{n\pi}{L} x \right)  \right] $$ 
 $$ a_{m} = \frac{2}{L} \int^{L}_{0} g(x) \cos\left(\frac{n\pi}{L} x\right) \cdot dx $$  
 $$ a_{0} = \frac{2}{L} \int^{L}_{0} g(x) \cdot dx $$

Then it's just the case of solving for the constants. [[UNFINISHED STUFF]] I DONT THINK THE $2\times \frac{1}{L}$ IS CORRECT, VERIFY

### Case: Odd extension
Since we're taking the function as an [[odd function]] we can use the [[shortcuts for the fourier series]] that apply to odd functions ($a_{n}=0,a_{0}=0$).

![[Pasted image 20221019155955.png]]

#### Example
> Given the function $g(x)$ over the half range $0\leq x < \pi$ what is it's fourier series (using a odd extension)

We find the period, which in this case is $2\pi$, hence it's half period $L=\pi$ so looking at [[defining the fourier series#^918760|these equations]] and the [[shortcuts for the fourier series]] since this is an odd function:
$$ g(x) = \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}\left[ b_{n} \sin \left( \frac{n\pi}{L} x \right)  \right] $$ 
 $$ b_{m} = \frac{2}{L} \int^{L}_{0}g(x) \sin\left(\frac{n\pi}{L} x\right) \cdot dx $$   

Then it's just the case of solving for the constants.