---
aliases: [""]
tags: []
---

## [[Integration by parts]] DI method

Essentially it is just this equation:

> ## $$ \int uv \cdot dx = u I_{1}[v] - \dot{u}I_{2}[v] + \ddot{u}I_{3}[v] - \dddot{u}I_{4}[v] + ... + (-1)^{n} \left( \frac{d^{n-1}}{dx^{n-1}} u \right) I_{n}[v] $$ 
>> where:
>> $v,u=$ functions of $x$
>> $I_{n}[v]=$ nth derivative of $v$ with respect to $x$ 

Which is trivial to prove by just subbing the [[Integration by parts]] equation into itself recursively, in implementation it can be done easily in the following manor:


