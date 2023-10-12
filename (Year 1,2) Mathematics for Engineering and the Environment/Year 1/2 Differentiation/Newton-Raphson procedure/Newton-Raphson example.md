---
aliases: [""]
tags: ["Question","QFormat1"]
---

## Newton-Raphson example
### Problem
Find a root of $8x^4+0.45x^3-4.544x-0.1136=0$ to 4d.p near $x=0.8$

### Method
Using [[Newton-Raphson]] and basic differentiation [[Derivative of simple exponent]]

> taking $f(x) = 8x^4+0.45x^3-4.544x-0.1136$
> $$ \begin{align*}
f(x) &= 8x^4+0.45x^3-4.544x-0.1136\\
\dot{f}(x) &= 32x^3+1.35x^2-4.544\\
x_{n+1} &= x_{n} - \dfrac{f(x_n)}{\dot{f}(x_n)}\\
x_{n+1} &= x_{n} - \dfrac{8x_{n}^4+0.45x_{n}^3-4.544x_{n}-0.1136}{32x_{n}^3+1.35x_{n}^2-4.544}
\end{align*}$$
> now we use $x = 0.8$ in our equation
> $$ \begin{align*}
x_0&=0.8\\
x_1&=0.8190176\\
x_2&=0.8181797\\
x_3&=0.8181780
\end{align*} $$
>> so to 4d.p $x = 0.8182$ 