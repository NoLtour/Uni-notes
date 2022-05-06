---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is
## Integration by completing the square
### Equation
You should probably do it using the full method for marks in the exam, but for completeness I made it into an eqauation:
> ### $$ \int \frac{1}{ax^{2} + bx +c} \cdot dx = \frac{2}{\sqrt{4ca-b^{2}}} \arctan \left( \frac{2ax+b}{\sqrt{4ca-b^{2}}} \right) $$ 
>> where:
>> $=$ 
>> $=$
>> $=$

### Theory
For some things like $\int \frac{1}{x^{2} + 2x +5} \cdot dx$ you can't solve it conventionally so:

$$\begin{align*}
& \int \frac{1}{x^{2} + 2x +5} \cdot dx\\
& \int \frac{1}{ (x + 1)^{2} +4} \cdot dx\\
& & 2u &= x+1\\
& \int \frac{1}{ (2u)^{2} +2^{2}} \cdot dx & 2du &=  dx\\
& \int \frac{1}{ 2^{2} (u^{2}+1) } 2 \cdot du\\
& \int \frac{1}{2} \frac{1}{ u^{2}+1 } \cdot du\\
&\:\:\:\:\:\: \frac{1}{2} \tan^{-1} \left(u\right) + c \\
&\:\:\:\:\:\: \frac{1}{2} \tan^{-1} \left(\frac{x+1}{2}\right) + c \\
\end{align*}$$
