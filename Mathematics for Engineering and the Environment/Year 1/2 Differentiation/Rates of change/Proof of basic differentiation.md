---
aliases: ["Differentiation proof"]
---

## Proof of basic differentiation
### Problem
How would you find the gradient of the following graph at a specific point? (Assuming the equation is known)
![[Pasted image 20211012162854.png]]

### Method
![[Pasted image 20211012163059.png]]
If you zoom into the graph at a specific point (here we are focusing on pint $t_1$), it will approach a strait line, so you can approximate the gradient by finding the gradient between $f(t_1)$ and $f(t_1+h)$. Put into an equation this is:
> $$ gradient \approx \dfrac{ f(t_1+h)-f(t_1) }{h} $$ 
>> $t_1$ = any point
>> $h$ = any value where $h>0$

As h approaches 0, the inaccuracy of our value decreasses until the inaccuracy is also 0.

$$ \dot{f}(t) = \lim_{h \rightarrow 0} \dfrac{ f(t_1+h)-f(t_1) }{h} $$

#### Example
![[Proof of basic differentiation example]]