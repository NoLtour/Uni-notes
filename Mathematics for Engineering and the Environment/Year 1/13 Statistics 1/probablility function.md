---
aliases: [""]
tags: ["Question","QFormat3"]
---

#### What is a
## Probablility function
### Theory
This is some function that returns the probability of the inputted number being selected for some event. This

> ### $$ f_{X}(x) = \begin{cases}u_{X_{1}}(x) & if\: x < k  \\u_{X_{2}}(x) & if\:x > k\end{cases} $$ 
>> where:
>> $f_{X}=$ the [[probablility function]]
>> $u_{X_{i}}=$ a probability function for that case
>
>> Note that the "$x<k$" and  "$x>k$" are just placeholders, these are just where you put conditional statements to show when the case specific functions should be applied.

Probability functions can be integrated over there entire range and the value outputted is equal to the probability that one of it's possible values will be selected, hence for a [[probablility function]] that isn't a sub function for some specific case:

> ### $$ \int^{\infty}_{-\infty} f_{X(x)} dx = 1 $$ 
>> where:
>> $f_{X(x)}=$ [[probablility function]] that isn't a sub function for some specific case of a different [[probablility function]]

### Example
> Find the constant $k$ in the probability function $f_{X}(x) = \begin{cases} kx^{2}e^{x} & if\: x \leq 1  \\0 & otherwise\end{cases}$

$$\begin{align*}
1 &= \int^{1}_{-\infty} kx^{2}e^{x} \cdot dx\\
&= k [ (x^{2} - 2x + 2) e^{x} ]^{1}_{-\infty}\\
&= k \left( (1^{2} - 2(1) + 2)e^{1} - (...) \frac{1}{e^{\infty}} \right)\\
1 &= ke\\
\frac{1}{e} &= k
\end{align*}$$

(Used the [[single-page-integral-table.pdf]])

So the final function becomes $f_{X}(x) = \begin{cases} x^{2}e^{x-1} & if\: x \leq 1  \\0 & otherwise\end{cases}$

