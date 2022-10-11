---
aliases: [""]
tags: []
---

## Defining the Fourier series
(ngl this sounds [[French|Fr*nch]]. (I looked it up, it is Fr\*nch [[ahhhhhhhhhhhhhhhhh FRENCH|:anguish:]], [[ewwwwwwwwwwwwwww]] ))

###### Note for this page I'm using $2\pi$ for the period

### Definition

> ### $$ f(x) = \frac{1}{2} a_{0} + \sum\limits^{\infty}_{n=1}[ a_{n} \cos ( n x ) + b_{n} \sin (n x) ] $$ 
>> where:
>> $f(x)=$ a periodic function (it repeats perfectly every $2\pi$)
>> $a_{0}=$ a offset constant (offsets the function from an average of 0)
>> $a_{n},b_{n}=$ the $n$th constant related to $\cos$ and $\sin$ respectively

The constants $a_{n},b_{n}$ usually end up being defined as a function of $n$ which when solved allows you to calculate the constants $a_{1},a_{2},a_{3}...$ where the more constants calculated the closer the approximation of the original periodic function $f(x)$.

(CBA to do the proof, just look it up)

#### Finding the constants

> ### $$ a_{m} = \frac{1}{\pi} \int^{\pi}_{-\pi} f(x) \cos(mx) \cdot dx $$ 
> ### $$ b_{m} = \frac{1}{\pi} \int^{\pi}_{-\pi} f(x) \sin(mx) \cdot dx $$ 
> ### $$ a_{0} = \frac{1}{\pi} \int^{\pi}_{-\pi} f(x) \cdot dx $$
>> where:
>> $a_{m}=$ often expands to a function defining the $n$th $a$ constant in terms of $m$.
>> $b_{m}=$ often expands to a function defining the $n$th $b$ constant in terms of $m$.
>> $f(x)=$ a periodic function (it repeats perfectly every $2\pi$)

^918760

### Example
> Find the [[Fourier Series Overview|Fourier series]] for:
> ![[Pasted image 20221011090614.png]]

From the graph we can clearly see that the function is $f(x)=x$ in the range $-\pi\leq x \leq \pi$ repeating every $2\pi$. 

So now we just sub the function into [[defining the fourier series#^918760|these equations]] and solve to get definitions for the constants.

$$\begin{align*}
a_{m} &= \frac{1}{\pi} \int^{\pi}_{-\pi} f(x) \cos(mx) \cdot dx & f(x) = x\\
&= \frac{1}{\pi} \int^{\pi}_{-\pi} x \cos(mx) \cdot dx
\end{align*}$$

Here we have to use the
