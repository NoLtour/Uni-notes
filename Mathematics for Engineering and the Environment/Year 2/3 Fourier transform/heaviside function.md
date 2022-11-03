---
aliases: [""]
tags: []
---

## Heaviside function

There are many situations where we need to model the effects of an instantaneous change to some output, also known as impulsive sources (since they have a measureable impact while acting over a negligible period of the independent variable, eg time):
![[Pasted image 20221103090528.png]]
(right it derivative)
Here we can see such an impulsive function, this can be quite useful and is called the [[heaviside function]]. It can be written as: 

> ## $$ H(x) = \begin{dcases}0, &x<0\\1,&x>0 \end{dcases} $$ 
> ## $$ H(x-a) = \begin{dcases}0, &x<a\\1,&x>a \end{dcases} $$ 
>> where:
>> $H(x)=$ [[heaviside function]]
>> $x=$ independent variable

By summing multiple together it becomes possible to define bounds:

> ## $$ H(x-a)\times H(b-x) = \begin{dcases}1, & a<x<b\\0,&else \end{dcases} $$ 
> ## $$ H(x-a) - H(x-b) = \begin{dcases}1, & a<x<b\\0,&else \end{dcases} $$ 
>> where:
>> $H(x)=$ [[heaviside function]]
>> $x=$ independent variable

Of course it is then also possible to toggle functions on/off over a given range by multiplying by ther