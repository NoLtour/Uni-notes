---
aliases: [""]
tags: []
---

## Defining the Fourier series
(ngl this sounds [[French|Fr\*nch]]. (I looked it up, it is Fr\*nch [[ahhhhhhhhhhhhhhhhh FRENCH|:anguish:]], [[ewwwwwwwwwwwwwww]] ))

###### Note for this page I'm using $2\pi$ for the period

### Definition

> ### $$ f(x) = \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}[ a_{n} \cos ( n x ) + b_{n} \sin (n x) ] $$ 
>> where:
>> $f(x)=$ a periodic function (it repeats perfectly every $2\pi$)
>> $a_{0}=$ a offset constant (offsets the function from an average of 0)
>> $a_{n},b_{n}=$ the $n$th constant related to $\cos$ and $\sin$ respectively

The constants $a_{n},b_{n}$ usually end up being defined as a function of $n$ which when solved allows you to calculate the constants $a_{1},a_{2},a_{3}...$ where the more constants calculated the closer the approximation of the original periodic function $f(x)$.

#### Finding the constants

> ### $$ a_{m} = \frac{1}{\pi} \int^{\pi}_{-\pi} f(x) \cos(mx) \cdot dx $$ 
> ### $$ b_{m} = \frac{1}{\pi} \int^{\pi}_{-\pi} f(x) \sin(mx) \cdot dx $$ 
> ### $$ a_{0} = \frac{1}{\pi} \int^{\pi}_{-\pi} f(x) \cdot dx $$
>> where:
>> $a_{m}=$ the $m$th constant related to $\cos$ and $\sin$ respectively, (basically $n$th constant, but changed essentially for convention)
>> $a_{0}=$ a offset constant (offsets the function from an average of 0)
>> $f(x)=$ a periodic function (it repeats perfectly every $2\pi$)
