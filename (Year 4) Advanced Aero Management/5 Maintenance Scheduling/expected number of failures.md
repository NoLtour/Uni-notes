---
aliases: [""]
tags: []
---

## Expected number of failures

This is the expected number of failures of a system that occur in some interval, it serves multiple uses:
- Can be used as a criteria for the acceptable reliability of a part during the design phase
- Can be used for determining maintenance schedule
- Can be used to calculate profitable warranty policy, which would simply be $(\text{Repair cost})\times(\text{Expected number of failures})$

There are multiple ways to calculate it, some are done directly on the input data but we will focus on parametric approaches that make use of our previous work on [[probability density function|PDFs]].

### Equation

This equation is a pain in the ass to solve, and relies on [[Laplace transform]]s for solving. We don't need to be able to apply it for our exam, so just be aware of it. For more details refer to the [[Lecture_15.pdf|management slides]].

> ### $$\begin{align*} \text{Continous approach:}&& M(t)  &=  F(t) + \int^{t}_{0} M(t-x) f(x) \cdot dx \\ \text{Discrete approach:}&& M(t)&= \sum\limits^{T-1}_{i=0} [1 + M(T-i-1)] \int^{i+1}_{i} f(t) \cdot dt \end{align*}$$
> ### $$\begin{align*} M(t)  &=  E[N(t)]  \end{align*}$$
>> where:
>> $M(t)=$ the expected number of failures from $0\to t$
>> $N(t)=$ the actual number of failures from $0\to t$
>> $F(t)=$ [[cumulative distribution function]] of the component
>> $f(t)=$ the [[probability density function|PDF]] of the component
>> $t_{i}=$ the length of the time interval between failure $i-1$ and failure $i$ (time between consecutive failures)
>> $S_{r}=$ the total up time to the $r^{th}$ failure 
>
>![[Pasted image 20241114133135.png|500]]
