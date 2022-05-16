---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is the
## Taylor series
### Method
In mathematics, the Taylor series of a function is an infinite sum of terms that are expressed in terms of the function's derivatives at a single point.

A Taylor Series simply approximates a function around a point. Basically, you take a point, and use the derivative to figure out how much the function would change if you move away from that point. And then use the second derivative to refine your guess on how much it would move. And the third, and so on until you get accurate enough. 

For a given function ( $f(x)$ ) it's [[Taylor series]] can be defined as:

> ### $$ f(x)= \sum\limits_{n=0}^{\infty} \frac{(x-a)^{n}}{n!} f^{(n)}(a)$$
> ### $$or$$
> ### $$ f(x)= f(a) + \frac{ (x-a)}{1!}f^{'}(a) + \frac{(x-a)^{2} }{2!}f^{''}(a)+ \frac{ (x-a)^{3}}{3!}f^{'''}(a)+ \frac{(x-a)^{4}  }{4!}f^{''''}(a)+ ... $$ 
>> where:
>> $f^{(n)}(a)=$ nth derivative of $f(a)$
>> $a=$ A value

an alternative form can be found by replacing x with x+a

> ### $$  f(x+a)= \sum\limits_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!}(x)^{n} $$
> ### $$or$$
> ### $$ f(x+a)= f(a) + \frac{f^{'}(a) }{1!}x + \frac{f^{''}(a) }{2!}x^{2}+ \frac{f^{'''}(a) }{3!}x^{3}+ \frac{f^{''''}(a) }{4!}x^{4} + ... $$ 
>> where:
>> $f^{(n)}(a)=$ nth derivative of $f(a)$
>> $a=$ A value

Here if we use a value of $a$ where $|x+a|<1$ our value of f(x+a) remains quite accurate even if we only define it interms of a few of it's bits

![[Pasted image 20211128124945.png]]

There is a special case of the [[Taylor series]], which is when $a=0$ we call this a [[Maclaurin series]]. This is like 99% of the use of the [[Taylor series]].