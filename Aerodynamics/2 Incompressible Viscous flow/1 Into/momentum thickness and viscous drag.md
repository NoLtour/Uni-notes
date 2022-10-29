---
aliases: ["calculating viscous drag","calculating skin drag","skin drag"]
tags: []
---

## Momentum thickness and [[skin drag|viscous drag]]

### Relationship

There is a direct relationship between [[skin drag|skin friction]] and [[boundary layer momentum thickness|momentum thickness]] (the proof is effort so you [[appreciate I even give you the equation smh|just]] get the equation):

> ## $$ D'(x) = \int^{x}_{0} \tau dx $$ 
> ## $$ D'(x) = \rho U_{\infty}^{2} \times \theta(x) $$ 
>> where:
>> $D'(x)=$ total [[skin drag|viscous drag]] caused up to that point as a function of $x$
>> $\theta(x)=$ [[boundary layer momentum thickness|momentum thickness]] as a function of $x$
>> $x=$ position on object
>> $\rho=$ density
>> $U_{\infty}=$ [[freestream]] velocity

This means that it is possible to calculate the skin drag of any body given you know the [[boundary layer momentum thickness|momentum thickness]] at the end.

### Calculating drag from wakes

Since we know that [[boundary layer momentum thickness|momentum thickness]] is directly proportional to drag using the identity above, we can easily calculate the skin drag of a object just by knowing the width of it's wake:
![[Pasted image 20221029201701.png]]

This is how we usually measure skin drag in a wind tunnel.
