---
aliases: [""]
tags: []
---

## [[Integration by parts]] DI method

### As an equation

Essentially it is just this equation:

> ## $$ \int uv \cdot dx = u I_{1}[v] - \dot{u}I_{2}[v] + \ddot{u}I_{3}[v] - \dddot{u}I_{4}[v] + ... + (-1)^{n} \left( \frac{d^{n-1}}{dx^{n-1}} u \right) I_{n}[v] $$ 
>> where:
>> $v,u=$ functions of $x$
>> $I_{n}[v]=$ nth derivative of $v$ with respect to $x$ 

Which is trivial to prove by just subbing the [[Integration by parts]] equation into itself recursively.

### Usage
Lets say we have the equation $\int x^{5} \sin\left(\frac{x}{2}\right) \cdot dx$, then normal by parts would take ages. Instead lets use the DI method, first draw a table with 3 columns:
- First column contains alternating signs $+/-$ starting with $+$
- Second column contains derivatives starting with the term you want to derive recursively, here we pick $x^{5}$
- Third column contains integral starting with the

![[Pasted image 20221109140218.png]]
![[Pasted image 20221109140203.png]]


